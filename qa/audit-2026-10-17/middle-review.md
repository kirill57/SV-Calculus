# Chapters 7–12 and Appendix F: audit report

Audit date: 2026-10-17. Scope: the PreTeXt edition only. Review began from the parent-reported commit `afde796172ecd268507c15604551363c95ce95a8` and an initially clean working tree. This worker did not run Git commands, builds, publication, or one-time scripts from earlier work.

## Source coverage

The review read all 56 section files, the six chapter introductions, and the Appendix F introduction. It included the complete explanations, theorem and note hypotheses, derivations, worked examples, exercise statements, and all hints. All 100 figure source blocks were checked against the accompanying mathematics and captions; their live renderings were then inspected as described below.

| Division | Sections read | Examples | Exercises | Hints | Figures | Tables |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Chapter 7 | 7.1–7.9 (9) | 20 | 33 | 33 | 24 | 3 |
| Chapter 8 | 8.1–8.8 (8) | 20 | 31 | 31 | 19 | 1 |
| Chapter 9 | 9.1–9.7 (7) | 22 | 28 | 28 | 13 | 2 |
| Chapter 10 | 10.1–10.9 (9) | 37 | 35 | 35 | 24 | 6 |
| Chapter 11 | 11.1–11.9 (9) | 53 | 37 | 37 | 8 | 14 |
| Chapter 12 | 12.1–12.7 and both additional-topic sections (9) | 16 | 30 | 30 | 12 | 16 |
| Appendix F | F.1–F.5 (5) | 0 | 0 | 0 | 0 | 20 |
| **Total** | **56** | **168** | **194** | **194** | **100** | **62** |

The section count includes the new Richardson/Romberg and complete adaptive-quadrature sections. Chapter 11 coverage includes the new inverse-hyperbolic antiderivatives and absolute/conditional improper convergence material. This worker did not change the separate original LaTeX edition.

## Corrections

The exact correction ledger is `middle-changes.jsonl`: currently **103 records across 43 source files**. Every record gives the original text or figure fragment, replacement, source path, reason, and mathematical verification. Location-only changes also identify the old and new placement. Several records concern distinct parts of the same figure or explanation; the record count is not a count of independent mathematical errors.

The principal corrections are:

