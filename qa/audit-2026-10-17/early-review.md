# Chapters 1–6 and Appendices A–C: fresh audit

Reviewed the current PreTeXt sources and genuine live-site captures on 2026-10-17. This review is independent of the earlier October audit. No original LaTeX-edition source was edited.

## Coverage

Read all 79 assigned source files: 70 complete sections and nine chapter/appendix introductions. The review included all exposition, definitions, theorems, proof paragraphs, worked examples, exercises, hints, review lists, projects, answers, tables, captions, descriptions, and TikZ figure sources. The source inventory contains:

| Group | Sections | Worked examples | Checkpoint exercises / hints | Figures / image panels | Tables |
|---|---:|---:|---:|---:|---:|
| Chapter 1 | 7 | 4 | 24 / 24 | 10 / 16 | 4 |
| Chapter 2 | 9 | 54 | 39 / 39 | 23 / 27 | 4 |
| Chapter 3 | 9 | 36 | 39 / 39 | 24 / 28 | 6 |
| Chapter 4 | 9 | 17 | 34 / 34 | 19 / 27 | 1 |
| Chapter 5 | 10 | 48 | 39 / 39 | 18 / 18 | 2 |
| Chapter 6 | 8 | 14 | 32 / 32 | 16 / 19 | 1 |
| Appendix A | 6 | 29 | 0 / 0 | 2 / 2 | 8 |
| Appendix B | 6 | 25 | 0 / 0 | 9 / 9 | 4 |
| Appendix C | 6 | 25 | 0 / 0 | 4 / 4 | 5 |
| **Total** | **70** | **252** | **207 / 207** | **125 / 150** | **35** |

The 585 list items include review problems, multipart tasks, and all Appendix A–C practice answers. They were read as well as the separately marked checkpoint exercises. Twelve elements carry the explicit `theorem` tag; additional rules and proof statements are marked as notes or paragraphs and were also reviewed. Machine-readable counts are in [early-coverage.json](early-coverage.json).

## Corrections

There are **122 exact before/after correction records in 44 source files**, recorded in [early-changes.jsonl](early-changes.jsonl). The list includes substantive mathematical corrections, hypothesis and prerequisite repairs, visual corrections, and small sentence repairs. It is a change journal, not a count of 122 independent mathematical errors.

The principal mathematical and logical repairs are:

