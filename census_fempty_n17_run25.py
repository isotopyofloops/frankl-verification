#!/usr/bin/env python3
"""
n=17 F=∅ 0-MI census — Fable 8 machine-readable fields (construction_guidance_fempty.md).

Pipeline: graded atomic height-4, linear-ish prune (|A_i∩A_j|≤1, |B_i∩B_j|≤1),
full cover of atoms/r2, col sizes ≥2, Fempty (deg r2 ≥2), 0-MI (c2 ≥2).
Lattice via bit-upset join/meet tables (same as zoo_probe / probe_femptyset).

Regression: C5-complement (k=5,s2=5,s3=5) MUST appear.

Usage:
  python3 census_fempty_n17_run25.py                # full n=17 (may be long)
  python3 census_fempty_n17_run25.py --doubleton-only
  python3 census_fempty_n17_run25.py --shapes 5,5,5
  python3 census_fempty_n17_run25.py --n 15         # empty regression
"""
from __future__ import annotations

import argparse
import json
import time
from collections import Counter
from itertools import combinations, permutations
from typing import Any


def is_lattice(n, k, s2, s3, A, B):
    atom = lambda i: 1 + i
    r2 = lambda i: 1 + k + i
    r3 = lambda i: 1 + k + s2 + i
    top = n - 1
    upcov = [[] for _ in range(n)]
    for i in range(k):
        upcov[0].append(atom(i))
    for j, c in enumerate(A):
        for i in c:
            upcov[atom(i)].append(r2(j))
    for j, c in enumerate(B):
        for i in c:
            upcov[r2(i)].append(r3(j))
    for j in range(s3):
        upcov[r3(j)].append(top)
    up = [0] * n
    for x in range(n - 1, -1, -1):
        m = 1 << x
        for y in upcov[x]:
            m |= up[y]
        up[x] = m
    dn = [0] * n
    for x in range(n):
        for y in range(n):
            if (up[y] >> x) & 1:
                dn[x] |= 1 << y
    for x in range(n):
        for y in range(x + 1, n):
            c = dn[x] & dn[y]
            if not any(dn[z] == c for z in range(n) if (c >> z) & 1):
                return None
            c = up[x] & up[y]
            if not any(up[z] == c for z in range(n) if (c >> z) & 1):
                return None
    return up, dn


