import csv, glob, os, re, sqlite3
from pathlib import Path
src, dst = Path("/tmp/MJNexus"), Path(".")
oid = lambda p, s: f"ONT_{p}_" + (re.sub(r"[^A-Z0-9]+", "_", re.sub(r"^(?:resource:|concept:|domain:)+", "", str(s).strip(), flags=re.I).upper()).strip("_") or "X")[:52]
res, cards, doms, nodes, tbls, locks = {}, [], set(), {}, [], 0
db = src / "knowledge/kg.sqlite"
if db.exists():
    c = sqlite3.connect(db); c.row_factory = sqlite3.Row
    tbls = [r[0] for r in c.execute("SELECT name FROM sqlite_master WHERE type='table'")]
    for t in tbls:
        for d in [dict(x) for x in c.execute(f"SELECT * FROM [{t}]")]:
            i = str(d.get("id") or d.get("resource_id") or d.get("slug") or "").strip()
            if i.startswith("resource:") or t in ("resources", "radar"):
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
    (od / f"{r['ont']}.md").write_text(f"---\nont_id: {r['ont']}\nsource_id: \"{r['id']}\"\ncategory: {r['cat']}\nwikidata_qid: \"{r['qid']}\"\nowner_only:\n  ring: {r['ring']}\n  verification: {r['ver']}\n  notes_fa: \"{r['note']}\"\n---\n# `{r['ont']}` — {r['name']}\n\n{r['what']}\n", encoding="utf-8")
for p in sorted((src / "learning").glob("*/*/README.md")):
    dom, slug = p.parent.parent.name, p.parent.name; doms.add(dom)
    cid, tid = oid("CONCEPT", f"{dom}_{slug}"), f"THR_{dom.upper()}_{slug.upper()}".replace("-", "_")[:42]
    txt = p.read_text(encoding="utf-8"); tm = re.search(r"^#\s+(.+)$", txt, re.M); title = tm.group(1).strip() if tm else f"{dom}/{slug}"
    pts = re.split(r"(?=^##\s+(?:تمرین|ارزیابی|سوالات|Assessment))", txt, 1, re.M)
    intu, ex = pts[0].strip(), (pts[1].strip() if len(pts) > 1 else "## تمرین ۱۰ دقیقه‌ای\n1. مفهوم کلیدی چیست؟")
    (od / f"{cid}.md").write_text(f"---\nont_id: {cid}\ndomain: {dom}\ntitle_fa: \"{title}\"\n---\n# `{cid}` — {title}\n", encoding="utf-8")
    (td / f"{tid}.thread.md").write_text(f"---\nthread_id: {tid}\nanchor_ont_id: {cid}\nstatus: RESOLVED\n---\n{ex}\n", encoding="utf-8")
    zd = dst / "learning" / dom / slug; zd.mkdir(parents=True, exist_ok=True)
    (zd / "README.md").write_text(f"---\nont_id: {cid}\ndomain: {dom}\ntitle_fa: \"{title}\"\ncontent_is_data: true\n---\n<!-- ZONE:HUMAN_INTUITION_START -->\n{intu}\n<!-- ZONE:HUMAN_INTUITION_END -->\n<!-- ZONE:CONTRACT_START -->\n- Ontology: `{cid}` | Thread: `{tid}`\n<!-- ZONE:CONTRACT_END -->\n<!-- ZONE:EXECUTION_CORE_START -->\n```python\nONT_ID = \"{cid}\"\n```\n<!-- ZONE:EXECUTION_CORE_END -->\n<!-- ZONE:WORKSHEET_START -->\n{ex}\n<details data-f1-thread=\"{tid}\"><summary>ThreadBox {tid}</summary></details>\n<!-- ZONE:WORKSHEET_END -->\n", encoding="utf-8")
    for j, q in enumerate(re.findall(r"^\s*\d+[\.\-\)]\s+(.+)$", ex, re.M) or [f"هدف {title} چیست؟"], 1): cards.append([f"CARD_{cid}_{j:02d}", cid, dom, f"{dom}/{slug}", q.strip(), "1.5", "5.0", "0.15"])
    nodes[f"{dom}/{slug}"] = cid
with open(dst / "notebook/cards.tsv", "w", encoding="utf-8", newline="") as f:
    w = csv.writer(f, delimiter="\t"); w.writerow(["card_id", "ont_id", "domain", "node", "question_fa", "S", "D", "p_mastery"]); w.writerows(cards)
(dst / "MIGRATION_REPORT.md").write_text(f"# گزارش مهاجرت خودکار MJNexus به F1uway\n\n- جداول SQLite خوانده‌شده از `knowledge/kg.sqlite`: `{tbls}`\n- منابع رادار تبدیل‌شده به `ONT_RES_*`: `{len(res)}` (قفل مالک `owner_only`: `{locks}`)\n- دامنه‌های یادگیری مهاجرت‌یافته ({len(doms)} دامنه): `{sorted(doms)}`\n- درس‌نامه‌های تبدیل‌شده به ۴ ناحیه `Zoned Markdown`: `{len(nodes)}`", encoding="utf-8")
