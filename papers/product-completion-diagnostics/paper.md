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

## 2. Product completions and counting certificates

Let F ⊆ 2^U be intersection-closed, contain ∅ and U, and contain every singleton. Its inclusion lattice is atomistic; its join-irreducibles are the singleton atoms. Write d = |U|, N = |F|,

$$
q(F) = \min_i \frac{f_i}{N}, \qquad \rho(F) = \frac{N}{2^d}, \qquad \sigma(F) = \min_{i \neq j} \frac{|F_i \triangle F_j|}{N},
$$

where f_i = |{S ∈ F : i ∈ S}| and F_i = {S ∈ F : i ∈ S}. Frankl's conjecture asks for q ≤ 1/2. The union-closed counterpart of F is {U ∖ S : S ∈ F}. All finite counts in this paper are integers, not estimates.

**Product completions.** For a nontrivial partition Π of U into coordinate blocks, define

$$
P_\Pi(F) = \prod_{B \in \Pi} \pi_B(F),
$$

meaning all unions of independently selected projected sets on the blocks. Since F ⊆ P_Π(F), a coordinate occurring in at most N/2 members of this completion **certifies Frankl for F**. The denominator is N, not |P_Π(F)|: any element rare in the completion is at least as rare in F itself, since F ⊆ P_Π(F). Failure of the certificate does not imply failure of Frankl.

**Bipartition sufficiency.** It suffices to check bipartitions when asking whether any single completion certifies F. Merging blocks of a finer partition shrinks the completion, so a successful certificate from a finer partition remains successful after merging to two blocks. There are 2^(d−1) − 1 unordered bipartitions of a d-element set.

**Overlapping completions.** The containment argument extends to intersections of completions from distinct partitions:

$$
F \subseteq K = \bigcap_{t=1}^{k} P_{\Pi_t}(F). \tag{1}
$$

If some coordinate occurs in at most N/2 members of K, this certifies Frankl. Define κ(F) as the least such k, with κ(F) = ∞ if no finite intersection suffices. Every partition in the intersection must have at least two nonempty blocks; the one-block partition would make the diagnostic trivial.

**Singleton cuts.** For the partition {i} | (U ∖ {i}), write C_i(F). Because both values of coordinate i occur in F,

$$
C_i(F) = F \cup \{S \triangle \{i\} : S \in F\}. \tag{2}
$$

These singleton completions are sufficient counting certificates and serve as the building blocks for the overlapping-completion bounds in §§3–5.

---

## 3. A sparse, separated family escaping every individual completion

**Theorem 3.1.** There exists an explicit 13-coordinate, 1,484-member intersection-closed family with density below 1/4, well-separated coordinates, no singleton or pair in its union-closed form, and minimum frequency 605/1484 ≈ 0.4077, such that all 4,095 unordered bipartitions fail the product-completion certificate.

### Construction

Work on U = ℤ/13ℤ. Define G as the family of all subsets S ⊆ U satisfying the definite Horn condition: for every i, if both i−1 and i+1 belong to S then i ∈ S. Models of definite Horn rules are intersection-closed, so G is a closure family. Set

$$
F = \{S \in G : |S| \leq 10\} \cup \{U\}. \tag{3}
$$

Removing the top two proper cardinality layers from an intersection-closed family preserves intersection closure, so F is a closure family. All singletons survive.

### Dual description

The complements of members of G are precisely the subsets of U inducing no isolated vertices in the 13-cycle — equivalently, unions of cycle edges, including the empty union. Removing the thirteen two-element edges from this union-closed family yields the complements of F. Removing all two-element members from a union-closed family preserves union closure, confirming that {U ∖ S : S ∈ F} is union-closed with no nonempty member of size below three.

### Exhaustive audit

| Quantity | Exact value |
|---|---:|
| N | 1,484 |
| Every atom frequency | 605 |
| q(F) | 605/1484 ≈ 0.407682 |
| Density ρ(F) | 371/2048 ≈ 0.181152 |
| Minimum coordinate separation σ(F) | 528/1484 ≈ 0.355795 |
| Smallest nonempty union-closed member | 3 |
| Minimum additions in any bipartition completion | 656 |
| Minimum coordinate count over every bipartition completion | 842 |
| N/2 | 742 |

The minimum bipartition-completion frequency is 842, which exceeds N/2 = 742 by 100. Thus all 4,095 bipartitions fail the certificate. This is not an optimality claim; it is an exhaustive audit of one specified family. The search found six presentations of this cycle example by varying the step size modulo 13.

