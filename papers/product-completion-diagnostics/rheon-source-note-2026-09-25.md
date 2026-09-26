# Beyond one product completion: constructions and exact limitations

**Rheon · research continuation for Sam White · 25 September 2026**

## What this pass established

No Frankl counterexample was found. This work concerns the strength of our
search diagnostics, not Bouchard's fifteen conditions or a revision to 035.

1. An explicit 13-coordinate, 1,484-member family meets the previous search
   restrictions: density below 1/4, well-separated coordinates, no singleton
   or pair in its union-closed form, and failure of **every individual product
   completion certificate**. Its smallest frequency is 605/1484 ≈ 0.407682.
2. There is an infinite family of **graded, atomistic, directly indecomposable**
   lattices with density tending to zero and smallest frequency tending to
   1/2 from below, for which every individual product completion fails. The
   union-closed families have no nonempty sets smaller than four. The weakness
   is explicit: coordinates come in pairs with almost identical columns.
3. Intersecting two product completions certifies both constructions. A simple
   reconstruction lemma explains why overlapping projections can recover
   information that any one partition loses.
4. Two completions are not a universal endpoint. For a dense truncated Boolean
   family, the minimum number required is asymptotic to
   (1−1/√2)d. Its coordinate separation and minimum frequency both approach 1/2.

These are proved limitations of particular sufficient certificates, with
finite checks supplied separately. Literature priority for these diagnostic
statements has not been established. The underlying Frankl cases used as
controls include known classes, identified below. No other agent has reviewed
this continuation yet; “independent checks” means separate constructions and
implementations in this package.

## 1. Conventions and certificates

Let F⊆2^U be intersection-closed, contain ∅ and U, and contain every singleton.
Its inclusion lattice is atomistic; its join-irreducibles are the singleton
atoms. Write d=|U|, N=|F|, f_i=|{S∈F:i∈S}|, and

\[
q(F)=\min_i f_i/N,\qquad
\rho(F)=N/2^d,\qquad
\sigma(F)=\min_{i\ne j}|F_i\mathbin\triangle F_j|/N.
\]

Frankl asks for q≤1/2. The union-closed counterpart is {U∖S:S∈F}.
Height counts edges. All finite counts below are integers, not estimates.

For a nontrivial partition Π of U into coordinate blocks, put

\[
P_\Pi(F)=\prod_{B\in\Pi}\pi_B(F).
\]

This means all unions of independently selected projected sets on the blocks.
Since F⊆P_Π(F), a coordinate occurring in at most N/2 members of this
completion certifies Frankl for F. **The denominator is N, not |P_Π(F)|.**
Failure of this sufficient certificate does not imply failure of Frankl.

It suffices to check bipartitions when asking whether any one completion
certifies F. Merging blocks shrinks a completion. Thus a successful certificate
from a finer partition would remain successful after merging to two blocks.
There are 2^(d−1)−1 unordered bipartitions.

The same containment argument allows overlapping completions:

\[
F\subseteq K=\bigcap_{t=1}^kP_{\Pi_t}(F).
\tag{1}
\]

If some coordinate occurs in at most N/2 members of K, this also certifies
Frankl. Define κ(F) as the least such k, and set κ(F)=∞ if none exists. In this
note every completion must come from a partition with at least two nonempty
blocks: allowing the one-block partition would make the diagnostic trivial.

For the singleton cut {i}|(U∖{i}), use the notation C_i(F). Because both values
of coordinate i occur in F,

\[
C_i(F)=F\cup\{S\mathbin\triangle\{i\}:S\in F\}.
\tag{2}
\]

These are sufficient counting certificates and useful benchmarks. No general
computational speedup, new proof of Frankl, or fixed bound on κ is asserted.

## 2. A sparse, separated example escaping every individual completion

Work on U=Z/13Z. Define

\[
G=\{S\subseteq U:\{i-1,i+1\}\subseteq S\Rightarrow i\in S
\text{ for every }i\}.
\]

Then set

\[
F=\{S\in G:|S|\le10\}\cup\{U\}.
\tag{3}
\]

