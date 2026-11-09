"""Persian/BiDi Offset-Preserving Normalizer, SimHash-64 & AST Content Hasher (G26, Universe 2).

Solves:
1. ADR-003 (F1uxus): Normalizing Persian characters (ي/ك -> ی/ک, ZWNJ spacing, NFKC)
   without losing exact character span offsets (`char_span`) in the original text.
2. Universe 2 (Unison/Nix): AST structural hashing for Python symbols so whitespace or
   comment edits never invalidate Ontology or Test caches.
3. Locality-Sensitive 64-bit SimHash + Char-Ngram Cosine Similarity for 0-token local
   deduplication when GPU/BGE-M3 is offline.
"""
from __future__ import annotations

import ast
import hashlib
import textwrap
import math
import re
import unicodedata
from collections import Counter
from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple

PERSIAN_CHAR_MAP: Dict[str, str] = {
    "ي": "ی",
    "ى": "ی",
    "ئ": "ی",
    "ك": "ک",
    "ة": "ه",
    "ؤ": "و",
    "إ": "ا",
    "أ": "ا",
    "ٱ": "ا",
    "۰": "0", "۱": "1", "۲": "2", "۳": "3", "۴": "4",
    "۵": "5", "۶": "6", "۷": "7", "۸": "8", "۹": "9",
    "٠": "0", "١": "1", "٢": "2", "٣": "3", "٤": "4",
    "٥": "5", "٦": "6", "٧": "7", "٨": "8", "٩": "9",
}

# Arabic diacritics (Tashkeel) and directional formatting characters stripped during normalization
DIACRITICS_SET = {
    "\u064b", "\u064c", "\u064d", "\u064e", "\u064f", "\u0650", "\u0651", "\u0652",
    "\u0670", "\u200e", "\u200f", "\u202a", "\u202b", "\u202c", "\u202d", "\u202e",
}

PERSIAN_SUFFIXES = ("های", "هایی", "ها", "ان", "ات", "تر", "ترین", "گر", "ام", "ات", "اش")
PERSIAN_PREFIXES = ("می\u200c", "نمی\u200c", "بی\u200c", "بر")


@dataclass(frozen=True)
class NormalizedTextWithOffsetMap:
    """Holds normalized text and a bidirectional index map to original raw text (G26)."""
    raw_text: str
    normalized_text: str
    norm_to_raw_index: List[int]

    def map_norm_span_to_raw(self, norm_start: int, norm_end: int) -> Tuple[int, int]:
        """Maps a (start, end) slice in normalized_text back to exact (start, end) in raw_text."""
        if not self.norm_to_raw_index or norm_start >= len(self.norm_to_raw_index):
            return (0, 0)
        clamped_start = max(0, min(norm_start, len(self.norm_to_raw_index) - 1))
        clamped_end = max(clamped_start, min(norm_end - 1, len(self.norm_to_raw_index) - 1))
        raw_start = self.norm_to_raw_index[clamped_start]
        raw_end = self.norm_to_raw_index[clamped_end] + 1
        return (raw_start, raw_end)


def normalize_persian_with_offsets(raw_text: str) -> NormalizedTextWithOffsetMap:
    """Normalizes Persian/Arabic/English text while tracking every character's original offset."""
    out_chars: List[str] = []
    norm_to_raw: List[int] = []
    prev_was_space = True

    for raw_idx, ch in enumerate(raw_text):
        if ch in DIACRITICS_SET:
            continue
        # Convert ZWNJ (\u200c) and whitespace sequences to a single canonical space for matching
        if ch == "\u200c" or ch.isspace():
            if not prev_was_space:
                out_chars.append(" ")
                norm_to_raw.append(raw_idx)
                prev_was_space = True
            continue

        mapped = PERSIAN_CHAR_MAP.get(ch, ch)
        nfkc_str = unicodedata.normalize("NFKC", mapped)
        for sub_ch in nfkc_str:
            out_chars.append(sub_ch)
            norm_to_raw.append(raw_idx)
            prev_was_space = False

    # Trim trailing space if present
    if out_chars and out_chars[-1] == " ":
        out_chars.pop()
        norm_to_raw.pop()

    return NormalizedTextWithOffsetMap(
        raw_text=raw_text,
        normalized_text="".join(out_chars),
        norm_to_raw_index=norm_to_raw,
    )


