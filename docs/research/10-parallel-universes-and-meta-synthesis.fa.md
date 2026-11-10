---
ont_id: ONT_F1UXUS_RESEARCH_10_PARALLEL_UNIVERSES_AND_META_SYNTHESIS_FA
source_project: F1uxus
domain: research
title_fa: "research/10-parallel-universes-and-meta-synthesis.fa"
content_is_data: true
---
<!-- ZONE:HUMAN_INTUITION_START -->
## ۱. داستان و شهود علمی (مخصوص مطالعه انسان — خارج از بودجه توکن ماشین)

چرا در این معماری هر پیام در یک مستطیل (`ThreadBox`) قرار می‌گیرد و چرا الفاظ منشعب‌شده در هستی‌شناسی (`OntologyRegistry`) ثبت می‌شوند؟ تصور کنید در حال خواندن یک مقاله یا نوشتن کد هستید و عبارتی مثل `extra="forbid"` یا `FSRS-6` ذهنتان را درگیر می‌کند. در چت‌بات‌های معمولی اگر درباره آن سوال بپرسید، رشته اصلی بحث پاره می‌شود و اگر یک هفته بعد در پروژه دیگری دوباره همان سوال را بپرسید، دوباره باید هزینه توکن بدهید. با مکانیسم **درونی‌سازی نمادها (Ontology-Backed Symbolic Interning)**:

* بار اول که روی عبارت `extra="forbid"` شاخه می‌زنید، تعریف آن در فایل `notebook/ontology/ONT_PYDANTIC_EXTRA_FORBID.md` قفل می‌شود.

* بار دوم در هر متن یا پروژه دیگری که روی عبارت مشابه (`extra='forbid'` یا `قفل اسکیمای پایدنتیک`) شاخه بزنید، قلاب `intercept_branch_spawn` با **هزینه ۰ توکن** مستقیماً همان تعریف تثبیت‌شده را به مستطیل جدید پیوند می‌زند!

### کد زنده همگام‌شده از هسته (`Two-Way Code Embed` — جهان موازی ۱):

<!-- EMBED: src/f1_core/contracts.py#ConstrainedLLMResponse -->

```
class ConstrainedLLMResponse(F1BaseModel):
    """Strict Schema for LLM Responses enforcing Key-Order Sensitivity & Anti-Sycophancy (G25).
    
    CRITICAL: `reasoning_chain` and `evidence_quote` MUST be the first two fields
    so Pushdown Automaton (PDA) constrained decoding populates reasoning before verdict.
    """
    reasoning_chain: str = Field(
        min_length=10,
        description="Step-by-step independent derivation with English technical anchors in parentheses BEFORE any verdict"
    )
    evidence_quote: str = Field(
        min_length=1,
        description="Verbatim quote or AST/Golden-Value reference supporting the reasoning"
    )
    independent_calculation_result: Optional[str] = Field(
        default=None,
        description="Result of independent symbolic/math verification prior to comparing with user premise"
    )
    detected_user_premise_error: Optional[str] = Field(
        default=None,
        description="If user prompt contained a flawed assumption, state the exact correction without sycophancy"
    )
    speech_act: SpeechAct = SpeechAct.SYNTHESIS
    topic_pill_fa: str = Field(min_length=2, max_length=80)
    final_answer_md: str = Field(min_length=5)
    extracted_concepts: List[str] = Field(default_factory=list)

    @field_validator("final_answer_md")
    @classmethod
    def forbid_sycophantic_opening(cls, v: str) -> str:
        stripped = v.strip()
        forbidden_starts = ("بله، کاملاً درست", "حق با شماست", "You are completely right", "Certainly!")
        for prefix in forbidden_starts:
            if stripped.startswith(prefix):
                raise ValueError(
                    f"Anti-Sycophancy Gate triggered: response cannot open with '{prefix}'. "
                    "Lead directly with the grounded finding."
                )
        return v

```

<!-- /EMBED -->
<!-- ZONE:HUMAN_INTUITION_END -->
<!-- ZONE:CONTRACT_START -->
- Project: `F1uxus` | Ontology: `ONT_F1UXUS_RESEARCH_10_PARALLEL_UNIVERSES_AND_META_SYNTHESIS_FA` | Thread: `THR_F1UXUS_10_PARALLEL_UNIVERSES_AND_META_`
<!-- ZONE:CONTRACT_END -->
<!-- ZONE:EXECUTION_CORE_START -->
```python
ONT_ID = "ONT_F1UXUS_RESEARCH_10_PARALLEL_UNIVERSES_AND_META_SYNTHESIS_FA"
SOURCE_REF = "initdb/01_schema.sql"
```
<!-- ZONE:EXECUTION_CORE_END -->
<!-- ZONE:WORKSHEET_START -->
## تمرین ۱۰ دقیقه‌ای (F1uxus)
1. معماری و قرارداد `ONT_F1UXUS_RESEARCH_10_PARALLEL_UNIVERSES_AND_META_SYNTHESIS_FA` در `F1uxus` چگونه راستی‌آزمایی می‌شود؟
<details data-f1-thread="THR_F1UXUS_10_PARALLEL_UNIVERSES_AND_META_"><summary>ThreadBox THR_F1UXUS_10_PARALLEL_UNIVERSES_AND_META_</summary></details>
<!-- ZONE:WORKSHEET_END -->
