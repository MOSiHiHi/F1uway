"""F1-Meta-Framework Core Contracts & Schemas (G01-G32 + 4 Parallel Universe Mechanisms).

Enforces:
1. Strict Pydantic v2 validation (`extra="forbid"`, `frozen=True`).
2. Key-Order Sensitivity for Constrained Decoding (PDA/FSM): `reasoning_chain` and
   `evidence_quote` ALWAYS appear first on LLM-facing structured schemas.
3. Bi-temporal provenance (`valid_at`, `invalid_at`, `superseded_by`) and spatial
   coordinates (`page_no`, `bbox`, `char_span`).
4. AST-Hash Content Addressing (Universe 2: Unison/Nix style).
"""
from __future__ import annotations

from datetime import datetime, timezone
from enum import Enum
from typing import Any, Dict, List, Literal, Optional, Tuple
from uuid import uuid4

import json as _json
import pydantic as _pydantic
from pydantic import BaseModel as _PydanticBaseModel, Field

PYDANTIC_V2 = int(_pydantic.__version__.split(".")[0]) >= 2

if PYDANTIC_V2:
    from pydantic import ConfigDict, field_validator
    class F1BaseModel(_PydanticBaseModel):
        model_config = ConfigDict(extra="forbid", frozen=True)
else:
    from pydantic import Extra, validator as _v1_validator
    def ConfigDict(**kwargs):
        return kwargs
    def field_validator(*fields, **kwargs):
        return _v1_validator(*fields, allow_reuse=True)
    class F1BaseModel(_PydanticBaseModel):
        class Config:
            extra = Extra.forbid
            allow_mutation = False
            frozen = True
        def model_dump(self, **kwargs):
            return self.dict(**kwargs)
        def model_dump_json(self, **kwargs):
            return _json.dumps(self.dict(**kwargs), ensure_ascii=False)
        def model_copy(self, update=None, deep=False):
            return self.copy(update=update, deep=deep)
        @classmethod
        def model_validate(cls, obj):
            return cls.parse_obj(obj)
        @classmethod
        def model_validate_json(cls, raw_json: str):
            return cls.parse_raw(raw_json)


CONTRACT_VERSION = "1.0.0"


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


class DevelopmentTrack(str, Enum):
    """8-Mode Development Spectrum (ADR-0002 / G01)."""
    H0_OFFLINE = "H0"          # Human Offline (Zero AI / Zero Internet)
    H1_WEB_DOCS = "H1"         # Human + Web Docs
    H2_SOCRATIC_TUTOR = "H2"   # Human + Socratic AI Tutor (--tutor)
    H3_AI_REVIEWER = "H3"      # Human Codes + AI Reviewer (--review)
    C1_CHATBOT_PACK = "C1"     # Web Chatbot Pack & Apply
    A1_PAIR_AGENT = "A1"       # Interactive Pair Coding Agent
    A2_AUTONOMOUS = "A2"       # Autonomous Agent Execution
    MIX_HYBRID = "MIX"         # Task-boundary track switching


class LearningValue(str, Enum):
    """Cognitive Routing Classifier (G17)."""
    HIGH = "HIGH"              # Core math/algorithms -> Route to H0-H2
    MEDIUM = "MEDIUM"          # Standard domain modules -> Route to H3/A1
    BOILERPLATE = "BOILERPLATE"# Wiring/config/CRUD -> Route to C1/A2


class ActorRole(str, Enum):
    """Unified Actor Taxonomy in ThreadBox DAG (G05)."""
    HUMAN = "human"
    AI_TUTOR = "ai_tutor"
    AI_ARCHITECT = "ai_architect"
    AI_WORKER = "ai_worker"
    MACHINE_TOOL = "machine_tool"  # pytest, ruff, tach, devloop gate


class SpeechAct(str, Enum):
    """Visual & Semantic Speech Act Tag on every TurnNode (G07)."""
    QUESTION = "question"          # ❓ پرسش یا ابهام
    HYPOTHESIS = "hypothesis"      # 💡 فرضیه یا ایده
    PROPOSAL = "proposal"          # 🛠️ پیشنهاد کد یا معماری
    CRITIQUE = "critique"          # 🛡️ نقد یا رد پیش‌فرض (ضدچاپلوسی)
    VERIFICATION = "verification"  # ✅ خروجی تست ماشین یا گیت
    SYNTHESIS = "synthesis"        # 📌 جمع‌بندی و تثبیت دانش


