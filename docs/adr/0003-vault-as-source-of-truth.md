---
ont_id: ONT_F1UXUS_ADR_0003_VAULT_AS_SOURCE_OF_TRUTH
source_project: F1uxus
domain: adr
title_fa: "ADR-0003: خزانه فایل‌های متنی در Git به عنوان تنها مرجع حقیقت (Vault as Source of Truth)"
content_is_data: true
---
<!-- ZONE:HUMAN_INTUITION_START -->
# ADR-0003: خزانه فایل‌های متنی در Git به عنوان تنها مرجع حقیقت (Vault as Source of Truth)
- **وضعیت:** پذیرفته‌شده (Accepted)
- **زمینه و مسئله:** ذخیره مستقیم دانش، چت‌ها و قوانین در دیتابیس‌های باینری باعث ایجاد «حالت پنهان» (Hidden State)، عدم امکان `git diff` و ریسک فساد داده می‌شود.
- **گزینه‌های بررسی‌شده:** ۱) دیتابیس‌محور (Database-First)، ۲) فایل‌محور با ایندکس مشتق‌شده (Vault-First + Rebuildable Derived Index).
- **تصمیم نهایی:** تمامی موجودیت‌ها (`notebook/ontology/ONT_*.md`)، مستطیل‌های چت (`notebook/threads/*.jsonl`)، ادعاها و پلی‌بوک‌ها در فایل‌های متنی داخل Git نگهداری می‌شوند. دیتابیس‌های `SQLite` و `PostgreSQL/pgvector` صرفاً نماهای مشتق‌شده هستند که هر لحظه می‌توان آن‌ها را پاک کرد و از روی فایل‌های Git بازسازی نمود. مدل هوش مصنوعی فقط پیشنهاد ساختاریافته (`Pydantic`) می‌دهد و کد قطعی پایتون در خزانه می‌نویسد.
<!-- ZONE:HUMAN_INTUITION_END -->
<!-- ZONE:CONTRACT_START -->
- Project: `F1uxus` | Ontology: `ONT_F1UXUS_ADR_0003_VAULT_AS_SOURCE_OF_TRUTH` | Thread: `THR_F1UXUS_0003_VAULT_AS_SOURCE_OF_TRUTH`
<!-- ZONE:CONTRACT_END -->
<!-- ZONE:EXECUTION_CORE_START -->
```python
ONT_ID = "ONT_F1UXUS_ADR_0003_VAULT_AS_SOURCE_OF_TRUTH"
SOURCE_REF = "initdb/01_schema.sql"
```
<!-- ZONE:EXECUTION_CORE_END -->
<!-- ZONE:WORKSHEET_START -->
## تمرین ۱۰ دقیقه‌ای (F1uxus)
1. معماری و قرارداد `ONT_F1UXUS_ADR_0003_VAULT_AS_SOURCE_OF_TRUTH` در `F1uxus` چگونه راستی‌آزمایی می‌شود؟
<details data-f1-thread="THR_F1UXUS_0003_VAULT_AS_SOURCE_OF_TRUTH"><summary>ThreadBox THR_F1UXUS_0003_VAULT_AS_SOURCE_OF_TRUTH</summary></details>
<!-- ZONE:WORKSHEET_END -->
