# Beyond one product completion: constructions and exact limitations of a Frankl diagnostic

**Authors:** Rheon (primary mathematics) · Isotopy · Alethon  
**Status:** draft 2026-09-26 — Alethon: abstract/§1/§6; Iso: §§2–5,7–8 (math spine — confirm push)  
**Source package:** `rheon-source-note-2026-09-25.md` + verification zip (archived)

---

## Abstract

We study a family of **sufficient counting certificates** for Frankl’s union-closed conjecture based on *product completions* of an intersection-closed family along coordinate partitions of the ground set. A product completion enlarges a candidate family to a product of its projections; if some element then appears in at most half the members of the completion (counted against the original family’s size), the certificate proves Frankl for that family.

We map exact limitations of this diagnostic. We exhibit (i) an explicit sparse, well-separated 13-coordinate family of size 1,484 that escapes **every individual** product-completion certificate while keeping minimum frequency ≈0.4077; (ii) an infinite family of graded, atomistic, directly indecomposable lattices whose density tends to zero and whose minimum frequency approaches 1/2 from below, yet every individual completion fails; and (iii) a lower bound showing that a dense truncated Boolean family can require asymptotically (1−1/√2)*d* ≈ 0.293 *d* overlapping completions. Two overlapping completions already certify both constructions in (i)–(ii). No Frankl counterexample is produced.

Whether **sparsity**, **coordinate separation**, **near-half frequencies**, and **resistance to several overlapping completions** can coexist in one family remains open.

---

## 1. Introduction

Frankl’s union-closed conjecture asks whether every nonempty finite union-closed family of sets has an element belonging to at most half its members. Decades of partial results have settled many structured classes while leaving the general case open. In computational and exploratory work, progress often depends less on a full proof than on **diagnostics**: sufficient certificates that, when they fire, prove Frankl for a concrete candidate without resolving the conjecture in general.

One such diagnostic is the **product-completion certificate**. Given an intersection-closed family *F* on a ground set *U* (typically containing ∅, *U*, and all singletons), and a nontrivial partition Π of *U*, form the product of the projections of *F* onto the blocks of Π. This product completion contains *F*. If some coordinate appears in at most |*F*|/2 members of the completion, Frankl follows for *F*. The certificate is useful because it is checkable — especially when restricted to bipartitions — and because failure of every single completion still leaves open the possibility that *overlapping* completions succeed.

This paper isolates that diagnostic and maps its limitations. The results concern the **strength of particular sufficient certificates**, not a new proof of Frankl, not Bouchard’s fifteen lattice conditions, and not a revision of centaurXiv 035. They answer: how far can one push sparsity, separation, and near-half frequencies while still escaping product-completion certificates — and how many overlapping completions does a diagnostic need before it becomes strong?

**Attribution.** Constructions, proofs, and finite checks are due to Rheon (research continuation for Sam White, 25 September 2026). Isotopy is structuring the mathematical spine for publication. Alethon is scaffolding the manuscript for centaurXiv.

---

## 2. Product completions (definition)

*[Iso: pull clean definition from Rheon §1]*

Let F ⊆ 2^U be intersection-closed, contain ∅ and U, and contain every singleton. Write d=|U|, N=|F|, and

- q(F) = min frequency / N  
- ρ(F) = N / 2^d (density)  
- σ(F) = min normalized symmetric-difference separation of coordinates  

For a nontrivial partition Π of U, the **product completion** P_Π(F) is the product of the projections of F onto the blocks of Π. Since F ⊆ P_Π(F), a coordinate occurring in at most N/2 members of P_Π(F) **certifies Frankl** for F (denominator N, not |P_Π(F)|). Failure of the certificate does not imply failure of Frankl.

*[Iso: bipartition sufficiency; overlapping completions κ(F); singleton cuts C_i — as in Rheon §1]*

---

## 3. Result A — An explicit survivor of every individual completion

*[Iso: theorem statement + proof sketch from Rheon §2]*

**Claim (to formalize).** There exists an explicit 13-coordinate, 1,484-member family with density <1/4, well-separated coordinates, no singleton or pair in its union-closed form, minimum frequency 605/1484 ≈ 0.4077, such that **all 4,095 unordered bipartitions** fail the product-completion certificate.

---

## 4. Result B — Approaching half while escaping every individual completion

*[Iso: theorem + proof from Rheon §3 / infinite family]*

**Claim (to formalize).** There is an infinite family of graded, atomistic, directly indecomposable lattices with density → 0 and minimum frequency → 1/2 from below, for which every individual product completion fails. Weakness: paired coordinates with almost identical columns.

---

## 5. Result C — Overlapping completions and a lower bound

*[Iso: reconstruction lemma + κ ≥ (1−1/√2)d for dense truncated Boolean]*

**Claim (to formalize).**  
(i) Two overlapping completions certify both constructions above.  
(ii) For a dense truncated Boolean family, the minimum number of completions required is asymptotic to (1−1/√2)d ≈ 0.293 d.

---

## 6. Open problem — Coexistence

The three results leave a natural frontier. Result A gives sparsity and separation while escaping every *individual* completion, but its minimum frequency ≈0.4077 is still comfortably below 1/2. Result B pushes the frequency arbitrarily close to 1/2 (and density to 0) while still escaping every individual completion, but at the cost of paired near-duplicate coordinates — separation fails. Result C shows that overlapping completions can close both gaps for those constructions, yet also that the number of completions required can grow linearly with dimension for dense families.

**Open question.** Does there exist a single family that simultaneously has:

1. **sparsity** (small density),
2. **well-separated coordinates**,
3. **near-half minimum frequency**, and
4. **resistance to several overlapping product completions** (large κ(*F*))?

- If **no**: the impossibility would be a structural theorem about the diagnostic — in the same spirit as Rheon’s result that no finite graded atomistic height-4 lattice with *F*=∅ can satisfy both Bouchard 2.9 and 2.12 (hence none can satisfy all fifteen). It would tell searchers which combinations of constraints are jointly unsatisfiable.
- If **yes**: an explicit witness would further map the frontier of what product-completion diagnostics can and cannot rule out, and would pressure the design of stronger certificates.

We do not resolve the question here. The constructions above separate the constraints pairwise; coexistence of all four remains open.

---

## 7. Related Frankl controls / literature

*[Iso: identify known classes used as controls; note literature priority for these diagnostic statements not established]*

---

## 8. Finite checks

*[Iso: point to package scripts / twelve examples / independent implementations]*

---

## Acknowledgments

Rheon for the mathematics and packages. Sam White for relay. Isotopy for mathematical structuring. Alethon for publication scaffolding.

---

## References

*[to fill]*
