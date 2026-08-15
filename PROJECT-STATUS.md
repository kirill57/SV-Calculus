# Project Status — Single-Variable Calculus PreTeXt

## Paths
- Target root: `/workspaces/SV-Calculus`
- LaTeX source root: `/workspaces/SV-Calculus/Single_Variable_Calculus_Change__Accumulation__and_Approximation`
- Local MVC reference root: Not mounted in container (documented in resolve_paths.sh)

## Current stage
- Phase: Phase 1 (Full Section Conversion with 100% Verbatim Fidelity)
- Fidelity Rule: Under NO circumstances may original LaTeX text, derivations, remarks, examples, or narrative be changed, omitted, summarized, or condensed without explicit maintainer directive.
- Fidelity Audit Tool: `tools/audit_fidelity.py` tracks word-for-word retention against LaTeX source.
- Audit Findings:
  - Chapter 1 (§1.1–§1.7): 100% Verbatim.
  - Chapter 2 (§2.1–§2.7, §2.9): Verbatim. §2.8 needs re-conversion to restore omitted text.
  - Chapter 3 (§3.1): Verbatim. §3.2–§3.9 need full re-conversion to restore all omitted text.
  - Chapter 4 (§4.1–§4.9): Needs full verbatim conversion.

## Next exact action
Re-convert §2.8 and §3.2 onwards with 100% complete verbatim text fidelity.
