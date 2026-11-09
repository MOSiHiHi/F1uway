"""Comprehensive Unit & Golden-Value Tests for F1-Meta-Framework (`tests/test_f1_core.py`)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))
import unittest
import tempfile
from pydantic import ValidationError

from f1_core import (
    ActorRole,
    CompetenceRecord,
    ConstrainedLLMResponse,
    OntologyRegistry,
    SpeechAct,
    ThreadDAGManager,
    assess_symbol_competence,
    compute_python_ast_hash,
    normalize_persian_with_offsets,
    slice_zoned_markdown_for_ai,
    sync_two_way_code_embeds,
    update_bkt_mastery,
    update_fsrs6_memory,
)


class TestF1Core(unittest.TestCase):
    def test_persian_bidi_offset_preservation(self):
        """Verifies ADR-003 / G26: Arabic Yeh/Kaf & ZWNJ normalization preserves exact raw char_span."""
        raw = "سلام بر كتاب‌های علمی"
        res = normalize_persian_with_offsets(raw)
        assert "کتاب های" in res.normalized_text
        idx = res.normalized_text.index("کتاب های")
        raw_start, raw_end = res.map_norm_span_to_raw(idx, idx + len("کتاب های"))
        assert raw[raw_start:raw_end] == "كتاب‌های"


    def test_unison_style_ast_structural_hash_invariance(self):
        """Verifies Universe 2 mechanism: formatting and docstring changes do not alter AST hash."""
        code_v1 = """
    def calc(x: int, y: int) -> int:
        \"\"\"Docstring v1.\"\"\"
        return x + y
    """
        code_v2 = """
    # Extra comment
    def calc(
        x: int,
        y: int,
    ) -> int:
        \"\"\"Modified docstring v2 with Persian text.\"\"\"
        return x + y
    """
        assert compute_python_ast_hash(code_v1, "calc") == compute_python_ast_hash(code_v2, "calc")


    def test_zero_token_ontology_interning_and_delta_mode(self):
        tmp_path = Path(tempfile.mkdtemp())
        """Verifies G10, G11, G12: 1st spawn interns; 2nd identical spawn hits 0-token cache; sub-question triggers Delta mode."""
        ont = OntologyRegistry(tmp_path)
        # 1. Miss before interning
        miss = ont.intercept_branch_spawn("extra='forbid'", source_ref="doc1.md")
        assert miss.status == "NEW_CONCEPT_MISS"

        # 2. Intern concept
        node = ont.intern_new_concept(
            canonical_name_en="Pydantic Extra Forbid",
            title_fa="قفل اسکیمای پایدنتیک",
            entity_type="CODE_SYMBOL",
            canonical_definition_fa="تعریف کامل قفل اسکیمای Pydantic v2.",
            canonical_summary_2line="منع فیلدهای اضافی و تغییرناپذیری شیء.",
            aliases=["extra='forbid'", "extra=forbid", "قفل اسکیما"],
            source_ref="doc1.md",
        )
        assert node.concept_id == "ONT_PYDANTIC_EXTRA_FORBID"

        # 3. Second encounter in another document -> ZERO_TOKEN_HIT!
        hit = ont.intercept_branch_spawn("extra=forbid", source_ref="doc2.md")
        assert hit.status == "ZERO_TOKEN_HIT"
        assert hit.estimated_tokens_saved == 450
        assert hit.concept is not None and hit.concept.saved_tokens_count == 450

        # 4. Encounter with a new sub-question -> DELTA_PROMPT_MODE!
        delta = ont.intercept_branch_spawn(
            "قفل اسکیما",
            source_ref="doc3.md",
            sub_question="در کلاس‌های فرزند چطور به ارث می‌رسد؟",
        )
        assert delta.status == "DELTA_PROMPT_MODE"
        assert delta.delta_prompt_payload is not None
        assert "ONT_PYDANTIC_EXTRA_FORBID" in delta.delta_prompt_payload
        assert delta.concept is not None and delta.concept.saved_tokens_count == 800


    def test_branchable_thread_dag_and_context_isolation(self):
        tmp_path = Path(tempfile.mkdtemp())
        """Verifies G05-G09: ThreadBoxes branch from specific TurnNodes and isolate context."""
        ont = OntologyRegistry(tmp_path)
        ont.intern_new_concept(
            canonical_name_en="FSRS Stability",
            title_fa="پایداری حافظه در FSRS-6",
            entity_type="CONCEPT",
            canonical_definition_fa="مدت زمانی که احتمال یادآوری از ۱۰۰٪ به ۹۰٪ می‌رسد.",
            canonical_summary_2line="پایداری حافظه (S): زمان رسیدن احتمال بازیابی به ۹۰٪.",
            aliases=["FSRS-6", "پایداری حافظه"],
        )
        dag = ThreadDAGManager(tmp_path, ontology=ont)
        root = dag.create_root_thread("T1.1", "رشته اصلی")
        t1 = dag.add_turn(
            task_id="T1.1",
            thread_id=root.thread_id,
            role=ActorRole.HUMAN,
            actor_id="user",
            speech_act=SpeechAct.QUESTION,
            topic_pill_fa="فرمول FSRS-6",
            content_md="چطور فرمول FSRS-6 را پیاده کنیم؟",
        )
        # Branch on cached span "FSRS-6" -> Auto-resolves with 0 tokens!
        child_box, lookup = dag.spawn_branch_thread(
            task_id="T1.1",
            parent_thread_id=root.thread_id,
            parent_turn_id=t1.turn_id,
            quoted_span="FSRS-6",
            title_fa="انشعاب روی FSRS-6",
        )
        assert lookup.status == "ZERO_TOKEN_HIT"
        assert child_box.status == "resolved"
        branch_msgs = dag.get_branch_context_messages("T1.1", child_box.thread_id)
        assert len(branch_msgs) == 2  # ancestor t1 + auto-synthesized 0-token turn


    def test_bkt_and_fsrs6_golden_values(self):
        """Verifies Golden Values from ARCHITECTURE.md (G19, G20)."""
        assert update_bkt_mastery(0.40, is_correct=True, p_transit=0.15, p_slip=0.10, p_guess=0.20) == 0.7875
        new_s, new_d, ivl = update_fsrs6_memory(stability=2.5, difficulty=5.0, grade=4, elapsed_days=2.5)
        assert new_s > 2.5
        assert new_d < 5.0
        assert ivl >= 3


    def test_anti_sycophancy_and_strict_schema_gate(self):
        """Verifies G25: Rejects extra fields and sycophantic openings."""
        with self.assertRaises(ValidationError):
            ConstrainedLLMResponse(
                reasoning_chain="Step 1: check math independently.",
                evidence_quote="x = 2",
                topic_pill_fa="تست",
                final_answer_md="بله، کاملاً درست است که ۲+۲=۵ می‌شود!",
            )


    def test_zoned_markdown_slicing_and_two_way_embed(self):
        """Verifies G14 & Universe 1/4: Two-way code embed and zone slicing."""
        repo_root = Path(__file__).resolve().parent.parent
        pb = repo_root / "docs" / "human" / "playbooks" / "T1.1.fa.md"
        cnt, _ = sync_two_way_code_embeds(pb, repo_root)
        assert cnt >= 1
        sliced = slice_zoned_markdown_for_ai(pb, allowed_zones=("CONTRACT", "GOLDEN_VALUES"))
        assert sliced.sliced_line_count < sliced.full_line_count
        assert "ZONE:HUMAN_INTUITION" not in sliced.sliced_zones_text

    def test_mjnexus_owner_only_curation_lock(self):
        """Verifies MJNexus owner_only principle: AI cannot overwrite owner_ring or owner_notes_fa."""
        from f1_core import RadarResourceNode, ResourceType, RadarCategory, RadarRing, OwnerCurationLockError, update_radar_resource_safely
        node = RadarResourceNode(
            resource_id="resource:gh:tt-a1i/archify",
            name="Archify",
            resource_type=ResourceType.REPO,
            category=RadarCategory.CODING_AGENTS,
            what_fa="تبدیل کدبیس به دیاگرام‌های تعاملی Explainer.",
            use_fa="مستندسازی معماری در اسکیل phase0-omni-audit.",
            owner_ring=RadarRing.ADOPT,
            owner_notes_fa="ابزار اصلی تصویرسازی ما",
        )
        with self.assertRaises(OwnerCurationLockError):
            update_radar_resource_safely(node, {"owner_ring": RadarRing.HOLD}, actor="ai_agent")
        updated = update_radar_resource_safely(node, {"owner_ring": RadarRing.TRIAL}, actor="owner")
        assert updated.owner_ring == RadarRing.TRIAL

if __name__ == "__main__":
    unittest.main()
