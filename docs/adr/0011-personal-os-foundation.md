---
ont_id: ONT_F1UXUS_ADR_0011_PERSONAL_OS_FOUNDATION
source_project: F1uxus
domain: adr
title_fa: "ADR-0011: معماری سیستم‌عامل شخصی اعلامی، بازتولیدپذیر و فارسی‌محور (`F1-OS` بر پایه NixOS)"
content_is_data: true
---
<!-- ZONE:HUMAN_INTUITION_START -->
# ADR-0011: معماری سیستم‌عامل شخصی اعلامی، بازتولیدپذیر و فارسی‌محور (`F1-OS` بر پایه NixOS)
- **وضعیت:** پذیرفته‌شده (Accepted)
- **مقایسه ۴ گزینه سیستم‌عامل پایه برای حل مسائل `P1` تا `P20`:**
  1. **`NixOS Flake Monorepo` (گزینه منتخب ⭐):** تضمین ۱۰۰٪ بازتولیدپذیری از یک فایل، پاکسازی حالت‌های پنهان در هر بوت با `Impermanence`، چند پروفایل دسکتاپ با `Specialisations`، رول‌بک اتمی با `Generations`، محیط توسعه ایزوله هر پروژه با `Nix Dev Shells + direnv` و مجازی‌سازی زیر ۱ ثانیه با `MicroVM.nix`.
  2. **`Arch + Ansible + Dotfiles`:** مستندات عالی Arch Wiki و مخزن AUR، اما بازتولیدپذیری ناقص (وجود State پنهان) و وابستگی رول‌بک به Btrfs/Snapper.
  3. **`Gentoo + Portage`:** کنترل کامل پرچم‌های کامپایل (`USE flags`)، اما زمان بیلد بسیار سنگین.
  4. **`Guix System`:** مشابه Nix با زبان Guile Scheme، اما محدودیت شدید در درایورهای سخت‌افزاری انحصاری (GPU/WiFi).
<!-- ZONE:HUMAN_INTUITION_END -->
<!-- ZONE:CONTRACT_START -->
- Project: `F1uxus` | Ontology: `ONT_F1UXUS_ADR_0011_PERSONAL_OS_FOUNDATION` | Thread: `THR_F1UXUS_0011_PERSONAL_OS_FOUNDATION`
<!-- ZONE:CONTRACT_END -->
<!-- ZONE:EXECUTION_CORE_START -->
```python
ONT_ID = "ONT_F1UXUS_ADR_0011_PERSONAL_OS_FOUNDATION"
SOURCE_REF = "initdb/01_schema.sql"
```
<!-- ZONE:EXECUTION_CORE_END -->
<!-- ZONE:WORKSHEET_START -->
## تمرین ۱۰ دقیقه‌ای (F1uxus)
1. معماری و قرارداد `ONT_F1UXUS_ADR_0011_PERSONAL_OS_FOUNDATION` در `F1uxus` چگونه راستی‌آزمایی می‌شود؟
<details data-f1-thread="THR_F1UXUS_0011_PERSONAL_OS_FOUNDATION"><summary>ThreadBox THR_F1UXUS_0011_PERSONAL_OS_FOUNDATION</summary></details>
<!-- ZONE:WORKSHEET_END -->
