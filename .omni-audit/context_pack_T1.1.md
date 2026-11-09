[F1_DETERMINISTIC_PREFIX_CACHE_HEADER v1.0]
- ONT_PUSHDOWN_AUTOMATON_CONSTRAINED_DECODING: ماسک کردن لاجیت‌های نامعتبر با اتوماتای پشته‌ای (PDA) برای تضمین ۱۰۰٪ صحت نحوی JSON و الزام به تقدم فیلد استدلال بر حکم نهایی.
- ONT_PYDANTIC_EXTRA_FORBID: منع ورود فیلدهای تعریف‌نشده (extra=forbid) و تغییرناپذیری شیء (frozen=True) در Pydantic v2 با سربار زمانی نزدیک به صفر در هسته Rust.

### [CONTRACT]
## ۲. قرارداد فنی ماشینی (`ZONE:CONTRACT` — برش ارسالی به هوش مصنوعی)
- تمامی مدل‌های داده در `src/f1_core/contracts.py` باید دارای `ConfigDict(extra="forbid", frozen=True)` باشند.
- در مدل `ConstrainedLLMResponse`، دو فیلد `reasoning_chain` و `evidence_quote` باید اولین کلیدهای کلاس باشند تا در رمزگشایی مقید به اتوماتای پشته‌ای (PDA) زنجیره استدلال پیش از حکم نهایی تولید شود.
- متد `OntologyRegistry.intercept_branch_spawn` باید برای تطابق‌های $\ge 0.92$ وضعیت `ZERO_TOKEN_HIT` و برای سوالات زاویه جدید روی مفهوم موجود وضعیت `DELTA_PROMPT_MODE` برگرداند.

### [GOLDEN_VALUES]
## ۳. مقادیر طلایی تست (`ZONE:GOLDEN_VALUES` — مرجع راستی‌آزمایی قطعی)
- **آپدیت BKT (`update_bkt_mastery`):** برای `p_known_prior=0.40` با پاسخ درست (`is_correct=True`, `p_transit=0.15`, `p_slip=0.10`, `p_guess=0.20`)، مقدار خروجی باید دقیقاً `0.7875` باشد.
- **نگاشت افست فارسی (`normalize_persian_with_offsets`):** در رشته `"كتاب‌ها"`، تبدیل `"ك"` عربی به `"ک"` فارسی و نیم‌فاصله به فاصله، باید بازه نرمال‌شده را بدون خطا به بازه اصلی `(0, 7)` نگاشت کند.
