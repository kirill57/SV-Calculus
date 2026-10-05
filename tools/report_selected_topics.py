"""Write the maintainer-facing implementation and language audit reports."""
from pathlib import Path
from lxml import etree as E
from html import unescape
import json, re, hashlib
ROOT=Path(__file__).resolve().parents[1];QA=ROOT/'qa/additions'
records=[json.loads(l) for l in (QA/'language-changes.jsonl').read_text('utf-8').splitlines()]
# Remove duplicate receipts from interrupted one-time authoring attempts.
unique={}
for r in records:unique[(r['file'],r['before'],r['after'])]=r
records=list(unique.values())
(QA/'language-changes.jsonl').write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in records),encoding='utf-8')
files=sorted({r['file'] for r in records})
def prose(text):
    text=re.sub(r'<xref[^>]*/>','[cross-reference]',text)
    return ' '.join(unescape(re.sub(r'<[^>]+>','',text)).split())
doc=E.parse(str(ROOT/'source/main.ptx'));doc.xinclude()
titles={el.get('{http://www.w3.org/XML/1998/namespace}id'):''.join(el.find('title').itertext())
        for el in doc.iter() if isinstance(el.tag,str) and el.find('title') is not None}
full=['# Language corrections: complete before-and-after record','',
      'Scope: the PreTeXt edition only. Each item records a flagged passage and its replacement. Formula notation is retained in TeX form in this review document.','']
for i,r in enumerate(records,1):
    full.extend([f"## {i}. {titles.get(r['id'],r['id'])}",'',
                 f"Source: [{r['file']}](../../{r['file']})",'',f"Flag: {r['flag']}",'',
                 '**Before**','', '> '+prose(r['before']),'','**After**','',prose(r['after']),''])
(QA/'LANGUAGE-CHANGES.md').write_text('\n'.join(full),encoding='utf-8')
overview=f'''# PreTeXt language audit

Reviewed all 17 chapter openings, all 188 section openings (including six new optional sections and appendix sections), the six appendix introductions, the frontmatter, and flagged explanatory prose, exercise statements, hints, and captions throughout the source. Retained direct, useful prose; replaced figurative filler, repetitive setup, unsupported generalizations, and vague claims.

The pass records **{len(records)} corrections across {len(files)} source files**. The formulas, worked examples, exercises, tables, and diagrams remain; introductions were shortened where repeated setup obscured the concept. Embedded figures and tables were explicitly preserved during opening rewrites.

The changes favor definitions, operations, domains, hypotheses, and concrete questions over references to promises, stories, magic, surprises, or the supposed personality of a function or method. Ordinary meaningful uses, such as a farmer wanting to enclose a field or pressure increasing with depth, were retained.

## Representative flags

| Passage | Issue | Replacement approach |
| --- | --- | --- |
| Section 3.7: “Continuity gave us two promises…” | Vague framing and an unnecessary claim about using theorems “illegally.” | State the continuity and interval hypotheses, then explain what the counterexamples test. |
| Chapter 6: “the graph wants to rise” | Personification obscures the mathematical condition. | Describe how derivative signs determine monotonicity on intervals. |
| Chapter 12: “a practical confession” | Dramatic setup gives no additional information. | State what numerical methods approximate and what their error analysis requires. |
| Sequence explanations: “friendly,” “generous,” and “honest” | Labels replace explanations of convergence or error control. | Identify explicit partial sums, convergence hypotheses, and remainder bounds. |
| Logistic models: “constant early relative growth” | Overstates an approximation. | Give the actual relative rate r(1-P/K), approximately r when P is much smaller than K. |
| Numerical methods: “wrong story” | Does not identify the discrepancy. | State that computed oscillation or growth contradicts the exact solution or direction field. |
| Appendix introductions: “repair bench,” “quiet promise,” “a table is a map” | General metaphors delay the scope of the material. | State the tools or proofs the appendix provides and how to use them. |

The [complete before-and-after record](additions/LANGUAGE-CHANGES.md) lists every flagged passage and replacement. The [machine-readable journal](additions/language-changes.jsonl) retains the exact source markup. One-time authoring scripts in `tools/language_round_*.py` document the edits and are not normal build commands.

Markup, mathematical rendering, and print-layout verification are recorded with the [selected-topic implementation](SELECTED-TOPICS-REPORT.md).
'''
(ROOT/'qa/LANGUAGE-AUDIT.md').write_text(overview,encoding='utf-8')
(ROOT/'qa/MISSING-TOPICS.md').write_text('''# Topic decisions

The ten topics selected by the maintainer have been implemented in the PreTeXt edition. Their locations and validation are recorded in [SELECTED-TOPICS-REPORT.md](SELECTED-TOPICS-REPORT.md).

## Implemented as main material

- Inverse hyperbolic functions, their real branches, derivatives, and integrals.
- Absolute and conditional convergence of improper integrals, with oscillatory examples.
- The Cauchy criterion for sequences and series.
- Dirichlet's and Abel's tests for series.

## Implemented as additional topics

- The Weierstrass M-test.
- Local existence and uniqueness for differential equations, with a Lipschitz condition and counterexamples.
- Runge–Kutta methods and accuracy comparisons with Euler methods.
- Richardson extrapolation and Romberg integration.
- A complete adaptive quadrature algorithm, stopping rule, and safeguards.
- Contraction-based fixed-point iteration and error estimates.

## Still proposed; not added

- Curvature, osculating circles, and arc-length parametrization.
- Subsequences and the Bolzano–Weierstrass theorem.
- Darboux's theorem for derivatives.
- Abel's limit theorem and a fuller treatment of endpoint power-series identities.
''',encoding='utf-8')
report='''# Selected topics implemented in the PreTeXt edition

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

Final build and verification receipts are recorded in `qa/additions/final-validation.json`. The repeatable mathematical checks are `python tools/verify_selected_topics.py`; these supplement the existing `python tools/audit_numerics.py`. Browser checks cover all sections and opened hints. Print checks scan every page for physical overflow and inspect the new material visually.

The earlier complete audit receipt in `qa/audit/final-validation.json` is retained as history for the pre-addition version. The additions receipt identifies the current source hashes and PDF. The existing local toolchain limitations remain: CLI/project versions differ, the publication schema is older than the functioning HTML configuration, and the native Asymptote print renderer uses the documented verified static sphere export.
'''
(ROOT/'qa/SELECTED-TOPICS-REPORT.md').write_text(report,encoding='utf-8')
p=ROOT/'README.md';text=p.read_text('utf-8')
before='The completed PreTeXt audit is documented in [qa/PRETEXT-AUDIT-REPORT.md](qa/PRETEXT-AUDIT-REPORT.md). Proposed additional topics are listed in [qa/MISSING-TOPICS.md](qa/MISSING-TOPICS.md); they have not been added. The separate original LaTeX edition was preserved.'
after='The complete PreTeXt audit is documented in [qa/PRETEXT-AUDIT-REPORT.md](qa/PRETEXT-AUDIT-REPORT.md). The ten selected additions are documented in [qa/SELECTED-TOPICS-REPORT.md](qa/SELECTED-TOPICS-REPORT.md), and the subsequent language revisions in [qa/LANGUAGE-AUDIT.md](qa/LANGUAGE-AUDIT.md). [qa/MISSING-TOPICS.md](qa/MISSING-TOPICS.md) lists the four remaining proposals. The separate original LaTeX edition was preserved.'
if before in text:p.write_text(text.replace(before,after),encoding='utf-8')
print('Language corrections:',len(records),'source files:',len(files))
