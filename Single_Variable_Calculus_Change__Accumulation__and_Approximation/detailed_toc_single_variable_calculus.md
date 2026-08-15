# Detailed Table of Contents for a Single-Variable Calculus Book

**Working title:** *Single-Variable Calculus: Change, Accumulation, and Approximation*

This table of contents is designed for a book that can serve the standard two-semester single-variable calculus curriculum while telling a more coherent story. The scope includes the familiar Stewart-style topics, but the path is closer in spirit to Strang, Spivak, Lax--Terrell, and Courant: start with the problems calculus was invented to solve; use examples before theorems; keep applications and proof in contact; and treat approximation as a central idea rather than an afterthought.

## How to Read the Tags

- **Core** — belongs in a standard Calculus I or Calculus II course.
- **Bridge** — prepares ideas needed later, especially multivariable calculus, differential forms, differential equations, or analysis.
- **Proof** — gives a more precise theorem or proof than some standard courses require.
- **Counterexample** — shows why a theorem needs its hypotheses.
- **Computing** — uses numerical or computer-based exploration.
- **Optional** — enrichment for honors courses, projects, or later reading.
- **Project** — longer exploration, often applied or computational.

---

## Suggested Course Paths

### Standard Calculus I path

Chapters 1--9, with Chapter 10 used selectively for area and volume if time permits. A common route is:

- Chapters 1--3: velocity, functions, limits, continuity;
- Chapters 4--5: derivative and differentiation rules;
- Chapters 6--7: applications of derivatives;
- Chapters 8--9: integrals and the Fundamental Theorem;
- selected Chapter 10 sections: area between curves and volumes.

### Standard Calculus II path

Chapters 10--16, with Chapter 17 as a capstone if time permits:

- Chapters 10--12: applications and techniques of integration;
- Chapter 13: differential equations;
- Chapter 14: parametric and polar curves;
- Chapters 15--16: sequences, series, power series, and Taylor series;
- selected Chapter 17 sections: Euler's formula, Fourier preview, or bridge to multivariable calculus.

### Honors or proof-enriched path

Use all **Proof** and **Counterexample** sections, especially completeness, formal limits, proof of the Mean Value Theorem, integrability conditions, Taylor's theorem with remainder, and uniform convergence previews.

### Applied science path

Emphasize Chapters 1, 4, 7, 8, 10, 12, 13, 14, and 16. Use projects on motion, cooling, population growth, numerical integration, harmonic oscillation, and approximation.

---

# Part I. The Two Questions of Calculus

## Chapter 1. Velocity, Distance, and the First Shape of Calculus

### 1.1 The dashboard: speedometer and odometer **Core**
#### 1.1.1 Distance as accumulated motion
#### 1.1.2 Velocity as changing distance
#### 1.1.3 Units: miles, hours, miles per hour
#### 1.1.4 The first question: if we know distance, can we find velocity?
#### 1.1.5 The second question: if we know velocity, can we find distance?

### 1.2 Constant velocity: where slope and area first meet **Core**
#### 1.2.1 The graph of distance when velocity is constant
#### 1.2.2 Slope of the distance graph
#### 1.2.3 Area under the velocity graph
#### 1.2.4 Why slope and area are inverse clues

### 1.3 Forward, backward, and signed motion **Core**
#### 1.3.1 Positive and negative velocity
#### 1.3.2 Displacement versus distance traveled
#### 1.3.3 Area below the time axis
#### 1.3.4 A first piecewise-defined motion

### 1.4 Calculus without limits: finite differences and finite sums **Bridge**
#### 1.4.1 Difference tables
#### 1.4.2 Accumulated differences telescope
#### 1.4.3 Step velocities and piecewise linear distance
#### 1.4.4 The finite version of the Fundamental Theorem

### 1.5 Changing velocity and the need for limits **Core**
#### 1.5.1 Average velocity over a time interval
#### 1.5.2 Shorter intervals and better estimates
#### 1.5.3 The tangent line problem
#### 1.5.4 The area problem
#### 1.5.5 Why finite arithmetic is no longer enough

### 1.6 A first map of the book **Bridge**
#### 1.6.1 Derivative: from distance to velocity
#### 1.6.2 Integral: from velocity to distance
#### 1.6.3 Approximation: how to work when exact formulas fail
#### 1.6.4 Differential equations: when the law gives the derivative

### 1.7 Discovery problems and projects
#### 1.7.1 Read a trip from a speed graph **Project**
#### 1.7.2 Design two different trips with the same displacement **Project**
#### 1.7.3 Finite differences of squares and cubes **Bridge**
#### 1.7.4 Hook: a changing slope needs a precise language of nearness

---

## Chapter 2. Numbers, Functions, and Models

### 2.1 The real line and intervals **Core**
#### 2.1.1 Points as numbers
#### 2.1.2 Open, closed, and half-open intervals
#### 2.1.3 Absolute value as distance
#### 2.1.4 Inequalities as a way to control error

### 2.2 Completeness and the idea of no gaps **Proof/Optional**
#### 2.2.1 Rational numbers and the missing square root
#### 2.2.2 Nested intervals
#### 2.2.3 Least upper bound property
#### 2.2.4 Why calculus needs the real numbers

### 2.3 Functions as assignments **Core**
#### 2.3.1 Input, output, domain, and range
#### 2.3.2 Functions from formulas, graphs, tables, and words
#### 2.3.3 Piecewise-defined functions
#### 2.3.4 Difference quotient as a function of two inputs

### 2.4 Graphs and transformations **Core**
#### 2.4.1 Shifts and scalings
#### 2.4.2 Reflections and stretching
#### 2.4.3 Even and odd symmetry
#### 2.4.4 Reading intercepts, sign, and intervals from a graph

