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
