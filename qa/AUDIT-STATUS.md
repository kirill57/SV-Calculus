# Latest PreTeXt audit

The complete 17 October 2026 source and HTML audit is documented in [AUDIT-2026-10-17.md](AUDIT-2026-10-17.md). It covers all 17 chapters, Appendices A–F, all 188 sections, 614 worked examples, 592 exercises and hints, 327 figures, 159 tables, and 112 displayed arrays. Source and live-browser review was followed by corrections, a local HTML build, full rendered verification, and a release comparison against the published files.

[audit-2026-10-17/final-validation.json](audit-2026-10-17/final-validation.json) records the validated source fingerprint and HTML hashes. Exact before/after journals and detailed reviews are linked from the report. The [live build record](https://kirill57.github.io/SV-Calculus/audit-build.json) identifies the published source commit and file hashes. The original LaTeX edition's 34 files remain unchanged.

The earlier audit, ten selected additions, and language pass below are retained as dated history. Their PDF verification applies to their earlier print build; this latest round validates HTML.

## Earlier audit, additions, and language pass — 5 October 2026

Completed 5 October 2026. Scope: the PreTeXt edition, its figures, HTML, and PDF print rendering. The separate original LaTeX edition is preserved: all 34 files match their starting SHA-256 hashes.

The initial complete audit covers all 17 chapters and Appendices A–F. The four selected main topics and six additional topics are implemented with explanations, proofs or derivations, examples, counterexamples, exercises, and hints. Their locations are in [SELECTED-TOPICS-REPORT.md](SELECTED-TOPICS-REPORT.md).

The subsequent language pass reviewed all chapter and section openings, appendix introductions, frontmatter, and flagged prose throughout the book. It records 392 corrections across 173 source files. [LANGUAGE-AUDIT.md](LANGUAGE-AUDIT.md) explains the flags and links to every before-and-after replacement.

Final verification passed: manuscript schema, XML assembly, IDs and references, math grouping, all 188 section pages and 28 supplemental pages in desktop/mobile browsers, and all 592 opened hints. The 40 existing numerical/code checks and 63 new mathematical/numerical checks pass. The interactive and embedded sphere render correctly. Four new vector figures were inspected visually.

The final 1,448-page PDF has no text outside physical page boundaries and no overfull boxes of 12 points or more. Every page of the new material and all chapter and appendix openings were rendered; 58 selected pages were inspected visually.

Current source and PDF hashes and verification results are in [additions/final-validation.json](additions/final-validation.json). The initial audit receipt in `audit/final-validation.json` is retained as history. [PRETEXT-AUDIT-REPORT.md](PRETEXT-AUDIT-REPORT.md) records the initial corrections and local toolchain limitations.

[MISSING-TOPICS.md](MISSING-TOPICS.md) records the ten implemented topics and four remaining proposals awaiting a later decision.
