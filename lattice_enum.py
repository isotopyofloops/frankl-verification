#!/usr/bin/env python3
"""
Enumerate small labeled lattices and run Bouchard filters.

For n elements {0..n-1}, generate strict orders via bitmasks over ordered pairs,
keep posets that are lattices, apply check_all_bouchard (+ optional Thm 2.9).

WARNING (Rheon review 2026-09-18): this enumerator generates directed-edge
subsets then takes transitive closure WITHOUT deduplicating isomorphic
order matrices. Different edge sets can yield the same partial order
(e.g. 0<1,1<2 with or without 0<2). Do NOT treat raw counts as a
trustworthy labeled-lattice census. Manuscript tables use a separate
graded-atomistic enumeration (atom-set representation). Prefer that
pipeline for published counts; use this file only for filter smoke tests.

Usage:
  python3 lattice_enum.py --n-max 5
  python3 lattice_enum.py --n-max 4 --json-out lattice_enum_n4.json
"""

from __future__ import annotations

import argparse
import json
import sys
import time
from itertools import combinations
from pathlib import Path

from bouchard_filters import (
    LatticeInfo,
    check_all_bouchard,
    check_meet_irr_subset_coverage,
    passes_all,
)


def leq_matrix_from_strict(n, strict_pairs):
    """strict_pairs: set of (i,j) meaning i < j. Build reflexive transitive leq."""
    leq = [[False] * n for _ in range(n)]
    for i in range(n):
        leq[i][i] = True
    for i, j in strict_pairs:
        leq[i][j] = True
    # Floyd-Warshall transitive closure
    for k in range(n):
        for i in range(n):
            if leq[i][k]:
                for j in range(n):
                    if leq[k][j]:
                        leq[i][j] = True
    return leq


def is_poset(n, leq):
    # antisymmetric: leq[i][j] and leq[j][i] ⇒ i==j
    for i in range(n):
        for j in range(n):
            if i != j and leq[i][j] and leq[j][i]:
                return False
    return True


def hasse_from_leq(n, leq):
    """Hasse: node -> set of covered nodes (immediate lower). LatticeInfo convention."""
    hasse = {i: set() for i in range(n)}
    for j in range(n):
        for i in range(n):
            if i == j or not leq[i][j]:
                continue
            # i < j strictly
            between = False
            for k in range(n):
                if k == i or k == j:
                    continue
                if leq[i][k] and leq[k][j] and i != k and k != j:
                    # strict: not leq[k][i] etc already
                    if not (leq[k][i] or leq[j][k]):
                        between = True
                        break
            if not between:
                hasse[j].add(i)  # j covers i
    return hasse


def is_lattice_leq(n, leq):
    """Every pair has unique join (lub) and meet (glb)."""
    for a, b in combinations(range(n), 2):
        # upper bounds
        upper = [x for x in range(n) if leq[a][x] and leq[b][x]]
        if not upper:
            return False
        # lub = least upper: in all upper and leq to all others
        lubs = []
        for u in upper:
            if all(leq[u][v] for v in upper):
                lubs.append(u)
        if len(lubs) != 1:
            return False
        lower = [x for x in range(n) if leq[x][a] and leq[x][b]]
        if not lower:
            return False
        glbs = []
        for g in lower:
            if all(leq[v][g] for v in lower):
                glbs.append(g)
        if len(glbs) != 1:
            return False
    return True


def enumerate_lattices(n):
    """Yield (hasse, leq) for each labeled lattice on n elements."""
    pairs = [(i, j) for i in range(n) for j in range(n) if i != j]
    n_pairs = len(pairs)
    seen = 0
    for mask in range(1 << n_pairs):
        strict = set()
        for b, (i, j) in enumerate(pairs):
            if mask & (1 << b):
                strict.add((i, j))
        leq = leq_matrix_from_strict(n, strict)
        if not is_poset(n, leq):
            continue
        if not is_lattice_leq(n, leq):
            continue
        hasse = hasse_from_leq(n, leq)
        seen += 1
        yield hasse, leq
    return


def run_n(n, use_thm29=True):
    t0 = time.time()
    total_lat = 0
    pass_std = 0
    pass_29 = 0
    survivors = []
    fail_counts = {}
    for hasse, leq in enumerate_lattices(n):
        total_lat += 1
        info = LatticeInfo(hasse)
        if not info.is_lattice:
            continue  # Hasse/LatticeInfo disagreement — skip
        results = check_all_bouchard(info)
        # remove 2.9 from standard if present in ALL_FILTERS for fair split
        std_ok = all(
            p for name, (p, _) in results.items() if not name.startswith("2.9")
        )
        thm29_ok = None
        if use_thm29:
            thm29_ok, _ = check_meet_irr_subset_coverage(info)
        if std_ok:
            pass_std += 1
        if use_thm29 and thm29_ok and std_ok:
            pass_29 += 1
        if std_ok:
            survivors.append(
                {
                    "n": n,
                    "|L|": info.n,
                    "thm29": thm29_ok,
                    "join_irr": sorted(info.join_irreducibles),
                    "meet_irr": sorted(info.meet_irreducibles),
                }
            )
        for name, (p, d) in results.items():
            if not p and not name.startswith("2.9"):
                fail_counts[name] = fail_counts.get(name, 0) + 1
    return {
        "n": n,
        "labeled_lattices": total_lat,
        "pass_bouchard_std": pass_std,
        "pass_std_and_thm29": pass_29 if use_thm29 else None,
        "fail_counts": fail_counts,
        "survivors_head": survivors[:20],
        "n_survivors": len(survivors),
        "elapsed_s": round(time.time() - t0, 3),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--n-max", type=int, default=4)
    ap.add_argument("--n-min", type=int, default=1)
    ap.add_argument("--json-out", type=Path, default=None)
    ap.add_argument("--no-thm29", action="store_true")
    args = ap.parse_args()
    rows = []
    for n in range(args.n_min, args.n_max + 1):
        print(f"=== n={n} ===", flush=True)
        r = run_n(n, use_thm29=not args.no_thm29)
        rows.append(r)
        print(
            f"  lattices={r['labeled_lattices']} pass_std={r['pass_bouchard_std']} "
            f"pass+29={r['pass_std_and_thm29']} t={r['elapsed_s']}s",
            flush=True,
        )
        print(f"  fail_counts={r['fail_counts']}", flush=True)
    if args.json_out:
        args.json_out.write_text(json.dumps(rows, indent=2))
        print("wrote", args.json_out, flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