class EdgeConfidence(str, Enum):
    """Epistemic confidence labels (Graphify / G25)."""
    EXTRACTED = "EXTRACTED"
    INFERRED = "INFERRED"
    AMBIGUOUS = "AMBIGUOUS"


class SpatialProvenance(F1BaseModel):
    """Exact source coordinates for F1uxus document grounding (G23, G26)."""
    source_id: str = Field(description="Path or URI of immutable source document")
    page_no: int = Field(ge=1, description="1-indexed page number")
    bbox: Optional[Tuple[float, float, float, float]] = Field(
        default=None, description="(left, top, right, bottom) bounding box"
    )
    char_span: Optional[Tuple[int, int]] = Field(
        default=None, description="(start_char, end_char) in original un-normalized text"
    )
    content_sha256: Optional[str] = None


class ActorStamp(F1BaseModel):
    """Identifies who emitted a TurnNode and under which spectrum track."""
    role: ActorRole
    actor_id: str = Field(min_length=1)
    track_mode: DevelopmentTrack = DevelopmentTrack.H2_SOCRATIC_TUTOR


class SpawnAnchor(F1BaseModel):
    """Pinpoints the exact parent message and text/code span where a Thread branched (G06)."""
    parent_thread_id: str
    parent_turn_id: str
    quoted_span: str = Field(min_length=1, description="Exact token/phrase branched from")
    char_range: Optional[Tuple[int, int]] = None
    ontology_concept_id: Optional[str] = Field(
        default=None, description="Canonical ONT_* ID if interned in Ontology Registry"
    )


class TurnNode(F1BaseModel):
    """Atomic node inside a ThreadBox container (G05, G06, G07, G08)."""
    record_type: Literal["turn_node"] = "turn_node"
    turn_id: str = Field(default_factory=lambda: f"turn_{uuid4().hex[:8]}")
    thread_id: str
    reply_to_turn_id: Optional[str] = None
    timestamp: str = Field(default_factory=utc_now_iso)
    actor: ActorStamp
    speech_act: SpeechAct
    topic_pill_fa: str = Field(
        min_length=2,
        max_length=80,
        description="3-5 word scannable badge shown on top of the node/edge"
    )
    content_md: str = Field(min_length=1)
    code_refs: List[str] = Field(default_factory=list, description="e.g. ['src/core/models.py:L10-L25']")
    ontology_refs: List[str] = Field(default_factory=list, description="e.g. ['ONT_PYDANTIC_FROZEN']")
    spawned_thread_ids: List[str] = Field(default_factory=list)
    token_cost: int = Field(default=0, ge=0, description="0 if served from Ontology Cache")


class ThreadBox(F1BaseModel):
    """Rectangular container of TurnNodes that can branch from any TurnNode (G05-G09)."""
    record_type: Literal["thread_box"] = "thread_box"
    thread_id: str = Field(default_factory=lambda: f"thr_{uuid4().hex[:8]}")
    task_id: str
    title_fa: str = Field(min_length=2, max_length=120)
    intent_type: Literal["main_task", "side_question", "what_if_fork", "bug_triage"] = "main_task"
    spawned_from: Optional[SpawnAnchor] = None
    status: Literal["active", "resolved", "merged", "abandoned"] = "active"
    created_at: str = Field(default_factory=utc_now_iso)
    resolved_at: Optional[str] = None
    resolution_summary_fa: Optional[str] = None
    promoted_ontology_id: Optional[str] = Field(
        default=None, description="If resolved into a reusable concept, stores ONT_* ID"
    )
    linked_artifacts: List[str] = Field(default_factory=list)


class OntologyOccurrence(F1BaseModel):
    """Records where an interned concept/symbol was encountered across texts/projects (G10-G12)."""
    source_ref: str
    thread_id: Optional[str] = None
    turn_id: Optional[str] = None
    surface_form: str
    recorded_at: str = Field(default_factory=utc_now_iso)


