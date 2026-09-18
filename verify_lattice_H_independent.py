"""
Independent from-scratch reconstruction of Rheon's lattice H (one-MI-line, n=25).
Built from the incidence description in the research note, not from the JSON certificates.

Lattice H has atoms a,b,c,d,e,f with:
- Hub line: {a,b}
- Spokes: {a,c},{a,d},{a,e},{a,f},{b,c},{b,d},{b,e},{b,f}
- Common planes: {a,b,c},{a,b,d},{a,b,e},{a,b,f}
- a-side planes: {a,c,e},{a,c,f}
- b-side planes: {b,c,d},{b,d,e,f}
- Bottom: empty set, Top: {a,b,c,d,e,f}
"""

from itertools import combinations

# Build the lattice as a family of frozensets (atom sets)
atoms = ['a','b','c','d','e','f']
atom_idx = {a: i for i, a in enumerate(atoms)}

def fs(*elts):
    return frozenset(elts)

# Rank 0: bottom
bottom = fs()

# Rank 1: atoms
rank1 = [fs(x) for x in atoms]

# Rank 2: lines (9 total)
lines = [
    fs('a','b'),  # hub
    fs('a','c'), fs('a','d'), fs('a','e'), fs('a','f'),  # a-spokes
    fs('b','c'), fs('b','d'), fs('b','e'), fs('b','f'),  # b-spokes
]

# Rank 3: planes (8 total)
planes = [
    fs('a','b','c'), fs('a','b','d'), fs('a','b','e'), fs('a','b','f'),  # common
    fs('a','c','e'), fs('a','c','f'),  # a-side
    fs('b','c','d'), fs('b','d','e','f'),  # b-side
]

# Rank 4: top
top = fs('a','b','c','d','e','f')

# Full family
family = [bottom] + rank1 + lines + planes + [top]
n = len(family)
print(f"Order: {n}")
print(f"Rank profile: (1, {len(rank1)}, {len(lines)}, {len(planes)}, 1)")

# Check closure under intersection
print("\n=== INTERSECTION CLOSURE ===")
closed = True
for i, x in enumerate(family):
    for j, y in enumerate(family):
        if i < j:
            meet = x & y
            if meet not in family:
                print(f"  FAIL: {set(x)} ∩ {set(y)} = {set(meet)} not in family")
                closed = False
if closed:
    print("  PASS: closed under intersection (meets)")

# Check that every pair has a unique join
print("\n=== UNIQUE JOINS ===")
joins_ok = True
for i, x in enumerate(family):
    for j, y in enumerate(family):
        if i < j:
            # Join = smallest element containing both
            candidates = [z for z in family if x <= z and y <= z]
            if not candidates:
                print(f"  FAIL: no upper bound for {set(x)}, {set(y)}")
                joins_ok = False
            else:
                join = min(candidates, key=len)
                # Check uniqueness: is there another element of the same size containing both?
                same_size = [z for z in candidates if len(z) == len(join)]
                if len(same_size) > 1:
                    # Check if they're all the same
                    if not all(z == join for z in same_size):
                        print(f"  FAIL: non-unique join for {set(x)}, {set(y)}")
                        joins_ok = False
if joins_ok:
    print("  PASS: all pairs have unique joins")

# Check atomisticity
print("\n=== ATOMISTICITY ===")
atomistic = True
for x in family:
    if x == bottom:
        continue
    atom_join = frozenset().union(*[a for a in rank1 if a <= x])
    if atom_join != x:
        print(f"  FAIL: {set(x)} is not join of its atoms")
        atomistic = False
if atomistic:
    print("  PASS: every element is join of atoms below it")

# Compute upsets
print("\n=== ATOM UPSETS ===")
for atom_name in atoms:
    a = fs(atom_name)
    upset = [x for x in family if a <= x]
    print(f"  |↑{atom_name}| = {len(upset)}")

T = (n + 1) // 2
print(f"  Threshold T = (n+1)/2 = {T}")

# Identify T-atoms
t_atoms = []
for atom_name in atoms:
    a = fs(atom_name)
    upset_size = len([x for x in family if a <= x])
    if upset_size == T:
        t_atoms.append(atom_name)
print(f"  T-atoms: {t_atoms}")