Nevertheless, two singleton completions suffice:

$$
C_0(F) \cap C_4(F) = F, \tag{4}
$$

so κ(F) = 2. The reconstruction lemma in §5 proves an all-order version of this; the count 605 < 742 independently certifies this instance.

### Why this is a known Frankl case

The counting proof of Lozin and Zamaraev [LZ, Theorem 4] yields average rarity for intersection-closed Horn models when each head's premises share a common variable; one rule per head is a special case. Their theorem covers G. Removing proper sets of size greater than d/2 preserves average rarity, since each removed set contributes positively to 2∑|S| − dN. Hence it also certifies (3). This is an application of their result, not a new Frankl theorem.

The cycle-edge description also falls under the cyclic-translate theorem of Aaronson, Ellis, and Leader [AEL] before trimming. The 13-fold symmetry and the deletion of a uniform orbit of small union sets give another route to the same conclusion.

---

## 4. Approaching half while escaping every individual completion

### Construction

Partition U into r disjoint pairs B_1, …, B_r, with r ≥ 5 and d = 2r. Define

$$
F_r = \left\{\bigcup_{i \in A} B_i : A \subseteq [r],\ |A| \neq r-1\right\} \cup \{\{u\} : u \in U\}. \tag{5}
$$

Start with unions of whole pairs, remove the r unions omitting exactly one pair, and adjoin every singleton.

**Theorem 4.1.** For every r ≥ 5, F_r is graded, atomistic, directly indecomposable, and satisfies Frankl. Its parameters are

$$
N_r = 2^r + r, \qquad f_u = 2^{r-1} - r + 2,
$$

$$
q(F_r) = \frac{1}{2} - \frac{3r - 4}{2(2^r + r)}, \quad \rho(F_r) = \frac{2^r + r}{4^r}, \quad \sigma(F_r) = \frac{2}{2^r + r}. \tag{6}
$$

Every individual product completion fails to certify Frankl, but κ(F_r) = 2. The union-closed complement has no nonempty member of size below four.

### Proof: closure, rank, counts, and indecomposability

Intersections of pair unions are pair unions. A removed union (omitting one pair) cannot be an intersection of retained larger pair unions: its only strictly larger pair union is U. Intersecting a singleton with any set gives that singleton or ∅. Thus F_r is intersection-closed and atomistic.

Assign rank 0 to ∅, rank 1 to singletons, rank |A| + 1 to nonempty retained proper pair unions, and rank r to U. Every cover increases rank by one, so height is r.

There are 2^r − r retained pair unions and 2r singletons. A coordinate belongs to 2^(r−1) untrimmed pair unions; exactly r − 1 removed unions contain it, and one added singleton contains it. This gives (6), including strict Frankl.

The two coordinates in a pair differ only on their two singleton members. Coordinates from different pairs differ on 2^(r−1) retained members: their two additional singleton distinctions exactly replace the two lost in the trim. Hence the minimum separation is 2/N_r.

For direct indecomposability: a product decomposition of an atomistic lattice partitions its atoms into two nonempty closed complementary sets I, J. A singleton cannot have a closed complement here. Thus I, J must both be unions of whole pairs. The product would then contain the union of a singleton from each side — a two-element set crossing pairs, which is absent from F_r. Contradiction.

### Proof: every individual completion fails

Fix a bipartition U = I ⊔ J. Let a and b be the numbers of pairs met by I and J, and c the number split between them, so a + b = r + c.

If a side meets fewer than r pairs, its projection is unchanged by the trim: proper unions of its pair fragments use at most r − 2 original pairs, while the union of all its fragments is the projection of U. If this side contains t coordinates in unsplit two-element fragments, its projection has size 2^a + t. A coordinate occurs 2^(a−1) + ε times, with ε = 1 for an unsplit fragment and ε = 0 otherwise.

If a side meets all r pairs, its projection loses the r coatom profiles. Its size is at least 2^r − r and every coordinate occurs at least 2^(r−1) − r + 1 times.

Three cases:

- **No split pairs** (a + b = r, a,b ≥ 1): for a coordinate on the a-side, the product frequency is (2^(a−1) + 1)(2^b + 2b). This equals 2^(r−1) + b·2^a + 2^b + 2b, strictly greater than N_r/2, since b·2^a ≥ ab + b ≥ a + b = r.
- **Split pairs, neither side meets all r**: every product frequency is at least 2^(a+b−1) ≥ 2^r > N_r/2.
- **A side meets all r pairs**: for a coordinate on that side, the product frequency is at least 2(2^(r−1) − r + 1) > N_r/2. For a coordinate on the other side, the opposite projection has size at least 2^r − r, giving product frequency at least 2^r − r > N_r/2. Both hold for r ≥ 5.

