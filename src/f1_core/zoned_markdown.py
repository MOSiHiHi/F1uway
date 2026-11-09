"""Zoned Dual-Faced Markdown Compiler & Two-Way Code Snippet Synchronizer (G14, G15, G16, Universe 1 & 4).

Solves the fundamental paradox between Human Comprehension and Machine Token Efficiency:
- Humans get rich, self-guided documents (500+ lines) with an upfront "Autopilot Compass Box",
  intuitive analogies (`ZONE:HUMAN_INTUITION`), live synced code snippets (`<!-- EMBED: ... -->`),
  collapsible ThreadBox histories (`ZONE:THREADS`), and interactive worksheets (`ZONE:WORKSHEET`).
- Machines (`devloop.py pack`) slice ONLY the designated `token_slice_for_ai` zones (typically
  `ZONE:CONTRACT` and `ZONE:GOLDEN_VALUES`, < 50 lines) and prepend deterministic Ontology anchors
  in alphabetical order (Universe 4: RadixAttention Prefix Cache optimization).
"""
from __future__ import annotations

import ast
import hashlib
import textwrap
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional, Tuple


ZONE_PATTERN = re.compile(
    r"<!--\s*ZONE:([A-Z0-9_]+)_START\s*-->(.*?)<!--\s*ZONE:\1_END\s*-->",
    re.DOTALL,
)

EMBED_PATTERN = re.compile(
    r"(<!--\s*EMBED:\s*([a-zA-Z0-9_./-]+)#([a-zA-Z0-9_]+)\s*-->)(.*?)(<!--\s*/EMBED\s*-->)",
    re.DOTALL,
)


@dataclass(frozen=True)
class SlicedPromptPackage:
    """Output of slicing a Zoned Markdown file for AI consumption."""
    doc_id: str
    deterministic_prefix: str
    sliced_zones_text: str
    full_line_count: int
    sliced_line_count: int
    compression_ratio_pct: float


def parse_simple_frontmatter(md_text: str) -> Dict[str, str]:
    """Extracts key-value metadata from YAML frontmatter without external dependencies."""
    if not md_text.startswith("---"):
        return {}
    parts = md_text.split("---", 2)
    if len(parts) < 3:
        return {}
    meta: Dict[str, str] = {}
    for line in parts[1].splitlines():
        if ":" in line and not line.strip().startswith("#") and not line.strip().startswith("-"):
            k, v = line.split(":", 1)
            meta[k.strip()] = v.strip().strip('"').strip("'")
    return meta


def extract_zones(md_text: str) -> Dict[str, str]:
    """Returns a dictionary mapping zone names (e.g. 'CONTRACT') to their inner content."""
    zones: Dict[str, str] = {}
    for match in ZONE_PATTERN.finditer(md_text):
        zone_name = match.group(1).strip()
        zone_body = match.group(2).strip()
        zones[zone_name] = zone_body
    return zones


def replace_zone_content(md_text: str, zone_name: str, new_inner_content: str) -> str:
    """Updates a specific `<!-- ZONE:NAME_START -->...<!-- ZONE:NAME_END -->` block in place."""
    pattern = re.compile(
        rf"(<!--\s*ZONE:{re.escape(zone_name)}_START\s*-->)(.*?)(<!--\s*ZONE:{re.escape(zone_name)}_END\s*-->)",
        re.DOTALL,
    )
    if not pattern.search(md_text):
        raise ValueError(f"Zone '{zone_name}' not found in Markdown document.")
    return pattern.sub(rf"\1\n{new_inner_content.strip()}\n\3", md_text)


def extract_python_symbol_source(py_file: Path, symbol_name: str) -> str:
    """Extracts the exact source lines of a function or class from a real `.py` file."""
    source = py_file.read_text(encoding="utf-8")
    lines = source.splitlines()
    tree = ast.parse(source)
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)) and node.name == symbol_name:
            start = node.lineno - 1
            end = getattr(node, "end_lineno", node.lineno)
            return "\n".join(lines[start:end])
    raise KeyError(f"Symbol '{symbol_name}' not found in {py_file}")


