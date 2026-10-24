#!/usr/bin/env python3
"""Critical path calculator for a task CSV. Standard library only.

Input CSV columns (header required, extra columns are passed through):
  id, name, duration, predecessors
    duration      working days (number; 0 = milestone)
    predecessors  semicolon-separated ids, each optionally with a type and lag:
                  "A", "A;B", "A:SS", "A:FF+2", "A:FS-1"  (default FS, lag 0)

Optional columns: owner, phase (used as Gantt sections),
  not_before (YYYY-MM-DD; task cannot start earlier, e.g. permit date or status date; needs --start).

Usage:
  cpm.py tasks.csv                         # print table + critical path
  cpm.py tasks.csv --start 2026-11-02      # also compute calendar dates (Mon-Fri)
  cpm.py tasks.csv --start 2026-11-02 --gantt gantt.md --out schedule.csv
  cpm.py tasks.csv --start 2026-11-02 --holidays 2026-12-25,2027-01-01
"""
import argparse
import csv
import datetime as dt
import re
import sys
from collections import defaultdict, deque

PRED_RE = re.compile(r"^\s*([^:+\-\s]+)\s*(?::\s*(FS|SS|FF|SF))?\s*([+-]\s*\d+(?:\.\d+)?)?\s*$", re.I)


def parse_preds(text):
    preds = []
    for part in (text or "").split(";"):
        if not part.strip():
            continue
        m = PRED_RE.match(part)
        if not m:
            sys.exit(f"Cannot parse predecessor '{part}'. Use forms like A, A:SS, A:FS+2.")
        pid, kind, lag = m.groups()
        preds.append((pid, (kind or "FS").upper(), float(lag.replace(" ", "")) if lag else 0.0))
    return preds


def load(path):
    with open(path, newline="", encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))
    if not rows:
        sys.exit("CSV has no rows.")
    missing = {"id", "name", "duration"} - set(rows[0].keys())
    if missing:
        sys.exit(f"CSV is missing columns: {', '.join(sorted(missing))}")
    tasks = {}
    for r in rows:
        tid = r["id"].strip()
        if tid in tasks:
            sys.exit(f"Duplicate task id '{tid}'.")
        r["duration"] = float(r["duration"] or 0)
        r["_preds"] = parse_preds(r.get("predecessors", ""))
        tasks[tid] = r
    for tid, t in tasks.items():
        for pid, _, _ in t["_preds"]:
            if pid not in tasks:
                sys.exit(f"Task '{tid}' depends on unknown task '{pid}'.")
    return tasks


def topo_order(tasks):
    indeg = {t: 0 for t in tasks}
    succs = defaultdict(list)
    for tid, t in tasks.items():
        for pid, _, _ in t["_preds"]:
            indeg[tid] += 1
            succs[pid].append(tid)
    queue = deque(t for t in tasks if indeg[t] == 0)
    order = []
    while queue:
        n = queue.popleft()
        order.append(n)
        for s in succs[n]:
            indeg[s] -= 1
            if indeg[s] == 0:
                queue.append(s)
    if len(order) != len(tasks):
        cyclic = sorted(t for t in tasks if indeg[t] > 0)
        sys.exit(f"Dependency loop detected among: {', '.join(cyclic)}")
    return order, succs


def forward_pass(tasks, order, offset_of=None):
    for tid in order:
        t = tasks[tid]
        d = t["duration"]
        es = 0.0
        nb = (t.get("not_before") or "").strip()
        if nb:
            if not offset_of:
                sys.exit(f"Task '{tid}' has not_before; pass --start so dates can be resolved.")
            es = float(offset_of(dt.date.fromisoformat(nb)))
        for pid, kind, lag in t["_preds"]:
            p = tasks[pid]
            es = max(es, {
                "FS": p["EF"] + lag,
                "SS": p["ES"] + lag,
                "FF": p["EF"] + lag - d,
                "SF": p["ES"] + lag - d,
            }[kind])
        t["ES"], t["EF"] = es, es + d


def backward_pass(tasks, order, succs):
    end = max(t["EF"] for t in tasks.values())
    for tid in reversed(order):
        t = tasks[tid]
        d = t["duration"]
        lf = end
        for sid in succs[tid]:
            s = tasks[sid]
            for pid, kind, lag in s["_preds"]:
                if pid != tid:
                    continue
                lf = min(lf, {
                    "FS": s["LS"] - lag,
                    "SS": s["LS"] - lag + d,
                    "FF": s["LF"] - lag,
                    "SF": s["LF"] - lag + d,
                }[kind])
        t["LF"], t["LS"] = lf, lf - d
        t["float"] = round(t["LS"] - t["ES"], 6)
    return end


