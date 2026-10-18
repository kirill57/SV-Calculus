# Late-chapter audit: chapters 13–17 and Appendices D–E

Audit date: 2026-10-17. Scope: the current PreTeXt edition only. The separate original LaTeX edition was not edited.

## Coverage

The source review covers all 69 owned chapter/appendix and section files: 62 sections, 279 subsections, 194 examples, 18 theorems, 2 definitions, 191 exercises with 191 hints, 62 tables, 102 figures containing 110 image panels, and 13 printed Python code blocks. Mathematical review included formulas and worked calculations; theorem hypotheses and proof steps; question/hint agreement; the distinction between necessary and sufficient conditions; domains and parameter intervals; and figure geometry, arrows, plotted values, and labels.

The chapter groups reviewed were:

- Chapter 13: rate models, slope fields, Euler/Heun, separation, logistic and harvesting models, linear equations, oscillators, systems, warning examples, review, and the additional Runge–Kutta section.
- Chapter 14: parametric slopes, tangents, concavity, length, surface area, signed area, cycloids, polar graphs, intersections, conics, planetary motion, complex polar form, warnings, and projects.
- Chapter 15: sequence and series definitions, monotone/Cauchy criteria, geometric and telescoping sums, positive and alternating tests, absolute convergence, ratio/root/Dirichlet/Abel tests, rearrangement, and contraction iteration.
- Chapter 16: power-series domains and endpoint tests; algebra, integration and differentiation; elementary Taylor/binomial representations; finite remainders; series solutions; pointwise/uniform convergence; warning examples; and the M-test.
- Chapter 17: complex series and Euler’s formula, oscillator energy and forcing, Fourier coefficients and jumps, boundary identities, density/flux conservation, first variation and action, projects, and the local Lipschitz existence/uniqueness theorem.
- Appendix D: supremum/infimum, completeness, monotone and nested-interval arguments, bisection, extrema, uniform continuity, finite-cover proof, practice problems, and answers.
- Appendix E: graphing windows, finite precision, syntax/radians, printed Python experiments, sequence/series/Taylor plots, practice problems, and answers.

## Corrections

55 correction records across 25 source files are documented with exact original/replacement text, reasons, and mathematical verification in `late-changes.jsonl`. Related replacements are grouped where they repair one figure, table, or explanation.

Substantive findings corrected:

- Two logistic phase lines pointed upward below zero although their displayed derivatives are negative.
- The stability interpretation confused stability with asymptotic stability and described all nearby trajectories as repelled by an unstable equilibrium.
- Early initial-value language implied uniqueness without conditions; the general solution definition required only one derivative even for second-order equations.
- The polar slope rule omitted its nonzero denominator condition. The ellipse-comparison panel cut off a closed endpoint; two spiral diagrams cut their plotted turns into disconnected pieces; the polar-circle intersection diagram omitted substantial parts of both circles.
- The final eight bars in the harmonic-series grouping picture had incorrect heights, and two decimal expansions showed rounded digits followed by ellipses.
- The power-series addition checkpoint incorrectly suggested that absolute convergence is needed for addition at a common endpoint. Another explanation attributed differentiation to uniform convergence of the original functions alone.
- The six-decimal sine example did not justify correct rounding; the replacement supplies a genuine enclosure inside one rounding interval.
- The complex exponential used Euler’s formula immediately before proving it. The consequence now follows its proof. Complex series convergence, complex-valued integration, and symmetric two-sided Fourier sums are defined before being used without explanation.
- The Fourier-coefficient statement omitted integrability; its orthogonality sentence confused a self-product with distinct frequencies. The square wave now assigns zero at jump points before claiming odd symmetry.
- The first-variation calculation needed path regularity and a justification that a continuous coefficient vanishes when all supported variations give zero. An explicit C2 polynomial variation with a zero extension now supplies this step.
- The bisection summary omitted continuity, and the Newton derivative guard needed a clear statement of its limitations.
- Live visual inspection found transparent excluded-point markers, clipped table content, broken mathematical units inside tables, an overflowing midpoint-method display, and inconsistent sizing of the three tangent comparison panels. Corrected local inspection also found three remaining label collisions. These are corrected in source.
- Literal LaTeX-style double hyphens in ordinary HTML prose are replaced by en dashes. No detached `[1mm]`, `[2mm]`, or `[3mm]` array-spacing artifacts were found in this source scope.

## Prerequisite and organization checks

The additions retain their intended ordering. The Cauchy criteria precede the proofs of Dirichlet/Abel and contraction iteration; the M-test follows the definitions and consequences of uniform convergence; the local existence proof follows real completeness, contraction, and uniform-limit results. The Runge–Kutta section defines its local/global error and big-O conventions and explains partial derivatives and the Lipschitz condition where first needed. Euler’s formula in chapter 14 and the end of chapter 16 is explicitly presented as a preview/formal motivation; its justified complex-series derivation is in 17.1. The local theorem remains an optional final section and does not depend on the intervening Fourier/complex previews.

Intentionally blank project tables are student worksheets, not omitted answers. The existing cross-references and chapter/section numbering are retained.

## Live visual inspection

The parent audit captured the user-supplied live URL, https://kirill57.github.io/SV-Calculus/single-variable-calculus.html. I inspected every completed component sheet for this group:

- `live-before/contacts/late/figure/`: `01.png`, `02.png`, `03.png`, `04.png`, `05.png`, `06.png`, `07.png`, `08.png`, `09.png`.
- `live-before/contacts/late/table/`: `01.png`, `02.png`, `03.png`, `04.png`, `05.png`, `06.png`.
- `live-before/contacts/late/opening/`: `01.png`, `02.png`, `03.png`, `04.png`, `05.png`, `06.png`.

