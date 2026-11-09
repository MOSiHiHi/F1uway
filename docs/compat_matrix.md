# ماتریس سازگاری نسخه‌ها (`docs/compat_matrix.md`)

| مؤلفه | نسخه استاندارد قفل‌شده | نقش در سیستم |
| :--- | :--- | :--- |
| **Python** | `>=3.11, <3.13` (مرجع: `3.12`) | زبان هسته، موتورهای ریاضی و اسکریپت‌های اتوماسیون |
| **Pydantic** | `v2.6+` (با شیم سازگاری دوگانه `v1/v2` در `F1BaseModel`) | قراردادهای داده تغییرناپذیر (`extra="forbid", frozen=True`) |
| **PostgreSQL + pgvector** | `PostgreSQL 16.15` + `pgvector 0.8.7` | ذخیره‌ساز برداری HNSW، جستجوی متنی GIN و پیمایش `Recursive CTE` |
| **SQLite** | `3.40+` (مجهز به `FTS5 unicode61`) | ایندکس سایه هستی‌شناسی (`shadow_index.sqlite`) و رادار ابزار (`kg.sqlite`) |
| **IBM Docling / Hazm** | `docling==2.140.0` / `hazm==0.12.1` | کالبدشکافی ساختار PDF/جداول و پردازش زبان طبیعی فارسی |