def canonical_lemmatize_key(phrase: str) -> str:
    """Lightweight deterministic Persian + English lemmatizer for Ontology Interning keys (G10)."""
    norm = normalize_persian_with_offsets(phrase).normalized_text.lower()
    # Keep alphanumeric and Persian letters
    tokens = re.findall(r"[a-z0-9_]+|[\u0600-\u06FF]+", norm)
    lemmatized_tokens: List[str] = []

    for tok in tokens:
        # Strip common Persian prefixes/suffixes if root remains >= 3 chars
        for pref in PERSIAN_PREFIXES:
            clean_pref = pref.replace("\u200c", "")
            if tok.startswith(clean_pref) and len(tok) - len(clean_pref) >= 3:
                tok = tok[len(clean_pref):]
                break
        for suf in PERSIAN_SUFFIXES:
            if tok.endswith(suf) and len(tok) - len(suf) >= 3:
                tok = tok[:-len(suf)]
                break
        # Strip simple English plural 's'
        if re.match(r"^[a-z]{4,}s$", tok) and not tok.endswith("ss"):
            tok = tok[:-1]
        lemmatized_tokens.append(tok)

    return "_".join(lemmatized_tokens) if lemmatized_tokens else "EMPTY_KEY"


def compute_simhash_64(text: str) -> str:
    """Computes a 64-bit SimHash fingerprint over character 3-grams and tokens (G01, G10, G23)."""
    norm = canonical_lemmatize_key(text)
    features = [norm[i:i + 3] for i in range(max(1, len(norm) - 2))]
    bit_weights = [0] * 64
    for feat in features:
        h = int(hashlib.md5(feat.encode("utf-8")).hexdigest()[:16], 16)
        for bit_idx in range(64):
            if (h >> bit_idx) & 1:
                bit_weights[bit_idx] += 1
            else:
                bit_weights[bit_idx] -= 1
    fingerprint = 0
    for bit_idx, weight in enumerate(bit_weights):
        if weight > 0:
            fingerprint |= (1 << bit_idx)
    return f"0x{fingerprint:016x}"


def char_ngram_cosine_similarity(text_a: str, text_b: str, n: int = 3) -> float:
    """Fast local semantic/lexical similarity fallback in [0.0, 1.0] (0-token, 0-GPU)."""
    norm_a = f"  {canonical_lemmatize_key(text_a)}  "
    norm_b = f"  {canonical_lemmatize_key(text_b)}  "
    vec_a = Counter(norm_a[i:i + n] for i in range(max(1, len(norm_a) - n + 1)))
    vec_b = Counter(norm_b[i:i + n] for i in range(max(1, len(norm_b) - n + 1)))
    intersection = set(vec_a.keys()) & set(vec_b.keys())
    numerator = sum(vec_a[k] * vec_b[k] for k in intersection)
    sum_a = sum(v * v for v in vec_a.values())
    sum_b = sum(v * v for v in vec_b.values())
    denom = math.sqrt(sum_a) * math.sqrt(sum_b)
    return round(numerator / denom, 4) if denom > 0 else 0.0


def compute_python_ast_hash(source_code: str, symbol_name: Optional[str] = None) -> str:
    """Universe 2 (Unison/Nix style): Content-addresses a Python file or specific function/class
    by hashing its normalized AST (ignoring comments, docstrings, and line formatting).
    """
    tree = ast.parse(textwrap.dedent(source_code))
    target_node: ast.AST = tree

    if symbol_name:
        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)) and node.name == symbol_name:
                target_node = node
                break

    # Strip docstrings so prose edits don't invalidate code logic hash
    for node in ast.walk(target_node):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef, ast.Module)):
            if (
                node.body
                and isinstance(node.body[0], ast.Expr)
                and isinstance(node.body[0].value, ast.Constant)
                and isinstance(node.body[0].value.value, str)
            ):
                node.body = node.body[1:] or [ast.Pass()]

    dumped = ast.dump(target_node, annotate_fields=True, include_attributes=False)
    return hashlib.sha256(dumped.encode("utf-8")).hexdigest()[:16]