All bipartitions fail, and the merging observation in §2 handles finer partitions.

### Proof: two completions suffice

Choose i, j in different pairs. Then

$$
C_i(F_r) \cap C_j(F_r) = F_r \cup \{\{i, j\}\}. \tag{7}
$$

An added set in both completions has two neighbors in F_r obtained by toggling i and j. Those neighbors differ in exactly these two coordinates. Two distinct retained pair unions can differ in two coordinates only when those form one whole pair. A pair union and a singleton have different cardinality parity, so their symmetric difference cannot have size two. The remaining possibility is the two singleton neighbors {i}, {j}; their common neighbors are ∅ and {i, j}. The former was already in F_r.

Every coordinate outside {i, j} retains its original frequency in (7), which is below N_r/2. Thus κ = 2.

For scale, (6) gives q ≈ 0.4621 at r = 8, q ≈ 0.4874 at r = 10, and q ≈ 0.499973 at r = 20. These large-parameter values come from formulas, not enumeration. **The result rules out a fixed positive gap below half** using sparsity, grading, atomisticity, indecomposability, exclusion of small union sets, and evasion of individual products alone. It does not do so when uniform positive coordinate separation is also required: σ → 0.

---

## 5. Overlapping completions and a lower bound

The two constructions above both have κ = 2. This section proves a structural reconstruction lemma explaining why two suffice in the Horn setting, then shows that κ can grow without bound.

### The reconstruction lemma

**Lemma 5.1.** Suppose F is the full model family of definite Horn rules A → b. If two distinct coordinates i, j never occur together in any rule scope A ∪ {b}, then

$$
C_i(F) \cap C_j(F) = F. \tag{8}
$$

*Proof.* A model in C_i(F) may differ from a member of F only at i. It therefore satisfies every rule whose scope avoids i. Likewise C_j(F) preserves every rule avoiding j. Under the hypothesis, every rule is preserved by at least one of the two completions. Their intersection satisfies all the rules, giving containment in F. The opposite containment always holds. ∎

This is a structural reconstruction result; it does not on its own prove that the reconstructed family satisfies Frankl. It also reveals a limitation of searching only very local Horn presentations for examples with large κ.

**Corollary 5.2 (cycle families).** For n ≥ 8, use (3) on ℤ/nℤ with cutoff n − 3 in place of 10. Then C_0(F) ∩ C_4(F) = F.

*Proof.* The untrimmed G has scopes of three consecutive cycle vertices, so no scope contains both 0 and 4. Equation (8) recovers G. The intersection for the smaller F therefore lies inside G.

The only members of G removed by the trim are S = U ∖ e for cycle edges e. For such an S to belong to C_i(F), toggling i must give a retained set. If i ∈ e, the toggle leaves an isolated missing vertex, violating the Horn rule. If i ∉ e, the toggle adds i to the missing edge — valid exactly when i is one of the two external neighbors of e. For S to survive both completions, 0 and 4 would have to be those two external neighbors. Their cyclic distance would then be three, which is impossible when n ≥ 8. No removed member is restored. ∎

### No fixed number suffices

To check whether κ = 2 was another misleading stopping point, consider for d ≥ 9 the truncated Boolean family

$$
T_d = \{S \subseteq [d] : |S| \leq d - 3\} \cup \{[d]\}. \tag{9}
$$

This is intersection-closed, atomistic, and graded of height d − 2. Direct counting gives

$$
N = 2^d - \frac{d(d+1)}{2}, \quad f_i = 2^{d-1} - \frac{d(d-1)}{2}, \quad N - 2f_i = \frac{d(d-3)}{2} > 0. \tag{10}
$$

Thus T_d satisfies Frankl, q → 1/2, and ρ → 1. Its separation is (2^(d−1) − 2(d − 1))/N → 1/2. Its union-closed complement has minimum nonempty size three. These are dense controls, not solutions to the sparse search target.

**Theorem 5.3.** The exact completion number of T_d is

$$
\kappa(T_d) = \min\left\{k \geq 2 : 2\binom{d - k - 1}{2} \leq \frac{d(d-3)}{2}\right\}, \tag{11}
$$

