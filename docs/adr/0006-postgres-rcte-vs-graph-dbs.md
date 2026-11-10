---
ont_id: ONT_F1UXUS_ADR_0006_POSTGRES_RCTE_VS_GRAPH_DBS
source_project: F1uxus
domain: adr
title_fa: "ADR-0006: انتخاب موتور ذخیره‌سازی گراف و بردار (PostgreSQL RCTE و SQLite در برابر Apache AGE / Neo4j / Kuzu)"
content_is_data: true
---
<!-- ZONE:HUMAN_INTUITION_START -->
# ADR-0006: انتخاب موتور ذخیره‌سازی گراف و بردار (PostgreSQL RCTE و SQLite در برابر Apache AGE / Neo4j / Kuzu)
- **وضعیت:** پذیرفته‌شده (Accepted)
- **گزینه‌های بررسی‌شده و بنچمارک‌ها:**
  1. **PostgreSQL 16 + `pgvector` (HNSW) + `tsvector` (GIN) + `Recursive CTE` (انتخاب پروفایل سنگین):** توان عملیاتی **۹,۱۶۹ درخواست بر ثانیه** و تأخیر صدک ۹۵ برابر با **۱.۴ میلی‌ثانیه** در پیمایش ۱ تا ۲ گامی؛ تجمیع کامل بردار، متن و گراف در یک کانتینر واحد.
  2. **SQLite + `FTS5 (unicode61)` (انتخاب پروفایل سبک و بدون سرور):** استفاده در `kg.sqlite` و `.omni-audit/shadow_index.sqlite` بدون نیاز به اجرای دیمن دیتابیس.
  3. **ArcadeDB Embedded (جایگزین Kuzu):** تنها دیتابیس گراف-برداری توکار با مجوز Apache 2.0 پس از بایگانی شدن مخزن `Kuzu` در اکتبر ۲۰۲۵.
  4. **Apache AGE روی Postgres (رد شده):** سربار ۲۹۰ برابری پارسر `cypher()` (سقوط توان عملیاتی به ۱۵۹ req/s) و باگ ۱۷ ساعته `get_all_edges` در گراف‌های بزرگ.
<!-- ZONE:HUMAN_INTUITION_END -->
<!-- ZONE:CONTRACT_START -->
- Project: `F1uxus` | Ontology: `ONT_F1UXUS_ADR_0006_POSTGRES_RCTE_VS_GRAPH_DBS` | Thread: `THR_F1UXUS_0006_POSTGRES_RCTE_VS_GRAPH_DBS`
<!-- ZONE:CONTRACT_END -->
<!-- ZONE:EXECUTION_CORE_START -->
```python
ONT_ID = "ONT_F1UXUS_ADR_0006_POSTGRES_RCTE_VS_GRAPH_DBS"
SOURCE_REF = "initdb/01_schema.sql"
```
<!-- ZONE:EXECUTION_CORE_END -->
<!-- ZONE:WORKSHEET_START -->
## تمرین ۱۰ دقیقه‌ای (F1uxus)
1. معماری و قرارداد `ONT_F1UXUS_ADR_0006_POSTGRES_RCTE_VS_GRAPH_DBS` در `F1uxus` چگونه راستی‌آزمایی می‌شود؟
<details data-f1-thread="THR_F1UXUS_0006_POSTGRES_RCTE_VS_GRAPH_DBS"><summary>ThreadBox THR_F1UXUS_0006_POSTGRES_RCTE_VS_GRAPH_DBS</summary></details>
<!-- ZONE:WORKSHEET_END -->