def record_fields(n, k, s2, s3, A, B, up):
    """Fable 8 machine-readable fields + filter pack."""
    atom = lambda i: 1 + i
    r2 = lambda i: 1 + k + i
    r3 = lambda i: 1 + k + s2 + i
    ups = lambda x: bin(up[x]).count("1")

    # 1 shape
    line_sizes = sorted(len(c) for c in A)
    block_sizes = sorted(len(c) for c in B)  # in r2-index cols
    # also atom-content of blocks for displacement
    block_atoms = []
    for bj, bc in enumerate(B):
        atoms_in = set()
        for li in bc:
            atoms_in |= set(A[li])
        block_atoms.append(frozenset(atoms_in))

    # 2 upsets / gap
    aups = [ups(atom(i)) for i in range(k)]
    T = (n + 1) // 2 if n % 2 else None
    maxup = max(aups) if aups else 0
    gap = (T - maxup) if T is not None else None

    # 3 T-atoms + displacement map
    T_atoms = [i for i in range(k) if aups[i] == T]
    r3_has_T = []
    for ba in block_atoms:
        r3_has_T.append(any(i in ba for i in T_atoms))

    # 4 pair-completeness for each T-atom
    c2 = [sum(1 for c in A if i in c) for i in range(k)]
    pair_complete = []
    for a in T_atoms:
        lines_thru = [c for c in A if a in c]
        all_doubleton = all(len(c) == 2 for c in lines_thru)
        pair_complete.append(
            {
                "a": a,
                "c2": c2[a],
                "k_minus_1": k - 1,
                "c2_eq_k_minus_1": c2[a] == k - 1,
                "all_r2_thru_a_doubleton": all_doubleton,
            }
        )

    # 5 two-T
    two_T = len(T_atoms) >= 2

    # 6 atom below all rank-3
    atom_below_all_r3 = []
    for i in range(k):
        if all((up[atom(i)] >> r3(j)) & 1 for j in range(s3)):
            atom_below_all_r3.append(i)

    # 7 filters 2.7 / 2.11 / 2.12
    # meet-irreducibles: atoms with c2==1 (none in 0-MI), r2 with deg==1 (none Fempty), all r3
    degB = [0] * s2
    for c in B:
        for i in c:
            degB[i] += 1
    Mset = (
        [atom(i) for i in range(k) if c2[i] == 1]
        + [r2(i) for i in range(s2) if degB[i] == 1]
        + [r3(i) for i in range(s3)]
    )
    c27 = all(u > 4 for u in aups)
    c211 = True
    for i in range(len(Mset)):
        for j in range(i + 1, len(Mset)):
            if not any(
                (up[atom(a)] >> Mset[i]) & 1 and (up[atom(a)] >> Mset[j]) & 1
                for a in range(k)
            ):
                c211 = False
                break
        if not c211:
            break
    c212 = (n % 2 == 1) and all(
        any((up[atom(a)] >> m) & 1 and aups[a] == T for a in range(k)) for m in Mset
    )

    # 8 automorphism count (cheap: atom-label perms preserving A,B up to line/block perm)
    aut = None
    if k <= 7 and s2 <= 8 and s3 <= 8:
        Aset = frozenset(A)
        # B as sets of atom-lines: map each B-col to frozenset of A-lines
        # For aut we need induced action on lines
        aut = count_atom_aut(k, A, B)

    return {
        # field 1
        "n": n,
        "k": k,
        "s2": s2,
        "s3": s3,
        "line_size_dist": dict(Counter(line_sizes)),
        "block_size_dist": dict(Counter(block_sizes)),
        "A": [sorted(c) for c in A],
        "B": [sorted(c) for c in B],
        # field 2
        "atom_upsets": aups,
        "T": T,
        "max_upset": maxup,
        "gap": gap,
        # field 3
        "T_atoms": T_atoms,
        "T_atom_count": len(T_atoms),
        "r3_contains_T_atom": r3_has_T,
        # field 4
        "pair_completeness": pair_complete,
        # field 5
        "two_T_atom_exists": two_T,
        # field 6
        "atoms_below_all_r3": atom_below_all_r3,
        # field 7
        "c27": c27,
        "c211": c211,
        "c212": c212,
        # field 8
        "aut_atom_label": aut,
        "c2": c2,
        "all_doubleton_lines": all(len(c) == 2 for c in A),
    }


def count_atom_aut(k, A, B):
    """Count atom permutations inducing a lattice automorphism (lines/blocks preserved)."""
    A_f = frozenset(frozenset(c) for c in A)
    # For each B-col (set of line indices), get the set of atom-sets
    def block_sig(A_list, B_list):
        lines = list(A_list)
        sigs = []
        for bc in B_list:
            sigs.append(frozenset(frozenset(lines[i]) for i in bc))
        return frozenset(sigs)

    target_lines = A_f
    target_blocks = block_sig(A, B)
    count = 0
    # only try if k small
    atoms = list(range(k))
    for perm in permutations(atoms):
        # map old->new
        def mp(s):
            return frozenset(perm[i] for i in s)

        new_lines = frozenset(mp(c) for c in A)
        if new_lines != target_lines:
            continue
        # lines may reorder: build index map from frozenset -> list of matching indices
        line_list = list(A)
        # for each old line index, new line content
        new_A = [mp(c) for c in A]
        # B cols as sets of new line contents
        ok = True
        new_block_sigs = []
        for bc in B:
            new_block_sigs.append(frozenset(new_A[i] for i in bc))
        if frozenset(new_block_sigs) != target_blocks:
            continue
        count += 1
    return count


def is_c5_complement(rec):
    """Regression anchor: Iso Petersen-type at n=17, k=5, doubleton cycle + triple complements."""
    if rec["n"] != 17 or rec["k"] != 5 or rec["s2"] != 5 or rec["s3"] != 5:
        return False
    if not rec["all_doubleton_lines"]:
        return False
    # up to atom relabel: lines form C5, blocks the complementary 3-sets
    A = [frozenset(c) for c in rec["A"]]
    # each atom in exactly 2 lines for C5
    if sorted(rec["c2"]) != [2, 2, 2, 2, 2]:
        return False
    if rec["atom_upsets"] != [7, 7, 7, 7, 7]:
        return False
    if not (rec["c27"] and rec["c211"] and not rec["c212"]):
        return False
    if rec["gap"] != 2:  # T=9, max=7
        return False
    return True