Definite Horn models are intersection-closed. Removing the top two proper
cardinality layers preserves intersection closure, so F is a closure family.
All singletons survive.

There is a second description, used for independent reconstruction. The
complements of members of G are precisely the subsets inducing no isolated
vertices in the 13-cycle: equivalently, unions of cycle edges, including the
empty union. Remove the thirteen two-element edges from this union-closed
family to obtain the complements of F. Removing all its two-element members
preserves union closure.

The exhaustive finite audit gives:

| Quantity | Exact value |
|---|---:|
| N | 1,484 |
| Every atom frequency | 605 |
| q | 605/1484 ≈ 0.407682 |
| Density | 371/2048 ≈ 0.181152 |
| Minimum coordinate separation | 528/1484 ≈ 0.355795 |
| Smallest nonempty union-closed member | 3 |
| Minimum additions in any bipartition completion | 656 |
| Minimum coordinate count over every bipartition completion | 842 |
| Half of the original family size | 742 |

Thus all 4,095 bipartitions fail the certificate: even the smallest completion
frequency is 100 above the required threshold. This is not a census or an
optimality claim among arbitrary families; it is an exhaustive audit of one
specified family. The search found six presentations of this cycle example
by changing the step size modulo 13.

Nevertheless,

\[
C_0(F)\cap C_4(F)=F.
\tag{4}
\]

In particular κ(F)=2. The next section proves an all-order version of the
reconstruction statement; the count 605 independently certifies this instance.

### Why this is a known Frankl case

The counting proof of Lozin and Zamaraev's Theorem 4 yields average rarity
for the intersection-closed models when each head's Horn premises have a common variable; one rule per
head is a special case. Their paper uses a Horn DNF for the *invalid* points,
the opposite Boolean truth convention from this package's model evaluator.
It covers G. Removing proper sets of size greater than d/2 preserves average
rarity: each removed set contributes positively to
2∑|S|−d|G|. Hence it also certifies (3). This is an application of their result,
not a new Frankl theorem. See [Lozin–Zamaraev, 2024, Theorem 4][LZ].

The cycle-edge construction also falls under the cyclic-translate theorem of
[Aaronson–Ellis–Leader, 2021][AEL] before trimming. Its symmetry and deletion
of a uniform orbit of small union sets give another explanation of the trim.

## 3. What two overlapping completions recover

**Reconstruction lemma.** Suppose F is the full model family of definite Horn
rules A→b. If two distinct coordinates i,j never occur together in any rule
scope A∪{b}, then

\[
C_i(F)\cap C_j(F)=F.
\tag{5}
\]

**Proof.** A model in C_i(F) may differ from a member of F only at i. It
therefore satisfies every rule whose scope avoids i. Likewise C_j(F)
preserves every rule avoiding j. Under the hypothesis every rule is preserved
by at least one of the two completions. Their intersection satisfies all the
rules, giving containment in F. The opposite containment always holds. ∎

This is a structural reconstruction result; it does not on its own prove
that the reconstructed family satisfies Frankl. It also explains a limitation
of searching only very local Horn presentations for examples with large κ.

**Cycle corollary.** For n≥8, use (3) on Z/nZ, with the cutoff n−3 in place
of 10. Then C_0(F)∩C_4(F)=F.

**Proof.** First consider the untrimmed G. Its scopes are three consecutive
cycle vertices, so no scope contains both 0 and 4. Equation (5) recovers G.
Consequently the intersection for the smaller F lies inside G.

The only members of G removed by the trim are S=U∖e for cycle edges e; a
co-singleton is already forbidden. For such an S to belong to C_i(F), toggling
i must give a retained set. If i∈e, the toggle leaves an isolated missing
vertex and fails the Horn rule. If i∉e, the toggle adds i to the missing edge:
this is valid exactly when i is one of the two external neighbors of e.
For S to survive both completions, 0 and 4 would have to be those two external
neighbors. Their cyclic distance would then be three, impossible when n≥8.
No removed member is restored, proving the claim. ∎

## 4. An infinite sparse near-half family with κ=2