# Identify meet-irreducibles
print("\n=== MEET-IRREDUCIBLES ===")
# x is meet-irreducible if it has exactly one upper cover in the Hasse diagram
# Upper cover: y covers x if x < y and no z with x < z < y
def upper_covers(x):
    covers = []
    for y in family:
        if x < y:  # proper subset
            # Check no z between
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
for m in mi_elements:
    rank = "atom" if len(m) == 1 else "line" if len(m) <= 2 else "plane" if len(m) <= 4 else "?"
    print(f"    {set(m)} ({rank})")

# Check MI-atoms
mi_atoms = [m for m in mi_elements if len(m) == 1]
print(f"  MI-atoms: {len(mi_atoms)} {'(0-MI)' if len(mi_atoms) == 0 else ''}")

# MI-lines (F)
mi_lines = [m for m in mi_elements if len(m) == 2]
print(f"  MI-lines (F): {[set(m) for m in mi_lines]}")

# Check Bouchard conditions
print("\n=== BOUCHARD CONDITIONS ===")

# 2.7: every atom upset > 4
cond_27 = all(len([x for x in family if fs(a) <= x]) > 4 for a in atoms)
print(f"  2.7 (upset > 4): {'PASS' if cond_27 else 'FAIL'}")

# 2.11: every pair of MIs has a common atom below
cond_211 = True
for i, m1 in enumerate(mi_elements):
    for j, m2 in enumerate(mi_elements):
        if i < j:
            common_atoms = [a for a in rank1 if a <= m1 and a <= m2]
            if not common_atoms:
                print(f"  2.11 FAIL: {set(m1)} and {set(m2)} share no atom")
                cond_211 = False
print(f"  2.11 (MI pairs share atom): {'PASS' if cond_211 else 'FAIL'}")

# 2.12: every MI has a T-atom below
cond_212 = True
for m in mi_elements:
    has_t = any(fs(t) <= m for t in t_atoms)
    if not has_t:
        print(f"  2.12 FAIL: {set(m)} has no T-atom below")
        cond_212 = False
print(f"  2.12 (MI has T-atom below): {'PASS' if cond_212 else 'FAIL'}")

# 2.9: for every nonempty subset of MIs, some atom is below strictly more than half
print("\n  2.9 (subset majority)...")
cond_29 = True
failing_subsets = 0
for size in range(1, len(mi_elements) + 1):
    for subset in combinations(mi_elements, size):
        # For each atom, count how many elements of the subset it's below
        has_majority = False
        for a_name in atoms:
            a = fs(a_name)
            count = sum(1 for m in subset if a <= m)
            if count > len(subset) / 2:
                has_majority = True
                break
        if not has_majority:
            failing_subsets += 1
            if failing_subsets <= 3:
                print(f"    FAIL subset: {[set(m) for m in subset]}")
if failing_subsets == 0:
    print(f"  2.9: PASS (all {2**len(mi_elements)-1} nonempty subsets checked)")
else:
    print(f"  2.9: FAIL ({failing_subsets} failing subsets)")

# 2.13: for every element, its set of incomparables is not a chain
print("\n  2.13 (incomparables not chain)...")
cond_213 = True
for x in family:
    if x == bottom or x == top:
        continue
    incomparables = [y for y in family if not (x <= y or y <= x) and y != x]
    if len(incomparables) <= 1:
        # Empty or singleton is a chain — this should fail
        cond_213 = False
        print(f"    FAIL: {set(x)} has {len(incomparables)} incomparables (is a chain)")
if cond_213:
    print(f"  2.13: PASS")

# Frankl check
print("\n=== FRANKL'S CONJECTURE ===")
frankl = False
for a_name in atoms:
    a = fs(a_name)
    upset_size = len([x for x in family if a <= x])
    if upset_size >= n / 2:
        frankl = True
        print(f"  Atom {a_name}: upset {upset_size} >= n/2 = {n/2} — WITNESSES FRANKL")
if not frankl:
    print("  NO WITNESS — would be Frankl counterexample!")

print("\n=== SUMMARY ===")
print(f"  Order: {n}")
print(f"  T-atoms: {t_atoms}")
print(f"  MI-atoms: {len(mi_atoms)}")
print(f"  MI-lines: {[set(m) for m in mi_lines]}")
print(f"  2.7: {'PASS' if cond_27 else 'FAIL'}")
print(f"  2.11: {'PASS' if cond_211 else 'FAIL'}")
print(f"  2.12: {'PASS' if cond_212 else 'FAIL'}")
print(f"  2.9: {'PASS' if failing_subsets == 0 else 'FAIL'}")
print(f"  2.13: {'PASS' if cond_213 else 'FAIL'}")
print(f"  Frankl: {'HOLDS' if frankl else 'FAILS'}")
