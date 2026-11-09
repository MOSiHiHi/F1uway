# 🗺️ نقشه راه جامع و تسک‌های اتمیک (`ROADMAP_AND_TASKS.md`)

این نقشه راه، ۲۸ تسک ۶ فازی را در قالب دو مسیر هم‌تکاملی **`Build-to-Learn (B2L)`** و **`Learn-to-Build (L2B)`** تعریف می‌کند. هر بخش دارای اثرانگشت `SHA-256` است که توسط `devloop.py doctor` با پلی‌بوک متناظر سنجیده می‌شود.

### T1.1
- **عنوان:** پیاده‌سازی قراردادهای هسته (`contracts.py`)، گراف مستطیل‌های چت (`thread_dag.py`) و یکتاساز هستی‌شناسی (`ontology_interner.py`)
- **ارزش یادگیری (`Learning-Value`):** `HIGH` (پیشنهاد مسیر: `H2_SOCRATIC_TUTOR`)
- **اهداف پوشش‌داده‌شده:** `G01` تا `G28` + ۴ مکانیسم جهان‌های موازی
- **گیت عبور (`Gate`):** `python3 scripts/devloop.py gate`

### T1.2
- **عنوان:** لایه نرمال‌سازی فارسی حافظ افست (`text_bidi.py`)، اثرانگشت `SimHash-64` و هش ساختاری AST (`compute_python_ast_hash`)
- **ارزش یادگیری (`Learning-Value`):** `HIGH` (پیشنهاد مسیر: `H2_SOCRATIC_TUTOR`)
- **گیت عبور (`Gate`):** `python3 -m unittest discover -s tests -p "test_*.py"`

### T2.1
- **عنوان:** کامپایلر ابرسندهای `Zoned Markdown` (`zoned_markdown.py`)، جاسازی دوطرفه کد (`Two-Way Code Embed`) و پیشوند قطعی کش LLM
- **ارزش یادگیری (`Learning-Value`):** `MEDIUM` (پیشنهاد مسیر: `H3_AI_REVIEWER`)
- **گیت عبور (`Gate`):** `python3 scripts/devloop.py sync-embeds && python3 scripts/devloop.py pack`

### T3.1
- **عنوان:** موتور ریاضی یادگیری سقراطی (`learning_engine.py`: `BKT + FSRS-6`) و اتصال رکورد تسلط (`CompetenceRecord`) به نمادهای AST
- **ارزش یادگیری (`Learning-Value`):** `HIGH` (پیشنهاد مسیر: `H2_SOCRATIC_TUTOR`)
- **گیت عبور (`Gate`):** `python3 scripts/devloop.py gate`

### T4.1
- **عنوان:** موتور رادار ابزارها و خزانه ۱۷ دامنه‌ای (`radar_nexus.py`) با قفل امنیتی فیلدهای `owner_only` و ادغام هستی‌شناسی
- **ارزش یادگیری (`Learning-Value`):** `MEDIUM` (پیشنهاد مسیر: `A1_PAIR_AGENT`)
- **گیت عبور (`Gate`):** `python3 scripts/devloop.py gate`

### T5.1
- **عنوان:** خط لوله استخراج اسناد و خزانه دو-زمانی (`Docling + GROBID + PostgreSQL pgvector/RCTE + RRF`) و اسکیل `phase0-omni-audit`
- **ارزش یادگیری (`Learning-Value`):** `HIGH` (پیشنهاد مسیر: `MIX_HYBRID`)
- **گیت عبور (`Gate`):** `python3 scripts/check_licenses.py && python3 scripts/devloop.py gate`

### T6.1
- **عنوان:** استودیوی وب تعاملی ۴ نمایی BiDi/فارسی (`site/index.html`: مستطیل‌های چت، رادار ابزار، هستی‌شناسی و نقشه تسلط)
- **ارزش یادگیری (`Learning-Value`):** `MEDIUM` (پیشنهاد مسیر: `A1_PAIR_AGENT`)
- **گیت عبور (`Gate`):** `python3 scripts/devloop.py gate`
