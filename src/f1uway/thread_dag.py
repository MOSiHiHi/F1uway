"""UI-Agnostic Branchable ThreadBox DAG Engine (G05, G06, G07, G08, G09).

Features:
- Stores every ThreadBox and TurnNode in append-only `.jsonl` files under `notebook/threads/`.
- Supports branching a new `ThreadBox` from ANY `TurnNode` (and specific `quoted_span`),
  automatically invoking the `OntologyRegistry` Spawn Interceptor first so duplicate concepts
  cost 0 API tokens.
- Renders into 3 UI-agnostic views:
  1. ASCII/Unicode Terminal Tree (`render_ascii_tree`) showing who replied to whom, speech acts,
     and spawned branches at a glance.
  2. Collapsible `<details>` Markdown + Mermaid DAG (`render_markdown_thread_zone`) for Zoned Markdown.
  3. React Flow DOM Graph JSON (`export_react_flow_graph`) with RTL/BiDi node metadata.
- Supports `resolve_and_distill_thread()` which collapses a side thread into its parent turn
  and optionally promotes the finding into the Ontology Registry and FSRS-6 flashcards.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List, Literal, Optional, Tuple

from .contracts import (
    ActorRole,
    ActorStamp,
    DevelopmentTrack,
    SpawnAnchor,
    SpeechAct,
    ThreadBox,
    TurnNode,
    utc_now_iso,
)
from .ontology_interner import InterningLookupResult, OntologyRegistry

SPEECH_ACT_BADGES: Dict[SpeechAct, str] = {
    SpeechAct.QUESTION: "❓ [پرسش]",
    SpeechAct.HYPOTHESIS: "💡 [فرضیه]",
    SpeechAct.PROPOSAL: "🛠️ [پیشنهاد]",
    SpeechAct.CRITIQUE: "🛡️ [نقد/ضدچاپلوسی]",
    SpeechAct.VERIFICATION: "✅ [تست ماشین]",
    SpeechAct.SYNTHESIS: "📌 [جمع‌بندی]",
}


class ThreadDAGManager:
    """Manages branchable ThreadBoxes and TurnNodes for tasks and documents."""

    def __init__(self, repo_root: Path, ontology: Optional[OntologyRegistry] = None):
        self.repo_root = repo_root
        self.threads_dir = repo_root / "notebook" / "threads"
        self.threads_dir.mkdir(parents=True, exist_ok=True)
        self.ontology = ontology or OntologyRegistry(repo_root)

    def _task_jsonl_path(self, task_id: str) -> Path:
        safe_id = task_id.replace("/", "_")
        return self.threads_dir / f"THR_{safe_id}.jsonl"

    def _load_task_records(self, task_id: str) -> Tuple[Dict[str, ThreadBox], Dict[str, TurnNode]]:
        path = self._task_jsonl_path(task_id)
        boxes: Dict[str, ThreadBox] = {}
        turns: Dict[str, TurnNode] = {}
        if not path.exists():
            return boxes, turns

        for line in path.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line:
                continue
            raw = json.loads(line)
            if raw.get("record_type") == "thread_box":
                box = ThreadBox.model_validate(raw)
                boxes[box.thread_id] = box
            elif raw.get("record_type") == "turn_node":
                turn = TurnNode.model_validate(raw)
                turns[turn.turn_id] = turn
        return boxes, turns

    def _persist_all(self, task_id: str, boxes: Dict[str, ThreadBox], turns: Dict[str, TurnNode]) -> None:
        path = self._task_jsonl_path(task_id)
        lines: List[str] = []
        for box in boxes.values():
            lines.append(box.model_dump_json())
        for turn in turns.values():
            lines.append(turn.model_dump_json())
        path.write_text("\n".join(lines) + "\n", encoding="utf-8")

    def create_root_thread(
        self,
        task_id: str,
        title_fa: str,
        thread_id: Optional[str] = None,
    ) -> ThreadBox:
        boxes, turns = self._load_task_records(task_id)
        kwargs: Dict[str, Any] = {
            "task_id": task_id,
            "title_fa": title_fa,
            "intent_type": "main_task",
        }
        if thread_id:
            kwargs["thread_id"] = thread_id
        box = ThreadBox(**kwargs)
        boxes[box.thread_id] = box
        self._persist_all(task_id, boxes, turns)
        return box

    def add_turn(
        self,
        task_id: str,
        thread_id: str,
        role: ActorRole,
        actor_id: str,
        speech_act: SpeechAct,
        topic_pill_fa: str,
        content_md: str,
        reply_to_turn_id: Optional[str] = None,
        track_mode: DevelopmentTrack = DevelopmentTrack.H2_SOCRATIC_TUTOR,
        code_refs: Optional[List[str]] = None,
        ontology_refs: Optional[List[str]] = None,
        token_cost: int = 0,
        turn_id: Optional[str] = None,
    ) -> TurnNode:
        boxes, turns = self._load_task_records(task_id)
        if thread_id not in boxes:
            raise KeyError(f"ThreadBox '{thread_id}' not found in task '{task_id}'.")

        kwargs: Dict[str, Any] = {
            "thread_id": thread_id,
            "reply_to_turn_id": reply_to_turn_id,
            "actor": ActorStamp(role=role, actor_id=actor_id, track_mode=track_mode),
            "speech_act": speech_act,
            "topic_pill_fa": topic_pill_fa,
            "content_md": content_md,
            "code_refs": code_refs or [],
            "ontology_refs": ontology_refs or [],
            "token_cost": token_cost,
        }
        if turn_id:
            kwargs["turn_id"] = turn_id
        node = TurnNode(**kwargs)
        turns[node.turn_id] = node
        self._persist_all(task_id, boxes, turns)
        return node

    def spawn_branch_thread(
        self,
        task_id: str,
        parent_thread_id: str,
        parent_turn_id: str,
        quoted_span: str,
        title_fa: str,
        sub_question: Optional[str] = None,
        intent_type: Literal["side_question", "what_if_fork", "bug_triage"] = "side_question",
        branch_thread_id: Optional[str] = None,
    ) -> Tuple[ThreadBox, InterningLookupResult]:
        """Spawns a new rectangular ThreadBox from a specific `parent_turn_id` and `quoted_span`.

        Automatically queries the OntologyRegistry first:
        - If `quoted_span` is already interned (ZERO_TOKEN_HIT), it immediately populates
          the child thread with a 0-token synthesis turn referencing the canonical definition
          and marks the thread resolved!
        """
        boxes, turns = self._load_task_records(task_id)
        if parent_turn_id not in turns:
            raise KeyError(f"Parent TurnNode '{parent_turn_id}' not found.")

        lookup = self.ontology.intercept_branch_spawn(
            span_text=quoted_span,
            source_ref=f"{task_id}::{parent_turn_id}",
            sub_question=sub_question,
            thread_id=parent_thread_id,
            turn_id=parent_turn_id,
        )

        anchor = SpawnAnchor(
            parent_thread_id=parent_thread_id,
            parent_turn_id=parent_turn_id,
            quoted_span=quoted_span,
            ontology_concept_id=lookup.concept.concept_id if lookup.concept else None,
        )

        box_kwargs: Dict[str, Any] = {
            "task_id": task_id,
            "title_fa": title_fa,
            "intent_type": intent_type,
            "spawned_from": anchor,
        }
        if branch_thread_id:
            box_kwargs["thread_id"] = branch_thread_id
        child_box = ThreadBox(**box_kwargs)

        # Link parent turn -> child_box
        parent_turn = turns[parent_turn_id]
        updated_parent_turn = parent_turn.model_copy(
            update={"spawned_thread_ids": parent_turn.spawned_thread_ids + [child_box.thread_id]}
        )
        turns[parent_turn_id] = updated_parent_turn
        boxes[child_box.thread_id] = child_box
        self._persist_all(task_id, boxes, turns)

        # If Ontology Registry hit with 0 tokens, auto-mount the canonical answer!
        if lookup.status == "ZERO_TOKEN_HIT" and lookup.concept is not None:
            auto_content = (
                f"⚡ **[بازیابی فوری از هستی‌شناسی محلی — هزینه: ۰ توکن]**\n\n"
                f"عبارت منشعب‌شده «`{quoted_span}`» قبلاً در گره کانونیکال "
                f"`[[{lookup.concept.concept_id}]]` ({lookup.concept.title_fa}) تعریف و تثبیت شده است:\n\n"
                f"> {lookup.concept.canonical_summary_2line}\n\n"
                f"{lookup.concept.canonical_definition_fa}"
            )
            self.add_turn(
                task_id=task_id,
                thread_id=child_box.thread_id,
                role=ActorRole.MACHINE_TOOL,
                actor_id="ontology_cache_interceptor",
                speech_act=SpeechAct.SYNTHESIS,
                topic_pill_fa=f"کش هستی‌شناسی: {lookup.concept.concept_id}",
                content_md=auto_content,
                ontology_refs=[lookup.concept.concept_id],
                token_cost=0,
            )
            child_box = self.resolve_thread(
                task_id=task_id,
                thread_id=child_box.thread_id,
                resolution_summary_fa=lookup.concept.canonical_summary_2line,
                promoted_ontology_id=lookup.concept.concept_id,
            )

        return child_box, lookup

    def resolve_thread(
        self,
        task_id: str,
        thread_id: str,
        resolution_summary_fa: str,
        promoted_ontology_id: Optional[str] = None,
    ) -> ThreadBox:
        """Marks a ThreadBox as resolved and attaches its distilled summary (G09)."""
        boxes, turns = self._load_task_records(task_id)
        box = boxes[thread_id]
        updated = box.model_copy(
            update={
                "status": "resolved",
                "resolved_at": utc_now_iso(),
                "resolution_summary_fa": resolution_summary_fa,
                "promoted_ontology_id": promoted_ontology_id or box.promoted_ontology_id,
            }
        )
        boxes[thread_id] = updated
        self._persist_all(task_id, boxes, turns)
        return updated

    def get_branch_context_messages(self, task_id: str, thread_id: str) -> List[TurnNode]:
        """GCC Branch Context Isolation (G06): Returns ONLY the ancestor chain up to the spawn point
        plus turns inside `thread_id`, preventing sibling side-threads from polluting LLM context.
        """
        boxes, turns = self._load_task_records(task_id)
        if thread_id not in boxes:
            return []

        box = boxes[thread_id]
        chain: List[TurnNode] = []

        # If spawned from a parent turn, trace ancestor turns in parent thread up to parent_turn_id
        if box.spawned_from:
            parent_tid = box.spawned_from.parent_turn_id
            ancestors: List[TurnNode] = []
            curr_id: Optional[str] = parent_tid
            while curr_id and curr_id in turns:
                t_node = turns[curr_id]
                ancestors.append(t_node)
                curr_id = t_node.reply_to_turn_id
            chain.extend(reversed(ancestors))

        # Append turns belonging to this thread_id in chronological order
        own_turns = [t for t in turns.values() if t.thread_id == thread_id]
        chain.extend(own_turns)
        return chain

    def render_ascii_tree(self, task_id: str) -> str:
        """Renders a visual rectangular box-and-branch tree for terminal CLI inspection (G07, G08)."""
        boxes, turns = self._load_task_records(task_id)
        if not boxes:
            return f"هیچ نشستی برای تسک {task_id} ثبت نشده است."

        lines: List[str] = []
        for box in boxes.values():
            status_icon = "🟢" if box.status == "resolved" else "🔵"
            spawn_info = (
                f" (منشعب از پیام `{box.spawned_from.parent_turn_id}` روی عبارت «{box.spawned_from.quoted_span}»)"
                if box.spawned_from else " (رشته اصلی تسک)"
            )
            lines.append(f"┏━━ {status_icon} مستطیل نشست [{box.thread_id}]: {box.title_fa}{spawn_info}")
            box_turns = [t for t in turns.values() if t.thread_id == box.thread_id]
            for t in box_turns:
                badge = SPEECH_ACT_BADGES.get(t.speech_act, "[پیام]")
                reply_str = f" ↩ در پاسخ به `{t.reply_to_turn_id}`" if t.reply_to_turn_id else ""
                cost_str = "⚡0-Token Cache" if t.token_cost == 0 and t.ontology_refs else f"{t.token_cost} tok"
                lines.append(
                    f"┃  ├─ ({t.turn_id}) [{t.actor.role.value}:{t.actor.actor_id}] "
                    f"{badge} «{t.topic_pill_fa}»{reply_str} [{cost_str}]"
                )
                preview = t.content_md.splitlines()[0][:85]
                lines.append(f"┃  │    متن: {preview}...")
                for child_thr_id in t.spawned_thread_ids:
                    child_box = boxes.get(child_thr_id)
                    c_title = child_box.title_fa if child_box else child_thr_id
                    c_ont = f" -> هستی‌شناسی: {child_box.promoted_ontology_id}" if (child_box and child_box.promoted_ontology_id) else ""
                    lines.append(f"┃  │    ╰──> 🌿 انشعاب مستطیل فرزند: [{child_thr_id}] «{c_title}»{c_ont}")
            if box.resolution_summary_fa:
                lines.append(f"┃  📌 نتیجه تقطیرشده: {box.resolution_summary_fa}")
            lines.append("┗" + "━" * 72)
        return "\n".join(lines)

    def render_markdown_thread_zone(self, task_id: str) -> str:
        """Renders collapsible `<details>` ThreadBoxes for embedding inside Zoned Markdown files."""
        boxes, turns = self._load_task_records(task_id)
        if not boxes:
            return "_هنوز مستطیل گفتگویی برای این تسک ثبت نشده است._"

        out: List[str] = []
        for box in boxes.values():
            open_attr = " open" if box.intent_type == "main_task" else ""
            spawn_note = (
                f" — 🌿 *منشعب از `{box.spawned_from.parent_turn_id}` روی عبارت* `{box.spawned_from.quoted_span}`"
                if box.spawned_from else " — *مسیر اصلی*"
            )
            ont_badge = f" | 🧠 `{box.promoted_ontology_id}`" if box.promoted_ontology_id else ""
            out.append(
                f"<details{open_attr}>\n"
                f"<summary>🟦 <b>[{box.thread_id}] {box.title_fa}</b> ({box.status}){spawn_note}{ont_badge}</summary>\n"
            )
            box_turns = [t for t in turns.values() if t.thread_id == box.thread_id]
            for t in box_turns:
                badge = SPEECH_ACT_BADGES.get(t.speech_act, "[پیام]")
                reply_tag = f" *(در پاسخ به `{t.reply_to_turn_id}`)*" if t.reply_to_turn_id else ""
                out.append(
                    f"- **`{t.turn_id}` | {t.actor.role.value} (`{t.actor.actor_id}`)** — {badge} **{t.topic_pill_fa}**{reply_tag}:\n"
                    f"  > {t.content_md.replace(chr(10), chr(10) + '  > ')}"
                )
                for child_id in t.spawned_thread_ids:
                    c_box = boxes.get(child_id)
                    if c_box:
                        out.append(
                            f"  - ↳ 🌿 **انشعاب به مستطیل `[{child_id}]` ({c_box.title_fa}):** "
                            f"{c_box.resolution_summary_fa or 'در جریان...'}"
                        )
            if box.resolution_summary_fa:
                out.append(f"\n> ✅ **جمع‌بندی تقطیرشده مستطیل:** {box.resolution_summary_fa}")
            out.append("</details>\n")
        return "\n".join(out)

    def export_react_flow_graph(self, task_id: str) -> Dict[str, Any]:
        """Exports UI-agnostic React Flow DOM nodes & edges with RTL/BiDi metadata (G08, G27)."""
        boxes, turns = self._load_task_records(task_id)
        rf_nodes: List[Dict[str, Any]] = []
        rf_edges: List[Dict[str, Any]] = []

        for idx, box in enumerate(boxes.values()):
            box_turns = [t.model_dump() for t in turns.values() if t.thread_id == box.thread_id]
            rf_nodes.append({
                "id": box.thread_id,
                "type": "threadBoxNode",
                "position": {"x": (idx % 2) * 420, "y": idx * 240},
                "data": {
                    "dir": "rtl",
                    "threadBox": box.model_dump(),
                    "turns": box_turns,
                },
            })
            if box.spawned_from:
                rf_edges.append({
                    "id": f"edge_{box.spawned_from.parent_turn_id}_to_{box.thread_id}",
                    "source": box.spawned_from.parent_thread_id,
                    "sourceHandle": box.spawned_from.parent_turn_id,
                    "target": box.thread_id,
                    "label": f"انشعاب: {box.spawned_from.quoted_span}",
                    "animated": box.status == "active",
                })
        return {"nodes": rf_nodes, "edges": rf_edges}
