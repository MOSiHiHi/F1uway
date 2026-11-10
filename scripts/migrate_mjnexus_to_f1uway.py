import csv, re, sqlite3
from pathlib import Path
src, dst = Path("/tmp/MJNexus"), Path(".")
oid = lambda p, s: f"ONT_{p}_" + (re.sub(r"[^A-Z0-9]+", "_", re.sub(r"^(?:resource:|concept:|domain:)+", "", str(s).strip(), flags=re.I).upper()).strip("_") or "X")[:52]
res, cards, doms, nodes, tbls, locks = {}, [], set(), {}, [], 0
f1uent_cnt, f1uxus_cnt, mod_cnt = 0, 0, 0
db = src / "knowledge/kg.sqlite"
if db.exists():
    c = sqlite3.connect(db); c.row_factory = sqlite3.Row
    tbls = [r[0] for r in c.execute("SELECT name FROM sqlite_master WHERE type='table'")]
    for t in tbls:
        for d in [dict(x) for x in c.execute(f"SELECT * FROM [{t}]")]:
            i = str(d.get("id") or d.get("resource_id") or d.get("slug") or "").strip()
            if i.startswith("resource:") or t in ("resources", "radar", "resource"):
                res[i] = {"id": i, "ont": oid("RES", i), "name": d.get("name") or i, "cat": d.get("category") or "other", "what": d.get("what_fa") or "", "ring": d.get("ring") or "assess", "ver": "unverified", "note": "", "qid": d.get("wikidata_id") or ""}
dd = src / "knowledge/data"
for fn in ("radar.tsv", "entity_links.tsv", "radar_owner.tsv"):
    if (dd / fn).exists():
        for r in csv.DictReader(open(dd / fn, encoding="utf-8"), delimiter="\t"):
            i = (r.get("id") or r.get("entity_id") or "").strip()
            if not i: continue
            x = res.setdefault(i, {"id": i, "ont": oid("RES", i), "name": r.get("name") or i, "cat": r.get("category") or "other", "what": r.get("what_fa") or "", "ring": "assess", "ver": "unverified", "note": "", "qid": ""})
            if r.get("wikidata_id"): x["qid"] = r["wikidata_id"]
            if fn == "radar_owner.tsv":
                locks += 1; x["ring"] = r.get("ring") or "assess"; x["ver"] = r.get("verification") or "verified"; x["note"] = r.get("notes_fa") or ""
od, td = dst / "notebook/ontology", dst / "notebook/threads"
od.mkdir(parents=True, exist_ok=True); td.mkdir(parents=True, exist_ok=True)
for r in res.values():
    (od / f"{r['ont']}.md").write_text(f"---\nont_id: {r['ont']}\nsource_project: MJNexus\nsource_id: \"{r['id']}\"\ncategory: {r['cat']}\nwikidata_qid: \"{r['qid']}\"\nowner_only:\n  ring: {r['ring']}\n  verification: {r['ver']}\n  notes_fa: \"{r['note']}\"\n---\n# `{r['ont']}` — {r['name']}\n\n{r['what']}\n", encoding="utf-8")