- **Related rates and optimization (7.1–7.2):** a wrong sign can arise from algebra as well as variable definitions; the reflection model first states the physical domain and justifies restricting the minimizer to the segment between the projected endpoints.
- **Newton iteration (7.4):** `577/408` does not round to the same five decimal places as `sqrt(2)`; the text now states the actual error bound. The first-step figure now places its `x_1` tick at `17/12`, and an incorrectly placed “tangent line” label was moved to the actual tangent. An anthropomorphic failure hint was replaced by the denominator-zero and cycle mechanisms.
- **Growth models (7.5–7.6, 7.9):** a positivity condition accidentally embedded in a long heading was restored to ordinary text; the logistic derivative caption now states `0<P<K`, and the solution caption specifies the positive initial-value family. The cooling review keeps the exact exponential constant rather than claiming an exact equivalence after rounding. A premature end-of-chapter transition was corrected because the light-path section still follows.
- **Integral construction (8.2, 8.6):** the introductory area explanation no longer relies on “integrable” before its definition. The equality case for the integral triangle inequality distinguishes vanishing positive/negative accumulated amounts from isolated sign changes.
- **FTC and antiderivatives (9.1, 9.4, 9.7):** signed velocity gives displacement, whereas odometer distance integrates its absolute value. Indefinite linearity now uses chosen antiderivatives plus an arbitrary constant, including the case of both coefficients zero. The chapter-map figure no longer suggests that one endpoint change determines an entire antiderivative. A second data experiment is explicitly independent of the earlier exact rate formula; its listed data were not samples of that rate.
- **Integral applications (10.1–10.9):** distinguish strip height from thickness; state the cross-sectional integrability assumption and the quadrant needed for the selected inverse-parabola branch; explain that simply splitting shells does not remove overlapping shells; distinguish a sufficient uniform-density condition from a necessary condition for a centroid; use signed coordinates in moments; state the ideal-work assumptions; repair an incorrect “last section” reference; give the missing definite bounds in normalization/expectation/center-of-mass analogies. The review now states the nonnegative shell-coordinate condition and uses the absolute distance from the axis in the surface-area formula.
- **Integration methods (11.3–11.9):** a raw-TeX table heading was replaced with a meaningful title; explain why roots excluded from a rational expression may be used in the cleared polynomial identity; state the radical-table domain; use the general singular-endpoint definition needed by oscillatory examples; remove the false claim that decay faster than `1/x` ensures convergence, with `1/(x log x)` as a counterexample; correct the hint for `x^3 exp(x^2)` to require integration by parts after substitution; distinguish checks of indefinite, definite, and improper CAS answers. Transitions now follow the newly added core subsections rather than interrupting them.
- **Numerical methods (12.1–12.8):** three Gaussian midpoint values were incorrect: for `n=8`, `.747290 → .747304`; for `n=16`, `.746941 → .746944`; for `n=32`, `.746853 → .746854`. The method is now identified so these values are reproducible. A quadratic interpolant may have degree at most two, since three data points can be collinear. Numerical noise averaging is qualified to distinguish zero-mean fluctuations from systematic bias. A tiny Newton derivative can cause a large step rather than a stall. Printed Newton residuals are explicitly calculated from unrounded iterates. The residual-to-root-error slope bound must hold on the entire interval joining the iterate and root. Statements about convergence order now refer to bounds or typical leading errors rather than asserting that every actual error decreases exactly by that order.
- **Prerequisite order (12.8):** the centered-difference extrapolation now uses an explicit finite remainder identity, proved by repeated integration, rather than relying on the Taylor material first developed in Chapter 16. The trapezoidal expansion points back to this already-established finite-remainder method. Chapter 12’s transition now accounts for the two optional numerical-integration sections before differential equations.
- **Reference tables (F.1–F.5):** add the missing standard-branch arccotangent derivative; make indefinite linearity’s arbitrary constant explicit; state the terminating binomial-polynomial exception; clarify the zero/infinite radius cases; align numerical-rule smoothness hypotheses with the continuous-derivative assumptions used in the main theorems.
- **Language:** replace uninformative metaphors such as “hypotheses are not decoration,” tangent lines “pointing somewhere the original curve never intended,” and “dangerous endpoints” with the actual assumptions or steps. The ledger flags these replacements explicitly.
- **Visible math typesetting:** optional array spacing placed on a separate line was printing literal `[2mm]` text in the live MathJax output. Four occurrences in 8.8 and one in 10.3 now attach the spacing argument directly to the row-break command.

## Figure corrections and visual evidence

The parent captured the actual live book, rather than relying on source inspection alone. I inspected every middle contact sheet under `live-before/contacts/middle/`:

- `figure/figure01.png` through `figure/figure09.png`: all 100 owned figures.
- `table/table01.png` through `table/table06.png`: the 62 structural tables, including Appendix F.
- `opening/opening01.png` through `opening/opening06.png`: all owned chapter, section, and appendix openings.

The manifests in those directories map tiles to the actual captured elements and pages. For close inspection, full-size renderings were also viewed for `fig-finite-difference-secants`, `fig-newton-wrong-root`, `fig-simpson-quadratic-through-three-points`, `fig-newton-double-root`, and `fig-hydrostatic-triangle`. The finite-difference labels were readable and did not need alteration. The upper part of the figure in one difference-quotient-tree contact tile was obscured by the browser’s capture position; inspection of the underlying figure did not establish a source defect.

**18 figures require regeneration.** The authoritative list is `middle-changed-figures.json`:

