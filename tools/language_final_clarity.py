"""Final wording refinements found while reviewing the printed manuscript."""
from language_audit import replace, opening

reason = 'State the failed hypothesis or undefined operation directly.'
replace('sec-3-6-two-theorems-about-continuous-functions', reason,
        'A function that jumps from <m>0</m> to <m>2</m> can miss the intermediate value <m>1</m> even on a closed interval. In your own words, why is continuity not decoration, and what illegal move would it be to apply the theorem to a graph with a break?',
        'A function that jumps from <m>0</m> to <m>2</m> can miss the intermediate value <m>1</m> even on a closed interval. Explain which hypothesis of the Intermediate Value Theorem fails and why its conclusion need not hold.')
replace('sec-3-7-warning-examples', reason,
        '<title>What illegal use of the Intermediate Value Theorem do the warnings protect against?</title>',
        '<title>Which hypothesis of the Intermediate Value Theorem must be checked?</title>')
replace('sec-3-9-chapter-review-and-discovery-problems', reason,
        'The Intermediate Value Theorem and the Extreme Value Theorem guarantee that answers exist; they do not usually compute those answers. In your own words, which hypotheses must be checked before using each theorem, and why is a true theorem still illegal to apply when a condition is missing?',
        'The Intermediate Value Theorem and the Extreme Value Theorem guarantee existence under stated hypotheses. List the hypotheses of each theorem and give a counterexample showing why a missing hypothesis can invalidate its conclusion.')
replace('sec-13-9-warning-examples', reason,
        'That division may be illegal at some values of the solution.  Those values often give',
        'Division is undefined when the factor is zero. Those values often give')
replace('sec-14-9-warning-examples', reason,
        'The parametric slope formula is illegal when both derivatives vanish, and the same warning applies to polar curves. In your own words, what different geometric behaviors can hide behind that <m>0/0</m>, and what extra tools can distinguish them?',
        'When both parametric derivatives vanish, the slope quotient is undefined. The same issue occurs for polar curves. Describe the different tangent behaviors that can occur and the limits or expansions that can distinguish them.')
replace('sec-12-6-computing-experiments', 'Identify the accuracy assumption without referring to a promise.',
        'A more powerful rule always gives its promised error behavior.',
        'A higher-order rule always achieves its stated convergence order.')
replace('sec-2-2-completeness-and-the-idea-of-no-gaps', 'Replace the vague claim about completeness with its specific role.',
        'We will not mention completeness every time we take a limit. But it is quietly underneath the whole subject. It is what lets the language of “as close as we want” point to an actual number.',
        'A gap in the number system can prevent these approximations from having a limit within that system.')
opening('sec-15-9-chapter-review-and-discovery-problems',
        'Shorten the test list and avoid an overfull line in the printed introduction.',
        '<p>These problems distinguish sequence limits from series sums and apply the convergence tests developed in this chapter. State the hypotheses of the selected test and explain why they hold.</p>')
