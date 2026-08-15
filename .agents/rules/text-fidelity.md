# Mandatory Rule: 100% Verbatim Text Fidelity

**CRITICAL INSTRUCTION**: Under NO circumstances may the original LaTeX text be shortened, condensed, summarized, abridged, omitted, or altered without explicit maintainer directive.

1. **Full Text Preservation**:
   - Every single paragraph, sentence, word, explanation, motivation, narrative remark, question, calculation step, derivation, and note present in the original LaTeX files (`Single_Variable_Calculus_Change__Accumulation__and_Approximation/chapters/*.tex`) MUST be converted into PreTeXt XML.
   - Do NOT summarize or condense long prose passages. Convert each paragraph into its corresponding `<p>...</p>`.
   - Do NOT omit intermediate algebraic steps, comments within derivations, or pedagogical remarks.
   - All `quote`, `remark`, `example`, `theorem`, `proof`, `definition`, and discussion blocks must retain their full original text.

2. **No Editorial Alterations**:
   - The author's voice, explanations, pedagogical style, and narrative flow must be strictly preserved word-for-word.
   - The only transformations allowed are semantic markup translations (e.g. `\textbf` / `\emph` -> `<em>` or `<term>`, `\[...\]` -> `<md>`, TikZ -> `<latex-image>`, `\section` / `\subsection` -> `<section>` / `<subsection>`).
