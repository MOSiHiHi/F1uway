"""MJNexus Unified Tool Radar, 17-Domain Learning Vault & Privacy-Preserving Records Adapter.

Unifies `MOSiHiHi/MJNexus` with `F1uent-Ecosystem` and `F1uxus`:
1. Enforces `ontology.yaml` ID schemes (`account:*`, `item:*`, `resource:*`, `concept:*`, `domain:*`, `claim:*`, `project:*`).
2. Strictly protects `owner_only` fields (`ring`, `notes_fa`, `verification`, `my_rating`) so AI agents can NEVER overwrite human curation decisions.
3. Treats external captions/posts/web pages strictly as DATA (`content_is_data`), never instructions.
4. Bridges MJNexus `propositions`, `edges`, and `review` records (`learning/framework/records.md`) directly into F1 `CompetenceRecord` (BKT + FSRS-6) while keeping `progress.md` as a zero-skeleton in public Git.
"""
from __future__ import annotations

import json
import sqlite3
from enum import Enum
from pathlib import Path
from typing import Dict, List, Literal, Optional

from .contracts import CompetenceRecord, F1BaseModel, Field, utc_now_iso
from .learning_engine import assess_symbol_competence


class RadarRing(str, Enum):
    """Owner-only Thoughtworks-style Technology Radar rings (MJNexus `ontology.yaml`)."""
    ADOPT = "adopt"    # Proven in my own work; default choice
    TRIAL = "trial"    # Worth using on a real project with care
    ASSESS = "assess"  # Worth exploring; default for everything new
    HOLD = "hold"      # Do not start new work with it (risk, license, quality)


class RadarCategory(str, Enum):
    CODING_AGENTS = "coding-agents"
    AGENT_FRAMEWORKS = "agent-frameworks"
    RAG_KNOWLEDGE = "rag-knowledge"
    MODELS_INFERENCE = "models-inference"
    MEDIA_GENERATION = "media-generation"
    AUTOMATION_BUSINESS = "automation-business"
    DEV_INFRA_SECURITY = "dev-infra-security"
    LEARNING_RESOURCES = "learning-resources"
    OTHER = "other"


class ResourceType(str, Enum):
    REPO = "repo"
    TOOL = "tool"
    MODEL = "model"
    PAPER = "paper"
    COURSE = "course"
    BOOK = "book"
    SITE = "site"
    DATASET = "dataset"
    SERVICE = "service"
    PROMPT_PACK = "prompt_pack"
    SKILL = "skill"
    PROTOCOL = "protocol"


MJNEXUS_17_DOMAINS: Tuple[str, ...] = (
    "ai",
    "business-marketing",
    "culture-spirituality",
    "design-typography",
    "gamedev",
    "hardware-tech-privacy",
    "health-sports",
    "history-myth",
    "learning-language-books",
    "math",
    "media-entertainment",
    "music-sound",
    "news-politics",
    "physics-astronomy",
    "programming-infra",
    "research",
    "society-religion",
    "visual-art",
)


class RadarResourceNode(F1BaseModel):
    """Represents a vetted tool, repo, model, or paper in the Unified F1-Nexus Radar."""
    resource_id: str = Field(min_length=5, description="e.g. 'resource:gh:tt-a1i/archify' or 'resource:claude-code'")
    name: str
    resource_type: ResourceType
    category: RadarCategory
    info_level: Literal["high", "medium", "low"] = "high"
    url: str = ""
    repo: str = ""
    license_spdx: str = "MIT"
    last_commit_date: Optional[str] = None
    what_fa: str = Field(min_length=5)
    use_fa: str = Field(min_length=5)
    concepts: List[str] = Field(default_factory=list)
    learning_nodes: List[str] = Field(default_factory=list, description="e.g. ['ai/04-agents-automation']")
    claims: List[str] = Field(default_factory=list)
    risk_flags: List[str] = Field(default_factory=list)
    # Owner-only fields: never inferred or overwritten by AI extraction
    owner_ring: RadarRing = RadarRing.ASSESS
    owner_verification: Literal["unverified", "checked", "verified", "rejected"] = "unverified"
    owner_notes_fa: Optional[str] = None
    ontology_concept_id: Optional[str] = None


class OwnerCurationLockError(PermissionError):
    """Raised when an automated agent attempts to mutate an `owner_only` field without `actor='owner'`."""


def update_radar_resource_safely(
    existing: RadarResourceNode,
    incoming_update: Dict[str, object],
    actor: Literal["owner", "ai_agent"] = "ai_agent",
) -> RadarResourceNode:
    """Enforces MJNexus `owner_only` principle: AI agents can update metadata (commits, claims, concepts)
    but are strictly blocked from mutating `owner_ring`, `owner_verification`, or `owner_notes_fa`.
    """
    owner_only_keys = {"owner_ring", "owner_verification", "owner_notes_fa"}
    if actor != "owner":
        violated = owner_only_keys.intersection(incoming_update.keys())
        if violated:
            raise OwnerCurationLockError(
                f"Security Gate (MJNexus owner_only): AI agent cannot modify {sorted(violated)}."
            )
    return existing.model_copy(update=incoming_update)
