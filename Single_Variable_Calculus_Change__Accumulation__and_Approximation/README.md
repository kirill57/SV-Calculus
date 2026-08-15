# Single-Variable Calculus — Book Template

LaTeX template for a single-variable calculus textbook organised
around two animating questions (slope and area) and the seven-tag
pedagogy system from the table of contents:

    Core | Bridge | Proof | Counterexample | Computing | Optional | Project

This is a **template only**: the chapter and appendix files contain
the full hierarchy of `\chapter`, `\section`, and `\subsection`
commands, with margin tags and `\label`s in place, but no prose.
Drop your content into each `\subsection`.

---

## Project layout

    .
    ├── main.tex                    Master file with parts, chapter \input's
    ├── preamble.tex                Packages, page geometry, theorem envs
    ├── commands.tex                Custom commands, including \sectag and
    │                               the seven tag aliases (\Core, \Bridge, …)
    ├── bibliography.bib            BibTeX stub
    ├── frontmatter/
    │   ├── titlepage.tex
    │   ├── preface.tex             [TODO]
    │   └── howtoread.tex           [TODO]
    ├── chapters/
    │   ├── ch01-velocity-distance.tex
    │   ├── ch02-numbers-functions.tex
    │   ├── ch03-limits-continuity.tex
    │   ├── ch04-derivative.tex
    │   ├── ch05-differentiation-rules.tex
    │   ├── ch06-shape-extremes.tex
    │   ├── ch07-optimization.tex
    │   ├── ch08-integral-accumulation.tex
    │   ├── ch09-fundamental-theorem.tex
    │   ├── ch10-what-integrals-measure.tex
    │   ├── ch11-techniques-integration.tex
    │   ├── ch12-numerical-integration.tex
    │   ├── ch13-differential-equations.tex
    │   ├── ch14-parametric-polar.tex
    │   ├── ch15-sequences-series.tex
    │   ├── ch16-power-series.tex
    │   └── ch17-complex-fourier.tex
    ├── appendices/
    │   ├── appA-algebra.tex
    │   ├── appB-coordinate-geometry.tex
    │   ├── appC-trigonometry.tex
    │   ├── appD-proofs.tex
    │   ├── appE-technology.tex
    │   └── appF-tables.tex
    └── figures/                    (drop .pdf / .png figures here)

---

## Building

### On Overleaf

1. Upload the entire zip via *New Project → Upload Project*.
2. Set the **Main document** to `main.tex` (Menu → Settings).
3. Set the **Compiler** to **pdfLaTeX** (Menu → Settings).
4. Press *Recompile*. Overleaf iterates the run automatically, so the
   table of contents, cross-references, bibliography, and index all
   resolve after a couple of recompiles.

### Locally

Standard pdfLaTeX with BibTeX and makeindex:

    pdflatex main
    bibtex   main
    makeindex main
    pdflatex main
    pdflatex main

### Switching to biblatex + biber

In `preamble.tex`, comment back in the two biblatex lines and remove
the `\bibliographystyle{plain}` / `\bibliography{bibliography}` pair
in `main.tex`, replacing them with `\printbibliography`.

---

## The tag system

Margin tags are produced by `\sectag{…}`, defined in `commands.tex`.
Seven aliases shorten the common cases:

    \Core              \Bridge            \Proof
    \Counter           \Computing         \Optional
    \Project

Combinations have aliases too — e.g. `\CoreProof`, `\CoreBridge`,
`\ComputingProject`, `\OptionalBridge`. For arbitrary combinations,
use the raw `\sectag{Core / Optional}` form, as in the example for
section 5.8 ("General power rule and hyperbolic functions").

Place the tag immediately after `\section{…}`:

    \section{The dashboard: speedometer and odometer}\Core

For tags on individual `\subsection`s (the chapter-end review
problems use these), the same convention applies.

---

## Theorem environments

Provided in `preamble.tex` and numbered within each chapter:

    theorem    proposition   lemma       corollary
    definition example       exercise    problem
    counterexample (own colour)
    remark     note          warning     (unnumbered)

`theorem`, `proposition`, `lemma`, `corollary`, `definition`,
`example`, and `counterexample` share a counter, so the numbering
threads naturally through a chapter.

---

## Cross-referencing

Every section and subsection in the template carries a `\label`
following the conventions:

    sec:slug                     for sections
    subsec:slug                  for subsections
    ch:slug                      for chapters
    app:slug                     for appendices

Use `\Cref{ch:derivative}` (capitalised) or `\cref{sec:eulers-method}`
(lowercase) for self-formatting cross-references.

---

## Typical first edits

  - Set the author and affiliation in `frontmatter/titlepage.tex` and
    in the `\author` field of `main.tex`.
  - Write the preface in `frontmatter/preface.tex`.
  - Decide whether to expose `subsubsection` numbering by raising
    `secnumdepth` in `preamble.tex`.
  - If margin tags feel too loud, change `\sectag` in `commands.tex`
    to a less prominent style (e.g. drop the `\fbox`).
