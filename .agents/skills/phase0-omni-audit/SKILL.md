---
name: phase0-omni-audit
description: >
  Comprehensive codebase intelligence skill orchestrating Code Knowledge Graphs (CBM, CodeGraph, Graphify, rgctl),
  self-maintaining wikis with doc0 verification gates, mechanical architecture governance (tach),
  security audits (Semgrep/SARIF), interactive visualizations (Archify, CodeFlow, CodeCharta),
  and AST-linked BKT/FSRS-6 learning graphs.
version: 1.0.0
---
# دستورالعمل اجرای اسکیل `phase0-omni-audit`
1. قبل از اجرای جستجوی متنی (`Grep`/`Glob`)، از گراف کد و رجیستری هستی‌شناسی (`python3 scripts/devloop.py ontology stats`) پرس‌وجو کنید.
2. پس از هر تغییر کد، `python3 scripts/devloop.py sync-embeds` و `python3 scripts/devloop.py gate` را اجرا نمایید.
