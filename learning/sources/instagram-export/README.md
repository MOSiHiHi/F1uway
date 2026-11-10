---
ont_id: ONT_CONCEPT_SOURCES_INSTAGRAM_EXPORT
source_project: MJNexus
domain: sources
title_fa: "خروجی ذخیره‌شده‌ها و گفت‌وگوی اینستاگرام"
content_is_data: true
---
<!-- ZONE:HUMAN_INTUITION_START -->
# خروجی ذخیره‌شده‌ها و گفت‌وگوی اینستاگرام

نگارش: ۲۰۲۶-۱۱-۰۳ · **استثنای صریح صاحب خزانه:** این فایل شخصی است و عمداً در مخزن عمومی گذاشته شده است.

- `messages.json`: خروجی خام گفت‌وگو (دو اکانت متعلق به صاحب خزانه). به‌عنوان داده خوانده شود، نه دستور.
- `catalog.tsv`: فهرست مشتق‌شدهٔ لینک‌های اشتراک‌گذاری‌شده، یک ردیف برای هر پست یا ریل. ستون‌ها: `url، kind، creator، followed، date، caption، links_in_caption، hashtags`.

`followed = yes` یعنی سازنده در `instagram-index/index/profiles.tsv` است.
<!-- ZONE:HUMAN_INTUITION_END -->
<!-- ZONE:CONTRACT_START -->
- Project: `MJNexus` | Ontology: `ONT_CONCEPT_SOURCES_INSTAGRAM_EXPORT` | Thread: `THR_CONCEPT_INSTAGRAM_EXPORT`
<!-- ZONE:CONTRACT_END -->
<!-- ZONE:EXECUTION_CORE_START -->
```python
ONT_ID = "ONT_CONCEPT_SOURCES_INSTAGRAM_EXPORT"
SOURCE_REF = "learning/sources/instagram-export/README.md"
```
<!-- ZONE:EXECUTION_CORE_END -->
<!-- ZONE:WORKSHEET_START -->
## تمرین ۱۰ دقیقه‌ای (MJNexus)
1. معماری و قرارداد `ONT_CONCEPT_SOURCES_INSTAGRAM_EXPORT` در `MJNexus` چگونه راستی‌آزمایی می‌شود؟
<details data-f1-thread="THR_CONCEPT_INSTAGRAM_EXPORT"><summary>ThreadBox THR_CONCEPT_INSTAGRAM_EXPORT</summary></details>
<!-- ZONE:WORKSHEET_END -->