1. `fig-newton-sqrt2-first-step`: correct the first tangent intercept.
2. `fig-newton-wrong-root`: attach the tangent label to the actual tangent.
3. `fig-partition-sample-points`: increase the vertical range so the right-hand sample is not clipped.
4. `fig-monotone-upper-lower-sums`: increase both panels’ vertical range to include the full graph and rectangles.
5. `fig-finite-jump-integrable`: use an opaque white interior for the excluded endpoint so the underlying curve does not show through it.
6. `fig-ftc1-squeeze-strip`: make the plotted endpoint agree exactly with its displayed value.
7. `fig-ftc1-step-counterexample`: make the excluded endpoint’s interior opaque.
8. `fig-chapter9-ftc-map`: remove an invalid reverse implication from an endpoint change to an antiderivative function.
9. `fig-warning-jump-accumulation`: make the excluded endpoint’s interior opaque.
10. `fig-spring-hookes-law`: measure extension to the spring attachment and add its natural-position reference.
11. `fig-hydrostatic-triangle`: make the highlighted strip meet the sloping plate sides and place its width dimension at the indicated depth.
12. `fig-sine-arc-length`: move a formula label out of the curve.
13. `fig-infinite-discontinuity-comparison`: put the two convergence descriptions in a legend so the longer description does not overflow the plot.
14. `fig-midpoint-single-interval`: prevent right-endpoint clipping and attach the marked-point label at its exact coordinate with a west anchor.
15. `fig-trapezoid-single-interval`: prevent right-endpoint/trapezoid clipping.
16. `fig-simpson-quadratic-through-three-points`: replace ambiguous, displaced interior descriptions with a compact legend for the actual graph and quadratic interpolant.
17. `fig-newton-double-root`: place the marked-point label at `(1.5,.25)` and prevent the line from crossing the text.
18. `fig-conditional-improper-lobes`: exclude the four shading plots from the legend so the signed and absolute-value curves have the correct solid/dashed legend samples.

White fills were used only where an actual underlying curve would remain visible through an excluded point or collide with a label. Hollow Newton-iteration markers were not restyled indiscriminately. No further missing explanatory figure was identified within this scope after the live and source review.

## Mathematical and executable verification

Run `python qa/audit-2026-10-17/middle_verify.py` from the repository root. It is a repeatable, read-only source checker apart from rewriting its own receipt, `middle-verification.json`. The receipt currently reports **181/181 checks passed**, with no failures, and records SHA-256 hashes of the 63 current owned section/chapter/appendix source files.

The checks include:

- XML parsing of all owned sources and the coverage counts above.
- Related-rate calculations, optimization derivatives and convexity, linearized measurement errors, cooling and logistic values, the logistic ODE identity, and the refraction example.
- Both Newton iterate tables and the displayed residuals calculated before decimal rounding.
- Independent exact evaluations of 36 representative geometric, physical, probability, work, and improper integrals, including pumping, hydrostatic force, and the circular window.
- Symbolic differentiation of the nontrivial integration-method answers, negative inverse-hyperbolic branches, both signs in the reciprocal inverse-hyperbolic patterns, the logarithmic decay counterexample, and the conditional-sine integration-by-parts formula and lobe lower bound.
- Every printed numerical quadrature table: introductory Gaussian midpoint sums, midpoint samples, Gaussian midpoint/trapezoid/Simpson comparison, the pi table, normal probabilities, and nonsmooth-square-root comparison. The finite-difference approximation/error table is recomputed too.
- The Gaussian fourth-derivative bound, Richardson cancellation, every printed quartic Romberg table entry, and the two-half-panel Simpson bound constant `1/46080`.
- Execution of the **exact Python algorithm printed in the current source**, including polynomial and pi success cases, a localized Gaussian peak, indicator accounting and evaluation reuse, evaluation-budget/depth/nonfinite/midpoint/roundoff failures, and the sampling-aliasing counterexample.

These checks supplement the full manual review; they do not claim that finite tests establish every analytic theorem or certify arbitrary adaptive-quadrature outputs. The printed algorithm correctly labels its indicator as an estimate and explains what a derivative bound would change.

## Handoff state

Source corrections, focused verification, and corrected local visual confirmation are complete. The parent completed the final HTML build and targeted browser recapture; all middle visual follow-ups are closed as documented below. The parent retains responsibility for origin synchronization and publication. This report does not claim that external publication has already succeeded.

Initial text/figure dumps under `middle-text/` are reading scratch snapshots from before these edits. The `middle_*fix*.py` / `middle_*followups.py` authoring helpers are one-time exact-replacement scripts and must not be rerun; the supported repeatable verification command is `middle_verify.py`.


