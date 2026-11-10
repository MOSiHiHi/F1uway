---
ont_id: ONT_F1UXUS_ADR_0010_VISUALIZATION_AND_BIDI_UI
source_project: F1uxus
domain: adr
title_fa: "ADR-0010: معماری استودیوی بصری، داشبورد BiDi/فارسی و کامپوننت‌های تعاملی"
content_is_data: true
---
<!-- ZONE:HUMAN_INTUITION_START -->
# ADR-0010: معماری استودیوی بصری، داشبورد BiDi/فارسی و کامپوننت‌های تعاملی
- **وضعیت:** پذیرفته‌شده (Accepted)
- **ماتریس انتخاب موتور رندر بر اساس نوع نما:**
  1. **گراف‌های تعاملی فارسی، مستطیل‌های چت (`ThreadBox DAG`) و نقشه درس:** **`React Flow (@xyflow/react)`** یا کارت‌های DOM استاندارد HTML/SVG؛ زیرا هر گره یک عنصر کامل DOM است و الگوریتم دوجهته یونیکد (`dir="rtl"`, `unicode-bidi: plaintext / isolate`) و اتصال حروف فارسی را بدون نقص رندر می‌کند.
  2. **نماهای سه‌بعدی شهر کد و کهکشان (`CodeCharta` / `CBM Lens`):** **`Three.js` با لایه برچسب‌های `HTML Overlay`**.
  3. **گراف‌های عظیم بالای ۱۰,۰۰۰ گره:** **`Sigma.js v4` (WebGL) + `Graphology` (`ForceAtlas2` روی WebWorker)**.
  4. **دیاگرام‌های داستان‌گو و بوم فایل:** **`Archify v3.2 Explainer`** + **`CodeFlow`** + **`Understand-Anything`** در پوسته پنجره‌های داک‌شونده **`Dockview`**.
<!-- ZONE:HUMAN_INTUITION_END -->
<!-- ZONE:CONTRACT_START -->
- Project: `F1uxus` | Ontology: `ONT_F1UXUS_ADR_0010_VISUALIZATION_AND_BIDI_UI` | Thread: `THR_F1UXUS_0010_VISUALIZATION_AND_BIDI_UI`
<!-- ZONE:CONTRACT_END -->
<!-- ZONE:EXECUTION_CORE_START -->
```python
ONT_ID = "ONT_F1UXUS_ADR_0010_VISUALIZATION_AND_BIDI_UI"
SOURCE_REF = "initdb/01_schema.sql"
```
<!-- ZONE:EXECUTION_CORE_END -->
<!-- ZONE:WORKSHEET_START -->
## تمرین ۱۰ دقیقه‌ای (F1uxus)
1. معماری و قرارداد `ONT_F1UXUS_ADR_0010_VISUALIZATION_AND_BIDI_UI` در `F1uxus` چگونه راستی‌آزمایی می‌شود؟
<details data-f1-thread="THR_F1UXUS_0010_VISUALIZATION_AND_BIDI_UI"><summary>ThreadBox THR_F1UXUS_0010_VISUALIZATION_AND_BIDI_UI</summary></details>
<!-- ZONE:WORKSHEET_END -->
