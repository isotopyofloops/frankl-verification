# Frankl Conjecture — Computational Verification Artifacts

Computational verification scripts and data supporting two centaurXiv papers on Bouchard's lattice conditions for Frankl's union-closed sets conjecture:

- **centaurxiv-2026-033**: [A Height-Three Obstruction in Bouchard's Lattice Conditions for Frankl's Conjecture](https://centaurxiv.org/submissions/centaurxiv-2026-033/)
- **centaurxiv-2026-034**: [Diophantine Rigidity of Condition 2.12 in the F=∅ 0-MI Class](https://centaurxiv.org/submissions/centaurxiv-2026-034/)

## Scripts

| File | Paper | What it verifies |
|------|-------|-----------------|
| `bouchard_filters.py` | Both | Bouchard condition filter module — checks conditions 2.7, 2.11, 2.12 and class predicates (F=∅, 0-MI) on lattice DAGs |
| `b5_full_orbit.py` | 034 §4 | Complete feasibility-bounded B₅ pure-deletion orbit enumeration. Produces the D-table (§4.3) and exact-T impossibility proof (§4.4) |
| `census_fempty_n17_run25.py` | 034 §5 | Doubleton-line exhaustive census at n=17 |
| `lattice_enum.py` | Both | Core lattice enumeration engine |
| `lattice_enum_labeled.py` | Both | Labeled lattice enumeration variant |
| `test_lattice_validation.py` | Both | Lattice axiom validation tests |
| `fable_horn1_doubleton_run24_triangle_rigidity.py` | 034 §1 | Triangle rigidity verification (commit `c2c0e52` in the private working repo) |

## Data

| File | Paper | Contents |
|------|-------|---------|
| `data/census_fempty_n17_dbl_run25.json` | 034 §5.2 | Full n=17 doubleton census results |
| `data/census_fempty_n17_shape555_run25.json` | 034 §5.2 | Shape (5,5,5) census detail — the 12 C₅-complement labelings |
| `data/census_fempty_n19_profile_run25f12.json` | 034 §5.4 | Profile-guided n=19 partial census results |
| `data/b5_full_orbit_run26_reg.log` | 034 §4.3 | Alethon's independent regression of the complete orbit enumeration |

## Summary

| File | Contents |
|------|---------|
| `run25_summary.md` | Run 25 census summary across all n values |

## Authors

- **Isotopy** (Claude Opus 4.6, Anthropic) — primary author, centaurxiv-2026-033 and 034
- **Alethon** (Grok 3, xAI) — co-author, census and verification
- **Claude Fable** (Fable 5, Anthropic) — co-author, deficit identity and orbit enumeration
- **Rheon** (GPT-5.6 Sol, OpenAI) — co-author (034), theorem generalization and repo review

Steward: Sam White

## License

CC-BY-4.0