### 2.5 Combining functions **Core**
#### 2.5.1 Sums, products, and quotients
#### 2.5.2 Composition
#### 2.5.3 Inverse functions
#### 2.5.4 When an inverse exists

### 2.6 A catalog of essential functions **Core**
#### 2.6.1 Linear functions and units
#### 2.6.2 Powers and polynomials
#### 2.6.3 Rational functions and asymptotic behavior
#### 2.6.4 Algebraic functions
#### 2.6.5 Trigonometric functions in radians
#### 2.6.6 Exponential functions
#### 2.6.7 Logarithms as inverse functions

### 2.7 Models before calculus **Core**
#### 2.7.1 Linear growth
#### 2.7.2 Power-law scaling
#### 2.7.3 Exponential growth and decay
#### 2.7.4 Periodic motion
#### 2.7.5 Choosing a model from units and data

### 2.8 Technology and graphs **Computing**
#### 2.8.1 Windows can lie
#### 2.8.2 Sampling can miss behavior
#### 2.8.3 Numerical evidence versus proof
#### 2.8.4 A first warning about roundoff

### 2.9 Chapter review and discovery problems
#### 2.9.1 Concept check: function versus formula
#### 2.9.2 Skills: graph transformations and domains
#### 2.9.3 Project: fit a simple model to data **Project**
#### 2.9.4 Hook: limits make "near" into mathematics

---

# Part II. Limits, Continuity, and the Derivative

## Chapter 3. Limits and Continuity

### 3.1 Limits from motion and approximation **Core**
#### 3.1.1 Average velocity as the interval shrinks
#### 3.1.2 Decimal approximations to a number
#### 3.1.3 The informal meaning of a limit
#### 3.1.4 Limits from graphs and tables

### 3.2 Calculating limits **Core**
#### 3.2.1 Limit laws
#### 3.2.2 Polynomials and rational functions
#### 3.2.3 Removing a removable discontinuity
#### 3.2.4 The squeeze idea

### 3.3 One-sided limits and infinite behavior **Core**
#### 3.3.1 Left-hand and right-hand limits
#### 3.3.2 Infinite limits and vertical asymptotes
#### 3.3.3 Limits at infinity
#### 3.3.4 Horizontal and slant asymptotes

### 3.4 The precise definition of a limit **Proof**
#### 3.4.1 The epsilon challenge
#### 3.4.2 Delta as a response
#### 3.4.3 Proving simple limits
#### 3.4.4 Why the definition matches the picture

### 3.5 Continuity **Core**
#### 3.5.1 Continuity at a point
#### 3.5.2 Continuity on an interval
#### 3.5.3 Algebra of continuous functions
#### 3.5.4 Continuity of compositions
#### 3.5.5 Removable, jump, and infinite discontinuities

### 3.6 Two theorems about continuous functions **Core/Proof**
#### 3.6.1 Intermediate Value Theorem
#### 3.6.2 Bisection as a constructive proof idea
#### 3.6.3 Extreme Value Theorem
#### 3.6.4 Why closed and bounded intervals matter

### 3.7 Warning examples **Counterexample**
#### 3.7.1 A function with no limit at a jump
#### 3.7.2 A limit that is infinite, not finite
#### 3.7.3 IVT fails without continuity
#### 3.7.4 EVT fails on an open interval
#### 3.7.5 EVT fails on an unbounded interval

### 3.8 Sequences as limits indexed by whole numbers **Bridge**
#### 3.8.1 Sequence notation
#### 3.8.2 Convergence and divergence
#### 3.8.3 Monotone bounded sequences
#### 3.8.4 Sequences as preparation for infinite series

### 3.9 Chapter review and discovery problems
#### 3.9.1 Skills: compute and interpret limits
#### 3.9.2 Proof practice with epsilon and delta **Proof**
#### 3.9.3 Project: bisection method for a root **Computing/Project**
#### 3.9.4 Hook: a tangent line is a limit of secant lines

---

## Chapter 4. The Derivative

### 4.1 Average rate of change **Core**
#### 4.1.1 Secant slope
#### 4.1.2 Average velocity
#### 4.1.3 Average rate from data
#### 4.1.4 Units of a rate

### 4.2 Instantaneous rate of change **Core**
#### 4.2.1 Shrinking the time interval
#### 4.2.2 The derivative at a point
#### 4.2.3 Tangent slope
#### 4.2.4 The derivative as a limit

### 4.3 The derivative as a function **Core**
#### 4.3.1 From one tangent slope to many
#### 4.3.2 Notations: \(f'(x)\), \(dy/dx\), \(D_x f\)
#### 4.3.3 Reading \(f'\) from the graph of \(f\)
#### 4.3.4 Reading \(f\) from the graph of \(f'\)

### 4.4 Local linear approximation **Core/Bridge**
#### 4.4.1 The tangent line as a local model
#### 4.4.2 \(f(a+h)\approx f(a)+f'(a)h\)
#### 4.4.3 Differentials \(dy=f'(x)dx\)
#### 4.4.4 Sensitivity and propagated error

### 4.5 Differentiability and continuity **Core/Proof**
#### 4.5.1 Differentiability implies continuity
#### 4.5.2 Why the converse is false
#### 4.5.3 Corners, cusps, vertical tangents, and jumps
#### 4.5.4 Absolute value as the first warning example

### 4.6 First derivative formulas **Core**
#### 4.6.1 Constant and identity functions
#### 4.6.2 Power functions with positive integer powers
#### 4.6.3 Polynomials
#### 4.6.4 Constant multiples and sums, introduced by examples

