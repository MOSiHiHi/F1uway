---
doc_id: "PLAYBOOK-PHASE-2"
doc_type: "executable_learning_spec"
phase: "2"
primary_task: "T2.1"
learning_value: "HIGH"
recommended_track: "H2_SOCRATIC_TUTOR"
token_slice_for_ai: "CONTRACT,GOLDEN_VALUES"
---

# 📘 پلی‌بوک خودران فاز 2: گراف مستطیل‌های چت منشعب‌شونده (ThreadBox DAG) و درونی‌سازی هستی‌شناختی ضدتکرار توکن

> 🧭 **قطب‌نمای خودران انسانی (`Autopilot Compass`):**
> - **موقعیت شما:** فاز 2 (تسک محوری `T2.1`).
> - **گام ۱:** بخش `ZONE:HUMAN_INTUITION` زیر را بخوانید تا شهود علمی و معماری این فاز را درک کنید.
> - **گام ۲:** اگر هر اصطلاحی برایتان سوال شد، دستور `python3 scripts/devloop.py thread branch --span "عبارت" --title "سوال"` را بزنید.
> - **گام ۳:** تمرین ۱۰ دقیقه‌ای انتهای صفحه (`ZONE:WORKSHEET`) را کامل کنید و با `python3 scripts/devloop.py gate` از گیت عبور کنید.

<!-- ZONE:HUMAN_INTUITION_START -->
## ۱. داستان و شهود علمی فاز 2 (مخصوص انسان — خارج از بودجه توکن ماشین)
در این فاز، ما بخش **گراف مستطیل‌های چت منشعب‌شونده (ThreadBox DAG) و درونی‌سازی هستی‌شناختی ضدتکرار توکن** را بر پایه اصل «چاهک‌ها، نه لوله‌ها» (`Sinks, Not Pipes`) و چرخه دوطرفه `Build-to-Learn` $ightleftharpoons$ `Learn-to-Build` پیاده‌سازی می‌کنیم. برای مطالعه مبانی نظری عمیق این فاز، به پوشه `docs/research/` و تصمیم‌نامه‌های `docs/adr/` مراجعه کنید.
<!-- ZONE:HUMAN_INTUITION_END -->

<!-- ZONE:CONTRACT_START -->
## ۲. قرارداد فنی ماشینی (`ZONE:CONTRACT`)
- پیاده‌سازی و تست کامل ماژول‌های فاز 2 منطبق بر `ARCHITECTURE.md` و `ROADMAP_AND_TASKS.md` (تسک `T2.1`).
- رعایت کامل تغییرناپذیری مدل‌ها (`extra='forbid', frozen=True`) و تفکیک کامیت‌های `struct:` از `feat:`.
<!-- ZONE:CONTRACT_END -->

<!-- ZONE:GOLDEN_VALUES_START -->
## ۳. مقادیر طلایی و معیار عبور (`ZONE:GOLDEN_VALUES`)
- پاس شدن ۱۰۰٪ تست‌های واحد در `tests/test_f1_core.py` و سبز شدن `python3 scripts/devloop.py gate`.
<!-- ZONE:GOLDEN_VALUES_END -->

<!-- ZONE:THREADS_START -->
## ۴. گراف مستطیل‌های چت و انشعابات فاز 2 (`ZONE:THREADS`)
_توسط دستور `python3 scripts/devloop.py thread sync-md` به‌روزرسانی می‌شود._
<!-- ZONE:THREADS_END -->

<!-- ZONE:WORKSHEET_START -->
## ۵. تمرین ۱۰ دقیقه‌ای و کاربرگ خودسنجی (`ZONE:WORKSHEET`)
- [ ] **پیش‌بینی قبل از اجرا:** کدام تصمیم معماری در این فاز مانع از تورم توکن و توهم هوش مصنوعی می‌شود؟
- [ ] **ساخت میکرو-ابزار / تست:** یک تست واحد جدید در `tests/test_f1_core.py` برای یکی از موارد مرزی این فاز اضافه کنید و `python3 scripts/devloop.py gate` را اجرا نمایید.
<!-- ZONE:WORKSHEET_END -->
