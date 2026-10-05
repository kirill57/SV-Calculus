# Audit of the PreTeXt edition

Audit date: 5 October 2026.

This report records the initial complete audit, before the selected additions and subsequent language pass. The current implementation and verification are documented in [SELECTED-TOPICS-REPORT.md](SELECTED-TOPICS-REPORT.md) and [LANGUAGE-AUDIT.md](LANGUAGE-AUDIT.md). Counts and receipts below describe the initial audited version.

## Scope and deliverables

The audit covers the PreTeXt manuscript in `source/`: all 17 chapters, Appendices A-F, frontmatter, examples, theorem statements and proofs, conceptual checkpoints, exercises, worked answers, and all 580 exercise hints. It also covers the generated diagrams, the interactive sphere, HTML rendering, and the PDF generated **from PreTeXt**.

The separate original LaTeX edition in `Single_Variable_Calculus_Change__Accumulation__and_Approximation/` is excluded. SHA-256 comparison against the starting inventory confirms that its 34 files are unchanged.

Corrections were applied directly to the PreTeXt source. The maintainer subsequently selected ten additions; [MISSING-TOPICS.md](MISSING-TOPICS.md) records those decisions and the four remaining proposals. The initial audit's detailed edit journal is [audit/editorial-changes.jsonl](audit/editorial-changes.jsonl). Journal records include repeated refinement of the same passage and mechanical markup repairs; their count is not a count of distinct mathematical errors.

## Mathematical and logical corrections

This table summarizes representative corrections. The journal provides the exact source paths, reasons, and replacement text.

| Material | Corrections |
| --- | --- |
| 1. Velocity and distance | Distinguished a distance function from a final odometer reading; corrected sampled-distance estimates and signed velocity interpretations; stated the conditions for forward motion. |
| 2. Numbers, functions, and models | Put completeness assumptions before their use; corrected the triangle-inequality discussion, punctured increments, monotonicity assumptions for inverses, and domains of real powers. |
| 3. Limits and continuity | Repaired composition-limit reasoning when the inner function reaches the limiting point; corrected an invalid differentiation argument based on a single sequence; repaired the intermediate-value bisection stopping case. |
| 4. Derivatives | Corrected the distinction between strict and non-strict monotonicity; supplied the hypotheses for differential estimates and the time domain of a motion example. |
| 5. Differentiation rules | Repaired the chain-rule proof at zero increments; placed inverse differentiation before the logarithm proof that uses it; corrected branches, logarithmic absolute values, catenary arc length, and the distinction between finite changes and differentials. |
| 6. Shape and the mean value theorem | Corrected mean-value and l'Hospital hypotheses; supplied continuity at an inflection point; repaired asymptotic notation and introduced factorial notation before use. |
| 7. Optimization and models | Corrected maximum/minimum interpretations, physical domains and parameter signs, the mirror-path argument, numerical starting values, and effective interest. Replaced a premature Taylor-based Newton argument with one using Rolle's theorem. |
| 8. The integral | Corrected rectangle sums and sample-point coordinates; repaired a differentiability claim at a velocity jump; supplied the completeness and continuity arguments used in integrability, and defined binomial coefficients and measure zero when needed. |
| 9. Fundamental theorem | Corrected endpoint and continuity assumptions, clarified accumulation versus instantaneous rates, justified substitution without assuming a monotone substitution, and replaced an exercise requiring an improper integral before that notion is introduced. |
| 10. Integral applications | Repaired shell overlap, orientations in mass and work, normal-density parameters, and interval assumptions. Expressed the centroid shortcut using the one-variable strip integral already available. |
| 11. Integration techniques | Corrected integration-by-parts regularity, trigonometric-power ranges, substitution parameters and branches, inverse-hyperbolic notation, and improper-comparison hypotheses. |
| 12. Numerical calculus | Repaired quadrature error proofs and distinguished error bounds from actual errors; supplied a finite Taylor remainder, corrected central-difference and noise bounds, and separated Newton residual error from root error. Corrected sampled rectangles and restored the missing Newton-map illustration. |
| 13. Differential equations | Distinguished stability from attraction; corrected forward-time and forcing assumptions, Euler stability and damping conditions, and the bank-balance calculation. Replaced the inaccurate predator-prey trajectory with a numerically checked orbit. |
| 14. Parametric and polar curves | Corrected tracing direction, regularity and single-tracing assumptions, polar intersection branches, conic distance signs, gravity direction, and angular versus linear speed. Defined moving unit vectors and excluded the argument of zero. Moved the eccentricity checkpoint after its definitions. |
| 15. Sequences and series | Removed undefined early terms and ratio-test cases; corrected an exact partial sum and outward-rounded error bounds; allowed equality in the alternating-series estimate and repaired the rearrangement argument. |
| 16. Power and Taylor series | Corrected radius/interval language, center cases, polynomial order and decimal approximations; supplied the continuity and differentiation arguments needed for termwise integration and differentiation. Repaired the Airy recurrence convergence discussion and illustrated the fixed-area shrinking-spike counterexample. |
| 17. Complex numbers and previews | Justified componentwise complex differentiation, repaired oscillator parameters and phase, preserved odd symmetry at Fourier jump points, and supplied the smoothness, notation, and local variation argument needed for Euler-Lagrange reasoning. Distinguished stationarity from minimization. |
| Appendices A-F | Corrected radical and rational-power domains, degenerate conics, signed angles, trigonometric branches and lost solutions, continuity/tangent claims, convergence examples, numerical notation, and hypotheses in reference tables. Executed the actual Python examples. |

The hint pass corrected misleading guidance about signs, parity, domains, hypotheses, and the conclusions available from a theorem. False checkpoint statements were corrected as well as their hints.