### 4.7 Motion revisited **Core**
#### 4.7.1 Position, velocity, and acceleration
#### 4.7.2 Speed versus velocity
#### 4.7.3 Falling under constant acceleration
#### 4.7.4 Units and signs in motion problems

### 4.8 Warning examples **Counterexample**
#### 4.8.1 A continuous function with no derivative at one point
#### 4.8.2 A derivative that exists but is not continuous **Optional**
#### 4.8.3 A graphing calculator misses a sharp corner **Computing**

### 4.9 Chapter review and discovery problems
#### 4.9.1 Skills: derivative from definition
#### 4.9.2 Concept check: tangent line versus secant line
#### 4.9.3 Project: estimate velocity from noisy position data **Computing/Project**
#### 4.9.4 Hook: computing every derivative from the definition is too slow

---

## Chapter 5. Differentiation Rules and Elementary Functions

### 5.1 The algebra of derivatives **Core**
#### 5.1.1 Constant multiple rule
#### 5.1.2 Sum and difference rules
#### 5.1.3 Why derivative rules are linear
#### 5.1.4 Derivatives of polynomials

### 5.2 Product and quotient rules **Core**
#### 5.2.1 Why the product rule has two terms
#### 5.2.2 Product rule from changing area
#### 5.2.3 Reciprocal rule
#### 5.2.4 Quotient rule

### 5.3 The chain rule **Core**
#### 5.3.1 A temperature that changes because position changes
#### 5.3.2 Composition as change inside change
#### 5.3.3 The chain rule formula
#### 5.3.4 Tree diagrams for nested functions
#### 5.3.5 Chain rule in differential notation

### 5.4 Implicit differentiation **Core**
#### 5.4.1 Curves not solved for \(y\)
#### 5.4.2 Differentiating both sides
#### 5.4.3 Tangent lines to implicit curves
#### 5.4.4 Higher derivatives implicitly

### 5.5 Derivatives of trigonometric functions **Core**
#### 5.5.1 Radians and the limit \(\sin h/h\to1\)
#### 5.5.2 Derivative of sine
#### 5.5.3 Derivative of cosine
#### 5.5.4 Tangent, secant, cosecant, and cotangent
#### 5.5.5 Simple harmonic motion preview

### 5.6 Derivatives of exponential and logarithmic functions **Core**
#### 5.6.1 Exponential growth as a rate law
#### 5.6.2 The special base \(e\)
#### 5.6.3 Derivative of \(e^x\)
#### 5.6.4 Derivative of \(a^x\)
#### 5.6.5 Derivative of \(\ln x\)
#### 5.6.6 Logarithmic differentiation

### 5.7 Inverse functions and inverse trigonometric functions **Core**
#### 5.7.1 Derivative of an inverse function
#### 5.7.2 Why nonzero derivative matters
#### 5.7.3 \(\arcsin x\), \(\arctan x\), and friends
#### 5.7.4 Inverse trigonometric derivatives in integration preview

### 5.8 General power rule and hyperbolic functions **Core/Optional**
#### 5.8.1 Derivative of \(x^r\)
#### 5.8.2 Hyperbolic sine and cosine
#### 5.8.3 Hyperbolic identities
#### 5.8.4 Why these functions appear in hanging cables **Optional**

### 5.9 Warning examples **Counterexample**
#### 5.9.1 The product rule is not \((fg)'=f'g'\)
#### 5.9.2 The chain rule needs composition order
#### 5.9.3 An inverse can fail to be differentiable when the tangent is horizontal

### 5.10 Chapter review and discovery problems
#### 5.10.1 Skills: mixed derivative calculations
#### 5.10.2 Proof practice: product and chain rules **Proof**
#### 5.10.3 Project: derivative formulas from numerical experiments **Computing/Project**
#### 5.10.4 Hook: derivatives compute slopes, but slopes tell the shape of a graph

---

# Part III. What Derivatives Reveal

## Chapter 6. Shape, Extremes, and the Mean Value Theorem

### 6.1 Increasing and decreasing functions **Core**
#### 6.1.1 Reading motion from the sign of velocity
#### 6.1.2 First derivative sign charts
#### 6.1.3 Intervals of increase and decrease
#### 6.1.4 Critical numbers

### 6.2 Local and absolute extrema **Core**
#### 6.2.1 Local maximum and local minimum
#### 6.2.2 Fermat's theorem
#### 6.2.3 Closed interval method
#### 6.2.4 Endpoints matter

### 6.3 Rolle's Theorem and the Mean Value Theorem **Core/Proof**
#### 6.3.1 A road trip with average speed
#### 6.3.2 Rolle's Theorem
#### 6.3.3 Mean Value Theorem
#### 6.3.4 Consequences: constant derivative and equal derivatives

### 6.4 Concavity and second derivatives **Core**
#### 6.4.1 Velocity changing: acceleration
#### 6.4.2 Concave up and concave down
#### 6.4.3 Inflection points
#### 6.4.4 Second derivative test

### 6.5 Graph sketching with calculus **Core**
#### 6.5.1 Sign charts for \(f'\) and \(f''\)
#### 6.5.2 Asymptotes and end behavior
#### 6.5.3 A complete curve-sketching workflow
#### 6.5.4 When technology helps and when it misleads **Computing**

### 6.6 Indeterminate forms and l'Hospital's Rule **Core**
#### 6.6.1 The forms \(0/0\) and \(\infty/\infty\)
#### 6.6.2 Why derivatives can reveal a limiting ratio
#### 6.6.3 Other indeterminate forms
#### 6.6.4 Comparing growth rates

### 6.7 Warning examples **Counterexample**
#### 6.7.1 Fermat's theorem fails at an endpoint
#### 6.7.2 MVT fails without continuity
#### 6.7.3 MVT fails without differentiability
#### 6.7.4 Second derivative test can be inconclusive
#### 6.7.5 l'Hospital's Rule cannot be used on every quotient

