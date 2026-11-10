# گزارش مهاجرت یکپارچه ۳ پروجه (MJNexus + F1uent-Ecosystem + F1uxus) به F1uway

- جداول SQLite خواندهcشده از `MJNexus/knowledge/kg.sqlite`: `['account', 'item', 'video', 'resource', 'concept', 'domain', 'series', 'claim', 'project', 'edge']`
- منابع رادار `MJNexus` تبدیلcشده به `ONT_RES_*`: `316` (قفل مالک `owner_only`: `0`)
- دامنهcهای یادگیری `MJNexus` (18 دامنه): `['ai', 'business-marketing', 'culture-spirituality', 'design-typography', 'gamedev', 'hardware-tech-privacy', 'health-sports', 'history-myth', 'learning-language-books', 'math', 'media-entertainment', 'music-sound', 'news-politics', 'physics-astronomy', 'programming-infra', 'society-religion', 'sources', 'visual-art']`
- درسcنامهcهای `MJNexus` تبدیلcشده به `Zoned Markdown` (`ONT_CONCEPT_*`): `80`
- پلی‌بوک‌ها، طیف توسعه و مشخصات `F1uent-Ecosystem` تبدیلcشده به `Zoned Markdown` (`ONT_F1UENT_*`): `11`
- ماژولهای هسته پایتون `F1uent-Ecosystem` (`ONT_MOD_*` در `src/f1_core/`): `7`
- اسناد پژوهشی، معماری (`ADR 0001-0012`) و زیرساخت `F1uxus` تبدیلcشده به `Zoned Markdown` (`ONT_F1UXUS_*`): `24`
- مجموع کل گرههای هستیcشناسی (`notebook/ontology/ONT_*.md`): `444`
- مجموع کل فلشcکارت‌های مرور فاصلهcدار `FSRS-6` (`notebook/cards.tsv`): `120`
