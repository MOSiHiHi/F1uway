---
ont_id: ONT_F1UENT_PLAYBOOKS_DEVELOPMENT_SPECTRUM_FA
source_project: F1uent-Ecosystem
domain: playbooks
title_fa: "طیف توسعه ۸ حالته و هسته ناوردا (`docs/DEVELOPMENT_SPECTRUM.fa.md`)"
content_is_data: true
---
<!-- ZONE:HUMAN_INTUITION_START -->
# طیف توسعه ۸ حالته و هسته ناوردا (`docs/DEVELOPMENT_SPECTRUM.fa.md`)

در `F1uway`، هر تسک را می‌توان در یکی از ۸ تراک زیر اجرا کرد، بدون آنکه یکپارچگی مخزن آسیب ببیند:
1. **`H0` (Human Offline):** توسعه کاملاً آفلاین توسط انسان با استفاده از پلی‌بوک فارسی و `offline-kit.fa.md`.
2. **`H1` (Human + Web Docs):** کدنویسی توسط انسان با مراجعه به مستندات رسمی وب.
3. **`H2` (Human + Socratic AI Tutor):** انسان کد می‌نویسد و هوش مصنوعی (`devloop.py pack --tutor`) با چرخه سقراطی و بدون لو دادن کد نهایی هدایت می‌کند.
4. **`H3` (Human + AI Reviewer):** انسان کد را کامل می‌نویسد و هوش مصنوعی (`--review`) کد را از نظر معماری چاهک‌ها و موارد مرزی نقد می‌کند.
5. **`C1` (Chatbot Pack & Apply):** بسته‌بندی زمینه برش‌خورده برای چت‌بات وب و اعمال خودکار خروجی.
6. **`A1` (Interactive Pair Agent):** هم‌برنامه‌نویسی زنده با ایجنت در ترمینال/IDE.
7. **`A2` (Autonomous Agent):** واگذاری کامل تسک‌های `BOILERPLATE` به ایجنت در `Git Worktree` ایزوله تا سبز شدن گیت.
8. **`MIX` (Hybrid Task-Boundary Switching):** انتخاب پویا بین `H0-H3` (برای تسک‌های دارای `Learning-Value: HIGH`) و `A1-A2` (برای تسک‌های زیرساختی).
<!-- ZONE:HUMAN_INTUITION_END -->
<!-- ZONE:CONTRACT_START -->
- Project: `F1uent-Ecosystem` | Ontology: `ONT_F1UENT_PLAYBOOKS_DEVELOPMENT_SPECTRUM_FA` | Thread: `THR_F1UENT_DEVELOPMENT_SPECTRUM_FA`
<!-- ZONE:CONTRACT_END -->
<!-- ZONE:EXECUTION_CORE_START -->
```python
ONT_ID = "ONT_F1UENT_PLAYBOOKS_DEVELOPMENT_SPECTRUM_FA"
SOURCE_REF = "docs/DEVELOPMENT_SPECTRUM.fa.md"
```
<!-- ZONE:EXECUTION_CORE_END -->
<!-- ZONE:WORKSHEET_START -->
## تمرین ۱۰ دقیقه‌ای (F1uent-Ecosystem)
1. معماری و قرارداد `ONT_F1UENT_PLAYBOOKS_DEVELOPMENT_SPECTRUM_FA` در `F1uent-Ecosystem` چگونه راستی‌آزمایی می‌شود؟
<details data-f1-thread="THR_F1UENT_DEVELOPMENT_SPECTRUM_FA"><summary>ThreadBox THR_F1UENT_DEVELOPMENT_SPECTRUM_FA</summary></details>
<!-- ZONE:WORKSHEET_END -->