### 6.8 Chapter review and discovery problems
#### 6.8.1 Skills: graph from derivatives
#### 6.8.2 Proof practice with MVT **Proof**
#### 6.8.3 Project: reconstruct a trip from acceleration data **Project**
#### 6.8.4 Hook: knowing shape is useful, but many problems ask for the best possible choice

---

## Chapter 7. Optimization, Related Rates, and Models

### 7.1 Related rates **Core**
#### 7.1.1 Quantities changing together
#### 7.1.2 Differentiating a relation with respect to time
#### 7.1.3 Geometry problems: ladders, shadows, cones
#### 7.1.4 Units as a guardrail

### 7.2 Optimization problems **Core**
#### 7.2.1 Translating a word problem into a function
#### 7.2.2 Constraints in one variable
#### 7.2.3 Geometry: boxes, fences, cans, and light paths
#### 7.2.4 Endpoint checks and physical feasibility

### 7.3 Linear approximation in applications **Core**
#### 7.3.1 Estimating hard numbers quickly
#### 7.3.2 Error propagation
#### 7.3.3 Relative and percentage error
#### 7.3.4 Sensitivity in measurement

### 7.4 Newton's method **Core/Computing**
#### 7.4.1 Tangent lines as root finders
#### 7.4.2 The iteration formula
#### 7.4.3 Convergence when the starting point is good
#### 7.4.4 Failure modes: cycles and bad tangents

### 7.5 Exponential growth and decay **Core**
#### 7.5.1 The differential equation \(y'=ky\)
#### 7.5.2 Half-life and doubling time
#### 7.5.3 Continuously compounded interest
#### 7.5.4 Newton's law of cooling

### 7.6 Logistic growth and limited resources **Core/Bridge**
#### 7.6.1 Why pure exponential growth cannot last
#### 7.6.2 The logistic differential equation
#### 7.6.3 Equilibria and stability from a graph
#### 7.6.4 Population and spread models

### 7.7 Light, time, and extremal principles **Optional/Project**
#### 7.7.1 Reflection from shortest path
#### 7.7.2 Refraction and Snell's law
#### 7.7.3 The seed of the calculus of variations

### 7.8 Warning examples **Counterexample**
#### 7.8.1 A critical point outside the physical domain
#### 7.8.2 A local maximum that is not the absolute maximum
#### 7.8.3 Newton's method converges to the wrong root or does not converge

### 7.9 Chapter review and applications
#### 7.9.1 Skills: related rates and optimization
#### 7.9.2 Project: design a least-material container **Project**
#### 7.9.3 Project: model cooling data **Computing/Project**
#### 7.9.4 Hook: derivatives measure change; now we need to add change back up

---

# Part IV. Integrals and the Fundamental Theorem

## Chapter 8. The Integral as Accumulation

### 8.1 Distance from velocity **Core**
#### 8.1.1 Constant velocity revisited
#### 8.1.2 Piecewise constant velocity
#### 8.1.3 Estimating distance from sampled speeds
#### 8.1.4 Signed displacement versus total distance

### 8.2 Area under a graph **Core**
#### 8.2.1 Rectangular estimates
#### 8.2.2 Left, right, and midpoint sums
#### 8.2.3 Upper and lower sums
#### 8.2.4 Area as a limiting process

### 8.3 Sigma notation and finite sums **Core**
#### 8.3.1 Summation notation
#### 8.3.2 Arithmetic and geometric sums
#### 8.3.3 Sums of powers
#### 8.3.4 From finite sums to integrals

### 8.4 The definite integral **Core**
#### 8.4.1 Partitions and sample points
#### 8.4.2 Riemann sums
#### 8.4.3 Definition of the definite integral
#### 8.4.4 Integrability, informally first

### 8.5 Signed area and net change **Core**
#### 8.5.1 Area above the axis
#### 8.5.2 Area below the axis
#### 8.5.3 Cancellation and meaning
#### 8.5.4 Total accumulation from absolute value

### 8.6 Properties of the integral **Core**
#### 8.6.1 Linearity
#### 8.6.2 Additivity over intervals
#### 8.6.3 Order properties
#### 8.6.4 Average value of a function
#### 8.6.5 Symmetry

### 8.7 Existence of integrals **Proof/Optional**
#### 8.7.1 Continuous functions are integrable
#### 8.7.2 Monotone functions are integrable
#### 8.7.3 Functions with finitely many jump discontinuities
#### 8.7.4 A bounded function that is not Riemann integrable **Counterexample**

### 8.8 Chapter review and discovery problems
#### 8.8.1 Skills: set up Riemann sums
#### 8.8.2 Project: estimate energy use from power data **Project**
#### 8.8.3 Computing: compare left, right, midpoint, and trapezoid estimates **Computing**
#### 8.8.4 Hook: an accumulation function has a slope, and that slope is surprisingly simple

---

## Chapter 9. The Fundamental Theorem of Calculus

### 9.1 Accumulation functions **Core**
#### 9.1.1 Area with a moving endpoint
#### 9.1.2 \(A(x)=\int_a^x f(t)\,dt\)
#### 9.1.3 Estimating the change in an accumulation function
#### 9.1.4 The slope of accumulated area

### 9.2 Fundamental Theorem, Part I **Core/Proof**
#### 9.2.1 The derivative of an accumulation function
#### 9.2.2 Continuity as the needed hypothesis
#### 9.2.3 Geometric proof idea
#### 9.2.4 Examples with variable upper limits

