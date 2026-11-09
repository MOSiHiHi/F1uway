# 🛠️ راهنمای عملیاتی حلقه توسعه و یادگیری (`GUIDE.fa.md`)

این سند مرجع کامل دستورات `scripts/devloop.py` و نحوه کار در ۸ تراک طیف توسعه (`H0` تا `A2`) است.

## ۱. دستورات اصلی `scripts/devloop.py`

| دستور | کاربرد دقیق |
| :--- | :--- |
| `python3 scripts/devloop.py next` | **قطب‌نمای خودران انسانی:** نمایش تسک جاری، آمار توکن‌های ذخیره‌شده و ۳ دستور بعدی. |
| `python3 scripts/devloop.py status` | خروجی JSON از وضعیت فعلی مخزن (`STATE.md`) و آمار هستی‌شناسی. |
| `python3 scripts/devloop.py doctor` | بررسی سلامت محیط و تطابق اثرانگشت `SHA-256` بین `ROADMAP_AND_TASKS.md` و پلی‌بوک‌ها. |
| `python3 scripts/devloop.py thread tree` | نمایش گراف مستطیل‌های چت (`ThreadBox DAG`)، کنش‌های کلامی و انشعاب‌ها در ترمینال. |
| `python3 scripts/devloop.py thread branch --span "X" --title "..."` | ایجاد مستطیل انشعاب جدید روی عبارت `X` (با بررسی خودکار کش ۰-توکنی در هستی‌شناسی). |
| `python3 scripts/devloop.py thread sync-md` | رندر کردن مستطیل‌های چت به صورت آکاردئون‌های `<details>` درون منطقه `ZONE:THREADS` پلی‌بوک. |
| `python3 scripts/devloop.py ontology stats` | نمایش تمام موجودیت‌های یکتاسازی‌شده در هستی‌شناسی و مجموع توکن‌های صرفه‌جویی‌شده. |
| `python3 scripts/devloop.py ontology lookup --span "X"` | آزمایش رهگیر انشعاب روی عبارت `X` (`ZERO_TOKEN_HIT` یا `DELTA_PROMPT_MODE`). |
| `python3 scripts/devloop.py sync-embeds` | همگام‌سازی دوطرفه کدهای زنده از فایل‌های `.py` به بلوک‌های `<!-- EMBED: ... -->` در پلی‌بوک‌ها. |
| `python3 scripts/devloop.py pack` | برش مناطق ماشینی (`ZONE:CONTRACT` + `ZONE:GOLDEN_VALUES`) و ساخت پرامپت کش‌شده با ۹۰٪ فشرده‌سازی. |
| `python3 scripts/devloop.py gate` | اجرای **دروازه دوگانه کیفیت** (تست‌های واحد مهندسی + بررسی فلش‌کارت‌های `FSRS-6` و سلامت مستندات). |
