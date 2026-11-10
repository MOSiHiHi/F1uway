---
ont_id: ONT_F1UXUS_ADR_0004_BITEMPORAL_KNOWLEDGE_MODEL
source_project: F1uxus
domain: adr
title_fa: "ADR-0004: مدل حافظه دو-زمانی (Bitemporality) و ابطال غیرمخرب حقایق"
content_is_data: true
---
<!-- ZONE:HUMAN_INTUITION_START -->
# ADR-0004: مدل حافظه دو-زمانی (Bitemporality) و ابطال غیرمخرب حقایق
- **وضعیت:** پذیرفته‌شده (Accepted)
- **زمینه و مسئله:** در گراف‌های دانش معمولی، وقتی یک واقعیت در دنیای واقعی تغییر می‌کند (مثلاً انتشار نسخه جدید یک کتابخانه یا نقض یک فرضیه)، یا یال قبلی پاک می‌شود (از دست رفتن تاریخچه) و یا دو یال متناقض هم‌زمان فعال می‌مانند (توهم عامل).
- **تصمیم نهایی:** به پیروی از معماری `F1uxus` و `Graphiti/Zep`، سیستم دو محور زمان را تفکیک می‌کند: ۱) **زمان تراکنش (`created_at` / Git Commit Time)** و ۲) **بازه اعتبار واقعی (`valid_at` و `invalid_at`)**. هنگام ورود حقیقت جدید که ناقض حقیقت قبلی است، یال قدیم حذف نمی‌شود بلکه مقدار `invalid_at` گرفته و فیلد `superseded_by` آن به شناسه جدید اشاره می‌کند.
<!-- ZONE:HUMAN_INTUITION_END -->
<!-- ZONE:CONTRACT_START -->
- Project: `F1uxus` | Ontology: `ONT_F1UXUS_ADR_0004_BITEMPORAL_KNOWLEDGE_MODEL` | Thread: `THR_F1UXUS_0004_BITEMPORAL_KNOWLEDGE_MODEL`
<!-- ZONE:CONTRACT_END -->
<!-- ZONE:EXECUTION_CORE_START -->
```python
ONT_ID = "ONT_F1UXUS_ADR_0004_BITEMPORAL_KNOWLEDGE_MODEL"
SOURCE_REF = "initdb/01_schema.sql"
```
<!-- ZONE:EXECUTION_CORE_END -->
<!-- ZONE:WORKSHEET_START -->
## تمرین ۱۰ دقیقه‌ای (F1uxus)
1. معماری و قرارداد `ONT_F1UXUS_ADR_0004_BITEMPORAL_KNOWLEDGE_MODEL` در `F1uxus` چگونه راستی‌آزمایی می‌شود؟
<details data-f1-thread="THR_F1UXUS_0004_BITEMPORAL_KNOWLEDGE_MODEL"><summary>ThreadBox THR_F1UXUS_0004_BITEMPORAL_KNOWLEDGE_MODEL</summary></details>
<!-- ZONE:WORKSHEET_END -->
