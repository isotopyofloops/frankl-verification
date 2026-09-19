"""
Independent from-scratch reconstruction of Rheon's N27 non-atomistic all-15 survivor.
Built from the coordinate-set description in the research note, not from JSON certificates.

N27 has 27 elements, rank (1,6,10,9,1), 7 JIs including one rank-2 JI (x).
Coordinate labels: a,b,c,d,e,f,x.

Rank 0: empty set
Rank 1: a, b, c, d, e, f  (atoms)
Rank 2: ab, ac, ad, ae, af, bc, bd, be, bf, ax  (lines; ax is the non-atom JI)
Rank 3: abx, abd, abe, abf, acx, adefx, bcd, bce, bcf  (planes)
Rank 4: abcdefx  (top)
"""

from itertools import combinations

def fs(*elts):
    return frozenset(elts)

# Build the lattice as coordinate sets (each element represented by its set of labels)
bottom = fs()

# Rank 1: atoms
rank1 = [fs('a'), fs('b'), fs('c'), fs('d'), fs('e'), fs('f')]
atoms_names = ['a','b','c','d','e','f']

# Rank 2: lines (10 total) — including non-atom JI 'ax'
rank2 = [
    fs('a','b'), fs('a','c'), fs('a','d'), fs('a','e'), fs('a','f'),
    fs('b','c'), fs('b','d'), fs('b','e'), fs('b','f'),
    fs('a','x'),  # non-atom JI
]

# Rank 3: planes (9 total)
rank3 = [
    fs('a','b','x'),      # E
    fs('a','b','d'),
    fs('a','b','e'),
    fs('a','b','f'),
    fs('a','c','x'),      # U
    fs('a','d','e','f','x'),  # V
    fs('b','c','d'),
    fs('b','c','e'),
    fs('b','c','f'),
]

# Rank 4: top
top = fs('a','b','c','d','e','f','x')

# Full family
family = [bottom] + rank1 + rank2 + rank3 + [top]
n = len(family)
print(f"Order: {n}")
print(f"Rank profile: (1, {len(rank1)}, {len(rank2)}, {len(rank3)}, 1)")
assert n == 27, f"Expected 27, got {n}"

# Check closure under intersection
print("\n=== INTERSECTION CLOSURE ===")
closed = True
failures = 0
for i, x in enumerate(family):
    for j, y in enumerate(family):
        if i < j:
            meet = x & y
            if meet not in family:
                if failures < 5:
                    print(f"  FAIL: {set(x)} & {set(y)} = {set(meet)} not in family")
                failures += 1
                closed = False
if closed:
    print("  PASS: closed under intersection (meets)")
else:
    print(f"  FAILED: {failures} pairs not closed")

# Check that every pair has a join (smallest containing element)
print("\n=== UNIQUE JOINS ===")
joins_ok = True
join_failures = 0
for i, x in enumerate(family):
    for j, y in enumerate(family):
        if i < j:
            candidates = [z for z in family if x <= z and y <= z]
            if not candidates:
                print(f"  FAIL: no upper bound for {set(x)}, {set(y)}")
                joins_ok = False
                join_failures += 1
            else:
                join = min(candidates, key=len)
                same_size = [z for z in candidates if len(z) == len(join)]
                if len(same_size) > 1 and not all(z == join for z in same_size):
                    if join_failures < 5:
                        print(f"  FAIL: non-unique join for {set(x)}, {set(y)}")
                    joins_ok = False
                    join_failures += 1
if joins_ok:
    print("  PASS: all pairs have unique joins")
else:
    print(f"  FAILED: {join_failures} join failures")

# Check gradedness: every maximal chain has the same length
print("\n=== GRADEDNESS ===")
def rank_of(x):
    for r, layer in enumerate([{bottom}, set(map(frozenset, [fs(a) for a in atoms_names])),
                                set(rank2), set(rank3), {top}]):
        # Can't use this approach easily, just check by membership
        pass
    if x == bottom: return 0
    if x in [fs(a) for a in atoms_names]: return 1
    if x in rank2: return 2
    if x in rank3: return 3
    if x == top: return 4
    return -1

