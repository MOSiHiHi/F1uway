-- اسکیمای یکپارچه PostgreSQL 16 + pgvector + tsvector + Recursive CTE (بدون نیاز به Apache AGE)
CREATE EXTENSION IF NOT EXISTS vector;
CREATE EXTENSION IF NOT EXISTS pgcrypto;

CREATE TABLE IF NOT EXISTS episodes (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    workspace TEXT NOT NULL DEFAULT 'default',
    source_url TEXT,
    title TEXT NOT NULL,
    raw_content TEXT NOT NULL,
    valid_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE IF NOT EXISTS chunks (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    workspace TEXT NOT NULL DEFAULT 'default',
    episode_id UUID NOT NULL REFERENCES episodes(id) ON DELETE CASCADE,
    page_no INT NOT NULL DEFAULT 1,
    bbox JSONB,
    char_span INT4RANGE,
    content TEXT NOT NULL,
    embedding vector(1024) NOT NULL,
    fts_stemmed tsvector GENERATED ALWAYS AS (to_tsvector('english', content)) STORED,
    fts_simple tsvector GENERATED ALWAYS AS (to_tsvector('simple', content)) STORED
);

CREATE INDEX IF NOT EXISTS idx_chunks_hnsw ON chunks USING hnsw (embedding vector_cosine_ops) WITH (m = 16, ef_construction = 200);
CREATE INDEX IF NOT EXISTS idx_chunks_fts_stem ON chunks USING gin (fts_stemmed);
CREATE INDEX IF NOT EXISTS idx_chunks_fts_simp ON chunks USING gin (fts_simple);

CREATE TABLE IF NOT EXISTS entities (
    id TEXT NOT NULL,
    workspace TEXT NOT NULL DEFAULT 'default',
    canonical_qid TEXT,
    entity_type TEXT NOT NULL CHECK (entity_type IN ('PERSON', 'ORG', 'LOCATION', 'CONCEPT', 'EVENT', 'TECH', 'PRODUCT', 'CODE_SYMBOL')),
    description TEXT NOT NULL,
    embedding vector(1024) NOT NULL,
    degree INT NOT NULL DEFAULT 0,
    PRIMARY KEY (workspace, id)
);

CREATE TABLE IF NOT EXISTS relationships (
    edge_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    workspace TEXT NOT NULL DEFAULT 'default',
    src_id TEXT NOT NULL,
    tgt_id TEXT NOT NULL,
    relation_type TEXT NOT NULL,
    description TEXT NOT NULL,
    weight FLOAT NOT NULL DEFAULT 1.0,
    valid_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    invalid_at TIMESTAMPTZ,
    superseded_by UUID REFERENCES relationships(edge_id)
);
