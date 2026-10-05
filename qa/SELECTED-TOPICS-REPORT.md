# Selected topics implemented in the PreTeXt edition

The four main topics and six optional topics requested by the maintainer have been written as original explanations with definitions, formulas, proofs or derivations, worked examples, counterexamples, and exercises with hints. The separate original LaTeX edition is excluded from the changes.

## Main material

| Topic | Location | Content |
| --- | --- | --- |
| Inverse hyperbolic functions | 5.8 and 11.3 | All six real branches; domains and ranges; logarithmic forms; derivative derivations; endpoint restrictions; scaled integral patterns, including negative branches; integrals of inverse functions. |
| Improper absolute and conditional convergence | 11.7 | Absolute convergence implies convergence; sine-tail integration by parts and remainder bound; divergence of unsigned lobe area; a singular oscillatory substitution; distinction from principal value. |
| Cauchy criteria | 15.1 and 15.2 | Definitions with all-index quantifiers; completeness proof using tail bounds; series-tail criterion; adjacent-step and harmonic-tail counterexamples. |
| Dirichlet and Abel tests | 15.6 | Finite summation by parts; proofs; trigonometric bounded partial sums; monotone factors with zero and nonzero limits; hypothesis failures. |

The main section numbers were preserved by adding subsections, so existing section references retain their meaning.

## Additional topics

These sections are explicitly headed **Additional topics** and placed after each chapter's core review.

| Topic | Section | Content |
| --- | --- | --- |
| Richardson and Romberg | 12.8 | Error expansion, cancellation derivation, Romberg recurrence, sample reuse, exact quartic table, stopping policy and smoothness limits. |
| Adaptive quadrature | 12.9 | Complete executable stack-based Simpson routine, divided absolute budgets, sample reuse, evaluation/depth limits, finite-value and midpoint checks, roundoff indicator, explicit failures, aliasing example, and a derivative-bound route to certification. |
| Runge–Kutta | 13.11 | Euler, Heun, midpoint, and RK4; correct stage times and states; local/global orders; propagation estimate; reproducible errors; equal-cost comparison and a stability counterexample. |
| Contraction iteration | 15.10 | Complete metric spaces and self-maps; general contraction theorem with proof; a priori, a posteriori, and residual bounds; inexact steps; scalar examples and failure of completeness or strict contraction. |
| Weierstrass M-test | 16.11 | Uniform function-series definition; majorant theorem and proof; tail bounds; continuity and integration consequences; limits of differentiation and necessity. |
| Local ODE existence and uniqueness | 17.8 | Rectangle, bounded slope, uniform Lipschitz condition, explicit admissible interval; complete uniform-function space; Picard contraction proof and estimates; failure of uniqueness, failure of existence, nonnecessary Lipschitz condition, and finite-time blow-up. |

The ODE proof is placed after the Cauchy, contraction, and uniform-convergence material it uses. A forward link from the core ODE warning section and the frontmatter reading guide make that placement explicit. It requires no complex-number material. Appendix F links to the new main formulas and optional tests; the series-test strategy table includes Dirichlet and Abel.

Four new vector figures show inverse branches, signed improper-integral lobes, contraction cobweb steps, and nonunique waiting solutions. The adaptive implementation printed in the book is checked against its executable version in `tools/selected_numerical_methods.py`.

## Accuracy distinctions

Difference-based Richardson, Romberg, and adaptive-Simpson quantities are identified as error estimates. They are not presented as certificates for arbitrary functions. The adaptive routine returns success only when its indicator budget is met and safeguards permit it; numerical failure is explicit. A separate derivative-bound variant explains what is needed for rigorous exact-arithmetic certification and notes the additional floating-point obligations.

The [language audit](LANGUAGE-AUDIT.md) replaces vague introductions and figurative filler while preserving mathematical and visual content. [MISSING-TOPICS.md](MISSING-TOPICS.md) now records the implemented topics and the four proposals still awaiting a decision.

## References consulted

The development is original prose and original examples, rather than a reproduction of source text or figures. These primary educational references were consulted to cross-check standard formulas and method conventions:

- [OpenStax, Calculus Volume 2, Section 2.9](https://openstax.org/books/calculus-volume-2/pages/2-9-calculus-of-the-hyperbolic-functions), the reference supplied by the maintainer; also linked in the inverse-hyperbolic subsection.
- [Joel Feldman, UBC: Richardson Extrapolation and Romberg Integration](https://personal.math.ubc.ca/~feldman/m101/richard.pdf).
- [UBC CLP-2: Adaptive Quadrature](https://personal.math.ubc.ca/~CLP/CLP2/clp_2_ic/ap_adaptive.html).
- [NTNU: Numerical Methods for Engineers](https://leifh.folk.ntnu.no/teaching/tkt4140/._main019.html).
- [Brown University: Existence and Uniqueness](https://www.cfm.brown.edu/people/dobrush/am33/Mathematica/intro/exist.html).

## Verification

The final builds pass: 188 section pages, 28 supplemental pages, 592 opened hints, and 103 mathematical/numerical checks, with no failures. The 1,448-page PDF has no text outside the physical page and no overfull boxes of 12 points or more. All new material and chapter/appendix openings were inspected in 58 rendered pages. Final build and verification receipts are recorded in `qa/additions/final-validation.json`. The repeatable mathematical checks are `python tools/verify_selected_topics.py`; these supplement the existing `python tools/audit_numerics.py`. Browser checks cover all sections and opened hints. Print checks scan every page for physical overflow and inspect the new material visually.

The earlier complete audit receipt in `qa/audit/final-validation.json` is retained as history for the pre-addition version. The additions receipt identifies the current source hashes and PDF. The existing local toolchain limitations remain: CLI/project versions differ, the publication schema is older than the functioning HTML configuration, and the native Asymptote print renderer uses the documented verified static sphere export.
