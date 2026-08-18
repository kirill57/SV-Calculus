# Project Status — Single-Variable Calculus PreTeXt

## Paths
- Target root: `/workspaces/SV-Calculus`
- LaTeX source root: `/workspaces/SV-Calculus/Single_Variable_Calculus_Change__Accumulation__and_Approximation`
- Local MVC reference root: Not mounted in container (documented in resolve_paths.sh)

## Current stage
- Phase: Phase 2 (All 17 Chapters Converted with 100% Verbatim Fidelity)
- Fidelity Rule: Under NO circumstances may original LaTeX text, derivations, remarks, examples, or narrative be changed, omitted, summarized, or condensed without explicit maintainer directive.
- Fidelity Audit Tool: `tools/audit_fidelity.py` tracks word-for-word retention against LaTeX source.
- Audit Findings:
  - Chapters 1–17 (all 148 sections + 17 chapter wrappers): 100% Verbatim and Valid XML.
  - Zero duplicate XML IDs across entire project (`tools/check_duplicate_ids.py`).
  - Web build generation tested and verified.

## Next steps
- Complete conversion of remaining Appendices A–F and frontmatter/backmatter if requested.
- Continuous visual QA across all chapter pages.