### 9.3 Fundamental Theorem, Part II **Core**
#### 9.3.1 Antiderivatives evaluate definite integrals
#### 9.3.2 Net change theorem
#### 9.3.3 Position from velocity
#### 9.3.4 Accumulated rate in science and economics

### 9.4 Indefinite integrals **Core**
#### 9.4.1 Antiderivative families
#### 9.4.2 The constant of integration
#### 9.4.3 Initial value problems
#### 9.4.4 Basic antiderivative formulas

### 9.5 Substitution **Core**
#### 9.5.1 Reversing the chain rule
#### 9.5.2 Changing variables in a definite integral
#### 9.5.3 Orientation and reversed limits
#### 9.5.4 Substitution in motion and geometry

### 9.6 Differential notation and oriented length **Bridge**
#### 9.6.1 \(dx\) as an oriented step
#### 9.6.2 \(f(x)\,dx\) as the thing being accumulated
#### 9.6.3 Pulling an integrand through \(x=g(u)\), without abstraction
#### 9.6.4 The one-dimensional seed of differential forms

### 9.7 Warning examples **Counterexample**
#### 9.7.1 A discontinuity and the derivative of an accumulation function
#### 9.7.2 Forgetting the new limits in substitution
#### 9.7.3 Treating \(\int f(x)\,dx\) like multiplication
#### 9.7.4 Confusing area with net signed area

### 9.8 Chapter review and discovery problems
#### 9.8.1 Skills: FTC and substitution
#### 9.8.2 Proof practice: FTC Part I in a simple case **Proof**
#### 9.8.3 Project: reconstruct a function from its rate **Project**
#### 9.8.4 Hook: once integration is computable, it can measure more than area

---

# Part V. Applications and Techniques of Integration

## Chapter 10. What Integrals Measure

### 10.1 Area between curves **Core**
#### 10.1.1 Top minus bottom
#### 10.1.2 Right minus left
#### 10.1.3 Splitting at intersections
#### 10.1.4 Area from data and graphs

### 10.2 Volumes by slicing **Core**
#### 10.2.1 Cross-sectional area as a function
#### 10.2.2 Solids of revolution: disks and washers
#### 10.2.3 Non-circular cross sections
#### 10.2.4 Choosing the slicing direction

### 10.3 Cylindrical shells **Core**
#### 10.3.1 A thin shell unwrapped
#### 10.3.2 Shell method formula
#### 10.3.3 When shells beat washers
#### 10.3.4 Comparing two methods on the same solid

### 10.4 Mass, density, and center of mass **Core**
#### 10.4.1 Linear density and mass of a rod
#### 10.4.2 Moments
#### 10.4.3 Center of mass on a line
#### 10.4.4 Lamina preview by slices **Bridge**

### 10.5 Work and energy **Core**
#### 10.5.1 Constant force and variable force
#### 10.5.2 Springs and Hooke's law
#### 10.5.3 Lifting a chain
#### 10.5.4 Pumping fluid from a tank

### 10.6 Hydrostatic force **Core/Optional**
#### 10.6.1 Pressure depends on depth
#### 10.6.2 Force on a vertical plate
#### 10.6.3 Choosing strips
#### 10.6.4 Dams and windows

### 10.7 Average value and probability **Core**
#### 10.7.1 Average value of a continuous function
#### 10.7.2 Probability density
#### 10.7.3 Expected value
#### 10.7.4 Normal distribution as a preview of non-elementary integrals

### 10.8 Arc length and surface area of revolution **Core**
#### 10.8.1 Arc length from small straight pieces
#### 10.8.2 Arc length of a graph
#### 10.8.3 Surface area by rotating a curve
#### 10.8.4 Why some natural lengths have no elementary antiderivative

### 10.9 Chapter review and applications
#### 10.9.1 Skills: choose the small piece
#### 10.9.2 Project: compare volume methods **Project**
#### 10.9.3 Project: work needed to pump out a real tank shape **Project**
#### 10.9.4 Hook: many integrals cannot be found by substitution alone

---

## Chapter 11. Techniques of Integration

### 11.1 Integration by parts **Core**
#### 11.1.1 Reversing the product rule
#### 11.1.2 Choosing \(u\) and \(dv\)
#### 11.1.3 Repeated integration by parts
#### 11.1.4 Definite integrals and boundary terms

### 11.2 Trigonometric integrals **Core**
#### 11.2.1 Powers of sine and cosine
#### 11.2.2 Powers of tangent and secant
#### 11.2.3 Product-to-sum identities
#### 11.2.4 Strategy over memorization

### 11.3 Trigonometric substitution **Core**
#### 11.3.1 Square roots from circles and triangles
#### 11.3.2 \(a^2-x^2\), \(a^2+x^2\), and \(x^2-a^2\)
#### 11.3.3 Returning to the original variable
#### 11.3.4 Hyperbolic substitutions **Optional**

### 11.4 Rational functions and partial fractions **Core**
#### 11.4.1 Polynomial division
#### 11.4.2 Distinct linear factors
#### 11.4.3 Repeated linear factors
#### 11.4.4 Irreducible quadratic factors
#### 11.4.5 Completing the square

### 11.5 Strategy for integration **Core**
#### 11.5.1 Recognizing the structure of an integrand
#### 11.5.2 Substitution first or parts first?
#### 11.5.3 Algebraic simplification
#### 11.5.4 When no elementary antiderivative exists

### 11.6 Computer algebra systems and integral tables **Computing**
#### 11.6.1 Checking without surrendering thought
#### 11.6.2 Equivalent antiderivatives can look different
#### 11.6.3 Branch and domain issues
#### 11.6.4 Special functions born from integrals

