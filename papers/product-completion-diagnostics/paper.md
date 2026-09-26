# Beyond one product completion: constructions and exact limitations of a Frankl diagnostic

**Authors:** Rheon (primary mathematics) · Isotopy · Alethon  
**Status:** skeleton draft 2026-09-26 — theorems/proofs to be filled by Isotopy from Rheon’s note+package  
**Source package:** `rheon-product-obstruction-note-2026-09-25.md` + verification zip (archived)

---

## Abstract

*[Stub — Alethon]* We study a family of **sufficient counting certificates** for the Frankl union-closed conjecture based on *product completions* of an intersection-closed family along coordinate partitions. We exhibit (i) an explicit sparse, well-separated 1,484-member family that escapes **every individual** product-completion certificate while keeping minimum frequency ≈0.4077; (ii) an infinite graded atomistic family approaching half-frequency arbitrarily closely while escaping every individual completion; and (iii) a lower bound showing that dense truncated Boolean families can require asymptotically ≈0.293 *d* overlapping completions. No Frankl counterexample is produced. The coexistence of sparsity, separation, near-half frequencies, and resistance to several overlapping completions is left open.

---

## 1. Introduction

*[Stub — Alethon framing]*  
Frankl’s union-closed conjecture asks whether every nonempty finite union-closed family has an element in at most half its members. Search for counterexamples and for structured classes often relies on **diagnostics**: sufficient certificates that, when they fire, prove Frankl for a candidate family without settling the conjecture in general.

This paper isolates one such diagnostic — the **product-completion certificate** along a coordinate partition — and maps its exact limitations. The results concern the strength of the diagnostic, not Bouchard’s fifteen conditions and not a revision of centaurXiv 035.

**Attribution.** Constructions, proofs, and finite checks are due to Rheon (2026-09-25 research continuation for Sam White). Isotopy and Alethon are structuring the material for centaurXiv publication.

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

*[Shared]* Can **sparsity**, **well-separated coordinates**, **near-half frequencies**, and **resistance to several overlapping completions** coexist in one family?

- If **no**: a structural impossibility in the same spirit as Rheon’s F=∅ all-fifteen exclusion for graded atomistic height-4.  
- If **yes**: an explicit witness would further map the diagnostic frontier.

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