Partition U into r disjoint pairs B_1,…,B_r, with r≥5 and d=2r. Define

\[
F_r=\left\{\bigcup_{i\in A}B_i:A\subseteq[r],\ |A|\ne r-1\right\}
\ \cup\ \{\{u\}:u\in U\}.
\tag{6}
\]

Thus start with unions of whole pairs, remove the r unions omitting exactly
one pair, and add every singleton.

**Theorem.** For every r≥5, F_r is graded, atomistic, directly indecomposable,
and satisfies Frankl. Its parameters are

\[
N_r=2^r+r,\qquad f_u=2^{r-1}-r+2,
\]

\[
q(F_r)=\frac12-\frac{3r-4}{2(2^r+r)},\quad
\rho(F_r)=\frac{2^r+r}{4^r},\quad
\sigma(F_r)=\frac2{2^r+r}.
\tag{7}
\]

Every individual product completion fails to certify Frankl, but κ(F_r)=2.
Its union-closed complement has no nonempty member of size below four.

### Closure, rank, counts, and indecomposability

Intersections of pair unions are pair unions. A removed union omitting one
pair cannot be an intersection of retained larger pair unions: its only
strictly larger pair union is U. Intersecting a singleton with anything gives
that singleton or ∅. Thus F_r is intersection-closed and atomistic.

Assign rank 0 to ∅, rank 1 to singletons, rank |A|+1 to nonempty retained proper
pair unions, and rank r to U. Every cover increases rank by one, so height is r.

There are 2^r−r pair unions and 2r extra singletons. A coordinate belongs to
2^(r−1) untrimmed pair unions; exactly r−1 removed unions contain it, and one
added singleton contains it. This gives (7), including strict Frankl.

The two coordinates in a pair differ only on their two singleton members.
Coordinates from different pairs differ on 2^(r−1) retained members: their
two additional singleton distinctions exactly replace the two distinctions
lost in the trim. Hence the minimum separation is 2/N_r.

For direct indecomposability, a product decomposition of an atomistic lattice
partitions its atoms into two nonempty closed complementary sets I,J.
A singleton cannot have a closed complement here. Thus I,J must both be
unions of whole pairs. The product would contain the union of a singleton
from each side, a two-element set crossing pairs, which is absent from F_r.
This contradiction excludes a nontrivial product.

### Why every individual completion fails

Fix a bipartition U=I⊔J. Let a and b be the numbers of pairs met by I and J,
and c the number split between them. Then a+b=r+c.

If a side meets fewer than r pairs, its projection is unchanged by the trim:
proper unions of its pair fragments use at most r−2 original pairs, while
the union of all its fragments is the projection of U. If this side contains
t coordinates in unsplit two-element fragments, its projection has size
2^a+t. A coordinate occurs 2^(a−1)+ε times there, with ε=1 for an unsplit
fragment and ε=0 for a one-element fragment.

If a side meets all r pairs, its projection loses the r coatom profiles. Its
size is at least 2^r−r and every coordinate occurs at least
2^(r−1)−r+1 times. The singletons do not reduce these bounds.

These observations give three cases.

* **No split pairs:** a+b=r, a,b≥1. For a coordinate on the a-side its product
  frequency is (2^(a−1)+1)(2^b+2b). This equals
  2^(r−1)+b2^a+2^b+2b, strictly greater than N_r/2. Indeed
  b2^a≥ab+b≥a+b=r. The other side is symmetric.
* **Split pairs, neither side meets all r:** every product frequency is at
  least 2^(a+b−1)≥2^r>N_r/2.
* **A side meets all r:** for a coordinate on such a side the product
  frequency is at least 2(2^(r−1)−r+1)>N_r/2. For a coordinate on a side
  meeting fewer pairs, its opposite projection has size at least 2^r−r,
  so its product frequency is at least 2^r−r>N_r/2. Both inequalities hold
  for r≥5. This also covers the case where both sides meet all pairs.

All bipartitions fail, and the merging observation in §1 covers finer
partitions as well.

### Why two suffice

Choose i,j in different pairs. Then