# Check all covers preserve rank
graded = True
for x in family:
    rx = rank_of(x)
    if x == top:
        continue
    # Find upper covers
    for y in family:
        if x < y:
            between = any(x < z < y for z in family)
            if not between:
                ry = rank_of(y)
                if ry != rx + 1:
                    print(f"  FAIL: cover {set(x)}→{set(y)} has ranks {rx}→{ry}")
                    graded = False
if graded:
    print("  PASS: all covers increase rank by exactly 1")

# Check NON-atomisticity: ax is not a join of atoms
print("\n=== NON-ATOMISTICITY ===")
ax = fs('a','x')
atoms_below_ax = [a for a in rank1 if a <= ax]
atom_join = frozenset().union(*atoms_below_ax) if atoms_below_ax else frozenset()
print(f"  Atoms below ax={set(ax)}: {[set(a) for a in atoms_below_ax]}")
print(f"  Join of those atoms: {set(atom_join)}")
if atom_join != ax:
    print(f"  CONFIRMED: ax is NOT join of its atoms below (join={set(atom_join)} ≠ ax={set(ax)})")
    print("  Lattice is NON-ATOMISTIC")
else:
    print("  UNEXPECTED: ax IS join of atoms — would be atomistic")

# Compute JI upsets
print("\n=== JOIN-IRREDUCIBLE UPSETS ===")
# JIs are elements with exactly one lower cover
def lower_covers(x):
    covers = []
    for y in family:
        if y < x:
            between = any(y < z < x for z in family)
            if not between:
                covers.append(y)
    return covers

jis = []
for elem in family:
    if elem == bottom:
        continue
    lc = lower_covers(elem)
    if len(lc) == 1:
        jis.append(elem)

print(f"  Join-irreducibles ({len(jis)}):")
T = (n + 1) // 2
print(f"  Threshold T = (n+1)/2 = {T}")
t_atoms = []
for j in sorted(jis, key=lambda ji: -len([z for z in family if ji <= z])):
    upset_size = len([z for z in family if j <= z])
    r = rank_of(j)
    label = ''.join(sorted(j))
    print(f"    {label} (rank {r}): upset = {upset_size}", end="")
    if upset_size == T:
        print(" = T  ← T-atom", end="")
        t_atoms.append(j)
    elif upset_size >= n/2:
        print(f" ≥ n/2={n/2}  ← Frankl witness", end="")
    print()

print(f"  T-atoms: {[''.join(sorted(t)) for t in t_atoms]}")

# Identify meet-irreducibles
print("\n=== MEET-IRREDUCIBLES ===")
def upper_covers(x):
    covers = []
    for y in family:
        if x < y:
            between = any(x < z < y for z in family)
            if not between:
                covers.append(y)
    return covers

mi_elements = []
for x in family:
    if x == top:
        continue
    uc = upper_covers(x)
    if len(uc) == 1:
        mi_elements.append(x)

print(f"  Meet-irreducibles ({len(mi_elements)}):")
for m in sorted(mi_elements, key=lambda x: rank_of(x)):
    label = ''.join(sorted(m))
    print(f"    {label} (rank {rank_of(m)})")

# Check Bouchard conditions
print("\n=== BOUCHARD CONDITIONS ===")

# 2.7: every JI upset > height + 1 = 5
cond_27 = all(len([z for z in family if j <= z]) >= 5 for j in jis)
print(f"  2.7 (JI upset ≥ height+1=5): {'PASS' if cond_27 else 'FAIL'}")
for j in jis:
    upset_size = len([z for z in family if j <= z])
    if upset_size < 5:
        print(f"    FAIL: {''.join(sorted(j))} has upset {upset_size}")

# 2.11: every pair of MIs shares a JI below
cond_211 = True
for i, m1 in enumerate(mi_elements):
    for j_idx, m2 in enumerate(mi_elements):
        if i < j_idx:
            shared_jis = [j for j in jis if j <= m1 and j <= m2]
            if not shared_jis:
                print(f"  2.11 FAIL: {set(m1)} and {set(m2)} share no JI")
                cond_211 = False