def search_shape(n, k, s2, s3, doubleton_only=False, max_store=200):
    acols = [
        frozenset(c)
        for r in range(2, (3 if doubleton_only else k + 1))
        for c in combinations(range(k), r)
    ]
    if doubleton_only:
        acols = [frozenset(c) for c in combinations(range(k), 2)]
    bcols = [frozenset(c) for r in range(2, s2 + 1) for c in combinations(range(s2), r)]
    stats = Counter()
    hits = []
    t0 = time.time()
    for A in combinations(acols, s2):
        ok = True
        for i in range(s2):
            for j in range(i + 1, s2):
                if len(A[i] & A[j]) > 1:
                    ok = False
                    break
            if not ok:
                break
        if not ok:
            continue
        if frozenset().union(*A) != frozenset(range(k)):
            continue
        c2 = [sum(1 for c in A if i in c) for i in range(k)]
        if any(v < 2 for v in c2):
            continue  # 0-MI
        stats["A_pass"] += 1
        for B in combinations(bcols, s3):
            ok = True
            for i in range(s3):
                for j in range(i + 1, s3):
                    if len(B[i] & B[j]) > 1:
                        ok = False
                        break
                if not ok:
                    break
            if not ok:
                continue
            if frozenset().union(*B) != frozenset(range(s2)):
                continue
            deg = [0] * s2
            for c in B:
                for i in c:
                    deg[i] += 1
            if any(d < 2 for d in deg):
                continue  # Fempty
            stats["systems"] += 1
            lat = is_lattice(n, k, s2, s3, A, B)
            if lat is None:
                continue
            up, _dn = lat
            stats["lattices"] += 1
            rec = record_fields(n, k, s2, s3, A, B, up)
            if rec["c27"] and rec["c211"]:
                stats["hunt"] += 1  # pass 2.7 ∧ 2.11
            if rec["c212"]:
                stats["c212"] += 1
            if rec["two_T_atom_exists"]:
                stats["twoT"] += 1
            if any(pc["c2_eq_k_minus_1"] for pc in rec["pair_completeness"]):
                stats["pair_complete_T"] += 1
            if any(not pc["c2_eq_k_minus_1"] for pc in rec["pair_completeness"]):
                stats["pair_incomplete_T"] += 1
            if rec["atoms_below_all_r3"]:
                stats["disp_hyp"] += 1
            if len(hits) < max_store:
                hits.append(rec)
            elif is_c5_complement(rec) and not any(is_c5_complement(h) for h in hits):
                hits.append(rec)
    elapsed = time.time() - t0
    return dict(stats), hits, round(elapsed, 3)


