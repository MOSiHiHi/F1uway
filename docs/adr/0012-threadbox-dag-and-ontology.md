# ADR-0012: معماری گراف مستطیل‌های چت (`ThreadBox DAG`)، درونی‌سازی هستی‌شناختی ضدتکرار و ۴ جهان موازی
- **وضعیت:** پذیرفته‌شده (Accepted)
- **تصمیم معماری:**
  1. هر نشست کاری یا آموزشی به صورت گراف جهت‌دار غیرمدور از مستطیل‌های `ThreadBox` و گره‌های `TurnNode` در `notebook/threads/THR_*.jsonl` ثبت می‌شود.
  2. هر انشعاب روی عبارت $X$ ابتدا از قلاب `OntologyRegistry.intercept_branch_spawn` عبور می‌کند تا در صورت وجود در هستی‌شناسی، با **۰ توکن (`ZERO_TOKEN_HIT`)** یا به صورت تفاضلی (`DELTA_PROMPT_MODE`) پاسخ داده شود.
  3. چهار مکانیسم از جهان‌های موازی در هسته تعبیه شده‌اند: جاسازی دوطرفه کد (`<!-- EMBED: ... -->` از *Literate Programming*)، هش ساختاری AST (`compute_python_ast_hash` از *Unison*)، ایندکس سایه SQLite (`.omni-audit/shadow_index.sqlite` از *Datomic*) و چیدمان الفبایی پیشوند پرامپت (از *RadixAttention*).