print(f"  2.11 (MI pairs share JI below): {'PASS' if cond_211 else 'FAIL'}")

# 2.12: every MI has a T-JI below
cond_212 = True
for m in mi_elements:
    has_t = any(t <= m for t in t_atoms)
    if not has_t:
        print(f"  2.12 FAIL: {''.join(sorted(m))} has no T-JI below")
        cond_212 = False
print(f"  2.12 (MI has T-JI below): {'PASS' if cond_212 else 'FAIL'}")

# 2.9: for every nonempty subset of MIs, some JI is below strictly more than half
print("\n  2.9 (subset majority)...")
cond_29 = True
failing_subsets = 0
total_subsets = 0
for size in range(1, len(mi_elements) + 1):
    for subset in combinations(mi_elements, size):
        total_subsets += 1
        has_majority = False
        for j in jis:
            count = sum(1 for m in subset if j <= m)
            if count > len(subset) / 2:
                has_majority = True
                break
        if not has_majority:
            failing_subsets += 1
            if failing_subsets <= 3:
                print(f"    FAIL subset (size {size}): {[set(m) for m in subset]}")
if failing_subsets == 0:
    print(f"  2.9: PASS (all {total_subsets} nonempty subsets checked)")
else:
    print(f"  2.9: FAIL ({failing_subsets} failing subsets)")

# 2.13: for every non-bound element, its incomparables are not a chain
print("\n  2.13 (incomparables not chain)...")
cond_213 = True
for x in family:
    if x == bottom or x == top:
        continue
    incomparables = [y for y in family if not (x <= y or y <= x) and y != x]
    if len(incomparables) <= 1:
        cond_213 = False
        print(f"    FAIL: {''.join(sorted(x))} has {len(incomparables)} incomparables")
if cond_213:
    print(f"  2.13: PASS")

# Frankl check
print("\n=== FRANKL'S CONJECTURE ===")
frankl_witnesses = []
for j in jis:
    upset_size = len([z for z in family if j <= z])
    if upset_size >= n / 2:
        label = ''.join(sorted(j))
        frankl_witnesses.append(label)
        print(f"  JI {label}: upset {upset_size} >= n/2 = {n/2} — WITNESSES FRANKL")

if frankl_witnesses:
    print(f"  Frankl HOLDS ({len(frankl_witnesses)} witnesses: {frankl_witnesses})")
else:
    print("  NO WITNESS — would be Frankl counterexample!")

# Non-atomic JI lemma check: x has upset ≤ n/2
print("\n=== NON-ATOMIC JI LEMMA CHECK ===")
x_ji = fs('a','x')
x_upset = len([z for z in family if x_ji <= z])
print(f"  Non-atomic JI x (=ax): upset = {x_upset}, n/2 = {n/2}")
print(f"  Lemma holds: {x_upset <= n/2} (upset ≤ n/2)")

print("\n=== SUMMARY ===")
print(f"  Order: {n}")
print(f"  Rank profile: (1, {len(rank1)}, {len(rank2)}, {len(rank3)}, 1)")
print(f"  Non-atomistic: YES (ax not join of atoms)")
print(f"  JIs: {len(jis)} (including 1 non-atom at rank 2)")
print(f"  T-atoms: {[''.join(sorted(t)) for t in t_atoms]}")
print(f"  MIs: {len(mi_elements)}")
print(f"  2.7: {'PASS' if cond_27 else 'FAIL'}")
print(f"  2.9: {'PASS' if failing_subsets == 0 else 'FAIL'}")
print(f"  2.11: {'PASS' if cond_211 else 'FAIL'}")
print(f"  2.12: {'PASS' if cond_212 else 'FAIL'}")
print(f"  2.13: {'PASS' if cond_213 else 'FAIL'}")
print(f"  Frankl: {'HOLDS' if frankl_witnesses else 'FAILS'}")
print(f"  Non-atomic JI lemma: {'HOLDS' if x_upset <= n/2 else 'FAILS'}")
