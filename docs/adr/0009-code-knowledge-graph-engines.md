# ADR-0009: موتورهای گراف دانش کدبیس (CKG)، اسکیل `phase0-omni-audit` و ویکی خودنگهدار
- **وضعیت:** پذیرفته‌شده (Accepted)
- **ماتریس ابزارهای یکپارچه‌شده در اسکیل `.agents/skills/phase0-omni-audit`:**
  - **ایندکس گراف کد (`00-index.sh`):** ترکیب **`codebase-memory-mcp (CBM)`** (۱۶۲ زبان + Cypher + نمای کهکشانی `CBM Lens`)، **`CodeGraph`** (موتور Rust + SQLite FTS5 با کاهش ۵۹٪ توکن)، **`Graphify`** (دوگذره کد و اسناد با کاهش ۹۰–۹۵٪ توکن و برچسب‌های اطمینان `EXTRACTED/INFERRED/AMBIGUOUS`) و **`rgctl`** (بیت‌ست‌های تنک شعاع انفجار زیر ۱ms).
  - **ویکی خودنگهدار و ضدتوهم (`01-wiki-compile.sh`):** ترکیب **`llm-wiki-compiler` / `pi-codebase-wiki` / `Klore`** با دروازه ممیزی گراف **`doc0`** (چک کردن تمام نام توابع/کلاس‌های داخل متن ویکی با گراف AST) و دیمن‌های پس‌زمینه **`CodeAlmanac`** (`Sync` هر ۵ ساعت روی لاگ‌های JSONL و `Garden` هر ۲۴ ساعت).
