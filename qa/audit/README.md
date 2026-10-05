# Audit evidence and verification tools

The report in `../PRETEXT-AUDIT-REPORT.md` describes scope, corrections and limitations. `editorial-changes.jsonl` contains the edit journal. Figure contact sheets and print-page renders are visual review evidence. Build logs may contain historical failed attempts; use the `*-final.log` files and the current JSON receipts for the final state.

## Repeatable verification

Run from the project root using the existing Python and PreTeXt installations:

```powershell
python tools/audit_pretext.py inventory
python tools/audit_math_structure.py
python tools/audit_numerics.py
python tools/audit_browser.py
python tools/audit_browser.py supplement
python tools/audit_interactive.py
python tools/audit_inline_sphere.py
python tools/audit_print_check.py
python tools/audit_print_render.py
```

The browser checks use Playwright with Microsoft Edge, serve the generated files on a temporary localhost port, check MathJax, and open hints in small section-sized batches. They require network access for the web edition's existing hosted dependencies. The render helper creates selected-page images and sets their visual review status to pending; a human or visual model must inspect those images before marking them reviewed.

Schema validation used the installed PreTeXt Jing shim directly because the CLI validation wrapper failed on this workstation:

```powershell
node C:\Users\cyril\.ptx\2.53.0\salve\ptx-jing-shim.mjs C:\Users\cyril\.ptx\2.53.0\core\schema\pretext.rng qa/audit/schema-input.xml
```

The schema input is assembled by the inventory command, with XInclude-generated `xml:base` metadata removed. It is not a second editable manuscript.

## One-time edit scripts and abandoned experiments

The `audit_round_*.py`, `repair_pretext_markup.py`, `audit_fix_paragraph_groups.py`, `audit_repair_tex_leaks.py`, and `audit_print_*` repair scripts record how corrections were made. They are not generally safe to replay and are not part of the normal book build. Use the corrected source and journal for subsequent edits.

`audit_hint_page.py` and `audit_hint_browser.py` belong to a superseded experiment that aggregated all 580 hints into one page. That test stalled; the final section-by-section browser check covers every hint without relying on that aggregate experiment. Native Asymptote PDF experiments are likewise superseded by the verified static export described in the main report.

Generated artifacts in `output/` and `generated-assets/` remain build outputs. The original LaTeX edition is only hashed and must not be edited by these audit tools.
