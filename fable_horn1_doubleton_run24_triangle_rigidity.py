# Test predictions of the proposed triangle-rigidity theorem on ALL class lattices, odd n<=15:
# For any lattice whose F (rank-2 MI atom-sets) is a triangle of doubletons and which satisfies FULL 2.11:
#   P1: s3 == 3 exactly, and every rank-3 element is the unique cover of one triangle edge
#   P2: each triangle vertex lies below exactly 2 rank-3 elements (opposite-miss)
#   P3: no such lattice satisfies 2.12  (even without assuming 2.7)
from itertools import combinations

tested=0; p1v=0; p2v=0; p3v=0; c212_hits=0
for n in (9,11,13,15):
    inner=n-2
    for k in range(3, inner-4):
        for s2 in range(3, inner-k-1):
            s3=inner-k-s2
            if s3<2: continue
            acols=[frozenset(c) for r in range(2,k+1) for c in combinations(range(k),r)]
            bcols=[frozenset(c) for r in range(2,s2+1) for c in combinations(range(s2),r)]
            for A in combinations(acols,s2):
                if any(len(A[i]&A[j])>1 for i in range(s2) for j in range(i+1,s2)): continue
                if frozenset().union(*A)!=frozenset(range(k)): continue
                for B in combinations(bcols,s3):
                    if any(len(B[i]&B[j])>1 for i in range(s3) for j in range(i+1,s3)): continue
                    if frozenset().union(*B)!=frozenset(range(s2)): continue
                    deg=[0]*s2
                    for c in B:
                        for i in c: deg[i]+=1
                    Fidx=[i for i in range(s2) if deg[i]==1]
                    F=[A[i] for i in Fidx]
                    # triangle of doubletons?
                    if len(F)!=3 or any(len(f)!=2 for f in F): continue
                    if not all(F[i]&F[j] for i in range(3) for j in range(i+1,3)): continue
                    if F[0]&F[1]&F[2]: continue
                    # build + lattice
                    atom=lambda i:1+i; r2=lambda i:1+k+i; r3=lambda i:1+k+s2+i; top=n-1
                    upcov=[[] for _ in range(n)]
                    for i in range(k): upcov[0].append(atom(i))
                    for j,c in enumerate(A):
                        for i in c: upcov[atom(i)].append(r2(j))
                    for j,c in enumerate(B):
                        for i in c: upcov[r2(i)].append(r3(j))
                    for j in range(s3): upcov[r3(j)].append(top)
                    up=[0]*n
                    for x in range(n-1,-1,-1):
                        m=1<<x
                        for y in upcov[x]: m|=up[y]
                        up[x]=m
                    dn=[0]*n
                    for x in range(n):
                        for y in range(n):
                            if (up[y]>>x)&1: dn[x]|=1<<y
                    lat=True
                    for x in range(n):
                        for y in range(x+1,n):
                            c=dn[x]&dn[y]
                            if not any(dn[z]==c for z in range(n) if (c>>z)&1): lat=False; break
                            c=up[x]&up[y]
                            if not any(up[z]==c for z in range(n) if (c>>z)&1): lat=False; break
                        if not lat: break
                    if not lat: continue
                    # full 2.11
                    c2=[sum(1 for c in A if i in c) for i in range(k)]
                    Mset=[atom(i) for i in range(k) if c2[i]==1]+[r2(i) for i in Fidx]+[r3(i) for i in range(s3)]
                    ups=lambda x: bin(up[x]).count('1')
                    c211=all(any((up[atom(a)]>>Mset[i])&1 and (up[atom(a)]>>Mset[j])&1 for a in range(k))
                             for i in range(len(Mset)) for j in range(i+1,len(Mset)))
                    if not c211: continue
                    tested+=1
                    # P1: s3==3 and every rank-3 covers exactly one triangle edge (is that edge's unique cover)
                    tau=set()
                    ok1 = (s3==3)
                    for j,c in enumerate(B):
                        covered_edges=[i for i in Fidx if i in c]
                        if len(covered_edges)!=1: ok1=False
                        else: tau.add(covered_edges[0])
                    if ok1 and tau==set(Fidx): p1v+=1
                    # P2: triangle vertices below exactly 2 rank-3
                    V=set().union(*F)
                    r3cnt={v: sum(1 for j in range(s3) if (up[atom(v)]>>r3(j))&1) for v in V}
                    if all(r3cnt[v]==2 for v in V): p2v+=1
                    # P3: 2.12
                    T=(n+1)//2
                    c212=all(any((up[atom(a)]>>m)&1 and ups(atom(a))==T for a in range(k)) for m in Mset)
                    if c212: c212_hits+=1
                    else: p3v+=1
print(f"triangle-doubleton-F lattices with FULL 2.11 (odd n<=15): {tested}")
print(f"  P1 (s3=3, rank-3 = exactly the three edge-covers): {p1v}/{tested}")
print(f"  P2 (each vertex below exactly 2 rank-3): {p2v}/{tested}")
print(f"  P3 (2.12 fails): {p3v}/{tested}   (2.12 satisfied: {c212_hits} — theorem predicts 0)")