- **1.7: unsigned distance and average speed.** The trip's interval contributions are `30, 75, 0, -30, 40`. Its displacement is correctly 115 miles, but its total distance is **175**, not 155 miles. The average speed is **175/6**, not 155/6 miles/hour. The second rectangle was also mislabeled +50 rather than its signed area +75.
- **1.4: sampled motion.** Recorded positions determine interval displacement and average velocity. They do not determine the sign of velocity throughout an interval or reveal intervening reversals. The text now states those distinctions before introducing the separate step-velocity model.
- **2.1: strict zero tolerance.** The hint incorrectly said a strict distance bound of zero would require equality. A nonnegative distance cannot be strictly less than zero. The corrected hint matches the definition.
- **2.3: piecewise functions.** A boundary input may appear in both pieces if the outputs agree. The checkpoint title now asks for an unambiguous boundary value rather than requiring exactly one occurrence in the cases.
- **2.7–2.9: models and domains.** The power-law scaling statement now assumes positive inputs and positive scale factors for unrestricted real exponents. A duplicated copy of the previous function catalog is replaced by a model-selection table tied to the four modeling patterns taught in the section. An incomplete logarithmic-classification problem now supplies an actual time-as-a-function-of-amount formula and its physical domain.
- **3.2: square-root limit law.** The rationalization example used a root limit rule not included in the earlier arithmetic limit laws. A short note proves it from `|sqrt(u)-sqrt(v)| <= sqrt(|u-v|)` before its first use; it does not assume the later continuity or derivative formulas.
- **4.4: prerequisite order.** The circle-area differential example now computes its derivative directly from its difference quotient, rather than silently using the constant-multiple derivative rule before section 4.6 proves it.
- **5.3: composite functions.** Different composites need not have different derivatives. Both the exposition and its checkpoint now avoid that invalid implication.
- **5.6: existence of the special exponential base.** The book previously assumed the existence of `lambda(a) = lim (a^h-1)/h` and asserted a unique base giving slope one. A self-contained argument now supplies that existence and uniqueness using the exponent laws, the earlier continuity of real powers, dyadic bisection, and completeness. It defines any needed greatest-lower-bound notation locally and does not depend on later series, integrals, or concavity tests.
- **5.7: inverse prerequisites.** Strict increase of `x^3+x` is proved algebraically before invoking its inverse. This avoids using a derivative-sign consequence of the Mean Value Theorem that is only justified in Chapter 6. Endpoint arcsine slopes are described as lacking a finite one-sided derivative, consistently with the book's derivative definition.
- **5.10: proof exercises.** The reciprocal and inverse chain-rule calculations now explicitly use previously established differentiability before differentiating their defining identities. The original prompts risked circular proofs of the very differentiability that the product/chain rules assume.
- **6.3 and 6.8: MVT corollaries.** Constant-derivative, equal-derivative, and derivative-bound statements now require continuity at included endpoints and differentiability only in the interior. This both supplies the MVT hypotheses and respects the book's convention about ordinary endpoint derivatives. Corresponding proof exercises were aligned.
- **6.4–6.8: shape tests.** The speeding-up example specifies the nonnegative time interval; increasing signed slope is distinguished from increasing steepness; the slant-asymptote definition excludes zero slope; summary and checklist text preserves the required interval, continuity, and differentiability hypotheses. Repeated Rolle applications now require three distinct zeros and explicit twice differentiability. The quadratic root-counting question is phrased for `ax^2+bx+c`, including the zero-polynomial case correctly.
- **Appendices A–C.** The fractional-power example retains its original domain; algebraic sign-chart zeros are not called derivative critical numbers; the general line-through-two-points procedure handles vertical lines; parallel lines are stated as distinct; the angle-difference proof uses an actual rotation argument; and integer periodic indices are distinguished from nonnegative whole numbers.

The exponential foundation can be checked in four steps: the square `(sqrt(F(u))-sqrt(F(v)))^2` yields the midpoint chord inequality for `F(x)=2^x`; dyadic bisection and known continuity yield all chord inequalities; these imply `1/2 <= S(h) <= S(1)=1` and monotonicity of `S(h)=(2^h-1)/h` for positive h; completeness supplies its right limit c, while `S(-h)=S(h)/2^h` supplies the same left limit. Rescaling gives `lambda(2^r)=rc`, so `e=2^(1/c)` is the unique base with slope one. This argument requires independent written proof review in addition to the computational checks below.

## Genuine live visual inspection

Inspected every sheet under `live-before/contacts/early/`:

- `figure/01.png` through `figure/11.png`: **all 125 figures**, including their 150 panels.
- `table/01.png` through `table/03.png`: **all 35 tables**.
- `opening/01.png` through `opening/07.png`: **all 79 assigned chapter, appendix, and section page openings**, with examples and hints expanded by the capture sweep.

Also inspected the full-size live captures of `fig-inverse-slopes-reciprocal`, `fig-x-cubed-inverse-vertical`, and `fig-arcsin-reflection` to distinguish true legend occlusion from sticky navigation capture artifacts. The in-plot legends really obscure curves and, in one case, the marked point and tangent; they are now moved below the graph.

Other visual corrections include:

- The nested-interval picture for sqrt(2) no longer pretends to use a single common scale while placing sqrt(2) halfway between 1.4 and 1.5. Each row has a clearly declared independent zoom and the correctly calculated relative root position.
- The sine-limit picture now contains the missing chord AP, so the small triangle used in its area proof is actually drawn. Its labeled circle point and tangent intersection use trigonometric coordinates rather than inconsistent rounded coordinates.
- The square-root tangent guide no longer runs below the plot into whitespace; its start matches the plot's actual lower boundary.
- The derivative concept-map arrow no longer crosses a box, direction annotations no longer sit on the position curve, and the circle radius label is attached to its radius segment.
- Inverse-function reflection plots use equal coordinate scales. Appendix C's legends were moved clear of its curves as well.
- The corner/cusp sample grids contain zero, and hyperbola branches meet their actual vertices.
- Quartic inflection points use filled diamonds rather than open circles suggesting missing points. Genuine missing-point circles have opaque white interiors, and interval endpoints are drawn after their interval line so excluded endpoints stay visibly open.
- Increasing-branch point labels use exact point coordinates and `anchor=west`, following `.cursor/rules/tikz-point-labels.mdc`.
- Appendix C's special-angle table no longer prints literal `\text{undefined}` in an ordinary text cell. A separated optional `[2mm]` array spacing argument is joined to its row break in 1.7 so it cannot become a literal HTML row.