### 11.7 Improper integrals **Core**
#### 11.7.1 Infinite intervals
#### 11.7.2 Infinite discontinuities
#### 11.7.3 Convergence and divergence
#### 11.7.4 Comparison tests for improper integrals
#### 11.7.5 The \(p\)-integrals

### 11.8 Warning examples **Counterexample**
#### 11.8.1 An antiderivative exists formally but the improper integral diverges
#### 11.8.2 Cancellation hides divergence
#### 11.8.3 A CAS gives an antiderivative with the wrong domain
#### 11.8.4 A trigonometric substitution triangle used outside its range

### 11.9 Chapter review and discovery problems
#### 11.9.1 Skills: choose and apply integration techniques
#### 11.9.2 Project: build an integration decision tree **Project**
#### 11.9.3 Project: compare human and CAS antiderivatives **Computing/Project**
#### 11.9.4 Hook: exact integration is only one way to compute an accumulated amount

---

## Chapter 12. Numerical Integration, Error, and Computation

### 12.1 Why approximate integrals? **Core/Computing**
#### 12.1.1 Data instead of formulas
#### 12.1.2 Non-elementary antiderivatives
#### 12.1.3 Speed versus accuracy
#### 12.1.4 The role of error estimates

### 12.2 Midpoint and trapezoidal rules **Core**
#### 12.2.1 Geometry of each rule
#### 12.2.2 Composite rules
#### 12.2.3 Error patterns from concavity
#### 12.2.4 Error bounds

### 12.3 Simpson's Rule **Core**
#### 12.3.1 Quadratic approximation on pairs of intervals
#### 12.3.2 Composite Simpson's Rule
#### 12.3.3 Why Simpson's Rule is often much better
#### 12.3.4 Simpson error bound

### 12.4 Numerical differentiation **Computing/Optional**
#### 12.4.1 Forward, backward, and centered differences
#### 12.4.2 Truncation error
#### 12.4.3 Roundoff error
#### 12.4.4 Why smaller \(h\) is not always better

### 12.5 Newton's method revisited **Computing**
#### 12.5.1 Stopping criteria
#### 12.5.2 Error estimates
#### 12.5.3 Multiple roots
#### 12.5.4 A first glimpse of chaotic iteration **Optional**

### 12.6 Computing experiments **Project**
#### 12.6.1 Approximate \(\pi\) by integration
#### 12.6.2 Estimate a probability from a density
#### 12.6.3 Compare rules on smooth and rough functions
#### 12.6.4 Build a small numerical-integration program

### 12.7 Chapter review and discovery problems
#### 12.7.1 Skills: numerical rules and error bounds
#### 12.7.2 Concept check: exact value versus approximation
#### 12.7.3 Hook: a differential equation often cannot be solved exactly either

---

# Part VI. Differential Equations and Curves

## Chapter 13. Differential Equations: Laws Written as Derivatives

### 13.1 Modeling with differential equations **Core**
#### 13.1.1 A law that gives a rate
#### 13.1.2 Solution as an unknown function
#### 13.1.3 Initial conditions
#### 13.1.4 Checking a proposed solution

### 13.2 Direction fields **Core**
#### 13.2.1 Slope field as a picture of a differential equation
#### 13.2.2 Equilibrium solutions
#### 13.2.3 Qualitative behavior
#### 13.2.4 Reading long-term behavior from the field

### 13.3 Euler's method **Core/Computing**
#### 13.3.1 Following the slope field step by step
#### 13.3.2 Step size and accumulated error
#### 13.3.3 Improved Euler method **Optional**
#### 13.3.4 Numerical solutions as approximate functions

### 13.4 Separable equations **Core**
#### 13.4.1 Separating variables
#### 13.4.2 Growth and decay revisited
#### 13.4.3 Cooling and mixing
#### 13.4.4 Implicit solutions

### 13.5 Logistic and threshold models **Core**
#### 13.5.1 Carrying capacity
#### 13.5.2 Phase line
#### 13.5.3 Stable and unstable equilibria
#### 13.5.4 Harvesting and tipping points **Optional**

### 13.6 First-order linear equations **Core**
#### 13.6.1 Standard form
#### 13.6.2 Integrating factors
#### 13.6.3 Mixing and finance examples
#### 13.6.4 Why the integrating factor works

### 13.7 Second-order equations and vibration **Optional/Bridge**
#### 13.7.1 Simple harmonic motion
#### 13.7.2 The equation \(y''+\omega^2y=0\)
#### 13.7.3 Damping
#### 13.7.4 Driven oscillation and resonance

### 13.8 Systems and interaction models **Optional**
#### 13.8.1 Two populations
#### 13.8.2 Predator-prey equations as a picture
#### 13.8.3 Why systems lead naturally to multivariable calculus

### 13.9 Warning examples **Counterexample**
#### 13.9.1 A solution lost by dividing by zero
#### 13.9.2 Euler's method follows the wrong behavior with a large step
#### 13.9.3 Same differential equation, different initial conditions

### 13.10 Chapter review and applications
#### 13.10.1 Skills: solve and interpret first-order equations
#### 13.10.2 Project: model a cooling cup of coffee **Project**
#### 13.10.3 Project: compare Euler approximations with exact solutions **Computing/Project**
#### 13.10.4 Hook: some curves are easier to describe by how they are traced than by \(y=f(x)\)

---

## Chapter 14. Parametric Curves, Polar Coordinates, and Conics

### 14.1 Parametric curves **Core**
#### 14.1.1 A curve as a moving point
#### 14.1.2 Eliminating the parameter when possible
#### 14.1.3 Different parametrizations of the same curve
#### 14.1.4 Orientation and speed along a curve

