# 🧠 نقشه یادگیری و درخت وابستگی مفاهیم (`learning-map.fa.md`)

| فاز پروژه | نمادهای کد هدف (`AST Symbols`) | مفاهیم علمی و مهندسی متصل (`Ontology Concepts`) | الگوریتم سنجش |
| :--- | :--- | :--- | :--- |
| **فاز ۱** | `src/f1uway/contracts.py::ConstrainedLLMResponse` <br> `src/f1uway/text_bidi.py::normalize_persian_with_offsets` | `ONT_PYDANTIC_EXTRA_FORBID`, `ONT_PUSHDOWN_AUTOMATON_CONSTRAINED_DECODING`, الگوریتم یونیکد BiDi (`UAX #9`) | `BKT + FSRS-6` |
| **فاز ۲** | `src/f1uway/ontology_interner.py::OntologyRegistry` <br> `src/f1uway/thread_dag.py::ThreadDAGManager` | درونی‌سازی نمادها، هش درخت نحوی (`Unison AST Hash`), گراف جهت‌دار غیرمدور (`DAG`) و ایزولاسیون زمینه (`GCC`) | `BKT + FSRS-6` |
| **فاز ۳** | `src/f1uway/learning_engine.py::update_bkt_mastery` <br> `src/f1uway/learning_engine.py::update_fsrs6_memory` | استنتاج بیزی (`Bayesian Posterior`), منحنی فراموشی نمایی-توانی و زمان‌بندی تکرار فاصله‌دار | `BKT + FSRS-6` |
| **فاز ۴ تا ۶** | `src/f1uway/radar_nexus.py::RadarResourceNode` <br> `initdb/01_schema.sql` | بازیابی هیبریدی `RRF (k=60)`, پیمایش `Recursive CTE`, حاکمیت داده `owner_only` و ارگونومی دیداری ساکاد چشم | `BKT + FSRS-6` |
