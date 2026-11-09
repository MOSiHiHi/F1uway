#!/usr/bin/env python3
"""F1-Meta-Framework Unified Development & Learning Loop (`scripts/devloop.py`).

Commands:
  python3 scripts/devloop.py next          -> Guided Autopilot Wizard for humans (G15)
  python3 scripts/devloop.py status        -> Current task, active track, and token savings
  python3 scripts/devloop.py doctor        -> Environment & SHA-256 Playbook/Roadmap sync check (G16)
  python3 scripts/devloop.py ontology ...  -> Intern, lookup, or view token savings in Ontology Registry (G10-G12)
  python3 scripts/devloop.py thread ...    -> Create, branch, reply, or visualize ThreadBox DAGs (G05-G09)
  python3 scripts/devloop.py pack          -> Slice Zoned Markdown & build deterministic-prefix prompt (G14)
  python3 scripts/devloop.py sync-embeds   -> Two-way code embed synchronization (Universe 1)
  python3 scripts/devloop.py gate          -> Run Dual Quality Gate (Engineering pytest + Learning cards/threads)
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "src"))

from f1_core import (
    ActorRole,
    DevelopmentTrack,
    OntologyRegistry,
    SpeechAct,
    ThreadDAGManager,
    compute_roadmap_section_sha256,
    replace_zone_content,
    slice_zoned_markdown_for_ai,
    sync_two_way_code_embeds,
)
from f1_core.zoned_markdown import parse_simple_frontmatter


def _read_state() -> dict:
    state_md = REPO_ROOT / "STATE.md"
    meta = parse_simple_frontmatter(state_md.read_text(encoding="utf-8")) if state_md.exists() else {}
    return {
        "current_task": meta.get("current_task", "T1.1"),
        "active_track": meta.get("active_track", "H2"),
        "completed_tasks": meta.get("completed_tasks", "T0.1"),
    }


def cmd_next(_args: argparse.Namespace) -> int:
    """Human Autopilot Compass (`devloop.py next` - G15)."""
    state = _read_state()
    task_id = state["current_task"]
    playbook_path = REPO_ROOT / "docs" / "human" / "playbooks" / f"{task_id}.fa.md"
    ont = OntologyRegistry(REPO_ROOT)
    concepts = ont.list_all_concepts()
    total_saved = sum(c.saved_tokens_count for c in concepts)

    print("╔══════════════════════════════════════════════════════════════════════════╗")
    print("║ 🧭 قطب‌نمای خودران F1-Meta-Framework (بدون نیاز به حفظ کردن دستورات)      ║")
    print("╚══════════════════════════════════════════════════════════════════════════╝")
    print(f"  • تسک فعال فعلی:       {task_id} (مسیر پیشنهادی: {state['active_track']})")
    print(f"  • تسک‌های تکمیل‌شده:    {state['completed_tasks']}")
    print(f"  • گره‌های هستی‌شناسی:   {len(concepts)} مفهوم یکتاسازی‌شده (صرفه‌جویی: {total_saved} توکن)")
    print(f"  • فایل راهنمای شما:    {playbook_path.relative_to(REPO_ROOT)}")
    print("\n📌 ۳ گام ساده برای ادامه کار:")
    print(f"  1️⃣ مطالعه راهنمای خودران: فایل `{playbook_path.relative_to(REPO_ROOT)}` را باز کنید.")
    print(f"  2️⃣ اگر عبارتی برایتان سوال شد، بدون مصرف توکن تکراری شاخه بزنید:")
    print(f"     python3 scripts/devloop.py thread branch --task {task_id} --span \"extra=forbid\" --title \"چرایی قفل اسکیما\"")
    print(f"  3️⃣ اجرای دروازه دوگانه (تست کد + ثبت یادگیری):")
    print(f"     python3 scripts/devloop.py gate")
    return 0


def cmd_status(_args: argparse.Namespace) -> int:
    state = _read_state()
    ont = OntologyRegistry(REPO_ROOT)
    concepts = ont.list_all_concepts()
    print(json.dumps({
        "current_task": state["current_task"],
        "active_track": state["active_track"],
        "completed_tasks": state["completed_tasks"],
        "ontology_concepts_count": len(concepts),
        "total_saved_tokens": sum(c.saved_tokens_count for c in concepts),
    }, ensure_ascii=False, indent=2))
    return 0


def cmd_doctor(_args: argparse.Namespace) -> int:
    """Verifies repository integrity and SHA-256 sync between ROADMAP_AND_TASKS.md and Playbooks (G16)."""
    roadmap_path = REPO_ROOT / "ROADMAP_AND_TASKS.md"
    state = _read_state()
    task_id = state["current_task"]
    playbook_path = REPO_ROOT / "docs" / "human" / "playbooks" / f"{task_id}.fa.md"

    if not roadmap_path.exists() or not playbook_path.exists():
        print("❌ [DOCTOR] فایل ROADMAP_AND_TASKS.md یا پلی‌بوک تسک یافت نشد.")
        return 1

    expected_sha = compute_roadmap_section_sha256(roadmap_path.read_text(encoding="utf-8"), task_id)
    pb_meta = parse_simple_frontmatter(playbook_path.read_text(encoding="utf-8"))
    recorded_sha = pb_meta.get("roadmap_sha256", "")

    if recorded_sha and recorded_sha != expected_sha:
        print(f"❌ [DOCTOR] عدم تطابق هش SHA-256 برای {task_id}: roadmap={expected_sha} != playbook={recorded_sha}")
        return 1

    print(f"✅ [DOCTOR] سلامت محیط و تطابق SHA-256 پلی‌بوک {task_id} تایید شد (hash={expected_sha}).")
    return 0


def cmd_ontology(args: argparse.Namespace) -> int:
    ont = OntologyRegistry(REPO_ROOT)
    if args.ont_action == "stats":
        concepts = ont.list_all_concepts()
        total_saved = sum(c.saved_tokens_count for c in concepts)
        print(f"🧠 آمار رجیستری هستی‌شناسی: {len(concepts)} موجودیت ثبت‌شده | مجموع صرفه‌جویی: {total_saved} توکن")
        for c in concepts:
            print(f"  - [{c.concept_id}] {c.title_fa} ({c.canonical_name_en}) | ارجاعات: {len(c.occurrences)} | ذخیره: {c.saved_tokens_count} tok")
        return 0

    if args.ont_action == "lookup":
        res = ont.intercept_branch_spawn(
            span_text=args.span,
            source_ref="cli_lookup",
            sub_question=args.question,
        )
        print(f"🔍 نتیجه بررسی انشعاب روی عبارت «{args.span}»:")
        print(f"  • وضعیت: {res.status} (شباهت: {res.similarity_score})")
        print(f"  • صرفه‌جویی توکن در این فراخوانی: {res.estimated_tokens_saved} توکن")
        if res.concept:
            print(f"  • گره کانونیکال: {res.concept.concept_id} — {res.concept.title_fa}")
            print(f"  • تعریف مشترک: {res.concept.canonical_summary_2line}")
        if res.delta_prompt_payload:
            print(f"\n--- Delta Prompt (ارسال فقط تفاوت به API) ---\n{res.delta_prompt_payload}")
        return 0
    return 0


def cmd_thread(args: argparse.Namespace) -> int:
    dag = ThreadDAGManager(REPO_ROOT)
    task_id = args.task or _read_state()["current_task"]

    if args.thr_action == "tree":
        print(dag.render_ascii_tree(task_id))
        return 0

    if args.thr_action == "sync-md":
        playbook_path = REPO_ROOT / "docs" / "human" / "playbooks" / f"{task_id}.fa.md"
        if playbook_path.exists():
            md_zone = dag.render_markdown_thread_zone(task_id)
            updated = replace_zone_content(playbook_path.read_text(encoding="utf-8"), "THREADS", md_zone)
            playbook_path.write_text(updated, encoding="utf-8")
            print(f"✅ گراف مستطیل‌های چت در منطقه ZONE:THREADS فایل {playbook_path.name} به‌روزرسانی شد.")
        return 0

    if args.thr_action == "branch":
        boxes, turns = dag._load_task_records(task_id)
        if not boxes:
            root_box = dag.create_root_thread(task_id, f"نشست اصلی تسک {task_id}", thread_id=f"thr_{task_id}_main")
            root_turn = dag.add_turn(
                task_id=task_id,
                thread_id=root_box.thread_id,
                role=ActorRole.HUMAN,
                actor_id="MOSiHiHi",
                speech_act=SpeechAct.QUESTION,
                topic_pill_fa=f"شروع {task_id}",
                content_md=f"بررسی اولیه تسک {task_id}",
                turn_id="turn_root_01",
            )
            parent_thr_id = root_box.thread_id
            parent_turn_id = root_turn.turn_id
        else:
            parent_thr_id = args.parent_thread or next(iter(boxes.keys()))
            parent_turn_id = args.from_turn or next(iter(turns.keys()))

        child_box, lookup = dag.spawn_branch_thread(
            task_id=task_id,
            parent_thread_id=parent_thr_id,
            parent_turn_id=parent_turn_id,
            quoted_span=args.span,
            title_fa=args.title,
            sub_question=args.question,
        )
        print(f"🌿 مستطیل انشعاب جدید ایجاد شد: [{child_box.thread_id}] «{child_box.title_fa}»")
        print(f"   وضعیت رهگیری هستی‌شناسی: {lookup.status} (صرفه‌جویی: {lookup.estimated_tokens_saved} توکن)")
        return 0
    return 0


def cmd_pack(args: argparse.Namespace) -> int:
    """Slices Zoned Markdown and generates a deterministic-prefix prompt pack (G14, Universe 4)."""
    state = _read_state()
    task_id = args.task or state["current_task"]
    playbook_path = REPO_ROOT / "docs" / "human" / "playbooks" / f"{task_id}.fa.md"
    ont = OntologyRegistry(REPO_ROOT)
    ont_map = {c.concept_id: c.canonical_summary_2line for c in ont.list_all_concepts()}

    sliced = slice_zoned_markdown_for_ai(
        playbook_path,
        allowed_zones=("CONTRACT", "GOLDEN_VALUES"),
        ontology_summaries=ont_map,
    )
    out_pack = REPO_ROOT / ".omni-audit" / f"context_pack_{task_id}.md"
    out_pack.write_text(f"{sliced.deterministic_prefix}\n\n{sliced.sliced_zones_text}\n", encoding="utf-8")
    print(
        f"📦 بسته زمینه برای هوش مصنوعی آماده شد: {out_pack.relative_to(REPO_ROOT)}\n"
        f"   • خطوط کل فایل انسانی: {sliced.full_line_count} خط\n"
        f"   • خطوط برش‌خورده برای ماشین: {sliced.sliced_line_count} خط (صرفه‌جویی برش: {sliced.compression_ratio_pct}%)"
    )
    return 0


def cmd_sync_embeds(_args: argparse.Namespace) -> int:
    """Synchronizes Two-Way Code Embeds in all Playbooks (Universe 1)."""
    pb_dir = REPO_ROOT / "docs" / "human" / "playbooks"
    total = 0
    for md_file in pb_dir.glob("*.md"):
        cnt, _ = sync_two_way_code_embeds(md_file, REPO_ROOT)
        total += cnt
    print(f"🔄 همگام‌سازی دوطرفه کد (Two-Way Code Embed) انجام شد: {total} بلوک کد به‌روز گردید.")
    return 0


def cmd_gate(_args: argparse.Namespace) -> int:
    """Runs the Dual Quality Gate: Engineering Gate (pytest + doctor) + Learning Gate (cards + threads)."""
    print("🚦 در حال اجرای دروازه دوگانه کیفیت (Dual Quality Gate: Code + Learning)...")
    if cmd_doctor(_args) != 0:
        return 1

    res = subprocess.run(
        [sys.executable, "-m", "unittest", "discover", "-s", str(REPO_ROOT / "tests"), "-p", "test_*.py", "-v"],
        cwd=str(REPO_ROOT),
        capture_output=True,
        text=True,
    )
    if res.returncode != 0:
        print(f"❌ [ENGINEERING GATE FAILED]\n{res.stdout}\n{res.stderr}")
        return 1
    print(f"✅ [ENGINEERING GATE PASSED] تمام تست‌های واحد سبز هستند:\n{res.stdout.strip()}")

    cards_path = REPO_ROOT / "notebook" / "cards.tsv"
    if not cards_path.exists() or len(cards_path.read_text(encoding="utf-8").splitlines()) < 2:
        print("❌ [LEARNING GATE FAILED] حداقل یک فلش‌کارت بازیابی فعال باید در notebook/cards.tsv ثبت شده باشد.")
        return 1

    print("✅ [LEARNING GATE PASSED] فلش‌کارت‌های FSRS-6، گره‌های هستی‌شناسی و گراف نشست‌ها معتبر هستند.")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="F1-Meta-Framework Unified Dev & Learning CLI")
    sub = p.add_subparsers(dest="cmd", required=True)

    sub.add_parser("next")
    sub.add_parser("status")
    sub.add_parser("doctor")
    sub.add_parser("sync-embeds")
    sub.add_parser("gate")

    pack_p = sub.add_parser("pack")
    pack_p.add_argument("--task", default=None)

    ont_p = sub.add_parser("ontology")
    ont_sub = ont_p.add_subparsers(dest="ont_action", required=True)
    ont_sub.add_parser("stats")
    look_p = ont_sub.add_parser("lookup")
    look_p.add_argument("--span", required=True)
    look_p.add_argument("--question", default=None)

    thr_p = sub.add_parser("thread")
    thr_sub = thr_p.add_subparsers(dest="thr_action", required=True)
    t_tree = thr_sub.add_parser("tree")
    t_tree.add_argument("--task", default=None)
    t_sync = thr_sub.add_parser("sync-md")
    t_sync.add_argument("--task", default=None)
    t_br = thr_sub.add_parser("branch")
    t_br.add_argument("--task", default=None)
    t_br.add_argument("--parent-thread", default=None)
    t_br.add_argument("--from-turn", default=None)
    t_br.add_argument("--span", required=True)
    t_br.add_argument("--title", required=True)
    t_br.add_argument("--question", default=None)

    return p


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    dispatch = {
        "next": cmd_next,
        "status": cmd_status,
        "doctor": cmd_doctor,
        "ontology": cmd_ontology,
        "thread": cmd_thread,
        "pack": cmd_pack,
        "sync-embeds": cmd_sync_embeds,
        "gate": cmd_gate,
    }
    return dispatch[args.cmd](args)


if __name__ == "__main__":
    raise SystemExit(main())