def zone_wrap(p, proj, prefix, dom, slug, code_ref, keep_file=False):
    txt = p.read_text(encoding="utf-8")
    if "<!-- ZONE:HUMAN_INTUITION_START -->" in txt and not keep_file:
        m = re.search(r"<!-- ZONE:HUMAN_INTUITION_START -->\s*(.*?)\s*<!-- ZONE:HUMAN_INTUITION_END -->", txt, re.S)
        if m: txt = m.group(1)
    cid, tid = oid(prefix, f"{dom}_{slug}"), f"THR_{prefix}_{slug.upper()}".replace("-", "_").replace(".", "_")[:42]
    tm = re.search(r"^#\s+(.+)$", txt, re.M); title = tm.group(1).strip() if tm else f"{dom}/{slug}"
    pts = re.split(r"(?=^##\s+(?:\u062a\u0645\u0631\u06cc\u0646|\u0627\u0631\u0632\u06cc\u0627\u0628\u06cc|\u0633\u0648\u0627\u0644\u0627\u062a|Assessment|\u06af\u06cc\u062a))", txt, 1, re.M)
    intu, ex = pts[0].strip(), (pts[1].strip() if len(pts) > 1 else f"## \u062a\u0645\u0631\u06cc\u0646 \u06f1\u06f0 \u062f\u0642\u06cc\u0642\u0647\u200c\u0627\u06cc ({proj})\n1. \u0645\u0639\u0645\u0627\u0631\u06cc \u0648 \u0642\u0631\u0627\u0631\u062f\u0627\u062f `{cid}` \u062f\u0631 `{proj}` \u0686\u06af\u0648\u0646\u0647 \u0631\u0627\u0633\u062a\u06cc\u200c\u0622\u0632\u0645\u0627\u06cc\u06cc \u0645\u06cc\u200c\u0634\u0648\u062f\u061f")
    (od / f"{cid}.md").write_text(f"---\nont_id: {cid}\nsource_project: {proj}\ndomain: {dom}\ntitle_fa: \"{title}\"\n---\n# `{cid}` — {title}\n", encoding="utf-8")
    (td / f"{tid}.thread.md").write_text(f"---\nthread_id: {tid}\nanchor_ont_id: {cid}\nsource_project: {proj}\nstatus: RESOLVED\n---\n{ex}\n", encoding="utf-8")
    if not keep_file:
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(f"---\nont_id: {cid}\nsource_project: {proj}\ndomain: {dom}\ntitle_fa: \"{title}\"\ncontent_is_data: true\n---\n<!-- ZONE:HUMAN_INTUITION_START -->\n{intu}\n<!-- ZONE:HUMAN_INTUITION_END -->\n<!-- ZONE:CONTRACT_START -->\n- Project: `{proj}` | Ontology: `{cid}` | Thread: `{tid}`\n<!-- ZONE:CONTRACT_END -->\n<!-- ZONE:EXECUTION_CORE_START -->\n```python\nONT_ID = \"{cid}\"\nSOURCE_REF = \"{code_ref}\"\n```\n<!-- ZONE:EXECUTION_CORE_END -->\n<!-- ZONE:WORKSHEET_START -->\n{ex}\n<details data-f1-thread=\"{tid}\"><summary>ThreadBox {tid}</summary></details>\n<!-- ZONE:WORKSHEET_END -->\n", encoding="utf-8")
    for j, q in enumerate(re.findall(r"^\s*\d+[\.\-\)]\s+(.+)$", ex, re.M) or [f"\u0647\u062f\u0641 \u0648 \u0645\u0639\u06cc\u0627\u0631 \u0633\u0646\u062c\u0634 {title} \u062f\u0631 {proj} \u0686\u06cc\u0633\u062a\u061f"], 1):
        cards.append([f"CARD_{cid}_{j:02d}", cid, f"{proj}:{dom}", f"{dom}/{slug}", q.strip(), "1.5", "5.0", "0.15"])
    return cid
for p in sorted((src / "learning").glob("*/*/README.md")):
    dom, slug = p.parent.parent.name, p.parent.name; doms.add(dom)
    target = dst / "learning" / dom / slug / "README.md"; target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(p.read_text(encoding="utf-8"), encoding="utf-8")
    nodes[f"{dom}/{slug}"] = zone_wrap(target, "MJNexus", "CONCEPT", dom, slug, f"learning/{dom}/{slug}/README.md")
for p in sorted((dst / "docs/human/playbooks").glob("*.md")) + sorted((dst / "specs").glob("*.md")) + [dst / "docs/DEVELOPMENT_SPECTRUM.fa.md"]:
    if p.exists():
        zone_wrap(p, "F1uent-Ecosystem", "F1UENT", "playbooks", p.stem, str(p), keep_file=(p.name=="T1.1.fa.md")); f1uent_cnt += 1
for p in sorted((dst / "src/f1_core").glob("*.py")):
    if p.name != "__init__.py":
        cid = oid("MOD", f"F1_CORE_{p.stem}"); mod_cnt += 1
        (od / f"{cid}.md").write_text(f"---\nont_id: {cid}\nsource_project: F1uent-Ecosystem\nmodule: src/f1_core/{p.name}\n---\n# `{cid}` — \u0647\u0633\u062a\u0647\u064c \u0627\u062c\u0631\u0627\u06cc\u06cc `{p.name}`\n", encoding="utf-8")
        cards.append([f"CARD_{cid}_01", cid, "F1uent-Ecosystem:core", p.name, f"\u0642\u0631\u0627\u0631\u062f\u0627\u062f \u0648 \u0645\u0633\u0624\u0644\u06cc\u062a \u0645\u0627\u0698\u0648\u0644 {p.name} \u062f\u0631 \u0647\u0633\u062a\u0647 F1uway \u0686\u06cc\u0633\u062a\u061f", "1.8", "4.5", "0.25"])
for p in sorted((dst / "docs/research").glob("*.md")) + sorted((dst / "docs/adr").glob("*.md")):
    if p.exists():
        zone_wrap(p, "F1uxus", "F1UXUS", p.parent.name, p.stem, "initdb/01_schema.sql"); f1uxus_cnt += 1
for infra in (dst / "initdb/01_schema.sql", dst / "searxng/settings.yml"):
    if infra.exists():
        cid = oid("F1UXUS", f"INFRA_{infra.stem}"); f1uxus_cnt += 1
        (od / f"{cid}.md").write_text(f"---\nont_id: {cid}\nsource_project: F1uxus\ninfra_path: {infra}\n---\n# `{cid}` — \u0632\u06cc\u0631\u0633\u0627\u062e\u062a `{infra.name}`\n", encoding="utf-8")
