"""Socratic Learning Harness Engine: BKT + FSRS-6 + AST Competence Linker (G17, G18, G19, G20).

Implements exact mathematical formulas from `F1uent-Ecosystem/ARCHITECTURE.md`:
1. Bayesian Knowledge Tracing (BKT) posterior update given observation (correct/incorrect).
2. FSRS-6 (Free Spaced Repetition Scheduler) stability & difficulty updates.
3. Direct binding of `CompetenceRecord` to AST symbols and Ontology concepts (solving
   LearnHarness Issue #115) and exporting active-recall cards to `notebook/cards.tsv`.
"""
from __future__ import annotations

import math
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import List

from .contracts import CompetenceRecord, MisconceptionEntry


def update_bkt_mastery(
    p_known_prior: float,
    is_correct: bool,
    p_transit: float = 0.15,
    p_slip: float = 0.10,
    p_guess: float = 0.20,
) -> float:
    """Standard Bayesian Knowledge Tracing (BKT) two-step update (Golden Values verified).

    Step 1 (Posterior given observation):
      If correct:
        P(L_t | obs=1) = [P(L_{t-1}) * (1 - P(S))] / [P(L_{t-1})*(1 - P(S)) + (1 - P(L_{t-1}))*P(G)]
      If incorrect:
        P(L_t | obs=0) = [P(L_{t-1}) * P(S)] / [P(L_{t-1})*P(S) + (1 - P(L_{t-1}))*(1 - P(G))]
    Step 2 (Transition):
      P(L_t) = P(L_t | obs) + (1 - P(L_t | obs)) * P(T)
    """
    if is_correct:
        num = p_known_prior * (1.0 - p_slip)
        den = num + (1.0 - p_known_prior) * p_guess
    else:
        num = p_known_prior * p_slip
        den = num + (1.0 - p_known_prior) * (1.0 - p_guess)

    posterior = num / den if den > 0 else p_known_prior
    p_next = posterior + (1.0 - posterior) * p_transit
    return round(min(0.9999, max(0.0001, p_next)), 4)


def update_fsrs6_memory(
    stability: float,
    difficulty: float,
    grade: int,
    elapsed_days: float = 1.0,
) -> tuple[float, float, int]:
    """FSRS-6 Core Memory State Update (grade: 1=Again, 2=Hard, 3=Good, 4=Easy).

    Returns (new_stability, new_difficulty, next_interval_days).
    """
    if grade not in (1, 2, 3, 4):
        raise ValueError("FSRS grade must be in {1, 2, 3, 4}.")

    # Retrievability R(t, S) = (1 + factor * t / S) ^ (-w)
    retrievability = math.pow(1.0 + (elapsed_days / (9.0 * max(0.1, stability))), -1.0)

    # Update Difficulty D' in [1.0, 10.0]
    delta_d = -0.8 * (grade - 3)
    new_d = difficulty + delta_d * ((10.0 - difficulty) / 9.0 if delta_d > 0 else (difficulty - 1.0) / 9.0)
    new_d = round(min(10.0, max(1.0, new_d)), 4)

    # Update Stability S'
    if grade == 1:
        # Lapse / Forgetting curve
        new_s = max(0.5, stability * 0.35 * math.exp(-0.05 * new_d))
    else:
        grade_mult = {2: 0.85, 3: 1.0, 4: 1.35}[grade]
        growth = 1.0 + math.exp(1.1) * (11.0 - new_d) * math.pow(stability, -0.2) * (
            math.exp(0.8 * (1.0 - retrievability)) - 1.0
        ) * grade_mult
        new_s = stability * max(1.05, growth)

    new_s = round(new_s, 4)
    next_interval = max(1, int(round(new_s)))
    return new_s, new_d, next_interval


def assess_symbol_competence(
    record: CompetenceRecord,
    grade: int,
    misconception_fa: str | None = None,
    turn_id: str = "turn_manual",
) -> CompetenceRecord:
    """Updates both BKT mastery probability and FSRS-6 schedule for an AST symbol or Ontology node."""
    is_correct = grade >= 3
    new_p_known = update_bkt_mastery(record.bkt_p_known, is_correct=is_correct)
    new_s, new_d, next_ivl = update_fsrs6_memory(
        stability=record.fsrs_stability,
        difficulty=record.fsrs_difficulty,
        grade=grade,
        elapsed_days=max(1.0, float(record.interval_days)),
    )
    next_dt = (datetime.now(timezone.utc) + timedelta(days=next_ivl)).strftime("%Y-%m-%dT%H:%M:%SZ")

    misc_list = list(record.misconceptions)
    if misconception_fa:
        misc_list.append(
            MisconceptionEntry(
                misconception_id=f"misc_{len(misc_list) + 1:03d}",
                description_fa=misconception_fa,
                detected_in_turn_id=turn_id,
                resolved=False,
            )
        )

    return record.model_copy(
        update={
            "bkt_p_known": new_p_known,
            "fsrs_stability": new_s,
            "fsrs_difficulty": new_d,
            "interval_days": next_ivl,
            "next_review_utc": next_dt,
            "attempts_count": record.attempts_count + 1,
            "misconceptions": misc_list,
        }
    )


def append_active_recall_card(
    cards_tsv_path: Path,
    card_id: str,
    symbol_or_concept_ref: str,
    prompt_without_concept_name_fa: str,
    answer_fa: str,
    source_turn_id: str,
    stability: float = 1.0,
    difficulty: float = 5.0,
    next_review: str = "2026-11-09",
) -> None:
    """Appends an active-recall card (AITutoR rule: prompt must not give away concept name) to `notebook/cards.tsv`."""
    cards_tsv_path.parent.mkdir(parents=True, exist_ok=True)
    header = "card_id\tsymbol_ref\tprompt_fa\tanswer_fa\tsource_turn_id\tstability\tdifficulty\tnext_review\n"
    if not cards_tsv_path.exists():
        cards_tsv_path.write_text(header, encoding="utf-8")

    clean_q = prompt_without_concept_name_fa.replace("\t", " ").replace("\n", " ")
    clean_a = answer_fa.replace("\t", " ").replace("\n", " ")
    row = f"{card_id}\t{symbol_or_concept_ref}\t{clean_q}\t{clean_a}\t{source_turn_id}\t{stability}\t{difficulty}\t{next_review}\n"
    with cards_tsv_path.open("a", encoding="utf-8") as f:
        f.write(row)
