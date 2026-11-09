"""Ontology-Backed Symbolic Interning & Zero-Token Branch Deduplication Engine (G10, G11, G12).

Implements the 4-Stage Spawn Interceptor:
1. Normalize & Lemmatize span X (`Hazm`/Persian + English + AST Symbol normalization).
2. Check Ontology Registry + SQLite Shadow Index (Universe 3):
   - Exact key/alias match OR similarity >= 0.92 -> **ZERO_TOKEN_HIT** (0 API tokens, mounts existing definition).
   - Similarity in [0.75, 0.92) OR user asks a new sub-angle on an existing concept -> **DELTA_PROMPT_MODE**
     (sends only the 2-line canonical summary + delta question, saving ~85% tokens).
   - No match (< 0.75) -> **NEW_CONCEPT_MISS** (creates a new canonical `ONT_*` node upon resolution).
3. Maintains a Single Point of Definition (`notebook/ontology/ONT_*.md`) and updates occurrence backlinks.
"""
from __future__ import annotations

import json
import re
import sqlite3
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Literal, Optional

from .contracts import OntologyConceptNode, OntologyOccurrence, utc_now_iso
from .text_bidi import (
    canonical_lemmatize_key,
    char_ngram_cosine_similarity,
    compute_simhash_64,
)


@dataclass(frozen=True)
class InterningLookupResult:
    """Result returned by the Spawn Interceptor before any LLM API call is made."""
    status: Literal["ZERO_TOKEN_HIT", "DELTA_PROMPT_MODE", "NEW_CONCEPT_MISS"]
    concept: Optional[OntologyConceptNode]
    similarity_score: float
    estimated_tokens_saved: int
    delta_prompt_payload: Optional[str]
    transclusion_tag: Optional[str]


