# LaTeX Source Inventory

- Source root: `/workspaces/SV-Calculus/Single_Variable_Calculus_Change__Accumulation__and_Approximation`
- Files scanned: 29
- Numbered section commands detected: 186
- Numbered subsection commands detected: 935
- Unnumbered section commands detected: 7
- Unnumbered subsection commands detected: 50
- Figure environments: 325
- TikZ pictures: 368
- PGFPlots axes: 278
- Explicit true-3D figure environments: 3
- Semantic 3D review candidates: 7
- Duplicate labels: 15
- Source references with no detected label: 0

## Section-count comparison

| File | Ch. | Actual | Planned | Match | Duplicate titles |
|---|---:|---:|---:|---|---|
| `appendices/appA-algebra.tex` |  | 6 |  |  |  |
| `appendices/appB-coordinate-geometry.tex` |  | 6 |  |  |  |
| `appendices/appC-trigonometry.tex` |  | 6 |  |  |  |
| `appendices/appD-proofs.tex` |  | 6 |  |  |  |
| `appendices/appE-technology.tex` |  | 6 |  |  |  |
| `appendices/appF-tables.tex` |  | 5 |  |  |  |
| `chapters/ch01-velocity-distance.tex` |  | 7 |  |  |  |
| `chapters/ch02-numbers-functions.tex` |  | 9 |  |  |  |
| `chapters/ch03-limits-continuity.tex` |  | 10 |  |  | Chapter review and discovery problems |
| `chapters/ch04-derivative.tex` |  | 9 |  |  |  |
| `chapters/ch05-differentiation-rules.tex` |  | 11 |  |  | Derivatives of trigonometric functions |
| `chapters/ch06-shape-extremes.tex` |  | 8 |  |  |  |
| `chapters/ch07-optimization.tex` |  | 9 |  |  |  |
| `chapters/ch08-integral-accumulation.tex` |  | 8 |  |  |  |
| `chapters/ch09-fundamental-theorem.tex` |  | 7 |  |  |  |
| `chapters/ch10-what-integrals-measure.tex` |  | 9 |  |  |  |
| `chapters/ch11-techniques-integration.tex` |  | 9 |  |  |  |
| `chapters/ch12-numerical-integration.tex` |  | 7 |  |  |  |
| `chapters/ch13-differential-equations.tex` |  | 10 |  |  |  |
| `chapters/ch14-parametric-polar.tex` |  | 10 |  |  |  |
| `chapters/ch15-sequences-series.tex` |  | 9 |  |  |  |
| `chapters/ch16-power-series.tex` |  | 10 |  |  |  |
| `chapters/ch17-complex-fourier.tex` |  | 7 |  |  |  |
| `commands.tex` |  | 2 |  |  | Title |

## True-3D figures

| File | Line | Label | Signals | Caption |
|---|---:|---|---|---|
| `chapters/ch10-what-integrals-measure.tex` | 754 | `fig:volume-by-slicing-loaf` | \addplot3; 3D axis view; z-axis limits; z-buffer; surface/mesh axis | Volume by slicing: a differential slice of thickness \(\Delta x\) has volume approximately \(A(x)\Delta x\). |
| `chapters/ch10-what-integrals-measure.tex` | 1011 | `fig:disk-method-sqrtx` | \addplot3; 3D axis view; z-axis limits; z-buffer; surface/mesh axis | Rotating the region under \(y=\sqrt{x}\) around the \(x\)-axis gives disk slices. |
| `chapters/ch10-what-integrals-measure.tex` | 1439 | `fig:disk-method-y-axis` | \addplot3; 3D axis view; z-axis limits; z-buffer; surface/mesh axis | Rotating around the \(y\)-axis suggests horizontal slices and an integral in \(y\). |

## Duplicate labels

- `fig:chapter3-concept-map` — `chapters/ch03-limits-continuity.tex:5070`, `chapters/ch03-limits-continuity.tex:5906`
- `fig:chapter3-graph-reading-review` — `chapters/ch03-limits-continuity.tex:5350`, `chapters/ch03-limits-continuity.tex:6186`
- `fig:logistic-phase-line` — `chapters/ch07-optimization.tex:3980`, `chapters/ch13-differential-equations.tex:919`
- `fig:multiply-by-i-rotation` — `chapters/ch14-parametric-polar.tex:6620`, `chapters/ch17-complex-fourier.tex:575`
- `fig:sin-h-over-h-geometry` — `chapters/ch05-differentiation-rules.tex:3139`, `chapters/ch05-differentiation-rules.tex:4842`
- `fig:sine-derivative-cosine` — `chapters/ch05-differentiation-rules.tex:3368`, `chapters/ch05-differentiation-rules.tex:5128`
- `sec:chapter3-review-discovery` — `chapters/ch03-limits-continuity.tex:5016`, `chapters/ch03-limits-continuity.tex:5852`
- `subsec:bisection-project` — `chapters/ch03-limits-continuity.tex:5574`, `chapters/ch03-limits-continuity.tex:6410`
- `subsec:chapter3-decision-guide` — `chapters/ch03-limits-continuity.tex:5080`, `chapters/ch03-limits-continuity.tex:5916`
- `subsec:chapter3-hook-to-derivative` — `chapters/ch03-limits-continuity.tex:5838`, `chapters/ch03-limits-continuity.tex:6674`
- `subsec:chapter3-one-picture` — `chapters/ch03-limits-continuity.tex:5030`, `chapters/ch03-limits-continuity.tex:5866`
- `subsec:chapter3-review-problems` — `chapters/ch03-limits-continuity.tex:5109`, `chapters/ch03-limits-continuity.tex:5945`
- `subsec:monotone-bounded-sequences` — `chapters/ch03-limits-continuity.tex:4613`, `chapters/ch15-sequences-series.tex:595`
- `subsec:secant-slope-discovery` — `chapters/ch03-limits-continuity.tex:5717`, `chapters/ch03-limits-continuity.tex:6553`
- `subsec:sequence-convergence-divergence` — `chapters/ch03-limits-continuity.tex:4358`, `chapters/ch15-sequences-series.tex:235`

## Required human review

- Compare source section order with the authoritative TOC.
- Inspect every semantic 3D candidate; explicit-command detection is not sufficient.
- Review uppercase/custom-command candidates for undefined editorial macros.
- Confirm that unresolved source references are not defined in an external included file.
- Record resolutions without editing the LaTeX source.