def enumerate_n(
    n: int,
    doubleton_only: bool = False,
    shapes: list[tuple[int, int, int]] | None = None,
    max_store: int = 200,
):
    assert n % 2 == 1
    inner = n - 2
    all_hits = []
    by_shape = []
    totals = Counter()
    t0 = time.time()
    if shapes is None:
        shape_iter = []
        for k in range(3, inner - 3):
            for s2 in range(2, inner - k):
                s3 = inner - k - s2
                if s3 < 2:
                    continue
                shape_iter.append((k, s2, s3))
    else:
        shape_iter = shapes
    for k, s2, s3 in shape_iter:
        print(f"  shape k={k} s2={s2} s3={s3} doubleton_only={doubleton_only} ...", flush=True)
        stats, hits, elapsed = search_shape(
            n, k, s2, s3, doubleton_only=doubleton_only, max_store=max_store
        )
        by_shape.append(
            {
                "k": k,
                "s2": s2,
                "s3": s3,
                "stats": stats,
                "elapsed_sec": elapsed,
                "n_hits_stored": len(hits),
            }
        )
        for key, v in stats.items():
            totals[key] += v
        all_hits.extend(hits)
        if stats.get("lattices"):
            print(
                f"    lat={stats.get('lattices',0)} hunt={stats.get('hunt',0)} "
                f"twoT={stats.get('twoT',0)} systems={stats.get('systems',0)} "
                f"t={elapsed}s",
                flush=True,
            )
    # C5 regression
    c5_found = any(is_c5_complement(h) for h in all_hits) if n == 17 else None
    # also explicit C5 construct check
    c5_construct = None
    if n == 17:
        R2 = [frozenset({i, (i + 1) % 5}) for i in range(5)]
        # B as covers of lines: for C5, each triple of consecutive-ish lines
        # Original zoo: R3 as atom sets; convert to r2-index covers
        # lines: L_i = {i,i+1}
        # block i covers atoms {(i+2)%5,(i+3)%5,(i+4)%5} = all except i and i+1
        # lines inside those atoms: lines wholly in the 3-set
        R3_atoms = [frozenset({(i + 2) % 5, (i + 3) % 5, (i + 4) % 5}) for i in range(5)]
        B = []
        for P in R3_atoms:
            cov = frozenset(j for j, L in enumerate(R2) if L <= P)
            B.append(cov)
        lat = is_lattice(17, 5, 5, 5, R2, B)
        if lat:
            rec = record_fields(17, 5, 5, 5, R2, B, lat[0])
            c5_construct = rec
            if not any(is_c5_complement(h) for h in all_hits):
                all_hits.append(rec)
            c5_found = is_c5_complement(rec)

    # summary aggregates for gate fields 4 and 5
    field4_gate = {
        "lattices_with_T": sum(1 for h in all_hits if h["T_atom_count"] > 0),
        "T_instances_pair_complete": sum(
            1
            for h in all_hits
            for pc in h["pair_completeness"]
            if pc["c2_eq_k_minus_1"] and pc["all_r2_thru_a_doubleton"]
        ),
        "T_instances_incomplete": sum(
            1
            for h in all_hits
            for pc in h["pair_completeness"]
            if not pc["c2_eq_k_minus_1"]
        ),
        "T_instances_nondoubleton_line": sum(
            1
            for h in all_hits
            for pc in h["pair_completeness"]
            if not pc["all_r2_thru_a_doubleton"]
        ),
    }
    field5_gate = {
        "lattices_with_2T": sum(1 for h in all_hits if h["two_T_atom_exists"]),
        "all_shared_case_populated": None,  # needs deeper ab classification; flag later
    }

    return {
        "n": n,
        "pipeline": "alethon-fempty-0mi-fable8",
        "doubleton_only": doubleton_only,
        "totals": dict(totals),
        "by_shape": by_shape,
        "hits": all_hits,
        "c5_complement_regression": c5_found,
        "c5_construct": c5_construct,
        "field4_pair_completeness_gate": field4_gate,
        "field5_twoT_gate": field5_gate,
        "elapsed_sec": round(time.time() - t0, 3),
        "note": "hits may be capped per shape; totals.lattices is complete for shapes searched",
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=int, default=17)
    ap.add_argument("--doubleton-only", action="store_true")
    ap.add_argument(
        "--shapes",
        default=None,
        help="comma triples k.s2.s3 e.g. 5.5.5,5.4.6",
    )
    ap.add_argument("--json-out", default="census_fempty_n17_run25.json")
    ap.add_argument("--max-store", type=int, default=100)
    args = ap.parse_args()
    shapes = None
    if args.shapes:
        shapes = []
        for tok in args.shapes.split(","):
            k, s2, s3 = map(int, tok.replace("x", ".").split("."))
            shapes.append((k, s2, s3))
    print(
        f"=== F=∅ 0-MI census n={args.n} doubleton_only={args.doubleton_only} ===",
        flush=True,
    )
    r = enumerate_n(
        args.n,
        doubleton_only=args.doubleton_only,
        shapes=shapes,
        max_store=args.max_store,
    )
    print(
        f"DONE n={args.n}: lat={r['totals'].get('lattices',0)} "
        f"hunt={r['totals'].get('hunt',0)} twoT={r['totals'].get('twoT',0)} "
        f"c5_reg={r['c5_complement_regression']} elapsed={r['elapsed_sec']}s",
        flush=True,
    )
    print("field4 gate:", r["field4_pair_completeness_gate"], flush=True)
    print("field5 gate:", r["field5_twoT_gate"], flush=True)
    # strip heavy for json if many hits — keep all for now under cap
    with open(args.json_out, "w") as f:
        json.dump(r, f, indent=2)
    print("wrote", args.json_out, flush=True)


if __name__ == "__main__":
    main()
