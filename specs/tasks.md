---
ont_id: ONT_F1UENT_PLAYBOOKS_TASKS
source_project: F1uent-Ecosystem
domain: playbooks
title_fa: "فهرست وظایف اجرایی و نقاط بازرسی فاز ۰ تا ۶ (`specs/tasks.md`)"
content_is_data: true
---
<!-- ZONE:HUMAN_INTUITION_START -->
# فهرست وظایف اجرایی و نقاط بازرسی فاز ۰ تا ۶ (`specs/tasks.md`)

- [x] **فاز ۰ (Foundations & Meta-Governance):**
  - [x] `T0.1`: راه‌اندازی ساختار دایرکتوری ۶۰+ فایلی، قوانین `AGENTS.md`/`CLAUDE.md` و اسکریپت `devloop.py`.
  - [x] `T0.2`: استقرار ۱۲ سند تصمیم‌نامه معماری (`docs/adr/0001..0012`) و ۱۰ سند پژوهشی (`docs/research/01..10`).
- [x] **فاز ۱ (Core Contracts & Persian BiDi Layer):**
  - [x] `T1.1`: پیاده‌سازی مدل‌های تغییرناپذیر Pydantic با تقدم استدلال و گیت ضدچاپلوسی (`contracts.py`).
  - [x] `T1.2`: پیاده‌سازی نرمال‌ساز فارسی حافظ افست کاراکتری، `SimHash-64` و هش ساختاری AST (`text_bidi.py`).
- [x] **فاز ۲ (ThreadBox DAG, Ontology Interning & Zoned Markdown):**
  - [x] `T2.1`: پیاده‌سازی رجیستری هستی‌شناسی ضدتکرار توکن و ایندکس سایه SQLite (`ontology_interner.py`).
  - [x] `T2.2`: پیاده‌سازی موتور مستطیل‌های چت منشعب‌شونده (`thread_dag.py`) و کامپایلر `Zoned Markdown` (`zoned_markdown.py`).
- [x] **فاز ۳ (Socratic Learning Engine & Tool Radar):**
  - [x] `T3.1`: پیاده‌سازی فرمول‌های `BKT` و `FSRS-6` متصل به AST (`learning_engine.py`) و قفل `owner_only` رادار (`radar_nexus.py`).
- [ ] **فاز ۴ تا ۶ (Full Ingestion Pipeline, Multi-Agent Worktrees & 3D Galaxy Studio):**
  - [ ] اتصال کانتینرهای `PostgreSQL 16 + pgvector` و `SearXNG` (`docker-compose.yml`) و اجرای اسکیل `.agents/skills/phase0-omni-audit`.
<!-- ZONE:HUMAN_INTUITION_END -->
<!-- ZONE:CONTRACT_START -->
- Project: `F1uent-Ecosystem` | Ontology: `ONT_F1UENT_PLAYBOOKS_TASKS` | Thread: `THR_F1UENT_TASKS`
<!-- ZONE:CONTRACT_END -->
<!-- ZONE:EXECUTION_CORE_START -->
```python
ONT_ID = "ONT_F1UENT_PLAYBOOKS_TASKS"
SOURCE_REF = "specs/tasks.md"
```
<!-- ZONE:EXECUTION_CORE_END -->
<!-- ZONE:WORKSHEET_START -->
## تمرین ۱۰ دقیقه‌ای (F1uent-Ecosystem)
1. معماری و قرارداد `ONT_F1UENT_PLAYBOOKS_TASKS` در `F1uent-Ecosystem` چگونه راستی‌آزمایی می‌شود؟
<details data-f1-thread="THR_F1UENT_TASKS"><summary>ThreadBox THR_F1UENT_TASKS</summary></details>
<!-- ZONE:WORKSHEET_END -->
