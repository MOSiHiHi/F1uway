---
ont_id: ONT_F1UENT_PLAYBOOKS_PLAN
source_project: F1uent-Ecosystem
domain: playbooks
title_fa: "نقشه معماری و گزارش تحلیل اثر همگام‌سازی (`specs/plan.md` — Sync Impact Report)"
content_is_data: true
---
<!-- ZONE:HUMAN_INTUITION_START -->
# نقشه معماری و گزارش تحلیل اثر همگام‌سازی (`specs/plan.md` — Sync Impact Report)

## ۱. ماتریس نگاشت ماژول‌ها و تحلیل اثر تغییرات (`Sync Impact Report`)

| ماژول تغییریافته در `src/f1uway/` | فایل‌های وابسته که باید همگام شوند | گیت راستی‌آزمایی خودکار |
| :--- | :--- | :--- |
| `src/f1uway/contracts.py` | `docs/human/playbooks/T1.1.fa.md` (بلوک `EMBED`) + `tests/test_f1_core.py` | `python3 scripts/devloop.py sync-embeds && python3 scripts/devloop.py gate` |
| `src/f1uway/ontology_interner.py` | `.omni-audit/shadow_index.sqlite` + `notebook/ontology/ONT_*.md` | `python3 scripts/devloop.py ontology stats` |
| `src/f1uway/thread_dag.py` | `notebook/threads/THR_*.jsonl` + منطقه `ZONE:THREADS` در پلی‌بوک‌ها + `site/index.html` | `python3 scripts/devloop.py thread sync-md` |
| `ROADMAP_AND_TASKS.md` | فیلد `roadmap_sha256` در هدر پلی‌بوک‌های `docs/human/playbooks/*.md` | `python3 scripts/devloop.py doctor` |

## ۲. بودجه‌های تأخیر و عملکرد (SLO Budgets)
- **لایه ۱ (رهگیر هستی‌شناسی و کش محلی SQLite):** $\le 5	ext{ ms}$ (۰ توکن API).
- **لایه ۲ (بازیابی هیبریدی PostgreSQL `pgvector` HNSW + `tsvector` GIN + `Recursive CTE`):** $\le 50	ext{ ms}$.
- **لایه ۳ (برش `Zoned Markdown` و ساخت پرامپت کش‌شده):** $\le 15	ext{ ms}$ (فشرده‌سازی $\ge 80\%$ خطوط).
<!-- ZONE:HUMAN_INTUITION_END -->
<!-- ZONE:CONTRACT_START -->
- Project: `F1uent-Ecosystem` | Ontology: `ONT_F1UENT_PLAYBOOKS_PLAN` | Thread: `THR_F1UENT_PLAN`
<!-- ZONE:CONTRACT_END -->
<!-- ZONE:EXECUTION_CORE_START -->
```python
ONT_ID = "ONT_F1UENT_PLAYBOOKS_PLAN"
SOURCE_REF = "specs/plan.md"
```
<!-- ZONE:EXECUTION_CORE_END -->
<!-- ZONE:WORKSHEET_START -->
## تمرین ۱۰ دقیقه‌ای (F1uent-Ecosystem)
1. معماری و قرارداد `ONT_F1UENT_PLAYBOOKS_PLAN` در `F1uent-Ecosystem` چگونه راستی‌آزمایی می‌شود؟
<details data-f1-thread="THR_F1UENT_PLAN"><summary>ThreadBox THR_F1UENT_PLAN</summary></details>
<!-- ZONE:WORKSHEET_END -->
