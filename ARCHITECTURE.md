# 🏛️ سند جامع معماری، فرمول‌های ریاضی و مقادیر طلایی (`ARCHITECTURE.md`)

این سند، قراردادهای فنی، معادلات ریاضی و مقادیر مرجع تست (`Golden Values`) را برای هر سه زیرسیستم **`F1uent`** (هارنس کد و یادگیری)، **`F1uxus`** (موتور اسناد و خزانه دو-زمانی BiDi) و **`MJNexus`** (رادار ابزار و ۱۷ دامنه دانش) تعریف می‌کند.

---

## ۱. لایه‌بندی مکانیکی کد (`Layered Sink Architecture`)

```text
[src.f1uway.server]   -> FastAPI Local Bridge + SSE Stream
       ↓
[src.f1uway.agent]    -> LangGraph Orchestrator + 5 Agent Profiles (Scout/Worker/Auditor/Tutor/Sentinel)
       ↓
[src.f1uway.harness]  -> Append-Only EventLog + 3-Action ACI + GCC (Commit/Branch/Merge) + Condenser
       ↓
[src.f1uway.store]    -> Git Markdown Vault + SQLite Shadow Index + Postgres pgvector/RCTE + Radar DB
       ↓
[src.f1uway.core]     -> Strict Pydantic Contracts + Persian BiDi Offset Map + Ontology Interner + ThreadBox DAG + BKT/FSRS-6
```

---

## ۲. فرمول‌های ریاضی هسته و مقادیر طلایی (`Golden Values`)

### ۲.۱. ردیابی دانش بیزی (`Bayesian Knowledge Tracing - BKT`)
برای هر نماد کد (`AST Symbol`) یا مفهوم هستی‌شناسی (`ONT_*`)، احتمال تسلط یادگیرنده پس از مشاهده پاسخ درست ($	ext{obs}=1$) یا غلط ($	ext{obs}=0$) در دو گام محاسبه می‌شود:
- **گام ۱ (احتمال پسین):**
  $$P(L_t \mid 	ext{obs}=1) = rac{P(L_{t-1})(1 - P(S))}{P(L_{t-1})(1 - P(S)) + (1 - P(L_{t-1}))P(G)}$$
  $$P(L_t \mid 	ext{obs}=0) = rac{P(L_{t-1})P(S)}{P(L_{t-1})P(S) + (1 - P(L_{t-1}))(1 - P(G))}$$
- **گام ۲ (انتقال یادگیری):**
  $$P(L_t) = P(L_t \mid 	ext{obs}) + ig(1 - P(L_t \mid 	ext{obs})ig) \cdot P(T)$$
- **مقدار طلایی الزامی در تست واحد (`Golden Value #1`):**
  به ازای $P(L_{t-1}) = 0.40$، $	ext{obs}=1$، $P(T)=0.15$، $P(S)=0.10$ و $P(G)=0.20$:
  $$P(L_t \mid 1) = rac{0.36}{0.36 + 0.12} = 0.75 \implies P(L_t) = 0.75 + 0.25 	imes 0.15 = \mathbf{0.7875}$$

### ۲.۲. الگوریتم تکرار فاصله‌دار آزاد نسخه ۶ (`FSRS-6`)
- **منحنی فراموشی و قابلیت بازیابی ($R$):**
  $$R(t, S) = \left(1 + rac{t}{9 \cdot S}ight)^{-1}$$
- **به‌روزرسانی دشواری ($D \in [1, 10]$) و پایداری حافظه ($S$ برحسب روز):**
  به ازای نمره ارزیابی $g \in \{1	ext{ (Again)}, 2	ext{ (Hard)}, 3	ext{ (Good)}, 4	ext{ (Easy)}\}$، برای $g \ge 3$ پایداری افزایش یافته ($S' > S$) و برای $g = 4$ دشواری کاهش می‌یابد ($D' < D$).

### ۲.۳. بازیابی هیبریدی سه‌فهرسته (`Triple-List RRF`) و تعامل دیرهنگام (`MaxSim`)
$$	ext{RRF}(d) = rac{w_{	ext{dense}}}{60 + r_{	ext{dense}}(d)} + rac{0.5 \cdot w_{	ext{lex}}}{60 + r_{	ext{stemmed}}(d)} + rac{0.5 \cdot w_{	ext{lex}}}{60 + r_{	ext{simple}}(d)}$$
$$S_{	ext{MaxSim}}(Q, D) = \sum_{i=1}^{|Q|} \max_{j=1}^{|D|} \left( E_{q, i} \cdot 	ilde{E}_{d, j}^	op ight)$$

### ۲.۴. آنتروپی معنایی (`Semantic Entropy`) و وفاداری اتمی (`FActScore`)
$$SE(\mathbf{x}) = -\sum_{c \in \mathcal{C}} P(c \mid \mathbf{x}) \log P(c \mid \mathbf{x}), \quad 	ext{FActScore}(y) = rac{1}{|A(y)|} \sum_{a_i \in A(y)} \mathbb{I}ig[	ext{supported}(a_i, \mathcal{K})ig]$$

### ۲.۵. نگاشت افست کاراکتری در نرمال‌سازی فارسی (`Golden Value #2`)
در رشته خام `"سلام بر كتاب‌های علمی"`، پس از تبدیل `"ك"` عربی به `"ک"` فارسی و نیم‌فاصله (`‌`) به فاصله استاندارد، عبارت نرمال‌شده `"کتاب های"` باید از طریق آرایه `norm_to_raw_index` دقیقاً به بازه کاراکتری اصلی `(8, 20)` یعنی زیررشته `"كتاب‌های"` در متن خام نگاشت شود.