## Corrected local browser visual review

The completed `local-final` sweep was used after regenerating all four middle contact-sheet kinds. I inspected all **24 local sheets**, with complete coverage:

- `local-final/contacts/middle/figure/01.png`–`09.png`: **100 figures**, including the 17 originally corrected figures.
- `local-final/contacts/middle/table/01.png`–`06.png`: **62 structural tables**, including all Appendix F reference tables.
- `local-final/contacts/middle/array/01.png`–`03.png`: **33 display-math arrays**. The spacing artifacts repaired in 8.8 are gone; the numerical and formula arrays are legible.
- `local-final/contacts/middle/opening/01.png`–`06.png`: **70 chapter/section/appendix/index/introduction openings**, including the separate introduction chunks.

I also inspected all **seven original-live introduction chunks** in `live-before-extra/contacts/middle/opening/01.png`. These had been omitted from the initial canonical sweep. They introduce no further language or typesetting issue beyond the already-reviewed text.

Full-size local captures were inspected for the oscillatory-integral legend, the Simpson interpolant legend, and the large Chapter 10 review table. Two actual remaining visual defects were found and corrected with the parent's coordination:

1. In `fig-conditional-improper-lobes`, the shading plots were being used as legend styles, making the dashed absolute-value curve's legend sample solid. Adding `forget plot` to the four shading plots leaves the actual curve styles in the legend.
2. `tab-sec-10-9-chapter-review-and-applications-1` clipped the right side of several formulas at an ordinary desktop width. It now has two columns: quantity (20%) and small piece/total (80%). Each row retains its original contribution and total in separate paragraphs, with all formulas and conditions preserved.

These two source corrections are journaled (records 99 and 100). The focused checker was rerun after both changes and remains **181/181 passing**. The final build also requested explicit column widths for the paragraph-containing inverse-trigonometric derivative table in F.1; record101 adds33%/34%/33% without changing its cells or formulas. F.1 was included in the targeted recapture. All three follow-ups are now render-confirmed below, and no further source correction is pending.


### Final targeted visual confirmation

After the parent's final build and eight-page browser recapture passed, I inspected these full-size actual local browser captures:

- `local-followup/screenshots/sec-11-7-improper-integrals/figure-fig-conditional-improper-lobes.png`: the legend now has the correct solid sine sample and dashed absolute-value sample, matching the plotted curves.
- `local-followup/screenshots/sec-10-9-chapter-review-and-applications/table-tab-sec-10-9-chapter-review-and-applications-1.png`: all13 rows, contribution and total formulas, and conditions fit within the desktop table. No right-side clipping remains, including the long surface-area formula.
- `local-followup/screenshots/sec-f-1-derivative-formulas/table-tab-sec-f-1-derivative-formulas-3.png`: the explicit-width inverse-trigonometric derivative table is legible; all six functions, derivatives, and domain conditions are visible.

**Visual closure: passed.** The source journal contains **103 records across43 source files**, the regeneration list contains **18 figures**, and the repeatable focused verification remains **181/181 passing**. No unresolved mathematical, source, or visible-layout finding remains within this worker's assigned chapters7–12 and AppendixF scope.


### Final total-work correction and release confirmation

The final full-size table review identified the missing definite bounds in the pumping-fluid total-work row. Records102 and103 add `a,b` to the total-work integral in both the review table (10.9) and its original derivation (10.5), and define these as the fluid-slice height limits. The independently checked rectangular and conical examples already used the correct definite integrals.

I inspected `local-last/screenshots/sec-10-9-chapter-review-and-applications/table-tab-sec-10-9-chapter-review-and-applications-1.png`: the bounds are visible, the new height-range explanation is clear, and all table content still fits without clipping. I also checked the current10.5 source: it displays `W=\int_a^b \gamma A(y)D(y)\,dy` and defines `a,b` as the lowest/highest fluid-slice heights. The parent reports the final rebuild and browser checks of10.5,10.9, and the index passed.

**Final closure:103 correction records,43 source files,18 changed figures,181/181 focused checks, and no unresolved finding in the assigned scope.** No source edit remains pending.