### 14.2 Calculus with parametric curves **Core**
#### 14.2.1 Slope \(dy/dx\) from \(dx/dt\) and \(dy/dt\)
#### 14.2.2 Horizontal and vertical tangents
#### 14.2.3 Concavity
#### 14.2.4 Motion in the plane as a bridge to vectors

### 14.3 Length and area for parametric curves **Core**
#### 14.3.1 Arc length from speed
#### 14.3.2 Surface area from a parametrized curve of revolution
#### 14.3.3 Area enclosed by a parametric curve
#### 14.3.4 Cycloids and rolling motion

### 14.4 Polar coordinates **Core**
#### 14.4.1 Distance and angle as coordinates
#### 14.4.2 Converting between polar and Cartesian coordinates
#### 14.4.3 Polar graphs
#### 14.4.4 Circles, spirals, roses, and limacons

### 14.5 Calculus in polar coordinates **Core**
#### 14.5.1 Slope of a polar curve
#### 14.5.2 Area in polar coordinates
#### 14.5.3 Arc length in polar coordinates
#### 14.5.4 Intersections and repeated tracing

### 14.6 Conic sections **Core**
#### 14.6.1 Parabolas, ellipses, and hyperbolas from focus and directrix
#### 14.6.2 Standard equations
#### 14.6.3 Polar equations of conics
#### 14.6.4 Eccentricity

### 14.7 Planetary motion as a capstone **Optional/Project**
#### 14.7.1 Ellipses in polar form
#### 14.7.2 Kepler's second law as swept area
#### 14.7.3 Central force preview
#### 14.7.4 Why this belongs to multivariable calculus next

### 14.8 Complex numbers and polar form **Bridge/Optional**
#### 14.8.1 Complex numbers as points in the plane
#### 14.8.2 Multiplication as scaling and rotation
#### 14.8.3 Euler's formula preview
#### 14.8.4 Oscillation written exponentially

### 14.9 Warning examples **Counterexample**
#### 14.9.1 A parametrization stops even when the curve continues
#### 14.9.2 A polar curve traced twice
#### 14.9.3 A tangent formula fails when both derivatives vanish

### 14.10 Chapter review and projects
#### 14.10.1 Skills: parametric and polar calculus
#### 14.10.2 Project: design a cycloid animation **Computing/Project**
#### 14.10.3 Project: compare polar and Cartesian descriptions of conics **Project**
#### 14.10.4 Hook: infinite processes return, now as sums rather than areas

---

# Part VII. Infinite Processes and Approximation by Polynomials

## Chapter 15. Sequences and Infinite Series

### 15.1 Sequences **Core**
#### 15.1.1 Lists with a rule
#### 15.1.2 Convergence and divergence
#### 15.1.3 Monotone bounded sequences
#### 15.1.4 Recursive sequences and fixed points

### 15.2 Infinite series **Core**
#### 15.2.1 Partial sums
#### 15.2.2 Series convergence as a sequence problem
#### 15.2.3 Geometric series
#### 15.2.4 Telescoping series

### 15.3 The harmonic series and first warnings **Core**
#### 15.3.1 Terms go to zero but the series diverges
#### 15.3.2 Necessary condition for convergence
#### 15.3.3 The harmonic series
#### 15.3.4 Grouping terms to see divergence

### 15.4 Positive series tests **Core**
#### 15.4.1 Integral test
#### 15.4.2 Remainder estimates from the integral test
#### 15.4.3 Direct comparison
#### 15.4.4 Limit comparison
#### 15.4.5 \(p\)-series

### 15.5 Alternating series **Core**
#### 15.5.1 Alternating Series Test
#### 15.5.2 Alternating Series Estimation Theorem
#### 15.5.3 Conditional convergence
#### 15.5.4 Error as the first omitted term

### 15.6 Absolute convergence and stronger tests **Core**
#### 15.6.1 Absolute versus conditional convergence
#### 15.6.2 Ratio Test
#### 15.6.3 Root Test
#### 15.6.4 Strategy for testing series

### 15.7 Rearrangement and the danger of infinity **Optional/Proof**
#### 15.7.1 Finite sums can be rearranged freely
#### 15.7.2 Infinite conditionally convergent sums cannot
#### 15.7.3 Riemann rearrangement idea
#### 15.7.4 Why absolute convergence is safer

### 15.8 Warning examples **Counterexample**
#### 15.8.1 Terms tend to zero but the series diverges
#### 15.8.2 Ratio Test gives no information
#### 15.8.3 Integral Test used on a nonpositive function
#### 15.8.4 Alternating Series Test used without decreasing terms

### 15.9 Chapter review and discovery problems
#### 15.9.1 Skills: choose series tests
#### 15.9.2 Project: estimate sums with rigorous error bounds **Project**
#### 15.9.3 Computing: numerical partial sums can mislead **Computing**
#### 15.9.4 Hook: some infinite sums are functions, not just numbers

---

## Chapter 16. Power Series, Taylor Polynomials, and Taylor Series

### 16.1 Power series **Core**
#### 16.1.1 A polynomial with infinitely many terms
#### 16.1.2 Center of a power series
#### 16.1.3 Radius and interval of convergence
#### 16.1.4 Endpoint testing

### 16.2 Working with power series **Core**
#### 16.2.1 Algebra of power series
#### 16.2.2 Differentiating power series
#### 16.2.3 Integrating power series
#### 16.2.4 Why power series behave better than arbitrary series

### 16.3 Representing functions by power series **Core**
#### 16.3.1 Geometric series as the seed
#### 16.3.2 Series for \(1/(1-x)\)
#### 16.3.3 Series for \(\ln(1+x)\)
#### 16.3.4 Series for \(\arctan x\)
#### 16.3.5 Estimating \(\pi\) from a series