## Order of presentation

The principal dependency repairs include inverse differentiation before the logarithm derivative, factorials and binomial coefficients at first use, an elementary Newton proof before Taylor's theorem, proper integrals before improper-integral exercises, the one-variable centroid identity before multivariable notation, eccentricity after its defining parameters, and uniform-limit continuity before integrating a limit of polynomials. Preview material retains its introductory role, with necessary local notation and hypotheses supplied.

## Figures and document structure

- Reviewed all 365 generated SVG panels visually in chapter and appendix contact sheets, then rechecked revised panels. Reviewed the native interactive sphere separately and within its section.
- Corrected unequal coordinate scales in inverse-reflection and circle/oscillator diagrams, inaccurate regions and trajectories, clipping, overlaps, labels, endpoint conventions, and mismatched caption interpretations.
- Replaced the missing Newton-map drawing and added the shrinking-spike drawing supporting an existing counterexample. The final manuscript has 323 figures containing 366 image panels: 365 SVG panels and one interactive Asymptote panel.
- Supplied image descriptions based on existing captions, with panel identification where needed. These descriptions provide alternatives to previously undescribed images; they are not a replacement for a separate accessibility review of every mathematical diagram.
- Repaired malformed display and cases markup, leaked TeX in prose and tables, unsupported paragraph nesting, empty semantic blocks, table titles, multipanel grouping, and cross-references. Restored existing text rather than abridging it.
- Added short running titles, made prose tables wrap within the page width, converted prose workflows to numbered lists, changed long prose equations to wrapping text, and split oversized formulas across lines. Paragraph cells were supplied in 116 tables: column-width declarations alone had allowed long cells to shrink the whole table to an unreadable size.
- Moved the sphere outside a collapsed example. A zero-size hidden WebGL canvas had caused recursive rendering and a JavaScript stack overflow; the corrected section loads without that error.

## Verification

Final verification passed for all 182 sections, all 580 opened hints and 28 supplemental pages, with no formula-rendering errors, JavaScript errors, broken generated images, or desktop/mobile horizontal overflow. All 40 numerical/code checks passed. The final PDF has 1,447 pages, no text outside physical page boundaries, and no overfull boxes of 12 points or more. Forty-eight selected PDF pages were rendered and reviewed visually. The original edition's 34 files are unchanged.

Final source hashes and the combined verification receipt are in `audit/final-validation.json`. The status file summarizes the completed checks.

| Check | Evidence |
| --- | --- |
| Complete XML assembly, unique IDs, resolved cross-references, image inventory | `audit/inventory.json` |
| Manuscript PreTeXt schema validation | `audit/schema-current.log` (empty on success) |
| Balanced display-math grouping and repeated-sentence scan | `audit/math-grouping.json`, `audit/repeated-sentences.json` |
| Desktop and mobile browser checks for all 182 sections, including opened hints | `audit/browser-results.json` |
| Chapter introductions, appendices and frontmatter browser checks | `audit/browser-supplement.json` |
| Interactive sphere and embedded section | `audit/interactive-sphere.json`, `audit/inline-sphere-errors.json` |
| Figure inventory and visual contact sheets | `audit/figure-manifest.json`, `audit/figures/` |
| Independently recalculated quadrature tables, polynomial exactness, bank balance, arctangent approximation and execution of 12 printed Python snippets | `audit/numerical-code-checks.json` (40 checks) |
| Near-critical p-series partial sums and predator-prey orbit invariant | `audit/series-partial-sums.json`, `audit/predator-prey-orbit.json` |
| PDF build, page-boundary scan, selected page rendering and visual review | `audit/print-build-final.log`, `audit/print-physical-boundaries.json`, `audit/print-visual-review.json` |
| Preservation of the original edition | `audit/original-edition-preservation.json` |

All source sections, hints and figure panels were reviewed. PDF visual review uses selected pages, including chapter openings and changed or previously defective layouts; the automated boundary scan covers every PDF page. The audit combines mathematical reading, independent calculations and rendering checks, rather than formal machine verification of every proof.

## Rebuilding and local toolchain limitations

The corrected outputs are `output/web/index.html` and `output/print/main.pdf`. The PDF is the print rendering of the corrected PreTeXt edition.

The installed CLI is PreTeXt 2.53.0, while the project's requirements specify 2.49.1. The installed stylesheets warn about older display-math and directory syntax that their accompanying schema still accepts. These compatibility warnings do not prevent the verified builds. The audit does not update the project's toolchain version.

The installed publication schema also rejects the project's existing HTML theme/contents settings and empty EPUB configuration, although the current build pipeline processes them successfully. Its diagnostics are retained in `audit/publication-schema-current.log`. The manuscript schema passes; publication-schema compatibility is a separate toolchain limitation.

On this workstation, native Asymptote PDF generation fails in the MiKTeX rendering/label pipeline. A high-resolution static export of the book's verified WebGL sphere supplies the print asset; its provenance is in `audit/sphere-print-fallback.json`. The interactive web figure remains available. To reproduce this print build after regenerating web assets:

```powershell
pretext generate latex-image -t web
pretext build web --no-generate
python tools/prepare_print_sphere.py
pretext build print --no-generate --latex
```

The helper requires the existing Python, Pillow, Playwright and Microsoft Edge installations. A plain `pretext build print` may attempt the failing native Asymptote renderer again. No toolchain software was installed as part of this audit.

The `audit_round_*.py` and markup-repair scripts are one-time edit records, not a rebuild pipeline; do not replay them on an already corrected manuscript. Read-only verification commands are documented in [audit/README.md](audit/README.md).
