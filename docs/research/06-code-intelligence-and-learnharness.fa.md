# گزارش مهندسی اسکیل و هارنس \- Google Gemini

**Date**: November 6, 2026 at 12:48 AM
**Turns**: 1
**Source**: [Gemini Chat](https://gemini.google.com/u/1/app/e39a037d9035aa5d)

---

## Turn 1

### 👤 User

من این پرامپت رو دادم به ایجنت و این گزارش رو بهم داد که ذیل هردو رو می‌فرستم و ازت می‌خوام با همون پرامپت یه گزارش جامع‌تر و بهتر و حرفه‌ای‌تر و سودمندتر و پلندپروازانه‌تر و ایده‌آل‌تر و خلاقانه‌تر و اجرایی‌تر برام بنویسی.
پرامپت:
```md
# دستورکار جامع پژوهش عمیق (Master Deep Research Specification): مهندسی اسکیل هوش کدبیس (Code Intelligence Skill) و هارنس اختصاصی دومنظوره (درک کدبیس + یادگیری تعاملی با هوش مصنوعی) با داشبورد بصری BiDi/فارسی
## ۱. شرح مسئله، وضعیت فعلی پروژه و دو هدف کلان پژوهش
من یک پروژه نرم‌افزاری دارم که «فاز صفر» (Phase 0) آن را پیش برده‌ام و در حال حاضر دارای ساختار اولیه و کانتکست است. من به دنبال یک گزارش پژوهشی-مهندسی فوق‌العاده جامع، عمیق و بدون هیچ‌گونه حذفیات هستم که دانش، منابع، معماری و کدهای مرجع لازم را برای تحقق دو هدف پیوسته زیر فراهم کند:
طراحی و ساخت یک اسکیل استاندارد و بهینه (`.agents/skills/phase0-omni-audit`) که با اجرای یک دستور روی مخزن کد، زنجیره‌ای از بهترین ابزارهای تحلیل کدبیس را به صورت هماهنگ اجرا کند و خروجی‌های زیر را از جزئی‌ترین سطح (خط کد و AST) تا کلان‌ترین سطح (معماری و دامنه کسب‌وکار) تحویل دهد:
* گراف دانش قطعی و چندوجهی کدبیس (Code Knowledge Graph) و ردیابی وابستگی‌ها در کد و زیرساخت.
* استخراج آنتالوژی (Ontology) و مفاهیم دامنه کسب‌وکار.
* ویکی کدبیس خودنگهدار، قابل جست‌وجو و بدون توهم (Self-Maintaining Codebase Wiki).
* ریویو کد، ممیزی امنیتی (Security Audit)، بررسی کیفیت کد، شناسایی الگوها/ضدالگوها و نمره سلامت مخزن (Repo Health Grade).
* بررسی و قفل کردن مرزهای معماری (Mechanical Architecture Governance).
* داشبورد تعاملی و تصویرسازی غنی (Interactive Visualization Studio): خروجی‌ها نباید گزارش‌های متنی خشک و دم‌دستی باشند، بلکه باید شامل بوم‌های تعاملی (Interactive Canvas)، نماهای سه‌بعدی شهر/کهکشان کد، دیاگرام‌های داستان‌گوی گام‌به‌گام (Explainers) و تورهای تعاملی کدبیس باشند.
2. هدف دوم (نهایی — مهندسی و ساخت Harness اختصاصی دومنظوره: Code Intelligence + AI Learning):
پس از ساخت اسکیل و تست آن روی مخزن فاز صفر، می‌خواهیم از ترکیب بهترین روش‌ها، الگوریتم‌ها و کامپوننت‌های متن‌باز کشف‌شده، هارنس (Agent Harness) اختصاصی و پلتفرم وب/دسکتاپ Local-First خودمان را مهندسی کنیم. این هارنس باید به صورت هم‌زمان دو ماموریت را انجام دهد:
* ماموریت الف (مهندسی و هوش کدبیس): درک عمیق مخزن، مدیریت زمینه (Context)، کاهش مصرف توکن، اجرای ایجنت‌های کدنویسی در محیط ایزوله و حفظ سلامت معماری.
* ماموریت ب (یادگیری عمیق و مربی‌گری هوشمند با الهام مستقیم از `LearnHarness`): تبدیل کدبیسِ خودِ پروژه و مفاهیم مهندسی به یک محیط یادگیری تطبیقی، سقراطی و تعاملی که مرز دانش من را بسنجد، نقشه درس بسازد، گام‌به‌گام با مثال‌های واقعی از کدهای مخزن خودم آموزش دهد و میزان تسلط من را روی تک‌تک ماژول‌های کدبیس ردیابی کند.
* ماموریت ج (داشبورد تعاملی با پشتیبانی بومی از زبان فارسی و متون دوجهته BiDi / RTL): استفاده از بهترین کامپوننت‌های متن‌باز آماده برای ساخت رابط کاربری داشبورد که یا به صورت بومی از فارسی و BiDi/RTL پشتیبانی می‌کنند و یا معماری DOM/CSS آن‌ها امکان بهینه‌سازی بی‌نقص برای تایپوگرافی دوزبانه (فارسی/انگلیسی) را فراهم می‌سازد.
---
## ۲. قوانین سخت‌گیرانه و خط قرمزهای اجرای پژوهش (Strict Research Directives)
در تدوین طرح پژوهش (Research Plan) و نگارش گزارش نهایی، رعایت این ۶ قانون الزامی است:
2. خزش عمیق در تاپیک‌های گیت‌هاب (Topic Crawling): در تمام تاپیک‌های گیت‌هاب ذکرشده، علاوه بر ابزارهای نام‌برده، باید پروژه‌های مشابه، جایگزین‌ها، نرم‌افزارها، راهنماها (Awesome Lists / Guides)، فریم‌ورک‌ها، سرورهای MCP و اسکیل‌ها (`SKILL.md`) استخراج و مقایسه شوند.
3. تمرکز ویژه بر `LearnHarness` و ادغام آن با هوش کدبیس: معماری داخلی `amosblomqvist/learnharness` (نسخه 0.4.1 به بعد)، چرخه پداگوژیکی آن، ساختار گراف گزاره‌ها، نقص‌های فعلی آن (مانند Issue `#115`) و نحوه پیوند دادن آن با گراف AST کدبیس باید با جزئیات کامل مهندسی معکوس شود.
4. تمرکز بر تصویرسازی تعاملی (غیرخشک) و Codebase Wiki: ابزارهایی که صرفاً خروجی متنی خام یا نمودار ایستای ساده می‌دهند کافی نیستند؛ تمرکز باید بر ابزارهای دارای UI تعاملی، بوم‌های کد (Canvas)، نماهای سه‌بعدی، صفحات Explainer و ویکی‌های زنده دارای گراف دانش باشد.
5. مهندسی رابط کاربری BiDi / RTL و کامپوننت‌های آماده داشبورد: تمام کتابخانه‌ها و پروژه‌های متن‌باز که می‌توان کامپوننت‌های UI آن‌ها (گراف، بوم، پنل‌های داک‌شونده، ویکی‌خوان، داک‌های تمرین) را مستقیماً در داشبورد به کار برد، باید از نظر سازگاری با زبان فارسی، الگوریتم دوجهته یونیکد (BiDi) و تایپوگرافی دوزبانه (ترکیب فونت‌های انگلیسی نظیر `Space Grotesk`، `Unbounded` و `JetBrains Mono` با فونت‌های فارسی نظیر `IBM Plex Sans Arabic`، `Lalezar` و `Vazirmatn`) بررسی و بهینه‌سازی شوند.
6. خروجی در سطح Blueprint مهندسی: گزارش نهایی نباید کلی‌گویی باشد؛ بلکه باید شامل جداول مقایسه‌ای جامع، معماری دقیق اسکیل و هارنس، اسکیماهای داده، قوانین CSS/BiDi و نقشه راه پیاده‌سازی گام‌به‌گام باشد.
---
## ۳. لینک‌ها و منابع هسته‌ای که باید به طور کامل بررسی و کالبدشکافی شوند
### الف) لینک‌های اصلی تصویرسازی، گراف دانش و شهر کد:
### ب) لینک‌های اصلی یادگیری با هوش مصنوعی، تورهوشمند و هارنس:
### ج) فهرست کامل ۴۱ تاپیک گیت‌هاب که باید تمام مخازن مهم آن‌ها (نرم‌افزار، فریم‌ورک، راهنما، اسکیل) استخراج شوند:
2. `https://github.com/topics/code-visualization`
3. `https://github.com/topics/codebase-visualization`
4. `https://github.com/topics/code-mapping`
5. `https://github.com/topics/system-mapping`
6. `https://github.com/topics/repo-visualizer`
7. `https://github.com/topics/plan-visualizer`
8. `https://github.com/topics/architecture-diagram`
9. `https://github.com/topics/diagrams-as-code`
10. `https://github.com/topics/3d-map`
11. `https://github.com/topics/city-map`
12. `https://github.com/topics/fantasy-map`
13. `https://github.com/topics/graph-visualizer`
14. `https://github.com/topics/agent-context`
15. `https://github.com/topics/developer-tools`
16. `https://github.com/topics/code-intelligence`
17. `https://github.com/topics/system-intelligence`
18. `https://github.com/topics/code-knowledge-graph`
19. `https://github.com/topics/ontology-engineering`
20. `https://github.com/topics/ontology-management-framework`
21. `https://github.com/topics/context-engineering`
22. `https://github.com/topics/token-optimization`
23. `https://github.com/topics/persistent-memory`
24. `https://github.com/topics/code-memory`
25. `https://github.com/topics/impact-analysis`
26. `https://github.com/topics/model-context-protocol` (و `mcp-server`)
27. `https://github.com/topics/agent-harness`
28. `https://github.com/topics/agent-skills`
29. `https://github.com/topics/claude-code-skill`
30. `https://github.com/topics/claude-code-plugin`
31. `https://github.com/topics/codex-plugin`
32. `https://github.com/topics/gemini-cli-extension`
33. `https://github.com/topics/ai-coding-agent`
34. `https://github.com/topics/vibe-coding`
35. `https://github.com/topics/living-documentation`
36. `https://github.com/topics/ai-education`
37. `https://github.com/topics/ai-tutor`
38. `https://github.com/topics/interactive-learning`
39. `https://github.com/topics/learning-system`
40. `https://github.com/topics/spaced-repetition`
---
## ۴. بانک اطلاعات، جداول و یافته‌های مرجع از تعاملات قبلی (الزامی برای حفظ و بسط در پژوهش)
پژوهشگر باید تمام داده‌ها، ابزارها، مکانیسم‌ها و جداول زیر را به عنوان پایه دانش تاییدشده در طرح پژوهش و گزارش نهایی حفظ کرده و آن‌ها را با یافته‌های جدید تکمیل کند:
### جدول مرجع ۱: ابزارهای تصویرسازی تعاملی، بوم‌های کد و استعاره‌های فضایی سه‌بعدی
| نام ابزار / مخزن | تکنولوژی رندرینگ و الگوی بصری | مکانیسم‌ها و ویژگی‌های کلیدی که باید در گزارش بررسی و استخراج شوند |
| :--- | :--- | :--- |
| `tt-a1i/archify` (نسخه 3.2.0+) | کامپایل JSON تایپ‌شده به HTML مستقل، SVG, PNG, WebP, PDF, WebM؛ ۴ استایل (`clean`, `editorial`, `product`, `Swiss`) و پریست `signal-flow`. | ۱۰ نوع دیاگرام بومی (`Architecture`, `Workflow`, `Sequence`, `Dataflow`, `Lifecycle/State v2`, `ERD`, `Class/Interface`, `Tree`, `Timeline`, `Waterfall`)؛ معماری تک‌صفحه‌ای `explainer` (رویکرد Conclusion-First)؛ هایلایت دوطرفه گام‌های متنی و گره‌های دیاگرام (`Interactive Step-Walkthrough`)؛ کارت‌های شواهد پین‌شده به کامیت (`Commit-Pinned Source Cards`)؛ ردیابی مسیر و مرزهای اعتماد (`lanes`, `phases`)؛ دستور `patch explainer`؛ راهنمای `archify.mjs guide --json`؛ ۴ گیت اعتبارسنجی در `finalize` (`validate`, `deliver`, `strict check`, `real-browser browser-check` با سنجش `minimumProjectedTextPx`). |
| `Egonex-AI/Understand-Anything` | داشبورد وب تعاملی (`/understand-dashboard`) رنگ‌بندی‌شده بر اساس لایه‌های معماری با پشتیبانی چندزبانه (`--language`). | فلسفه «گراف‌هایی که آموزش می‌دهند نه صرفاً شگفت‌زده می‌کنند»؛ خط لوله ۷ ایجنت تخصصی: دستور `/understand` (شامل `project-scanner`، `file-analyzer` با ۵ کارگر موازی، `architecture-analyzer`، `tour-builder` برای ساخت تورهای یادگیری هدایت‌شده، و `graph-reviewer`)، دستور `/understand-domain` (ایجنت `domain-analyzer` برای نگاشت کد به فرآیندهای کسب‌وکار، Domains, Flows & Steps در گراف افقی)، و دستور `/understand-knowledge` (ایجنت `article-analyzer` برای استخراج موجودیت‌ها و ادعاها از مستندات و ویکی‌ها). |
| `braedonsaunders/codeflow` | تک‌فایل HTML بدون سرور و بدون Build در مرورگر (React 18 + D3 v7 از CDN)؛ آفلاین با Drag & Drop یا اتصال به GitHub API. | نمای کارت‌های کامل فایل روی بوم بی‌نهایت (`Full-File Cards on Canvas`) بدون نیاز به پرش بین تب‌ها؛ محاسبه شعاع انفجار (`Blast Radius`) برای فایل و Pull Request؛ تشخیص خودکار الگوها (`Singleton`, `Factory`, `Observer`, `React Custom Hooks`) و ضدالگوها (`God Objects`, `High Coupling`)؛ نمره سلامت مخزن (A تا F) بر اساس کدهای مرده و دورها؛ نقشه حرارتی تلاطم گیت (`Churn View`) و استخراج مالکیت واقعی در برابر `CODEOWNERS`؛ اسکنر امنیتی (کلیدهای هاردکدشده، SQLi، `eval()`) و تولید `.patch` برای حذف دستورات دیباگ؛ رسم گراف برای Markdown و `[[wiki-links]]`. |
| `DeusData/codebase-memory-mcp` + `CBM Lens` (و نسخه `win4r/codebase-memory-mcp-pro`) | هسته سرور به زبان C خالص + استودیوی بصری بومی سه‌بعدی CBM Lens (بدون نیاز به داکر). | پشتیبانی از ۱۵۸ زبان، رزولوشن نوع `Hybrid LSP` + `Tree-sitter`، ۱۷ ابزار MCP، ایندکس کرنل لینوکس (۲۸ میلیون خط کد) در ۳ دقیقه و پاسخ زیر ۱ میلی‌ثانیه؛ در CBM Lens: نمای کهکشانی سه‌بعدی (`3D Galaxy View`) با پالس‌های نوری روی یال‌ها (`Edge Pulses`) برای نمایش جریان فراخوانی چندگامی، سکوهای تودرتوی پوشه‌ها (`Nested Platforms`)، ارتفاع بلوک = حجم کد، جاذبه نقاط داغ = `Static Fan-In`؛ نمایش شکاف پوشش تست (`Coverage Gaps`) و `ADRs`؛ چت محلی با کد؛ ردیابی وابستگی در `Docker`, `K8s`, `Helm`, `Terraform`, `Ansible`, `SQL` و `CI`؛ پروفایل‌های `Scout / Verify / Auditor`. |
| `MaibornWolff/codecharta` | استعاره شهر سه‌بعدی نرم‌افزار (`3D Software City`) در Web Studio + CLI (`ccsh`) به زبان Kotlin و TypeScript. | ۱) نمای شهر سه‌بعدی متریک‌ها (`3D Metric City`): هر پوشه یک محله و هر فایل یک ساختمان (نگاشت دلخواه متریک‌ها به مساحت کف، ارتفاع و رنگ؛ مثلاً تشخیص فایل‌های بحرانی به صورت آسمان‌خراش‌های عریض، بلند و قرمز)؛ ۲) نمای زبان دامنه (`Domain Language View` با الگوریتم `TF-IDF`): حذف کلمات کلیدی زبان/فریم‌ورک و ساخت ابر واژگان تعاملی از مفاهیم تجاری واقعی هر پوشه؛ ۳) نمای وابستگی و دروازه کیفیت (`ccsh gate`): تشخیص دورها و توقف خودکار بیلد در صورت عبور پیچیدگی کد ایجنت از حد مجاز. |
| سایر ابزارهای بصری و کارتوگرافی کشف‌شده | `React Flow`, `Three.js`, `GraphViz DOT`, `SVG`, `Mermaid`. | `sverweij/dependency-cruiser` (`depcruise-wrap-stream-in-html`)؛ `CodeScene` (تحلیل رفتاری کد)؛ `CodeCity`؛ `Codeatlas` / `Repo-Visualizer` (نقشه‌های زنده SVG در CI)؛ `plan-visualizer` (دیاگرام‌های برنامه‌ریزی دوطرفه مبتنی بر React Flow که به عنوان دستگاه ورودی برای تغییر کد توسط ایجنت عمل می‌کنند)؛ `Warehouse 3D Map` (نقشه انبار سه‌بعدی ایزومتریک آفلاین با حرکت داده روی یال‌ها)؛ `Fantasy Map` (اژدهاها = نقاط داغ بدهی فنی)؛ `Growth Rings`؛ `Birdview`؛ `UIGraph` (تولید کاتالوگ سرویس‌ها و API). |
### جدول مرجع ۲: موتورهای گراف دانش کدبیس (CKG)، بهینه‌سازی توکن و مهندسی آنتالوژی
| نام ابزار / چارچوب | معماری هسته و ذخیره‌سازی | ویژگی‌ها، الگوریتم‌ها و متریک‌های اثبات‌شده (حذف مالیات اکتشاف) |
| :--- | :--- | :--- |
| `colbymchenry/codegraph` | هسته تجزیه‌گر Rust + ذخیره‌سازی SQLite محلی با جستجوی تمام‌متن `FTS5`. | ۱۰۰٪ محلی در ۲۰ زبان؛ تشخیص مسیرهای URL فریم‌ورک‌ها؛ همگام‌سازی خودکار با `File Watcher`؛ سرور MCP (`codegraph_context`, `codegraph_explore`)؛ کاهش میانگین ۳۵٪ هزینه API، ۵۹٪ مصرف توکن، ۴۹٪ زمان دیواری و ۷۰٪ فراخوانی ابزار در بنچمارک ۷ مخزن واقعی. |
| `rgctl` | Rust (موازی‌سازی با `Rayon` و `Tokio`) + ذخیره‌سازی `mmap-backed` در `.rgctl/`. | پیش‌محاسبه بیت‌ست‌های تنک دسترس‌پذیری (`Sparse Reachability Bitsets`) برای تحلیل شعاع انفجار (`rgctl -f json blast-radius`) در کمتر از ۱ میلی‌ثانیه بدون دی‌سریالایز کردن گراف در رم؛ زبان پرس‌وجوی گراف مشابه Cypher/SPARQL (`rgctl gql`)؛ الگوریتم PageRank داخلی (`rgctl -f json metrics --pagerank`)؛ فایل `SKILL.md` تعبیه‌شده درون باینری (`rgctl install --skill`). |
| `Graphify-Labs/graphify` (`graphifyy`) و `pyshine-labs/graphified` و `HelixDB/graphify-v8` | معماری دوگذره (`Dual-Pass`): تجزیه قطعی Tree-sitter در ۳۶ زبان + گذرگاه معنایی LLM برای مستندات/SQL/PDF/تصویر/ویدیو. | خوشه‌بندی اجتماعات با الگوریتم Leiden؛ شناسایی God Nodes با PageRank در `GRAPH_REPORT.md`؛ برچسب‌های معرفت‌شناختی سطح اطمینان یال‌ها (`EXTRACTED`, `INFERRED`, `AMBIGUOUS`) و محاسبه اطمینان مسیر بر اساس قانون «ضعیف‌ترین گام» (`Weakest Hop` در `graphify path A B`)؛ کش تدریجی با `SHA256`؛ قلاب رهگیری `PreToolUse`؛ قلاب `post-commit` گیت + درایور ادغام اختصاصی `Union-Merge` برای `graph.json`؛ کاهش ۹۰ تا ۹۵ درصدی توکن (از ۵۰٬۰۰۰ به ۳٬۰۰۰–۷٬۰۰۰ توکن). |
| `topoteretes/cognee` & `jayesh1126/memberry` | پایتون + مدل‌سازی گره‌های دانش با `Pydantic` + موتور ترکیبی گراف-بردار (`Hybrid Graph-Vector`). | CLI (`cognee-cli`) و اسکیل `cognee-recall` مجهز به `code_query`؛ مدل‌سازی وابستگی‌های زنجیره‌ای و واسطه‌ای (`init mediated`) در سطوح مختلف دانه‌بندی. |
| سایر موتورهای گراف و زمینه ایجنت | `Neo4j`, `Rust`, `TypeScript`, `Python`. | `CodeGraphContext (CGC)`؛ `Nomik` (گراف بومی روی Neo4j متصل به MCP)؛ `agentralabs/codebase` (گراف مفاهیم، تشخیص جفت‌شدگی و پیش‌بینی اثر تغییرات یا `Prophecy`)؛ `Beadnall/codemap`؛ `CCE`؛ `Bitloops`؛ `OpenViking`؛ `Airweave`. |
| چارچوب‌های آنتالوژی کدبیس (`OKF` & `.llmwiki/profile.json`) | فایل‌های پیکربندی خطاناپذیر (`Fail-Closed`) در `.llmwiki/profile.json`، `SCHEMA.md` و فرمت دانش باز (`OKF` با خروجی `JSON-LD` و `GraphML`). | تعریف رسمی انواع موجودیت (`concept`, `entity`, `module`, `service`, `comparison`, `overview`, `ADR`)، قرارداد فیلدها و ماشین حالت چرخه حیات؛ اعمال گیت‌های اعتماد زمان اجرا (`Runtime Trust Gates`) در مسیر نوشتن (`Write Path`) که ثبت هر گره بدون ارجاع خطی معتبر یا شواهد پین‌شده به هش محتوا را مسدود کرده یا به صف بازبینی (`Review Queue`) می‌فرستد. |
### جدول مرجع ۳: ویکی‌های کدبیس خودنگهدار (Self-Maintaining Codebase Wikis) و دروازه‌های ضدتوهم
| نام ابزار / مخزن | معماری کامپایل و نگهداری دانش (الگوی LLM Wiki کارپاتی) | قابلیت‌های تصویرسازی، جست‌وجو و جلوگیری از توهم (Zero-Hallucination) |
| :--- | :--- | :--- |
| `ussumant/llm-wiki-compiler` (v2.0) و `atomicstrata/llm-wiki-compiler` (`llmwiki`) | دارای `Codebase Mode` (`/wiki-init --codebase`)؛ کامپایل معماری، APIها، تصمیمات و Gotchas در `wiki/INDEX.md`؛ کاهش ۹۰٪ هزینه زمینه (خواندن ۳۳۰ خط به جای ۳٬۲۰۰ خط). | دستور `/wiki-visualize` برای باز کردن گراف دانش تعاملی مبتنی بر Canvas (کلیک روی گره = نمایش مقاله کامل در پنل کناری؛ `Shift+Click` = روشن شدن همسایگان مفهومی در عمق ۱، ۲ و ۳)؛ دستور `/wiki-migrate` برای بازنویسی خودکار `AGENTS.md`؛ دستورات `llmwiki lint`، `llmwiki refresh --stale` و هارنس ارزیابی `llmwiki eval`. |
| `vbarsoum1/llm-wiki-compiler` (`Klore`) | معماری مدل سه‌لایه به رهبری مدل کارگردان (`Three-Tier Director Model`): ۱) مدل سریع برای نرمال‌سازی تگ‌ها، ۲) مدل‌های قوی موازی برای نگارش مقالات، ۳) مدل کارگردان (سردبیر ارشد) برای مدیریت `INDEX.md`، `overview.md` و رفع تناقض‌ها. | کامپایل ۵۷ هزار کلمه با هزینه ~۰.۵۰ دلار و به‌روزرسانی تدریجی با ۰.۰۵ دلار؛ دستور `klore ask --save` با بازیابی ترکیبی (معنایی + بازرتبه‌بندی `BM25` + بسط گراف ویکی‌لینک‌ها) که پاسخ‌های تحلیلی خوب را به عنوان صفحات جدید در ویکی ذخیره می‌کند (`Knowledge Compounding`). |
| `0xKobold/pi-codebase-wiki` | ساخت دایرکتوری `.codebase-wiki/` شامل قانون اساسی `SCHEMA.md`، `INDEX.md`، `CHANGELOG.md`، `entities/`، `concepts/` و دیتابیس `wiki.db` از روی تاریخچه کامیت‌های گیت و درخت فایل‌ها. | چرخه `Ingest -> Query -> Lint`؛ دارای Content Viewer (حالت تاریک، لینک‌های دوطرفه `[[wikilinks]]` و جست‌وجوی تمام‌متن) در کنار گراف تعاملی Force-Directed با قابلیت Drag و Zoom؛ دستور `wiki lint` برای کشف صفحات یتیم (`Orphaned`) و کهنه (`Stale`). |
| `AlmanacCode/codealmanac` (`ca`) | تمرکز بر ثبت «چیزهایی که کد نمی‌تواند بگوید»: تصمیمات معماری، ناورداها (`Invariants`)، جریان‌ها و تله‌های پنهان در پوشه `almanac/`. | دستور `codealmanac serve` برای اجرای ویکی‌خوان محلی در مرورگر؛ دارای دو حلقه خودکار پس‌زمینه (Daemon): ۱) `Sync` (هر ۵ ساعت لاگ مکالمات JSONL شما با ایجنت‌های کدنویسی را اسکن کرده و دانش مفید را وارد ویکی می‌کند) و ۲) `Garden` (هر ۲۴ ساعت صفحات قدیمی و لینک‌های ضعیف ویکی را هرس و بهینه می‌نماید). |
| `rekipedia` (`reki`) | کامپایل کدبیس با `reki scan .` به پایگاه دانش SQLite و صفحات ویکی در `docs/wiki/` با ارجاع دقیق `file:line`. | حالت ۱۰۰٪ آفلاین و بدون LLM با پرچم `reki scan . --no-llm` مبتنی بر تحلیل ایستای خالص؛ دستور `reki onboard .` برای تولید تور آشنایی در چند ثانیه؛ `reki hotspots` برای نمایش گره‌های پل (`Bridge/Hub Nodes`)؛ سرور `reki mcp` با تشخیص خودکار کهنگی (`Auto-staleness`). |
| `doc0` (`doc0.dev`) | استخراج گراف قطعی با `tree-sitter` و تطبیق با کامپایلر زبان (دقت ۹۹.۹٪ روی ۸٬۷۸۶ فراخوانی در مخزن Next.js)؛ خوشه‌بندی با `graphology-communities-leiden`؛ علامت‌گذاری موارد نامطمئن با `unresolved`. | دروازه ممیزی گراف (`Graph Verification Gate`): هر تابع یا کلاسی که در متن ویکی تولیدشده توسط LLM نام برده شود به صورت خودکار با گراف AST چک می‌شود؛ اگر نام‌های ناموجود از حد آستانه بگذرد، صفحه برای بازنویسی برگردانده می‌شود (کسب امتیاز ۰.۸۵۶ در پشتیبانی ادعاها)؛ لینک مستقیم قطعات کد به خطوط دقیق همان کامیت. |
### جدول مرجع ۴: حکمرانی مکانیکی معماری، امنیت و کالبدشکافی رفتاری کدبیس
| حوزه کنترلی | ابزارها و متدولوژی‌های اجرایی که باید در اسکیل و هارنس ادغام شوند |
| :--- | :--- |
| قفل کردن مرزهای ماژولار پایتون و JS/TS | `tach-org/tach` (Rust + Python AST، بدون سربار زمان اجرا): دستورات `tach init`، `tach check`، `tach show` (خروجی GraphViz DOT) و `tach report`؛ پیکربندی `tach.toml` با `strict: true` و تعریف معماری لایه‌ای (`serving -> cli -> pipeline -> library`) با `layers_explicit_depends_on` و `exact=true`. ترکیب با `import-linter` در `pyproject.toml` و اسکنرهای AST سفارشی در `tests/test_architecture.py` (برای شکار دستورات SQL درون رشته‌ها، بارگذاری پویا با `importlib`/`getattr`، فراخوانی `subprocess` و Lazy Imports به همراه ۳۰+ تست منفی). در JS/TS استفاده از `dependency-cruiser` (`.dependency-cruiser.js`). |
| کالبدشکافی رفتاری گیت (`Behavioral Git Forensics`) | تقاطع دادن توپولوژی ایستا با تاریخچه گیت برای استخراج ۳ سیگنال: ۱) نرخ تلاطم (`Churn`)، ۲) شکاف مالکیت واقعی در برابر فایل `CODEOWNERS`، ۳) جفت‌فایل‌های هم‌تغییر (`Co-change Pairs`) که هیچ لینک Import مستقیمی ندارند اما همیشه در کامیت‌ها با هم ویرایش می‌شوند (کشف جفت‌شدگی پنهان یا زمانی `Implicit/Temporal Coupling`). |
| ممیزی امنیتی و کیفیت پیشرفته | اسکن آسیب‌پذیری‌ها (CVEs)، قواعد `Semgrep` و `CodeQL`، تجزیه‌گرهای گزارش استاندارد `SARIF`، بررسی زمان ثابت (`Constant-Time Analysis`)، تست جهش (`Mutation Testing`)، تست مبتنی بر ویژگی (`Property-Based Testing`)، بررسی صفرسازی حافظه (`Zeroization Review`) و تطبیق مشخصات با کد (`Spec-to-Code Checks`). |
### جدول مرجع ۵: کالبدشکافی `LearnHarness`، علوم شناختی یادگیری و ابزارهای AI Tutor
| نام پروژه / منبع | معماری و چرخه پداگوژیکی | ویژگی‌های کلیدی که باید در هارنس نهایی (Code Intelligence + Learning) پیاده‌سازی شوند |
| :--- | :--- | :--- |
| `amosblomqvist/learnharness` (v0.4.1+, AGPL-3.0) | اپلیکیشن Next.js + Electron (`electron/main.cjs`) مبتنی بر موتور بومی Pi (`Native Pi Agents & Server-Owned Conversation Records`)، پنل Transcript، داک‌های آموزش/تمرین (`Docks`) و گراف دانش؛ دارای پوشه `skills/learnharness` و `AGENTS.md`. | ۱) چرخه چهارمرحله‌ای $\text{Measure/Probe} \rightarrow \text{Plan} \rightarrow \text{Teach} \rightarrow \text{Practice}$: در `Probe` کشف مرز پیش‌نیازها، اسلایدر اطمینان (`Confidence Slider`)، فیلد صوتی/متنی «بلند فکر کردن» (`Think Out Loud`)، کالیبراسیون قطعی اطمینان و گیت سخت‌گیرانه `probe_done`؛ در `Plan` ساخت نقشه وابستگی زنده (`Dependency Map / Lesson Map`)؛ در `Teach` الگوی `Predict -> Interactive Demos/SVG -> Check Question -> Repair Misconceptions` به همراه سؤالات حاشیه‌ای درجا (`/btw` و `Inline Side Questions`)؛ در `Practice` تمرین بازیابی فعال بدون بردن نام مفهوم در صورت سؤال، برگه‌های تمرین تمام‌صفحه (`Fullscreen Worksheets`) و تکرار فاصله‌دار به سبک Anki. ۲) گراف دانش گزاره و مقدمه (`Proposition & Premise Knowledge Graph`) متصل به نشست منبع برای ردیابی و اصلاح آموزش‌های غلط مدل ضعیف‌تر. ۳) رفع شکاف معماری Issue `#115` در هارنس ما: در LearnHarness فعلی، ردیابی تسلط کاربر (`Competence Tracking`) در نشست Practice محبوس می‌ماند؛ در هارنس ما، امتیاز تسلط مهندس مستقیماً روی گره‌های گراف کدبیس و گزاره‌ها ذخیره می‌شود. ۴) مسیریاب سه‌گانه مدل (`Strong`, `Cheap`, `Vision`)، پل ارتباطی به `Claude Code CLI`، فشرده‌سازی Checkpoint برای نشست‌های ۴۰ تا ۵۵ هزار توکنی، و پشتیبانی بومی از راست‌به‌چپ (`RTL` در PR `#457`) و کپی سورس TeX فرمول‌های KaTeX (`#481`). |
| `psyteachr.github.io/AITutoR/` (دانشگاه گلاسگو) | چارچوب علوم شناختی یادگیری برنامه‌نویسی و داده. | ۴ ستون شناختی: ۱) تمرین بازیابی (`Retrieval Practice`) با کوئیزهای گام‌به‌گام، ۲) تمرین توزیع‌شده (`Distributed Practice`)، ۳) بسط معنایی (`Elaboration`) با مقایسه رویکردها در سطوح مختلف پیچیدگی، ۴) فراشناخت (`Metacognition`) برای حفظ استقلال، تاب‌آوری و حس شایستگی مهندس؛ به همراه پرامپت‌های سیستمی سقراطی و ضدچاپلوسی (`Anti-Sycophancy`). |
| `TovTechOrg/Tov-learn` | اسکیل کدنویسی (`/learn` و `/learn status`) با حالت `Project Analysis`. | اسکن بی‌صدای مخزن، پرسیدن ۵ سؤال درباره هدف و گلوگاه‌های پروژه، تولید نقشه معماری بصری HTML و داشبورد پیشرفت؛ فرمت آموزشی ۴ بخشی `Journey`: ۱) *مسئله (`The Problem`)*، ۲) *بینش خبرگان (`The Insight`)*، ۳) *در پروژه شما (`In Your Project` — اتصال مستقیم مفهوم به کد واقعی مخزن کاربر)*، ۴) *پرسش تفکری*؛ به همراه تکرار فاصله‌دار فیبوناچی در بازه‌های ۲، ۱۳، ۳۴ و ۸۹ روز. |
| `eugeniughelbur/doceo` | اسکیل آموزش بصری (`/doceo`). | مصاحبه کالیبراسیون ۳۰ ثانیه‌ای اولیه؛ تبدیل هر کدبیس، پوشه ترسناک به ارث رسیده، فایل کانفیگ مبهم یا خطای کامپایل به یک درس بصری تک‌صفحه‌ای (`One-Screen Visual Lesson`)؛ ۱۰ سناریوی مهندسی از جمله «آموزش خودِ خطا، نه فقط راه‌حل آن». |
| `coding-tutor` (`codewithbehnam/cc-docs`) | اسکیل آموزش کدنویسی (`SKILL.md`). | ساخت مسیر یادگیری ماندگار (`Persistent Learning Trail`) در کنار کدبیس با استفاده از کدهای واقعی داخل مخزن خود کاربر به عنوان مثال‌های آموزشی. |
| `ai-learning-path-generator` (`Enterprise-DNA-OS`) | پلتفرم React/Vite + Supabase + Copilot. | دیاگرام‌های مدل ذهنی بصری (`Visual Mental Model Diagrams`)، مینی‌درس‌های عمیق کلیک‌پذیر (`Deep-Dive`)، حالت پادکست/ارائه و موتور `Learning DNA Profile` (تحلیل الگوهای پرامپت کاربر برای کشف نقاط کور علمی). |
| `TutorAI` & `AI-Tutor-Multi-Agent` | سیستم‌های چندعاملی TypeScript/Next.js. | استفاده از مدل‌های ریاضی ردیابی دانش (`Knowledge Tracing Models` نظیر BKT/DKT) برای تخمین احتمال تسلط کاربر بر هر گره از گراف دانش. |
### جدول مرجع ۶: معماری هسته اجرایی هارنس ایجنتیک (`ai.miraheze.org`, `SWE-agent`, `OpenHands V1`, `Antigravity`)
| الگو و کامپوننت معماری | منبع الهام | مشخصات فنی دقیق برای پیاده‌سازی در هارنس اختصاصی ما |
| :--- | :--- | :--- |
| هسته بدون حالت مبتنی بر `Append-Only EventLog` | `OpenHands V1` + `Mini-SWE-agent` (معماری ۱۰۰ خطی در `ai.miraheze.org`) | تعریف تمام اجزا با مدل‌های تغییرناپذیر Pydantic؛ `Agent` به عنوان تابع خالص ($\text{History} \rightarrow \text{Action}$)؛ شیء `Conversation` و `ConversationState` با حلقه ۳۰ خطی؛ ثبت هر رویداد (`MessageEvent`, `ActionEvent`, `ObservationEvent`, `AgentErrorEvent`, `Condensation`) به صورت فایل JSON مستقل روی دیسک برای بازپخش کامل (`Replayability`)، دیباگ سفر در زمان (`Time-Travel Debugging`) و جمع‌آوری داده‌های `Trajectory Training` (مشابه `SWE-agent-LM-32b`). انتزاع `Workspace` (`LocalWorkspace` و `DockerWorkspace` با `cap-drop ALL`). |
| رابط ایجنت-کامپیوتر (`ACI`) با ۳ کنش پایه و لینتر درون‌خطی | `SWE-agent ACI` (افزایش ۶۴٪ نرخ حل مسئله نسبت به شل خام و ۶.۷ برابر نسبت به RAG) | سه کنش جهانی: ۱) `RunCommand(command: str)`، ۲) `EditFile(path: str, old: str, new: str)` (ویرایشگر String-Replace متصل به اجرای خودکار لینتر نحوی و `tach check` و `ccsh gate` که خطاها را فوراً در همان گام برمی‌گرداند)، ۳) `Finish(summary: str)`. تزریق پیام صریح در صورت خروجی خالی دستور شل. |
| مدیریت حافظه، فشرده‌سازی (`Condenser`) و کنترل زمینه Git-گونه (`GCC`) | `OpenHands V1` + `Antigravity` + الگوی `GCC` | اجرای `Condenser` در آستانه مشخص توکن (مثلاً ۱۳۵٬۰۰۰ توکن یا ۴۰–۵۵ هزار توکن در نشست‌های آموزشی) با ثبت رویداد `Condensation` بدون حذف تاریخچه دیسک؛ پیاده‌سازی عملیات صریح `GCC` (`COMMIT`, `BRANCH`, `MERGE`, `CONTEXT`) روی حافظه کاری ایجنت؛ اجرای سرویس ۵ الگویی `StuckDetector` برای توقف حلقه‌های تکرار معیوب. |
| استاندارد افشای تدریجی مهارت‌ها و قلاب `PreToolUse` | `Google Antigravity` + `Graphify` | بارگذاری تدریجی `.agents/skills/<skill-name>/SKILL.md` (فرانت‌متر YAML شامل `name` و `description` سوم‌شخص، بدنه زیر ۵۰۰ خط، اسکریپت‌های جعبه سیاه در `scripts/` که ابتدا با `--help` فراخوانی می‌شوند، در ۴ سطح بلوغ). قلاب رهگیری `PreToolUse` روی ابزارهای `Read` / `Grep` / `Glob` که پیش از جستجوی کورکورانه، ایجنت را مجبور به پرس‌وجو از گراف دانش و `wiki/INDEX.md` می‌کند. |
| ارکستراسیون چندایجنتی (`/teamwork`) و ایزولاسیون `Git Worktrees` | `Google Antigravity` | فاز ۱: مصاحبه تعیین محدوده (`Scoping Interview`)، تعیین `Integrity Mode` و ثبت `ORIGINAL_REQUEST.md`. فاز ۲: توپولوژی نقش‌محور شامل `Sentinel` (هماهنگ‌کننده)، `Project Orchestrator` (تحویل به جانشین تازه `Fresh Successor` در پایان هر مایل‌استون)، `Explorers` (کاوشگران صرفاً خواندنی روی گراف)، `Workers` (کدنویسی موازی در `Git Worktrees` ایزوله با قابلیت `Idle`/`Auto-wake` و `Permission Bubbling` با `Alt+J`)، و ممیزی متخاصم توسط `Auditor`، `Victory Auditor` و ایجنت `/browser` تا صدور آرتیفکت `Walkthrough`. |
### جدول مرجع ۷: کامپوننت‌های متن‌باز آماده برای داشبورد و استانداردهای مهندسی فارسی / BiDi / RTL
| لایه رابط کاربری داشبورد | پروژه‌ها و کتابخانه‌های متن‌باز آماده برای استفاده و ترکیب | الزامات مهندسی BiDi / RTL و تایپوگرافی دوزبانه که باید در گزارش تدوین شوند |
| :--- | :--- | :--- |
| پوسته اصلی، داک‌های یادگیری و پنجره‌های چندگانه (Split/Dockable Views) | پوسته `LearnHarness v0.4.1` (Next.js + Tailwind + KaTeX با پشتیبانی بومی RTL در PR `#457`) + کتابخانه‌های مدیریت چیدمان پنجره‌های تودرتو و داک‌شونده (`Dockview`, `FlexLayout`, `GoldenLayout`). | کانتینر ریشه با `dir="rtl"`؛ طراحی بدون قاب مزاحم مرورگر (مناسب برای وب و دسکتاپ بومی نظیر Tauri v2 / Electron) با تم تاریک عمیق (OLED-Void / Catppuccin). |
| موتور گراف دانش، نقشه درس و دیاگرام‌های تعاملی | `React Flow` (`@xyflow/react`) (هر گره یک کامپوننت کامل DOM/HTML است، ایده‌آل برای کارت‌های فارسی/انگلیسی بدون مشکل Text Shaping در WebGL خام) + موتور نمایشگر `Archify v3.2` (`@meta locale=fa`) + بوم کارت‌های کد `CodeFlow` (React 18 + D3 v7) + `vis-network.js` / `Sigma.js` / `Graphology` / `Three.js`. | اعمال `unicode-bidi: plaintext` (یا `dir="auto"`) روی تمام پاراگراف‌های توضیحی فارسی؛ ایزولاسیون کامل (`unicode-bidi: isolate` و `dir="ltr"`) روی تمام نام توابع، مسیر فایل‌ها، بلوک‌های کد (`<pre><code dir="ltr">`)، عبارات ریاضی KaTeX و برچسب‌های AST درون گره‌های گراف تا پرانتزها، نقطه‌ها و عملگرها در جملات فارسی جابه‌جا نشوند. |
| تایپوگرافی دوزبانه (Bilingual Typographic Hierarchy) | ترکیب فونت‌های مهندسی انگلیسی و فارسی در سطح متغیرهای CSS (`font-family` stack). | تعریف سلسله‌مراتب تایپوگرافی دقیق با ترکیب فونت‌های انگلیسی (`Space Grotesk`, `Unbounded`, `JetBrains Mono`) با فونت‌های فارسی/عربی (`IBM Plex Sans Arabic`, `Lalezar`, `Vazirmatn`) به تفکیک تیترها، متن بدنه ویکی، گره‌های گراف و محیط کد/ترمینال. |
---
## ۵. ساختار و سرفصل‌های الزامی گزارش نهایی پژوهش (Deliverable Structure)
لطفاً طرح پژوهش و گزارش نهایی را دقیقاً در ۸ فصل جامع و عمیق زیر سازمان‌دهی کن تا مستقیماً به عنوان مرجع کدنویسی اسکیل و هارنس استفاده شود:
* بررسی کامل تمام ابزارهای نام‌برده در جداول ۱ تا ۶ به همراه کشف و معرفی پروژه‌های جدید، جایگزین‌ها، راهنماها، فریم‌ورک‌ها و اسکیل‌های موجود در تمام ۴۱ تاپیک گیت‌هاب (در دسته‌های تصویرسازی، گراف دانش، آنتالوژی، ویکی کدبیس، امنیت/کیفیت، حکمرانی معماری و آموزش با هوش مصنوعی).
2. فصل دوم — کالبدشکافی عمیق معماری `LearnHarness` و ترکیب آن با علوم شناختی (`AITutoR`, `Tov-learn`, `doceo`):
* تحلیل کدهای منبع، ساختار پوشه‌ها، موتور Pi، اسکیمای گراف گزاره‌ها و مقدمه‌ها (`Propositions & Premises`)، چرخه `Probe -> Plan -> Teach -> Practice`، مکانیسم‌های علوم شناختی و راه‌حل مهندسی دقیق برای رفع نقص Issue `#115` از طریق ادغام گراف تسلط یادگیرنده (`Competence Graph` و `Knowledge Tracing`) با گراف نمادهای کدبیس (`AST Symbol Graph`).
3. فصل سوم — معماری کامل و کدهای اجرایی «Skill جامع هوش کدبیس» (`.agents/skills/phase0-omni-audit`) برای Antigravity:
* طراحی دقیق ساختار دایرکتوری اسکیل، فایل کامل `SKILL.md`، اسکریپت‌های ارکستراسیون جعبه سیاه (`scripts/`)، پیکربندی سرورهای MCP (`codebase-memory-mcp`, `CodeGraph`, `rgctl`)، خط لوله تولید ویکی خودنگهدار (`llmwiki` / `pi-codebase-wiki` / `doc0`)، گیت‌های معماری (`tach`) و تولید خودکار داشبوردهای بصری (`Archify`, `Understand-Anything`, `CodeFlow`, `CodeCharta`) روی مخزن فاز صفر.
4. فصل چهارم — معماری مرجع «Harness اختصاصی دومنظوره» (هوش کدبیس + یادگیری تعاملی):
* طراحی لایه‌به‌لایه هارنس شامل: هسته `Append-Only EventLog`، رابط ۳ کنشی `ACI` با لینترهای درون‌خطی، قلاب‌های رهگیری `PreToolUse` و `SessionStart`، کنترل زمینه `GCC` (`COMMIT`/`BRANCH`/`MERGE`)، حلقه‌های پس‌زمینه `Sync` و `Garden` (الگوی `CodeAlmanac`)، گیت راستی‌آزمایی ضدتوهم گراف (الگوی `doc0`) و پروفایل‌های چندایجنتی (`Scout / Worker / Auditor / Socratic Tutor`) در درخت‌های کاری ایزوله Git.
5. فصل پنجم — مهندسی داشبورد تعاملی، کامپوننت‌های متن‌باز آماده و استانداردهای فارسی / BiDi / RTL:
* بررسی و انتخاب بهترین کامپوننت‌های متن‌باز قابل استفاده مستقیم (از `LearnHarness`، `React Flow`، `Archify`، `CodeFlow`، `Dockview` و ویکی‌خوان‌ها)؛ ارائه قواعد کامل CSS BiDi، نحوه رندر بدون نقص متون دوجهته در بوم‌های گراف (DOM در برابر Canvas/WebGL) و پیاده‌سازی سلسله‌مراتب تایپوگرافی دوزبانه (`Space Grotesk` / `Unbounded` / `JetBrains Mono` در کنار `IBM Plex Sans Arabic` / `Lalezar` / `Vazirmatn`).
6. فصل ششم — اسکیمای یکپارچه داده و آنتالوژی (Unified Data & Ontology Schema):
* طراحی اسکیمای دقیق (SQLite / JSON / Markdown Frontmatter) که گره‌های کد (فایل، کلاس، تابع، زیرساخت)، گره‌های ویکی و معماری (`ADR`, `Invariant`, `Domain Flow`) و گره‌های یادگیری (`Proposition`, `Premise`, `Competence Score`, `Spaced Repetition Schedule`) را در یک گراف واحد به هم پیوند می‌دهد.
7. فصل هفتم — ماتریس نهایی انتخاب ویژگی‌های برتر (Golden Feature Matrix):
* جدول جامع نگاشتِ اینکه کدام ویژگی و الگوریتم دقیقاً از کدام پروژه متن‌باز برداشته می‌شود و در کدام ماژول از اسکیل و هارنس ما قرار می‌گیرد.
8. فصل هشتم — نقشه راه اجرایی گام‌به‌گام (از اجرای اسکیل روی فاز صفر تا ساخت و استقرار هارنس نهایی):
* برنامه عملیاتی فازبندی‌شده همراه با گیت‌های راستی‌آزمایی (Verification Gates) برای تعاملات بعدی ما که در آن کدنویسی عملی اسکیل و هارنس را آغاز خواهیم کرد.
```
گزارش:
```md
# گزارش پژوهشی-مهندسی جامع: مهندسی اسکیل هوش کدبیس و هارنس دومنظوره با داشبورد BiDi/فارسی
در ادامه، پژوهش عمیق و چندوجهی درباره تمامی ابزارها، معماری‌ها و تاپیک‌های مطرح‌شده ارائه می‌شود. ابتدا باید اطلاعات به‌روز از مخازن و تاپیک‌های کلیدی استخراج شود.
---
بگذارید ابتدا بررسی‌های لازم را انجام دهم:بر اساس پژوهش گسترده، اکنون گزارش جامع ۸ فصلی را ارائه می‌دهم:
---
# 📘 گزارش پژوهشی-مهندسی جامع
## مهندسی اسکیل هوش کدبیس و هارنس دومنظوره با داشبورد BiDi/فارسی
---
## فصل اول — کاتالوگ جامع و کالبدشکافی ابزارهای استخراج‌شده
### ۱.۱ ابزارهای تصویرسازی تعاملی و بوم‌های کد
#### Archify (`tt-a1i/archify`)
Archify یک اسکیل ایجنتی برای Claude Code، Codex و ابزارهای مشابه است. با درخواست ایجنت از آن می‌توان صفحات توضیحی (Explainer) ساخت که ابتدا نتیجه‌گیری و سپس پنل‌های گام‌به‌گام شامل جداول، مراحل، نمودارها، کد و دیاگرام‌های اعتبارسنجی‌شده ارائه می‌شوند. با بیش از ۳۶٬۰۰۰ ستاره گیت‌هاب (و حتی ۳٬۷۲۲ ستاره در یک روز)، یکی از محبوب‌ترین ابزارهای توسعه‌دهنده فعلی است.
معماری هسته‌ای: ایجنت هوش مصنوعی کد یا پرامپت را تحلیل کرده، JSON IR تایپ‌شده (Intermediate Representation) تولید می‌کند و Archify آن را به فایل‌های مستقل HTML/SVG با اعتبارسنجی کامل کامپایل می‌نماید. Archify از اعتبارسنجی اتمیک استفاده می‌کند — هر دیاگرام باید قبل از تحویل، بررسی‌های اسکیما، قواعد چیدمان، رندرینگ HTML/SVG، اعتبارسنجی مسیرها و فاصله برچسب‌ها از مسیرها را با موفقیت بگذراند.
ویژگی‌های حیاتی برای اسکیل ما:
#### Understand-Anything (`Egonex-AI/Understand-Anything`)
Understand-Anything با ۷۱.۷ هزار ستاره گیت‌هاب، هر کدبیسی را به گراف دانش تعاملی و قابل اشتراک‌گذاری تبدیل می‌کند. خط لوله چندایجنتی آن پنج ایجنت تخصصی را به صورت موازی اجرا می‌کند و حقایق ساختاری را با Tree-Sitter و معنای مفهومی را با LLM استخراج کرده، سپس داشبورد تعاملی ارائه می‌دهد.
معماری ۷ ایجنتی:
تحلیل ایستا و LLMها هرکدام بهترین کارشان را انجام می‌دهند. دستور `/understand` پنج ایجنت تخصصی را هماهنگ می‌کند (project-scanner، file-analyzer، architecture-analyzer، tour-builder و graph-reviewer)، `/understand-domain` ایجنت ششم (domain-analyzer) و `/understand-knowledge` ایجنت هفتم (article-analyzer) را اضافه می‌کند.
قابلیت‌های آموزشی:
#### CodeFlow (`braedonsaunders/codeflow`)
بر اساس اطلاعات مرجع: یک تک‌فایل HTML بدون سرور و بدون Build (React 18 + D3 v7 از CDN) با ویژگی‌های کلیدی:
#### CBM — Codebase Memory MCP (`DeusData/codebase-memory-mcp`)
CBM یک سرور هوش کد محلی برای ایجنت‌های هوش مصنوعی از طریق MCP است با قابلیت کاوش گراف دانش کد به صورت سه‌بعدی.
معماری فنی:
ساختار سورس شامل: `main.c` (نقطه ورود سرور MCP stdio + CLI)، `daemon/` (هماهنگی نشست)، `mcp/` (سرور MCP با ۱۷ ابزار JSON-RPC 2.0)، `store/` (ذخیره‌سازی گراف SQLite شامل گره‌ها، یال‌ها، پیمایش، جست‌وجو و Louvain)، `pipeline/` (ایندکس‌گذاری چندمرحله‌ای: ساختار ← تعاریف ← فراخوانی‌ها ← لینک‌های HTTP ← کانفیگ ← تست)، `cypher/` (لکسر، پارسر، برنامه‌ریز و اجراکننده پرس‌وجوی Cypher) و `internal/cbm/` (گرامرهای Tree-sitter برای ۱۶۲ زبان).
CBM Lens Beta:
ابزارهای MCP رابط ایجنت با گراف هستند. CBM Lens Beta رابط انسانی است: تلاش برای رساندن قدرت گراف دانش کد به انسان‌ها.
#### CodeCharta (`MaibornWolff/codecharta`)
بر اساس جداول مرجع: استعاره شهر سه‌بعدی نرم‌افزار با ویژگی‌های:
### ۱.۲ موتورهای گراف دانش کدبیس (CKG)
#### Graphify (`Graphify-Labs/graphify`)
Graphify (Apache-2.0 با حدود ۱۳۸٬۰۰۰ ستاره، اکنون توسط Graphify Labs پشتیبانی‌شده) یک اسکیل `/graphify` برای Claude Code، Codex، Cursor و دیگران است، با سرور MCP اختیاری شامل ده ابزار نظیر `query_graph`، `get_neighbors`، `shortest_path` و `get_pr_impact`.
معماری دوگذره:
Graphify در صورتی برتری دارد که مخزن شامل Terraform، اسکیماهای SQL یا انبوهی از مستندات معماری و RFCها باشد که بخواهید در همان گراف کد قرار بگیرند.
Graphify تنها ابزاری است که یک مدل را فراخوانی می‌کند و آن هم فقط برای فایل‌های غیرکد.
ویژگی‌های کلیدی: خوشه‌بندی Leiden، شناسایی God Nodes با PageRank، برچسب‌های اطمینان یال‌ها (`EXTRACTED`, `INFERRED`, `AMBIGUOUS`)، کش تدریجی SHA256، قلاب `PreToolUse` و کاهش ۹۰–۹۵ درصدی مصرف توکن.
#### CodeGraph (`colbymchenry/codegraph`)
CodeGraph یک کتابخانه، CLI و سرور MCP هوش کد متن‌باز و محلی-اول است. تحت لایسنس MIT، گراف دانش پیش‌ایندکس‌شده از کدبیس شامل روابط نمادها، گراف فراخوانی، ساختارهای import و معماری کد را ارائه می‌دهد.
معماری سه‌لایه:
CodeGraph کد را به گراف محلی SQLite تجزیه می‌کند (نسخه v1.5.0 در ژوئیه به موتور Rust منتقل شد) و آن را از طریق MCP عرضه می‌کند. به صورت پیش‌فرض سرور تنها یک ابزار `codegraph_explore` ارائه می‌دهد که سورس مرتبط و مسیرهای فراخوانی را در یک فراخوانی برمی‌گرداند. ابزارهای اضافی مانند callers، callees و impact نیز وجود دارند.
بنچمارک اثبات‌شده: کاهش میانگین ۳۵٪ هزینه API، ۵۹٪ مصرف توکن، ۴۹٪ زمان دیواری و ۷۰٪ فراخوانی ابزار.
#### codebase-memory-mcp (قبلاً بررسی شد)
یک سرور MCP است که کدبیس را در گراف دانش محلی پایدار با استفاده از Tree-sitter ایندکس کرده و پرس‌وجوهای ساختاری را به ایجنت‌های کدنویسی ارائه می‌دهد.
#### مقایسه سه‌گانه موتورهای CKG
| ویژگی | Graphify | CodeGraph | CBM |
|--------|----------|-----------|-----|
| لایسنس | Apache-2.0 | MIT | MIT |
| زبان‌ها | ~۴۰ + اسناد | ۲۰+ | ۱۶۲ |
| ذخیره‌سازی | graph.json (Neo4j اختیاری) | SQLite + FTS5 | SQLite + mmap |
| ابزارهای MCP | ۱۰ | ۲+ | ۱۷ |
| ایندکس اسناد | بله (با LLM) | خیر | بله (v0.12) |
| UI بصری | مرورگر | خیر | CBM Lens 3D |
| قلاب PreToolUse | بله | خیر | بله |
| کاهش توکن | ۹۰-۹۵٪ | ۵۹٪ | بالا |
هر سه ابزار ادغام دسته‌اول با Claude Code (پیکربندی MCP، قلاب‌ها و/یا نصب خودکار اسکیل‌ها) ارائه می‌دهند. code-review-graph و codebase-memory-mcp هر دو قلاب‌های PreToolUse نصب می‌کنند که Claude Code را به سمت پرس‌وجو از گراف به جای Grep/Glob سوق می‌دهند.
### ۱.۳ ابزارهای جدید کشف‌شده از تاپیک‌های گیت‌هاب
بر اساس جست‌وجوهای انجام‌شده و اطلاعات مرجع:
| ابزار | حوزه | ویژگی کلیدی |
|-------|------|-------------|
| rgctl | گراف + تحلیل شعاع انفجار | بیت‌ست‌های تنک دسترس‌پذیری، PageRank داخلی، زبان پرس‌وجوی Cypher/SPARQL، SKILL.md تعبیه‌شده |
| Nomik | گراف بومی Neo4j + MCP | اتصال مستقیم به پایگاه داده گراف |
| agentralabs/codebase | تشخیص جفت‌شدگی + پیش‌بینی اثر تغییرات | الگوریتم Prophecy |
| Serena | ویرایش مبتنی بر گراف | بهترین گزینه اگر ایجنت عمدتاً ویرایش انجام می‌دهد. |
| dependency-cruiser | حکمرانی وابستگی JS/TS | خروجی HTML تعاملی با `depcruise-wrap-stream-in-html` |
| CodeScene | تحلیل رفتاری کد | ادغام داده‌های گیت با متریک‌های کد |
| doc0 | ویکی + گراف قطعی | دقت ۹۹.۹٪ با Tree-sitter + دروازه ممیزی ضدتوهم |
| CodebaseMemory (مقاله آکادمیک) | گراف دانش Tree-sitter برای کاوش کد LLM از طریق MCP | |
| RepoGraph | بهبود مهندسی نرم‌افزار هوش مصنوعی با گراف کد سطح مخزن | |
---
## فصل دوم — کالبدشکافی عمیق LearnHarness و ترکیب با علوم شناختی
### ۲.۱ معماری داخلی LearnHarness
LearnHarness یک هارنس ایجنتی برای یادگیری است. از ایجنت‌های هوش مصنوعی برای برنامه‌ریزی و تدریس درس‌ها بر اساس درک فعلی کاربر تا هدف او استفاده می‌کند. تصویر دقیقی از آنچه کاربر می‌فهمد و چگونه استدلال می‌کند می‌سازد و با یادگیری کاربر آن را به‌روز می‌کند.
چرخه چهارمرحله‌ای:
گراف دانش گزاره‌ها:
LearnHarness گزاره‌ها را با مقدمه‌ها و نتیجه‌گیری‌هایشان در گراف دانش انباشت می‌کند، نه صرفاً نتایج درست/غلط. گراف این ساختار را با لینک‌های بازگشت به نشست‌های منبع نشان می‌دهد. نشست‌های تدریس آینده می‌توانند گراف را بخوانند به جای شروع از صفر.
ساختار فنی (از دیاگرام معماری):
LearnHarness یک هارنس یادگیری محلی-اول هوش مصنوعی است. یادگیرنده نشستی با یک هدف شروع می‌کند؛ اپ درک موجود را ارزیابی، برنامه‌ریزی و از طریق یک نوبت ایجنت تدریس می‌کند، سپس از تمرین تطبیقی جداگانه پشتیبانی می‌کند. نثر معلم می‌تواند به گراف دانش پایدار استخراج شود.
کامپوننت‌های اصلی:
شامل: `components/new-session.tsx` (رابط نشست)، `components/chat.tsx` (رابط چت)، `components/practice-cards.tsx` (کارت‌های تمرین)، `components/activity-dock.tsx` (فعالیت‌ها و آرتیفکت‌ها)، `components/graph-view.tsx` (نمای گراف دانش)، `app/api/graph/import/route.ts` (نقاط پایانی گراف)، `src/agent/subagents/extraction.ts` (استخراج گراف)، `src/store/graph.ts` (ذخیره‌سازی گراف دانش).
فورک‌های فعال و اکوسیستم:
### ۲.۲ راه‌حل Issue #115: ادغام گراف تسلط با گراف AST کدبیس
مسئله: در LearnHarness فعلی، ردیابی تسلط کاربر در نشست Practice محبوس می‌ماند و به گره‌های کدبیس متصل نیست.
راه‌حل مهندسی پیشنهادی:
```
┌─────────────────────────────────────────────┐
│ Unified Knowledge Graph │
├────────────┬───────────────┬────────────────┤
│ Code Layer │ Pedagogy Layer│ Competence Layer│
│ (AST nodes,│ (Propositions,│ (Mastery Score, │
│ Functions,│ Premises, │ Last Review, │
│ Modules) │ Conclusions) │ SR Schedule) │
├────────────┴───────────────┴────────────────┤
│ Edges: EXPLAINS, DEPENDS_ON, ASSESSED_BY │
│ COVERS_SYMBOL, MISCONCEPTION_ABOUT │
└─────────────────────────────────────────────┘
```
اسکیمای پیوند:
```json
{
"node_type": "competence_record",
"symbol_ref": "src/pipeline/indexer.ts::buildGraph",
"proposition_ids": ["prop_042", "prop_043"],
"mastery_score": 0.72,
"last_assessed": "2026-11-01T10:30:00Z",
"sr_interval_days": 13,
"sr_next_review": "2026-11-14T10:30:00Z",
"misconceptions": [
{
"id": "misc_007",
"description_fa": "تصور اشتباه: ایندکسر فقط فایل‌های TS را پشتیبانی می‌کند",
"corrected_in_session": "session_2026_10_28"
}
]
}
```
### ۲.۳ ادغام علوم شناختی از منابع مکمل
از AITutoR (دانشگاه گلاسگو): ۴ ستون شناختی:
از Tov-learn: فرمت آموزشی ۴ بخشی `Journey` (`Problem → Insight → In Your Project → Reflection Question`) با اتصال مستقیم مفهوم به کد واقعی مخزن.
از doceo: مصاحبه کالیبراسیون ۳۰ ثانیه‌ای اولیه و تبدیل هر پوشه ترسناک به درس بصری تک‌صفحه‌ای.
---
## فصل سوم — معماری کامل اسکیل `phase0-omni-audit`
### ۳.۱ ساختار دایرکتوری اسکیل
```
.agents/skills/phase0-omni-audit/
├── SKILL.md # مانیفست اسکیل (< 500 خط)
├── scripts/
│ ├── 00-index.sh # ایندکس‌گذاری CKG (CBM + CodeGraph + Graphify)
│ ├── 01-wiki-compile.sh # کامپایل ویکی خودنگهدار
│ ├── 02-arch-govern.sh # حکمرانی معماری (tach + dependency-cruiser)
│ ├── 03-security-audit.sh # ممیزی امنیتی (Semgrep + CodeQL + SARIF)
│ ├── 04-visualize.sh # تولید داشبوردهای بصری
│ ├── 05-learn-graph.sh # ساخت گراف یادگیری از گراف کد
│ └── utils/
│ ├── merge-graphs.py # ادغام خروجی‌های CKG مختلف
│ └── health-grade.py # محاسبه نمره سلامت A-F
├── config/
│ ├── mcp-servers.json # پیکربندی سرورهای MCP
│ ├── tach.toml # قواعد مرزهای معماری
│ ├── .dependency-cruiser.js # قواعد وابستگی JS/TS
│ └── semgrep-rules/ # قواعد امنیتی سفارشی
├── templates/
│ ├── wiki-profile.json # اسکیمای پروفایل ویکی (.llmwiki/)
│ ├── dashboard.html # قالب داشبورد تعاملی
│ └── explainer-template.json # قالب Archify Explainer
└── schemas/
├── unified-graph.schema.json
└── competence-node.schema.json
```
### ۳.۲ فایل SKILL.md (خلاصه ساختاری)
```yaml
---
name: phase0-omni-audit
description: >
Comprehensive codebase intelligence skill that orchestrates
code knowledge graphs, self-maintaining wikis, architecture
governance, security audits, and interactive visualizations.
Produces a unified knowledge graph with learning-ready nodes.
version: 1.0.0
triggers:
dependencies:
mcp_servers:
cli_tools:
optional:
---
```
قوانین اجرا:
### ۳.۳ خط لوله اجرایی اسکیل
```
Phase 1: Index (00-index.sh)
├── codebase-memory-mcp daemon start → index project
├── codegraph index .
├── [optional] graphify scan .
└── merge-graphs.py → unified-graph.json
Phase 2: Wiki (01-wiki-compile.sh)
├── llmwiki init --codebase (یا pi-codebase-wiki)
├── doc0 verify-graph (دروازه ضدتوهم)
└── wiki/INDEX.md + entities/ + concepts/
Phase 3: Governance (02-arch-govern.sh)
├── tach init → tach check (strict: true)
├── dependency-cruiser (JS/TS)
├── tests/test_architecture.py (30+ تست منفی)
└── co-change analysis (Git forensics)
Phase 4: Security (03-security-audit.sh)
├── semgrep --config=auto
├── CodeQL analyze
├── SARIF merge → security-report.json
└── hardcoded secrets scan + eval() detection
Phase 5: Visualize (04-visualize.sh)
├── archify explainer (معماری + جریان داده)
├── codecharta ccsh (نقشه شهر 3D)
├── CBM Lens --ui=true (کهکشان 3D)
└── codeflow dashboard.html (بوم تعاملی)
Phase 6: Learn Graph (05-learn-graph.sh)
├── Extract propositions from wiki
├── Map to AST symbols
├── Initialize competence nodes (score=0)
└── Generate onboarding tour
```
---
## فصل چهارم — معماری مرجع هارنس دومنظوره
### ۴.۱ هسته مبتنی بر Append-Only EventLog
```python
# models.py — Pydantic Immutable Models
from pydantic import BaseModel, Field
from datetime import datetime
from enum import Enum
from typing import Union
class EventType(str, Enum):
MESSAGE = "message"
ACTION = "action"
OBSERVATION = "observation"
AGENT_ERROR = "agent_error"
CONDENSATION = "condensation"
COMPETENCE_UPDATE = "competence_update"
PROPOSITION_ADDED = "proposition_added"
class Event(BaseModel):
id: str = Field(default_factory=lambda: str(uuid4()))
timestamp: datetime = Field(default_factory=datetime.utcnow)
event_type: EventType
payload: dict
class Config:
frozen = True # تغییرناپذیر
class ConversationState(BaseModel):
events: list[Event] = []
token_count: int = 0
condensation_count: int = 0
# Agent as Pure Function
def agent_step(history: list[Event]) -> "Action":
"""History → Action (تابع خالص)"""
...
```
### ۴.۲ رابط ایجنت-کامپیوتر (ACI) سه‌کنشی
```python
class RunCommand(BaseModel):
command: str
timeout_seconds: int = 30
class EditFile(BaseModel):
path: str
old_content: str
new_content: str
# لینتر درون‌خطی: پس از هر ویرایش، اجرای خودکار:
# 1. لینتر نحوی زبان
# 2. tach check (مرزهای معماری)
# 3. ccsh gate (آستانه پیچیدگی)
class Finish(BaseModel):
summary: str
artifacts: list[str] = []
Action = Union[RunCommand, EditFile, Finish]
```
### ۴.۳ قلاب‌های رهگیری
```python
class PreToolUseHook:
"""قبل از Read/Grep/Glob:
INTERCEPTED_TOOLS = ["Read", "Grep", "Glob"]
async def before(self, tool_name: str, args: dict) -> str | None:
if tool_name in self.INTERCEPTED_TOOLS:
# پرس‌وجو از گراف
graph_result = await self.query_graph(args)
if graph_result.confidence > 0.8:
return graph_result.formatted()
return None # اجازه اجرای ابزار اصلی
class SessionStartHook:
"""در شروع هر نشست:
...
```
### ۴.۴ کنترل زمینه Git-گونه (GCC)
```python
class GitContextControl:
"""عملیات صریح روی حافظه کاری ایجنت"""
def commit(self, message: str):
"""ثبت وضعیت فعلی زمینه"""
snapshot = self.serialize_context()
self.context_log.append(ContextCommit(
message=message,
snapshot=snapshot,
token_count=self.count_tokens(snapshot)
))
def branch(self, name: str):
"""ایجاد شاخه جدید زمینه برای کاوش"""
self.branches[name] = deepcopy(self.current_context)
def merge(self, branch_name: str, strategy="ours"):
"""ادغام شاخه زمینه"""
...
def context(self, query: str) -> str:
"""بازیابی هوشمند زمینه مرتبط"""
return self.retriever.query(query,
sources=["graph", "wiki", "events"])
```
### ۴.۵ Condenser و StuckDetector
```python
class Condenser:
THRESHOLD_TOKENS = 135_000 # کدنویسی
LEARN_THRESHOLD = 45_000 # نشست‌های آموزشی
async def maybe_condense(self, state: ConversationState):
if state.token_count > self.threshold:
summary = await self.summarize(state.events)
condensation_event = Event(
event_type=EventType.CONDENSATION,
payload={"summary": summary,
"events_condensed": len(state.events)}
)
# رویداد روی دیسک حفظ می‌شود
state.events = [condensation_event]
class StuckDetector:
"""۵ الگوی شناسایی گیرافتادگی"""
PATTERNS = [
"repeated_identical_edits",
"oscillating_between_two_states",
"monotonic_error_count_increase",
"empty_shell_output_loop",
"exceed_max_iterations"
]
```
### ۴.۶ پروفایل‌های چندایجنتی
| پروفایل | نقش | دسترسی |
|---------|-----|--------|
| Scout/Explorer | کاوش صرفاً خواندنی روی گراف | فقط Read + Query Graph |
| Worker | کدنویسی موازی | Git Worktree ایزوله + EditFile |
| Auditor | ممیزی متخاصم | Read + tach check + security scan |
| Socratic Tutor | مربی‌گری سقراطی | Read Graph + Competence Graph + Practice Engine |
| Sentinel | هماهنگ‌کننده | تمام دسترسی‌ها + Orchestration |
### ۴.۷ حلقه‌های پس‌زمینه (الگوی CodeAlmanac)
```python
class SyncDaemon:
"""هر ۵ ساعت: اسکن لاگ مکالمات JSONL با ایجنت‌ها
و استخراج دانش مفید برای ورود به ویکی"""
interval_hours = 5
class GardenDaemon:
"""هر ۲۴ ساعت: هرس صفحات قدیمی،
بهینه‌سازی لینک‌های ضعیف ویکی،
به‌روزرسانی competence scores"""
interval_hours = 24
```
---
## فصل پنجم — مهندسی داشبورد BiDi/RTL و تایپوگرافی فارسی
### ۵.۱ کامپوننت‌های متن‌باز انتخاب‌شده
| لایه | کامپوننت | دلیل انتخاب |
|------|---------|------------|
| پوسته | LearnHarness (Next.js + Tailwind) | پشتیبانی بومی RTL در PR #457، KaTeX، گراف دانش |
| مدیریت پنجره | Dockview | داک‌های تودرتو، Tab Groups، تم تاریک |
| گراف تعاملی | React Flow (`@xyflow/react`) | هر گره یک کامپوننت کامل DOM — ایده‌آل برای متن فارسی |
| گراف سه‌بعدی | Three.js + CBM Lens | نمای کهکشانی برای کدبیس‌های بزرگ |
| دیاگرام | Archify Renderer | ۱۰ نوع دیاگرام + Explainer |
| بوم کد | CodeFlow (React 18 + D3 v7) | کارت‌های فایل کامل روی بوم بی‌نهایت |
| ویکی‌خوان | pi-codebase-wiki Content Viewer | تم تاریک، wikilinks دوطرفه |
| فرمول | KaTeX (با فیکس #481) | کپی سورس TeX |
### ۵.۲ قواعد CSS BiDi — مرجع کامل
```css
/* ===== 1. کانتینر ریشه ===== */
:root {
direction: rtl;
/* متغیرهای تایپوگرافی دوزبانه */
--font-heading-fa: 'Lalezar', 'IBM Plex Sans Arabic', sans-serif;
--font-body-fa: 'Vazirmatn', 'IBM Plex Sans Arabic', sans-serif;
--font-heading-en: 'Unbounded', 'Space Grotesk', sans-serif;
--font-body-en: 'Space Grotesk', sans-serif;
--font-mono: 'JetBrains Mono', monospace;
/* تم تاریک عمیق OLED-Void */
--bg-void: #000000;
--bg-surface: #0a0a0f;
--bg-card: #111118;
--text-primary: #e4e4ed;
--text-secondary: #8b8b9e;
--accent-primary: #6366f1; /* Indigo */
--accent-success: #22c55e;
--accent-danger: #ef4444;
}
/* ===== 2. پاراگراف‌های فارسی ===== */
.prose-fa,
[lang="fa"] p,
.wiki-body p {
direction: rtl;
unicode-bidi: plaintext; /* یا dir="auto" */
font-family: var(--font-body-fa);
line-height: 1.8;
text-align: right;
}
/* ===== 3. ایزولاسیون عناصر LTR درون متن فارسی ===== */
.code-inline,
.function-name,
.file-path,
.ast-label,
.graph-node-label code,
.katex-display {
direction: ltr;
unicode-bidi: isolate;
font-family: var(--font-mono);
}
/* بلوک‌های کد */
pre, code, .monaco-editor {
direction: ltr !important;
unicode-bidi: isolate !important;
text-align: left !important;
font-family: var(--font-mono);
}
/* ===== 4. گره‌های React Flow ===== */
.react-flow__node {
direction: rtl;
}
.react-flow__node .node-title {
font-family: var(--font-heading-fa);
unicode-bidi: plaintext;
}
.react-flow__node .node-code-ref {
direction: ltr;
unicode-bidi: isolate;
font-family: var(--font-mono);
font-size: 0.75rem;
}
/* ===== 5. Dockview Panels ===== */
.dockview-theme-dark {
--dv-activeTab-background: var(--bg-card);
--dv-tab-font-family: var(--font-body-fa);
}
.dockview-panel[data-panel-type="wiki"] {
direction: rtl;
}
.dockview-panel[data-panel-type="terminal"] {
direction: ltr;
}
/* ===== 6. سلسله‌مراتب تایپوگرافی ===== */
h1, h2, h3 {
font-family: var(--font-heading-fa);
}
h1:lang(en), h2:lang(en), h3:lang(en) {
font-family: var(--font-heading-en);
}
/* ===== 7. رفع مشکل پرانتز و نقطه ===== */
.bidi-safe {
/* جلوگیری از جابه‌جایی پرانتز و نقطه */
unicode-bidi: isolate-override;
}
/* برای مسیرهای فایل درون جملات فارسی */
.inline-path {
direction: ltr;
unicode-bidi: embed;
background: var(--bg-card);
padding: 0.1em 0.3em;
border-radius: 3px;
}
```
### ۵.۳ سلسله‌مراتب تایپوگرافی دوزبانه
| سطح | فونت فارسی | فونت انگلیسی | سایز | وزن |
|-----|-----------|-------------|------|-----|
| H1 — عنوان صفحه | Lalezar | Unbounded | 2rem | 400 |
| H2 — سرفصل | IBM Plex Sans Arabic | Space Grotesk | 1.5rem | 700 |
| H3 — زیرسرفصل | Vazirmatn | Space Grotesk | 1.25rem | 600 |
| بدنه ویکی | Vazirmatn | Space Grotesk | 1rem | 400 |
| گره‌های گراف | IBM Plex Sans Arabic | Space Grotesk | 0.875rem | 500 |
| کد / ترمینال | — | JetBrains Mono | 0.8125rem | 400 |
| برچسب AST | — | JetBrains Mono | 0.75rem | 500 |
### ۵.۴ الگوریتم رندر BiDi در بوم‌های گراف: DOM در برابر Canvas/WebGL
| رویکرد | مزیت BiDi | محدودیت |
|--------|----------|--------|
| React Flow (DOM) | ✅ هر گره یک HTML element کامل با پشتیبانی بومی `dir` و `unicode-bidi` | عملکرد تا ~۵۰۰۰ گره |
| Sigma.js (WebGL) | ❌ Text Shaping فارسی در WebGL خام مشکل‌ساز | عملکرد عالی ۱۰۰K+ گره |
| vis-network (Canvas) | ⚠️ نیاز به `measureText` سفارشی برای فارسی | عملکرد متوسط |
| Three.js + HTML Overlay | ✅ لیبل‌های HTML روی صحنه 3D | بهترین ترکیب: 3D + BiDi |
نتیجه‌گیری: برای داشبورد ما، React Flow برای گراف‌های تعاملی اصلی (گراف دانش، نقشه درس، وابستگی‌ها) و Three.js با HTML Overlay برای نماهای سه‌بعدی (شهر کد، کهکشان) بهترین انتخاب هستند.
---
## فصل ششم — اسکیمای یکپارچه داده و آنتالوژی
### ۶.۱ انواع گره‌ها در گراف واحد
```json
{
"$schema": "unified-graph-node",
"node_types": {
"code_file": {
"fields": ["path", "language", "loc", "complexity", "last_modified"],
"edges_out": ["IMPORTS", "CONTAINS"]
},
"code_symbol": {
"subtypes": ["function", "class", "method", "variable", "type"],
"fields": ["name", "signature", "docstring", "start_line", "end_line"],
"edges_out": ["CALLS", "INHERITS", "IMPLEMENTS", "RETURNS"]
},
"infra_resource": {
"subtypes": ["docker_service", "k8s_deployment", "terraform_resource",
"helm_chart", "ci_pipeline", "sql_table"],
"fields": ["resource_type", "config_path", "config_line"],
"edges_out": ["DEPENDS_ON", "DEPLOYS", "CONNECTS_TO"]
},
"wiki_article": {
"subtypes": ["concept", "entity", "module_doc", "service_doc",
"comparison", "overview", "ADR", "invariant",
"domain_flow", "gotcha"],
"fields": ["title", "title_fa", "body_md", "last_verified",
"staleness_days", "evidence_hashes"],
"edges_out": ["WIKILINK", "EXPLAINS_SYMBOL", "CITES_COMMIT"]
},
"proposition": {
"fields": ["statement", "statement_fa", "confidence",
"source_session_id", "extraction_timestamp"],
"edges_out": ["HAS_PREMISE", "HAS_CONCLUSION",
"COVERS_SYMBOL", "CONTRADICTS"]
},
"premise": {
"fields": ["content", "content_fa", "verified", "source_ref"],
"edges_out": ["SUPPORTS"]
},
"competence_record": {
"fields": ["learner_id", "mastery_score", "attempts",
"last_assessed", "sr_interval_days", "sr_next_review",
"misconceptions"],
"edges_out": ["ASSESSED_ON_SYMBOL", "ASSESSED_ON_PROPOSITION",
"MISCONCEPTION_ABOUT"]
}
},
"edge_confidence_labels": ["EXTRACTED", "INFERRED", "AMBIGUOUS"],
"trust_gates": {
"write_path": {
"require_line_ref_or_hash": true,
"fail_action": "send_to_review_queue"
}
}
}
```
### ۶.۲ ذخیره‌سازی (SQLite + فایل)
```sql
-- جدول اصلی گره‌ها
CREATE TABLE nodes (
id TEXT PRIMARY KEY,
node_type TEXT NOT NULL,
subtype TEXT,
data JSON NOT NULL, -- فیلدهای خاص هر نوع
created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
content_hash TEXT -- SHA256 برای کش تدریجی
);
-- جدول یال‌ها
CREATE TABLE edges (
source_id TEXT REFERENCES nodes(id),
target_id TEXT REFERENCES nodes(id),
edge_type TEXT NOT NULL,
confidence TEXT DEFAULT 'EXTRACTED', -- EXTRACTED|INFERRED|AMBIGUOUS
weight REAL DEFAULT 1.0,
metadata JSON,
PRIMARY KEY (source_id, target_id, edge_type)
);
-- جست‌وجوی تمام‌متن
CREATE VIRTUAL TABLE nodes_fts USING fts5(
id, content,
tokenize='unicode61' -- پشتیبانی از یونیکد فارسی
);
-- تکرار فاصله‌دار
CREATE TABLE sr_schedule (
competence_id TEXT REFERENCES nodes(id),
symbol_id TEXT REFERENCES nodes(id),
interval_days INTEGER DEFAULT 1,
ease_factor REAL DEFAULT 2.5,
next_review DATE,
review_count INTEGER DEFAULT 0
);
```
### ۶.۳ فرمت Markdown Frontmatter برای صفحات ویکی
```yaml
---
type: concept # concept|entity|module_doc|ADR|invariant|...
title: Context Engineering
title_fa: مهندسی زمینه
symbols:
wikilinks:
evidence:
file: "src/harness/gcc.py"
lines: "45-78"
staleness_threshold_days: 14
last_verified: 2026-11-01
competence_coverage:
propositions: ["prop_042", "prop_043", "prop_044"]
avg_mastery: 0.65
---
```
---
## فصل هفتم — ماتریس نهایی انتخاب ویژگی‌های برتر (Golden Feature Matrix)
| ویژگی / الگوریتم | منبع (پروژه متن‌باز) | ماژول مقصد در اسکیل/هارنس |
|---|---|---|
| خط لوله ۷ ایجنت تحلیل | Understand-Anything | `00-index.sh` (فاز Index) |
| ایندکس‌گذاری ۱۶۲ زبان + Cypher | codebase-memory-mcp | MCP Server اصلی |
| کاهش ۵۹٪ توکن + FTS5 | CodeGraph | MCP Server کمکی |
| کاهش ۹۰-۹۵٪ توکن + Leiden | Graphify | گراف اسناد + کد |
| بیت‌ست‌های شعاع انفجار | rgctl | تحلیل blast-radius |
| برچسب‌های اطمینان یال‌ها | Graphify | اسکیمای گراف (`confidence` field) |
| ویکی خودنگهدار + دروازه ضدتوهم | doc0 + llm-wiki-compiler | `01-wiki-compile.sh` |
| حلقه‌های Sync/Garden | CodeAlmanac | دیمن‌های پس‌زمینه هارنس |
| ویکی‌خوان + wikilinks + گراف | pi-codebase-wiki | پنل ویکی داشبورد |
| بازیابی ترکیبی (BM25 + گراف) | Klore | موتور جست‌وجوی هارنس |
| قفل مرزهای معماری Python | tach | `02-arch-govern.sh` |
| قفل مرزهای JS/TS | dependency-cruiser | `02-arch-govern.sh` |
| ممیزی امنیتی SARIF | Semgrep + CodeQL | `03-security-audit.sh` |
| Co-change Pairs (جفت‌شدگی زمانی) | Git Forensics (CodeScene) | `02-arch-govern.sh` |
| ۱۰ نوع دیاگرام + Explainer | Archify v3.2 | `04-visualize.sh` |
| شهر سه‌بعدی + TF-IDF دامنه | CodeCharta | `04-visualize.sh` |
| کهکشان سه‌بعدی + Galaxy View | CBM Lens | پنل 3D داشبورد |
| بوم بی‌نهایت + Blast Radius | CodeFlow | پنل بوم داشبورد |
| Append-Only EventLog | OpenHands V1 + Mini-SWE-agent | هسته هارنس (`event_log.py`) |
| ACI سه‌کنشی + لینتر درون‌خطی | SWE-agent ACI | `aci.py` |
| قلاب PreToolUse | Graphify + CBM | `hooks.py` |
| GCC (COMMIT/BRANCH/MERGE) | Antigravity | `gcc.py` |
| Condenser + StuckDetector | OpenHands V1 | `condenser.py` |
| ارکستراسیون Git Worktrees | Antigravity /teamwork | `orchestrator.py` |
| چرخه Probe→Plan→Teach→Practice | LearnHarness v0.4.1 | ایجنت Socratic Tutor |
| گراف گزاره و مقدمه | LearnHarness | `proposition_graph.py` |
| تکرار فاصله‌دار فیبوناچی | Tov-learn (۲,۱۳,۳۴,۸۹ روز) | `sr_scheduler.py` |
| Knowledge Tracing (BKT/DKT) | TutorAI | `competence_tracker.py` |
| فرمت Journey ۴ بخشی | Tov-learn | قالب درس‌های آموزشی |
| درس بصری تک‌صفحه‌ای | doceo | `visual_lesson.py` |
| مسیر یادگیری ماندگار | coding-tutor | `learning_trail.py` |
| Learning DNA Profile | ai-learning-path-generator | `learner_profile.py` |
| پرامپت‌های ضدچاپلوسی | AITutoR (گلاسگو) | System prompts |
| پشتیبانی RTL | LearnHarness PR #457 | CSS/Layout داشبورد |
| React Flow (DOM-based graph) | @xyflow/react | گراف تعاملی فارسی |
| Dockview (پنجره‌های داک‌شونده) | Dockview | پوسته داشبورد |
---
## فصل هشتم — نقشه راه اجرایی گام‌به‌گام
### فاز ۱: اسکیل MVP (هفته ۱-۲)
| گام | عملیات | گیت راستی‌آزمایی |
|-----|--------|-----------------|
| 1.1 | نصب CBM + CodeGraph + Archify | هر سه سرور MCP پاسخ‌دهنده |
| 1.2 | نوشتن `SKILL.md` و `00-index.sh` | ایندکس مخزن فاز صفر < ۶۰ ثانیه |
| 1.3 | نوشتن `01-wiki-compile.sh` | `wiki/INDEX.md` تولید شده با ≥۵ صفحه |
| 1.4 | نوشتن `02-arch-govern.sh` | `tach check` بدون خطا یا خطاهای شناخته‌شده |
| 1.5 | نوشتن `04-visualize.sh` | دیاگرام Archify + داشبورد HTML تولید شده |
| Gate 1 | اجرای کامل اسکیل با `/audit` | گزارش `health-report.json` با نمره A-F |
### فاز ۲: ویکی خودنگهدار (هفته ۳)
| گام | عملیات | گیت راستی‌آزمایی |
|-----|--------|-----------------|
| 2.1 | ادغام doc0 Graph Verification Gate | ۰ نام تابع/کلاس ناموجود در ویکی |
| 2.2 | پیاده‌سازی `wiki lint` + staleness detection | صفحات یتیم/کهنه شناسایی شده |
| 2.3 | ادغام wikilinks دوطرفه | کلیک روی `[[Module X]]` → صفحه مقصد |
| Gate 2 | `llmwiki eval` | امتیاز پشتیبانی ادعاها ≥ ۰.۸۵ |
### فاز ۳: هسته هارنس (هفته ۴-۵)
| گام | عملیات | گیت راستی‌آزمایی |
|-----|--------|-----------------|
| 3.1 | پیاده‌سازی EventLog + مدل‌های Pydantic | بازپخش کامل ۱۰ نشست ذخیره‌شده |
| 3.2 | پیاده‌سازی ACI سه‌کنشی + لینتر | ویرایش → لینتر → خطا/موفقیت فوری |
| 3.3 | پیاده‌سازی Condenser | فشرده‌سازی در آستانه ۱۳۵K توکن |
| 3.4 | پیاده‌سازی GCC | عملیات COMMIT/BRANCH/MERGE |
| 3.5 | پیاده‌سازی PreToolUse Hook | ≥ ۸۰٪ پرس‌وجوها از گراف قبل از Grep |
| Gate 3 | حل ۳ issue واقعی از مخزن فاز صفر | مقایسه توکن: با/بدون هارنس |
### فاز ۴: موتور یادگیری (هفته ۶-۷)
| گام | عملیات | گیت راستی‌آزمایی |
|-----|--------|-----------------|
| 4.1 | پیاده‌سازی چرخه Probe→Plan→Teach→Practice | نشست آزمایشی کامل ۴ مرحله |
| 4.2 | ساخت Proposition Graph متصل به AST | ≥ ۲۰ گزاره متصل به نمادهای کد |
| 4.3 | پیاده‌سازی Competence Tracker (رفع #115) | امتیاز تسلط روی گره‌های گراف |
| 4.4 | تکرار فاصله‌دار فیبوناچی | زمان‌بندی مرور بعدی محاسبه‌شده |
| Gate 4 | آموزش ۳ ماژول کدبیس فاز صفر | نقشه تسلط با ≥ ۳ سطح رنگی |
### فاز ۵: داشبورد BiDi (هفته ۸-۹)
| گام | عملیات | گیت راستی‌آزمایی |
|-----|--------|-----------------|
| 5.1 | پوسته Next.js + Dockview + تم تاریک | پنجره‌های داک‌شونده عملیاتی |
| 5.2 | گراف React Flow + فونت‌های فارسی | متن فارسی بدون جابه‌جایی پرانتز |
| 5.3 | ویکی‌خوان + جست‌وجو | جست‌وجوی فارسی + انگلیسی |
| 5.4 | نمای Three.js Galaxy | نمایش ۳D کدبیس |
| 5.5 | پنل Practice (Dockable) | برگه‌های تمرین تمام‌صفحه |
| Gate 5 | تست ۵ کاربر فارسی‌زبان | ≥ ۴.۰/۵.۰ رضایت BiDi |
### فاز ۶: ادغام و بهینه‌سازی (هفته ۱۰)
| گام | عملیات | گیت راستی‌آزمایی |
|-----|--------|-----------------|
| 6.1 | ادغام حلقه‌های Sync/Garden | به‌روزرسانی خودکار ویکی |
| 6.2 | ارکستراسیون چندایجنتی | ≥ ۲ Worker موازی در Git Worktrees |
| 6.3 | بسته‌بندی Tauri v2 / Electron | اپلیکیشن دسکتاپ بومی |
| Gate 6 (نهایی) | دمو کامل اسکیل + هارنس + داشبورد | ویدیوی ۵ دقیقه‌ای walkthrough |
---
## خلاصه اجرایی
این گزارش یک Blueprint مهندسی کامل ارائه می‌دهد که از کالبدشکافی عمیق ابزارهای موجود تا طراحی معماری هارنس دومنظوره و مهندسی داشبورد BiDi/فارسی را پوشش می‌دهد. نقاط کلیدی:
2. هارنس دومنظوره از الگوی Append-Only EventLog (OpenHands) + ACI سه‌کنشی (SWE-agent) + چرخه پداگوژیکی (LearnHarness) + گراف واحد (کد + دانش + تسلط) تشکیل شده و مشکل Issue #115 را با اتصال مستقیم `CompetenceRecord` به گره‌های AST حل می‌کند.
3. داشبورد BiDi با انتخاب React Flow (DOM-based برای پشتیبانی بومی فارسی)، Dockview (پنجره‌های داک‌شونده) و قواعد CSS دقیق `unicode-bidi: isolate` / `plaintext` رندر بی‌نقص متون دوجهته را تضمین می‌کند.
```


---

*Exported from [Voyager](https://github.com/voyager-crew/voyager)*  
*Generated on November 6, 2026 at 12:48 AM*