class OntologyConceptNode(F1BaseModel):
    """Canonical Entity in the Ontology Registry for Zero-Token Deduplication (G10-G12).
    
    Incorporates Universe 2 (Unison/Nix AST-Hash & SimHash Content Addressing) and
    Bi-temporality (`valid_at`, `invalid_at`).
    """
    concept_id: str = Field( min_length=5)
    canonical_name_en: str
    title_fa: str
    entity_type: Literal["PERSON", "ORG", "LOCATION", "CONCEPT", "EVENT", "TECH", "PRODUCT", "CODE_SYMBOL"]
    normalized_key: str = Field(description="Lemmatized/normalized lookup key")
    aliases: List[str] = Field(default_factory=list)
    simhash_64: str = Field(description="64-bit locality-sensitive hash for fast near-duplicate check")
    ast_structural_hash: Optional[str] = Field(
        default=None, description="SHA-256 of normalized AST if this node represents a code symbol"
    )
    canonical_definition_fa: str = Field(
        min_length=5, description="Shared single-source-of-truth definition (bilingual anchored)"
    )
    canonical_summary_2line: str = Field(
        min_length=5, description="Compact 2-line summary injected in Delta-Mode prompts"
    )
    wikidata_qid: Optional[str] = None
    valid_at: str = Field(default_factory=utc_now_iso)
    invalid_at: Optional[str] = None
    superseded_by: Optional[str] = None
    occurrences: List[OntologyOccurrence] = Field(default_factory=list)
    saved_tokens_count: int = Field(default=0, ge=0)


class MisconceptionEntry(F1BaseModel):
    """Tracks a specific learner misconception diagnosed via Anti-Sycophancy Tutor (G19, G25)."""
    misconception_id: str
    description_fa: str
    detected_in_turn_id: str
    resolved: bool = False


class CompetenceRecord(F1BaseModel):
    """Solves LearnHarness Issue #115 by binding BKT + FSRS-6 mastery directly to AST symbols & Ontology nodes (G19, G20)."""
    competence_id: str
    symbol_or_concept_ref: str = Field(description="e.g. 'src/f1uway/contracts.py::TurnNode' or 'ONT_PYDANTIC_FROZEN'")
    bkt_p_known: float = Field(ge=0.0, le=1.0, default=0.15, description="Bayesian Knowledge Tracing P(L_t)")
    fsrs_stability: float = Field(gt=0.0, default=1.0, description="FSRS-6 memory stability S (days)")
    fsrs_difficulty: float = Field(ge=1.0, le=10.0, default=5.0, description="FSRS-6 item difficulty D")
    interval_days: int = Field(ge=0, default=1)
    next_review_utc: str = Field(default_factory=utc_now_iso)
    attempts_count: int = Field(ge=0, default=0)
    misconceptions: List[MisconceptionEntry] = Field(default_factory=list)


class ConstrainedLLMResponse(F1BaseModel):
    """Strict Schema for LLM Responses enforcing Key-Order Sensitivity & Anti-Sycophancy (G25).
    
    CRITICAL: `reasoning_chain` and `evidence_quote` MUST be the first two fields
    so Pushdown Automaton (PDA) constrained decoding populates reasoning before verdict.
    """
    reasoning_chain: str = Field(
        min_length=10,
        description="Step-by-step independent derivation with English technical anchors in parentheses BEFORE any verdict"
    )
    evidence_quote: str = Field(
        min_length=1,
        description="Verbatim quote or AST/Golden-Value reference supporting the reasoning"
    )
    independent_calculation_result: Optional[str] = Field(
        default=None,
        description="Result of independent symbolic/math verification prior to comparing with user premise"
    )
    detected_user_premise_error: Optional[str] = Field(
        default=None,
        description="If user prompt contained a flawed assumption, state the exact correction without sycophancy"
    )
    speech_act: SpeechAct = SpeechAct.SYNTHESIS
    topic_pill_fa: str = Field(min_length=2, max_length=80)
    final_answer_md: str = Field(min_length=5)
    extracted_concepts: List[str] = Field(default_factory=list)

    @field_validator("final_answer_md")
    @classmethod
    def forbid_sycophantic_opening(cls, v: str) -> str:
        stripped = v.strip()
        forbidden_starts = ("بله، کاملاً درست", "حق با شماست", "You are completely right", "Certainly!")
        for prefix in forbidden_starts:
            if stripped.startswith(prefix):
                raise ValueError(
                    f"Anti-Sycophancy Gate triggered: response cannot open with '{prefix}'. "
                    "Lead directly with the grounded finding."
                )
        return v