class OntologyRegistry:
    """Manages canonical Ontology Concept Nodes on disk (Markdown + JSON) & SQLite Shadow Index."""

    def __init__(self, repo_root: Path):
        self.repo_root = repo_root
        self.ontology_dir = repo_root / "notebook" / "ontology"
        self.ontology_dir.mkdir(parents=True, exist_ok=True)
        self.db_path = repo_root / ".omni-audit" / "shadow_index.sqlite"
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self._init_sqlite_shadow_index()

    def _init_sqlite_shadow_index(self) -> None:
        """Universe 3 (Datomic/DuckDB/SQLite Shadow Index): Rebuilds or syncs fast lookup tables."""
        with sqlite3.connect(self.db_path) as conn:
            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS ontology_nodes (
                    concept_id TEXT PRIMARY KEY,
                    normalized_key TEXT NOT NULL,
                    canonical_name_en TEXT NOT NULL,
                    title_fa TEXT NOT NULL,
                    entity_type TEXT NOT NULL,
                    simhash_64 TEXT NOT NULL,
                    ast_structural_hash TEXT,
                    saved_tokens_count INTEGER DEFAULT 0,
                    json_payload TEXT NOT NULL
                )
                """
            )
            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS ontology_aliases (
                    alias_norm_key TEXT NOT NULL,
                    concept_id TEXT NOT NULL,
                    PRIMARY KEY (alias_norm_key, concept_id)
                )
                """
            )
            conn.commit()

    def _concept_md_path(self, concept_id: str) -> Path:
        return self.ontology_dir / f"{concept_id}.md"

    def save_concept(self, node: OntologyConceptNode) -> Path:
        """Writes the canonical Markdown file (Source of Truth) and updates SQLite Shadow Index."""
        md_path = self._concept_md_path(node.concept_id)
        aliases_yaml = json.dumps(node.aliases, ensure_ascii=False)
        occ_lines = [
            f"- `{occ.source_ref}` (Thread: `{occ.thread_id or 'N/A'}`, عبارت: «{occ.surface_form}» — `{occ.recorded_at}`)"
            for occ in node.occurrences
        ] or ["- هنوز ارجاعی ثبت نشده است."]

        md_content = f"""---
concept_id: "{node.concept_id}"
canonical_name_en: "{node.canonical_name_en}"
title_fa: "{node.title_fa}"
entity_type: "{node.entity_type}"
normalized_key: "{node.normalized_key}"
aliases: {aliases_yaml}
simhash_64: "{node.simhash_64}"
ast_structural_hash: {json.dumps(node.ast_structural_hash)}
wikidata_qid: {json.dumps(node.wikidata_qid)}
valid_at: "{node.valid_at}"
invalid_at: {json.dumps(node.invalid_at)}
saved_tokens_count: {node.saved_tokens_count}
---

# 🧠 گره هستی‌شناسی: {node.title_fa} (`{node.canonical_name_en}`)

<!-- ZONE:SUMMARY_START -->
> 📌 **چکیده ۲ خطی (مخصوص تزریق Delta-Prompt و Transclusion):**
> {node.canonical_summary_2line}
<!-- ZONE:SUMMARY_END -->

<!-- ZONE:DEFINITION_START -->
## تعریف مشترک و کانونیکال (Single Point of Definition)
{node.canonical_definition_fa}
<!-- ZONE:DEFINITION_END -->

## مترادف‌ها و کلیدهای یکتاسازی (Aliases)
- **کلید نرمال‌شده:** `{node.normalized_key}`
- **مترادف‌ها:** {", ".join(f"`{a}`" for a in node.aliases) if node.aliases else "—"}
- **صرفه‌جویی تجمعی توکن تا این لحظه:** `{node.saved_tokens_count}` توکن

## ردپای وقوع در متون و مستطیل‌های چت (Provenance Backlinks)
{chr(10).join(occ_lines)}

<!-- JSON_STATE: {node.model_dump_json()} -->
"""
        md_path.write_text(md_content, encoding="utf-8")

        with sqlite3.connect(self.db_path) as conn:
            conn.execute(
                """
                INSERT OR REPLACE INTO ontology_nodes
                (concept_id, normalized_key, canonical_name_en, title_fa, entity_type,
                 simhash_64, ast_structural_hash, saved_tokens_count, json_payload)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    node.concept_id,
                    node.normalized_key,
                    node.canonical_name_en,
                    node.title_fa,
                    node.entity_type,
                    node.simhash_64,
                    node.ast_structural_hash,
                    node.saved_tokens_count,
                    node.model_dump_json(),
                ),
            )
            all_keys = {node.normalized_key, canonical_lemmatize_key(node.canonical_name_en), canonical_lemmatize_key(node.title_fa)}
            for alias in node.aliases:
                all_keys.add(canonical_lemmatize_key(alias))
            for k in all_keys:
                conn.execute(
                    "INSERT OR REPLACE INTO ontology_aliases (alias_norm_key, concept_id) VALUES (?, ?)",
                    (k, node.concept_id),
                )
            conn.commit()
        return md_path

    def list_all_concepts(self) -> List[OntologyConceptNode]:
        with sqlite3.connect(self.db_path) as conn:
            rows = conn.execute("SELECT json_payload FROM ontology_nodes ORDER BY concept_id ASC").fetchall()
        return [OntologyConceptNode.model_validate_json(r[0]) for r in rows]

    def intercept_branch_spawn(
        self,
        span_text: str,
        source_ref: str,
        sub_question: Optional[str] = None,
        thread_id: Optional[str] = None,
        turn_id: Optional[str] = None,
        ast_hash: Optional[str] = None,
    ) -> InterningLookupResult:
        """Intercepts a user/agent attempt to branch on `span_text` BEFORE calling any LLM API.

        - If exact alias/AST-hash match or similarity >= 0.92 and no new sub_question:
          returns ZERO_TOKEN_HIT (0 API tokens used, increments saved_tokens_count by ~450).
        - If matched concept exists and user has a new `sub_question` (or similarity in [0.75, 0.92)):
          returns DELTA_PROMPT_MODE (sends only the 2-line summary + sub_question, saving ~350 tokens).
        - Otherwise: returns NEW_CONCEPT_MISS.
        """
        norm_key = canonical_lemmatize_key(span_text)
        matched_node: Optional[OntologyConceptNode] = None
        best_sim = 0.0

        with sqlite3.connect(self.db_path) as conn:
            # 1. Check AST structural hash first (Universe 2: Unison content-addressing)
            if ast_hash:
                row = conn.execute(
                    "SELECT json_payload FROM ontology_nodes WHERE ast_structural_hash = ?",
                    (ast_hash,),
                ).fetchone()
                if row:
                    matched_node = OntologyConceptNode.model_validate_json(row[0])
                    best_sim = 1.0

            # 2. Check exact normalized alias table
            if matched_node is None:
                alias_row = conn.execute(
                    """
                    SELECT n.json_payload FROM ontology_aliases a
                    JOIN ontology_nodes n ON n.concept_id = a.concept_id
                    WHERE a.alias_norm_key = ?
                    """,
                    (norm_key,),
                ).fetchone()
                if alias_row:
                    matched_node = OntologyConceptNode.model_validate_json(alias_row[0])
                    best_sim = 1.0

        # 3. Fallback to local similarity scan across registered concepts
        if matched_node is None:
            for candidate in self.list_all_concepts():
                candidate_texts = [candidate.canonical_name_en, candidate.title_fa] + candidate.aliases
                for ct in candidate_texts:
                    sim = char_ngram_cosine_similarity(span_text, ct)
                    if sim > best_sim:
                        best_sim = sim
                        matched_node = candidate

        if matched_node is not None and best_sim >= 0.75:
            # Record occurrence & token savings
            is_zero_token = (best_sim >= 0.92) and not sub_question
            saved = 450 if is_zero_token else 350
            new_occ = OntologyOccurrence(
                source_ref=source_ref,
                thread_id=thread_id,
                turn_id=turn_id,
                surface_form=span_text,
            )
            updated_node = matched_node.model_copy(
                update={
                    "occurrences": matched_node.occurrences + [new_occ],
                    "saved_tokens_count": matched_node.saved_tokens_count + saved,
                }
            )
            self.save_concept(updated_node)

            if is_zero_token:
                return InterningLookupResult(
                    status="ZERO_TOKEN_HIT",
                    concept=updated_node,
                    similarity_score=best_sim,
                    estimated_tokens_saved=saved,
                    delta_prompt_payload=None,
                    transclusion_tag=f"![[{updated_node.concept_id}#ZONE:SUMMARY]]",
                )

            delta_prompt = (
                f"[ONTOLOGY_CACHE_ANCHOR id={updated_node.concept_id}]\n"
                f"Known Baseline ({updated_node.canonical_name_en}): {updated_node.canonical_summary_2line}\n"
                f"Instruction: Do NOT repeat the baseline definition. Answer ONLY the delta question below:\n"
                f"Delta Question on '{span_text}': {sub_question or 'Explain contextual difference in ' + source_ref}"
            )
            return InterningLookupResult(
                status="DELTA_PROMPT_MODE",
                concept=updated_node,
                similarity_score=best_sim,
                estimated_tokens_saved=saved,
                delta_prompt_payload=delta_prompt,
                transclusion_tag=f"![[{updated_node.concept_id}#ZONE:SUMMARY]]",
            )

        return InterningLookupResult(
            status="NEW_CONCEPT_MISS",
            concept=None,
            similarity_score=best_sim,
            estimated_tokens_saved=0,
            delta_prompt_payload=None,
            transclusion_tag=None,
        )

    def intern_new_concept(
        self,
        canonical_name_en: str,
        title_fa: str,
        entity_type: Literal["PERSON", "ORG", "LOCATION", "CONCEPT", "EVENT", "TECH", "PRODUCT", "CODE_SYMBOL"],
        canonical_definition_fa: str,
        canonical_summary_2line: str,
        aliases: Optional[List[str]] = None,
        source_ref: str = "manual",
        surface_form: Optional[str] = None,
        thread_id: Optional[str] = None,
        turn_id: Optional[str] = None,
        ast_structural_hash: Optional[str] = None,
        wikidata_qid: Optional[str] = None,
    ) -> OntologyConceptNode:
        """Creates and persists a brand-new canonical OntologyConceptNode."""
        slug = re.sub(r"[^A-Za-z0-9]+", "_", canonical_name_en.strip()).strip("_").upper()
        concept_id = f"ONT_{slug}"
        norm_key = canonical_lemmatize_key(canonical_name_en)
        all_aliases = sorted(set((aliases or []) + [canonical_name_en, title_fa]))
        occ = OntologyOccurrence(
            source_ref=source_ref,
            thread_id=thread_id,
            turn_id=turn_id,
            surface_form=surface_form or canonical_name_en,
        )
        node = OntologyConceptNode(
            concept_id=concept_id,
            canonical_name_en=canonical_name_en,
            title_fa=title_fa,
            entity_type=entity_type,
            normalized_key=norm_key,
            aliases=all_aliases,
            simhash_64=compute_simhash_64(canonical_definition_fa),
            ast_structural_hash=ast_structural_hash,
            canonical_definition_fa=canonical_definition_fa,
            canonical_summary_2line=canonical_summary_2line,
            wikidata_qid=wikidata_qid,
            occurrences=[occ],
            saved_tokens_count=0,
        )
        self.save_concept(node)
        return node
