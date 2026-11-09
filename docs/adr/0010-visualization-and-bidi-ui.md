# ADR-0010: معماری استودیوی بصری، داشبورد BiDi/فارسی و کامپوننت‌های تعاملی
- **وضعیت:** پذیرفته‌شده (Accepted)
- **ماتریس انتخاب موتور رندر بر اساس نوع نما:**
  1. **گراف‌های تعاملی فارسی، مستطیل‌های چت (`ThreadBox DAG`) و نقشه درس:** **`React Flow (@xyflow/react)`** یا کارت‌های DOM استاندارد HTML/SVG؛ زیرا هر گره یک عنصر کامل DOM است و الگوریتم دوجهته یونیکد (`dir="rtl"`, `unicode-bidi: plaintext / isolate`) و اتصال حروف فارسی را بدون نقص رندر می‌کند.
  2. **نماهای سه‌بعدی شهر کد و کهکشان (`CodeCharta` / `CBM Lens`):** **`Three.js` با لایه برچسب‌های `HTML Overlay`**.
  3. **گراف‌های عظیم بالای ۱۰,۰۰۰ گره:** **`Sigma.js v4` (WebGL) + `Graphology` (`ForceAtlas2` روی WebWorker)**.
  4. **دیاگرام‌های داستان‌گو و بوم فایل:** **`Archify v3.2 Explainer`** + **`CodeFlow`** + **`Understand-Anything`** در پوسته پنجره‌های داک‌شونده **`Dockview`**.
