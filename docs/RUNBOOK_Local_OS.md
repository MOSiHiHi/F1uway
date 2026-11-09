# رانبوک استقرار محلی و آفلاین (`docs/RUNBOOK_Local_OS.md`)

## ۱. پروفایل سخت‌افزاری مرجع و اجرای ۱۰۰٪ آفلاین (`F1UXUS_OFFLINE=1`)
- بهینه‌سازی‌شده برای اجرا روی سخت‌افزار شخصی (مانند `Intel i5-11400`, `32GB RAM`, `NVIDIA RTX 3050 Ti` یا کارت‌های ۲۴GB) و لینوکس (`CachyOS` / `NixOS` / `Arch`).
- مدیریت بسته پایتون با `uv` (`uv sync --all-extras`) و اجرای تست‌های واحد بدون نیاز به اینترنت، دیتابیس خارجی یا GPU (`python3 scripts/devloop.py gate`).
