from audit_edit import replace
replace('chapters/ch13*/sections/sec-13-7-*.xml',r'\node[anchor=south west] at (axis cs:0.15,3) {\(y=3\cos(2t)\)};',r'\node[anchor=south west] at (axis cs:1.0,3.1) {\(y=3\cos(2t)\)};','Separate the oscillation formula from the vertical-axis label')
replace('chapters/ch13*/sections/sec-13-6-*.xml',r'\node[anchor=west] at (axis cs:52,20.4) {equilibrium \(20\) grams};',r'\node[anchor=west] at (axis cs:52,22.2) {equilibrium \(20\) grams};','Separate the equilibrium annotation from the solution curve')
