---
ont_id: ONT_F1UXUS_ADR_0005_PERSIAN_BIDI_OFFSET_MAPPING
source_project: F1uxus
domain: adr
title_fa: "ADR-0005: لایه نرمال‌سازی متن فارسی/دواتجاهی با حفظ جدول نگاشت افست کاراکتری"
content_is_data: true
---
<!-- ZONE:HUMAN_INTUITION_START -->
# ADR-0005: لایه نرمال‌سازی متن فارسی/دواتجاهی با حفظ جدول نگاشت افست کاراکتری
- **وضعیت:** پذیرفته‌شده (Accepted)
- **زمینه و مسئله:** نرمال‌سازی متون فارسی (تبدیل «ي/ك» عربی به «ی/ک» فارسی، حذف اعراب و تبدیل نیم‌فاصله `ZWNJ` یا کاراکترهای کنترلی BiDi) طول رشته را تغییر می‌دهد و باعث می‌شود بازه کاراکتری (`char_span`) استخراج‌شده توسط مدل دیگر با متن خام سند اصلی مطابقت نداشته باشد.
- **تصمیم نهایی:** پیاده‌سازی تابع `normalize_persian_with_offsets` در `src/f1uway/text_bidi.py` که به ازای هر کاراکتر در رشته نرمال‌شده، اندیس دقیق آن را در رشته خام اولیه درون آرایه `norm_to_raw_index` نگه می‌دارد و با متد `map_norm_span_to_raw` بازه‌ها را بدون خطا به سند اصلی برمی‌گرداند.
<!-- ZONE:HUMAN_INTUITION_END -->
<!-- ZONE:CONTRACT_START -->
- Project: `F1uxus` | Ontology: `ONT_F1UXUS_ADR_0005_PERSIAN_BIDI_OFFSET_MAPPING` | Thread: `THR_F1UXUS_0005_PERSIAN_BIDI_OFFSET_MAPPIN`
<!-- ZONE:CONTRACT_END -->
<!-- ZONE:EXECUTION_CORE_START -->
```python
ONT_ID = "ONT_F1UXUS_ADR_0005_PERSIAN_BIDI_OFFSET_MAPPING"
SOURCE_REF = "initdb/01_schema.sql"
```
<!-- ZONE:EXECUTION_CORE_END -->
<!-- ZONE:WORKSHEET_START -->
## تمرین ۱۰ دقیقه‌ای (F1uxus)
1. معماری و قرارداد `ONT_F1UXUS_ADR_0005_PERSIAN_BIDI_OFFSET_MAPPING` در `F1uxus` چگونه راستی‌آزمایی می‌شود؟
<details data-f1-thread="THR_F1UXUS_0005_PERSIAN_BIDI_OFFSET_MAPPIN"><summary>ThreadBox THR_F1UXUS_0005_PERSIAN_BIDI_OFFSET_MAPPIN</summary></details>
<!-- ZONE:WORKSHEET_END -->