\[
C_i(F_r)\cap C_j(F_r)=F_r\cup\{\{i,j\}\}.
\tag{8}
\]

To see this, an added set in both completions has two neighbors in F_r,
obtained by toggling i and j. Those neighbors differ in exactly these two
coordinates. Two distinct retained pair unions can differ in two coordinates
only when those coordinates form one whole pair. A pair union and a singleton
have different parity of cardinality, so their symmetric difference cannot
have size two. The remaining possibility is the two singleton neighbors
{i},{j}; their common neighbors are ∅ and {i,j}. The former was already in F_r.

Every coordinate outside {i,j} retains its original frequency in (8), which
is below N_r/2. Thus κ=2.

For scale, (7) gives q≈0.4621 at r=8, q≈0.4874 at r=10, and
q≈0.499973 at r=20. These large-parameter values come from formulas, not
enumeration. The result rules out a fixed positive gap below half using
sparsity, grading, atomisticity, indecomposability, exclusion of small union
sets, and evasion of individual products alone. **It does not do so when
uniform positive coordinate separation is also required:** σ tends to zero.

## 5. No fixed number of completions suffices in general

To check whether κ=2 was another misleading stopping point, consider for d≥9

\[
T_d=\{S\subseteq[d]:|S|\le d-3\}\cup\{[d]\}.
\tag{9}
\]

This familiar truncated Boolean family is intersection-closed, atomistic,
and graded of height d−2. Direct counting gives

\[
N=2^d-\frac{d(d+1)}2,\quad
f_i=2^{d-1}-\frac{d(d-1)}2,\quad
N-2f_i=\frac{d(d-3)}2>0.
\tag{10}
\]

Thus it satisfies Frankl, q→1/2, and ρ→1. Its separation is
(2^(d−1)−2(d−1))/N→1/2. Its union-closed complement has minimum nonempty
size three. These are dense controls, not solutions to the sparse target.

**Theorem.** Its exact completion number is

\[
\kappa(T_d)=\min\left\{k\ge2:
2\binom{d-k-1}{2}\le\frac{d(d-3)}2\right\},
\tag{11}
\]

where the minimum is attained before k=d−1. Consequently

\[
\frac{\kappa(T_d)}d\longrightarrow1-\frac1{\sqrt2}.
\tag{12}
\]

**Proof.** Every projection on at most d−2 coordinates is a full power set:
proper subsets occur directly, and the full projected block is the trace of
[d]. Hence a bipartition with both sides of size at least two, or any partition
into at least three blocks, has completion 2^[d]. Only singleton cuts matter.

An individual C_i adds all (d−2)-sets containing i and the co-singleton
[d]∖{i}. For j≠i its frequency exceeds the half threshold, since twice the
added frequency minus the deficit in (10) is
(d−3)(d−4)/2+2>0. Coordinate i has completion frequency
|π_[d]∖{i} T_d|=2^(d−1)−(d−1)>N/2.

For k≥2 distinct singleton cuts K, the co-singletons disappear from the
intersection. The additional sets are precisely the (d−2)-sets containing
every coordinate of K. For i∉K, their number containing i is
binom(d−k−1,2); for i∈K it is binom(d−k,2), which is no smaller. Comparing
the minimum frequency with (10) proves (11). The inequality is
(d−k−1)(d−k−2)≤d(d−3)/2; division by d² yields (12). ∎

The verified finite values are κ(T_9)=3, κ(T_10)=3, and κ(T_13)=4.
This provides arbitrarily large κ among straightforward Frankl families.
It does not establish unbounded κ at low density. The broader class of
downward-closed families with an added top is also covered by the average
rarity result of [Hachimori–Kashiwabara, 2025][HK].

## 6. Searches and verification boundaries

The one-orbit scan considers, on 13 coordinates, all head-zero premises of
sizes 2 through 6, then all thirteen cyclic translates of each rule. It uses
the trim in (3), N≤2048, and tests individual singleton completions first.
There are 2,497 such templates. Exactly six pass that initial completion
test under the size cap; all are cycle presentations. All bipartitions were
then tested for each saved example. This is complete only within that
specified one-orbit presentation scan.

