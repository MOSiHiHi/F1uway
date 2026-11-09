# F1-Meta-Framework — Agent & Human Constitution (`AGENTS.md`)

> **Symlinked to `CLAUDE.md` and `GEMINI.md`**. Kept strictly under 150 lines for >92% adherence.

## 1. Mission & Core Architecture
This repository implements the **F1 Co-Evolutionary Engineering & Learning Framework**, unifying:
1. **Spec-First Spectrum (`H0` to `A2`):** Tasks run in human Socratic learning mode (`H0-H2`) or autonomous agent mode (`A1-A2`) while converging on the exact same deterministic gate (`scripts/devloop.py gate`).
2. **Branchable ThreadBox DAG (`src/f1_core/thread_dag.py`):** Every human/AI/machine step is recorded as an immutable `TurnNode` inside rectangular `ThreadBox` containers that can branch from any phrase (`quoted_span`).
3. **Zero-Token Ontology Interning (`src/f1_core/ontology_interner.py`):** Before calling any LLM API on a branched phrase, the local Ontology Registry (`notebook/ontology/ONT_*.md`) and SQLite shadow index are queried. Exact or near-duplicate ($\ge 0.92$) spans resolve in **0 API tokens**; partial overlaps use **Delta-Only Prompting**.
4. **Dual-Faced Zoned Markdown (`src/f1_core/zoned_markdown.py`):** Human playbooks contain rich self-guided explanations (`ZONE:HUMAN_INTUITION`, `ZONE:THREADS`, `ZONE:WORKSHEET`), while `devloop.py pack` slices only `ZONE:CONTRACT` and `ZONE:GOLDEN_VALUES` for the AI.

## 2. Toolchain Registry
| Operation | Exact Command |
| :--- | :--- |
| **Human Autopilot Compass** | `python3 scripts/devloop.py next` |
| **Environment & SHA-256 Check** | `python3 scripts/devloop.py doctor` |
| **Ontology Lookup / Token Stats** | `python3 scripts/devloop.py ontology stats` |
| **Branch a Thread on Span X** | `python3 scripts/devloop.py thread branch --span "X" --title "..."` |
| **Visualize Thread DAG in CLI** | `python3 scripts/devloop.py thread tree` |
| **Build Sliced AI Context Pack** | `python3 scripts/devloop.py pack` |
| **Run Dual Quality Gate** | `python3 scripts/devloop.py gate` |

## 3. Judgment Boundaries (`NEVER` / `ASK` / `ALWAYS`)
- **NEVER** mix structural refactoring (`struct:`) with behavioral changes (`feat:` / `fix:`) in the same commit (*Tidy First*).
- **NEVER** place verdict or boolean fields before `reasoning_chain` and `evidence_quote` in any Pydantic schema (`ConstrainedLLMResponse`).
- **NEVER** open a Socratic Tutor or review response with sycophantic validation ("بله، کاملاً درست است" / "You are completely right"); always run independent verification first.
- **NEVER** overwrite human notes in `docs/human/` or `notebook/` without explicit user confirmation.
- **ALWAYS** preserve Persian character offsets (`normalize_persian_with_offsets`) when indexing documents or spans.
- **ALWAYS** isolate inline LTR code/paths/math (`direction: ltr; unicode-bidi: isolate`) inside RTL Persian paragraphs.