def workday_calendar(start, holidays):
    """Return (at, offset_of): at(offset) -> date, where offset counts working days from
    start (0 = start); offset_of(date) -> offset of the first working day on or after date."""
    cache = [start]

    def is_work(d):
        return d.weekday() < 5 and d not in holidays

    while not is_work(cache[0]):
        cache[0] += dt.timedelta(days=1)

    def at(offset):
        i = int(offset)
        while len(cache) <= i:
            d = cache[-1] + dt.timedelta(days=1)
            while not is_work(d):
                d += dt.timedelta(days=1)
            cache.append(d)
        return cache[i]

    def offset_of(date):
        i = 0
        while at(i) < date:
            i += 1
        return i

    return at, offset_of


def date_of(at, es, duration):
    # Milestones mark the end of their predecessor's day, so show them on that day.
    return at(max(es - 1, 0)) if duration == 0 else at(es)


def fmt(n):
    return str(int(n)) if float(n).is_integer() else f"{n:g}"


def critical_chain(tasks, order):
    return [tid for tid in order if abs(tasks[tid]["float"]) < 1e-9]


def write_gantt(path, tasks, order, at, title, holidays):
    excludes = ", ".join(["weekends"] + sorted(h.isoformat() for h in holidays))
    lines = ["```mermaid", "gantt", f"    title {title}", "    dateFormat YYYY-MM-DD", f"    excludes {excludes}"]
    sections = defaultdict(list)
    for tid in order:
        sections[tasks[tid].get("phase") or "Tasks"].append(tid)
    for section, ids in sections.items():
        lines.append(f"    section {section}")
        for tid in ids:
            t = tasks[tid]
            name = re.sub(r"[:#;]", " ", t["name"]).strip()
            tags = []
            if abs(t["float"]) < 1e-9:
                tags.append("crit")
            if t["duration"] == 0:
                tags.append("milestone")
            tag = ", ".join(tags + [f"t_{tid}"])
            start = date_of(at, t["ES"], t["duration"]).isoformat()
            length = f"{max(int(round(t['duration'])), 1)}d" if t["duration"] else "0d"
            lines.append(f"    {name} :{tag}, {start}, {length}")
    lines.append("```")
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("csv")
    ap.add_argument("--start", help="project start date YYYY-MM-DD (enables calendar dates)")
    ap.add_argument("--holidays", default="", help="comma-separated YYYY-MM-DD non-working days")
    ap.add_argument("--out", help="write enriched schedule CSV here")
    ap.add_argument("--gantt", help="write Mermaid Gantt markdown here (needs --start)")
    ap.add_argument("--title", default="Project schedule")
    args = ap.parse_args()

    tasks = load(args.csv)
    order, succs = topo_order(tasks)

    at = offset_of = None
    holidays = set()
    if args.start:
        holidays = {dt.date.fromisoformat(h.strip()) for h in args.holidays.split(",") if h.strip()}
        at, offset_of = workday_calendar(dt.date.fromisoformat(args.start), holidays)

    forward_pass(tasks, order, offset_of)
    end = backward_pass(tasks, order, succs)

    if at:
        for t in tasks.values():
            t["start_date"] = date_of(at, t["ES"], t["duration"]).isoformat()
            # A task of d days starting at offset ES finishes on offset ES+d-1.
            t["finish_date"] = at(max(t["EF"] - 1, t["ES"])).isoformat() if t["duration"] else t["start_date"]

    cols = ["id", "name", "duration", "ES", "EF", "LS", "LF", "float"] + (["start_date", "finish_date"] if at else [])
    widths = {c: max(len(c), *(len(fmt(tasks[t][c]) if isinstance(tasks[t][c], float) else str(tasks[t][c])) for t in order)) for c in cols}
    print("  ".join(c.ljust(widths[c]) for c in cols))
    for tid in order:
        t = tasks[tid]
        print("  ".join((fmt(t[c]) if isinstance(t[c], float) else str(t[c])).ljust(widths[c]) for c in cols))

    crit = critical_chain(tasks, order)
    print(f"\nProject duration: {fmt(end)} working days")
    if at:
        print(f"Finish date: {at(max(end - 1, 0)).isoformat()}")
    print("Critical tasks (zero float, in dependency order): " + ", ".join(crit))
    negative = [tid for tid in order if tasks[tid]["float"] < -1e-9]
    if negative:
        print("WARNING: negative float on " + ", ".join(negative))

    if args.out:
        base = [c for c in tasks[order[0]].keys() if not c.startswith("_") and c not in cols]
        out_cols = ["id", "name", "duration"] + [c for c in base if c not in ("id", "name", "duration")] + cols[3:] + ["critical"]
        with open(args.out, "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=out_cols, extrasaction="ignore")
            w.writeheader()
            for tid in order:
                row = {k: (fmt(v) if isinstance(v, float) else v) for k, v in tasks[tid].items()}
                row["critical"] = "yes" if tid in crit else ""
                w.writerow(row)
        print(f"Wrote {args.out}")

    if args.gantt:
        if not at:
            sys.exit("--gantt needs --start so bars have dates.")
        write_gantt(args.gantt, tasks, order, at, args.title, holidays)
        print(f"Wrote {args.gantt}")


if __name__ == "__main__":
    main()
