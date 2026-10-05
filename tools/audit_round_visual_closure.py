import sys
sys.path.insert(0,'tools')
from audit_edit import replace
replace('chapters/ch01*/sections/sec-1-5-*.xml',r'\node[anchor=south east] at (axis cs:1.95,4.05) {\(P=(2,4)\)};',r'\node[anchor=west,fill=white,inner sep=2pt] at (axis cs:2,4) {\(P=(2,4)\)};','Place the marked point label at its actual coordinate with a clear background')
replace('chapters/ch01*/sections/sec-1-5-*.xml',r'\node[anchor=west] at (axis cs:3,9) {\(Q\)};',r'\node[anchor=west,fill=white,inner sep=2pt] at (axis cs:3,9) {\(Q_1\)};','Distinguish and clear the first secant-point label')
replace('chapters/ch01*/sections/sec-1-5-*.xml',r'\node[anchor=west] at (axis cs:2.5,6.25) {\(Q\)};',r'\node[anchor=west,fill=white,inner sep=2pt] at (axis cs:2.5,6.25) {\(Q_2\)};','Distinguish and clear the second secant-point label')
replace('chapters/ch01*/sections/sec-1-5-*.xml',r'\node[anchor=west] at (axis cs:2.5,8.9) {secants};',r'\node[anchor=west] at (axis cs:1.6,9.8) {secants};','Move a descriptive label away from the marked point')
replace('chapters/ch01*/sections/sec-1-5-*.xml',r'\node[anchor=west] at (axis cs:2.0,3.6) {tangent slope \(4\)};',r'\node[anchor=west] at (axis cs:2.0,2.6) {tangent slope \(4\)};','Separate the tangent description from the point label')
replace('chapters/ch03*/sections/sec-3-1-*.xml',r'\node[anchor=west] at (axis cs:1.0,2.8) {hole at the limiting value};',r'\node[anchor=west,fill=white,inner sep=2pt] at (axis cs:1,3) {hole at the limiting value};','Keep the hole annotation off the diagonal curve')
replace('chapters/ch03*/sections/sec-3-1-*.xml',r'\node[anchor=south west] at (axis cs:0.18,1.22) {right side approaches \(1\)};',r'\node[anchor=west] at (axis cs:0.35,0.55) {right side approaches \(1\)};','Separate the jump annotation from the vertical-axis label')
replace('chapters/ch03*/sections/sec-3-1-*.xml',r'\node[anchor=north east] at (axis cs:-0.18,-1.22) {left side approaches \(-1\)};',r'\node[anchor=east] at (axis cs:-0.35,-0.55) {left side approaches \(-1\)};','Balance the lower jump annotation inside the plot window')
replace('chapters/ch03*/sections/sec-3-5-*.xml',r'\node[anchor=west] at (axis cs:0.95,1.8) {missing point};',r'\node[anchor=west,fill=white,inner sep=2pt] at (axis cs:1,2) {missing point};','Use the exact hole coordinate and clear the label from the curve')
replace('chapters/ch14*/sections/sec-14-2-*.xml',r'\node[anchor=south east] at (axis cs:0,1) {\(t=1\)};',r'\node[anchor=west,fill=white,inner sep=2pt] at (axis cs:0,1) {\(t=1\)};','Place the increasing-curve point label to the right at the marked coordinate')
