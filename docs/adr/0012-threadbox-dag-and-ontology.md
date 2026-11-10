---
ont_id: ONT_F1UXUS_ADR_0012_THREADBOX_DAG_AND_ONTOLOGY
source_project: F1uxus
domain: adr
title_fa: "ADR-0012: معماری گراف مستطیل‌های چت (`ThreadBox DAG`)، درونی‌سازی هستی‌شناختی ضدتکرار و ۴ جهان موازی"
content_is_data: true
---
<!-- ZONE:HUMAN_INTUITION_START -->
# ADR-0012: معماری گراف مستطیل‌های چت (`ThreadBox DAG`)، درونی‌سازی هستی‌شناختی ضدتکرار و ۴ جهان موازی
- **وضعیت:** پذیرفته‌شده (Accepted)
- **تصمیم معماری:**
  1. هر نشست کاری یا آموزشی به صورت گراف جهت‌دار غیرمدور از مستطیل‌های `ThreadBox` و گره‌های `TurnNode` در `notebook/threads/THR_*.jsonl` ثبت می‌شود.
  2. هر انشعاب روی عبارت $X$ ابتدا از قلاب `OntologyRegistry.intercept_branch_spawn` عبور می‌کند تا در صورت وجود در هستی‌شناسی، با **۰ توکن (`ZERO_TOKEN_HIT`)** یا به صورت تفاضلی (`DELTA_PROMPT_MODE`) پاسخ داده شود.
  3. چهار مکانیسم از جهان‌های موازی در هسته تعبیه شده‌اند: جاسازی دوطرفه کد (`<!-- EMBED: ... -->` از *Literate Programming*)، هش ساختاری AST (`compute_python_ast_hash` از *Unison*)، ایندکس سایه SQLite (`.omni-audit/shadow_index.sqlite` از *Datomic*) و چیدمان الفبایی پیشوند پرامپت (از *RadixAttention*).
<!-- ZONE:HUMAN_INTUITION_END -->
<!-- ZONE:CONTRACT_START -->
- Project: `F1uxus` | Ontology: `ONT_F1UXUS_ADR_0012_THREADBOX_DAG_AND_ONTOLOGY` | Thread: `THR_F1UXUS_0012_THREADBOX_DAG_AND_ONTOLOGY`
<!-- ZONE:CONTRACT_END -->
<!-- ZONE:EXECUTION_CORE_START -->
```python
ONT_ID = "ONT_F1UXUS_ADR_0012_THREADBOX_DAG_AND_ONTOLOGY"
SOURCE_REF = "initdb/01_schema.sql"
```
<!-- ZONE:EXECUTION_CORE_END -->
<!-- ZONE:WORKSHEET_START -->
## تمرین ۱۰ دقیقه‌ای (F1uxus)
1. معماری و قرارداد `ONT_F1UXUS_ADR_0012_THREADBOX_DAG_AND_ONTOLOGY` در `F1uxus` چگونه راستی‌آزمایی می‌شود؟
<details data-f1-thread="THR_F1UXUS_0012_THREADBOX_DAG_AND_ONTOLOGY"><summary>ThreadBox THR_F1UXUS_0012_THREADBOX_DAG_AND_ONTOLOGY</summary></details>
<!-- ZONE:WORKSHEET_END -->
