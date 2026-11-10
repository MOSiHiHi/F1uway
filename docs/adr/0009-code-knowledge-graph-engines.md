---
ont_id: ONT_F1UXUS_ADR_0009_CODE_KNOWLEDGE_GRAPH_ENGINES
source_project: F1uxus
domain: adr
title_fa: "ADR-0009: موتورهای گراف دانش کدبیس (CKG)، اسکیل `phase0-omni-audit` و ویکی خودنگهدار"
content_is_data: true
---
<!-- ZONE:HUMAN_INTUITION_START -->
# ADR-0009: موتورهای گراف دانش کدبیس (CKG)، اسکیل `phase0-omni-audit` و ویکی خودنگهدار
- **وضعیت:** پذیرفته‌شده (Accepted)
- **ماتریس ابزارهای یکپارچه‌شده در اسکیل `.agents/skills/phase0-omni-audit`:**
  - **ایندکس گراف کد (`00-index.sh`):** ترکیب **`codebase-memory-mcp (CBM)`** (۱۶۲ زبان + Cypher + نمای کهکشانی `CBM Lens`)، **`CodeGraph`** (موتور Rust + SQLite FTS5 با کاهش ۵۹٪ توکن)، **`Graphify`** (دوگذره کد و اسناد با کاهش ۹۰–۹۵٪ توکن و برچسب‌های اطمینان `EXTRACTED/INFERRED/AMBIGUOUS`) و **`rgctl`** (بیت‌ست‌های تنک شعاع انفجار زیر ۱ms).
  - **ویکی خودنگهدار و ضدتوهم (`01-wiki-compile.sh`):** ترکیب **`llm-wiki-compiler` / `pi-codebase-wiki` / `Klore`** با دروازه ممیزی گراف **`doc0`** (چک کردن تمام نام توابع/کلاس‌های داخل متن ویکی با گراف AST) و دیمن‌های پس‌زمینه **`CodeAlmanac`** (`Sync` هر ۵ ساعت روی لاگ‌های JSONL و `Garden` هر ۲۴ ساعت).
<!-- ZONE:HUMAN_INTUITION_END -->
<!-- ZONE:CONTRACT_START -->
- Project: `F1uxus` | Ontology: `ONT_F1UXUS_ADR_0009_CODE_KNOWLEDGE_GRAPH_ENGINES` | Thread: `THR_F1UXUS_0009_CODE_KNOWLEDGE_GRAPH_ENGIN`
<!-- ZONE:CONTRACT_END -->
<!-- ZONE:EXECUTION_CORE_START -->
```python
ONT_ID = "ONT_F1UXUS_ADR_0009_CODE_KNOWLEDGE_GRAPH_ENGINES"
SOURCE_REF = "initdb/01_schema.sql"
```
<!-- ZONE:EXECUTION_CORE_END -->
<!-- ZONE:WORKSHEET_START -->
## تمرین ۱۰ دقیقه‌ای (F1uxus)
1. معماری و قرارداد `ONT_F1UXUS_ADR_0009_CODE_KNOWLEDGE_GRAPH_ENGINES` در `F1uxus` چگونه راستی‌آزمایی می‌شود؟
<details data-f1-thread="THR_F1UXUS_0009_CODE_KNOWLEDGE_GRAPH_ENGIN"><summary>ThreadBox THR_F1UXUS_0009_CODE_KNOWLEDGE_GRAPH_ENGIN</summary></details>
<!-- ZONE:WORKSHEET_END -->
