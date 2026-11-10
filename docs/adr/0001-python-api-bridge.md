---
ont_id: ONT_F1UXUS_ADR_0001_PYTHON_API_BRIDGE
source_project: F1uxus
domain: adr
title_fa: "ADR-0001: پل ارتباطی محلی پایتون (FastAPI + CLI) به رابط کاربری وب (Next.js / Static SPA)"
content_is_data: true
---
<!-- ZONE:HUMAN_INTUITION_START -->
# ADR-0001: پل ارتباطی محلی پایتون (FastAPI + CLI) به رابط کاربری وب (Next.js / Static SPA)
- **وضعیت:** پذیرفته‌شده (Accepted)
- **زمینه و مسئله:** موتورهای محاسباتی یادگیری (`FSRS-6`, `BKT`)، پارسینگ اسناد (`IBM Docling`), پردازش زبان فارسی (`Hazm`) و مدل‌های هوش مصنوعی (`PyTorch`, `BGE-M3`, `Pydantic`) در اکوسیستم پایتون قرار دارند، در حالی که داشبورد تعاملی (`React Flow`, `Dockview`, `D3/Cytoscape`) در مرورگر اجرا می‌شود.
- **گزینه‌های بررسی‌شده (Decision Options Matrix):**
  1. **گزینه A (Static File Bridge — پروفایل سبک و GitHub Pages):** اسکریپت‌های پایتون (`devloop.py`, `export_dashboard.py`) خروجی‌ها را به فایل‌های JSON/Markdown کامپایل می‌کنند و `site/index.html` بدون نیاز به سرور آن‌ها را رندر می‌کند.
  2. **گزینه B (FastAPI + SSE Local Bridge — پروفایل تعاملی زنده):** سرور `src/f1uway/server/main.py` روی پورت محلی بالا می‌آید و رویدادهای انشعاب مستطیل‌های چت و استنتاج عامل را با `Server-Sent Events (SSE)` به UI استریم می‌کند.
  3. **گزینه C (Pyodide / WebAssembly):** اجرای پایتون داخل مرورگر (رد شده به دلیل عدم پشتیبانی از `PyTorch`/`Docling` و محدودیت حافظه).
- **تصمیم نهایی:** پشتیبانی دوگانه از **گزینه A** (برای انتشار رایگان و بدون سرور روی GitHub Pages مشابه `MJNexus`) و **گزینه B** (برای نشست‌های تعاملی زنده با عامل‌ها مشابه `F1uent-Ecosystem`).
<!-- ZONE:HUMAN_INTUITION_END -->
<!-- ZONE:CONTRACT_START -->
- Project: `F1uxus` | Ontology: `ONT_F1UXUS_ADR_0001_PYTHON_API_BRIDGE` | Thread: `THR_F1UXUS_0001_PYTHON_API_BRIDGE`
<!-- ZONE:CONTRACT_END -->
<!-- ZONE:EXECUTION_CORE_START -->
```python
ONT_ID = "ONT_F1UXUS_ADR_0001_PYTHON_API_BRIDGE"
SOURCE_REF = "initdb/01_schema.sql"
```
<!-- ZONE:EXECUTION_CORE_END -->
<!-- ZONE:WORKSHEET_START -->
## تمرین ۱۰ دقیقه‌ای (F1uxus)
1. معماری و قرارداد `ONT_F1UXUS_ADR_0001_PYTHON_API_BRIDGE` در `F1uxus` چگونه راستی‌آزمایی می‌شود؟
<details data-f1-thread="THR_F1UXUS_0001_PYTHON_API_BRIDGE"><summary>ThreadBox THR_F1UXUS_0001_PYTHON_API_BRIDGE</summary></details>
<!-- ZONE:WORKSHEET_END -->
