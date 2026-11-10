---
ont_id: ONT_F1UXUS_ADR_0008_OCR_AND_DOCUMENT_INGESTION
source_project: F1uxus
domain: adr
title_fa: "ADR-0008: خط لوله هوشمندی اسناد، اعتبارسنجی منشأ و مسیریاب دوطبقه OCR فارسی"
content_is_data: true
---
<!-- ZONE:HUMAN_INTUITION_START -->
# ADR-0008: خط لوله هوشمندی اسناد، اعتبارسنجی منشأ و مسیریاب دوطبقه OCR فارسی
- **وضعیت:** پذیرفته‌شده (Accepted)
- **گزینه‌های تصمیم‌گیری در خط لوله اسناد:**
  1. **تأیید موجودیت و یکتایی سند:** استخراج هدر `TEI XML` با **`GROBID`** + تطبیق شناسه در **`OpenAlex API`** و **`Crossref`** + بررسی گواهی **`C2PA`** و اثرانگشت ۶۴ بیتی **`SimHash`**.
  2. **کالبدشکافی ساختار صفحه و جداول:** **`IBM Docling v2.140`** (`DocLayNet` + `TableFormer` در حالت `ACCURATE` با مجوز MIT) به عنوان پیش‌فرض؛ **`MinerU 2.5`** (امتیاز ۹۵.۷۵٪ در OmniDocBench v1.6) برای مقالات سنگین ریاضی؛ **`PaddleOCR-VL-1.6`** برای تصاویر خمیده و دوربین.
  3. **مسیریاب دوطبقه OCR فارسی:** مسیر اول (متون چاپی تمیز روی CPU محلی): `RapidOCR (Arabic PP-OCRv5)` یا `Tesseract 5.5.3` (و در ابر `Gemini 2.5 Flash Lite`)؛ مسیر دوم (جداول متراکم و دست‌خط فارسی): `Gemini 3.8 Flash` در ابر یا مدل‌های آفلاین `Gemma 4 (31B)` / `Qwen 3.6 (35B)` روی GPU ۲۴ گیگابایتی (با منع اکید استفاده از DeepSeek روی دست‌خط ناخوانا به دلیل توهم‌زایی).
<!-- ZONE:HUMAN_INTUITION_END -->
<!-- ZONE:CONTRACT_START -->
- Project: `F1uxus` | Ontology: `ONT_F1UXUS_ADR_0008_OCR_AND_DOCUMENT_INGESTION` | Thread: `THR_F1UXUS_0008_OCR_AND_DOCUMENT_INGESTION`
<!-- ZONE:CONTRACT_END -->
<!-- ZONE:EXECUTION_CORE_START -->
```python
ONT_ID = "ONT_F1UXUS_ADR_0008_OCR_AND_DOCUMENT_INGESTION"
SOURCE_REF = "initdb/01_schema.sql"
```
<!-- ZONE:EXECUTION_CORE_END -->
<!-- ZONE:WORKSHEET_START -->
## تمرین ۱۰ دقیقه‌ای (F1uxus)
1. معماری و قرارداد `ONT_F1UXUS_ADR_0008_OCR_AND_DOCUMENT_INGESTION` در `F1uxus` چگونه راستی‌آزمایی می‌شود؟
<details data-f1-thread="THR_F1UXUS_0008_OCR_AND_DOCUMENT_INGESTION"><summary>ThreadBox THR_F1UXUS_0008_OCR_AND_DOCUMENT_INGESTION</summary></details>
<!-- ZONE:WORKSHEET_END -->