with open(dst / "notebook/cards.tsv", "w", encoding="utf-8", newline="") as f:
    w = csv.writer(f, delimiter="\t"); w.writerow(["card_id", "ont_id", "domain", "node", "question_fa", "S", "D", "p_mastery"]); w.writerows(cards)
f1db = dst / ".f1/index.sqlite"; f1db.parent.mkdir(parents=True, exist_ok=True)
with sqlite3.connect(f1db) as c:
    c.execute("CREATE TABLE IF NOT EXISTS ontology_index (ont_id TEXT PRIMARY KEY, path TEXT)")
    for f in sorted(od.glob("ONT_*.md")): c.execute("INSERT OR REPLACE INTO ontology_index VALUES (?, ?)", (f.stem, str(f)))
    c.commit()
total_ont = len(list(od.glob("ONT_*.md")))
(dst / "MIGRATION_REPORT.md").write_text(f"# \u06af\u0632\u0627\u0631\u0634 \u0645\u0647\u0627\u062c\u0631\u062a \u06cc\u06a9\u067e\u0627\u0631\u0686\u0647 \u06f3 \u067e\u0631\u0648\u062c\u0647 (MJNexus + F1uent-Ecosystem + F1uxus) \u0628\u0647 F1uway\n\n- \u062c\u062f\u0627\u0648\u0644 SQLite \u062e\u0648\u0627\u0646\u062f\u0647\200c\u0634\u062f\u0647 \u0627\u0632 `MJNexus/knowledge/kg.sqlite`: `{tbls}`\n- \u0645\u0646\u0627\u0628\u0639 \u0631\u0627\u062f\u0627\u0631 `MJNexus` \u062a\u0628\u062f\u06cc\u0644\200c\u0634\u062f\u0647 \u0628\u0647 `ONT_RES_*`: `{len(res)}` (\u0642\u0641\u0644 \u0645\u0627\u0644\u06a9 `owner_only`: `{locks}`)\n- \u062f\u0627\u0645\u0646\u0647\200c\u0647\u0627\u06cc \u06cc\u0627\u062f\u06af\u06cc\u0631\u06cc `MJNexus` ({len(doms)} \u062f\u0627\u0645\u0646\u0647): `{sorted(doms)}`\n- \u062f\u0631\u0633\200c\u0646\u0627\u0645\u0647\200c\u0647\u0627\u06cc `MJNexus` \u062a\u0628\u062f\u06cc\u0644\200c\u0634\u062f\u0647 \u0628\u0647 `Zoned Markdown` (`ONT_CONCEPT_*`): `{len(nodes)}`\n- \u067e\u0644\u06cc\u200c\u0628\u0648\u06a9\u200c\u0647\u0627\u060c \u0637\u06cc\u0641 \u062a\u0648\u0633\u0639\u0647 \u0648 \u0645\u0634\u062e\u0635\u0627\u062a `F1uent-Ecosystem` \u062a\u0628\u062f\u06cc\u0644\200c\u0634\u062f\u0647 \u0628\u0647 `Zoned Markdown` (`ONT_F1UENT_*`): `{f1uent_cnt}`\n- \u0645\u0627\u0698\u0648\u0644\u0647\u0627\u06cc \u0647\u0633\u062a\u0647 \u067e\u0627\u06cc\u062a\u0648\u0646 `F1uent-Ecosystem` (`ONT_MOD_*` \u062f\u0631 `src/f1_core/`): `{mod_cnt}`\n- \u0627\u0633\u0646\u0627\u062f \u067e\u0698\u0648\u0647\u0634\u06cc\u060c \u0645\u0639\u0645\u0627\u0631\u06cc (`ADR 0001-0012`) \u0648 \u0632\u06cc\u0631\u0633\u0627\u062e\u062a `F1uxus` \u062a\u0628\u062f\u06cc\u0644\200c\u0634\u062f\u0647 \u0628\u0647 `Zoned Markdown` (`ONT_F1UXUS_*`): `{f1uxus_cnt}`\n- \u0645\u062c\u0645\u0648\u0639 \u06a9\u0644 \u06af\u0631\u0647\u0647\u0627\u06cc \u0647\u0633\u062a\u06cc\200c\u0634\u0646\u0627\u0633\u06cc (`notebook/ontology/ONT_*.md`): `{total_ont}`\n- \u0645\u062c\u0645\u0648\u0639 \u06a9\u0644 \u0641\u0644\u0634\200c\u06a9\u0627\u0631\u062a\u200c\u0647\u0627\u06cc \u0645\u0631\u0648\u0631 \u0641\u0627\u0635\u0644\u0647\200c\u062f\u0627\u0631 `FSRS-6` (`notebook/cards.tsv`): `{len(cards)}`\n", encoding="utf-8")