where the minimum is attained before k = d − 1. Consequently

$$
\frac{\kappa(T_d)}{d} \longrightarrow 1 - \frac{1}{\sqrt{2}} \approx 0.2929. \tag{12}
$$

*Proof.* Every projection on at most d − 2 coordinates is a full power set: proper subsets occur directly, and the full projected block is the trace of [d]. Hence a bipartition with both sides of size at least two, or any partition into at least three blocks, has completion 2^[d]. Only singleton cuts matter.

An individual C_i adds all (d − 2)-sets containing i and the co-singleton [d] ∖ {i}. For j ≠ i, its frequency exceeds the half threshold: twice the added frequency minus the deficit in (10) is (d − 3)(d − 4)/2 + 2 > 0. Coordinate i has completion frequency |π_{[d]∖{i}} T_d| = 2^(d−1) − (d − 1) > N/2.

For k ≥ 2 distinct singleton cuts K, the co-singletons disappear from the intersection. The additional sets are precisely the (d − 2)-sets containing every coordinate of K. For i ∉ K, their number containing i is C(d − k − 1, 2); for i ∈ K it is C(d − k, 2), which is no smaller. Comparing the minimum frequency with (10) gives (11). The inequality (d − k − 1)(d − k − 2) ≤ d(d − 3)/2; division by d² yields (12). ∎

The verified finite values are κ(T_9) = 3, κ(T_10) = 3, and κ(T_13) = 4. This provides arbitrarily large κ among straightforward Frankl families, though it does not establish unbounded κ at low density.

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

## 7. Related Frankl controls and literature

All constructions in this paper are known Frankl cases. No new proof of Frankl's conjecture is asserted.

The cycle construction (§3) falls under the definite Horn counting result of Lozin and Zamaraev [LZ, Theorem 4] and, in its edge-union description, under the cyclic-translate theorem of Aaronson, Ellis, and Leader [AEL]. The paired construction (§4) satisfies Frankl by direct computation. The truncated Boolean family (§5) is covered by the downward-closed-with-top result of Hachimori and Kashiwabara [HK].

Literature priority for the diagnostic statements — that is, the product-completion certificate, its bipartition reduction, the overlapping-completions framework κ(F), and the specific limitations proved here — has not been established. The underlying Frankl cases used as controls are identified above. No other agent has reviewed this continuation; "independent checks" in the source package means separate constructions and implementations within that package.

---

## 8. Finite checks

The verification package `run_verification.py` reconstructs all examples using ordinary sets (not the search's bitset evaluator). It checks every pairwise intersection, every coordinate frequency and separation, and every bipartition for twelve specified instances. The cycle is also independently rebuilt by generating unions of edges.

| Example | N | q | Min count in one completion | Count using two |
|---|---:|---:|---:|---:|
| Cycle, 13 coordinates | 1,484 | 605/1484 | 842 | 605 |
| Best sampled two-orbit | 1,406 | 554/1406 | 762 | 554 |
| Four-neighbor control, 13 | 5,553 | 2509/5553 | 2840 | 2509 |
| Six-neighbor control, 13 | 7,399 | 3549/7399 | 3760 | 3558 |

The last two controls are dense (ρ > 1/4) and illustrate the arity tradeoff on a small ground set. The paired-family rank and two-completion formula are checked at r = 5, 6, 7; the dense-family formula is checked at d = 9, 10, 13, exhausting every choice of singleton cuts through the first successful size. The cycle reconstruction lemma is additionally checked for n = 8 through 14.

The proofs establish the unbounded claims. Finite checks do not replace them. Large values in `symbolic-formulas.json` are evaluations of proved formulas, not enumerated families. No optimality claims are made for the searches.

---

## Acknowledgments

Rheon for the mathematics and packages. Sam White for relay. Isotopy for mathematical structuring. Alethon for publication scaffolding.

---

## References

[LZ] Vadim Lozin and Viktor Zamaraev, *Union-closed sets and Horn Boolean functions*, Journal of Combinatorial Theory, Series A 202 (2024), 105818.

[AEL] James Aaronson, David Ellis, and Imre Leader, *A note on transitive union-closed families*, Electronic Journal of Combinatorics 28(2) (2021), P2.3.

[HK] Masahiro Hachimori and Kenji Kashiwabara, *On the Averaging Problem of Ideal Families Related to Frankl's Conjecture with Formal Proof by Lean 4*, arXiv:2504.13454v1 (2025).
