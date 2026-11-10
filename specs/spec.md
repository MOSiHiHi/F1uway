---
ont_id: ONT_F1UENT_PLAYBOOKS_SPEC
source_project: F1uent-Ecosystem
domain: playbooks
title_fa: "قرارداد رسمی مشخصات سیستم (`specs/spec.md` — SDD Single Source of Truth)"
content_is_data: true
---
<!-- ZONE:HUMAN_INTUITION_START -->
# قرارداد رسمی مشخصات سیستم (`specs/spec.md` — SDD Single Source of Truth)

## ۱. نمای کلی و سناریوهای کاربری اولویت‌بندی‌شده

### سناریوی P1 (حیاتی — هسته تعامل و حذف توکن تکراری):
- **شرح:** کاربر یا ایجنت حین مطالعه یک متن یا نوشتن کد، روی عبارت یا نماد $X$ یک مستطیل انشعاب (`ThreadBox`) ایجاد می‌کند.
- **دلیل اولویت P1:** بدون این مکانیسم، هم جریان تفکر غیرخطی انسان شکسته می‌شود و هم برای مفاهیم تکراری بارها هزینه API پرداخت می‌گردد.
- **معیارهای پذیرش (`Acceptance Criteria`):**
  - [x] اگر $X$ قبلاً در `notebook/ontology/ONT_*.md` ثبت شده باشد (شباهت $\ge 0.92$)، پاسخ باید در کمتر از ۵ میلی‌ثانیه و با مصرف **۰ توکن API** در مستطیل فرزند درج و تقطیر شود (`ZERO_TOKEN_HIT`).
  - [x] اگر سوال جدیدی درباره مفهوم موجود پرسیده شود، فقط چکیده ۲ خطی قبلی + سوال تفاضلی ارسال گردد (`DELTA_PROMPT_MODE`).

### سناریوی P2 (معماری دوچهره مستندات و همگام‌سازی کد):
- **شرح:** پلی‌بوک‌های آموزشی انسان باید حاوی صدها خط داستان علمی، کدهای زنده و تاریخچه مستطیل‌های چت باشند، بدون آنکه پرامپت ارسالی به هوش مصنوعی متورم شود.
- **معیارهای پذیرش:**
  - [x] دستور `devloop.py sync-embeds` سورس واقعی توابع/کلاس‌ها را از `src/` داخل بلوک‌های `<!-- EMBED: ... -->` پلی‌بوک‌ها به‌روز کند.
  - [x] دستور `devloop.py pack` صرفاً مناطق `ZONE:CONTRACT` و `ZONE:GOLDEN_VALUES` را به همراه پیشوند الفبایی هستی‌شناسی برش بزند.

### سناریوی P3 (یکپارچگی سه‌گانه F1uxus + F1uent + MJNexus):
- **معیارهای پذیرش:**
  - [x] حفظ مختصات کاراکتری (`char_span`) در نرمال‌سازی متون فارسی (`normalize_persian_with_offsets`).
  - [x] اتصال مستقیم رکورد تسلط (`CompetenceRecord` با `BKT + FSRS-6`) به نمادهای AST و گره‌های هستی‌شناسی.
  - [x] قفل امنیتی فیلدهای `owner_only` در رادار ابزار (`OwnerCurationLockError`).
<!-- ZONE:HUMAN_INTUITION_END -->
<!-- ZONE:CONTRACT_START -->
- Project: `F1uent-Ecosystem` | Ontology: `ONT_F1UENT_PLAYBOOKS_SPEC` | Thread: `THR_F1UENT_SPEC`
<!-- ZONE:CONTRACT_END -->
<!-- ZONE:EXECUTION_CORE_START -->
```python
ONT_ID = "ONT_F1UENT_PLAYBOOKS_SPEC"
SOURCE_REF = "specs/spec.md"
```
<!-- ZONE:EXECUTION_CORE_END -->
<!-- ZONE:WORKSHEET_START -->
## تمرین ۱۰ دقیقه‌ای (F1uent-Ecosystem)
1. معماری و قرارداد `ONT_F1UENT_PLAYBOOKS_SPEC` در `F1uent-Ecosystem` چگونه راستی‌آزمایی می‌شود؟
<details data-f1-thread="THR_F1UENT_SPEC"><summary>ThreadBox THR_F1UENT_SPEC</summary></details>
<!-- ZONE:WORKSHEET_END -->