These contain all 102 figures, 62 tables, and 69 opening captures assigned by the complete live-site sweep. I also inspected these full-size captures where a tile needed clarification:

- `screenshots/sec-d-3-bolzano-s-theorem-and-bisection/table-tab-sec-d-3-bolzano-s-theorem-and-bisection-2.png` (confirmed right-edge table clipping).
- `screenshots/sec-16-4-taylor-polynomials/table-tab-sec-16-4-taylor-polynomials-2.png` (a polynomial split across lines).
- `screenshots/sec-17-3-fourier-series-preview/table-tab-sec-17-3-fourier-series-preview-3.png` (a break inside `(x-a)`).
- `screenshots/sec-17-2-vibrations-and-second-order-equations/figure-fig-phase-plane-energy-ellipse.png` (the apparent cropped top label was a floating-toolbar capture artifact; the source/figure was consistent).

All paths in that list are relative to `live-before/`. Some component captures included floating site controls over their top edge; this was distinguished from a defect in an image itself. Corrected local and final live verification is coordinated by the parent audit and is recorded separately.

Figures needing regenerated assets:

- `fig-bolzano-crossing`.
- `fig-bolzano-fails-jump`.
- `fig-ch13-logistic-phase-line`.
- `fig-circle-and-spiral-polar`.
- `fig-complex-plane-3-plus-4i`.
- `fig-eccentricity-polar-conics`.
- `fig-harmonic-grouping-blocks`.
- `fig-logistic-phase-line-ch13`.
- `fig-pointwise-xn`.
- `fig-polar-intersections-origin`.
- `fig-polar-spiral-slope`.
- `fig-riemann-rearrangement-idea`.
- `fig-spring-mass-equation`.
- `fig-technology-hidden-hole`.
- `fig-three-zero-velocity-tangent-outcomes`.

Tables changed after live inspection:

- `tab-sec-16-4-taylor-polynomials-2`.
- `tab-sec-17-3-fourier-series-preview-3`.
- `tab-sec-d-3-bolzano-s-theorem-and-bisection-2`.

## Corrected local visual inspection

After the `local-final` browser sweep finished, I regenerated and inspected all 23 late-group contact sheets:

- `local-final/contacts/late/figure/01.png` through `09.png`: 102 figures.
- `local-final/contacts/late/table/01.png` through `06.png`: 62 tables.
- `local-final/contacts/late/array/01.png`: all 4 captured display arrays in this scope.
- `local-final/contacts/late/opening/01.png` through `07.png`: 76 openings, including the 69 canonical chapter/appendix/section pages and 7 separate introduction chunks.

I separately generated and inspected `live-before-extra/contacts/late/opening/01.png`, containing the 7 introduction chunks omitted by the original live sweep. No additional defects were found in those original introduction captures.

Full-size corrected-local captures were inspected for the unit-circle tangent diagram, fourth roots of unity, Riemann rearrangement diagram, complex number 3+4i, spring-mass diagram, and all three previously repaired tables (Maclaurin polynomials, Fourier/Taylor comparison, and bisection). The circle was confirmed circular; the upper fourth root is labeled i; all three tables fit and preserve complete mathematical units. All four display arrays render cleanly, including the corrected harmonic decimal prefixes. Opaque holes, corrected phase arrows, extended polar windows, and common tangent-panel scales are visible in the regenerated figures.

Three further label collisions were confirmed at full size and corrected after coordination with the parent audit:

- `fig-riemann-rearrangement-idea`: removed the redundant target-T annotation across the zigzag; the dashed target remains identified by the vertical-axis T tick.
- `fig-complex-plane-3-plus-4i`: moved the real-part annotation below the horizontal-axis tick labels.
- `fig-spring-mass-equation`: moved F=-ky to the left of its force arrow so the track does not cross the formula.

These three label-only repairs are journaled, parse successfully, and leave the mathematical data unchanged. After the parent's final asset regeneration and web rebuild, I inspected all three full-size captures in `local-followup/screenshots/`: the Riemann target line and zigzag are clear, the real-part annotation is below the axis ticks, and the spring-force formula is clear of the track. All three repairs are render-confirmed. No visible issue remains from this completed local review. `late-local-visual.json` records exact coverage and closure.

## Independent verification

`verify_late.py` passes 36 grouped checks with zero failures. `late-verification.json` records the results, source hashes, coverage, exact figure list, and printed-code output. The checks include:

- Exact symbolic cooling/logistic/damping identities; finite exponential-product and Euler even/odd identities; Fourier orthogonality and square-wave coefficients; and the equivalence of symmetric complex and real Fourier pairs.
- Exact rational harmonic sums, sine enclosure and six-decimal rounding, contraction iteration count, and plotted polynomial endpoint values.
- Logistic arrow signs; complete ellipse/spiral/circle windows; harmonic grouping bars; the predator–prey trajectory’s conserved quantity; Picard bounds; all printed RK comparison values; and opaque hole markers.
- Parsing all owned source files and checking unique IDs and exercise/hint counts.
- Executing all 13 printed Appendix E Python blocks in document order with a noninteractive plotting backend.

This report does not substitute for the parent’s full HTML compilation, schema validation, all-page browser sweep, local opening check, or publication verification. No git, publish, broad build, or separate-LaTeX operation was performed by this reviewer.
