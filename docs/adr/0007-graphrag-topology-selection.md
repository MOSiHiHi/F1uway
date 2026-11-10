---
ont_id: ONT_F1UXUS_ADR_0007_GRAPHRAG_TOPOLOGY_SELECTION
source_project: F1uxus
domain: adr
title_fa: "ADR-0007: انتخاب توپولوژی GraphRAG و بازیابی ترکیبی سه‌وجهی"
content_is_data: true
---
<!-- ZONE:HUMAN_INTUITION_START -->
# ADR-0007: انتخاب توپولوژی GraphRAG و بازیابی ترکیبی سه‌وجهی
- **وضعیت:** پذیرفته‌شده (Accepted)
- **ماتریس گزینه‌های معماری:**
  - **پایه استخراج و درج افزایشی:** الگوی **`LightRAG` + `EdgeQuake`** (محدود کردن موجودیت‌ها به ۷ نوع پایه `PERSON, ORG, LOCATION, CONCEPT, EVENT, TECH, PRODUCT` + نرمال‌سازی `UPPERCASE_UNDERSCORE` که تکرار گره‌ها را ۴۰٪ کاهش می‌دهد + حلقه بازپرسش `Gleaning` که Recall موجودیت را ۲۵٪ بالا می‌برد).
  - **خوشه‌بندی گراف:** ترکیب الگوریتم **لیدن (`Leiden`)** با **تجزیه خطی $k$-هسته (`k-core Decomposition`)** برای جلوگیری از پدیده تباهی نمایی ماژولاریتی روی گراف‌های پراکنده.
  - **بازیابی هیبریدی:** ترکیب بردار متراکم و وزن واژگانی **`BAAI/bge-m3`** (یا `SPLADE++` با `DF-FLOPS` + تعامل دیرهنگام `ColBERTv2/PLAID`) از طریق فرمول **`RRF (k=60)`**.
<!-- ZONE:HUMAN_INTUITION_END -->
<!-- ZONE:CONTRACT_START -->
- Project: `F1uxus` | Ontology: `ONT_F1UXUS_ADR_0007_GRAPHRAG_TOPOLOGY_SELECTION` | Thread: `THR_F1UXUS_0007_GRAPHRAG_TOPOLOGY_SELECTIO`
<!-- ZONE:CONTRACT_END -->
<!-- ZONE:EXECUTION_CORE_START -->
```python
ONT_ID = "ONT_F1UXUS_ADR_0007_GRAPHRAG_TOPOLOGY_SELECTION"
SOURCE_REF = "initdb/01_schema.sql"
```
<!-- ZONE:EXECUTION_CORE_END -->
<!-- ZONE:WORKSHEET_START -->
## تمرین ۱۰ دقیقه‌ای (F1uxus)
1. معماری و قرارداد `ONT_F1UXUS_ADR_0007_GRAPHRAG_TOPOLOGY_SELECTION` در `F1uxus` چگونه راستی‌آزمایی می‌شود؟
<details data-f1-thread="THR_F1UXUS_0007_GRAPHRAG_TOPOLOGY_SELECTIO"><summary>ThreadBox THR_F1UXUS_0007_GRAPHRAG_TOPOLOGY_SELECTIO</summary></details>
<!-- ZONE:WORKSHEET_END -->