The **44 affected figure IDs** are listed in [early-changed-figures.json](early-changed-figures.json). These IDs were regenerated and inspected in the corrected local captures described below. Cached SVGs were not used to judge source repairs.

## Verification and handoff

- All 79 owned source files parse as XML after the corrections.
- [early-mathematical-checks.json](early-mathematical-checks.json): **59 exact symbolic/arithmetic checks, zero failures**, including the corrected trip, rectangle sums, worked derivatives, implicit second derivatives, conic completions, trigonometric identities, and the algebra supporting the new proof estimates.
- [early-numeric-equalities.json](early-numeric-equalities.json): **242 adjacent purely numeric equality pairs checked, zero mismatches**. The parser deliberately skips symbolic and unsupported TeX rather than guessing; this supplements the full manual reading.
- Full XInclude/schema validation, regeneration, HTML compilation, corrected local browser review, Git synchronization, and live publication are handled by the root audit workflow. This report does not claim those publication steps have already passed.

No known substantive error remains in the assigned source review. Integration and final visual checks are recorded below; no remaining issue was found in the assigned material.


## Corrected local HTML visual review

The final local browser sweep at `http://127.0.0.1:54532/` was reviewed after all workers completed, and contact sheets were regenerated from the completed results. Inspected every sheet in `local-final/contacts/early/`: figure `01.png`–`11.png` (**125 figures**), table `01.png`–`03.png` (**35 tables**), array `01.png`–`07.png` (**75 displayed arrays and related structured mathematics**), and opening `01.png`–`08.png` (**88 pages: 70 sections, nine division contents pages, and nine separate introductions**). Also generated and reviewed `live-before-extra/contacts/early/opening/01.png`, covering all nine original live chapter/appendix introduction chunks that were absent from the first canonical opening sweep.

The corrected nested-interval scale, trip rectangle label, true open markers, corner/cusp samples, sine-limit chord, inverse-graph scales and external legends, hyperbola vertices, quartic inflection markers, and special-angle table all render correctly in the local captures. The corrected 1.7 array row spacing produces no literal `[2mm]`; the 2.4 transformation array renders its nested mathematical axis names correctly. No displayed-array or table rendering defect remains in the reviewed material.

Full-size inspection revealed two remaining label collisions: `(4,2)` and “tangent line” in `fig-sqrt-local-linear`, and the center `(2,-3)` and radius `r=5` in `fig-appendix-circle-center-radius`. After coordinating with the root reviewer, moved the tangent description down/right and the radius description below its actual segment. Both repairs are journaled. The root workflow regenerated both components and rebuilt the HTML. Their full-size `local-followup` captures were inspected: the descriptions and coordinate labels are now clearly separated. Apparent missing first letters in reduced table contact tiles were checked against the full-size 3.7 table capture and are reduction artifacts, not source defects.

Compact capture counts, exact sheet lists, full-size inspection paths, and repair status are recorded in [early-local-visual.json](early-local-visual.json). No additional local rendering issue was found. Final visual closure is complete: both corrected component recaptures are clear, and no further source edit is needed.


Final component confirmation: inspected `local-followup/screenshots/sec-4-4-local-linear-approximation/figure-fig-sqrt-local-linear.png` and `local-followup/screenshots/sec-b-2-circles/figure-fig-appendix-circle-center-radius.png` at full size after regeneration and the successful rebuilt HTML check. Both label collisions are resolved. All 44 changed figures are covered by the corrected local review. No known mathematical, logical, pedagogical, organizational, or visible typesetting issue remains from this assigned review.