A separate seeded run proposes 12,000 pairs of disjoint head-zero premises,
giving 10,661 distinct unordered template pairs. Premise sizes are sampled
from {2,3,4}, with the weighting specified in the script. Under the size cap,
52-member lower cutoff, separation ≥1/10, and singleton-completion evasion,
139 template pairs pass. These are not counts of distinct families or
isomorphism classes. Only the top three were audited over all bipartitions;
all three pass that test and all three are certified by two completions.

Their displayed two-rule-per-head presentations have empty common premises,
so the sufficient dependency test discussed in §2 does not apply directly
to those presentations. This is **not** a claim that no alternative Horn
presentation or other known Frankl theorem covers the resulting families.

| Example | N | q | Minimum count in one completion | Count sufficient using two |
|---|---:|---:|---:|---:|
| Cycle, 13 coordinates | 1,484 | 605/1484 | 842 | 605 |
| Best sampled two-orbit example | 1,406 | 554/1406 | 762 | 554 |
| Four-neighbor control, 13 coordinates | 5,553 | 2509/5553 | 2840 | 2509 |
| Six-neighbor control, 13 coordinates | 7,399 | 3549/7399 | 3760 | 3558 |

The last two controls are dense; they do not meet the 1/4 density cap. They
illustrate the tradeoff in increasing rule arity on this small ground set.
The second column of frequencies for two completions need not equal the
original minimum: containment only requires a bound below N/2.

`run_verification.py` reconstructs all examples using ordinary sets rather
than the search's bitset rule evaluator. It checks every pairwise intersection,
every coordinate frequency and separation, and every bipartition for twelve
specified instances. The cycle is also rebuilt by generating unions of edges.
The paired-family rank and two-completion formula are checked at r=5,6,7;
the dense-family formula is checked at d=9,10,13, exhausting every choice of
singleton cuts through the first successful size. The cycle reconstruction
lemma is additionally checked for n=8 through 14.

The proofs establish the unbounded claims. Finite checks do not replace them.
Large values in `symbolic-formulas.json` are evaluations of proved formulas,
not enumerated families. No optimality claims are made for the searches.

## 7. Where to continue

The useful target is now a combination that none of these controls supplies:
low density, uniformly separated coordinate columns, q close to half, and
resistance to several overlapping completions. The cycle meets the first
two but has a visible gap and κ=2. The paired construction approaches half
at low density but loses separation and has κ=2. The truncated Boolean
construction has separation, q→1/2, and κ→∞, but density tends to one.

That is an experimental target, not a new conjecture asserted as true, and
not a set of conditions sufficient for a counterexample. A productive next
step is to couple local constructions so that no small set of projection
cuts recovers all their constraints, while monitoring both the numerical gap
and known structural certificates. The new reconstruction lemma helps identify
when a proposed search presentation cannot produce the desired benchmarks.

## References

[LZ]: https://wrap.warwick.ac.uk/id/eprint/180696/1/1-s2.0-S0097316523000869-main.pdf
[AEL]: https://www.combinatorics.org/ojs/index.php/eljc/article/download/v28i2p3/pdf/
[HK]: https://arxiv.org/html/2504.13454v1

- Vadim Lozin and Viktor Zamaraev, *Union-closed sets and Horn Boolean
  functions*, Journal of Combinatorial Theory, Series A 202 (2024), 105818.
  Theorem 4 and its counting proof were inspected for this application.
- James Aaronson, David Ellis, and Imre Leader, *A note on transitive
  union-closed families*, Electronic Journal of Combinatorics 28(2) (2021), P2.3.
- Masahiro Hachimori and Kenji Kashiwabara, *On the Averaging Problem of Ideal
  Families Related to Frankl's Conjecture with Formal Proof by Lean 4*,
  arXiv:2504.13454v1 (2025). Statement and scope inspected; the external Lean
  development was not rerun.

The earlier 18 September near-half note supplies the starting diagnostic.
The new files do not alter its results or the 034–035 classification packages.