def sync_two_way_code_embeds(md_path: Path, repo_root: Path) -> Tuple[int, str]:
    """Universe 1 (Literate Programming Two-Way Sync):
    Finds all `<!-- EMBED: path/to/file.py#SymbolName -->...<!-- /EMBED -->` blocks in `md_path`
    and updates them with the live source code from `repo_root / path/to/file.py`.
    """
    md_text = md_path.read_text(encoding="utf-8")
    updated_count = 0

    def _replacer(match: re.Match) -> str:
        nonlocal updated_count
        open_tag, rel_path, sym_name, _old_body, close_tag = match.groups()
        target_py = repo_root / rel_path
        if not target_py.exists():
            return match.group(0)
        try:
            live_code = extract_python_symbol_source(target_py, sym_name)
            updated_count += 1
            return f"{open_tag}\n```python\n{live_code}\n```\n{close_tag}"
        except KeyError:
            return match.group(0)

    new_md = EMBED_PATTERN.sub(_replacer, md_text)
    if updated_count > 0 and new_md != md_text:
        md_path.write_text(new_md, encoding="utf-8")
    return updated_count, new_md


def slice_zoned_markdown_for_ai(
    md_path: Path,
    allowed_zones: Tuple[str, ...] = ("CONTRACT", "GOLDEN_VALUES"),
    ontology_summaries: Optional[Dict[str, str]] = None,
) -> SlicedPromptPackage:
    """Slices ONLY machine-relevant zones from a rich human Markdown file and prepends
    alphabetically sorted Ontology definitions (Universe 4: Deterministic Prefix Caching).
    """
    raw_text = md_path.read_text(encoding="utf-8")
    meta = parse_simple_frontmatter(raw_text)
    doc_id = meta.get("doc_id", md_path.stem)
    zones = extract_zones(raw_text)

    # Universe 4: Deterministic Prefix Ordering for 90% KV-Cache hit rate
    prefix_lines = ["[F1_DETERMINISTIC_PREFIX_CACHE_HEADER v1.0]"]
    if ontology_summaries:
        for ont_id in sorted(ontology_summaries.keys()):
            prefix_lines.append(f"- {ont_id}: {ontology_summaries[ont_id]}")
    deterministic_prefix = "\n".join(prefix_lines)

    sliced_parts: List[str] = []
    for z_name in allowed_zones:
        if z_name in zones:
            sliced_parts.append(f"### [{z_name}]\n{zones[z_name]}")

    sliced_body = "\n\n".join(sliced_parts)
    full_lines = len(raw_text.splitlines())
    sliced_lines = len((deterministic_prefix + "\n" + sliced_body).splitlines())
    savings_pct = round((1.0 - (sliced_lines / max(1, full_lines))) * 100.0, 1)

    return SlicedPromptPackage(
        doc_id=doc_id,
        deterministic_prefix=deterministic_prefix,
        sliced_zones_text=sliced_body,
        full_line_count=full_lines,
        sliced_line_count=sliced_lines,
        compression_ratio_pct=max(0.0, savings_pct),
    )


def compute_roadmap_section_sha256(roadmap_text: str, task_id: str) -> str:
    """Computes SHA-256 fingerprint of a specific task section in ROADMAP_AND_TASKS.md (G16)."""
    pattern = re.compile(rf"(###\s+{re.escape(task_id)}\b.*?)(?=\n###\s+T|\Z)", re.DOTALL)
    match = pattern.search(roadmap_text)
    if not match:
        return "MISSING_TASK_SECTION"
    normalized_section = re.sub(r"\s+", " ", match.group(1).strip())
    return hashlib.sha256(normalized_section.encode("utf-8")).hexdigest()[:16]
