"""F1-Meta-Framework Core Library (`f1_core`)."""
from .contracts import (
    CONTRACT_VERSION,
    ActorRole,
    ActorStamp,
    CompetenceRecord,
    ConstrainedLLMResponse,
    DevelopmentTrack,
    LearningValue,
    OntologyConceptNode,
    SpatialProvenance,
    SpawnAnchor,
    SpeechAct,
    ThreadBox,
    TurnNode,
)
from .learning_engine import (
    append_active_recall_card,
    assess_symbol_competence,
    update_bkt_mastery,
    update_fsrs6_memory,
)
from .ontology_interner import InterningLookupResult, OntologyRegistry
from .text_bidi import (
    canonical_lemmatize_key,
    char_ngram_cosine_similarity,
    compute_python_ast_hash,
    compute_simhash_64,
    normalize_persian_with_offsets,
)
from .thread_dag import ThreadDAGManager
from .zoned_markdown import (
    compute_roadmap_section_sha256,
    extract_zones,
    replace_zone_content,
    slice_zoned_markdown_for_ai,
    sync_two_way_code_embeds,
)

__all__ = [
    "CONTRACT_VERSION",
    "ActorRole",
    "ActorStamp",
    "CompetenceRecord",
    "ConstrainedLLMResponse",
    "DevelopmentTrack",
    "InterningLookupResult",
    "LearningValue",
    "OntologyConceptNode",
    "OntologyRegistry",
    "SpatialProvenance",
    "SpawnAnchor",
    "SpeechAct",
    "ThreadBox",
    "ThreadDAGManager",
    "TurnNode",
    "append_active_recall_card",
    "assess_symbol_competence",
    "canonical_lemmatize_key",
    "char_ngram_cosine_similarity",
    "compute_python_ast_hash",
    "compute_roadmap_section_sha256",
    "compute_simhash_64",
    "extract_zones",
    "normalize_persian_with_offsets",
    "replace_zone_content",
    "slice_zoned_markdown_for_ai",
    "sync_two_way_code_embeds",
    "update_bkt_mastery",
    "update_fsrs6_memory",
]

from .radar_nexus import MJNEXUS_17_DOMAINS, OwnerCurationLockError, RadarCategory, RadarResourceNode, RadarRing, ResourceType, update_radar_resource_safely
