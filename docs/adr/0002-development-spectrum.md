---
ont_id: ONT_F1UXUS_ADR_0002_DEVELOPMENT_SPECTRUM
source_project: F1uxus
domain: adr
title_fa: "ADR-0002: مدل طیف توسعه ۸ حالته (Development Spectrum H0–A2) با دروازه کیفیت ناوردا"
content_is_data: true
---
<!-- ZONE:HUMAN_INTUITION_START -->
# ADR-0002: مدل طیف توسعه ۸ حالته (Development Spectrum H0–A2) با دروازه کیفیت ناوردا
- **وضعیت:** پذیرفته‌شده (Accepted)
- **زمینه و مسئله:** توسعه‌دهنده در شرایط مختلف (آفلاین بدون اینترنت، زمان یادگیری عمیق مفاهیم جدید، یا زمان تولید سریع کدهای تکراری) به سطوح متفاوتی از مداخله هوش مصنوعی نیاز دارد، اما خروجی نهایی نباید دچار ناهماهنگی کیفی شود.
- **گزینه‌های تصمیم‌گیری (۸ تراک طیف توسعه):**
  - `H0` (انسان کاملاً آفلاین با `offline-kit.fa.md`) | `H1` (انسان + مستندات وب) | `H2` (انسان + مربی سقراطی `--tutor`) | `H3` (انسان کدنویس + بازبین هوش مصنوعی `--review`)
  - `C1` (چت‌بات وب با `pack` و `apply`) | `A1` (هم‌برنامه‌نویسی با ایجنت تعاملی) | `A2` (ایجنت خودمختار) | `MIX` (تغییر تراک در مرز هر تسک بر اساس برچسب `Learning-Value`).
- **تصمیم نهایی:** آزادی کامل در انتخاب تراک برای هر تسک، به شرط عبور اجباری از **دروازه دوگانه ناوردا (`devloop.py gate` و `verify`)**.
<!-- ZONE:HUMAN_INTUITION_END -->
<!-- ZONE:CONTRACT_START -->
- Project: `F1uxus` | Ontology: `ONT_F1UXUS_ADR_0002_DEVELOPMENT_SPECTRUM` | Thread: `THR_F1UXUS_0002_DEVELOPMENT_SPECTRUM`
<!-- ZONE:CONTRACT_END -->
<!-- ZONE:EXECUTION_CORE_START -->
```python
ONT_ID = "ONT_F1UXUS_ADR_0002_DEVELOPMENT_SPECTRUM"
SOURCE_REF = "initdb/01_schema.sql"
```
<!-- ZONE:EXECUTION_CORE_END -->
<!-- ZONE:WORKSHEET_START -->
## تمرین ۱۰ دقیقه‌ای (F1uxus)
1. معماری و قرارداد `ONT_F1UXUS_ADR_0002_DEVELOPMENT_SPECTRUM` در `F1uxus` چگونه راستی‌آزمایی می‌شود؟
<details data-f1-thread="THR_F1UXUS_0002_DEVELOPMENT_SPECTRUM"><summary>ThreadBox THR_F1UXUS_0002_DEVELOPMENT_SPECTRUM</summary></details>
<!-- ZONE:WORKSHEET_END -->
