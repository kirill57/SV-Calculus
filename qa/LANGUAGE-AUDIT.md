# PreTeXt language audit

Reviewed all 17 chapter openings, all 188 section openings (including six new optional sections and appendix sections), the six appendix introductions, the frontmatter, and flagged explanatory prose, exercise statements, hints, and captions throughout the source. Retained direct, useful prose; replaced figurative filler, repetitive setup, unsupported generalizations, and vague claims.

The pass records **392 corrections across 173 source files**. The formulas, worked examples, exercises, tables, and diagrams remain; introductions were shortened where repeated setup obscured the concept. Embedded figures and tables were explicitly preserved during opening rewrites.

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