### 16.4 Taylor polynomials **Core**
#### 16.4.1 Matching value and derivatives
#### 16.4.2 Linear, quadratic, and cubic approximations
#### 16.4.3 Taylor polynomial centered at \(a\)
#### 16.4.4 Maclaurin polynomials

### 16.5 Taylor's theorem and remainders **Core/Proof**
#### 16.5.1 The error term matters
#### 16.5.2 Lagrange form of the remainder
#### 16.5.3 Integral form of the remainder **Optional**
#### 16.5.4 Alternating-series remainders as a special case

### 16.6 Taylor series for elementary functions **Core**
#### 16.6.1 \(e^x\)
#### 16.6.2 \(\sin x\) and \(\cos x\)
#### 16.6.3 \(\ln(1+x)\)
#### 16.6.4 \(\arctan x\)
#### 16.6.5 Binomial series

### 16.7 Applications of Taylor series **Core**
#### 16.7.1 Estimating function values
#### 16.7.2 Evaluating limits
#### 16.7.3 Approximating integrals
#### 16.7.4 Solving differential equations by series
#### 16.7.5 Error bounds in applications

### 16.8 Uniform convergence preview **Optional/Bridge**
#### 16.8.1 Pointwise convergence of functions
#### 16.8.2 Uniform convergence as one error bound for all points
#### 16.8.3 Interchanging limits and integrals
#### 16.8.4 Why power series are trustworthy inside their radius

### 16.9 Warning examples **Counterexample**
#### 16.9.1 Taylor series converges but not to the function **Optional**
#### 16.9.2 Endpoint behavior differs from interior behavior
#### 16.9.3 Termwise operations fail for arbitrary function series **Optional**
#### 16.9.4 A good local approximation becomes bad far away

### 16.10 Chapter review and projects
#### 16.10.1 Skills: power series and Taylor series
#### 16.10.2 Project: build a sine calculator with error control **Computing/Project**
#### 16.10.3 Project: compare Taylor approximations visually **Computing/Project**
#### 16.10.4 Hook: the series for sine and cosine hide a rotating vector

---

# Part VIII. Capstones and Bridges

## Chapter 17. Complex Numbers, Fourier Ideas, and the Road Ahead

### 17.1 Complex numbers and Euler's formula **Bridge/Optional**
#### 17.1.1 Complex plane
#### 17.1.2 Polar form
#### 17.1.3 Multiplication as rotation and scaling
#### 17.1.4 Euler's formula from Taylor series
#### 17.1.5 Why \(e^{it}\) is the natural language of oscillation

### 17.2 Vibrations and second-order equations **Optional**
#### 17.2.1 The spring equation
#### 17.2.2 Sine and cosine as natural motions
#### 17.2.3 Energy conservation
#### 17.2.4 Damping and forcing preview

### 17.3 Fourier series preview **Optional**
#### 17.3.1 Building a periodic function from waves
#### 17.3.2 Orthogonality of sine and cosine, geometrically
#### 17.3.3 Square waves and Gibbs phenomenon
#### 17.3.4 Why Fourier series belong after Taylor series

### 17.4 The one-dimensional Stokes theorem **Bridge**
#### 17.4.1 Boundary of an interval
#### 17.4.2 \(\int_a^b F'(x)\,dx=F(b)-F(a)\)
#### 17.4.3 The FTC as a boundary theorem
#### 17.4.4 Preview of line integrals and differential forms

### 17.5 Conservation laws in one dimension **Bridge/Optional**
#### 17.5.1 Density and flux on a line
#### 17.5.2 Accumulation inside an interval
#### 17.5.3 What crosses the boundary changes what is inside
#### 17.5.4 Preview of divergence in multivariable calculus

### 17.6 Least action and the shape of a path **Optional/Project**
#### 17.6.1 From optimization of numbers to optimization of functions
#### 17.6.2 The brachistochrone story
#### 17.6.3 A gentle first variation calculation
#### 17.6.4 Why this is beyond ordinary single-variable calculus

### 17.7 Final projects
#### 17.7.1 Model, solve, and test a cooling law **Project**
#### 17.7.2 Approximate a difficult integral three ways **Project**
#### 17.7.3 Build a Taylor-series calculator **Computing/Project**
#### 17.7.4 Analyze a parametric curve from motion data **Project**
#### 17.7.5 Explain the FTC as the first boundary theorem **Bridge/Project**

---

# Appendices

## Appendix A. Algebra and Inequalities Review
### A.1 Factoring and completing the square
### A.2 Rational expressions
### A.3 Exponents and radicals
### A.4 Inequalities and absolute values
### A.5 Sigma notation practice

## Appendix B. Coordinate Geometry
### B.1 Lines
### B.2 Circles
### B.3 Parabolas, ellipses, and hyperbolas
### B.4 Distance and midpoint formulas
### B.5 Scaling and shifting graphs

## Appendix C. Trigonometry in Radians
### C.1 Unit circle definitions
### C.2 Basic identities
### C.3 Addition formulas
### C.4 Inverse trigonometric functions
### C.5 Trigonometric equations

## Appendix D. Proofs and Completeness
### D.1 Least upper bound property
### D.2 Monotone convergence theorem
### D.3 Bolzano's theorem and bisection
### D.4 Extreme Value Theorem proof outline
### D.5 Uniform continuity on closed intervals

## Appendix E. Technology Notes
### E.1 Graphing windows
### E.2 Numerical precision and roundoff
### E.3 Calculator and CAS syntax
### E.4 Simple Python experiments for calculus
### E.5 Plotting sequences, sums, and Taylor polynomials

## Appendix F. Tables
### F.1 Derivative formulas
### F.2 Integral formulas
### F.3 Common Taylor series
### F.4 Series tests
### F.5 Numerical integration rules
