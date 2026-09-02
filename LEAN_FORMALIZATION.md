# Lean formalization plan — centaurXiv 033 & 034

**Status:** not urgent · coordination sketch for Iso / Alethon / Sam  
**Date:** 2026-09-02  
**Papers:**
- [033 — Height-three obstruction](https://centaurxiv.org/submissions/centaurxiv-2026-033/)
- [034 — Diophantine rigidity of 2.12](https://centaurxiv.org/submissions/centaurxiv-2026-034/)

**Working repos:** this public verification pack; private draft history in `frankl-search/papers/{height-boundary,fempty-212-rigidity}/`.

---

## Goal

Machine-check the **analytic** claims that are Lean-shaped. Leave full census / orbit emptiness as computational certificates unless someone wants a longer certified-enumeration sprint.

**Success bar (lean, small):** Thm 1 (033) + deficit identity (034) + concrete n=13 witness object — enough to say “Lean checked the proofs that aren’t search.”

---

## Fit summary

| Claim | Paper | Fit | Notes |
|-------|--------|-----|-------|
| Height-3 impossibility (Thm 1) | 033 | **Best** | Finite lattice + covering/upset counting + incidence. No search. |
| Deficit identity + \(R_2 \le k+s_3-1\) | 034 | **Excellent** | Short ℕ algebra on graded height-4. |
| Free-atom lemma (D=4 untouched ⇒ F=∅ fails) | 034 | **Good** | Finite case split; local to B₅. |
| n=13 Hasse specimen (lattice + 2.7 ∧ 2.12) | 033 | **Strong** | Concrete Finset/poset object; also a regression for filters. |
| “None at n=11 / odd n≤15 / B₅ orbit exact-T=0” | 033/034 | **Hard** | Certified enumeration or trust Python receipts. Formalize *feasibility bounds* first; full “we checked every config” is a separate project. |

---

## Phases

### Phase 0 — Scaffold (autonomous-friendly)

- [ ] Lake project under `lean/` (Mathlib4 pin recorded).
- [ ] Minimal lattice API we actually need (not all of Order theory):
  - finite poset / covering relation
  - upset size, length \(\ell(L)\)
  - join-/meet-irreducible
  - graded height-3 / height-4 rank profile helpers
- [ ] One smoke lemma that compiles (e.g. upset of top = 1).

**Owner guess:** Alethon can start; Iso review Mathlib idioms.

### Phase 1 — 033 Theorem 1 (highest proof value)

Formalize the paper’s proof arc:

0. From 2.7 ∧ 2.12 at \(\ell(L)=3\): odd \(n\), JI = atoms, effective graded height-3  
i–ii. Middles cover ≥2 atoms; any two middles share ≤1 atom (partial linear space)  
iii–v. 2.12 target atom; \(k\) lower bound; target lies under every middle  
vi–viii. Non-target atoms have \(r_x=1\) ⇒ \(|\uparrow x|=3\) ⇒ contradicts 2.7  

**Done when:** `theorem height3_no_joint_27_212 : …` compiles with no `sorry` on the main path.

**Owner guess:** Iso primary (proof author); Alethon dual-verify against `bouchard_filters.py` definitions.

### Phase 2 — 034 deficit identity

- [ ] State graded atomistic height-4 rank profile \((1,k,R_2,s_3,1)\).
- [ ] Prove \(|\uparrow a| = 2 + c_2(a) + c_3(a)\) under that grading.
- [ ] Prove the identity and corollary \(R_2 \le k + s_3 - 1\) for any T-atom.
- [ ] Optional: replay the k=6 numeric check as a `#eval` / example.

**Done when:** identity + corollary have no `sorry`.

**Owner guess:** Alethon (verified by integer scan historically) or Fable (identity author) if present; Iso review.

### Phase 3 — n=13 witness object

- [ ] Encode the Hasse diagram from 033 §5.2 as a finite covering relation.
- [ ] Prove: unique meets/joins (or invoke a verified lattice-check matching `test_lattice_validation.py`).
- [ ] Prove: 2.7 and 2.12 hold; record that 2.9/2.11 fail if desired.

**Done when:** `def N13 : …` + `theorem n13_joint_27_212` with no `sorry`.

**Owner guess:** Alethon (filter module) + Iso.

### Phase 4 — Enumeration claims (optional / later)

Do **not** block Phases 1–3 on this.

Options, cheapest first:

1. **Certificate style:** Lean states feasibility bounds; Python receipts remain the population evidence; Lean verifies named specimens (C₅-complement, D=4 gap-1 profiles).
2. **Verified enumerator:** encode the search as a Lean function with a proof that “all feasible configs are in this Finset” — large.

Suggested first certificate objects: C₅-complement (n=17), free-atom lemma statement for D=4.

---

## Autonomously doable vs needs human/Iso

| Autonomously (Alethon) | Needs Iso / Sam |
|------------------------|-----------------|
| Lake scaffold, API stubs, smoke lemmas | Proof strategy choices where Mathlib has multiple encodings |
| Deficit identity draft | Thm 1 style match to Iso’s writeup |
| n=13 encoding + filter checks | Merge/review of PRs; Mathlib version pin policy |
| Mapping Lean defs ↔ `bouchard_filters.py` | Deciding Phase 4 depth |

Sam: facilitation / board-side “we have a Lean check in progress” if useful — not blocking.

---

## Definition alignment (load-bearing)

Lean predicates must match the **executable** filters in `bouchard_filters.py`, not a soft paraphrase:

- **2.7:** \(\forall j\in J(L),\ |\uparrow j| > \ell(L)\)
- **2.12:** \(\forall m\in M(L),\ \exists j\le m,\ 2|\uparrow j| = n+1\) (integer form)
- Upsets include the element itself (as in the papers’ appendices)

Open a short `lean/DEFINITIONS.md` once Phase 0 lands, with side-by-side Python ↔ Lean.

---

## Out of scope (this plan)

- Proving Frankl / full Bouchard survivor existence
- Replacing the Python census
- Formalizing retracted dBE claims
- Paper thrash / reopening 033–034 text unless a Lean gap forces an erratum

---

## First concrete next step

When someone picks this up (Sam free tomorrow / Iso when awake):

1. Create `lean/` Lake + Mathlib pin.  
2. File an issue or branch `lean-phase0-scaffold`.  
3. Alethon: smoke compile + DEFINITIONS stub.  
4. Iso: sanity-check encoding of height-3 / JI before Thm 1 attempt.

Not urgent. Coordination file only until then.

— Alethon (draft for Iso/Sam), 2026-09-02
