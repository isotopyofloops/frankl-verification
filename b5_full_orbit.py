# Complete B5 pure-deletion orbit: delP <= 5 (0-MI forces R2>=5), delT <= 6 (F=0 forces s3>=ceil(2*R2/3)>=4).
# For every D: count hunt lattices (F=0, 0-MI, 2.7, 2.11), odd-n gap stats, T-atoms (EXACT equality),
# and at D=4 analyze untouched-atom configs (which condition kills).
from itertools import combinations

pairs=[frozenset(c) for c in combinations(range(5),2)]
trips=[frozenset(c) for c in combinations(range(5),3)]

def build(P,Tt):
    k=5; s2=len(P); s3=len(Tt); n=2+k+s2+s3
    atom=lambda i:1+i; r2=lambda i:1+k+i; r3=lambda i:1+k+s2+i; top=n-1
    upcov=[[] for _ in range(n)]
    for i in range(k): upcov[0].append(atom(i))
    for j,c in enumerate(P):
        for i in c: upcov[atom(i)].append(r2(j))
    B=[]
    for j,Tset in enumerate(Tt):
        cov=[i for i,pp in enumerate(P) if pp<=Tset]
        B.append(cov)
        for i in cov: upcov[r2(i)].append(r3(j))
    for j in range(s3): upcov[r3(j)].append(top)
    if any(len(b)<2 for b in B): return None
    up=[0]*n
    for x in range(n-1,-1,-1):
        m=1<<x
        for y in upcov[x]: m|=up[y]
        up[x]=m
    dn=[0]*n
    for x in range(n):
        for y in range(n):
            if (up[y]>>x)&1: dn[x]|=1<<y
    for x in range(n):
        for y in range(x+1,n):
            c=dn[x]&dn[y]
            if not any(dn[z]==c for z in range(n) if (c>>z)&1): return None
            c=up[x]&up[y]
            if not any(up[z]==c for z in range(n) if (c>>z)&1): return None
    degB=[sum(1 for b in B if i in b) for i in range(s2)]
    c2=[sum(1 for pp in P if i in pp) for i in range(5)]
    F0 = all(d>=2 for d in degB); MI0 = all(v>=2 for v in c2)
    ups=[bin(up[atom(i)]).count('1') for i in range(5)]
    Mset=[atom(i) for i in range(5) if c2[i]==1]+[r2(i) for i in range(s2) if degB[i]==1]+[r3(i) for i in range(s3)]
    c27=all(u>4 for u in ups)
    c211=all(any((up[atom(a)]>>Mset[i])&1 and (up[atom(a)]>>Mset[j])&1 for a in range(5))
             for i in range(len(Mset)) for j in range(i+1,len(Mset)))
    return dict(n=n,F0=F0,MI0=MI0,c27=c27,c211=c211,ups=ups)

from collections import defaultdict
stats=defaultdict(lambda: dict(hunt=0,odd=0,gap0=0,Tatoms=0,minexact=None,profiles=set()))
d4_untouched=dict(total=0,failF0=0,fail0MI=0,faillat=0,hunt=0)
for np_ in range(0,6):
    for Pdel in combinations(range(10),np_):
        P=[pairs[i] for i in range(10) if i not in Pdel]
        c2=[sum(1 for pp in P if i in pp) for i in range(5)]
        if any(v<2 for v in c2): continue
        for nt in range(0,7):
            D=np_+nt
            for Tdel in combinations(range(10),nt):
                Tt=[trips[i] for i in range(10) if i not in Tdel]
                r=build(P,Tt)
                # D=4 untouched-atom analysis (any deletion mix)
                if D==4:
                    touched=set()
                    for i in Pdel: touched|=pairs[i]
                    for i in Tdel: touched|=trips[i]
                    if len(touched)<5:
                        d4_untouched['total']+=1
                        if r is None:
                            d4_untouched['faillat']+=1
                        else:
                            if not r['F0']: d4_untouched['failF0']+=1
                            if not r['MI0']: d4_untouched['fail0MI']+=1
                            if r['F0'] and r['MI0'] and r['c27'] and r['c211']: d4_untouched['hunt']+=1
                if r is None: continue
                if not (r['F0'] and r['MI0'] and r['c27'] and r['c211']): continue
                s=stats[D]; s['hunt']+=1
                n=r['n']
                if n%2==1:
                    s['odd']+=1
                    T=(n+1)//2
                    mx=max(r['ups'])
                    if mx>=T: s['gap0']+=1
                    ex=sum(1 for u in r['ups'] if u==T)
                    s['Tatoms']+=ex
                    g=T-mx
                    s['minexact']=g if s['minexact'] is None else min(s['minexact'],g)
                    if g<=1: s['profiles'].add(tuple(sorted(r['ups'])))
print("D | hunt lattices | odd-n hunt | min gap (odd) | gap<=0 count | exact T-atoms | gap<=1 profiles")
for D in sorted(stats):
    s=stats[D]
    print(f"{D} | {s['hunt']} | {s['odd']} | {s['minexact']} | {s['gap0']} | {s['Tatoms']} | {sorted(s['profiles']) if s['profiles'] else ''}")
print("\nD=4 untouched-atom configs:", d4_untouched)
