# Language corrections: complete before-and-after record

Scope: the PreTeXt edition only. Each item records a flagged passage and its replacement. Formula notation is retained in TeX form in this review document.

## 1. Velocity, Distance, and the First Shape of Calculus

Source: [source\chapters\ch01-velocity-distance-and-the-first-shape-of-calculus\ch01-velocity-distance-and-the-first-shape-of-calculus.ptx](../../source\chapters\ch01-velocity-distance-and-the-first-shape-of-calculus\ch01-velocity-distance-and-the-first-shape-of-calculus.ptx)

Flag: Replace vague metaphors, repetition, or introductory filler with the section concept and conditions.

**Before**

> A car dashboard already contains the first story of calculus. One instrument remembers how much road has been accumulated. Another tells how fast that accumulated amount is changing. Those two ideas are not separate. They are inverse clues. \text{distance changes} \quad \longleftrightarrow \quad \text{velocity is measured}, and \text{velocity is accumulated} \quad \longleftrightarrow \quad \text{distance changes}. Calculus begins by making this relation precise.

**After**

Velocity describes how position changes with time. Accumulating velocity over a time interval gives the change in position. This chapter develops these two relationships using motion, slopes, areas, finite differences, and finite sums.

## 2. Changing velocity and the need for limits

Source: [source\chapters\ch01-velocity-distance-and-the-first-shape-of-calculus\sections\sec-1-5-changing-velocity-and-the-need-for-limits.xml](../../source\chapters\ch01-velocity-distance-and-the-first-shape-of-calculus\sections\sec-1-5-changing-velocity-and-the-need-for-limits.xml)

Flag: Replace vague metaphors, repetition, or introductory filler with the section concept and conditions.

**Before**

> Step velocities were friendly. On each interval, the velocity graph was flat, so a rectangle gave exact displacement and a line segment gave exact position. Real motion is not usually so polite. A car speeds up while the clock is running. A falling stone moves faster at each instant. A population grows at a rate that changes with its size. The old rectangle and slope pictures still guide us, but now they are no longer exact after only finitely many pieces. The new idea is to look closer and closer.

**After**

When velocity is constant on each of finitely many time intervals, rectangles give the exact displacement. When velocity changes continuously, rectangles give approximations. We will refine those approximations by using shorter intervals. The same limiting process turns average velocity into instantaneous velocity.

## 3. A first map of the book

Source: [source\chapters\ch01-velocity-distance-and-the-first-shape-of-calculus\sections\sec-1-6-a-first-map-of-the-book.xml](../../source\chapters\ch01-velocity-distance-and-the-first-shape-of-calculus\sections\sec-1-6-a-first-map-of-the-book.xml)

Flag: Replace vague metaphors, repetition, or introductory filler with the section concept and conditions.

**Before**

> We have now met the four pictures that will guide the whole course: \text{slope},\qquad \text{area},\qquad \text{difference},\qquad \text{sum}. They do not represent four distinct topics. Instead, they are four perspectives of a single story: change and accumulation counteract each other.

**After**

Slope measures a rate of change, and signed area measures an accumulated change. Finite differences and finite sums give discrete versions of these operations. Limits will connect them to derivatives and integrals.

## 4. Discovery problems and projects

Source: [source\chapters\ch01-velocity-distance-and-the-first-shape-of-calculus\sections\sec-1-7-discovery-problems-and-projects.xml](../../source\chapters\ch01-velocity-distance-and-the-first-shape-of-calculus\sections\sec-1-7-discovery-problems-and-projects.xml)

Flag: Replace vague metaphors, repetition, or introductory filler with the section concept and conditions.

**Before**

> The dashboard story has given us four ways to talk about the same motion: \text{velocity},\qquad \text{position},\qquad \text{slope},\qquad \text{signed area}. Before we build the formal language of limits, it is worth testing those ideas. The problems in this section are not only practice. They are small investigations. Each one asks you to read a graph, build a trip, or discover a pattern that will return later in a more precise form.

**After**

These problems connect velocity, position, slope, and signed area. Use graphs, tables, and motion examples to explain how a rate determines a change and how a change determines an average rate.

## 5. Numbers, Functions, and Models

Source: [source\chapters\ch02-numbers-functions-and-models\ch02-numbers-functions-and-models.ptx](../../source\chapters\ch02-numbers-functions-and-models\ch02-numbers-functions-and-models.ptx)

Flag: Replace vague metaphors, repetition, or introductory filler with the section concept and conditions.

**Before**

> The first chapter began with motion and ended with a promise: \text{make the input close enough, and the output becomes as close as required.} For s(t)=t^2, the average velocity from t=2 to t=2+h was \frac{s(2+h)-s(2)}{h}=4+h, \qquad h\neq 0. The error from the expected value 4 was |(4+h)-4|=|h|. That small calculation already contains the next need. Calculus needs a way to speak about closeness, intervals around a point, and errors that can be made as small as we want. The real line is the measuring tape.

**After**

Calculus uses functions to describe dependence and limits to describe approximation. Before defining limits, we need the real number line, intervals, distances, and error bounds. This chapter develops that language and uses it to describe graphs and mathematical models.

## 6. Functions as assignments

Source: [source\chapters\ch02-numbers-functions-and-models\sections\sec-2-3-functions-as-assignments.xml](../../source\chapters\ch02-numbers-functions-and-models\sections\sec-2-3-functions-as-assignments.xml)

Flag: Replace vague metaphors, repetition, or introductory filler with the section concept and conditions.

**Before**

> The real line gave us a language for position, distance, intervals, and error. Calculus begins when one number on that line determines another. A time determines a position. A radius determines an area. A temperature determines the volume of a gas. A step size h determines the error in an approximation. That kind of dependence is called a function.

**After**

A function assigns one output to each allowed input. For example, a time can determine a position, a radius can determine an area, and a step size can determine an approximation error. We will specify both the assignment and the set of inputs on which it is defined.

## 7. Combining functions

Source: [source\chapters\ch02-numbers-functions-and-models\sections\sec-2-5-combining-functions.xml](../../source\chapters\ch02-numbers-functions-and-models\sections\sec-2-5-combining-functions.xml)

Flag: Replace vague metaphors, repetition, or introductory filler with the section concept and conditions.

**Before**

> Transformations moved a graph without changing its basic identity. A parabola could shift, stretch, or reflect and still be built from the same old rule. There is another way to make new functions. We can combine outputs. We can multiply two changing quantities. We can divide one quantity by another. Most importantly, we can feed the output of one function into the input of another. These operations are not bookkeeping. Later, each one will force a derivative rule.

**After**

We can form new functions by adding, subtracting, multiplying, or dividing their outputs. Composition forms a new function by using the output of one function as the input of another. Each operation also imposes requirements on the domain.

## 8. A catalog of essential functions

Source: [source\chapters\ch02-numbers-functions-and-models\sections\sec-2-6-a-catalog-of-essential-functions.xml](../../source\chapters\ch02-numbers-functions-and-models\sections\sec-2-6-a-catalog-of-essential-functions.xml)

Flag: Replace vague metaphors, repetition, or introductory filler with the section concept and conditions.

**Before**

> We can now build functions by formulas, graphs, tables, words, transformations, arithmetic, composition, and inverses. But calculus does not treat every function as a stranger. Some families appear again and again. Lines describe constant rates. Polynomials describe smooth algebraic change. Rational functions show ratios and asymptotes. Trigonometric functions describe periodic motion. Exponential functions describe constant percentage change. Logarithms undo exponentials. This catalog is not a list to memorize. It is a set of familiar shapes and stories.

**After**

Several function families occur frequently in calculus. Lines describe constant rates, polynomials and rational functions describe algebraic relationships, trigonometric functions describe periodic behavior, and exponentials describe constant proportional growth or decay. Logarithms invert exponentials. This section reviews their formulas, domains, and graphs.

## 9. Calculating limits

Source: [source\chapters\ch03-limits-and-continuity\sections\sec-3-2-calculating-limits.xml](../../source\chapters\ch03-limits-and-continuity\sections\sec-3-2-calculating-limits.xml)

Flag: Replace vague metaphors, repetition, or introductory filler with the section concept and conditions.

**Before**

> A table can point toward a limit, but a table only checks a few inputs. A graph can reveal the shape, but a graph depends on the viewing window. Algebra lets us prove what the nearby values are doing. The first limits we can calculate are the ones where nearby behavior is preserved by arithmetic.

**After**

Limit laws allow us to calculate limits using arithmetic operations on simpler functions. We will also use algebraic simplification and inequalities when direct substitution is unavailable. Tables and graphs can suggest an answer; the calculation must justify it.

## 10. One-sided limits and infinite behavior

Source: [source\chapters\ch03-limits-and-continuity\sections\sec-3-3-one-sided-limits-and-infinite-behavior.xml](../../source\chapters\ch03-limits-and-continuity\sections\sec-3-3-one-sided-limits-and-infinite-behavior.xml)

Flag: Replace vague metaphors, repetition, or introductory filler with the section concept and conditions.

**Before**

> Section [cross-reference] gave us tools for limits that settle down to a finite number. But limits can fail, or change character, in several different ways. A graph can approach one value from the left and another from the right. A function can grow without bound near a point. Or the input itself can move farther and farther away, so that we ask what happens at the far ends of the graph. These are not rare exceptions. They are some of the most important behaviors calculus has to name.

**After**

A function can approach different values from the left and right, grow without bound near a point, or approach a limit as the input tends to infinity. These behaviors require separate definitions. A two-sided finite limit exists only when both one-sided limits exist and agree.

## 11. Continuity

Source: [source\chapters\ch03-limits-and-continuity\sections\sec-3-5-continuity.xml](../../source\chapters\ch03-limits-and-continuity\sections\sec-3-5-continuity.xml)

Flag: Replace vague metaphors, repetition, or introductory filler with the section concept and conditions.

**Before**

> The precise definition of a limit gave us a way to control nearby values. It said: x\text{ close to }a \quad \Longrightarrow \quad f(x)\text{ close to }L. But a limit still does not have to care about the value at the point. A function may have a hole, a wrong value, or no value at all, and still have a limit nearby. Continuity is the calm case. It is the case where the nearby behavior and the actual value agree.

**After**

A limit describes nearby function values and may exist even when the function is undefined at the point. Continuity at a requires the function value to exist and equal that limit: \lim_{x\to a}f(x)=f(a).

## 12. Two theorems about continuous functions

Source: [source\chapters\ch03-limits-and-continuity\sections\sec-3-6-two-theorems-about-continuous-functions.xml](../../source\chapters\ch03-limits-and-continuity\sections\sec-3-6-two-theorems-about-continuous-functions.xml)

Flag: Replace vague metaphors, repetition, or introductory filler with the section concept and conditions.

**Before**

> Continuity began as a local condition: x\text{ close to }a \quad \Longrightarrow \quad f(x)\text{ close to }f(a). But local calm forces global behavior. If a continuous graph starts below a horizontal line and ends above it, it must cross that line somewhere. If a continuous graph lives on a closed finite interval, it must reach a highest point and a lowest point. These facts sound obvious from a picture. Their hypotheses are where the mathematics lives.

**After**

A continuous function on a closed finite interval takes every value between its endpoint values and attains a maximum and a minimum. The Intermediate Value Theorem and the Extreme Value Theorem make these statements precise. Both depend on continuity; the extrema theorem also depends on the interval being closed and bounded.

## 13. Warning examples

Source: [source\chapters\ch03-limits-and-continuity\sections\sec-3-7-warning-examples.xml](../../source\chapters\ch03-limits-and-continuity\sections\sec-3-7-warning-examples.xml)

Flag: Replace vague metaphors, repetition, or introductory filler with the section concept and conditions.

**Before**

> Continuity gave us two promises. The Intermediate Value Theorem says that a continuous graph cannot skip a height. The Extreme Value Theorem says that a continuous function on a closed finite interval reaches a highest and lowest value. Those promises are strong because their hypotheses are strong. If we remove a hypothesis, the conclusion may fail. This section gathers the warnings in one place. Each example is small, but each one protects a theorem from being used illegally.

**After**

The Intermediate Value Theorem requires continuity on an interval. The Extreme Value Theorem requires continuity on a closed, bounded interval. The examples below show how their conclusions can fail when these conditions are removed. We will also distinguish a function value from its nearby limit.

## 14. Chapter review and discovery problems

Source: [source\chapters\ch03-limits-and-continuity\sections\sec-3-9-chapter-review-and-discovery-problems.xml](../../source\chapters\ch03-limits-and-continuity\sections\sec-3-9-chapter-review-and-discovery-problems.xml)

Flag: Replace vague metaphors, repetition, or introductory filler with the section concept and conditions.

**Before**

> This chapter began with one small calculation: \frac{(2+h)^2-2^2}{h}=4+h, \qquad h\neq0. The forbidden value h=0 did not stop us from seeing what happens as h gets close to 0. That idea became the language of limits. Limits then gave us continuity, one-sided behavior, infinite behavior, asymptotes, sequences, and two existence theorems. Before we use limits to define derivatives, it is worth pausing to see the whole map.

**After**

This chapter defined limits and continuity, distinguished one-sided limits from two-sided limits, and treated unbounded behavior and sequence limits. The review problems ask you to calculate limits, check hypotheses, and apply the Intermediate Value and Extreme Value Theorems.

## 15. The Derivative

Source: [source\chapters\ch04-the-derivative\ch04-the-derivative.ptx](../../source\chapters\ch04-the-derivative\ch04-the-derivative.ptx)

Flag: Replace vague metaphors, repetition, or introductory filler with the section concept and conditions.

**Before**

> The last chapter ended with one limit: \lim_{h\to0}\frac{f(a+h)-f(a)}{h}. The numerator measures change in output. The denominator measures change in input. The quotient is an average rate of change. The limit, if it exists, is the instantaneous rate of change. That limit will now become a new object: the derivative. It is the mathematical version of what a speedometer does. It is also the slope of a curve when we zoom in until the curve looks straight.

**After**

A derivative is the limit of average rates of change over intervals shrinking to a point:f\prime(a)=\lim_{h\to0}\frac{f(a+h)-f(a)}{h}.When this finite limit exists, it gives the instantaneous rate of change and the tangent slope at that point. This chapter defines the derivative, develops its first formulas, and explains its use in local approximation and motion.

## 16. Instantaneous rate of change

Source: [source\chapters\ch04-the-derivative\sections\sec-4-2-instantaneous-rate-of-change.xml](../../source\chapters\ch04-the-derivative\sections\sec-4-2-instantaneous-rate-of-change.xml)

Flag: Replace vague metaphors, repetition, or introductory filler with the section concept and conditions.

**Before**

> Average velocity looks across an interval. Instantaneous velocity looks at one time. That sounds impossible at first. If there is only one time, there is no change in time, and a quotient like \frac{\text{change in position}}{\text{change in time}} would have denominator 0. The way out is not to divide by 0. The way out is to divide by a nonzero time change h, and then let h approach 0.

**After**

Average velocity is displacement divided by elapsed time. Instantaneous velocity is the limit of this quotient as the nonzero time interval shrinks to zero. We take a limit; we do not evaluate the quotient with a zero denominator.

## 17. The derivative as a function

Source: [source\chapters\ch04-the-derivative\sections\sec-4-3-the-derivative-as-a-function.xml](../../source\chapters\ch04-the-derivative\sections\sec-4-3-the-derivative-as-a-function.xml)

Flag: Replace vague metaphors, repetition, or introductory filler with the section concept and conditions.

**Before**

> Section [cross-reference] gave the derivative at one point. For example, f(x)=x^2 has f'(2)=4. That number is the slope of one tangent line. But a curve has many points, and the slope usually changes from point to point. If the point moves, the derivative moves with it. So the derivative is not only a number. It is also a new function.

**After**

At each input where a function is differentiable, its derivative gives the tangent slope. Collecting these values defines a new function, f\prime. For f(x)=x^2, the derivative function is f\prime(x)=2x, so in particular f\prime(2)=4.

## 18. Local linear approximation

Source: [source\chapters\ch04-the-derivative\sections\sec-4-4-local-linear-approximation.xml](../../source\chapters\ch04-the-derivative\sections\sec-4-4-local-linear-approximation.xml)

Flag: Replace vague metaphors, repetition, or introductory filler with the section concept and conditions.

**Before**

> The derivative function records many slopes. At a single point, the derivative does something even more practical: it gives the best linear model of the function near that point. A curved graph may be difficult. A line is simple. Calculus lets us replace a curve by a line, as long as we stay close enough to the point of tangency.

**After**

If f is differentiable at a, the tangent line gives the local approximation f(x)\approx f(a)+f\prime(a)(x-a). We will describe how the approximation error behaves as x\to a and use it to estimate changes in function values.

## 19. Differentiability and continuity

Source: [source\chapters\ch04-the-derivative\sections\sec-4-5-differentiability-and-continuity.xml](../../source\chapters\ch04-the-derivative\sections\sec-4-5-differentiability-and-continuity.xml)

Flag: Replace vague metaphors, repetition, or introductory filler with the section concept and conditions.

**Before**

> Local linear approximation ended with the formula f(a+h)=f(a)+f'(a)h+E(h), \qquad \frac{E(h)}{h}\to0. This says that, near a, a differentiable function behaves like a line. A line cannot jump. So a differentiable function cannot jump either. That is our first structural theorem about derivatives: \text{differentiability is stronger than continuity.}

**After**

Differentiability at a givesf(a+h)=f(a)+f\prime(a)h+E(h),\qquad E(h)/h\to0.The terms f\prime(a)h and E(h) both tend to zero. Hence f(a+h)\to f(a): differentiability implies continuity. The converse fails, as the examples below show.

## 20. Motion revisited

Source: [source\chapters\ch04-the-derivative\sections\sec-4-7-motion-revisited.xml](../../source\chapters\ch04-the-derivative\sections\sec-4-7-motion-revisited.xml)

Flag: Replace vague metaphors, repetition, or introductory filler with the section concept and conditions.

**Before**

> The derivative began as velocity. Then it became slope, local linear approximation, and a function of position along a graph. Now the original motion story returns, but with sharper language. A position function tells where an object is. Its derivative tells how fast that position is changing. The derivative of the derivative tells how fast the velocity is changing.

**After**

For a position function s(t), velocity is v(t)=s\prime(t) and acceleration is a(t)=v\prime(t), wherever these derivatives exist. We will use their signs and units to describe direction, speed, and changes in speed.

## 21. Warning examples

Source: [source\chapters\ch04-the-derivative\sections\sec-4-8-warning-examples.xml](../../source\chapters\ch04-the-derivative\sections\sec-4-8-warning-examples.xml)

Flag: Replace vague metaphors, repetition, or introductory filler with the section concept and conditions.

**Before**

> Motion gives the derivative a natural meaning. It also shows why the derivative is a demanding idea. A position can be continuous and still have no velocity at one instant. A derivative can exist and still behave badly nearby. A graph can look harmless because the picture has missed the trouble. These examples are not exceptions to the theory. They are the reason the definitions were made carefully.

**After**

A continuous function need not be differentiable, and a derivative need not be continuous. These examples distinguish those properties and show why a sampled graph cannot establish differentiability.

## 22. Constant velocity: where slope and area first meet

Source: [source\chapters\ch01-velocity-distance-and-the-first-shape-of-calculus\sections\sec-1-2-constant-velocity-where-slope-and-area-first-meet.xml](../../source\chapters\ch01-velocity-distance-and-the-first-shape-of-calculus\sections\sec-1-2-constant-velocity-where-slope-and-area-first-meet.xml)

Flag: Replace a backward-looking setup with the assumption being studied.

**Before**

> The dashboard gave us two questions. Constant velocity is the first case where both questions can be answered without any limiting process.

**After**

With constant velocity, displacement is velocity multiplied by elapsed time. The position graph has constant slope, and the velocity graph gives a rectangle whose area is the displacement.

## 23. Forward, backward, and signed motion

Source: [source\chapters\ch01-velocity-distance-and-the-first-shape-of-calculus\sections\sec-1-3-forward-backward-and-signed-motion.xml](../../source\chapters\ch01-velocity-distance-and-the-first-shape-of-calculus\sections\sec-1-3-forward-backward-and-signed-motion.xml)

Flag: Remove the dashboard-story metaphor.

**Before**

> Constant velocity gave us the first picture of calculus: slope on one graph and area on another. But we quietly assumed that the car only moved forward. The moment a car can reverse, the dashboard story needs one more idea.

**After**

When motion can reverse direction, speed alone does not describe it. Signed velocity records both how fast an object moves and which direction it moves.

## 24. Calculus without limits: finite differences and finite sums

Source: [source\chapters\ch01-velocity-distance-and-the-first-shape-of-calculus\sections\sec-1-4-calculus-without-limits-finite-differences-and-finite-sums.xml](../../source\chapters\ch01-velocity-distance-and-the-first-shape-of-calculus\sections\sec-1-4-calculus-without-limits-finite-differences-and-finite-sums.xml)

Flag: Replace an arithmetic-core slogan with the operation.

**Before**

> Signed motion taught us to add changes with their signs. Now we strip the story down to its arithmetic core.

**After**

A finite difference measures the change between two recorded positions. Adding successive signed changes gives the total displacement.

## 25. Completeness and the idea of no gaps

Source: [source\chapters\ch02-numbers-functions-and-models\sections\sec-2-2-completeness-and-the-idea-of-no-gaps.xml](../../source\chapters\ch02-numbers-functions-and-models\sections\sec-2-2-completeness-and-the-idea-of-no-gaps.xml)

Flag: Replace a vague promise with the completeness question.

**Before**

> The last section used the real line as if every point on it had a number. That is a stronger promise than it may first appear.

**After**

Rational numbers do not supply every point needed for limits. Completeness is the property of the real numbers that ensures bounded increasing approximations have a real limit.

## 26. Models before calculus

Source: [source\chapters\ch02-numbers-functions-and-models\sections\sec-2-7-models-before-calculus.xml](../../source\chapters\ch02-numbers-functions-and-models\sections\sec-2-7-models-before-calculus.xml)

Flag: Remove a metaphor while retaining the definition and checks.

**Before**

> A model is not the same thing as reality. It is a mathematical story about reality. A good model respects units, captures the main pattern, and makes predictions we can test.

**After**

A mathematical model represents selected features of a situation under stated assumptions. Its units should be consistent, and its predictions should be checked against data.

## 27. Technology and graphs

Source: [source\chapters\ch02-numbers-functions-and-models\sections\sec-2-8-technology-and-graphs.xml](../../source\chapters\ch02-numbers-functions-and-models\sections\sec-2-8-technology-and-graphs.xml)

Flag: Replace a partnership slogan with concrete limitations.

**Before**

> The right attitude is not distrust. It is partnership.

**After**

Check features suggested by a plotted graph using the formula, the sampling resolution, and the chosen viewing window.

## 28. The Fundamental Theorem of Calculus

Source: [source\chapters\ch09-the-fundamental-theorem-of-calculus\ch09-the-fundamental-theorem-of-calculus.ptx](../../source\chapters\ch09-the-fundamental-theorem-of-calculus\ch09-the-fundamental-theorem-of-calculus.ptx)

Flag: Replace generic transitions, metaphors, or promotional claims with the method and its mathematical conditions.

**Before**

> Chapter [cross-reference] built the integral as accumulated signed change: \int_a^b f(x)\,dx. At first this integral was a number. It accumulated from one fixed endpoint to another. Now we let one endpoint move. That small change turns the integral into a function. The surprise is that this new function has a derivative, and its derivative is the function we started with. accumulate f \Longrightarrow differentiate the accumulation \Longrightarrow f. This is the first half of the Fundamental Theorem of Calculus.

**After**

For a continuous function f, the accumulation function A(x)=\int_a^x f(t)\,dt has derivative A\prime(x)=f(x). Conversely, an antiderivative F evaluates a definite integral by \int_a^b f=F(b)-F(a). This chapter proves these two parts of the Fundamental Theorem and develops antiderivatives and substitution.

## 29. Fundamental Theorem, Part II

Source: [source\chapters\ch09-the-fundamental-theorem-of-calculus\sections\sec-9-3-fundamental-theorem-part-ii.xml](../../source\chapters\ch09-the-fundamental-theorem-of-calculus\sections\sec-9-3-fundamental-theorem-part-ii.xml)

Flag: Replace generic transitions, metaphors, or promotional claims with the method and its mathematical conditions.

**Before**

> Part I told us something surprising: A(x)=\int_a^x f(t)\,dt \quad\Longrightarrow\quad A'(x)=f(x), provided f is continuous. So accumulation creates an antiderivative. Now we reverse the question. Suppose we already know an antiderivative of f. Can we use it to compute the definite integral \int_a^b f(x)\,dx without returning to Riemann sums? The answer is yes. This is the computational half of the Fundamental Theorem.

**After**

The first part of the Fundamental Theorem produces an antiderivative by integration. The second part evaluates an integral using any antiderivative: if F\prime=f on the interval and f is continuous, then \int_a^b f(x)\,dx=F(b)-F(a). This avoids calculating a limit of Riemann sums separately for every integral.

## 30. Indefinite integrals

Source: [source\chapters\ch09-the-fundamental-theorem-of-calculus\sections\sec-9-4-indefinite-integrals.xml](../../source\chapters\ch09-the-fundamental-theorem-of-calculus\sections\sec-9-4-indefinite-integrals.xml)

Flag: Replace generic transitions, metaphors, or promotional claims with the method and its mathematical conditions.

**Before**

> Part II says that definite integrals can be evaluated by antiderivatives: \int_a^b f(x)\,dx=F(b)-F(a), \qquad F'=f. So integration now has two faces. One face is accumulation: \int_a^b f(x)\,dx. This is a number. The other face is antiderivatives: \text{find all functions }F\text{ such that }F'=f. That second task needs notation.

**After**

A definite integral gives a number. An indefinite integral denotes the family of antiderivatives of a function. On an interval, all antiderivatives of the same function differ by a constant. We will use this fact to write and check indefinite-integral formulas.

## 31. Differential notation and oriented length

Source: [source\chapters\ch09-the-fundamental-theorem-of-calculus\sections\sec-9-5-differential-notation-and-oriented-length.xml](../../source\chapters\ch09-the-fundamental-theorem-of-calculus\sections\sec-9-5-differential-notation-and-oriented-length.xml)

Flag: Replace generic transitions, metaphors, or promotional claims with the method and its mathematical conditions.

**Before**

> The reverse chain rule suggests a powerful substitution pattern, which we develop in this section: \int f(g(u))g'(u)\,du. At first this may look like a trick with symbols. But the symbols are trying to say something geometric. When x=g(u), a small step in u produces a small step in x: dx=g'(u)\,du. So the expression f(x)\,dx is not just a function f(x) with decoration attached. It is the small accumulated amount: \text{height}\times\text{oriented width}. This section slows down the notation so that later formulas feel less mysterious.

**After**

Substitution follows from the chain rule. When x=g(u), the expression dx=g\prime(u)\,du records the factor that converts the integrand to the new variable:f(x)\,dx=f(g(u))g\prime(u)\,du.The sign of g\prime records orientation. In a definite integral, the endpoints must also be expressed in the new variable.

## 32. Warning examples

Source: [source\chapters\ch09-the-fundamental-theorem-of-calculus\sections\sec-9-6-warning-examples.xml](../../source\chapters\ch09-the-fundamental-theorem-of-calculus\sections\sec-9-6-warning-examples.xml)

Flag: Replace generic transitions, metaphors, or promotional claims with the method and its mathematical conditions.

**Before**

> This section gathers the most common traps: a discontinuity in f, old limits after substitution, treating an integral like multiplication, and confusing signed area with ordinary area. A theorem is useful only when we know where it applies.

**After**

These examples examine four common errors: applying the Fundamental Theorem across a discontinuity, retaining old endpoints after substitution, treating an integral as a product, and confusing a signed integral with ordinary area.

## 33. Chapter review and discovery problems

Source: [source\chapters\ch09-the-fundamental-theorem-of-calculus\sections\sec-9-7-chapter-review-and-discovery-problems.xml](../../source\chapters\ch09-the-fundamental-theorem-of-calculus\sections\sec-9-7-chapter-review-and-discovery-problems.xml)

Flag: Replace generic transitions, metaphors, or promotional claims with the method and its mathematical conditions.

**Before**

> This chapter began with a moving endpoint: A(x)=\int_a^x f(t)\,dt. That small change turned an integral from a number into a function. Then the Fundamental Theorem revealed the main hinge of calculus: \text{accumulation and instantaneous change undo each other.} Part I says that differentiating an accumulation gives back the integrand: \frac{d}{dx}\int_a^x f(t)\,dt=f(x). Part II says that integrating a derivative gives net change: \int_a^b F'(x)\,dx=F(b)-F(a). These are not two unrelated formulas. They are the same story read in opposite directions.

**After**

The Fundamental Theorem relates differentiation to integration. For continuous f, differentiating \int_a^x f(t)\,dt gives f(x); integrating a continuous derivative gives F(b)-F(a). The review problems apply these results to accumulation functions, antiderivatives, and substitutions, with attention to domains and hypotheses.

## 34. What Integrals Measure

Source: [source\chapters\ch10-what-integrals-measure\ch10-what-integrals-measure.ptx](../../source\chapters\ch10-what-integrals-measure\ch10-what-integrals-measure.ptx)

Flag: Replace generic transitions, metaphors, or promotional claims with the method and its mathematical conditions.

**Before**

> In Chapter [cross-reference], the foundational slice was a rectangle: \text{height}\cdot\text{width}. Moving forward, the geometry of the slice will adapt to the problem. For the area between curves, the slice is a vertical strip. For the volume of a solid, the slice is a thin cross-section. Geometry is only the beginning. Integrals can just as easily accumulate mass, mechanical work, fluid pressure, or probability. In every new application, the formula and units of the slice will change. But while the definition of the slice varies wildly from problem to problem, the underlying architecture of the calculus does not. Every application relies on the exact same sequence: isolate a differential slice, approximate its contribution, and integrate to accumulate the total.

**After**

To set up an integral for a total quantity, identify the contribution of a small piece and add those contributions over the relevant interval. For volume, the contribution is cross-sectional area times thickness. For mass, it is density times length or area. This chapter develops that approach for geometric quantities, work, fluid force, averages, and probability, with units used to check each formula.

## 35. Area between curves

Source: [source\chapters\ch10-what-integrals-measure\sections\sec-10-1-area-between-curves.xml](../../source\chapters\ch10-what-integrals-measure\sections\sec-10-1-area-between-curves.xml)

Flag: Replace generic transitions, metaphors, or promotional claims with the method and its mathematical conditions.

**Before**

> Area under a graph measures the region between the graph and the x-axis. But the x-axis is only one possible lower boundary. Often a region lies between two curves. Then the vertical thickness of a small strip is not “height above the axis.” It is \text{top value}-\text{bottom value}. That is the first new small piece.

**After**

The area between two curves can be computed by adding thin strips. For vertical strips, the height is the upper function minus the lower function; for horizontal strips, the width is the right boundary minus the left boundary. Split the region where the order of the boundaries changes.

## 36. Differentiation Rules and Elementary Functions

Source: [source\chapters\ch05-differentiation-rules-and-elementary-functions\ch05-differentiation-rules-and-elementary-functions.ptx](../../source\chapters\ch05-differentiation-rules-and-elementary-functions\ch05-differentiation-rules-and-elementary-functions.ptx)

Flag: Replace personification, slogans, or repeated setup with the operation, application, and hypotheses.

**Before**

> The derivative came from a limit: f'(x)=\lim_{h\to0}\frac{f(x+h)-f(x)}{h}. That definition gives the meaning. It gives instantaneous rate of change, tangent slope, and local linear approximation. But it is too slow to use from the beginning every time. The last chapter already gave the first formulas: \frac{d}{dx}(c)=0, \qquad \frac{d}{dx}(x^n)=nx^{n-1} for positive integer powers n. Now we turn those first formulas into a working language. A complicated function is often built from simpler functions. The question is: \text{If we know how the pieces change, how does the whole expression change?}

**After**

Differentiation rules let us find derivatives without evaluating the defining limit each time. This chapter develops rules for sums, products, quotients, compositions, implicit relations, and inverse functions, then applies them to the elementary functions. The appropriate rule depends on how the function is formed and where it is defined.

## 37. The algebra of derivatives

Source: [source\chapters\ch05-differentiation-rules-and-elementary-functions\sections\sec-5-1-the-algebra-of-derivatives.xml](../../source\chapters\ch05-differentiation-rules-and-elementary-functions\sections\sec-5-1-the-algebra-of-derivatives.xml)

Flag: Replace personification, slogans, or repeated setup with the operation, application, and hypotheses.

**Before**

> Some ways of building functions are gentle. Multiplying by a constant, adding two functions, and subtracting two functions do not create any hidden interaction. Their derivatives behave exactly as we hope. This is the first algebra of derivatives.

**After**

The derivative of a sum is the sum of the derivatives. Multiplication by a constant also passes through differentiation. We will prove these rules from the limit definition and use them to differentiate polynomials.

## 38. The chain rule

Source: [source\chapters\ch05-differentiation-rules-and-elementary-functions\sections\sec-5-3-the-chain-rule.xml](../../source\chapters\ch05-differentiation-rules-and-elementary-functions\sections\sec-5-3-the-chain-rule.xml)

Flag: Replace personification, slogans, or repeated setup with the operation, application, and hypotheses.

**Before**

> The product rule handled functions built side by side: f(x)g(x). Composition is more hidden. One function changes because another function inside it changes first: f(g(x)). This happens constantly. A temperature changes because position changes. A cost changes because production changes. A population changes because time changes. The outside quantity does not see x directly. It sees an intermediate quantity.

**After**

In a composition f(g(x)), a change in x first changes g(x), which then changes the output of f. The chain rule multiplies the derivative of the outer function, evaluated at g(x), by the derivative of the inner function.

## 39. Derivatives of trigonometric functions

Source: [source\chapters\ch05-differentiation-rules-and-elementary-functions\sections\sec-5-5-derivatives-of-trigonometric-functions.xml](../../source\chapters\ch05-differentiation-rules-and-elementary-functions\sections\sec-5-5-derivatives-of-trigonometric-functions.xml)

Flag: Replace personification, slogans, or repeated setup with the operation, application, and hypotheses.

**Before**

> The chain rule let us follow change through layers. Implicit differentiation let us find slopes on curves that were not solved for y. But many motions are not built from powers and products. They repeat. A wheel turns. A pendulum swings. A spring moves down, then up, then down again. The functions that describe repeating motion are sine and cosine. The surprise is that their derivatives are not new functions. They are sine and cosine again, shifted and signed.

**After**

Sine and cosine describe periodic behavior such as rotation and oscillation. Their derivatives are (\sin x)\prime=\cos x and (\cos x)\prime=-\sin x when angles are measured in radians. We will derive these formulas from limits and use them to differentiate the remaining trigonometric functions.

## 40. Derivatives of exponential and logarithmic functions

Source: [source\chapters\ch05-differentiation-rules-and-elementary-functions\sections\sec-5-6-derivatives-of-exponential-and-logarithmic-functions.xml](../../source\chapters\ch05-differentiation-rules-and-elementary-functions\sections\sec-5-6-derivatives-of-exponential-and-logarithmic-functions.xml)

Flag: Replace personification, slogans, or repeated setup with the operation, application, and hypotheses.

**Before**

> Sine and cosine return to themselves after differentiation, with a shift and a sign. Exponential functions are even more direct. The right exponential function returns exactly to itself. That one fact explains why exponentials appear whenever the rate of change depends on the current amount.

**After**

The function e^x equals its own derivative. Consequently, exponentials describe quantities whose rates of change are proportional to their current values. We will derive exponential and logarithmic derivative formulas, with their domains stated explicitly.

## 41. Inverse functions and inverse trigonometric functions

Source: [source\chapters\ch05-differentiation-rules-and-elementary-functions\sections\sec-5-7-inverse-functions-and-inverse-trigonometric-functions.xml](../../source\chapters\ch05-differentiation-rules-and-elementary-functions\sections\sec-5-7-inverse-functions-and-inverse-trigonometric-functions.xml)

Flag: Replace personification, slogans, or repeated setup with the operation, application, and hypotheses.

**Before**

> The last section found the derivative of \ln x by reversing the exponential function: y=\ln x \qquad\Longleftrightarrow\qquad x=e^y. That was not a special trick. It was the first example of a general idea. If a function can be reversed, then its derivative tells us the derivative of the reverse function. The two slopes are reciprocals, but at corresponding points.

**After**

The derivative of an inverse function is the reciprocal of the original derivative at the corresponding input, provided that derivative is nonzero. We will justify this relation and apply it to inverse trigonometric functions. Choosing the inverse branch is necessary to specify both its domain and its derivative.

## 42. General power rule and hyperbolic functions

Source: [source\chapters\ch05-differentiation-rules-and-elementary-functions\sections\sec-5-8-general-power-rule-and-hyperbolic-functions.xml](../../source\chapters\ch05-differentiation-rules-and-elementary-functions\sections\sec-5-8-general-power-rule-and-hyperbolic-functions.xml)

Flag: Replace personification, slogans, or repeated setup with the operation, application, and hypotheses.

**Before**

> The power rule first appeared for positive integer powers: \frac{d}{dx}x^n=nx^{n-1}. Then negative powers came from the reciprocal rule, and fractional-looking powers appeared through roots. But the formula is larger than all of those cases. It works for any real exponent, as long as the function is defined and differentiable. The logarithm gives the cleanest proof.

**After**

For x>0, logarithms extend the power rule to every real exponent: (x^r)\prime=rx^{r-1}. This section proves that result, defines hyperbolic functions using exponentials, and develops their identities, inverses, and derivatives.

## 43. Warning examples

Source: [source\chapters\ch05-differentiation-rules-and-elementary-functions\sections\sec-5-9-warning-examples.xml](../../source\chapters\ch05-differentiation-rules-and-elementary-functions\sections\sec-5-9-warning-examples.xml)

Flag: Replace personification, slogans, or repeated setup with the operation, application, and hypotheses.

**Before**

> This chapter has given us speed. We no longer need to return to the limit definition every time we differentiate. We have rules. That speed is useful, but it also creates a danger. A rule that is remembered only as a symbol can be used in the wrong place. The safest way to use derivative rules is to keep asking: \text{How was this function built?} A sum, a product, a quotient, a composition, and an inverse are different constructions. Their derivatives are different because their changes are different.

**After**

Sums, products, quotients, compositions, and inverses require different differentiation rules. These examples show common errors in choosing a rule, applying the chain rule, and ignoring a function's domain.

## 44. Chapter review and discovery problems

Source: [source\chapters\ch05-differentiation-rules-and-elementary-functions\sections\sec-5-10-chapter-review-and-discovery-problems.xml](../../source\chapters\ch05-differentiation-rules-and-elementary-functions\sections\sec-5-10-chapter-review-and-discovery-problems.xml)

Flag: Replace personification, slogans, or repeated setup with the operation, application, and hypotheses.

**Before**

> Chapter 4 defined the derivative: f'(a)=\lim_{h\to0}\frac{f(a+h)-f(a)}{h}. That definition gave meaning, but it was too slow for everyday use. Chapter 5 built a working language. We learned how derivatives behave under algebra, composition, implicit relations, inverse functions, and the elementary functions. The point was not to memorize a long table. The point was to read structure.

**After**

The review problems combine derivative rules with elementary functions, implicit relations, and inverse functions. Identify the structure of each expression before differentiating, and state the domain where the resulting formula applies.

## 45. Shape, Extremes, and the Mean Value Theorem

Source: [source\chapters\ch06-shape-extremes-and-the-mean-value-theorem\ch06-shape-extremes-and-the-mean-value-theorem.ptx](../../source\chapters\ch06-shape-extremes-and-the-mean-value-theorem\ch06-shape-extremes-and-the-mean-value-theorem.ptx)

Flag: Replace personification, slogans, or repeated setup with the operation, application, and hypotheses.

**Before**

> Chapter 5 gave us a working language for derivatives. We learned how to differentiate sums, products, quotients, compositions, inverse functions, and the elementary functions. That language is useful because a derivative is more than a formula. It is information about shape. If f'(x)>0, then the graph wants to rise. If f'(x)<0, then the graph wants to fall. If f'(x)=0, then the graph has a horizontal tangent. A horizontal tangent may mark a high point, a low point, or only a momentary pause. This chapter asks how far we can push that idea. \text{derivative information} \quad\Longrightarrow\quad \text{shape information}. The answer will lead to one of the central theorems of differential calculus: the Mean Value Theorem.

**After**

Derivatives describe more than rates of change. Their signs determine intervals of increase and decrease, and second derivatives describe concavity. This chapter connects derivative information to extrema and graph shape, proves Rolle's Theorem and the Mean Value Theorem, and applies these results to limits and estimates.

## 46. Concavity and second derivatives

Source: [source\chapters\ch06-shape-extremes-and-the-mean-value-theorem\sections\sec-6-4-concavity-and-second-derivatives.xml](../../source\chapters\ch06-shape-extremes-and-the-mean-value-theorem\sections\sec-6-4-concavity-and-second-derivatives.xml)

Flag: Replace personification, slogans, or repeated setup with the operation, application, and hypotheses.

**Before**

> The first derivative tells whether a function is rising or falling. It does not tell the whole shape. A car can move forward while speeding up. It can also move forward while slowing down. In both cases the velocity is positive, but the motion feels different. Graphs have the same distinction. A graph can be increasing while bending upward, or increasing while bending downward. The second derivative measures that bending.

**After**

The first derivative describes whether a function increases or decreases. The second derivative describes how its slope changes. An increasing slope gives concave-up behavior, and a decreasing slope gives concave-down behavior. For motion, this distinction separates positive velocity from positive acceleration.

## 47. Graph sketching with calculus

Source: [source\chapters\ch06-shape-extremes-and-the-mean-value-theorem\sections\sec-6-5-graph-sketching-with-calculus.xml](../../source\chapters\ch06-shape-extremes-and-the-mean-value-theorem\sections\sec-6-5-graph-sketching-with-calculus.xml)

Flag: Replace personification, slogans, or repeated setup with the operation, application, and hypotheses.

**Before**

> The first derivative tells where a graph rises and falls. The second derivative tells where it bends upward and downward. A graph sketch is not a guess. It is a summary of evidence. f' \quad\text{gives direction,} f'' \quad\text{gives bending,} and limits tell what happens near breaks and far away. The goal is not to draw a perfect picture. The goal is to draw a picture that tells the truth.

**After**

A graph sketch combines the domain, intercepts, limits, derivative signs, extrema, and concavity. We will organize this information to draw a graph consistent with the function's formulas and limiting behavior.

## 48. Warning examples

Source: [source\chapters\ch06-shape-extremes-and-the-mean-value-theorem\sections\sec-6-7-warning-examples.xml](../../source\chapters\ch06-shape-extremes-and-the-mean-value-theorem\sections\sec-6-7-warning-examples.xml)

Flag: Replace personification, slogans, or repeated setup with the operation, application, and hypotheses.

**Before**

> The last few sections gave us strong tools: \text{Fermat's theorem, Rolle's theorem, the Mean Value Theorem,} \text{the first derivative test, the second derivative test, and l'Hospital's Rule.} Each one has a boundary. A theorem is useful only when its hypotheses are true. This section collects the warning examples in one place, so the rules are easier to use and harder to misuse.

**After**

The conclusions of Rolle's Theorem, the Mean Value Theorem, derivative tests for extrema, and l'Hospital's Rule depend on their hypotheses. The examples below show failures caused by missing continuity, differentiability, endpoint conditions, or sign conditions.

## 49. Chapter review and discovery problems

Source: [source\chapters\ch06-shape-extremes-and-the-mean-value-theorem\sections\sec-6-8-chapter-review-and-discovery-problems.xml](../../source\chapters\ch06-shape-extremes-and-the-mean-value-theorem\sections\sec-6-8-chapter-review-and-discovery-problems.xml)

Flag: Replace personification, slogans, or repeated setup with the operation, application, and hypotheses.

**Before**

> This chapter began with a simple observation: f'(x)>0 \text{ means rising}, \qquad f'(x)<0 \text{ means falling}. That observation grew into a much larger picture. The derivative gives more than instantaneous rate. It gives shape, turning, bending, bounds, and sometimes limits.

**After**

These problems use derivatives to determine monotonicity, extrema, and concavity; sketch graphs; prove estimates with the Mean Value Theorem; and evaluate limits with l'Hospital's Rule when its hypotheses hold.

## 50. Optimization, Related Rates, and Models

Source: [source\chapters\ch07-optimization-related-rates-and-models\ch07-optimization-related-rates-and-models.ptx](../../source\chapters\ch07-optimization-related-rates-and-models\ch07-optimization-related-rates-and-models.ptx)

Flag: Replace personification, slogans, or repeated setup with the operation, application, and hypotheses.

**Before**

> The last chapter taught us how to read a graph from its derivatives. We used f' to find where a function rises and falls, f'' to find how it bends, and the Mean Value Theorem to explain why local derivative information can control a whole interval. Now the questions become more active. \text{How fast is the water level rising?} \text{What dimensions give the largest volume?} \text{What route gives the shortest path?} \text{What price gives the greatest profit?} These are still derivative questions, but they are not only graph questions. They ask us to build a model, read what the derivative says, and then translate the result back into the situation.

**After**

Applications of derivatives begin by expressing the relevant quantities as functions. We will build models for related rates, optimization, measurement error, growth, and least-time paths. In each case, interpret the result using the model's domain, assumptions, and units.

## 51. Related rates

Source: [source\chapters\ch07-optimization-related-rates-and-models\sections\sec-7-1-related-rates.xml](../../source\chapters\ch07-optimization-related-rates-and-models\sections\sec-7-1-related-rates.xml)

Flag: Replace personification, slogans, or repeated setup with the operation, application, and hypotheses.

**Before**

> Some quantities change alone. Many do not. If a balloon is being inflated, its radius changes, its surface area changes, and its volume changes. These quantities are linked. Knowing how fast one changes can tell us how fast another changes. That is the idea of a related rates problem. an equation relating quantities \Longrightarrow an equation relating their rates. The bridge is the chain rule.

**After**

When changing quantities satisfy an equation, differentiating that equation with respect to time relates their rates of change. For example, a balloon's radius, surface area, and volume change together. The chain rule allows one known rate to determine another.

## 52. Optimization problems

Source: [source\chapters\ch07-optimization-related-rates-and-models\sections\sec-7-2-optimization-problems.xml](../../source\chapters\ch07-optimization-related-rates-and-models\sections\sec-7-2-optimization-problems.xml)

Flag: Replace personification, slogans, or repeated setup with the operation, application, and hypotheses.

**Before**

> The previous chapter taught us how to find high and low points of a function. Optimization turns that skill into a method for solving word problems. A real question rarely arrives as \text{maximize } f(x). It arrives as a sentence: \text{Build the largest box from this sheet of cardboard.} \text{Use the least metal for this can.} \text{Enclose the most area with this much fence.} The first task is not calculus. The first task is translation. situation \longrightarrow function \longrightarrow derivative \longrightarrow decision.

**After**

An optimization problem asks for a maximum or minimum under given constraints. First choose variables, determine their allowed values, and express the quantity to be optimized as a function. Then use derivatives and endpoint checks to compare all relevant candidates.

## 53. Linear approximation in applications

Source: [source\chapters\ch07-optimization-related-rates-and-models\sections\sec-7-3-linear-approximation-in-applications.xml](../../source\chapters\ch07-optimization-related-rates-and-models\sections\sec-7-3-linear-approximation-in-applications.xml)

Flag: Replace personification, slogans, or repeated setup with the operation, application, and hypotheses.

**Before**

> Optimization asked for the best choice. Related rates asked how fast quantities change together. Measurements ask a quieter question. \text{If the input is a little wrong, how wrong is the output?} A radius may be measured only to the nearest millimeter. An angle may be off by one degree. A price model may be only an approximation. Calculus gives a first answer through the tangent line. Recall the local linear approximation: f(a+\Delta x)\approx f(a)+f'(a)\Delta x. The derivative is the multiplier that turns a small input change into a small output change. \Delta y\approx f'(a)\Delta x. That is the practical meaning of the derivative in this section.

**After**

A small measurement error in an input produces a corresponding change in the output. If f is differentiable near a, the tangent-line approximation givesf(a+\Delta x)-f(a)\approx f\prime(a)\Delta x.Thus the derivative estimates how sensitive the output is to an input change. We will apply this to measurement errors and explain the limitations of the approximation.

## 54. Exponential growth and decay

Source: [source\chapters\ch07-optimization-related-rates-and-models\sections\sec-7-5-exponential-growth-and-decay.xml](../../source\chapters\ch07-optimization-related-rates-and-models\sections\sec-7-5-exponential-growth-and-decay.xml)

Flag: Replace personification, slogans, or repeated setup with the operation, application, and hypotheses.

**Before**

> Newton’s method used a tangent line to solve an equation. Linear approximation helped us decide how far to move. But many models do not first give an equation like f(x)=0. They give a law about change. A population grows because each individual helps create more individuals. A radioactive substance decays because each atom has a chance to decay. A bank account grows because interest is earned on the current balance. In each case, the rate of change is tied to the amount already present. That leads to the simplest and most important differential equation: y'=ky.

**After**

When a quantity's rate of change is proportional to its current amount, it satisfies y\prime=ky. Positive k gives exponential growth, and negative k gives exponential decay. Population models, radioactive decay, and continuously compounded interest provide examples.

## 55. Logistic growth and limited resources

Source: [source\chapters\ch07-optimization-related-rates-and-models\sections\sec-7-6-logistic-growth-and-limited-resources.xml](../../source\chapters\ch07-optimization-related-rates-and-models\sections\sec-7-6-logistic-growth-and-limited-resources.xml)

Flag: Replace personification, slogans, or repeated setup with the operation, application, and hypotheses.

**Before**

> Exponential growth has no memory of limits. If P'=rP, then a positive population keeps growing faster and faster forever. That can describe the beginning of a process. It cannot describe the whole life of a population in a bounded environment. A petri dish has limited nutrients. A lake has limited space. A rumor has only so many people left to reach. The first correction is simple: \text{growth should slow down as the quantity approaches a maximum size.} That idea leads to the logistic equation.

**After**

The exponential model P\prime=rP, with r>0, allows a positive population to grow without bound. To model limited resources, the logistic equation reduces the per-capita growth rate as the population approaches a carrying capacity.

## 56. Light, time, and extremal principles

Source: [source\chapters\ch07-optimization-related-rates-and-models\sections\sec-7-7-light-time-and-extremal-principles.xml](../../source\chapters\ch07-optimization-related-rates-and-models\sections\sec-7-7-light-time-and-extremal-principles.xml)

Flag: Replace personification, slogans, or repeated setup with the operation, application, and hypotheses.

**Before**

> Optimization problems usually begin with an ordinary choice: a width, a height, a price, a radius, a time. The derivative helps us find the best value of that choice. But some of the most beautiful optimization problems ask for more than a number. They ask for a path. Light gives the simplest surprise. A ray of light reflecting from a mirror behaves as if it has solved an optimization problem. A ray passing from air into water behaves as if it has solved a different one. The calculus is the same calculus we have been using: write the quantity to be minimized, differentiate, set the derivative equal to 0. The meaning is deeper. A law of nature can sometimes be written as a best-choice principle.

**After**

Some optimization problems choose a path rather than a dimension or price. Reflection and refraction can be derived by minimizing travel time within a specified family of paths. We will write the travel time as a function of the crossing or reflection point and use its derivative to find the minimizing path.

## 57. Warning examples

Source: [source\chapters\ch07-optimization-related-rates-and-models\sections\sec-7-8-warning-examples.xml](../../source\chapters\ch07-optimization-related-rates-and-models\sections\sec-7-8-warning-examples.xml)

Flag: Replace personification, slogans, or repeated setup with the operation, application, and hypotheses.

**Before**

> This chapter used derivatives for many practical tasks: related rates, optimization, linear approximation, Newton’s method, growth models, logistic models, and least-time paths. Those methods are powerful. They are also easy to misuse. A derivative answers the question asked by the model. If the model has the wrong domain, the derivative may find an impossible choice. If a point is only locally best, it may lose globally. If Newton’s method begins from a bad guess, the tangent line may lead somewhere unexpected. The warnings below are not exceptions to calculus. They are reminders to read the hypotheses and the situation.

**After**

Derivative calculations must respect the model's domain and constraints. A critical point may be infeasible or only a local optimum, and Newton's method may fail to converge. These examples show how to check those possibilities.

## 58. Chapter review and applications

Source: [source\chapters\ch07-optimization-related-rates-and-models\sections\sec-7-9-chapter-review-and-applications.xml](../../source\chapters\ch07-optimization-related-rates-and-models\sections\sec-7-9-chapter-review-and-applications.xml)

Flag: Replace personification, slogans, or repeated setup with the operation, application, and hypotheses.

**Before**

> This chapter began with a simple change in perspective. Instead of being handed a function and asked to differentiate it, we were asked to build the function first. A ladder slides. A box is folded. A cup cools. A population grows. A light ray chooses a path. In each case, the derivative did not appear at the beginning. It appeared after we translated the situation into mathematics. That is the main skill of the chapter: real situation \longrightarrow mathematical model \longrightarrow derivative information \longrightarrow interpretation. The last step is as important as the first. A derivative answer without units, sign, domain, and meaning is not yet an answer to the problem.

**After**

These problems ask you to formulate models before applying derivatives. Specify the variables, constraints, and units; carry out the calculation; and interpret the result in the original situation.

## 59. The Integral as Accumulation

Source: [source\chapters\ch08-the-integral-as-accumulation\ch08-the-integral-as-accumulation.ptx](../../source\chapters\ch08-the-integral-as-accumulation\ch08-the-integral-as-accumulation.ptx)

Flag: Replace personification, slogans, or repeated setup with the operation, application, and hypotheses.

**Before**

> The last chapter showed how much a derivative can do. A derivative can relate changing quantities, find a best choice, estimate error, and express laws such as T'=-k(T-T_s) or P'=rP\left(1-\frac{P}{K}\right). But a derivative is local. It tells what is happening at an instant. Many questions ask for the accumulated result of those instant-by-instant changes. \text{If velocity is known, how far did the object travel?} \text{If power is used over time, how much energy was used?} \text{If density varies along a rod, what is the rod's total mass?} \text{If a rate of change is known, what is the total change?} These questions return us to the dashboard from the beginning of the book. The speedometer gives a rate. The odometer gives an accumulated amount. Differentiation went from accumulation to rate: \text{position} \longrightarrow \text{velocity}. Integration goes in the opposite direction: \text{velocity} \longrightarrow \text{position change}. This chapter builds the integral from the ground up. We will not begin with antiderivatives. We will begin with the simpler and older idea: break a quantity into small pieces, estimate each piece, and add.

**After**

An integral measures an accumulated quantity. Velocity determines displacement, power determines energy use, and density determines mass. We will approximate each total by dividing an interval into small pieces and adding their contributions, then define the definite integral as a limit of these sums.

## 60. The definite integral

Source: [source\chapters\ch08-the-integral-as-accumulation\sections\sec-8-4-the-definite-integral.xml](../../source\chapters\ch08-the-integral-as-accumulation\sections\sec-8-4-the-definite-integral.xml)

Flag: Replace personification, slogans, or repeated setup with the operation, application, and hypotheses.

**Before**

> Sigma notation made rectangular sums readable. Now we give the limiting process a name. The definite integral is the number that rectangular sums approach when every rectangle becomes thin. \text{finite sum of rectangles} \quad\longrightarrow\quad \text{definite integral}. This definition is the formal version of the accumulation idea that began the chapter.

**After**

A Riemann sum approximates accumulation by adding function values multiplied by subinterval widths. The definite integral is their common limit, when it exists, as the largest subinterval width tends to zero. The limit must be independent of the partitions and sample points.

## 61. Properties of the integral

Source: [source\chapters\ch08-the-integral-as-accumulation\sections\sec-8-6-properties-of-the-integral.xml](../../source\chapters\ch08-the-integral-as-accumulation\sections\sec-8-6-properties-of-the-integral.xml)

Flag: Replace personification, slogans, or repeated setup with the operation, application, and hypotheses.

**Before**

> The integral was born from sums. Its basic properties are inherited from sums. A Riemann sum has the form \sum_{j=1}^{n} f(x_j^*)\Delta x_j. Finite sums are linear. They can be split into pieces. They preserve inequalities. They respect symmetry. When the Riemann sums approach a limit, those same habits survive in the integral. This section is not a list of tricks. It is the arithmetic of accumulation.

**After**

The basic integral properties follow from Riemann sums and their limits. Integrals are linear, can be split at an intermediate endpoint, and preserve inequalities. Symmetry can also simplify calculations when the interval and integrand satisfy the required conditions.

## 62. Existence of integrals

Source: [source\chapters\ch08-the-integral-as-accumulation\sections\sec-8-7-existence-of-integrals.xml](../../source\chapters\ch08-the-integral-as-accumulation\sections\sec-8-7-existence-of-integrals.xml)

Flag: Replace personification, slogans, or repeated setup with the operation, application, and hypotheses.

**Before**

> The last section used the integral as if it were already available. We split it, compared it, averaged it, and used symmetry to simplify it. But one question is still waiting: \text{When does a function actually have a Riemann integral?} For the functions that appear in most applications, the answer is reassuring. Continuous functions are integrable. Monotone functions are integrable. Functions with finitely many jumps are integrable. But boundedness alone is not enough. A function can be bounded and still be too wild for its Riemann sums to settle down. The test is this: \text{Can upper and lower estimates be forced together?}

**After**

A bounded function has a Riemann integral when its upper and lower sums can be made arbitrarily close. This section uses that criterion to establish integrability for continuous functions, monotone functions, and bounded functions with finitely many discontinuities. Boundedness alone is insufficient.

## 63. Area under a graph

Source: [source\chapters\ch08-the-integral-as-accumulation\sections\sec-8-2-area-under-a-graph.xml](../../source\chapters\ch08-the-integral-as-accumulation\sections\sec-8-2-area-under-a-graph.xml)

Flag: Remove a generic claim about usefulness.

**Before**

> When velocity is nonnegative, distance traveled is the area under the velocity graph. That observation is too useful to keep only for motion.

**After**

The area calculation used for nonnegative velocity also applies to any nonnegative integrable function.

## 64. Cylindrical shells

Source: [source\chapters\ch10-what-integrals-measure\sections\sec-10-3-cylindrical-shells.xml](../../source\chapters\ch10-what-integrals-measure\sections\sec-10-3-cylindrical-shells.xml)

Flag: Replace generic transitions, metaphors, or promotional claims with the method and its mathematical conditions.

**Before**

> Disks and washers came from slices perpendicular to the axis of rotation. A vertical slice rotated around the x-axis made a disk or a washer. A horizontal slice rotated around the y-axis did the same. But a slice can also be parallel to the axis of rotation. Then it does not sweep out a disk. It sweeps out a thin cylindrical shell. The small piece changes shape again: \text{shell volume} \approx (\text{circumference})(\text{height})(\text{thickness}). This is the shell method.

**After**

Rotating a strip parallel to the axis produces a thin cylindrical shell. Its volume is approximately circumference times height times thickness:\text{shell volume}\approx2\pi(\text{radius})(\text{height})(\text{thickness}).Integrating these contributions gives the shell method. The radius is the distance from the strip to the rotation axis.

## 65. Work and energy

Source: [source\chapters\ch10-what-integrals-measure\sections\sec-10-5-work-and-energy.xml](../../source\chapters\ch10-what-integrals-measure\sections\sec-10-5-work-and-energy.xml)

Flag: Replace generic transitions, metaphors, or promotional claims with the method and its mathematical conditions.

**Before**

> The last section added small pieces of mass: dm=\lambda(x)\,dx. Now the quantity changes again. A force moves an object through a distance. The small piece is dW=F(x)\,dx. This accumulated quantity is called work. It measures energy transferred by a force through motion.

**After**

Work measures energy transferred by a force through displacement. For a force along a line, a small displacement contributes approximately F(x)\,\Delta x. Integrating the signed force over the displacement gives the total work.

## 66. Hydrostatic force

Source: [source\chapters\ch10-what-integrals-measure\sections\sec-10-6-hydrostatic-force.xml](../../source\chapters\ch10-what-integrals-measure\sections\sec-10-6-hydrostatic-force.xml)

Flag: Replace generic transitions, metaphors, or promotional claims with the method and its mathematical conditions.

**Before**

> Pumping water asked how much work is needed to move water. A dam or a window in a tank asks a different question: \text{How hard does still water push?} The force is not spread evenly. Near the surface, the water pressure is small. Deep below the surface, the pressure is larger. So the small piece changes again: dF=(\text{pressure})(\text{small area}).

**After**

Fluid pressure increases with depth. To compute the force on a submerged surface, divide it into strips narrow enough that the pressure is nearly constant on each strip. Multiply the pressure by the strip area and integrate.

## 67. Average value and probability

Source: [source\chapters\ch10-what-integrals-measure\sections\sec-10-7-average-value-and-probability.xml](../../source\chapters\ch10-what-integrals-measure\sections\sec-10-7-average-value-and-probability.xml)

Flag: Replace generic transitions, metaphors, or promotional claims with the method and its mathematical conditions.

**Before**

> Hydrostatic force added pressure over area: dF=(\text{pressure})(\text{small area}). Work added force over distance: dW=(\text{force})(\text{small displacement}). Mass added density over length or area. Now we ask a quieter question. Suppose a quantity changes over an interval. What single number best represents it? If a car’s velocity changes during a trip, we can still ask for its average velocity. If a temperature changes during a day, we can still ask for the average temperature. If a probability is spread over many possible outcomes, we can still ask for the expected outcome. The integral answers all of these by the same idea: \text{weighted average}=\frac{\text{weighted accumulated amount}}{\text{total weight}}.

**After**

The average value of an integrable function on [a,b], with a<b, is its integral divided by the interval length. Weighted averages replace equal weighting by a density or weight function. Probability densities provide an important application of this distinction.

## 68. Arc length and surface area of revolution

Source: [source\chapters\ch10-what-integrals-measure\sections\sec-10-8-arc-length-and-surface-area-of-revolution.xml](../../source\chapters\ch10-what-integrals-measure\sections\sec-10-8-arc-length-and-surface-area-of-revolution.xml)

Flag: Replace generic transitions, metaphors, or promotional claims with the method and its mathematical conditions.

**Before**

> Area comes from small rectangles. Volume comes from small slices. Work comes from small force-times-distance pieces. Length should come from small straight pieces. A curve is not straight, but if we zoom in far enough, a smooth curve looks almost like a line segment. So the small piece of length is not just dx. It is a slanted distance: ds\approx \sqrt{(dx)^2+(dy)^2}. That is the new small piece.

**After**

Approximate a smooth curve by short line segments to compute its length. For a graph, the Pythagorean theorem gives the length factor \sqrt{1+(dy/dx)^2}. Rotating a short segment about an axis gives a surface-area contribution equal to circumference times segment length.

## 69. Chapter review and applications

Source: [source\chapters\ch10-what-integrals-measure\sections\sec-10-9-chapter-review-and-applications.xml](../../source\chapters\ch10-what-integrals-measure\sections\sec-10-9-chapter-review-and-applications.xml)

Flag: Replace generic transitions, metaphors, or promotional claims with the method and its mathematical conditions.

**Before**

> This chapter has changed the shape of the small piece again and again. At first the small piece was a strip of area: dA=(\text{height})\,dx. Then it became a slice of volume: dV=(\text{cross-sectional area})\,dx. Then it became a shell, a mass element, a moment, a work element, a pressure-force element, a probability element, and a tiny slanted piece of length. The question stayed the same: \text{What is one small piece, and what does it contribute?} That is the main skill of applications of integration.

**After**

The review problems ask you to choose and integrate the contributions that give area, volume, mass, work, fluid force, averages, probability, arc length, and surface area. State the boundaries, check the units, and explain why the chosen integral represents the requested quantity.

## 70. Techniques of Integration

Source: [source\chapters\ch11-techniques-of-integration\ch11-techniques-of-integration.ptx](../../source\chapters\ch11-techniques-of-integration\ch11-techniques-of-integration.ptx)

Flag: Replace generic transitions, metaphors, or promotional claims with the method and its mathematical conditions.

**Before**

> Chapter [cross-reference] showed why integrals appear everywhere. They measure area, volume, work, mass, probability, arc length, and many other accumulated quantities. But setting up an integral and evaluating it are different tasks. Substitution gave us one powerful method. It reverses the chain rule. But many integrals do not come from the chain rule. Some come from the product rule. Some come from trigonometric identities. Some come from algebraic decomposition. And some have no elementary antiderivative at all. So the next question is practical: \text{Once an application gives us an integral, how do we find its value?} The goal of this chapter is not to memorize tricks. The goal is to recognize structure. Every technique in this chapter answers the same question: \text{What derivative rule, identity, or algebraic form produced this integrand?}

**After**

Different integrands require different methods. Substitution reverses the chain rule, integration by parts reverses the product rule, and identities or partial fractions simplify the expression before integration. We will also treat improper integrals as limits and distinguish convergence from the availability of an elementary antiderivative.

## 71. Integration by parts

Source: [source\chapters\ch11-techniques-of-integration\sections\sec-11-1-integration-by-parts.xml](../../source\chapters\ch11-techniques-of-integration\sections\sec-11-1-integration-by-parts.xml)

Flag: Replace generic transitions, metaphors, or promotional claims with the method and its mathematical conditions.

**Before**

> Substitution reverses the chain rule. Integration by parts reverses the product rule. This is the first new method because products occur naturally. Work integrals may contain force times distance. Probability integrals may contain a variable times a density. Arc length and center of mass can also produce products. When an integrand looks like x e^x,\qquad x\cos x,\qquad x^2\ln x, substitution may not know what to do. The product rule does.

**After**

Integration by parts follows from the product rule. It rewrites the integral of one product in terms of another, which may be easier to evaluate. Integrands such as xe^x, x\cos x, and x^2\ln x are typical applications.

## 72. Strategy for integration

Source: [source\chapters\ch11-techniques-of-integration\sections\sec-11-5-strategy-for-integration.xml](../../source\chapters\ch11-techniques-of-integration\sections\sec-11-5-strategy-for-integration.xml)

Flag: Replace generic transitions, metaphors, or promotional claims with the method and its mathematical conditions.

**Before**

> We now have several methods: \text{substitution, integration by parts, trigonometric identities,} \text{trigonometric substitution, and partial fractions.} Each method is useful. None is universal. The hard part is no longer only carrying out a technique. The hard part is recognizing which technique the integral is asking for. That recognition is not magic. It comes from looking for structure. \text{An integration technique is a response to the shape of the integrand.}

**After**

Before choosing a method, simplify the integrand and look for a derivative factor, a product suitable for integration by parts, a useful identity, or a rational expression suitable for partial fractions. No single technique works for every integral. We will compare these choices on examples.

## 73. Computer algebra systems and integral tables

Source: [source\chapters\ch11-techniques-of-integration\sections\sec-11-6-computer-algebra-systems-and-integral-tables.xml](../../source\chapters\ch11-techniques-of-integration\sections\sec-11-6-computer-algebra-systems-and-integral-tables.xml)

Flag: Replace generic transitions, metaphors, or promotional claims with the method and its mathematical conditions.

**Before**

> A computer algebra system can differentiate, integrate, simplify, factor, expand, and solve equations. An integral table can list thousands of antiderivative patterns. These tools are useful. They are also dangerous when used passively. A tool may give an answer that is correct on one interval but not another. It may return an expression that looks different from yours. It may use a special function you have not seen before. It may hide an absolute value. It may even produce a form that is harder to understand than the original problem. So the rule is: \text{Use tools to check and explore, not to surrender judgment.}

**After**

Integral tables and computer algebra systems can suggest antiderivatives and simplify expressions. Check a proposed answer by differentiating it on the relevant domain. Pay particular attention to absolute values, branch choices, singularities, and assumptions that may be implicit in the output.

## 74. Improper integrals

Source: [source\chapters\ch11-techniques-of-integration\sections\sec-11-7-improper-integrals.xml](../../source\chapters\ch11-techniques-of-integration\sections\sec-11-7-improper-integrals.xml)

Flag: Replace generic transitions, metaphors, or promotional claims with the method and its mathematical conditions.

**Before**

> The last section ended with a warning. A definite integral over a closed, finite interval is safe when the integrand is continuous. The interval has finite length, the function stays bounded, and the accumulated amount is a finite number. But many natural accumulations do not fit that safe pattern. A radioactive particle may decay forever. A probability density may stretch over the whole real line. A force law may blow up near a point. A curve may enclose an infinite region whose area is still finite. So we have to ask a more careful question: \text{When does an infinite or singular accumulation have a finite value?} That is the question of improper integrals. An improper integral is not wrong or badly formed. The word improper means that the integral lies outside the original definition and must be interpreted as a limit.

**After**

An integral over an infinite interval, or with an unbounded integrand near an endpoint or interior point, is defined using limits of integrals over finite nonsingular intervals. It converges when every required limit is finite. This section develops comparison tests and distinguishes absolute convergence from convergence caused by cancellation.

## 75. Warning examples

Source: [source\chapters\ch11-techniques-of-integration\sections\sec-11-8-warning-examples.xml](../../source\chapters\ch11-techniques-of-integration\sections\sec-11-8-warning-examples.xml)

Flag: Replace generic transitions, metaphors, or promotional claims with the method and its mathematical conditions.

**Before**

> Improper integrals are limits. That one sentence prevents many errors. The errors below are common because they look like ordinary applications of the Fundamental Theorem of Calculus. But the Fundamental Theorem applies directly only on intervals where the integrand is continuous. When the interval is infinite or the integrand blows up, the limit must be handled first.

**After**

For an improper integral, apply the Fundamental Theorem only on finite nonsingular intervals, then take the required limits. If there is an interior singularity or two infinite tails, treat each piece separately. The examples below show errors caused by skipping these steps.

## 76. Chapter review and discovery problems

Source: [source\chapters\ch11-techniques-of-integration\sections\sec-11-9-chapter-review-and-discovery-problems.xml](../../source\chapters\ch11-techniques-of-integration\sections\sec-11-9-chapter-review-and-discovery-problems.xml)

Flag: Replace generic transitions, metaphors, or promotional claims with the method and its mathematical conditions.

**Before**

> This chapter began with a practical problem: \text{Applications give us integrals. How do we evaluate them?} The answer was not one method. It was a collection of ways to recognize structure. Substitution reverses the chain rule. Integration by parts reverses the product rule. Trigonometric identities reshape trigonometric expressions. Trigonometric substitution uses right triangles to simplify square roots. Partial fractions split rational functions into simpler pieces. Improper integrals add one more demand: before evaluating, we must ask whether the accumulated amount is finite. So the main lesson is not a list of tricks. It is a habit: \text{Read the integrand before choosing a method.}

**After**

These problems combine substitution, integration by parts, trigonometric and hyperbolic identities, partial fractions, and improper-integral tests. Explain the choice of method, check antiderivatives by differentiation, and justify any improper limits.

## 77. Numerical Integration, Error, and Computation

Source: [source\chapters\ch12-numerical-integration-error-and-computation\ch12-numerical-integration-error-and-computation.ptx](../../source\chapters\ch12-numerical-integration-error-and-computation\ch12-numerical-integration-error-and-computation.ptx)

Flag: Replace generic transitions, metaphors, or promotional claims with the method and its mathematical conditions.

**Before**

> The last chapter gave us a large toolbox for exact integration. We learned to look for hidden chain rules, product rules, trigonometric identities, right triangles, partial fractions, and limiting processes. That toolbox is valuable. It is also not the whole story. Some accumulated quantities come from data, not formulas. Some functions have no elementary antiderivative. Some exact answers exist but are less useful than a decimal number with a reliable error bound. So we return to the oldest picture of the integral: \int_a^b f(x)\,dx is an accumulated amount. If we cannot compute it exactly, we can still approximate it. The new question is not only \text{What number do we get?} but also \text{How close is the approximation to the true accumulated amount?}

**After**

Numerical methods approximate integrals, derivatives, and roots when exact calculations are unavailable or inconvenient. We will derive the methods, state the smoothness conditions behind their error estimates, and examine how step size, stopping rules, and rounding affect the results.

## 78. Why approximate integrals?

Source: [source\chapters\ch12-numerical-integration-error-and-computation\sections\sec-12-1-why-approximate-integrals.xml](../../source\chapters\ch12-numerical-integration-error-and-computation\sections\sec-12-1-why-approximate-integrals.xml)

Flag: Replace generic transitions, metaphors, or promotional claims with the method and its mathematical conditions.

**Before**

> A definite integral is an exact idea. Numerical integration is the art of computing a usable approximation to that exact idea. This is not a retreat from calculus. It is one of the main ways calculus is used.

**After**

Numerical integration approximates a definite integral using sampled function values. It is useful when the function is given by data, has no accessible antiderivative, or requires a numerical answer. An approximation should be accompanied by an error bound or a clearly identified error estimate.

## 79. Midpoint and trapezoidal rules

Source: [source\chapters\ch12-numerical-integration-error-and-computation\sections\sec-12-2-midpoint-and-trapezoidal-rules.xml](../../source\chapters\ch12-numerical-integration-error-and-computation\sections\sec-12-2-midpoint-and-trapezoidal-rules.xml)

Flag: Replace generic transitions, metaphors, or promotional claims with the method and its mathematical conditions.

**Before**

> A rectangle is the simplest approximation to area. But there is more than one sensible rectangle, and a rectangle is not the only simple shape. On a short interval [a,b], the graph may not be exactly straight, but it may be close to straight. This suggests two improvements over the roughest left and right rectangle rules: \text{use the value at the midpoint} or \text{connect the endpoint values by a straight line}. These ideas give the midpoint rule and the trapezoidal rule.

**After**

The midpoint rule uses a rectangle whose height is the function value at the midpoint. The trapezoidal rule joins the endpoint values by a line. Applying either rule on many subintervals approximates an integral. We will derive their error bounds under bounds on the second derivative.

## 80. Simpson’s Rule

Source: [source\chapters\ch12-numerical-integration-error-and-computation\sections\sec-12-3-simpson-s-rule.xml](../../source\chapters\ch12-numerical-integration-error-and-computation\sections\sec-12-3-simpson-s-rule.xml)

Flag: Replace generic transitions, metaphors, or promotional claims with the method and its mathematical conditions.

**Before**

> The midpoint and trapezoidal rules replaced the graph by something simple: a horizontal line or a straight line. Those approximations are easy to compute, and their errors are controlled by curvature. But a curve is not usually straight. On a short interval, a better first picture may be a parabola. That is the idea behind Simpson’s Rule. \text{Use a quadratic curve instead of a line.} The reward is surprisingly large. Midpoint and trapezoidal errors usually shrink like 1/n^2. Simpson’s Rule, for smooth functions, usually shrinks like 1/n^4.

**After**

Simpson's rule integrates a quadratic interpolant through two endpoints and their midpoint. Its composite form uses an even number of equal subintervals. When the fourth derivative is bounded, the error is bounded by a constant times the fourth power of the mesh width.

## 81. Numerical differentiation

Source: [source\chapters\ch12-numerical-integration-error-and-computation\sections\sec-12-4-numerical-differentiation.xml](../../source\chapters\ch12-numerical-integration-error-and-computation\sections\sec-12-4-numerical-differentiation.xml)

Flag: Replace generic transitions, metaphors, or promotional claims with the method and its mathematical conditions.

**Before**

> Integration is forgiving. It averages values over an interval. Differentiation is less forgiving. It subtracts nearby values and divides by a small number. That difference matters. If we know a formula for f, exact differentiation may be best. But in experiments, we may only know values from a table. A motion sensor records position. A weather station records temperature. A lab instrument records concentration. We then ask: \text{Can we estimate the instantaneous rate of change from sampled values?} The answer is yes, but with a warning: smaller steps are not always better.

**After**

Finite differences estimate derivatives from sampled values. Their truncation error decreases as the step shrinks under suitable smoothness assumptions, but subtracting nearby values and dividing by a small step can amplify measurement and rounding errors. We will examine this tradeoff.

## 82. Newton’s method revisited

Source: [source\chapters\ch12-numerical-integration-error-and-computation\sections\sec-12-5-newton-s-method-revisited.xml](../../source\chapters\ch12-numerical-integration-error-and-computation\sections\sec-12-5-newton-s-method-revisited.xml)

Flag: Replace generic transitions, metaphors, or promotional claims with the method and its mathematical conditions.

**Before**

> Numerical differentiation taught us a useful warning: a formula can be mathematically correct and still be delicate in computation. Newton’s method has the same personality. Earlier, Newton’s method came from tangent lines. To solve f(x)=0, we replaced the curve by its tangent line at a current guess x_n, then used the x-intercept of that tangent line as the next guess: x_{n+1}=x_n-\frac{f(x_n)}{f'(x_n)}. That formula is simple. The computational questions are not. \text{When should we stop?} \text{How close is the current guess to the root?} \text{What changes when the root is multiple?} \text{What can go wrong if we iterate from a bad starting point?} These are not side questions. They are the questions that turn Newton’s method from a geometric idea into a numerical algorithm.

**After**

Newton's iteration for a root of f isx_{n+1}=x_n-\frac{f(x_n)}{f\prime(x_n)},when the denominator is nonzero. This section examines convergence near a root, error and residual estimates, multiple roots, and stopping rules. It also shows how a poor starting value or a small derivative can cause failure.

## 83. Computing experiments

Source: [source\chapters\ch12-numerical-integration-error-and-computation\sections\sec-12-6-computing-experiments.xml](../../source\chapters\ch12-numerical-integration-error-and-computation\sections\sec-12-6-computing-experiments.xml)

Flag: Replace generic transitions, metaphors, or promotional claims with the method and its mathematical conditions.

**Before**

> Numerical methods become real when we use them. The purpose of these experiments is not only to produce decimals. A calculator can produce decimals. The purpose is to learn how numerical answers behave when the step size changes, when the function becomes less smooth, and when an algorithm is implemented by an actual person or machine. Each experiment follows the same pattern: \text{compute},\qquad \text{compare},\qquad \text{explain}.

**After**

These experiments compare numerical rules on functions with known reference values. Vary the step size, record the errors, and explain how smoothness and rounding affect the observed accuracy. Verify the implementation on simple exact cases before using it on harder examples.

## 84. Chapter review and discovery problems

Source: [source\chapters\ch12-numerical-integration-error-and-computation\sections\sec-12-7-chapter-review-and-discovery-problems.xml](../../source\chapters\ch12-numerical-integration-error-and-computation\sections\sec-12-7-chapter-review-and-discovery-problems.xml)

Flag: Replace generic transitions, metaphors, or promotional claims with the method and its mathematical conditions.

**Before**

> This chapter began with a practical confession: \text{exact integration is powerful, but not always available.} A function may come from data. An antiderivative may not be elementary. A computer may give a decimal but no explanation of how trustworthy the decimal is. So the chapter built a second habit: \text{approximate, then ask how large the error might be.} The rules in this chapter are not only computational recipes. They are controlled ways of replacing a difficult object by a simpler one: \text{a curve by rectangles, trapezoids, or parabolas;} \text{a derivative by a finite difference;} \text{a root by tangent-line iteration.} The common theme is the same theme that has run through the book from the beginning: \text{local information can produce global understanding, if we control the error.}

**After**

These problems compare numerical integration rules, finite-difference derivatives, and Newton iteration. For each approximation, identify the exact quantity, the algorithm, its hypotheses, and the available error evidence.

## 85. Additional topics: Richardson and Romberg methods

Source: [source\chapters\ch12-numerical-integration-error-and-computation\sections\sec-additional-richardson-romberg.xml](../../source\chapters\ch12-numerical-integration-error-and-computation\sections\sec-additional-richardson-romberg.xml)

Flag: Replace generic transitions, metaphors, or promotional claims with the method and its mathematical conditions.

**Before**

> Refining a numerical rule makes its error smaller. If we know how the leading error depends on the step size, two approximations can also cancel that error. This optional section extends the midpoint, trapezoidal, Simpson, and numerical-differentiation methods already developed in this chapter.

**After**

When an approximation has a known leading error term in the step size, two mesh sizes can be combined to cancel that term. This optional section derives Richardson extrapolation and applies it repeatedly to the trapezoidal rule to obtain Romberg integration. The improved orders require the stated error expansion and sufficient smoothness.

## 86. Trigonometric substitution

Source: [source\chapters\ch11-techniques-of-integration\sections\sec-11-3-trigonometric-substitution.xml](../../source\chapters\ch11-techniques-of-integration\sections\sec-11-3-trigonometric-substitution.xml)

Flag: Remove the magic and hidden-geometry metaphor.

**Before**

> The square root does not vanish by magic. It vanishes because a right triangle or a circle was hidden inside it.

**After**

The identities simplify the square root after a branch has been chosen to give the correct sign.

## 87. Differential Equations: Laws Written as Derivatives

Source: [source\chapters\ch13-differential-equations-laws-written-as-derivatives\ch13-differential-equations-laws-written-as-derivatives.ptx](../../source\chapters\ch13-differential-equations-laws-written-as-derivatives\ch13-differential-equations-laws-written-as-derivatives.ptx)

Flag: Replace dramatic framing and repeated narrative with a direct description of the concepts and required checks.

**Before**

> The last chapter was about approximation with responsibility. We approximated accumulated quantities, roots of equations, and derivatives from finite data. Each time, the question was not only what number an algorithm produced, but how much that number could be trusted. Differential equations carry the same lesson into a larger setting. A differential equation does not usually give us the function directly. It gives a law for the function’s derivative. The unknown is not a number. The unknown is a whole function. \text{A differential equation is a law written in the language of change.} We have already seen hints of this idea. Exponential growth was written as P'=kP. Cooling was written as T'=-k(T-T_s). Logistic growth was written as P'=rP\left(1-\frac{P}{K}\right). Those equations say how a quantity changes. Solving them means finding the function whose change obeys the law.

**After**

A differential equation specifies a relation involving an unknown function and its derivatives. Initial conditions specify the starting values. We will formulate rate models, solve several important equation types, and use direction fields and numerical methods when an explicit solution is unavailable.

## 88. Modeling with differential equations

Source: [source\chapters\ch13-differential-equations-laws-written-as-derivatives\sections\sec-13-1-modeling-with-differential-equations.xml](../../source\chapters\ch13-differential-equations-laws-written-as-derivatives\sections\sec-13-1-modeling-with-differential-equations.xml)

Flag: Replace dramatic framing and repeated narrative with a direct description of the concepts and required checks.

**Before**

> A derivative measures an instant-by-instant rate. A differential equation starts when a situation gives that rate before it gives the function. law of change \Longrightarrow equation for a derivative \Longrightarrow unknown function. The direction is different from many earlier problems. We are not given y(t) and asked to find y'(t). We are given information about y'(t) and asked to find y(t).

**After**

To model a changing quantity with a differential equation, express its rate in terms of time, the current state, or other changing quantities. The unknown is the function that satisfies that rate equation and the given initial conditions.

## 89. Euler’s method

Source: [source\chapters\ch13-differential-equations-laws-written-as-derivatives\sections\sec-13-3-euler-s-method.xml](../../source\chapters\ch13-differential-equations-laws-written-as-derivatives\sections\sec-13-3-euler-s-method.xml)

Flag: Replace dramatic framing and repeated narrative with a direct description of the concepts and required checks.

**Before**

> A direction field tells us the slope a solution must have at each point. If we cannot find a formula for the solution, we can still try to follow those slopes. This is an old idea in new clothing. The derivative gives a local linear approximation: y(x+h)\approx y(x)+y'(x)h. If the differential equation says y'=F(x,y), then at the point (x,y), the slope is F(x,y). So one small step should look like y(x+h)\approx y(x)+hF(x,y). Euler’s method is this local linear approximation repeated again and again.

**After**

Euler's method approximates a solution of y\prime=F(t,y) by repeated tangent-line steps. With step size h, it uses y_{n+1}=y_n+hF(t_n,y_n). We will compute these steps and examine how the step size affects accuracy.

## 90. Separable equations

Source: [source\chapters\ch13-differential-equations-laws-written-as-derivatives\sections\sec-13-4-separable-equations.xml](../../source\chapters\ch13-differential-equations-laws-written-as-derivatives\sections\sec-13-4-separable-equations.xml)

Flag: Replace dramatic framing and repeated narrative with a direct description of the concepts and required checks.

**Before**

> Euler’s method follows a differential equation numerically. A separable equation can sometimes be solved by integration. The idea is simple. Some differential equations can be rearranged so that all the y’s are on one side and all the x’s are on the other. Then the equation becomes an integral statement. separate \Longrightarrow integrate \Longrightarrow solve for the constant.

**After**

A separable differential equation has the form y\prime=g(t)h(y). On intervals where h(y)\ne0, divide by h(y) and integrate to obtain an implicit relation between t and y. Check the zeros of h separately, since they may give equilibrium solutions lost by division.

## 91. Logistic and threshold models

Source: [source\chapters\ch13-differential-equations-laws-written-as-derivatives\sections\sec-13-5-logistic-and-threshold-models.xml](../../source\chapters\ch13-differential-equations-laws-written-as-derivatives\sections\sec-13-5-logistic-and-threshold-models.xml)

Flag: Replace dramatic framing and repeated narrative with a direct description of the concepts and required checks.

**Before**

> Separable equations gave us exact formulas when the variables could be pulled apart. But the formula is not always the first thing we should look for. For an autonomous equation y'=f(y), the graph of f already tells a story. It tells where solutions rise, where they fall, and which equilibrium values attract nearby solutions. The logistic equation is the best first example. It can be solved by separation, but it is often understood first from its phase line.

**After**

For an autonomous equation y\prime=f(y), zeros of f give equilibria and its sign determines whether solutions increase or decrease. A phase line organizes this information without requiring an explicit formula. We will apply it to logistic and threshold population models.

## 92. First-order linear equations

Source: [source\chapters\ch13-differential-equations-laws-written-as-derivatives\sections\sec-13-6-first-order-linear-equations.xml](../../source\chapters\ch13-differential-equations-laws-written-as-derivatives\sections\sec-13-6-first-order-linear-equations.xml)

Flag: Replace dramatic framing and repeated narrative with a direct description of the concepts and required checks.

**Before**

> Separable equations can be solved by pulling all y’s to one side and all x’s to the other. Many useful equations do not separate. A tank may have salt entering and salt leaving. A bank account may earn interest while money is also being deposited. A cooling object may sit in a room whose temperature is changing. These models have a common form: \text{rate of change} + \text{known multiple of the current amount} = \text{outside input}. That is the shape of a first-order linear equation.

**After**

A first-order linear equation has the form y\prime+p(t)y=q(t), where p and q are known functions. Such equations model a current amount affected by an outside input, as in mixing tanks, deposits with interest, or cooling in a changing environment. An integrating factor reduces the equation to a product derivative.

## 93. Second-order equations and vibration

Source: [source\chapters\ch13-differential-equations-laws-written-as-derivatives\sections\sec-13-7-second-order-equations-and-vibration.xml](../../source\chapters\ch13-differential-equations-laws-written-as-derivatives\sections\sec-13-7-second-order-equations-and-vibration.xml)

Flag: Replace dramatic framing and repeated narrative with a direct description of the concepts and required checks.

**Before**

> The first-order equations in this chapter described quantities whose rates were governed by their current state or by an outside input. But many physical laws do not begin with velocity. They begin with acceleration. A spring does not merely say where a mass is. It pulls harder when the mass is farther from equilibrium. Newton’s second law then connects that force to acceleration. force \Longrightarrow acceleration \Longrightarrow second derivative. That is why vibrating systems naturally lead to second-order differential equations.

**After**

Newton's second law relates force to acceleration, so motion models often involve the second derivative of position. For a mass attached to a spring, the restoring force gives a second-order equation. We will solve constant-coefficient examples and relate their solutions to oscillation and damping.

## 94. Systems and interaction models

Source: [source\chapters\ch13-differential-equations-laws-written-as-derivatives\sections\sec-13-8-systems-and-interaction-models.xml](../../source\chapters\ch13-differential-equations-laws-written-as-derivatives\sections\sec-13-8-systems-and-interaction-models.xml)

Flag: Replace dramatic framing and repeated narrative with a direct description of the concepts and required checks.

**Before**

> A first-order equation such as y'=f(y) uses one number to describe the current state. A spring needs two numbers: position and velocity. Two interacting populations need two numbers: one for each population. When the state has several components, one differential equation becomes a system. \text{one changing quantity} \quad\Longrightarrow\quad \text{one differential equation}, several changing quantities \Longrightarrow several linked differential equations.

**After**

When the state has several components, their rates form a system of differential equations. A spring can be described by position and velocity; interacting populations require one variable for each population. The equations couple those components through their rates of change.

## 95. Warning examples

Source: [source\chapters\ch13-differential-equations-laws-written-as-derivatives\sections\sec-13-9-warning-examples.xml](../../source\chapters\ch13-differential-equations-laws-written-as-derivatives\sections\sec-13-9-warning-examples.xml)

Flag: Replace dramatic framing and repeated narrative with a direct description of the concepts and required checks.

**Before**

> Differential equations are laws written as derivatives. In this chapter, we learned to read those laws in several ways: direction fields, Euler steps, separation, integrating factors, phase lines. Each method is useful. Each method also has a danger. Before leaving differential equations, we collect three warnings. They are not side remarks. They protect the meaning of the whole chapter. \text{Algebra can lose solutions.} \text{Numerical methods can create false behavior.} \text{A differential equation is not complete without enough starting information.}

**After**

Solving differential equations requires checking for equilibria lost by division, numerical behavior caused by large steps, and the initial data needed to select a solution. The examples below illustrate these three issues. Existence and uniqueness also depend on the slope law; a precise theorem and counterexamples appear in [cross-reference].

## 96. Chapter review and applications

Source: [source\chapters\ch13-differential-equations-laws-written-as-derivatives\sections\sec-13-10-chapter-review-and-applications.xml](../../source\chapters\ch13-differential-equations-laws-written-as-derivatives\sections\sec-13-10-chapter-review-and-applications.xml)

Flag: Replace dramatic framing and repeated narrative with a direct description of the concepts and required checks.

**Before**

> This chapter began with a sentence: \text{A differential equation is a law written in the language of change.} We have now seen several versions of that sentence. A cooling cup obeys a law involving temperature difference. A population obeys a law involving current population and available capacity. A tank obeys a law involving inflow and outflow. A spring obeys a law involving displacement, velocity, and acceleration. Two populations can obey linked laws. The methods differ, but the pattern is the same: \text{model the rate, then understand the function.}

**After**

The review problems ask you to formulate differential equations, use direction fields and phase lines, apply Euler's method, and solve separable, linear, second-order, and coupled equations. State initial conditions and check any solutions excluded by algebraic steps.

## 97. Parametric Curves, Polar Coordinates, and Conics

Source: [source\chapters\ch14-parametric-curves-polar-coordinates-and-conics\ch14-parametric-curves-polar-coordinates-and-conics.ptx](../../source\chapters\ch14-parametric-curves-polar-coordinates-and-conics\ch14-parametric-curves-polar-coordinates-and-conics.ptx)

Flag: Replace dramatic framing and repeated narrative with a direct description of the concepts and required checks.

**Before**

> Differential equations taught us to let time drive a function. A solution might be written as t\longmapsto y(t), where one input t produces one output y. But some curves resist being written as y=f(x). A circle fails the vertical line test. A loop may pass above the same x-value more than once. A point on a wheel can rise, fall, and return to the same horizontal position. The curve is not the problem. The notation is the problem. Instead of forcing one coordinate to depend on the other, we let both coordinates depend on a parameter: x=x(t), \qquad y=y(t). A moving point draws the curve.

**After**

A plane curve need not be the graph of a single function y=f(x). Parametric equations describe both coordinates using one parameter, and polar coordinates describe position using a radius and angle. This chapter develops calculus in these coordinates, studies conic sections and planetary motion, and introduces complex numbers in polar form.

## 98. Parametric curves

Source: [source\chapters\ch14-parametric-curves-polar-coordinates-and-conics\sections\sec-14-1-parametric-curves.xml](../../source\chapters\ch14-parametric-curves-polar-coordinates-and-conics\sections\sec-14-1-parametric-curves.xml)

Flag: Replace dramatic framing and repeated narrative with a direct description of the concepts and required checks.

**Before**

> A graph y=f(x) is one way to describe a curve. A parametric description is another. It is often closer to the way the curve is actually produced. A particle has a horizontal position and a vertical position. A wheel point has an x-coordinate and a y-coordinate. A planet has two coordinates in a plane. In each case, time does not have to appear on the final picture, but it may be the easiest way to draw the picture. \text{A parametric curve is a curve traced by a moving point.}

**After**

A parametric curve is described by coordinate functions x(t) and y(t) on a specified parameter interval. The parameter may represent time, but it need not. The description records how the curve is traced, including its direction and possible repeated traversal.

## 99. Calculus with parametric curves

Source: [source\chapters\ch14-parametric-curves-polar-coordinates-and-conics\sections\sec-14-2-calculus-with-parametric-curves.xml](../../source\chapters\ch14-parametric-curves-polar-coordinates-and-conics\sections\sec-14-2-calculus-with-parametric-curves.xml)

Flag: Replace dramatic framing and repeated narrative with a direct description of the concepts and required checks.

**Before**

> A parametric curve gives two functions: x=x(t), \qquad y=y(t). The graph is drawn in the xy-plane, but the motion is controlled by t. So a slope question must be translated. \text{How fast does \(y\) change with respect to \(x\)?} The parameter tells us two easier facts: \text{how fast \(y\) changes with respect to \(t\),} and \text{how fast \(x\) changes with respect to \(t\).} The slope \dfrac{dy}{dx} is the ratio of those two rates.

**After**

For a differentiable parametric curve (x(t),y(t)), the chain rule gives dy/dx=y\prime(t)/x\prime(t) wherever x\prime(t)\ne0. We will use the coordinate derivatives to find tangents and concavity and examine points where the usual quotient is unavailable.

## 100. Length and area for parametric curves

Source: [source\chapters\ch14-parametric-curves-polar-coordinates-and-conics\sections\sec-14-3-length-and-area-for-parametric-curves.xml](../../source\chapters\ch14-parametric-curves-polar-coordinates-and-conics\sections\sec-14-3-length-and-area-for-parametric-curves.xml)

Flag: Replace dramatic framing and repeated narrative with a direct description of the concepts and required checks.

**Before**

> The last section used the coordinate rates \frac{dx}{dt} \qquad\text{and}\qquad \frac{dy}{dt} to find slope and concavity. Those same rates also measure something more physical: how much distance the moving point travels. A parametric curve is drawn by motion. So its length should come from speed.

**After**

The speed along a differentiable parametric curve is \sqrt{(x\prime(t))^2+(y\prime(t))^2}. Its integral gives the distance traveled over the parameter interval. To compute the geometric curve length or an enclosed area, we must also check how many times the curve is traced.

## 101. Calculus in polar coordinates

Source: [source\chapters\ch14-parametric-curves-polar-coordinates-and-conics\sections\sec-14-5-calculus-in-polar-coordinates.xml](../../source\chapters\ch14-parametric-curves-polar-coordinates-and-conics\sections\sec-14-5-calculus-in-polar-coordinates.xml)

Flag: Replace dramatic framing and repeated narrative with a direct description of the concepts and required checks.

**Before**

> The last section ended with one important observation: r=f(\theta) is already a parametric curve, because x=f(\theta)\cos\theta, \qquad y=f(\theta)\sin\theta. So polar calculus is not a new kind of calculus. It is parametric calculus with the angle \theta as the parameter. The polar picture, however, gives new geometry. A small change in \theta sweeps out a small sector. A small change in r moves the point in or out along a ray. That is why the formulas for slope, area, and length look different from the ones for ordinary graphs.

**After**

A polar curve r=f(\theta) has the parametric description x=f(\theta)\cos\theta, y=f(\theta)\sin\theta. We will use these coordinate formulas to find tangents and lengths, and use circular sectors to derive the polar area formula. The parameter interval determines which parts of the curve are traced and how often.

## 102. Complex numbers and polar form

Source: [source\chapters\ch14-parametric-curves-polar-coordinates-and-conics\sections\sec-14-8-complex-numbers-and-polar-form.xml](../../source\chapters\ch14-parametric-curves-polar-coordinates-and-conics\sections\sec-14-8-complex-numbers-and-polar-form.xml)

Flag: Replace dramatic framing and repeated narrative with a direct description of the concepts and required checks.

**Before**

> Polar coordinates describe a point by distance and angle. Complex numbers give another way to do the same thing. At first this looks like notation. Then multiplication reveals the surprise. In ordinary coordinates, multiplying two points does not make sense. In complex coordinates, multiplying two points means: \text{multiply the distances and add the angles.} That is why complex numbers are so useful for rotation and oscillation.

**After**

A complex number x+iy represents a point in the plane. Its polar form records its distance from the origin and its angle. Multiplication multiplies the distances and adds the angles, so complex numbers provide formulas for scaling and rotation.

## 103. Warning examples

Source: [source\chapters\ch14-parametric-curves-polar-coordinates-and-conics\sections\sec-14-9-warning-examples.xml](../../source\chapters\ch14-parametric-curves-polar-coordinates-and-conics\sections\sec-14-9-warning-examples.xml)

Flag: Replace dramatic framing and repeated narrative with a direct description of the concepts and required checks.

**Before**

> This chapter gave us three new languages for plane curves: x=x(t),\quad y=y(t), r=f(\theta), and z=re^{i\theta}. Each language is powerful because it carries more information than a plain Cartesian equation. It can tell direction, speed, repeated tracing, and rotation. That extra information is useful. It is also dangerous if we forget what the parameters are doing. The safest habit is simple: \text{Before using a formula, ask how the curve is being traced.}

**After**

Parametric and polar formulas depend on how a curve is traced. Repeated traversal can multiply a length or area integral, a zero coordinate derivative can invalidate a slope quotient, and signed radii affect the interpretation of polar coordinates. Check the parameter interval before applying a formula.

## 104. Chapter review and projects

Source: [source\chapters\ch14-parametric-curves-polar-coordinates-and-conics\sections\sec-14-10-chapter-review-and-projects.xml](../../source\chapters\ch14-parametric-curves-polar-coordinates-and-conics\sections\sec-14-10-chapter-review-and-projects.xml)

Flag: Replace dramatic framing and repeated narrative with a direct description of the concepts and required checks.

**Before**

> This chapter began with a simple move: instead of forcing a curve to be a graph y=f(x), let a moving point draw it. That one move opened many doors. A circle could be traced by x=\cos t, \qquad y=\sin t. A rolling wheel produced a cycloid. A rotating ray produced polar coordinates. A focus and directrix produced conics. A point x+iy became a complex number, and multiplication became scaling plus rotation. The theme stayed the same: \text{Choose coordinates that match the geometry.}

**After**

These problems compare Cartesian, parametric, polar, and complex descriptions of plane curves. Choose coordinates appropriate to the geometry, calculate slopes, lengths, and areas, and check the direction and multiplicity of tracing.

## 105. Sequences and Infinite Series

Source: [source\chapters\ch15-sequences-and-infinite-series\ch15-sequences-and-infinite-series.ptx](../../source\chapters\ch15-sequences-and-infinite-series\ch15-sequences-and-infinite-series.ptx)

Flag: Replace dramatic framing and repeated narrative with a direct description of the concepts and required checks.

**Before**

> The last chapter ended with a formula we have not yet earned: e^{i\theta}=\cos\theta+i\sin\theta. It says that an exponential can move around a circle. That is not something ordinary algebra explains. The explanation will come from writing functions as infinite polynomials: 1+x+\frac{x^2}{2!}+\frac{x^3}{3!}+\cdots. So calculus now turns to a new kind of infinite process. We have already met infinity in two forms. A derivative was a limit of secant slopes. An integral was a limit of finite sums. Now infinity enters more directly: \text{an infinite list} \qquad\text{and}\qquad \text{an infinite sum}. An infinite list is called a sequence. An infinite sum is called a series. \text{sequence:} \quad \amp a_1,\ a_2,\ a_3,\ldots, \text{series:} \quad \amp a_1+a_2+a_3+\cdots. A sequence asks where the terms go. A series asks what happens when we keep adding the terms.

**After**

A sequence is an indexed list of numbers, and a series is defined by the limit of its finite partial sums. This chapter develops convergence criteria, tests for positive and signed series, and the distinction between absolute and conditional convergence. These results will justify the function series and approximations in the next chapter.

## 106. Sequences

Source: [source\chapters\ch15-sequences-and-infinite-series\sections\sec-15-1-sequences.xml](../../source\chapters\ch15-sequences-and-infinite-series\sections\sec-15-1-sequences.xml)

Flag: Replace dramatic framing and repeated narrative with a direct description of the concepts and required checks.

**Before**

> A sequence is a function whose inputs are whole numbers. That sounds dry, but the idea is familiar. A table of decimal approximations is a sequence. The outputs of Newton’s method form a sequence. The yearly values in a population model form a sequence. The finite approximations to an integral form a sequence. The input is not a continuous variable like x or t. It is a counting index: n=1,2,3,\ldots. The central question is: \text{Do the terms settle toward a number?}

**After**

A sequence assigns a value to each integer index in its domain. Decimal approximations, Newton iterates, and successive integral approximations are examples. We will define convergence, prove criteria that establish a limit, and examine recursive sequences.

## 107. Infinite series

Source: [source\chapters\ch15-sequences-and-infinite-series\sections\sec-15-2-infinite-series.xml](../../source\chapters\ch15-sequences-and-infinite-series\sections\sec-15-2-infinite-series.xml)

Flag: Replace dramatic framing and repeated narrative with a direct description of the concepts and required checks.

**Before**

> A sequence is an infinite list. A series is an infinite sum. But an infinite sum cannot mean that we literally finish adding infinitely many numbers. There is no last step. The only honest definition is through limits. We add finitely many terms, watch the partial sums, and ask whether those partial sums approach a number. \text{An infinite series is a limit of finite sums.}

**After**

An infinite series is defined as the limit of its partial sums. We add the first n terms and ask whether those finite totals converge as n\to\infty. Geometric and telescoping series provide cases where the partial sums can be calculated explicitly.

## 108. The harmonic series and first warnings

Source: [source\chapters\ch15-sequences-and-infinite-series\sections\sec-15-3-the-harmonic-series-and-first-warnings.xml](../../source\chapters\ch15-sequences-and-infinite-series\sections\sec-15-3-the-harmonic-series-and-first-warnings.xml)

Flag: Replace dramatic framing and repeated narrative with a direct description of the concepts and required checks.

**Before**

> The last section gave two friendly kinds of series. A geometric series has partial sums with a formula. A telescoping series has partial sums with cancellation. Most series are less generous. We often cannot compute S_n=a_1+a_2+\cdots+a_n exactly. We need tests that tell whether the partial sums settle down. The first test is not a convergence test. It is a warning test. \text{If an infinite sum converges, the terms being added must become small.} That sounds obvious. The danger is the converse. Terms can become small and still add up to infinity.

**After**

Convergence of \sum a_n requires a_n\to0, but this condition is not sufficient. The harmonic series demonstrates the distinction: its terms tend to zero while its partial sums grow without bound. We will prove that divergence and use it as a comparison.

## 109. Alternating series

Source: [source\chapters\ch15-sequences-and-infinite-series\sections\sec-15-5-alternating-series.xml](../../source\chapters\ch15-sequences-and-infinite-series\sections\sec-15-5-alternating-series.xml)

Flag: Replace dramatic framing and repeated narrative with a direct description of the concepts and required checks.

**Before**

> Positive series have no cancellation. Every term pushes the partial sums upward. That is why comparison and the integral test work so cleanly. But many important series change sign: 1-\frac12+\frac13-\frac14+\frac15-\cdots. The positive version, 1+\frac12+\frac13+\frac14+\cdots, diverges. The alternating version behaves differently because each term partially corrects the last one. This is the next idea: \text{organized cancellation can make an infinite sum converge.}

**After**

Alternating signs can make a series converge even when the corresponding series of absolute values diverges. The alternating harmonic series is an example. The alternating-series test gives a convergence criterion and a remainder bound when term magnitudes decrease to zero.

## 110. Absolute convergence and stronger tests

Source: [source\chapters\ch15-sequences-and-infinite-series\sections\sec-15-6-absolute-convergence-and-stronger-tests.xml](../../source\chapters\ch15-sequences-and-infinite-series\sections\sec-15-6-absolute-convergence-and-stronger-tests.xml)

Flag: Replace dramatic framing and repeated narrative with a direct description of the concepts and required checks.

**Before**

> Alternating series taught us that cancellation can make a divergent positive series turn into a convergent signed series. But cancellation is fragile. It depends on order and balance. A stronger kind of convergence ignores cancellation entirely. It asks whether the total size of all terms is finite: \sum |a_k|<\infty. If that positive series converges, then the original signed series converges no matter how the signs behave.

**After**

A series converges absolutely when the sum of its term magnitudes is finite. Absolute convergence implies convergence, regardless of the signs. This section develops the ratio and root tests for absolute convergence and Dirichlet's and Abel's tests for controlled cancellation.

## 111. Rearrangement and the danger of infinity

Source: [source\chapters\ch15-sequences-and-infinite-series\sections\sec-15-7-rearrangement-and-the-danger-of-infinity.xml](../../source\chapters\ch15-sequences-and-infinite-series\sections\sec-15-7-rearrangement-and-the-danger-of-infinity.xml)

Flag: Replace dramatic framing and repeated narrative with a direct description of the concepts and required checks.

**Before**

> Absolute convergence gave us a safer kind of infinite sum. If \sum_{k=1}^{\infty}|a_k| converges, then the original series \sum_{k=1}^{\infty}a_k converges without needing cancellation. Conditional convergence is different. It survives because positive and negative terms balance each other. That balance is real, but it is fragile. The next question is simple to ask: \text{Can we rearrange the terms of an infinite sum?} For finite sums, the answer is yes. For infinite sums, the answer depends on what kind of convergence we have.

**After**

Rearranging finitely many terms preserves their sum. For an infinite series, this remains true under absolute convergence. A conditionally convergent series can change its sum or diverge after rearrangement. We will explain the difference through its positive and negative terms.

## 112. Warning examples

Source: [source\chapters\ch15-sequences-and-infinite-series\sections\sec-15-8-warning-examples.xml](../../source\chapters\ch15-sequences-and-infinite-series\sections\sec-15-8-warning-examples.xml)

Flag: Replace dramatic framing and repeated narrative with a direct description of the concepts and required checks.

**Before**

> Series tests are not recipes to apply by reflex. Each test has hypotheses, and those hypotheses are part of the mathematics. This section collects the main warnings before we leave numerical series. \text{A series test used without its hypotheses is not a test.}

**After**

A series test applies only under its stated hypotheses. These examples distinguish a term tending to zero from a convergent sum, examine limits where the ratio and root tests are inconclusive, and show why endpoint and sign conditions must be checked.

## 113. Chapter review and discovery problems

Source: [source\chapters\ch15-sequences-and-infinite-series\sections\sec-15-9-chapter-review-and-discovery-problems.xml](../../source\chapters\ch15-sequences-and-infinite-series\sections\sec-15-9-chapter-review-and-discovery-problems.xml)

Flag: Replace dramatic framing and repeated narrative with a direct description of the concepts and required checks.

**Before**

> This chapter began with a list: a_1,\ a_2,\ a_3,\ldots. Then we added the list: a_1+a_2+a_3+\cdots. That small change created a large question. A sequence asks whether the terms settle down. A series asks whether the accumulated partial sums settle down. \sum_{k=1}^{\infty}a_k = \lim_{n\to\infty} \sum_{k=1}^{n}a_k. Everything in this chapter is a way to understand that limit.

**After**

These problems distinguish sequence limits from series sums and apply the Cauchy criterion, comparison tests, alternating-series bounds, absolute-convergence tests, and the Dirichlet and Abel tests. Explain why the selected test applies before drawing a convergence conclusion.

## 114. Power Series, Taylor Polynomials, and Taylor Series

Source: [source\chapters\ch16-power-series-taylor-polynomials-and-taylor-series\ch16-power-series-taylor-polynomials-and-taylor-series.ptx](../../source\chapters\ch16-power-series-taylor-polynomials-and-taylor-series\ch16-power-series-taylor-polynomials-and-taylor-series.ptx)

Flag: Replace dramatic framing and repeated narrative with a direct description of the concepts and required checks.

**Before**

> The last chapter ended with a change in viewpoint. A numerical series is an infinite sum of numbers: \sum_{n=1}^{\infty} a_n. Now the terms will depend on x: a_0+a_1x+a_2x^2+a_3x^3+\cdots. Then the infinite sum is no longer only a number. It can become a function. This is a large step. Polynomials are the friendliest functions in calculus. We can add them, multiply them, differentiate them, and integrate them term by term. A power series asks whether we can keep those polynomial habits when the polynomial has infinitely many terms. \text{A power series is an infinite polynomial, but only where it converges.} That last phrase is the warning. A power series may behave beautifully near its center and fail completely farther away.

**After**

A power series is a series whose terms are powers of the input multiplied by fixed coefficients. We will determine where it converges and justify operations on it inside that interval. Taylor polynomials match derivatives at a chosen point; remainder estimates determine whether they approximate the function and whether its Taylor series represents it.

## 115. Power series

Source: [source\chapters\ch16-power-series-taylor-polynomials-and-taylor-series\sections\sec-16-1-power-series.xml](../../source\chapters\ch16-power-series-taylor-polynomials-and-taylor-series\sections\sec-16-1-power-series.xml)

Flag: Replace dramatic framing and repeated narrative with a direct description of the concepts and required checks.

**Before**

> The simplest infinite polynomial is 1+x+x^2+x^3+\cdots. For a fixed value of x, this becomes a numerical series. The same formula can converge for some inputs and diverge for others. That is the first new question: \text{For which \(x\)-values does the infinite polynomial make sense?}

**After**

For each fixed x, a power series is a numerical series. Its convergence can change with x; for example, \sum_{n=0}^\infty x^n converges exactly when |x|<1. This section determines the radius and interval of convergence and tests the endpoints separately.

## 116. Working with power series

Source: [source\chapters\ch16-power-series-taylor-polynomials-and-taylor-series\sections\sec-16-2-working-with-power-series.xml](../../source\chapters\ch16-power-series-taylor-polynomials-and-taylor-series\sections\sec-16-2-working-with-power-series.xml)

Flag: Replace dramatic framing and repeated narrative with a direct description of the concepts and required checks.

**Before**

> A power series first asks where it converges. Once we are safely inside that interval, a second question begins: \text{Can we calculate with it as if it were a polynomial?} The answer is mostly yes, but the words “safely inside” matter. Inside the radius of convergence, power series are unusually well behaved. At endpoints, every operation must be checked again.

**After**

Inside their radii of convergence, power series can be added, multiplied, differentiated, and integrated under the conditions given below. Work on a common interval where the required series converge. At the endpoints, test convergence and justify the operation separately.

## 117. Representing functions by power series

Source: [source\chapters\ch16-power-series-taylor-polynomials-and-taylor-series\sections\sec-16-3-representing-functions-by-power-series.xml](../../source\chapters\ch16-power-series-taylor-polynomials-and-taylor-series\sections\sec-16-3-representing-functions-by-power-series.xml)

Flag: Replace dramatic framing and repeated narrative with a direct description of the concepts and required checks.

**Before**

> The last section gave us permission to work with power series inside their radius of convergence. We can add, multiply, differentiate, and integrate them term by term. Now we use that permission in the opposite direction. Instead of starting with a power series and asking where it converges, we start with a function and ask: \text{Can this function be written as an infinite polynomial?} The first seed is the geometric series. From that one seed, differentiation, integration, and substitution will grow new series.

**After**

Known series can produce representations of new functions by substitution, differentiation, and integration. We will start with the geometric series and state the interval on which each resulting identity holds.

## 118. Taylor polynomials

Source: [source\chapters\ch16-power-series-taylor-polynomials-and-taylor-series\sections\sec-16-4-taylor-polynomials.xml](../../source\chapters\ch16-power-series-taylor-polynomials-and-taylor-series\sections\sec-16-4-taylor-polynomials.xml)

Flag: Replace dramatic framing and repeated narrative with a direct description of the concepts and required checks.

**Before**

> Power series gave us infinite polynomials. But before an infinite polynomial can be trusted, we should understand the finite ones that approximate a function near one point. The derivative already gave us the first approximation: f(x)\approx f(a)+f'(a)(x-a). That is the tangent line. It matches the value and slope of f at a. Taylor’s idea is to continue the matching. \text{match value, slope, curvature, and higher derivatives.} The result is a polynomial built from local information.

**After**

The Taylor polynomial at a matches a function's value and derivatives through a chosen order. Its first-degree case is the tangent-line approximation f(a)+f\prime(a)(x-a). Higher degrees incorporate higher derivatives. The next section will bound the remainder.

## 119. Taylor’s theorem and remainders

Source: [source\chapters\ch16-power-series-taylor-polynomials-and-taylor-series\sections\sec-16-5-taylor-s-theorem-and-remainders.xml](../../source\chapters\ch16-power-series-taylor-polynomials-and-taylor-series\sections\sec-16-5-taylor-s-theorem-and-remainders.xml)

Flag: Replace dramatic framing and repeated narrative with a direct description of the concepts and required checks.

**Before**

> Taylor polynomials gave us a finite approximation: f(x)\approx T_n(x). But approximation without an error term is only a hope. The next question is the one calculus must answer: \text{How far is \(f(x)\) from its Taylor polynomial?} The difference f(x)-T_n(x) is called the remainder. It is the part of the function that the polynomial has not yet captured.

**After**

The remainder R_n(x)=f(x)-T_n(x) is the error in the Taylor polynomial. Taylor's theorem expresses or bounds that error under differentiability assumptions. Those bounds determine where the approximation is accurate and whether the remainder tends to zero as the degree increases.

## 120. Applications of Taylor series

Source: [source\chapters\ch16-power-series-taylor-polynomials-and-taylor-series\sections\sec-16-7-applications-of-taylor-series.xml](../../source\chapters\ch16-power-series-taylor-polynomials-and-taylor-series\sections\sec-16-7-applications-of-taylor-series.xml)

Flag: Replace dramatic framing and repeated narrative with a direct description of the concepts and required checks.

**Before**

> The last section collected Taylor series for the elementary functions: e^x,\qquad \sin x,\qquad \cos x,\qquad \ln(1+x),\qquad \arctan x, \qquad (1+x)^p. These formulas are not only identities. They are tools. A Taylor series can turn a difficult function into a polynomial calculation. That makes it useful for estimating function values, evaluating limits, approximating integrals, and solving differential equations. But the same warning remains: \text{A Taylor approximation is useful only when its error is controlled.} So every application in this section will keep the error visible.

**After**

Taylor expansions simplify estimates of function values, limits, integrals, and differential-equation solutions. For each application, choose an expansion valid on the relevant domain and bound the omitted terms.

## 121. Uniform convergence preview

Source: [source\chapters\ch16-power-series-taylor-polynomials-and-taylor-series\sections\sec-16-8-uniform-convergence-preview.xml](../../source\chapters\ch16-power-series-taylor-polynomials-and-taylor-series\sections\sec-16-8-uniform-convergence-preview.xml)

Flag: Replace dramatic framing and repeated narrative with a direct description of the concepts and required checks.

**Before**

> Power series have been unusually obedient. Inside their radius of convergence, we have added them, multiplied them, differentiated them, integrated them, and used them to represent functions. This is not how arbitrary infinite sums of functions behave. The missing idea is not another formula. It is a stronger kind of convergence. Ordinary convergence can happen separately at each point. Uniform convergence means the approximation is good on a whole interval at once. \text{Uniform convergence is convergence with one error bound for all points in a set.} This section is a preview. A later analysis course will make these ideas fully systematic. Here we use them to explain why power series are trustworthy inside their radius.

**After**

Pointwise convergence allows the index needed for a given accuracy to depend on the input. Uniform convergence requires one index to work for every input in the set. This section defines that distinction, shows how uniform convergence preserves continuity and integrals, and applies it to power series on smaller closed intervals inside their radii.

## 122. Warning examples

Source: [source\chapters\ch16-power-series-taylor-polynomials-and-taylor-series\sections\sec-16-9-warning-examples.xml](../../source\chapters\ch16-power-series-taylor-polynomials-and-taylor-series\sections\sec-16-9-warning-examples.xml)

Flag: Replace dramatic framing and repeated narrative with a direct description of the concepts and required checks.

**Before**

> Uniform convergence explained why power series behave so well inside their radius. That explanation should not make us careless. Infinite processes are powerful because they are controlled. When the control is missing, familiar-looking operations can fail. This section collects the warnings that belong at the end of the story. \text{A Taylor series is not automatically the function that produced it.} \text{Endpoint behavior is not decided by the interior.} \text{Term-by-term operations need hypotheses.}

**After**

A Taylor series may fail to represent its defining function, and convergence inside an interval does not decide endpoint behavior. Also, term-by-term differentiation and integration require hypotheses on convergence. The examples below distinguish these failures.

## 123. Chapter review and projects

Source: [source\chapters\ch16-power-series-taylor-polynomials-and-taylor-series\sections\sec-16-10-chapter-review-and-projects.xml](../../source\chapters\ch16-power-series-taylor-polynomials-and-taylor-series\sections\sec-16-10-chapter-review-and-projects.xml)

Flag: Replace dramatic framing and repeated narrative with a direct description of the concepts and required checks.

**Before**

> Chapter 16 started with infinite polynomials and ended with a warning about their limits. The main thread was approximation with control. A power series is a function-building machine. A Taylor polynomial is a finite local approximation. A Taylor series is what happens when the degree grows without bound. Taylor’s theorem tells us when the finite approximations actually approach the function.

**After**

These problems determine convergence intervals, construct Taylor polynomials and series, bound remainders, and justify operations on function series. Distinguish a convergent formal series from a series that actually represents the given function.

## 124. Complex Numbers, Fourier Ideas, and the Road Ahead

Source: [source\chapters\ch17-complex-numbers-fourier-ideas-and-the-road-ahead\ch17-complex-numbers-fourier-ideas-and-the-road-ahead.ptx](../../source\chapters\ch17-complex-numbers-fourier-ideas-and-the-road-ahead\ch17-complex-numbers-fourier-ideas-and-the-road-ahead.ptx)

Flag: Replace dramatic framing and repeated narrative with a direct description of the concepts and required checks.

**Before**

> The last chapter ended with a strange-looking promise: e^{i\theta}=\cos\theta+i\sin\theta. The formula says that an exponential can trace a circle. At first that sounds impossible. Exponential growth moves away from 0. Sine and cosine move back and forth. A circle turns. Why should one formula connect all three? Taylor series gave the clue. The series for e^x, \cos x, and \sin x have the same factorials hiding inside them. The missing ingredient is a number whose square is -1. That number is called i. It opens a new plane of numbers, and in that plane the exponential becomes the natural language of rotation.

**After**

Complex exponentials express rotation through Euler's formula e^{i\theta}=\cos\theta+i\sin\theta. This chapter uses that relation to study oscillation and introduces Fourier series, boundary identities, conservation laws, and stationary-action calculations. The final optional section proves a local differential-equation existence and uniqueness theorem using the convergence results from earlier chapters.

## 125. Complex numbers and Euler’s formula

Source: [source\chapters\ch17-complex-numbers-fourier-ideas-and-the-road-ahead\sections\sec-17-1-complex-numbers-and-euler-s-formula.xml](../../source\chapters\ch17-complex-numbers-fourier-ideas-and-the-road-ahead\sections\sec-17-1-complex-numbers-and-euler-s-formula.xml)

Flag: Replace dramatic framing and repeated narrative with a direct description of the concepts and required checks.

**Before**

> The real number line is one-dimensional. It can measure position to the left and right, size, error, and signed change. But it cannot solve x^2+1=0. No real number has square -1. Instead of giving up, mathematics enlarges the number system.

**After**

Complex numbers extend the real numbers by a number i satisfying i^2=-1. We will use their algebra and polar form to define the complex exponential and prove Euler's formula.

## 126. Vibrations and second-order equations

Source: [source\chapters\ch17-complex-numbers-fourier-ideas-and-the-road-ahead\sections\sec-17-2-vibrations-and-second-order-equations.xml](../../source\chapters\ch17-complex-numbers-fourier-ideas-and-the-road-ahead\sections\sec-17-2-vibrations-and-second-order-equations.xml)

Flag: Replace dramatic framing and repeated narrative with a direct description of the concepts and required checks.

**Before**

> Chapter [cross-reference] already introduced second-order equations through vibrating systems. A spring gave us y''+\omega^2y=0. At that time, sine and cosine solved the equation because their second derivatives return negative copies of themselves. Complex numbers explain the deeper reason: \text{oscillation is the shadow of rotation.} A point rotating in the complex plane has a horizontal shadow \cos(\omega t) and a vertical shadow \sin(\omega t). Those shadows move back and forth. The spring motion is one such shadow.

**After**

The equation y^{\prime\prime}+\omega^2y=0 has sine and cosine solutions. Complex exponentials combine these oscillations in e^{i\omega t}, whose real and imaginary parts are \cos(\omega t) and \sin(\omega t). We will use this representation for constant-coefficient second-order equations.

## 127. Fourier series preview

Source: [source\chapters\ch17-complex-numbers-fourier-ideas-and-the-road-ahead\sections\sec-17-3-fourier-series-preview.xml](../../source\chapters\ch17-complex-numbers-fourier-ideas-and-the-road-ahead\sections\sec-17-3-fourier-series-preview.xml)

Flag: Replace dramatic framing and repeated narrative with a direct description of the concepts and required checks.

**Before**

> A single spring gives one clean frequency: \cos(\omega t) \qquad\text{or}\qquad \sin(\omega t). But real periodic motion is rarely one pure wave. A violin string, an electrical signal, a heartbeat, a tide table, and a repeating temperature pattern all contain mixtures. Taylor series built functions from powers: 1,\ x,\ x^2,\ x^3,\ldots. Fourier series build periodic functions from waves: 1,\ \cos t,\ \sin t,\ \cos(2t),\ \sin(2t),\ \cos(3t),\ \sin(3t),\ldots. This section is a preview. The full convergence theory belongs to a later course. But the main idea is already visible with the calculus we know: \text{Fourier series use integrals to measure how much of each wave is present.}

**After**

A Fourier series represents a periodic function using a constant and sine and cosine terms at integer multiples of a basic frequency. Integrals determine the coefficients by measuring these components. This section derives those formulas and works through examples; full convergence theory requires further results.

## 128. The one-dimensional Stokes theorem

Source: [source\chapters\ch17-complex-numbers-fourier-ideas-and-the-road-ahead\sections\sec-17-4-the-one-dimensional-stokes-theorem.xml](../../source\chapters\ch17-complex-numbers-fourier-ideas-and-the-road-ahead\sections\sec-17-4-the-one-dimensional-stokes-theorem.xml)

Flag: Replace dramatic framing and repeated narrative with a direct description of the concepts and required checks.

**Before**

> The Fundamental Theorem told us that \int_a^b F'(x)\,dx=F(b)-F(a). At first, this was an antiderivative rule. It let us evaluate integrals. But there is a deeper geometric reading: what accumulates inside an interval is measured by what happens on its boundary. In one dimension, the boundary of an interval consists of two endpoints. The right endpoint counts positively. The left endpoint counts negatively. That signed boundary is the seed of Stokes’ theorem.

**After**

The Fundamental Theorem writes an integral of a derivative as a signed endpoint sum:\int_a^b F\prime(x)\,dx=F(b)-F(a).This is the one-dimensional case of a boundary identity. We will define the oriented boundary of an interval and use differential notation to express the identity.

## 129. Conservation laws in one dimension

Source: [source\chapters\ch17-complex-numbers-fourier-ideas-and-the-road-ahead\sections\sec-17-5-conservation-laws-in-one-dimension.xml](../../source\chapters\ch17-complex-numbers-fourier-ideas-and-the-road-ahead\sections\sec-17-5-conservation-laws-in-one-dimension.xml)

Flag: Replace dramatic framing and repeated narrative with a direct description of the concepts and required checks.

**Before**

> The last section rewrote the Fundamental Theorem as a boundary theorem: \int_{[a,b]} dF=\int_{\partial[a,b]}F. The interval contributes its two endpoints. The inside contributes a derivative. The same boundary idea explains one of the most important patterns in science: what is inside changes because something crosses the boundary or is created inside. That sentence is a conservation law.

**After**

A conservation law balances the change of a quantity in a region against inflow, outflow, and production within it. In one dimension, the region is an interval and fluxes enter or leave through its endpoints. We will derive integral and differential forms of that balance.

## 130. Least action and the shape of a path

Source: [source\chapters\ch17-complex-numbers-fourier-ideas-and-the-road-ahead\sections\sec-17-6-least-action-and-the-shape-of-a-path.xml](../../source\chapters\ch17-complex-numbers-fourier-ideas-and-the-road-ahead\sections\sec-17-6-least-action-and-the-shape-of-a-path.xml)

Flag: Replace dramatic framing and repeated narrative with a direct description of the concepts and required checks.

**Before**

> Optimization began with numbers. We chose a radius, a price, a time, or a point and made a function as large or as small as possible. But a path is not one number. A path is a whole function. A bead sliding along a wire chooses a curve. Light traveling through different media chooses a path. A planet moving under gravity traces an orbit. The question is no longer \text{Which number is best?} but \text{Which function is best?} That question leads beyond ordinary single-variable calculus. Still, the first idea is visible with tools we already know: derivatives, integrals, and integration by parts.

**After**

Some optimization problems vary an entire path rather than a single number. A path determines an integral, called a functional, and small changes in the path change that integral. We will use differentiation and integration by parts to find a condition for a stationary value. Stationary does not necessarily mean minimal.

## 131. Final projects

Source: [source\chapters\ch17-complex-numbers-fourier-ideas-and-the-road-ahead\sections\sec-17-7-final-projects.xml](../../source\chapters\ch17-complex-numbers-fourier-ideas-and-the-road-ahead\sections\sec-17-7-final-projects.xml)

Flag: Replace dramatic framing and repeated narrative with a direct description of the concepts and required checks.

**Before**

> The book began with two instruments on a dashboard. One measured accumulated distance. The other measured instantaneous change. Since then, the same two ideas have appeared in many forms: \text{derivatives measure local change}, \qquad \text{integrals accumulate small pieces}. Taylor polynomials turned local derivative information into approximations. Differential equations turned laws of change into unknown functions. Parametric curves let motion draw geometry. Fourier ideas built periodic motion from waves. The one-dimensional Stokes theorem revealed the Fundamental Theorem as a boundary theorem. These final projects ask you to use the whole story. Calculus is one connected language: change, accumulation, approximation, models, and boundary terms. Calculus is one connected language: change, accumulation, approximation, models, and boundary terms. \begin{tikzpicture}[every node/.style={font=\small}, scale=1] \node[draw, rounded corners, align=center, minimum width=3.1cm, minimum height=1cm] (change) at (0,2.3) {instantaneous\\change}; \node[draw, rounded corners, align=center, minimum width=3.1cm, minimum height=1cm] (accum) at (6.6,2.3) {accumulated\\change}; \node[draw, rounded corners, align=center, minimum width=3.1cm, minimum height=1cm] (approx) at (0,-0.3) {approximation\\and error}; \node[draw, rounded corners, align=center, minimum width=3.1cm, minimum height=1cm] (models) at (6.6,-0.3) {models and\\differential equations}; \node[draw, rounded corners, align=center, minimum width=3.1cm, minimum height=1cm] (boundary) at (3.3,-2.5) {boundary\\ideas}; \draw[->, thick] (change) -- node[above] {integrate} (accum); \draw[->, thick] (accum) -- node[below] {differentiate} (change); \draw[->, thick] (change) -- (approx); \draw[->, thick] (approx) -- (models); \draw[->, thick] (models) -- (accum); \draw[->, thick] ([xshift=-10pt]accum.south west) -- ([xshift=8pt]boundary.north); \draw[->, thick] ([xshift=-8pt]boundary.north) -- ([xshift=10pt]change.south east); \node[align=center] at (3.3,3.25) {The final projects connect the main ideas of the book.}; \end{tikzpicture} Each project below can be done alone or with a small group. A good solution should include clear calculations, graphs when they help, and a short written explanation of what the calculations mean.

**After**

These projects combine derivatives, integrals, differential equations, approximations, and geometric descriptions. Each may be completed individually or in a small group. Present the assumptions, calculations, useful graphs, error estimates where appropriate, and an explanation of the results. Calculus is one connected language: change, accumulation, approximation, models, and boundary terms. Calculus is one connected language: change, accumulation, approximation, models, and boundary terms. \begin{tikzpicture}[every node/.style={font=\small}, scale=1] \node[draw, rounded corners, align=center, minimum width=3.1cm, minimum height=1cm] (change) at (0,2.3) {instantaneous\\change}; \node[draw, rounded corners, align=center, minimum width=3.1cm, minimum height=1cm] (accum) at (6.6,2.3) {accumulated\\change}; \node[draw, rounded corners, align=center, minimum width=3.1cm, minimum height=1cm] (approx) at (0,-0.3) {approximation\\and error}; \node[draw, rounded corners, align=center, minimum width=3.1cm, minimum height=1cm] (models) at (6.6,-0.3) {models and\\differential equations}; \node[draw, rounded corners, align=center, minimum width=3.1cm, minimum height=1cm] (boundary) at (3.3,-2.5) {boundary\\ideas}; \draw[->, thick] (change) -- node[above] {integrate} (accum); \draw[->, thick] (accum) -- node[below] {differentiate} (change); \draw[->, thick] (change) -- (approx); \draw[->, thick] (approx) -- (models); \draw[->, thick] (models) -- (accum); \draw[->, thick] ([xshift=-10pt]accum.south west) -- ([xshift=8pt]boundary.north); \draw[->, thick] ([xshift=-8pt]boundary.north) -- ([xshift=10pt]change.south east); \node[align=center] at (3.3,3.25) {The final projects connect the main ideas of the book.}; \end{tikzpicture}

## 132. Taylor series for elementary functions

Source: [source\chapters\ch16-power-series-taylor-polynomials-and-taylor-series\sections\sec-16-6-taylor-series-for-elementary-functions.xml](../../source\chapters\ch16-power-series-taylor-polynomials-and-taylor-series\sections\sec-16-6-taylor-series-for-elementary-functions.xml)

Flag: Replace a hidden-warning metaphor with the convergence requirement.

**Before**

> There is a warning hidden in the definition.

**After**

The definition alone does not assert convergence or equality with the function.

## 133. Proofs and Completeness

Source: [source\appendices\appD-proofs-and-completeness\appD-proofs-and-completeness.ptx](../../source\appendices\appD-proofs-and-completeness\appD-proofs-and-completeness.ptx)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> Most of calculus can be learned first through motion, graphs, rates, and accumulated area. But underneath those pictures is a quiet promise:

**After**

Existence theorems justify limits, extrema, roots, and integrals under stated conditions. Their proofs depend on completeness of the real numbers.

## 134. Proofs and Completeness

Source: [source\appendices\appD-proofs-and-completeness\appD-proofs-and-completeness.ptx](../../source\appendices\appD-proofs-and-completeness\appD-proofs-and-completeness.ptx)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> This appendix collects the proof ideas that support that promise. It is not meant to replace the main story of the book. It is a proof workshop: a place to see why the closed interval [a,b], continuity, and the real numbers are so powerful.

**After**

This appendix develops the proof arguments behind those results, including the roles of continuity, completeness, and closed intervals.

## 135. Uniform Continuity on Closed Intervals

Source: [source\appendices\appD-proofs-and-completeness\sections\sec-d-5-uniform-continuity-on-closed-intervals.xml](../../source\appendices\appD-proofs-and-completeness\sections\sec-d-5-uniform-continuity-on-closed-intervals.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> Uniform continuity is the reason that, on a closed interval, making subintervals short enough controls the function’s oscillation everywhere. That is one of the quiet foundations behind Riemann sums and numerical integration.

**After**

Uniform continuity gives one interval-width bound that controls the oscillation throughout a closed interval. This is used to prove convergence of Riemann sums.

## 136. The dashboard: speedometer and odometer

Source: [source\chapters\ch01-velocity-distance-and-the-first-shape-of-calculus\sections\sec-1-1-the-dashboard-speedometer-and-odometer.xml](../../source\chapters\ch01-velocity-distance-and-the-first-shape-of-calculus\sections\sec-1-1-the-dashboard-speedometer-and-odometer.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> On a short piece where velocity hardly changes, the constant-velocity rule is a good local story. Accumulation is the act of adding those local stories.

**After**

When velocity changes little over a short interval, constant velocity gives a useful approximation to that interval's displacement. Adding these approximations estimates the total displacement.

## 137. The dashboard: speedometer and odometer

Source: [source\chapters\ch01-velocity-distance-and-the-first-shape-of-calculus\sections\sec-1-1-the-dashboard-speedometer-and-odometer.xml](../../source\chapters\ch01-velocity-distance-and-the-first-shape-of-calculus\sections\sec-1-1-the-dashboard-speedometer-and-odometer.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> One question goes from distance to velocity; the other goes from velocity to distance. In your own words, why should these two processes undo each other, and what would go wrong in the story if they did not?

**After**

For motion along a line, differentiating position gives velocity, and accumulating velocity over an interval gives the change in position. Explain why these operations are related and what additional starting information is needed to recover position.

## 138. The dashboard: speedometer and odometer

Source: [source\chapters\ch01-velocity-distance-and-the-first-shape-of-calculus\sections\sec-1-1-the-dashboard-speedometer-and-odometer.xml](../../source\chapters\ch01-velocity-distance-and-the-first-shape-of-calculus\sections\sec-1-1-the-dashboard-speedometer-and-odometer.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> For now, we test the story in the simplest case: constant velocity.

**After**

We first compute both quantities for constant velocity.

## 139. Constant velocity: where slope and area first meet

Source: [source\chapters\ch01-velocity-distance-and-the-first-shape-of-calculus\sections\sec-1-2-constant-velocity-where-slope-and-area-first-meet.xml](../../source\chapters\ch01-velocity-distance-and-the-first-shape-of-calculus\sections\sec-1-2-constant-velocity-where-slope-and-area-first-meet.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> For constant velocity, nothing mysterious is hidden.

**After**

For constant velocity, the slope calculation and the rectangular area calculation are exact.

## 140. Constant velocity: where slope and area first meet

Source: [source\chapters\ch01-velocity-distance-and-the-first-shape-of-calculus\sections\sec-1-2-constant-velocity-where-slope-and-area-first-meet.xml](../../source\chapters\ch01-velocity-distance-and-the-first-shape-of-calculus\sections\sec-1-2-constant-velocity-where-slope-and-area-first-meet.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> requires constant velocity. Without that assumption, it can give the wrong story.

**After**

This formula requires constant velocity. For changing velocity, a single velocity value does not generally determine the total displacement.

## 141. Constant velocity: where slope and area first meet

Source: [source\chapters\ch01-velocity-distance-and-the-first-shape-of-calculus\sections\sec-1-2-constant-velocity-where-slope-and-area-first-meet.xml](../../source\chapters\ch01-velocity-distance-and-the-first-shape-of-calculus\sections\sec-1-2-constant-velocity-where-slope-and-area-first-meet.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> The exact slope-and-area story in this section used a velocity that never changed. In your own words, what would break if the velocity started changing while the clock was running, and what new idea will be needed?

**After**

The slope and rectangle-area calculations here used constant velocity. Explain which calculation changes when velocity varies and why approximating over shorter intervals is useful.

## 142. Forward, backward, and signed motion

Source: [source\chapters\ch01-velocity-distance-and-the-first-shape-of-calculus\sections\sec-1-3-forward-backward-and-signed-motion.xml](../../source\chapters\ch01-velocity-distance-and-the-first-shape-of-calculus\sections\sec-1-3-forward-backward-and-signed-motion.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> The odometer would tell a different story. The car actually drove 80 miles forward and then 30 miles backward. The total distance traveled is

**After**

The car travels 80 miles forward and then 30 miles backward. Its odometer records total distance traveled:

## 143. Forward, backward, and signed motion

Source: [source\chapters\ch01-velocity-distance-and-the-first-shape-of-calculus\sections\sec-1-3-forward-backward-and-signed-motion.xml](../../source\chapters\ch01-velocity-distance-and-the-first-shape-of-calculus\sections\sec-1-3-forward-backward-and-signed-motion.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> For piecewise-constant velocity, we can compute everything with rectangles. But the next idea is even simpler and deeper: if we know a list of signed positions at equally spaced times, then the changes between them contain all the information needed to recover the final position from the first one.

**After**

For piecewise-constant velocity, rectangles give exact displacement. If instead we have signed positions at equally spaced times, adding consecutive position changes recovers the final position from the initial one.

## 144. Calculus without limits: finite differences and finite sums

Source: [source\chapters\ch01-velocity-distance-and-the-first-shape-of-calculus\sections\sec-1-4-calculus-without-limits-finite-differences-and-finite-sums.xml](../../source\chapters\ch01-velocity-distance-and-the-first-shape-of-calculus\sections\sec-1-4-calculus-without-limits-finite-differences-and-finite-sums.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> Write the sum as (s_1-s_0)+(s_2-s_1)+\cdots+(s_n-s_{n-1}) and watch what survives. The odometer already knew the same story: only the start and the end remain.

**After**

Expand the sum as (s_1-s_0)+(s_2-s_1)+\cdots+(s_n-s_{n-1}). Each interior position appears once positively and once negatively, leaving s_n-s_0.

## 145. Calculus without limits: finite differences and finite sums

Source: [source\chapters\ch01-velocity-distance-and-the-first-shape-of-calculus\sections\sec-1-4-calculus-without-limits-finite-differences-and-finite-sums.xml](../../source\chapters\ch01-velocity-distance-and-the-first-shape-of-calculus\sections\sec-1-4-calculus-without-limits-finite-differences-and-finite-sums.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> Finite differences go from position to change; finite sums go from change back to position. In your own words, why is that already the two-direction story of calculus, and what can this discrete version not yet handle?

**After**

Finite differences compute position changes, and summing consecutive differences recovers the total change. Explain this cancellation and why instantaneous velocity still requires a limiting process.

## 146. Changing velocity and the need for limits

Source: [source\chapters\ch01-velocity-distance-and-the-first-shape-of-calculus\sections\sec-1-5-changing-velocity-and-the-need-for-limits.xml](../../source\chapters\ch01-velocity-distance-and-the-first-shape-of-calculus\sections\sec-1-5-changing-velocity-and-the-need-for-limits.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> Now reverse the story. Suppose we know velocity and want displacement.

**After**

Now suppose velocity is known and displacement is required.

## 147. A first map of the book

Source: [source\chapters\ch01-velocity-distance-and-the-first-shape-of-calculus\sections\sec-1-6-a-first-map-of-the-book.xml](../../source\chapters\ch01-velocity-distance-and-the-first-shape-of-calculus\sections\sec-1-6-a-first-map-of-the-book.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> This section organizes the book into four roles: derivative, integral, approximation, and differential equations. In your own words, what job does each role do in the dashboard story, and why would leaving any one of them out make the map incomplete?

**After**

Explain the roles of derivatives, integrals, approximations, and differential equations in describing motion. Give one question answered by each.

## 148. A first map of the book

Source: [source\chapters\ch01-velocity-distance-and-the-first-shape-of-calculus\sections\sec-1-6-a-first-map-of-the-book.xml](../../source\chapters\ch01-velocity-distance-and-the-first-shape-of-calculus\sections\sec-1-6-a-first-map-of-the-book.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> Both depend on the same hidden idea: nearness. To make calculus honest, we need a precise language for numbers, intervals, functions, graphs, and limits. That language comes next.

**After**

Both processes require a precise meaning of approximation error and nearness. The next chapters define distances, intervals, functions, and limits.

## 149. A first map of the book

Source: [source\chapters\ch01-velocity-distance-and-the-first-shape-of-calculus\sections\sec-1-6-a-first-map-of-the-book.xml](../../source\chapters\ch01-velocity-distance-and-the-first-shape-of-calculus\sections\sec-1-6-a-first-map-of-the-book.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> Both h\to0 and better and better approximating sums depend on nearness. In your own words, what does near have to mean before those two phrases can be honest mathematics rather than slogans?

**After**

What must be specified to make h\to0 and convergence of approximating sums precise? Explain the input or index, the quantity being approximated, and the allowed error.

## 150. Discovery problems and projects

Source: [source\chapters\ch01-velocity-distance-and-the-first-shape-of-calculus\sections\sec-1-7-discovery-problems-and-projects.xml](../../source\chapters\ch01-velocity-distance-and-the-first-shape-of-calculus\sections\sec-1-7-discovery-problems-and-projects.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> Which graph gives a better story of what the driver actually did: the velocity graph or the final displacement alone?

**After**

Which gives more information about how the car moved: the velocity graph or the final displacement alone? Explain what the displacement omits.

## 151. Discovery problems and projects

Source: [source\chapters\ch01-velocity-distance-and-the-first-shape-of-calculus\sections\sec-1-7-discovery-problems-and-projects.xml](../../source\chapters\ch01-velocity-distance-and-the-first-shape-of-calculus\sections\sec-1-7-discovery-problems-and-projects.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> The last question matters. Calculus often compresses a whole history into one number. That number is useful, but it is not the whole story.

**After**

A total displacement does not determine the velocity history. Many different trips have the same signed displacement.

## 152. Discovery problems and projects

Source: [source\chapters\ch01-velocity-distance-and-the-first-shape-of-calculus\sections\sec-1-7-discovery-problems-and-projects.xml](../../source\chapters\ch01-velocity-distance-and-the-first-shape-of-calculus\sections\sec-1-7-discovery-problems-and-projects.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> This is the first glimpse of the precise language of limits. A limit is not a guess from a table. It is a promise:

**After**

The precise definition of a limit will require an input bound that meets every requested positive output tolerance:

## 153. Discovery problems and projects

Source: [source\chapters\ch01-velocity-distance-and-the-first-shape-of-calculus\sections\sec-1-7-discovery-problems-and-projects.xml](../../source\chapters\ch01-velocity-distance-and-the-first-shape-of-calculus\sections\sec-1-7-discovery-problems-and-projects.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> For this example, the promise is easy because the error is exactly |h|. In more difficult examples, the whole task is to control the error.

**After**

Here the error is exactly |h|, so the input and output tolerances can be the same. Other limits require a different relation between the two tolerances.

## 154. Discovery problems and projects

Source: [source\chapters\ch01-velocity-distance-and-the-first-shape-of-calculus\sections\sec-1-7-discovery-problems-and-projects.xml](../../source\chapters\ch01-velocity-distance-and-the-first-shape-of-calculus\sections\sec-1-7-discovery-problems-and-projects.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> In the average-velocity example, the error was exactly |h|, so requiring |h|<0.01 made the average within 0.01 of 4. In your own words, what promise is a limit making, and why is that promise stronger than reading a number from a table?

**After**

In this average-velocity example, the error from 4 is |h|. Explain how to meet any positive output tolerance and why checking a finite table does not prove this for every tolerance.

## 155. The real line and intervals

Source: [source\chapters\ch02-numbers-functions-and-models\sections\sec-2-1-the-real-line-and-intervals.xml](../../source\chapters\ch02-numbers-functions-and-models\sections\sec-2-1-the-real-line-and-intervals.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> The real line now gives us a way to talk about closeness. But there is a deeper question hiding under the picture. Is the line really unbroken? Are there numbers for all the points that geometry asks for?

**After**

Rational numbers measure many distances, but they do not represent every point required by geometry and limiting processes. The next section explains why the real numbers are needed.

## 156. Completeness and the idea of no gaps

Source: [source\chapters\ch02-numbers-functions-and-models\sections\sec-2-2-completeness-and-the-idea-of-no-gaps.xml](../../source\chapters\ch02-numbers-functions-and-models\sections\sec-2-2-completeness-and-the-idea-of-no-gaps.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> The decimal approximations to \sqrt2 produce nested closed intervals whose lengths shrink toward 0. In your own words, what does the Nested Interval Principle promise on the real line, and why does the same picture fail if we allow only rational numbers?

**After**

The decimal approximations to \sqrt2 give nested closed intervals whose lengths tend to zero. State what the Nested Interval Principle guarantees and explain why their common point is unavailable if only rational numbers are allowed.

## 157. Completeness and the idea of no gaps

Source: [source\chapters\ch02-numbers-functions-and-models\sections\sec-2-2-completeness-and-the-idea-of-no-gaps.xml](../../source\chapters\ch02-numbers-functions-and-models\sections\sec-2-2-completeness-and-the-idea-of-no-gaps.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> A tangent slope, an area, a bisection root, and an infinite decimal are all approached by approximations. In your own words, what promise is a limiting process making, and why is completeness the property that lets that destination be an actual real number?

**After**

Tangent slopes, areas, bisection roots, and infinite decimals are defined through approximations. Explain how completeness supplies real limiting values when the appropriate convergence conditions hold.

## 158. Graphs and transformations

Source: [source\chapters\ch02-numbers-functions-and-models\sections\sec-2-4-graphs-and-transformations.xml](../../source\chapters\ch02-numbers-functions-and-models\sections\sec-2-4-graphs-and-transformations.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> Graphs are honest when drawn carefully, but they are not proofs by themselves.

**After**

A graph can suggest a property of a function, but the plotted image alone does not prove it.

## 159. Graphs and transformations

Source: [source\chapters\ch02-numbers-functions-and-models\sections\sec-2-4-graphs-and-transformations.xml](../../source\chapters\ch02-numbers-functions-and-models\sections\sec-2-4-graphs-and-transformations.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> Graphs guide the eye. They are honest only at the scale and window you chose. A proof has to survive every allowed input, not only the ones that happened to be drawn.

**After**

A plotted graph depends on its window and sampling resolution. To establish a property for all inputs in a domain, use an argument that covers those inputs.

## 160. Models before calculus

Source: [source\chapters\ch02-numbers-functions-and-models\sections\sec-2-7-models-before-calculus.xml](../../source\chapters\ch02-numbers-functions-and-models\sections\sec-2-7-models-before-calculus.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> A model is a mathematical story about reality, not reality itself. In your own words, what four questions should we ask of a model, and why can a formula be algebraically correct yet still be physically wrong outside the range of its assumptions?

**After**

A model represents a situation under stated assumptions. What four checks should be made, and why can an algebraically correct formula give an incorrect physical prediction outside its assumed range?

## 161. Models before calculus

Source: [source\chapters\ch02-numbers-functions-and-models\sections\sec-2-7-models-before-calculus.xml](../../source\chapters\ch02-numbers-functions-and-models\sections\sec-2-7-models-before-calculus.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> Ask about assumptions, units, fit, and the region where the story should not be trusted. Algebra checks internal consistency; modeling also checks whether the situation still matches the story.

**After**

Check assumptions, units, agreement with data, and the applicable range. Algebraic consistency alone does not establish agreement with the modeled situation.

## 162. Models before calculus

Source: [source\chapters\ch02-numbers-functions-and-models\sections\sec-2-7-models-before-calculus.xml](../../source\chapters\ch02-numbers-functions-and-models\sections\sec-2-7-models-before-calculus.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> Doubling the side of a square quadruples the area. In your own words, what scaling rule does a model y=Cx^p encode, and why is that a different story from constant additive change?

**After**

Doubling the side of a square quadruples its area. Explain the scaling relation in y=Cx^p and how it differs from constant additive change.

## 163. Models before calculus

Source: [source\chapters\ch02-numbers-functions-and-models\sections\sec-2-7-models-before-calculus.xml](../../source\chapters\ch02-numbers-functions-and-models\sections\sec-2-7-models-before-calculus.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> Constant differences suggest addition. Constant ratios suggest multiplication. A closed dish, a finite population, or a changing interest rate can break a multiplicative story even if the first few steps look exponential.

**After**

Constant differences suggest an additive model, whereas constant ratios suggest a multiplicative model. Resource limits or changing rates may invalidate an exponential model beyond the observed data.

## 164. Technology and graphs

Source: [source\chapters\ch02-numbers-functions-and-models\sections\sec-2-8-technology-and-graphs.xml](../../source\chapters\ch02-numbers-functions-and-models\sections\sec-2-8-technology-and-graphs.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> When h is very small, the numerator often subtracts nearly equal numbers. That makes roundoff error part of the story.

**After**

When h is small, the numerator subtracts nearly equal numbers. Rounding can then affect the computed quotient substantially.

## 165. Chapter review and discovery problems

Source: [source\chapters\ch02-numbers-functions-and-models\sections\sec-2-9-chapter-review-and-discovery-problems.xml](../../source\chapters\ch02-numbers-functions-and-models\sections\sec-2-9-chapter-review-and-discovery-problems.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> Same formula, different story. Consider the formula

**After**

The same formula can describe different quantities. Consider

## 166. Chapter review and discovery problems

Source: [source\chapters\ch02-numbers-functions-and-models\sections\sec-2-9-chapter-review-and-discovery-problems.xml](../../source\chapters\ch02-numbers-functions-and-models\sections\sec-2-9-chapter-review-and-discovery-problems.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> For s(t)=t^2, the average velocity from t=2 to t=2+h is 4+h with h\neq0, and the error from 4 is exactly |h|. In your own words, what promise is already visible here, and why is the input allowed to approach a forbidden value while the output is forced into any desired error bound?

**After**

For s(t)=t^2, the average velocity from 2 to 2+h is 4+h for h\ne0. Explain how its error from 4 can be made smaller than any positive tolerance without evaluating the quotient at h=0.

## 167. Limits from motion and approximation

Source: [source\chapters\ch03-limits-and-continuity\sections\sec-3-1-limits-from-motion-and-approximation.xml](../../source\chapters\ch03-limits-and-continuity\sections\sec-3-1-limits-from-motion-and-approximation.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> A limit watches nearby outputs. The actual assigned height at the point is a separate piece of data. Continuity is the calm case where those two numbers match.

**After**

A limit concerns nearby values; the value assigned at the point is separate. Continuity requires those values to agree.

## 168. Limits from motion and approximation

Source: [source\chapters\ch03-limits-and-continuity\sections\sec-3-1-limits-from-motion-and-approximation.xml](../../source\chapters\ch03-limits-and-continuity\sections\sec-3-1-limits-from-motion-and-approximation.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> The first situation is the calm one. The second and third are warning signs. They show why limits must come before continuity.

**After**

The first situation is continuous at the point. The other two distinguish an existing nearby limit from the assigned function value.

## 169. Calculating limits

Source: [source\chapters\ch03-limits-and-continuity\sections\sec-3-2-calculating-limits.xml](../../source\chapters\ch03-limits-and-continuity\sections\sec-3-2-calculating-limits.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> The error of a sum is no worse than the sum of the errors. Cancellation can hide wild pieces inside a calm total, so existence of the combination does not imply existence of the parts.

**After**

The error in a sum is bounded by the sum of the individual errors. Conversely, cancellation may make a sum converge even when its components have no limits.

## 170. Calculating limits

Source: [source\chapters\ch03-limits-and-continuity\sections\sec-3-2-calculating-limits.xml](../../source\chapters\ch03-limits-and-continuity\sections\sec-3-2-calculating-limits.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> A limit already assumes x\neq a. Algebra can therefore rewrite the nearby rule. The rewritten rule may be calm, or it may still blow up or disagree from the two sides.

**After**

In a limit at a, only inputs x\ne a are relevant. Algebraic simplification may expose a limit, but the simplified expression must still be checked for unbounded or unequal one-sided behavior.

## 171. Calculating limits

Source: [source\chapters\ch03-limits-and-continuity\sections\sec-3-2-calculating-limits.xml](../../source\chapters\ch03-limits-and-continuity\sections\sec-3-2-calculating-limits.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> Some limits cannot be found by simplifying an expression into something calm. Instead, we trap the function between two simpler functions.

**After**

When algebraic simplification is insufficient, inequalities can bound a function between two functions with the same limit.

## 172. Calculating limits

Source: [source\chapters\ch03-limits-and-continuity\sections\sec-3-2-calculating-limits.xml](../../source\chapters\ch03-limits-and-continuity\sections\sec-3-2-calculating-limits.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> These tools are enough for many early limits. They are not the whole story. Limits can fail from a jump, explode toward infinity, or behave differently on the two sides of a point.

**After**

The next section treats unequal one-sided limits, unbounded outputs, and limits as the input tends to infinity.

## 173. One-sided limits and infinite behavior

Source: [source\chapters\ch03-limits-and-continuity\sections\sec-3-3-one-sided-limits-and-infinite-behavior.xml](../../source\chapters\ch03-limits-and-continuity\sections\sec-3-3-one-sided-limits-and-infinite-behavior.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> we usually mean that x approaches a from both sides. But sometimes the two sides tell different stories.

**After**

we usually mean approach from both sides. The two one-sided limits may differ.

## 174. One-sided limits and infinite behavior

Source: [source\chapters\ch03-limits-and-continuity\sections\sec-3-3-one-sided-limits-and-infinite-behavior.xml](../../source\chapters\ch03-limits-and-continuity\sections\sec-3-3-one-sided-limits-and-infinite-behavior.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> The left-hand limit only uses inputs less than a. The right-hand limit only uses inputs greater than a. A two-sided claim has to satisfy both stories at once.

**After**

A left-hand limit uses inputs less than a; a right-hand limit uses inputs greater than a. A two-sided limit requires agreement between them.

## 175. One-sided limits and infinite behavior

Source: [source\chapters\ch03-limits-and-continuity\sections\sec-3-3-one-sided-limits-and-infinite-behavior.xml](../../source\chapters\ch03-limits-and-continuity\sections\sec-3-3-one-sided-limits-and-infinite-behavior.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> Infinity is a direction of unbounded growth, not a real-number target. From one side the values may shoot up; from the other they may shoot down. Those are different stories.

**After**

Infinity is not a real limiting value. The function may grow without bound positively on one side and negatively on the other, so each side must be described separately.

## 176. The precise definition of a limit

Source: [source\chapters\ch03-limits-and-continuity\sections\sec-3-4-the-precise-definition-of-a-limit.xml](../../source\chapters\ch03-limits-and-continuity\sections\sec-3-4-the-precise-definition-of-a-limit.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> A table can meet a few tolerances. A limit promises that any requested closeness of outputs can be achieved. The challenger chooses \varepsilon first.

**After**

A finite table checks only finitely many inputs. The limit definition requires an input bound for every positive output tolerance \varepsilon.

## 177. Two theorems about continuous functions

Source: [source\chapters\ch03-limits-and-continuity\sections\sec-3-6-two-theorems-about-continuous-functions.xml](../../source\chapters\ch03-limits-and-continuity\sections\sec-3-6-two-theorems-about-continuous-functions.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> The graph may wiggle many times. It may hit the value N more than once. The theorem promises at least one hit, not exactly one.

**After**

The function may take the value N at several points. The theorem guarantees at least one such point, rather than uniqueness.

## 178. Two theorems about continuous functions

Source: [source\chapters\ch03-limits-and-continuity\sections\sec-3-6-two-theorems-about-continuous-functions.xml](../../source\chapters\ch03-limits-and-continuity\sections\sec-3-6-two-theorems-about-continuous-functions.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> A continuous graph cannot jump over a height. The theorem promises at least one hit, not exactly one, and not an exact algebraic expression for the hitting point.

**After**

The Intermediate Value Theorem guarantees a point with the specified intermediate value. It gives neither uniqueness nor a formula for that point.

## 179. Two theorems about continuous functions

Source: [source\chapters\ch03-limits-and-continuity\sections\sec-3-6-two-theorems-about-continuous-functions.xml](../../source\chapters\ch03-limits-and-continuity\sections\sec-3-6-two-theorems-about-continuous-functions.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> Continuity also gives a second global promise.

**After**

Continuity on a closed, bounded interval also ensures that the function attains its extrema.

## 180. Two theorems about continuous functions

Source: [source\chapters\ch03-limits-and-continuity\sections\sec-3-6-two-theorems-about-continuous-functions.xml](../../source\chapters\ch03-limits-and-continuity\sections\sec-3-6-two-theorems-about-continuous-functions.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> promise

**After**

conclusion

## 181. Two theorems about continuous functions

Source: [source\chapters\ch03-limits-and-continuity\sections\sec-3-6-two-theorems-about-continuous-functions.xml](../../source\chapters\ch03-limits-and-continuity\sections\sec-3-6-two-theorems-about-continuous-functions.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> Continuity gave us two promises: no skipped intermediate values, and actual highest and lowest values on closed finite intervals. The next section gathers the warning examples in one place. The goal is to learn when these promises are legal to use, and when a graph is quietly breaking one of the hypotheses.

**After**

The Intermediate Value and Extreme Value Theorems require their stated continuity and interval conditions. The next section gives counterexamples when those conditions are removed.

## 182. Average rate of change

Source: [source\chapters\ch04-the-derivative\sections\sec-4-1-average-rate-of-change.xml](../../source\chapters\ch04-the-derivative\sections\sec-4-1-average-rate-of-change.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> On a straight line, one slope tells the whole story. On a curved graph, the slope between two points depends on which two points we choose.

**After**

A line has constant slope. For a curved graph, the secant slope generally depends on both selected points.

## 183. The derivative as a function

Source: [source\chapters\ch04-the-derivative\sections\sec-4-3-the-derivative-as-a-function.xml](../../source\chapters\ch04-the-derivative\sections\sec-4-3-the-derivative-as-a-function.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> Thus the derivative graph tells the shape story:

**After**

The derivative determines these intervals of increase and decrease:

## 184. Differentiability and continuity

Source: [source\chapters\ch04-the-derivative\sections\sec-4-5-differentiability-and-continuity.xml](../../source\chapters\ch04-the-derivative\sections\sec-4-5-differentiability-and-continuity.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> Continuity promises that the graph does not break.

**After**

Continuity requires nearby function values to approach the value at the point.

## 185. Differentiability and continuity

Source: [source\chapters\ch04-the-derivative\sections\sec-4-5-differentiability-and-continuity.xml](../../source\chapters\ch04-the-derivative\sections\sec-4-5-differentiability-and-continuity.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> It does not promise that the graph has a tangent slope.

**After**

It does not imply that a finite tangent slope exists.

## 186. Differentiability and continuity

Source: [source\chapters\ch04-the-derivative\sections\sec-4-5-differentiability-and-continuity.xml](../../source\chapters\ch04-the-derivative\sections\sec-4-5-differentiability-and-continuity.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> is the example to keep in mind because it is simple and honest. Nothing strange happens to the height. The function is continuous everywhere. The only problem is that at 0, the graph wants two different tangent lines:

**After**

This function is continuous everywhere. At zero, however, its left and right slopes differ:

## 187. Warning examples

Source: [source\chapters\ch04-the-derivative\sections\sec-4-8-warning-examples.xml](../../source\chapters\ch04-the-derivative\sections\sec-4-8-warning-examples.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> The second property is stronger. Many functions in applications have continuous derivatives, and they are pleasant to work with. But the definition of derivative does not promise continuity of f'.

**After**

Continuity of the derivative is a stronger requirement than differentiability. The definition of a derivative does not by itself establish that f\prime is continuous.

## 188. Warning examples

Source: [source\chapters\ch04-the-derivative\sections\sec-4-8-warning-examples.xml](../../source\chapters\ch04-the-derivative\sections\sec-4-8-warning-examples.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> The squeezed oscillation x^2\sin(1/x) is differentiable at 0, yet nearby derivative values do not settle to f'(0). In your own words, why does the definition of derivative not promise that f' varies smoothly, and what stronger property is being separated from mere differentiability?

**After**

The function x^2\sin(1/x), extended by zero at the origin, is differentiable there, but its nearby derivative values do not approach f\prime(0). Explain the distinction between differentiability and continuity of the derivative.

## 189. Chapter review and discovery problems

Source: [source\chapters\ch05-differentiation-rules-and-elementary-functions\sections\sec-5-10-chapter-review-and-discovery-problems.xml](../../source\chapters\ch05-differentiation-rules-and-elementary-functions\sections\sec-5-10-chapter-review-and-discovery-problems.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> The chapter has one main story:

**After**

The rules in this chapter depend on how the function is formed:

## 190. Chapter review and discovery problems

Source: [source\chapters\ch05-differentiation-rules-and-elementary-functions\sections\sec-5-10-chapter-review-and-discovery-problems.xml](../../source\chapters\ch05-differentiation-rules-and-elementary-functions\sections\sec-5-10-chapter-review-and-discovery-problems.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> Chapter 5 has one main story: how a function is built determines how its derivative is built. In your own words, why are a sum, a product, a quotient, a composition, and an inverse different constructions, and why is reading the structure the first step rather than a race to symbols?

**After**

Explain how the differentiation rule depends on whether an expression is a sum, product, quotient, composition, or inverse. Why must this structure be identified before applying a formula?

## 191. General power rule and hyperbolic functions

Source: [source\chapters\ch05-differentiation-rules-and-elementary-functions\sections\sec-5-8-general-power-rule-and-hyperbolic-functions.xml](../../source\chapters\ch05-differentiation-rules-and-elementary-functions\sections\sec-5-8-general-power-rule-and-hyperbolic-functions.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> We have (\sinh x)'=\cosh x and (\cosh x)'=\sinh x, unlike the circular pair with a minus on cosine. In your own words, why does that happen from the exponential definitions, and why are hyperbolic functions not a new mystery?

**After**

Use the exponential definitions to explain why (\sinh x)\prime=\cosh x and (\cosh x)\prime=\sinh x. Compare the signs with the derivatives of sine and cosine.

## 192. Increasing and decreasing functions

Source: [source\chapters\ch06-shape-extremes-and-the-mean-value-theorem\sections\sec-6-1-increasing-and-decreasing-functions.xml](../../source\chapters\ch06-shape-extremes-and-the-mean-value-theorem\sections\sec-6-1-increasing-and-decreasing-functions.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> A critical number is a candidate for an important point on the graph. It is not a promise.

**After**

A critical number is a candidate for an extremum, but need not be one.

## 193. Increasing and decreasing functions

Source: [source\chapters\ch06-shape-extremes-and-the-mean-value-theorem\sections\sec-6-1-increasing-and-decreasing-functions.xml](../../source\chapters\ch06-shape-extremes-and-the-mean-value-theorem\sections\sec-6-1-increasing-and-decreasing-functions.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> A number c in the domain of f is critical if f'(c)=0 or if f'(c) does not exist. In your own words, why does that make c worth inspecting, and why does it not yet promise a high point or a low point?

**After**

A number c in the domain is critical when f\prime(c)=0 or the derivative is undefined. Explain why these points require checking and why either condition can occur without a local extremum.

## 194. Rolle’s Theorem and the Mean Value Theorem

Source: [source\chapters\ch06-shape-extremes-and-the-mean-value-theorem\sections\sec-6-3-rolle-s-theorem-and-the-mean-value-theorem.xml](../../source\chapters\ch06-shape-extremes-and-the-mean-value-theorem\sections\sec-6-3-rolle-s-theorem-and-the-mean-value-theorem.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> The point c may be hard to find. The theorem promises that it exists.

**After**

The theorem guarantees that c exists, even if it is difficult to calculate.

## 195. Rolle’s Theorem and the Mean Value Theorem

Source: [source\chapters\ch06-shape-extremes-and-the-mean-value-theorem\sections\sec-6-3-rolle-s-theorem-and-the-mean-value-theorem.xml](../../source\chapters\ch06-shape-extremes-and-the-mean-value-theorem\sections\sec-6-3-rolle-s-theorem-and-the-mean-value-theorem.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> Continuity on the closed interval, differentiability on the open interval, and (for Rolle) equal endpoint heights each prevent a different escape. In your own words, why can a jump, a corner, or unequal endpoint heights keep a graph from having the tangent the theorem promises?

**After**

Explain the roles of continuity on the closed interval, differentiability on its interior, and equal endpoint values in Rolle's Theorem. Which hypotheses fail for a jump or a corner?

## 196. Concavity and second derivatives

Source: [source\chapters\ch06-shape-extremes-and-the-mean-value-theorem\sections\sec-6-4-concavity-and-second-derivatives.xml](../../source\chapters\ch06-shape-extremes-and-the-mean-value-theorem\sections\sec-6-4-concavity-and-second-derivatives.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> The units also tell the story. If s(t) is measured in meters and t in seconds, then

**After**

If s(t) is measured in meters and t in seconds, the derivative units are

## 197. Warning examples

Source: [source\chapters\ch06-shape-extremes-and-the-mean-value-theorem\sections\sec-6-7-warning-examples.xml](../../source\chapters\ch06-shape-extremes-and-the-mean-value-theorem\sections\sec-6-7-warning-examples.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> The graph does return to the same height, but it turns too sharply. Rolle’s Theorem and the Mean Value Theorem do not promise a horizontal tangent unless the function is differentiable throughout the open interval.

**After**

The endpoint values agree, but the function has a corner. Rolle's Theorem does not apply because differentiability fails at an interior point.

## 198. Chapter review and discovery problems

Source: [source\chapters\ch06-shape-extremes-and-the-mean-value-theorem\sections\sec-6-8-chapter-review-and-discovery-problems.xml](../../source\chapters\ch06-shape-extremes-and-the-mean-value-theorem\sections\sec-6-8-chapter-review-and-discovery-problems.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> The first derivative is about direction of change; the second is about how that direction itself is changing. Sign charts are a way of reading those stories across intervals.

**After**

The sign of the first derivative describes increase and decrease. The sign of the second derivative describes increase and decrease of the slope. Sign charts organize these properties across intervals.

## 199. Chapter review and discovery problems

Source: [source\chapters\ch06-shape-extremes-and-the-mean-value-theorem\sections\sec-6-8-chapter-review-and-discovery-problems.xml](../../source\chapters\ch06-shape-extremes-and-the-mean-value-theorem\sections\sec-6-8-chapter-review-and-discovery-problems.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> Those questions still use derivatives, but now the graph is only part of the story. The next chapter turns shape information into decisions: related rates, optimization, and models.

**After**

The next chapter applies derivatives to related rates, optimization, and mathematical models.

## 200. Newton’s method

Source: [source\chapters\ch07-optimization-related-rates-and-models\sections\sec-7-4-newton-s-method.xml](../../source\chapters\ch07-optimization-related-rates-and-models\sections\sec-7-4-newton-s-method.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> Newton’s method can be fast. But it is not magic. It is a local method, just like linear approximation.

**After**

Newton's method uses a local linear approximation. Its convergence depends on the root, the derivative, and the starting value.

## 201. Newton’s method

Source: [source\chapters\ch07-optimization-related-rates-and-models\sections\sec-7-4-newton-s-method.xml](../../source\chapters\ch07-optimization-related-rates-and-models\sections\sec-7-4-newton-s-method.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> Linear approximation is local, so Newton’s method is local. Near a simple root the error is roughly squared at each step; a horizontal tangent at the root is a different story.

**After**

Near a simple root, under suitable smoothness conditions, Newton's error is approximately squared at each step. A multiple root requires a different convergence analysis.

## 202. Exponential growth and decay

Source: [source\chapters\ch07-optimization-related-rates-and-models\sections\sec-7-5-exponential-growth-and-decay.xml](../../source\chapters\ch07-optimization-related-rates-and-models\sections\sec-7-5-exponential-growth-and-decay.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> Continuously compounded interest and Newton’s law of cooling look like different stories. In your own words, why are they both versions of a rate proportional to the current amount (or to the current difference from equilibrium), and what does that common structure buy us?

**After**

Explain how continuously compounded interest and Newton's law of cooling both use a rate proportional to a current amount or difference from equilibrium. How does this relation determine the solution form?

## 203. Exponential growth and decay

Source: [source\chapters\ch07-optimization-related-rates-and-models\sections\sec-7-5-exponential-growth-and-decay.xml](../../source\chapters\ch07-optimization-related-rates-and-models\sections\sec-7-5-exponential-growth-and-decay.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> The equation y'=ky says y'/y=k. A quantity can increase without being exponential. In your own words, why is a changing relative rate a warning that the exponential model is the wrong promise, even if the graph is rising?

**After**

Where y\ne0, the exponential equation y\prime=ky specifies the constant relative rate y\prime/y=k. Explain why increasing values alone do not establish exponential growth.

## 204. Logistic growth and limited resources

Source: [source\chapters\ch07-optimization-related-rates-and-models\sections\sec-7-6-logistic-growth-and-limited-resources.xml](../../source\chapters\ch07-optimization-related-rates-and-models\sections\sec-7-6-logistic-growth-and-limited-resources.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> The law P'=rP has no built-in stopping mechanism. In your own words, why may that model still be excellent at the beginning of a process, and why must a bounded environment eventually make it the wrong whole-life story?

**After**

The model P\prime=rP, with r>0, permits unbounded growth. Explain why it can approximate early population growth and why limited resources may invalidate it later.

## 205. Logistic growth and limited resources

Source: [source\chapters\ch07-optimization-related-rates-and-models\sections\sec-7-6-logistic-growth-and-limited-resources.xml](../../source\chapters\ch07-optimization-related-rates-and-models\sections\sec-7-6-logistic-growth-and-limited-resources.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> Exponential growth promises constant relative growth.

**After**

Exponential growth assumes a constant relative growth rate.

## 206. Logistic growth and limited resources

Source: [source\chapters\ch07-optimization-related-rates-and-models\sections\sec-7-6-logistic-growth-and-limited-resources.xml](../../source\chapters\ch07-optimization-related-rates-and-models\sections\sec-7-6-logistic-growth-and-limited-resources.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> Logistic growth promises constant early relative growth and a fixed carrying capacity.

**After**

Logistic growth assumes a fixed carrying capacity and a relative growth rate r(1-P/K), approximately r when P\ll K.

## 207. Logistic growth and limited resources

Source: [source\chapters\ch07-optimization-related-rates-and-models\sections\sec-7-6-logistic-growth-and-limited-resources.xml](../../source\chapters\ch07-optimization-related-rates-and-models\sections\sec-7-6-logistic-growth-and-limited-resources.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> Before trusting the formula, check whether the promise matches the situation.

**After**

Check whether these assumptions describe the situation before using the model to predict its behavior.

## 208. Logistic growth and limited resources

Source: [source\chapters\ch07-optimization-related-rates-and-models\sections\sec-7-6-logistic-growth-and-limited-resources.xml](../../source\chapters\ch07-optimization-related-rates-and-models\sections\sec-7-6-logistic-growth-and-limited-resources.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> When P is far below K, logistic growth and exponential growth look almost the same. In your own words, why might early data reveal r but not K, and what does that show about treating a model as a promise with conditions?

**After**

When P\ll K, the logistic model closely approximates exponential growth. Explain why early data may estimate r while providing little information about K.

## 209. Light, time, and extremal principles

Source: [source\chapters\ch07-optimization-related-rates-and-models\sections\sec-7-7-light-time-and-extremal-principles.xml](../../source\chapters\ch07-optimization-related-rates-and-models\sections\sec-7-7-light-time-and-extremal-principles.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> But the deeper problem asks for an entire path.

**After**

A more general problem varies an entire path.

## 210. Light, time, and extremal principles

Source: [source\chapters\ch07-optimization-related-rates-and-models\sections\sec-7-7-light-time-and-extremal-principles.xml](../../source\chapters\ch07-optimization-related-rates-and-models\sections\sec-7-7-light-time-and-extremal-principles.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> The word stationary is important. It means that the first derivative-like change is zero. The path may be the absolute shortest or fastest path, but the deeper condition is local: nearby path changes do not change the total time to first order.

**After**

A stationary path has zero first-order change in travel time under the allowed small path variations. This condition does not by itself establish an absolute minimum.

## 211. Light, time, and extremal principles

Source: [source\chapters\ch07-optimization-related-rates-and-models\sections\sec-7-7-light-time-and-extremal-principles.xml](../../source\chapters\ch07-optimization-related-rates-and-models\sections\sec-7-7-light-time-and-extremal-principles.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> In the reflection and refraction examples, the unknown was one strike point. The deeper problem asks for an entire path. In your own words, why is a quantity that takes a path as input and returns a time or length as output a new kind of optimization, and why is that the seed of the calculus of variations?

**After**

The reflection and refraction examples vary one crossing point. A functional instead takes an entire path as input and returns a number such as time or length. Explain how this changes the optimization problem.

## 212. Chapter review and applications

Source: [source\chapters\ch07-optimization-related-rates-and-models\sections\sec-7-9-chapter-review-and-applications.xml](../../source\chapters\ch07-optimization-related-rates-and-models\sections\sec-7-9-chapter-review-and-applications.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> The hard part is not memorizing formulas. The hard part is choosing the right quantities and keeping the model honest.

**After**

Choose quantities and constraints that represent the situation, and check the resulting model's domain and assumptions.

## 213. Chapter review and applications

Source: [source\chapters\ch07-optimization-related-rates-and-models\sections\sec-7-9-chapter-review-and-applications.xml](../../source\chapters\ch07-optimization-related-rates-and-models\sections\sec-7-9-chapter-review-and-applications.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> The formula tells a physical story. If the circular ends are expensive, the design tries to reduce their area by using a smaller radius. To keep the same volume, the height must increase.

**After**

If the circular ends cost more, the minimizing radius decreases. Maintaining the fixed volume then requires a greater height.

## 214. Chapter review and applications

Source: [source\chapters\ch07-optimization-related-rates-and-models\sections\sec-7-9-chapter-review-and-applications.xml](../../source\chapters\ch07-optimization-related-rates-and-models\sections\sec-7-9-chapter-review-and-applications.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> Exponential growth promises a constant relative rate. Logistic growth adds a fixed carrying capacity. In your own words, why must we check whether that promise matches the situation before trusting a formula, and what goes wrong if the conditions are invisible in the early data?

**After**

Exponential growth assumes a constant relative rate; logistic growth adds a fixed carrying capacity. Explain why these assumptions must be checked and why early data may not reveal the eventual capacity.

## 215. Chapter review and applications

Source: [source\chapters\ch07-optimization-related-rates-and-models\sections\sec-7-9-chapter-review-and-applications.xml](../../source\chapters\ch07-optimization-related-rates-and-models\sections\sec-7-9-chapter-review-and-applications.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> A formula can be mathematically correct and still be the wrong story. Early exponential-looking data may hide a later ceiling.

**After**

A correct calculation does not validate the model's assumptions. Early data resembling exponential growth may fail to reveal a later resource limit.

## 216. Distance from velocity

Source: [source\chapters\ch08-the-integral-as-accumulation\sections\sec-8-1-distance-from-velocity.xml](../../source\chapters\ch08-the-integral-as-accumulation\sections\sec-8-1-distance-from-velocity.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> The graph tells the same story. The area under the velocity graph is the sum of three rectangle areas.

**After**

The displacement is the sum of the three rectangle areas under the velocity graph.

## 217. Distance from velocity

Source: [source\chapters\ch08-the-integral-as-accumulation\sections\sec-8-1-distance-from-velocity.xml](../../source\chapters\ch08-the-integral-as-accumulation\sections\sec-8-1-distance-from-velocity.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> On a short piece, the assumption that velocity hardly changes becomes more reasonable. Accumulation is the act of adding those local stories.

**After**

On sufficiently short intervals, slowly varying velocity is approximated by a constant. Summing the corresponding displacements estimates the total displacement.

## 218. Sigma notation and finite sums

Source: [source\chapters\ch08-the-integral-as-accumulation\sections\sec-8-3-sigma-notation-and-finite-sums.xml](../../source\chapters\ch08-the-integral-as-accumulation\sections\sec-8-3-sigma-notation-and-finite-sums.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> These rules are not mysterious. They come from ordinary addition.

**After**

These rules follow from the corresponding rules for finite addition.

## 219. Sigma notation and finite sums

Source: [source\chapters\ch08-the-integral-as-accumulation\sections\sec-8-3-sigma-notation-and-finite-sums.xml](../../source\chapters\ch08-the-integral-as-accumulation\sections\sec-8-3-sigma-notation-and-finite-sums.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> This is another hint of the larger story:

**After**

This finite-sum identity anticipates the relation between differentiation and integration:

## 220. The definite integral

Source: [source\chapters\ch08-the-integral-as-accumulation\sections\sec-8-4-the-definite-integral.xml](../../source\chapters\ch08-the-integral-as-accumulation\sections\sec-8-4-the-definite-integral.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> This warning is not meant to frighten us. It tells us why the definition is honest. The continuous functions, piecewise continuous functions, and ordinary models of science and geometry are integrable. But the definition knows how to reject functions that oscillate too violently at every scale.

**After**

Boundedness alone does not imply Riemann integrability. Continuous functions and bounded piecewise-continuous functions on a closed finite interval are integrable, but a bounded function can fail to have convergent Riemann sums.

## 221. Properties of the integral

Source: [source\chapters\ch08-the-integral-as-accumulation\sections\sec-8-6-properties-of-the-integral.xml](../../source\chapters\ch08-the-integral-as-accumulation\sections\sec-8-6-properties-of-the-integral.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> The properties of the integral are not mysterious. They are the properties of finite sums surviving a limiting process.

**After**

Linearity, interval splitting, and order properties of integrals follow by passing the corresponding finite-sum properties to limits.

## 222. Existence of integrals

Source: [source\chapters\ch08-the-integral-as-accumulation\sections\sec-8-7-existence-of-integrals.xml](../../source\chapters\ch08-the-integral-as-accumulation\sections\sec-8-7-existence-of-integrals.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> If the most generous overestimate and the most cautious underestimate can be made arbitrarily close, there is only one number left for the integral to be.

**After**

If upper and lower sums can be made arbitrarily close, their limiting values agree and determine a unique integral.

## 223. Existence of integrals

Source: [source\chapters\ch08-the-integral-as-accumulation\sections\sec-8-7-existence-of-integrals.xml](../../source\chapters\ch08-the-integral-as-accumulation\sections\sec-8-7-existence-of-integrals.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> The chapter ends by practicing the setup. The next chapter will reveal the surprise: if the upper endpoint moves, an integral becomes a function, and its derivative is the function we started with.

**After**

The next chapter studies accumulation functions with a moving endpoint. For a continuous integrand, differentiating the accumulation recovers the integrand.

## 224. Chapter review and discovery problems

Source: [source\chapters\ch08-the-integral-as-accumulation\sections\sec-8-8-chapter-review-and-discovery-problems.xml](../../source\chapters\ch08-the-integral-as-accumulation\sections\sec-8-8-chapter-review-and-discovery-problems.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> This is the next great surprise.

**After**

The Fundamental Theorem will establish this relation between integration and differentiation.

## 225. Fundamental Theorem, Part II

Source: [source\chapters\ch09-the-fundamental-theorem-of-calculus\sections\sec-9-3-fundamental-theorem-part-ii.xml](../../source\chapters\ch09-the-fundamental-theorem-of-calculus\sections\sec-9-3-fundamental-theorem-part-ii.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> The dashboard story now becomes a theorem.

**After**

The theorem applies the rate-accumulation relation to motion.

## 226. Indefinite integrals

Source: [source\chapters\ch09-the-fundamental-theorem-of-calculus\sections\sec-9-4-indefinite-integrals.xml](../../source\chapters\ch09-the-fundamental-theorem-of-calculus\sections\sec-9-4-indefinite-integrals.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> These formulas are not separate magic. They are derivative facts read backward.

**After**

These antiderivative formulas follow from the corresponding derivative formulas.

## 227. Warning examples

Source: [source\chapters\ch09-the-fundamental-theorem-of-calculus\sections\sec-9-6-warning-examples.xml](../../source\chapters\ch09-the-fundamental-theorem-of-calculus\sections\sec-9-6-warning-examples.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> Pulling a non-constant factor out of an integral, or treating \int f(x)\,dx as if it were f(x) times x, can look algebraically tempting. In your own words, why is that a false pattern, and what is the honest check that an antiderivative formula is right?

**After**

Explain why a variable factor cannot generally be pulled outside an integral and why \int f(x)\,dx is not generally xf(x). How can differentiation check a proposed antiderivative?

## 228. Cylindrical shells

Source: [source\chapters\ch10-what-integrals-measure\sections\sec-10-3-cylindrical-shells.xml](../../source\chapters\ch10-what-integrals-measure\sections\sec-10-3-cylindrical-shells.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> The word “approximately” is doing honest work. The outer surface of the shell has a slightly larger circumference than the inner surface. But when the thickness is very small, the difference is very small.

**After**

The inner and outer shell circumferences differ, so circumference times thickness gives an approximation to the annular cross-section. The resulting discrepancy tends to zero in the limiting sum.

## 229. Work and energy

Source: [source\chapters\ch10-what-integrals-measure\sections\sec-10-5-work-and-energy.xml](../../source\chapters\ch10-what-integrals-measure\sections\sec-10-5-work-and-energy.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> Constant force times distance is exact when the force does not change. In your own words, why is (\text{final force})(\text{total distance}) the wrong story for a spring or a changing push, and why does adding F(x)\,dx repair it?

**After**

For constant force along the motion, work equals force times displacement. Explain why using only the final force is invalid for a varying force and how \int F(x)\,dx accounts for the variation.

## 230. Average value and probability

Source: [source\chapters\ch10-what-integrals-measure\sections\sec-10-7-average-value-and-probability.xml](../../source\chapters\ch10-what-integrals-measure\sections\sec-10-7-average-value-and-probability.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> But there is a surprise. The function

**After**

However, the function

## 231. Arc length and surface area of revolution

Source: [source\chapters\ch10-what-integrals-measure\sections\sec-10-8-arc-length-and-surface-area-of-revolution.xml](../../source\chapters\ch10-what-integrals-measure\sections\sec-10-8-arc-length-and-surface-area-of-revolution.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> This is an important moment in the story.

**After**

The length calculation uses the speed along the curve.

## 232. Chapter review and applications

Source: [source\chapters\ch10-what-integrals-measure\sections\sec-10-9-chapter-review-and-applications.xml](../../source\chapters\ch10-what-integrals-measure\sections\sec-10-9-chapter-review-and-applications.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> Exact formulas are useful, but real tanks are not always cones, cylinders, or rectangular boxes. Sometimes the most honest description is measured data.

**After**

When a tank's shape has no convenient formula, measured cross-sectional data can be used to approximate the volume.

## 233. Trigonometric integrals

Source: [source\chapters\ch11-techniques-of-integration\sections\sec-11-2-trigonometric-integrals.xml](../../source\chapters\ch11-techniques-of-integration\sections\sec-11-2-trigonometric-integrals.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> The deeper habit is this:

**After**

The method uses this choice of factors:

## 234. Trigonometric substitution

Source: [source\chapters\ch11-techniques-of-integration\sections\sec-11-3-trigonometric-substitution.xml](../../source\chapters\ch11-techniques-of-integration\sections\sec-11-3-trigonometric-substitution.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> The expression \sqrt{9-x^2} is the upper half of a circle. In your own words, why does choosing x=3\sin\theta make the square root become 3\cos\theta, and why is that not magic but a Pythagorean identity?

**After**

For x=3\sin\theta, derive \sqrt{9-x^2}=3\cos\theta on a branch where \cos\theta\ge0. Which identity and sign condition are needed?

## 235. Chapter review and discovery problems

Source: [source\chapters\ch11-techniques-of-integration\sections\sec-11-9-chapter-review-and-discovery-problems.xml](../../source\chapters\ch11-techniques-of-integration\sections\sec-11-9-chapter-review-and-discovery-problems.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> Exact integration is powerful, but it is not the whole story.

**After**

When exact integration is unavailable, numerical integration can approximate the value.

## 236. Why approximate integrals?

Source: [source\chapters\ch12-numerical-integration-error-and-computation\sections\sec-12-1-why-approximate-integrals.xml](../../source\chapters\ch12-numerical-integration-error-and-computation\sections\sec-12-1-why-approximate-integrals.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> Think about a missed spike, an improper integral, or arithmetic that subtracts nearly equal numbers. A rule without an error story is still a guess.

**After**

A missed narrow peak, an improper endpoint, or subtractive rounding can invalidate an approximation. The algorithm must supply an applicable error bound or an explicitly qualified estimate.

## 237. Simpson’s Rule

Source: [source\chapters\ch12-numerical-integration-error-and-computation\sections\sec-12-3-simpson-s-rule.xml](../../source\chapters\ch12-numerical-integration-error-and-computation\sections\sec-12-3-simpson-s-rule.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> So it should be exact for quadratic functions. The surprise is that it is also exact for cubic functions.

**After**

Simpson's rule integrates quadratics exactly and, by symmetry, also integrates cubics exactly.

## 238. Numerical differentiation

Source: [source\chapters\ch12-numerical-integration-error-and-computation\sections\sec-12-4-numerical-differentiation.xml](../../source\chapters\ch12-numerical-integration-error-and-computation\sections\sec-12-4-numerical-differentiation.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> Numerical integration and numerical differentiation both replace a limit by a finite calculation. Each method has an error story.

**After**

Numerical integration and numerical differentiation replace limiting definitions by finite calculations. Both require analysis of truncation and rounding errors.

## 239. Newton’s method revisited

Source: [source\chapters\ch12-numerical-integration-error-and-computation\sections\sec-12-5-newton-s-method-revisited.xml](../../source\chapters\ch12-numerical-integration-error-and-computation\sections\sec-12-5-newton-s-method-revisited.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> When the starting point is close to a simple root, the dynamics are friendly. The root attracts nearby iterates.

**After**

Under the local convergence hypotheses, a simple root attracts Newton iterates started sufficiently close to it.

## 240. Newton’s method revisited

Source: [source\chapters\ch12-numerical-integration-error-and-computation\sections\sec-12-5-newton-s-method-revisited.xml](../../source\chapters\ch12-numerical-integration-error-and-computation\sections\sec-12-5-newton-s-method-revisited.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> Near a simple root the iteration is friendly, but the same formula is a dynamical system. In your own words, what kinds of failure can occur from a bad starting point, and why should a safe workflow monitor iterates rather than trust the formula blindly?

**After**

Newton's method can converge rapidly near a simple root yet fail from another starting value. Describe possible failures and explain which quantities should be monitored during iteration.

## 241. Newton’s method revisited

Source: [source\chapters\ch12-numerical-integration-error-and-computation\sections\sec-12-5-newton-s-method-revisited.xml](../../source\chapters\ch12-numerical-integration-error-and-computation\sections\sec-12-5-newton-s-method-revisited.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> A tiny change from 1 to 1.01 has produced a very different next story.

**After**

Changing the initial value from 1 to 1.01 changes the subsequent iterates substantially.

## 242. Newton’s method revisited

Source: [source\chapters\ch12-numerical-integration-error-and-computation\sections\sec-12-5-newton-s-method-revisited.xml](../../source\chapters\ch12-numerical-integration-error-and-computation\sections\sec-12-5-newton-s-method-revisited.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> It is here because it shows something deeper: an iteration can have a simple rule and complicated behavior.

**After**

This example shows that a simple iteration rule can produce complicated behavior.

## 243. Newton’s method revisited

Source: [source\chapters\ch12-numerical-integration-error-and-computation\sections\sec-12-5-newton-s-method-revisited.xml](../../source\chapters\ch12-numerical-integration-error-and-computation\sections\sec-12-5-newton-s-method-revisited.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> This warning does not make Newton’s method less valuable. It makes it more honest. In serious computation, a fast method and a safety check belong together.

**After**

Practical use of Newton's method requires checks on convergence, residuals, and the computed iterates.

## 244. Computing experiments

Source: [source\chapters\ch12-numerical-integration-error-and-computation\sections\sec-12-6-computing-experiments.xml](../../source\chapters\ch12-numerical-integration-error-and-computation\sections\sec-12-6-computing-experiments.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> Both stories have the same lesson.

**After**

Both examples illustrate the need to test a stopping criterion against a known reference.

## 245. Chapter review and discovery problems

Source: [source\chapters\ch12-numerical-integration-error-and-computation\sections\sec-12-7-chapter-review-and-discovery-problems.xml](../../source\chapters\ch12-numerical-integration-error-and-computation\sections\sec-12-7-chapter-review-and-discovery-problems.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> starting from x_0=1. What happens? Why should this not surprise you?

**After**

starting from x_0=1. What happens, and which feature of the iteration explains the result?

## 246. Additional topics: Richardson and Romberg methods

Source: [source\chapters\ch12-numerical-integration-error-and-computation\sections\sec-additional-richardson-romberg.xml](../../source\chapters\ch12-numerical-integration-error-and-computation\sections\sec-additional-richardson-romberg.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> Column j cancels the leading term of order h^{2j} left by the preceding column. For each fixed j, under sufficient smoothness its error is O(h_k^{2j+2}). This is an asymptotic statement as the mesh is refined; it does not promise that every new diagonal entry improves a finite-precision calculation.

**After**

Column j cancels the leading error of order h^{2j} from the preceding column. For fixed j and sufficient smoothness, its error is O(h_k^{2j+2}) as the mesh shrinks. Finite-precision diagonal entries need not improve at every refinement.

## 247. Chapter review and applications

Source: [source\chapters\ch13-differential-equations-laws-written-as-derivatives\sections\sec-13-10-chapter-review-and-applications.xml](../../source\chapters\ch13-differential-equations-laws-written-as-derivatives\sections\sec-13-10-chapter-review-and-applications.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> This chapter ends one story and opens another.

**After**

The next chapter changes the coordinate description of curves.

## 248. Euler’s method

Source: [source\chapters\ch13-differential-equations-laws-written-as-derivatives\sections\sec-13-3-euler-s-method.xml](../../source\chapters\ch13-differential-equations-laws-written-as-derivatives\sections\sec-13-3-euler-s-method.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> The word “usually” belongs in the sentence. A numerical method is not magic. If the step size is too large, the method may follow the wrong behavior.

**After**

Accuracy improves under the convergence hypotheses as the step shrinks. A large step can instead produce behavior inconsistent with the exact solution.

## 249. Euler’s method

Source: [source\chapters\ch13-differential-equations-laws-written-as-derivatives\sections\sec-13-3-euler-s-method.xml](../../source\chapters\ch13-differential-equations-laws-written-as-derivatives\sections\sec-13-3-euler-s-method.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> This does not make Euler’s method useless. It makes it honest. We should use it with step-size discipline and with checks against qualitative behavior.

**After**

Choose the step size using accuracy and stability considerations, and compare the numerical behavior with the direction field.

## 250. Euler’s method

Source: [source\chapters\ch13-differential-equations-laws-written-as-derivatives\sections\sec-13-3-euler-s-method.xml](../../source\chapters\ch13-differential-equations-laws-written-as-derivatives\sections\sec-13-3-euler-s-method.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> Smaller steps usually reduce error, but they are not magic. For y'=-4y, a large step can produce growing oscillations even though the true solution decays. In your own words, why is the numerical method a different object from the differential equation?

**After**

For y\prime=-4y, a large Euler step can produce growing oscillations although the exact solution decays. Explain how the numerical update produces this discrepancy.

## 251. Euler’s method

Source: [source\chapters\ch13-differential-equations-laws-written-as-derivatives\sections\sec-13-3-euler-s-method.xml](../../source\chapters\ch13-differential-equations-laws-written-as-derivatives\sections\sec-13-3-euler-s-method.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> Each Euler point is approximate, and the next slope is computed at that approximate point. A step that is too large can leave the qualitative story of the field.

**After**

Each Euler value is approximate, and the next slope is evaluated at that value. A large step may therefore lead to behavior inconsistent with the direction field.

## 252. Euler’s method

Source: [source\chapters\ch13-differential-equations-laws-written-as-derivatives\sections\sec-13-3-euler-s-method.xml](../../source\chapters\ch13-differential-equations-laws-written-as-derivatives\sections\sec-13-3-euler-s-method.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> That statement is honest. It names the approximation.

**After**

This statement identifies the numerical approximation and its step size.

## 253. Separable equations

Source: [source\chapters\ch13-differential-equations-laws-written-as-derivatives\sections\sec-13-4-separable-equations.xml](../../source\chapters\ch13-differential-equations-laws-written-as-derivatives\sections\sec-13-4-separable-equations.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> For y'=y(1-y), dividing by y(1-y) assumes y\neq0 and y\neq1. In your own words, why are those excluded values often the most important solutions in a model, and what honest extra step should follow every such division?

**After**

For y\prime=y(1-y), dividing by y(1-y) excludes y=0 and y=1. Explain why these are equilibrium solutions and how to check such excluded cases.

## 254. Logistic and threshold models

Source: [source\chapters\ch13-differential-equations-laws-written-as-derivatives\sections\sec-13-5-logistic-and-threshold-models.xml](../../source\chapters\ch13-differential-equations-laws-written-as-derivatives\sections\sec-13-5-logistic-and-threshold-models.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> The logistic equation multiplies the exponential factor rP by 1-P/K. In your own words, what story do those two factors tell, and why is pure exponential growth a good early approximation but a bad forever-model?

**After**

Explain the roles of rP and 1-P/K in the logistic equation. Why does the exponential model approximate early growth when P\ll K but fail to model a fixed carrying capacity?

## 255. Logistic and threshold models

Source: [source\chapters\ch13-differential-equations-laws-written-as-derivatives\sections\sec-13-5-logistic-and-threshold-models.xml](../../source\chapters\ch13-differential-equations-laws-written-as-derivatives\sections\sec-13-5-logistic-and-threshold-models.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> This model has a different story from logistic growth.

**After**

The threshold model has different equilibria and sign intervals from the logistic model.

## 256. Logistic and threshold models

Source: [source\chapters\ch13-differential-equations-laws-written-as-derivatives\sections\sec-13-5-logistic-and-threshold-models.xml](../../source\chapters\ch13-differential-equations-laws-written-as-derivatives\sections\sec-13-5-logistic-and-threshold-models.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> In P'=rP(1-P/K)-h, equilibria occur where the logistic growth curve meets the harvest line. In your own words, why is there a largest sustainable constant harvest, and what happens to the story if the harvest exceeds that value?

**After**

For P\prime=rP(1-P/K)-h, equilibria occur where logistic growth equals the harvest rate. Explain why the maximum of the growth term gives the largest sustainable constant harvest and what happens when h exceeds it.

## 257. First-order linear equations

Source: [source\chapters\ch13-differential-equations-laws-written-as-derivatives\sections\sec-13-6-first-order-linear-equations.xml](../../source\chapters\ch13-differential-equations-laws-written-as-derivatives\sections\sec-13-6-first-order-linear-equations.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> This example was friendly because the right side was constant. We need a method that also works when p(t) and q(t) vary with time.

**After**

The preceding equation had a constant right side. An integrating factor also handles time-dependent p(t) and q(t).

## 258. First-order linear equations

Source: [source\chapters\ch13-differential-equations-laws-written-as-derivatives\sections\sec-13-6-first-order-linear-equations.xml](../../source\chapters\ch13-differential-equations-laws-written-as-derivatives\sections\sec-13-6-first-order-linear-equations.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> Mixing tanks and continuous deposits produce linear equations with an outside input. In your own words, why does the solution combine an initial amount with accumulated weighted input, and what would q(t)=0 mean in those stories?

**After**

Explain why a first-order linear solution combines an initial amount with an accumulated weighted input. What does q(t)=0 mean in a mixing or deposit model?

## 259. Second-order equations and vibration

Source: [source\chapters\ch13-differential-equations-laws-written-as-derivatives\sections\sec-13-7-second-order-equations-and-vibration.xml](../../source\chapters\ch13-differential-equations-laws-written-as-derivatives\sections\sec-13-7-second-order-equations-and-vibration.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> is friendly because sine and cosine repeat under differentiation.

**After**

has sine and cosine solutions because their second derivatives are negative multiples of themselves.

## 260. Second-order equations and vibration

Source: [source\chapters\ch13-differential-equations-laws-written-as-derivatives\sections\sec-13-7-second-order-equations-and-vibration.xml](../../source\chapters\ch13-differential-equations-laws-written-as-derivatives\sections\sec-13-7-second-order-equations-and-vibration.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> The denominator tells the story. If the driving frequency \gamma is close to the natural frequency \omega, then

**After**

If the driving frequency \gamma is close to the natural frequency \omega, the denominator becomes small:

## 261. Warning examples

Source: [source\chapters\ch13-differential-equations-laws-written-as-derivatives\sections\sec-13-9-warning-examples.xml](../../source\chapters\ch13-differential-equations-laws-written-as-derivatives\sections\sec-13-9-warning-examples.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> Losing them would lose the story.

**After**

Discarding these solutions would omit the model's equilibria.

## 262. Warning examples

Source: [source\chapters\ch13-differential-equations-laws-written-as-derivatives\sections\sec-13-9-warning-examples.xml](../../source\chapters\ch13-differential-equations-laws-written-as-derivatives\sections\sec-13-9-warning-examples.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> Separation often begins by dividing by an expression involving y. In your own words, why are the values that make that expression zero often the equilibria of a model, and what story is lost if they are discarded?

**After**

When separation divides by an expression in y, its zeros are candidates for equilibrium solutions. Explain how to test them and why discarding them can omit important model behavior.

## 263. Warning examples

Source: [source\chapters\ch13-differential-equations-laws-written-as-derivatives\sections\sec-13-9-warning-examples.xml](../../source\chapters\ch13-differential-equations-laws-written-as-derivatives\sections\sec-13-9-warning-examples.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> This is why numerical methods and direction fields belong together. The direction field does not give exact values, but it can catch a numerical approximation that is following the wrong story.

**After**

A direction field can reveal numerical values inconsistent with the equation's slopes, even when it cannot provide exact solution values.

## 264. Parametric curves

Source: [source\chapters\ch14-parametric-curves-polar-coordinates-and-conics\sections\sec-14-1-parametric-curves.xml](../../source\chapters\ch14-parametric-curves-polar-coordinates-and-conics\sections\sec-14-1-parametric-curves.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> The formulas alone do not tell the whole story. The parameter interval matters.

**After**

The coordinate formulas must be accompanied by a parameter interval to specify which part of the curve is traced and how often.

## 265. Chapter review and projects

Source: [source\chapters\ch14-parametric-curves-polar-coordinates-and-conics\sections\sec-14-10-chapter-review-and-projects.xml](../../source\chapters\ch14-parametric-curves-polar-coordinates-and-conics\sections\sec-14-10-chapter-review-and-projects.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> An ellipse centered at the origin and an ellipse with a focus at the pole tell different stories. In your own words, why does planetary motion prefer the polar description, and what extra law besides the shape of the orbit is needed?

**After**

Compare an ellipse centered at the origin with one whose focus is at the pole. Explain the usefulness of the focus-based polar equation for an orbit and which law describes the rate of traversal.

## 266. Chapter review and projects

Source: [source\chapters\ch14-parametric-curves-polar-coordinates-and-conics\sections\sec-14-10-chapter-review-and-projects.xml](../../source\chapters\ch14-parametric-curves-polar-coordinates-and-conics\sections\sec-14-10-chapter-review-and-projects.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> Complex multiplication scales and rotates. In your own words, how does that continue the chapter’s move from graphs to motions, and why does Euler’s formula point toward infinite series rather than finish the story here?

**After**

Explain how complex multiplication represents scaling and rotation. Which power-series results are needed to justify Euler's formula?

## 267. Length and area for parametric curves

Source: [source\chapters\ch14-parametric-curves-polar-coordinates-and-conics\sections\sec-14-3-length-and-area-for-parametric-curves.xml](../../source\chapters\ch14-parametric-curves-polar-coordinates-and-conics\sections\sec-14-3-length-and-area-for-parametric-curves.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> A symmetric and orientation-friendly formula is

**After**

An area formula that also records orientation is

## 268. Planetary motion as a capstone

Source: [source\chapters\ch14-parametric-curves-polar-coordinates-and-conics\sections\sec-14-7-planetary-motion-as-a-capstone.xml](../../source\chapters\ch14-parametric-curves-polar-coordinates-and-conics\sections\sec-14-7-planetary-motion-as-a-capstone.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> Gravity points along the line from the planet to the sun, so it has no sideways component. In your own words, why does that make r^2\theta' constant, and what part of the story still belongs to multivariable calculus?

**After**

A central gravitational force has no tangential component. Explain why this implies conservation of r^2\theta\prime and which additional coordinate calculations are needed for a full orbit derivation.

## 269. Planetary motion as a capstone

Source: [source\chapters\ch14-parametric-curves-polar-coordinates-and-conics\sections\sec-14-7-planetary-motion-as-a-capstone.xml](../../source\chapters\ch14-parametric-curves-polar-coordinates-and-conics\sections\sec-14-7-planetary-motion-as-a-capstone.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> But the full story naturally belongs to multivariable calculus.

**After**

A full derivation requires the vector and coordinate tools developed in multivariable calculus.

## 270. Complex numbers and polar form

Source: [source\chapters\ch14-parametric-curves-polar-coordinates-and-conics\sections\sec-14-8-complex-numbers-and-polar-form.xml](../../source\chapters\ch14-parametric-curves-polar-coordinates-and-conics\sections\sec-14-8-complex-numbers-and-polar-form.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> This is a bridge, not a new requirement for the rest of the chapter. But it shows where the story is going.

**After**

This optional connection will be developed later using infinite series.

## 271. Sequences

Source: [source\chapters\ch15-sequences-and-infinite-series\sections\sec-15-1-sequences.xml](../../source\chapters\ch15-sequences-and-infinite-series\sections\sec-15-1-sequences.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> There is a next term, but there is no in-between input. The story is about a list, not about filling an interval.

**After**

The domain contains integer indices, with no required values between consecutive indices.

## 272. Sequences

Source: [source\chapters\ch15-sequences-and-infinite-series\sections\sec-15-1-sequences.xml](../../source\chapters\ch15-sequences-and-infinite-series\sections\sec-15-1-sequences.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> Convergence is a promise about every required closeness, not a snapshot of a few terms. Persistent oscillation between separated values and unbounded growth prevent convergence; oscillation with shrinking amplitude can still converge.

**After**

Convergence requires every sufficiently late term to meet each prescribed tolerance. Persistent separated oscillations and unbounded growth prevent convergence, but oscillations of shrinking amplitude may converge.

## 273. Infinite series

Source: [source\chapters\ch15-sequences-and-infinite-series\sections\sec-15-2-infinite-series.xml](../../source\chapters\ch15-sequences-and-infinite-series\sections\sec-15-2-infinite-series.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> The first examples were friendly because we could find exact formulas for the partial sums.

**After**

The preceding examples have explicit formulas for their partial sums.

## 274. Infinite series

Source: [source\chapters\ch15-sequences-and-infinite-series\sections\sec-15-2-infinite-series.xml](../../source\chapters\ch15-sequences-and-infinite-series\sections\sec-15-2-infinite-series.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> Most series will not be so generous. We will not usually have a simple formula for S_n. Instead, we will need tests that decide whether the partial sums converge without computing them exactly.

**After**

For many series there is no useful explicit formula for S_n. Convergence tests determine whether the partial sums converge without such a formula.

## 275. Infinite series

Source: [source\chapters\ch15-sequences-and-infinite-series\sections\sec-15-2-infinite-series.xml](../../source\chapters\ch15-sequences-and-infinite-series\sections\sec-15-2-infinite-series.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> Its terms approach 0. The surprise is that the sum still diverges.

**After**

Its terms tend to zero, but its partial sums grow without bound.

## 276. Infinite series

Source: [source\chapters\ch15-sequences-and-infinite-series\sections\sec-15-2-infinite-series.xml](../../source\chapters\ch15-sequences-and-infinite-series\sections\sec-15-2-infinite-series.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> Geometric and telescoping series are unusually generous: their partial sums simplify. A test is a way to decide whether the running totals settle without writing them in closed form.

**After**

Geometric and telescoping partial sums simplify explicitly. For other series, a convergence test may be needed instead.

## 277. The harmonic series and first warnings

Source: [source\chapters\ch15-sequences-and-infinite-series\sections\sec-15-3-the-harmonic-series-and-first-warnings.xml](../../source\chapters\ch15-sequences-and-infinite-series\sections\sec-15-3-the-harmonic-series-and-first-warnings.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> The surprise is that there is no ceiling.

**After**

The partial sums are unbounded.

## 278. Positive series tests

Source: [source\chapters\ch15-sequences-and-infinite-series\sections\sec-15-4-positive-series-tests.xml](../../source\chapters\ch15-sequences-and-infinite-series\sections\sec-15-4-positive-series-tests.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> The first ten terms alone do not give many correct decimal places, but the estimate is honest. It tells us exactly how uncertain we are.

**After**

The first ten terms give limited decimal accuracy, but the remainder estimate specifies an interval containing the true sum.

## 279. Positive series tests

Source: [source\chapters\ch15-sequences-and-infinite-series\sections\sec-15-4-positive-series-tests.xml](../../source\chapters\ch15-sequences-and-infinite-series\sections\sec-15-4-positive-series-tests.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> For nonnegative terms, boundedness of partial sums is the whole story. A smaller series cannot outrun a convergent ceiling, and a finite positive ratio means the two tails are comparable in both directions.

**After**

For nonnegative terms, convergence is equivalent to bounded partial sums. Comparison establishes boundedness, and a finite positive limit ratio makes the two positive tails comparable in both directions.

## 280. Positive series tests

Source: [source\chapters\ch15-sequences-and-infinite-series\sections\sec-15-4-positive-series-tests.xml](../../source\chapters\ch15-sequences-and-infinite-series\sections\sec-15-4-positive-series-tests.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> The positive version diverges. The alternating version behaves differently because cancellation becomes organized. That is the next story.

**After**

The positive series diverges. The next section shows how alternating signs change its convergence behavior.

## 281. Alternating series

Source: [source\chapters\ch15-sequences-and-infinite-series\sections\sec-15-5-alternating-series.xml](../../source\chapters\ch15-sequences-and-infinite-series\sections\sec-15-5-alternating-series.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> This is honest, but not fast. Alternating convergence can be slow when the term sizes decrease slowly.

**After**

This is a valid remainder bound, but it decreases slowly. Alternating convergence may require many terms for a small error.

## 282. Absolute convergence and stronger tests

Source: [source\chapters\ch15-sequences-and-infinite-series\sections\sec-15-6-absolute-convergence-and-stronger-tests.xml](../../source\chapters\ch15-sequences-and-infinite-series\sections\sec-15-6-absolute-convergence-and-stronger-tests.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> That is how the promise from the start of this chapter becomes possible. A function such as

**After**

These convergence results will allow us to represent functions by series. For example,

## 283. Chapter review and discovery problems

Source: [source\chapters\ch15-sequences-and-infinite-series\sections\sec-15-9-chapter-review-and-discovery-problems.xml](../../source\chapters\ch15-sequences-and-infinite-series\sections\sec-15-9-chapter-review-and-discovery-problems.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> A series often tells us which test it wants. The first step is to look at the shape of the term.

**After**

The form of a term helps determine an appropriate series test. Identify powers, factorials, ratios, or sign patterns before choosing the test.

## 284. Chapter review and discovery problems

Source: [source\chapters\ch15-sequences-and-infinite-series\sections\sec-15-9-chapter-review-and-discovery-problems.xml](../../source\chapters\ch15-sequences-and-infinite-series\sections\sec-15-9-chapter-review-and-discovery-problems.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> This is an honest interval for the true sum.

**After**

This interval contains the true sum by the remainder bound.

## 285. Chapter review and discovery problems

Source: [source\chapters\ch15-sequences-and-infinite-series\sections\sec-15-9-chapter-review-and-discovery-problems.xml](../../source\chapters\ch15-sequences-and-infinite-series\sections\sec-15-9-chapter-review-and-discovery-problems.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> This changes the story. We will ask:

**After**

When terms depend on x, additional questions arise:

## 286. Power series

Source: [source\chapters\ch16-power-series-taylor-polynomials-and-taylor-series\sections\sec-16-1-power-series.xml](../../source\chapters\ch16-power-series-taylor-polynomials-and-taylor-series\sections\sec-16-1-power-series.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> A power series centered at a is built from powers of x-a. In your own words, why is the center always a point of convergence, and why is distance from that center the quantity that controls the rest of the story?

**After**

Explain why a power series centered at a converges at a and how |x-a| enters the ratio or root analysis.

## 287. Power series

Source: [source\chapters\ch16-power-series-taylor-polynomials-and-taylor-series\sections\sec-16-1-power-series.xml](../../source\chapters\ch16-power-series-taylor-polynomials-and-taylor-series\sections\sec-16-1-power-series.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> The radius decides the open interval of guaranteed absolute convergence. The two endpoints are another story. In your own words, why can two series share a radius but have different intervals of convergence, and what extra work do the endpoints require?

**After**

The radius determines the open interval of absolute convergence. Explain why the two endpoints must be tested separately and how equal radii can give different convergence intervals.

## 288. Chapter review and projects

Source: [source\chapters\ch16-power-series-taylor-polynomials-and-taylor-series\sections\sec-16-10-chapter-review-and-projects.xml](../../source\chapters\ch16-power-series-taylor-polynomials-and-taylor-series\sections\sec-16-10-chapter-review-and-projects.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> A calculator does not know \sin x by magic. Somewhere underneath, it uses identities, approximations, and error control.

**After**

Calculators evaluate \sin x using numerical algorithms, identities, approximations, and error control.

## 289. Chapter review and projects

Source: [source\chapters\ch16-power-series-taylor-polynomials-and-taylor-series\sections\sec-16-10-chapter-review-and-projects.xml](../../source\chapters\ch16-power-series-taylor-polynomials-and-taylor-series\sections\sec-16-10-chapter-review-and-projects.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> The chapter began with a promise from the end of the previous chapter:

**After**

The earlier discussion of polar form introduced the identity

## 290. Working with power series

Source: [source\chapters\ch16-power-series-taylor-polynomials-and-taylor-series\sections\sec-16-2-working-with-power-series.xml](../../source\chapters\ch16-power-series-taylor-polynomials-and-taylor-series\sections\sec-16-2-working-with-power-series.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> Inside a common region of absolute convergence, power series with the same center may be added coefficient by coefficient. In your own words, why is that safe there, and why is the common interior the guaranteed region rather than a promise about endpoints?

**After**

Power series with the same center can be added coefficient by coefficient on a common interval of absolute convergence. Explain why this does not automatically justify endpoint operations.

## 291. Working with power series

Source: [source\chapters\ch16-power-series-taylor-polynomials-and-taylor-series\sections\sec-16-2-working-with-power-series.xml](../../source\chapters\ch16-power-series-taylor-polynomials-and-taylor-series\sections\sec-16-2-working-with-power-series.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> The definite-integral version fits the accumulation story. Each term

**After**

For term-by-term definite integration, each term

## 292. Working with power series

Source: [source\chapters\ch16-power-series-taylor-polynomials-and-taylor-series\sections\sec-16-2-working-with-power-series.xml](../../source\chapters\ch16-power-series-taylor-polynomials-and-taylor-series\sections\sec-16-2-working-with-power-series.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> The next step is to feed familiar functions into that machine. The geometric series will be the seed. From it, we will build series for logarithms, inverse tangents, and soon the functions that explain the mysterious formula

**After**

Next we derive series representations from the geometric series by substitution, differentiation, and integration. These methods produce logarithm and inverse-tangent series and help justify the identity

## 293. Representing functions by power series

Source: [source\chapters\ch16-power-series-taylor-polynomials-and-taylor-series\sections\sec-16-3-representing-functions-by-power-series.xml](../../source\chapters\ch16-power-series-taylor-polynomials-and-taylor-series\sections\sec-16-3-representing-functions-by-power-series.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> This is one of the famous surprises of power series: a series built from odd reciprocals knows the number \pi.

**After**

At the justified endpoint, this inverse-tangent series gives the displayed representation of \pi.

## 294. Taylor polynomials

Source: [source\chapters\ch16-power-series-taylor-polynomials-and-taylor-series\sections\sec-16-4-taylor-polynomials.xml](../../source\chapters\ch16-power-series-taylor-polynomials-and-taylor-series\sections\sec-16-4-taylor-polynomials.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> The factorials are not mysterious. They come from differentiating powers:

**After**

The factorial coefficients follow from repeated differentiation of powers:

## 295. Taylor polynomials

Source: [source\chapters\ch16-power-series-taylor-polynomials-and-taylor-series\sections\sec-16-4-taylor-polynomials.xml](../../source\chapters\ch16-power-series-taylor-polynomials-and-taylor-series\sections\sec-16-4-taylor-polynomials.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> is good near 0. It is not automatically good far away. Taylor polynomials are promises about contact at a point, not yet promises about accuracy on a whole interval.

**After**

approximates the function near zero under the relevant remainder estimate. Matching derivatives at one point alone gives no accuracy bound far from that point.

## 296. Taylor’s theorem and remainders

Source: [source\chapters\ch16-power-series-taylor-polynomials-and-taylor-series\sections\sec-16-5-taylor-s-theorem-and-remainders.xml](../../source\chapters\ch16-power-series-taylor-polynomials-and-taylor-series\sections\sec-16-5-taylor-s-theorem-and-remainders.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> This form is optional for computation, but important for the story. Taylor’s theorem is not magic. The error is an accumulated effect of higher derivatives.

**After**

The integral remainder expresses the error as an integral involving a higher derivative. It provides another way to estimate that error.

## 297. Applications of Taylor series

Source: [source\chapters\ch16-power-series-taylor-polynomials-and-taylor-series\sections\sec-16-7-applications-of-taylor-series.xml](../../source\chapters\ch16-power-series-taylor-polynomials-and-taylor-series\sections\sec-16-7-applications-of-taylor-series.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> A limit that pits two functions against each other often asks which derivative first distinguishes them. In your own words, why do you keep Taylor terms until the first surviving term after cancellation, and why is that still the derivative story in disguise?

**After**

When Taylor expansions cancel in a limit, retain enough terms to identify the first nonzero difference and control the remainder. Explain how the first differing derivative determines that leading term.

## 298. Applications of Taylor series

Source: [source\chapters\ch16-power-series-taylor-polynomials-and-taylor-series\sections\sec-16-7-applications-of-taylor-series.xml](../../source\chapters\ch16-power-series-taylor-polynomials-and-taylor-series\sections\sec-16-7-applications-of-taylor-series.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> This method is not separate from the derivative story. Taylor series are built from derivatives. A limit that asks about cancellation is often asking which derivative first distinguishes two functions.

**After**

Taylor coefficients are derivatives at the expansion point. After cancellation, the first differing coefficient often determines the leading behavior in the limit.

## 299. Applications of Taylor series

Source: [source\chapters\ch16-power-series-taylor-polynomials-and-taylor-series\sections\sec-16-7-applications-of-taylor-series.xml](../../source\chapters\ch16-power-series-taylor-polynomials-and-taylor-series\sections\sec-16-7-applications-of-taylor-series.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> Polynomials are easy to integrate. The series is justified on an interval inside the radius, so the integrated tail is a boundable error rather than an unknown mystery.

**After**

Uniform convergence on the integration interval justifies term-by-term integration. A bound on the remaining series then bounds the integral error.

## 300. Warning examples

Source: [source\chapters\ch16-power-series-taylor-polynomials-and-taylor-series\sections\sec-16-9-warning-examples.xml](../../source\chapters\ch16-power-series-taylor-polynomials-and-taylor-series\sections\sec-16-9-warning-examples.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> These warnings complete the chapter’s main lesson. Infinite polynomials are useful because they come with a domain, a remainder, and a convergence story. Without those three pieces, the formulas are only formal patterns.

**After**

A power-series calculation needs a specified domain, convergence justification, and an applicable remainder estimate. Without these, formal manipulations may not establish an identity or an accurate approximation.

## 301. Fourier series preview

Source: [source\chapters\ch17-complex-numbers-fourier-ideas-and-the-road-ahead\sections\sec-17-3-fourier-series-preview.xml](../../source\chapters\ch17-complex-numbers-fourier-ideas-and-the-road-ahead\sections\sec-17-3-fourier-series-preview.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> is being used carefully. It means “has Fourier series.” It does not automatically mean that the series converges everywhere to f(t). Convergence is part of the deeper theory.

**After**

means that the displayed series has the Fourier coefficients of f. It does not by itself establish convergence to f(t) at every point. That requires a separate convergence theorem.

## 302. Fourier series preview

Source: [source\chapters\ch17-complex-numbers-fourier-ideas-and-the-road-ahead\sections\sec-17-3-fourier-series-preview.xml](../../source\chapters\ch17-complex-numbers-fourier-ideas-and-the-road-ahead\sections\sec-17-3-fourier-series-preview.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> A repeating shape asks which frequencies are present, not how the function looks near one point. Convergence of the wave series is a separate, deeper issue, especially at jumps.

**After**

Fourier coefficients describe frequency components rather than derivatives at a point. Convergence of the resulting series requires separate conditions, particularly at discontinuities.

## 303. The one-dimensional Stokes theorem

Source: [source\chapters\ch17-complex-numbers-fourier-ideas-and-the-road-ahead\sections\sec-17-4-the-one-dimensional-stokes-theorem.xml](../../source\chapters\ch17-complex-numbers-fourier-ideas-and-the-road-ahead\sections\sec-17-4-the-one-dimensional-stokes-theorem.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> \text{The Fundamental Theorem applies to honest derivatives, not to hidden jumps.}

**After**

\int_a^b F\prime=F(b)-F(a) requires the theorem's differentiability and integrability conditions. A jump in F is not included in an ordinary derivative integral.

## 304. The one-dimensional Stokes theorem

Source: [source\chapters\ch17-complex-numbers-fourier-ideas-and-the-road-ahead\sections\sec-17-4-the-one-dimensional-stokes-theorem.xml](../../source\chapters\ch17-complex-numbers-fourier-ideas-and-the-road-ahead\sections\sec-17-4-the-one-dimensional-stokes-theorem.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> An integrand of the form dF=F'(x)\,dx is exact, and its integral depends only on the boundary. In your own words, why is finding an antiderivative the same as recognizing an exact differential, and why does that make interior cancellations the whole story?

**After**

An exact differential has the form dF=F\prime(x)\,dx. Explain why its integral reduces to a signed endpoint difference and how finding an antiderivative identifies such a differential.

## 305. Conservation laws in one dimension

Source: [source\chapters\ch17-complex-numbers-fourier-ideas-and-the-road-ahead\sections\sec-17-5-conservation-laws-in-one-dimension.xml](../../source\chapters\ch17-complex-numbers-fourier-ideas-and-the-road-ahead\sections\sec-17-5-conservation-laws-in-one-dimension.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> This is why the boundary viewpoint matters. The Fundamental Theorem, flux through endpoints, conservation laws, and divergence are not separate tricks. They are stages of one story:

**After**

The Fundamental Theorem converts an integral of a derivative into endpoint values. Applied to a flux, this expresses the net boundary flow used in a conservation law:

## 306. Least action and the shape of a path

Source: [source\chapters\ch17-complex-numbers-fourier-ideas-and-the-road-ahead\sections\sec-17-6-least-action-and-the-shape-of-a-path.xml](../../source\chapters\ch17-complex-numbers-fourier-ideas-and-the-road-ahead\sections\sec-17-6-least-action-and-the-shape-of-a-path.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> The Euler--Lagrange equation is a cousin of f'(c)=0, but the unknown is a function. In your own words, why is that beyond ordinary single-variable optimization, and how does the action integral turn a particle’s kinetic-minus-potential story into a path problem?

**After**

The Euler–Lagrange equation is a stationarity condition for a functional whose input is a path. Explain how integrating kinetic minus potential energy defines the action and why this optimization differs from varying a single real number.

## 307. Final projects

Source: [source\chapters\ch17-complex-numbers-fourier-ideas-and-the-road-ahead\sections\sec-17-7-final-projects.xml](../../source\chapters\ch17-complex-numbers-fourier-ideas-and-the-road-ahead\sections\sec-17-7-final-projects.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> The cooling project asks you to solve Newton’s law, estimate a constant from data, and then check whether the model deserves trust. In your own words, why is solving a differential equation not the end of the scientific story, and what does a mismatch with data force you to admit?

**After**

The cooling project asks for a solution, a parameter estimate, and a comparison with data. Explain why solving the equation does not establish the model's accuracy and how mismatches should affect its assumptions.

## 308. Final projects

Source: [source\chapters\ch17-complex-numbers-fourier-ideas-and-the-road-ahead\sections\sec-17-7-final-projects.xml](../../source\chapters\ch17-complex-numbers-fourier-ideas-and-the-road-ahead\sections\sec-17-7-final-projects.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> More digits are not a guarantee. An error bound turns a computation into a promise, which is the same remainder idea that made Taylor series into algorithms.

**After**

Additional computed digits do not establish accuracy. An applicable error bound quantifies the possible difference from the exact value.

## 309. Final projects

Source: [source\chapters\ch17-complex-numbers-fourier-ideas-and-the-road-ahead\sections\sec-17-7-final-projects.xml](../../source\chapters\ch17-complex-numbers-fourier-ideas-and-the-road-ahead\sections\sec-17-7-final-projects.xml)

Flag: Replace figurative or imprecise prose with the mathematical statement or question.

**Before**

> A calculator must be fast, but it must also be honest.

**After**

A numerical implementation needs both efficient evaluation and documented accuracy.

## 310. Graphing windows

Source: [source\appendices\appE-technology-notes\sections\sec-e-1-graphing-windows.xml](../../source\appendices\appE-technology-notes\sections\sec-e-1-graphing-windows.xml)

Flag: Align captions, descriptions, and questions with direct language.

**Before**

> The same function can tell a different visual story in different windows.

**After**

The viewing window can reveal or conceal features of the same function.

## 311. Discovery problems and projects

Source: [source\chapters\ch01-velocity-distance-and-the-first-shape-of-calculus\sections\sec-1-7-discovery-problems-and-projects.xml](../../source\chapters\ch01-velocity-distance-and-the-first-shape-of-calculus\sections\sec-1-7-discovery-problems-and-projects.xml)

Flag: Align captions, descriptions, and questions with direct language.

**Before**

> Signed area preserves the net change, not the full story.

**After**

Signed area gives the net change but does not determine the velocity at each time.

## 312. Two theorems about continuous functions

Source: [source\chapters\ch03-limits-and-continuity\sections\sec-3-6-two-theorems-about-continuous-functions.xml](../../source\chapters\ch03-limits-and-continuity\sections\sec-3-6-two-theorems-about-continuous-functions.xml)

Flag: Align captions, descriptions, and questions with direct language.

**Before**

> even when the picture still looks calm

**After**

even when a sampled graph appears to attain extrema

## 313. Algebra and Inequalities Review

Source: [source\appendices\appA-algebra-and-inequalities-review\appA-algebra-and-inequalities-review.ptx](../../source\appendices\appA-algebra-and-inequalities-review\appA-algebra-and-inequalities-review.ptx)

Flag: Replace appendix-opening filler or unsupported generalizations with scope and conditions.

**Before**

> Calculus often fails in the algebra, not in the calculus. A limit may look impossible until a factor cancels. An integral may look unfamiliar until a square is completed. A derivative formula may be easier to read after radicals are rewritten as powers. A theorem may ask for an interval, and the interval may come from solving an inequality carefully. This appendix collects the algebra that appears again and again in the book. It is not meant to replace a full algebra course. It is a repair bench. When a calculation in the main text gets stuck, the tool you need is often here.

**After**

This appendix reviews factoring, completing the square, rational expressions, powers, inequalities, and finite sums. These algebraic tools are used to simplify calculus expressions, determine domains, and prove error bounds.

## 314. Factoring and completing the square

Source: [source\appendices\appA-algebra-and-inequalities-review\sections\sec-a-1-factoring-and-completing-the-square.xml](../../source\appendices\appA-algebra-and-inequalities-review\sections\sec-a-1-factoring-and-completing-the-square.xml)

Flag: Replace appendix-opening filler or unsupported generalizations with scope and conditions.

**Before**

> Factoring turns addition into multiplication. That is why it is so useful in calculus. Multiplication can cancel. Multiplication has signs we can track. Multiplication reveals zeros.

**After**

Factoring expresses a polynomial as a product. It reveals zeros and signs and can expose common factors for cancellation. Completing the square gives a form useful for recognizing graphs and evaluating integrals.

## 315. Exponents and radicals

Source: [source\appendices\appA-algebra-and-inequalities-review\sections\sec-a-3-exponents-and-radicals.xml](../../source\appendices\appA-algebra-and-inequalities-review\sections\sec-a-3-exponents-and-radicals.xml)

Flag: Replace appendix-opening filler or unsupported generalizations with scope and conditions.

**Before**

> Powers are the native language of many calculus formulas. Radicals, roots, and reciprocals are often easier to differentiate or integrate after they are rewritten as powers.

**After**

Rewriting roots and reciprocals as powers can simplify differentiation and integration. The exponent laws must be used on domains where the expressions are defined.

## 316. Inequalities and absolute values

Source: [source\appendices\appA-algebra-and-inequalities-review\sections\sec-a-4-inequalities-and-absolute-values.xml](../../source\appendices\appA-algebra-and-inequalities-review\sections\sec-a-4-inequalities-and-absolute-values.xml)

Flag: Replace appendix-opening filler or unsupported generalizations with scope and conditions.

**Before**

> Calculus uses inequalities to control error. A limit proof says: make the input error small enough so that the output error is below a chosen bound. An approximation theorem says: the remainder is no larger than a certain expression. A convergence test says: compare one quantity with another. So inequalities are not only algebraic chores. They are the grammar of control.

**After**

Inequalities compare quantities and bound errors. Absolute values measure distances and unsigned magnitudes. This section reviews the rules used in limit proofs, approximation bounds, and convergence comparisons.

## 317. Coordinate Geometry

Source: [source\appendices\appB-coordinate-geometry\appB-coordinate-geometry.ptx](../../source\appendices\appB-coordinate-geometry\appB-coordinate-geometry.ptx)

Flag: Replace appendix-opening filler or unsupported generalizations with scope and conditions.

**Before**

> Calculus draws many pictures: tangent lines, areas between curves, solids of revolution, phase lines, parametric paths, and polar curves. But a picture becomes usable only when we can attach coordinates to it. Coordinate geometry is the bridge. \text{geometry} \quad\longleftrightarrow\quad \text{algebra}. A line becomes an equation. A circle becomes a distance condition. A parabola becomes a squared expression. Shifting a graph becomes replacing x by x-h or y by y-k. This appendix reviews the coordinate geometry used throughout the book. The goal is not to memorize many separate forms. The goal is to recognize what an equation is telling the picture to do.

**After**

Coordinate geometry expresses shapes using equations. This appendix reviews lines, circles, conics, distances, midpoints, and graph transformations, including the forms used for tangents and integral boundaries.

## 318. Lines

Source: [source\appendices\appB-coordinate-geometry\sections\sec-b-1-lines.xml](../../source\appendices\appB-coordinate-geometry\sections\sec-b-1-lines.xml)

Flag: Replace appendix-opening filler or unsupported generalizations with scope and conditions.

**Before**

> The first graph in calculus is often a line. Constant velocity gives a line. A tangent approximation gives a line. Newton’s method follows a line. The Mean Value Theorem compares a tangent slope with a secant slope. So lines deserve to be completely familiar.

**After**

A line is determined by two distinct points or by a point and a slope. Line equations are used for secants, tangents, linear approximations, and Newton steps.

## 319. Trigonometry in Radians

Source: [source\appendices\appC-trigonometry-in-radians\appC-trigonometry-in-radians.ptx](../../source\appendices\appC-trigonometry-in-radians\appC-trigonometry-in-radians.ptx)

Flag: Replace appendix-opening filler or unsupported generalizations with scope and conditions.

**Before**

> Trigonometry enters calculus whenever something turns, repeats, or oscillates. A wheel rotates. A spring vibrates. A wave rises and falls. A planet travels around a focus. A point on the unit circle moves with coordinates (\cos t,\sin t). That is why sine and cosine appear in derivatives, integrals, differential equations, parametric curves, polar coordinates, complex numbers, and Fourier series. This appendix reviews the trigonometry used in the book. The main point is not to memorize a long list of identities. The main point is to know where the identities come from: the unit circle, right triangles, and the Pythagorean Theorem. One habit matters more than all the others: In calculus, angles are measured in radians unless degrees are explicitly stated. Radians make the formulas of calculus clean.

**After**

This appendix reviews the unit-circle definitions, identities, addition formulas, inverse functions, and equations used in calculus. Angles are measured in radians unless degrees are explicitly stated. The derivative formulas for sine and cosine depend on that convention.

## 320. Proofs and Completeness

Source: [source\appendices\appD-proofs-and-completeness\appD-proofs-and-completeness.ptx](../../source\appendices\appD-proofs-and-completeness\appD-proofs-and-completeness.ptx)

Flag: Replace appendix-opening filler or unsupported generalizations with scope and conditions.

**Before**

> Existence theorems justify limits, extrema, roots, and integrals under stated conditions. Their proofs depend on completeness of the real numbers. \text{the limiting objects we are chasing really exist.} A tangent slope is approached by secant slopes. An integral is approached by Riemann sums. A root is trapped by bisection. A maximum value may be approached by better and better input choices. All of those processes need a number line with no holes. This appendix develops the proof arguments behind those results, including the roles of continuity, completeness, and closed intervals.

**After**

Completeness of the real numbers supports the existence results used throughout calculus. This appendix develops the least-upper-bound property, monotone convergence, bisection, extrema, and uniform continuity. The main-text Cauchy criterion in [cross-reference] gives another formulation of completeness.

## 321. The Least Upper Bound Property

Source: [source\appendices\appD-proofs-and-completeness\sections\sec-d-1-least-upper-bound-property.xml](../../source\appendices\appD-proofs-and-completeness\sections\sec-d-1-least-upper-bound-property.xml)

Flag: Replace appendix-opening filler or unsupported generalizations with scope and conditions.

**Before**

> The real line is more than a long list of numbers. It has no gaps. That phrase sounds geometric, but it becomes useful only after we translate it into a precise statement about sets of numbers.

**After**

The least-upper-bound property states completeness in terms of bounded sets of real numbers. Every nonempty set bounded above has a smallest real upper bound. We will use that property to justify limiting values.

## 322. The Monotone Convergence Theorem

Source: [source\appendices\appD-proofs-and-completeness\sections\sec-d-2-monotone-convergence-theorem.xml](../../source\appendices\appD-proofs-and-completeness\sections\sec-d-2-monotone-convergence-theorem.xml)

Flag: Replace appendix-opening filler or unsupported generalizations with scope and conditions.

**Before**

> A sequence may wander forever. But if it moves only in one direction and cannot escape past a bound, then it must settle down. That statement is the Monotone Convergence Theorem. It is one of the first places where completeness does visible work.

**After**

An increasing sequence bounded above converges to the supremum of its terms. A decreasing sequence bounded below converges to their infimum. This section proves both statements from the least-upper-bound property.

## 323. The Extreme Value Theorem: Proof Outline

Source: [source\appendices\appD-proofs-and-completeness\sections\sec-d-4-extreme-value-theorem-proof-outline.xml](../../source\appendices\appD-proofs-and-completeness\sections\sec-d-4-extreme-value-theorem-proof-outline.xml)

Flag: Replace appendix-opening filler or unsupported generalizations with scope and conditions.

**Before**

> The Extreme Value Theorem says that a continuous function on a closed and bounded interval reaches its highest and lowest values. The theorem sounds visually obvious. But each word is doing work. continuous on a closed bounded interval \Longrightarrow absolute max and min are attained. This section explains why completeness is hiding behind that statement.

**After**

A continuous function on a closed, bounded interval attains its maximum and minimum. This section outlines a proof using completeness and the interval conditions.

## 324. Technology Notes

Source: [source\appendices\appE-technology-notes\appE-technology-notes.ptx](../../source\appendices\appE-technology-notes\appE-technology-notes.ptx)

Flag: Replace appendix-opening filler or unsupported generalizations with scope and conditions.

**Before**

> Calculus is older than computers, but modern calculus practice is full of screens: graphing calculators, spreadsheets, computer algebra systems, numerical solvers, and short programs. These tools are useful because calculus is full of processes: zoom in on a graph, iterate Newton's method, add a Riemann sum, plot partial sums, compare Taylor polynomials. A computer can do thousands of arithmetic steps before a person finishes writing the first line. That speed is powerful. It also creates a new responsibility. \text{Technology should extend mathematical judgment, not replace it.} This appendix gives practical notes for using technology in this book. The examples use generic calculator language and simple Python code. The exact syntax of a particular device or app may differ, but the mathematical habits are the same.

**After**

This appendix explains graphing windows, finite precision, calculator syntax, and Python experiments. Use reference values and mathematical error estimates to check numerical results, and account for the sampling limitations of plots.

## 325. Calculator and CAS syntax

Source: [source\appendices\appE-technology-notes\sections\sec-e-3-calculator-and-cas-syntax.xml](../../source\appendices\appE-technology-notes\sections\sec-e-3-calculator-and-cas-syntax.xml)

Flag: Replace appendix-opening filler or unsupported generalizations with scope and conditions.

**Before**

> A calculator or computer algebra system must parse what you type. It does not read mathematical intention. Parentheses, multiplication signs, and mode settings matter. \text{Most technology errors in calculus are syntax errors or interpretation errors.}

**After**

Calculator and computer-algebra inputs require explicit syntax. Parentheses, multiplication signs, and angle settings affect how an expression is evaluated. Check the interpretation of the input as well as the returned value.

## 326. Simple Python experiments for calculus

Source: [source\appendices\appE-technology-notes\sections\sec-e-4-simple-python-experiments-for-calculus.xml](../../source\appendices\appE-technology-notes\sections\sec-e-4-simple-python-experiments-for-calculus.xml)

Flag: Replace appendix-opening filler or unsupported generalizations with scope and conditions.

**Before**

> A short program can make a calculus idea visible. The goal is not to turn this book into a programming course. The goal is to give a few readable experiments that show what the mathematics is doing. The examples below use plain Python. Some use the built-in math module. Plotting examples appear in the next section.

**After**

These short Python examples implement numerical calculations from the book. Some use the built-in math module. Check their results against the known formulas and error estimates; plotting examples appear in the next section.

## 327. Tables

Source: [source\appendices\appF-tables\appF-tables.ptx](../../source\appendices\appF-tables\appF-tables.ptx)

Flag: Replace appendix-opening filler or unsupported generalizations with scope and conditions.

**Before**

> A table is a map. It is not the trip. The formulas in this appendix are meant for quick reference after the ideas have been learned. Before using a formula, ask three questions. \text{What does the formula mean?} \text{What hypotheses does it require?} \text{Does the answer make sense in this problem?} A derivative formula should agree with the idea of local rate of change. An integral formula should agree with accumulated signed amount. A series test should be used only when its hypotheses are satisfied. A numerical rule should come with an error estimate when accuracy matters. Unless degrees are explicitly mentioned, all trigonometric formulas in calculus use radians.

**After**

These tables provide quick reference to formulas and tests developed in the text. Check the domain and hypotheses before using a formula, and include an applicable error bound or qualified estimate when reporting numerical accuracy. Trigonometric arguments are in radians unless stated otherwise.

## 328. Common Taylor series

Source: [source\appendices\appF-tables\sections\sec-f-3-common-taylor-series.xml](../../source\appendices\appF-tables\sections\sec-f-3-common-taylor-series.xml)

Flag: Replace appendix-opening filler or unsupported generalizations with scope and conditions.

**Before**

> Taylor polynomials approximate functions near a chosen center. Taylor series continue that approximation indefinitely.

**After**

The following series represent their functions on the stated domains. Constructing Taylor coefficients alone does not prove representation; the Taylor remainder must tend to zero.

## 329. Computer algebra systems and integral tables

Source: [source\chapters\ch11-techniques-of-integration\sections\sec-11-6-computer-algebra-systems-and-integral-tables.xml](../../source\chapters\ch11-techniques-of-integration\sections\sec-11-6-computer-algebra-systems-and-integral-tables.xml)

Flag: Replace personification in a substitution explanation.

**Before**

> But the numerator is dx, while the table formula wants du.

**After**

The numerator uses dx, whereas the table formula requires du.

## 330. Warning examples

Source: [source\chapters\ch03-limits-and-continuity\sections\sec-3-7-warning-examples.xml](../../source\chapters\ch03-limits-and-continuity\sections\sec-3-7-warning-examples.xml)

Flag: Make the warning heading identify the precise failure.

**Before**

> A function with no limit at a jump

**After**

Jump discontinuity: unequal one-sided limits

## 331. Additional topics: Runge–Kutta methods

Source: [source\chapters\ch13-differential-equations-laws-written-as-derivatives\sections\sec-additional-runge-kutta.xml](../../source\chapters\ch13-differential-equations-laws-written-as-derivatives\sections\sec-additional-runge-kutta.xml)

Flag: Define the Lipschitz condition at its first use in the optional numerical section.

**Before**

> and F is Lipschitz in y there.

**After**

and one constant L\ge0 satisfies |F(t,u)-F(t,v)|\le L|u-v| there. This is the Lipschitz condition in the dependent variable.

## 332. Additional topics: Runge–Kutta methods

Source: [source\chapters\ch13-differential-equations-laws-written-as-derivatives\sections\sec-additional-runge-kutta.xml](../../source\chapters\ch13-differential-equations-laws-written-as-derivatives\sections\sec-additional-runge-kutta.xml)

Flag: Define order notation locally so this optional section does not require another optional section.

**Before**

> Some texts divide the local error by h; here we do not.

**After**

Here O(h^r) means a magnitude bounded by a constant times h^r for all sufficiently small positive h, with the constant independent of the step size. Some texts divide the local error by h; here we do not.

## 333. Additional topics: local existence and uniqueness

Source: [source\chapters\ch17-complex-numbers-fourier-ideas-and-the-road-ahead\sections\sec-additional-local-existence-uniqueness.xml](../../source\chapters\ch17-complex-numbers-fourier-ideas-and-the-road-ahead\sections\sec-additional-local-existence-uniqueness.xml)

Flag: Use the stated bound instead of relying on an unstated multivariable boundedness theorem.

**Before**

> Continuity on the closed rectangle supplies a finite bound M.

**After**

The stated bounds M and L determine a positive interval length.

## 334. Least action and the shape of a path

Source: [source\chapters\ch17-complex-numbers-fourier-ideas-and-the-road-ahead\sections\sec-17-6-least-action-and-the-shape-of-a-path.xml](../../source\chapters\ch17-complex-numbers-fourier-ideas-and-the-road-ahead\sections\sec-17-6-least-action-and-the-shape-of-a-path.xml)

Flag: Make the heading name the concept or question directly.

**Before**

> The brachistochrone story

**After**

The brachistochrone problem

## 335. Taylor polynomials

Source: [source\chapters\ch16-power-series-taylor-polynomials-and-taylor-series\sections\sec-16-4-taylor-polynomials.xml](../../source\chapters\ch16-power-series-taylor-polynomials-and-taylor-series\sections\sec-16-4-taylor-polynomials.xml)

Flag: Make the heading name the concept or question directly.

**Before**

> Why is a Taylor polynomial a local promise?

**After**

What does a Taylor polynomial match at its center?

## 336. Separable equations

Source: [source\chapters\ch13-differential-equations-laws-written-as-derivatives\sections\sec-13-4-separable-equations.xml](../../source\chapters\ch13-differential-equations-laws-written-as-derivatives\sections\sec-13-4-separable-equations.xml)

Flag: Make the heading name the concept or question directly.

**Before**

> Separation rule of honesty

**After**

Check equilibrium solutions before division

## 337. First-order linear equations

Source: [source\chapters\ch13-differential-equations-laws-written-as-derivatives\sections\sec-13-6-first-order-linear-equations.xml](../../source\chapters\ch13-differential-equations-laws-written-as-derivatives\sections\sec-13-6-first-order-linear-equations.xml)

Flag: Make the heading name the concept or question directly.

**Before**

> What story does the nonhomogeneous term q(t) tell?

**After**

What input does the term q(t) represent?

## 338. Second-order equations and vibration

Source: [source\chapters\ch13-differential-equations-laws-written-as-derivatives\sections\sec-13-7-second-order-equations-and-vibration.xml](../../source\chapters\ch13-differential-equations-laws-written-as-derivatives\sections\sec-13-7-second-order-equations-and-vibration.xml)

Flag: Make the heading name the concept or question directly.

**Before**

> What does damping change in the energy story?

**After**

How does damping change the energy?

## 339. Warning examples

Source: [source\chapters\ch13-differential-equations-laws-written-as-derivatives\sections\sec-13-9-warning-examples.xml](../../source\chapters\ch13-differential-equations-laws-written-as-derivatives\sections\sec-13-9-warning-examples.xml)

Flag: Make the heading name the concept or question directly.

**Before**

> Why can Euler’s method follow the wrong story?

**After**

Why can Euler’s method contradict the exact solution?

## 340. Computer algebra systems and integral tables

Source: [source\chapters\ch11-techniques-of-integration\sections\sec-11-6-computer-algebra-systems-and-integral-tables.xml](../../source\chapters\ch11-techniques-of-integration\sections\sec-11-6-computer-algebra-systems-and-integral-tables.xml)

Flag: Make the heading name the concept or question directly.

**Before**

> Why is differentiating the honest check of an antiderivative?

**After**

How does differentiation check an antiderivative?

## 341. Computer algebra systems and integral tables

Source: [source\chapters\ch11-techniques-of-integration\sections\sec-11-6-computer-algebra-systems-and-integral-tables.xml](../../source\chapters\ch11-techniques-of-integration\sections\sec-11-6-computer-algebra-systems-and-integral-tables.xml)

Flag: Make the heading name the concept or question directly.

**Before**

> A new function is sometimes the honest answer

**After**

Defining a function by an integral

## 342. Chapter review and discovery problems

Source: [source\chapters\ch11-techniques-of-integration\sections\sec-11-9-chapter-review-and-discovery-problems.xml](../../source\chapters\ch11-techniques-of-integration\sections\sec-11-9-chapter-review-and-discovery-problems.xml)

Flag: Make the heading name the concept or question directly.

**Before**

> Why is an exact antiderivative not the whole story?

**After**

When is numerical integration needed?

## 343. Chapter review and discovery problems

Source: [source\chapters\ch09-the-fundamental-theorem-of-calculus\sections\sec-9-7-chapter-review-and-discovery-problems.xml](../../source\chapters\ch09-the-fundamental-theorem-of-calculus\sections\sec-9-7-chapter-review-and-discovery-problems.xml)

Flag: Make the heading name the concept or question directly.

**Before**

> Why are the two parts of the Fundamental Theorem the same story?

**After**

How do the two parts of the Fundamental Theorem connect?

## 344. Logistic growth and limited resources

Source: [source\chapters\ch07-optimization-related-rates-and-models\sections\sec-7-6-logistic-growth-and-limited-resources.xml](../../source\chapters\ch07-optimization-related-rates-and-models\sections\sec-7-6-logistic-growth-and-limited-resources.xml)

Flag: Make the heading name the concept or question directly.

**Before**

> The logistic story

**After**

Interpreting the logistic model

## 345. Logistic growth and limited resources

Source: [source\chapters\ch07-optimization-related-rates-and-models\sections\sec-7-6-logistic-growth-and-limited-resources.xml](../../source\chapters\ch07-optimization-related-rates-and-models\sections\sec-7-6-logistic-growth-and-limited-resources.xml)

Flag: Make the heading name the concept or question directly.

**Before**

> A model is a promise with conditions

**After**

Check the model’s assumptions

## 346. Chapter review and applications

Source: [source\chapters\ch07-optimization-related-rates-and-models\sections\sec-7-9-chapter-review-and-applications.xml](../../source\chapters\ch07-optimization-related-rates-and-models\sections\sec-7-9-chapter-review-and-applications.xml)

Flag: Make the heading name the concept or question directly.

**Before**

> Why is a model a promise with conditions?

**After**

Why must a model’s assumptions be checked?

## 347. Differentiability and continuity

Source: [source\chapters\ch04-the-derivative\sections\sec-4-5-differentiability-and-continuity.xml](../../source\chapters\ch04-the-derivative\sections\sec-4-5-differentiability-and-continuity.xml)

Flag: Make the heading name the concept or question directly.

**Before**

> Why does continuity not promise a derivative?

**After**

Why does continuity not imply differentiability?

## 348. Differentiability and continuity

Source: [source\chapters\ch04-the-derivative\sections\sec-4-5-differentiability-and-continuity.xml](../../source\chapters\ch04-the-derivative\sections\sec-4-5-differentiability-and-continuity.xml)

Flag: Make the heading name the concept or question directly.

**Before**

> What continuity can and cannot promise

**After**

Continuity and differentiability

## 349. Two theorems about continuous functions

Source: [source\chapters\ch03-limits-and-continuity\sections\sec-3-6-two-theorems-about-continuous-functions.xml](../../source\chapters\ch03-limits-and-continuity\sections\sec-3-6-two-theorems-about-continuous-functions.xml)

Flag: Make the heading name the concept or question directly.

**Before**

> What does the Intermediate Value Theorem promise, and what does it refuse to compute?

**After**

What does the Intermediate Value Theorem establish?

## 350. Warning examples

Source: [source\chapters\ch03-limits-and-continuity\sections\sec-3-7-warning-examples.xml](../../source\chapters\ch03-limits-and-continuity\sections\sec-3-7-warning-examples.xml)

Flag: Make the heading name the concept or question directly.

**Before**

> Which Extreme Value Theorem hypotheses can quietly fail?

**After**

Which Extreme Value Theorem hypotheses fail in these examples?

## 351. The dashboard: speedometer and odometer

Source: [source\chapters\ch01-velocity-distance-and-the-first-shape-of-calculus\sections\sec-1-1-the-dashboard-speedometer-and-odometer.xml](../../source\chapters\ch01-velocity-distance-and-the-first-shape-of-calculus\sections\sec-1-1-the-dashboard-speedometer-and-odometer.xml)

Flag: Make the heading name the concept or question directly.

**Before**

> Units already tell the story

**After**

Units of velocity and distance

## 352. Discovery problems and projects

Source: [source\chapters\ch01-velocity-distance-and-the-first-shape-of-calculus\sections\sec-1-7-discovery-problems-and-projects.xml](../../source\chapters\ch01-velocity-distance-and-the-first-shape-of-calculus\sections\sec-1-7-discovery-problems-and-projects.xml)

Flag: Make the heading name the concept or question directly.

**Before**

> What promise is a limit making?

**After**

What accuracy does a limit assertion require?

## 353. General power rule and hyperbolic functions

Source: [source\chapters\ch05-differentiation-rules-and-elementary-functions\sections\sec-5-8-general-power-rule-and-hyperbolic-functions.xml](../../source\chapters\ch05-differentiation-rules-and-elementary-functions\sections\sec-5-8-general-power-rule-and-hyperbolic-functions.xml)

Flag: Replace the remaining figurative claim with the specific mathematical result or model condition.

**Before**

> So hyperbolic functions are not new mysteries. They are a useful way to package exponentials symmetrically.

**After**

Hyperbolic sine and cosine express the odd and even parts of the exponential function.

## 354. Fourier series preview

Source: [source\chapters\ch17-complex-numbers-fourier-ideas-and-the-road-ahead\sections\sec-17-3-fourier-series-preview.xml](../../source\chapters\ch17-complex-numbers-fourier-ideas-and-the-road-ahead\sections\sec-17-3-fourier-series-preview.xml)

Flag: Replace the remaining figurative claim with the specific mathematical result or model condition.

**Before**

> That is a new kind of honesty. Fourier series can represent discontinuous shapes, but they do not erase the discontinuity. The jump leaves a visible trace in the approximation.

**After**

The Fourier partial sums overshoot near a jump even as their values converge away from it. This behavior must be distinguished from pointwise convergence.

## 355. Fourier series preview

Source: [source\chapters\ch17-complex-numbers-fourier-ideas-and-the-road-ahead\sections\sec-17-3-fourier-series-preview.xml](../../source\chapters\ch17-complex-numbers-fourier-ideas-and-the-road-ahead\sections\sec-17-3-fourier-series-preview.xml)

Flag: Replace the remaining figurative claim with the specific mathematical result or model condition.

**Before**

> Fourier series can represent a square wave, but they overshoot near a jump and converge at the jump to the average of the two sides. In your own words, why is that a kind of honesty rather than a failure, and why can Fourier series handle discontinuities that Taylor series cannot?

**After**

For the square-wave example, Fourier partial sums overshoot near a jump and converge at the jump to the average of the two sides. Explain why this prevents uniform convergence and how it differs from Taylor representation.

## 356. Conservation laws in one dimension

Source: [source\chapters\ch17-complex-numbers-fourier-ideas-and-the-road-ahead\sections\sec-17-5-conservation-laws-in-one-dimension.xml](../../source\chapters\ch17-complex-numbers-fourier-ideas-and-the-road-ahead\sections\sec-17-5-conservation-laws-in-one-dimension.xml)

Flag: Replace the remaining figurative claim with the specific mathematical result or model condition.

**Before**

> This is the same kind of honesty we used throughout calculus. A theorem’s hypotheses are not decoration. They say exactly what the formula is allowed to ignore.

**After**

The balance equation must include every mechanism that changes the quantity. Omitting a source term changes the model’s assumptions.

## 357. Conservation laws in one dimension

Source: [source\chapters\ch17-complex-numbers-fourier-ideas-and-the-road-ahead\sections\sec-17-5-conservation-laws-in-one-dimension.xml](../../source\chapters\ch17-complex-numbers-fourier-ideas-and-the-road-ahead\sections\sec-17-5-conservation-laws-in-one-dimension.xml)

Flag: Replace the remaining figurative claim with the specific mathematical result or model condition.

**Before**

> Boundary flux alone explains the change inside only when nothing is created or destroyed in the interval. In your own words, why is that hypothesis part of the conservation law, and how does a source term restore honesty when cars appear from an on-ramp?

**After**

If cars enter from an on-ramp inside the interval, endpoint flux alone does not describe the change in their number. Explain how an interior source term completes the balance equation.

## 358. Conic sections

Source: [source\chapters\ch14-parametric-curves-polar-coordinates-and-conics\sections\sec-14-6-conic-sections.xml](../../source\chapters\ch14-parametric-curves-polar-coordinates-and-conics\sections\sec-14-6-conic-sections.xml)

Flag: Replace the remaining figurative claim with the specific mathematical result or model condition.

**Before**

> This is a parabola opening left. Its focus is at the origin, exactly as the polar setup promised.

**After**

This is a left-opening parabola with its focus at the origin.

## 359. Chapter review and discovery problems

Source: [source\chapters\ch15-sequences-and-infinite-series\sections\sec-15-9-chapter-review-and-discovery-problems.xml](../../source\chapters\ch15-sequences-and-infinite-series\sections\sec-15-9-chapter-review-and-discovery-problems.xml)

Flag: Replace the remaining figurative claim with the specific mathematical result or model condition.

**Before**

> That question leads to power series, Taylor polynomials, and the promised bridge to

**After**

The next chapter develops power series and Taylor polynomials, which will justify

## 360. Indeterminate forms and l’Hospital’s Rule

Source: [source\chapters\ch06-shape-extremes-and-the-mean-value-theorem\sections\sec-6-6-indeterminate-forms-and-l-hospital-s-rule.xml](../../source\chapters\ch06-shape-extremes-and-the-mean-value-theorem\sections\sec-6-6-indeterminate-forms-and-l-hospital-s-rule.xml)

Flag: Replace the remaining figurative claim with the specific mathematical result or model condition.

**Before**

> The converse is not promised.

**After**

The converse does not follow from the theorem.

## 361. Chapter review and discovery problems

Source: [source\chapters\ch06-shape-extremes-and-the-mean-value-theorem\sections\sec-6-8-chapter-review-and-discovery-problems.xml](../../source\chapters\ch06-shape-extremes-and-the-mean-value-theorem\sections\sec-6-8-chapter-review-and-discovery-problems.xml)

Flag: Replace the remaining figurative claim with the specific mathematical result or model condition.

**Before**

> Find the number c promised by the theorem.

**After**

Find a number c satisfying the theorem’s conclusion.

## 362. Chapter review and discovery problems

Source: [source\chapters\ch06-shape-extremes-and-the-mean-value-theorem\sections\sec-6-8-chapter-review-and-discovery-problems.xml](../../source\chapters\ch06-shape-extremes-and-the-mean-value-theorem\sections\sec-6-8-chapter-review-and-discovery-problems.xml)

Flag: Replace the remaining figurative claim with the specific mathematical result or model condition.

**Before**

> Find the number c promised by the Mean Value Theorem.

**After**

Find a number c satisfying the Mean Value Theorem’s conclusion.

## 363. Two theorems about continuous functions

Source: [source\chapters\ch03-limits-and-continuity\sections\sec-3-6-two-theorems-about-continuous-functions.xml](../../source\chapters\ch03-limits-and-continuity\sections\sec-3-6-two-theorems-about-continuous-functions.xml)

Flag: State the failed hypothesis or undefined operation directly.

**Before**

> A function that jumps from 0 to 2 can miss the intermediate value 1 even on a closed interval. In your own words, why is continuity not decoration, and what illegal move would it be to apply the theorem to a graph with a break?

**After**

A function that jumps from 0 to 2 can miss the intermediate value 1 even on a closed interval. Explain which hypothesis of the Intermediate Value Theorem fails and why its conclusion need not hold.

## 364. Warning examples

Source: [source\chapters\ch03-limits-and-continuity\sections\sec-3-7-warning-examples.xml](../../source\chapters\ch03-limits-and-continuity\sections\sec-3-7-warning-examples.xml)

Flag: State the failed hypothesis or undefined operation directly.

**Before**

> What illegal use of the Intermediate Value Theorem do the warnings protect against?

**After**

Which hypothesis of the Intermediate Value Theorem must be checked?

## 365. Chapter review and discovery problems

Source: [source\chapters\ch03-limits-and-continuity\sections\sec-3-9-chapter-review-and-discovery-problems.xml](../../source\chapters\ch03-limits-and-continuity\sections\sec-3-9-chapter-review-and-discovery-problems.xml)

Flag: State the failed hypothesis or undefined operation directly.

**Before**

> The Intermediate Value Theorem and the Extreme Value Theorem guarantee that answers exist; they do not usually compute those answers. In your own words, which hypotheses must be checked before using each theorem, and why is a true theorem still illegal to apply when a condition is missing?

**After**

The Intermediate Value Theorem and the Extreme Value Theorem guarantee existence under stated hypotheses. List the hypotheses of each theorem and give a counterexample showing why a missing hypothesis can invalidate its conclusion.

## 366. Warning examples

Source: [source\chapters\ch13-differential-equations-laws-written-as-derivatives\sections\sec-13-9-warning-examples.xml](../../source\chapters\ch13-differential-equations-laws-written-as-derivatives\sections\sec-13-9-warning-examples.xml)

Flag: State the failed hypothesis or undefined operation directly.

**Before**

> That division may be illegal at some values of the solution. Those values often give

**After**

Division is undefined when the factor is zero. Those values often give

## 367. Warning examples

Source: [source\chapters\ch14-parametric-curves-polar-coordinates-and-conics\sections\sec-14-9-warning-examples.xml](../../source\chapters\ch14-parametric-curves-polar-coordinates-and-conics\sections\sec-14-9-warning-examples.xml)

Flag: State the failed hypothesis or undefined operation directly.

**Before**

> The parametric slope formula is illegal when both derivatives vanish, and the same warning applies to polar curves. In your own words, what different geometric behaviors can hide behind that 0/0, and what extra tools can distinguish them?

**After**

When both parametric derivatives vanish, the slope quotient is undefined. The same issue occurs for polar curves. Describe the different tangent behaviors that can occur and the limits or expansions that can distinguish them.

## 368. Computing experiments

Source: [source\chapters\ch12-numerical-integration-error-and-computation\sections\sec-12-6-computing-experiments.xml](../../source\chapters\ch12-numerical-integration-error-and-computation\sections\sec-12-6-computing-experiments.xml)

Flag: Identify the accuracy assumption without referring to a promise.

**Before**

> A more powerful rule always gives its promised error behavior.

**After**

A higher-order rule always achieves its stated convergence order.

## 369. Completeness and the idea of no gaps

Source: [source\chapters\ch02-numbers-functions-and-models\sections\sec-2-2-completeness-and-the-idea-of-no-gaps.xml](../../source\chapters\ch02-numbers-functions-and-models\sections\sec-2-2-completeness-and-the-idea-of-no-gaps.xml)

Flag: Replace the vague claim about completeness with its specific role.

**Before**

> We will not mention completeness every time we take a limit. But it is quietly underneath the whole subject. It is what lets the language of “as close as we want” point to an actual number.

**After**

A gap in the number system can prevent these approximations from having a limit within that system.

## 370. Chapter review and discovery problems

Source: [source\chapters\ch15-sequences-and-infinite-series\sections\sec-15-9-chapter-review-and-discovery-problems.xml](../../source\chapters\ch15-sequences-and-infinite-series\sections\sec-15-9-chapter-review-and-discovery-problems.xml)

Flag: Shorten the test list and avoid an overfull line in the printed introduction.

**Before**

> These problems distinguish sequence limits from series sums and apply the Cauchy criterion, comparison tests, alternating-series bounds, absolute-convergence tests, and the Dirichlet and Abel tests. Explain why the selected test applies before drawing a convergence conclusion.

**After**

These problems distinguish sequence limits from series sums and apply the convergence tests developed in this chapter. State the hypotheses of the selected test and explain why they hold.

## 371. Final projects

Source: [source\chapters\ch17-complex-numbers-fourier-ideas-and-the-road-ahead\sections\sec-17-7-final-projects.xml](../../source\chapters\ch17-complex-numbers-fourier-ideas-and-the-road-ahead\sections\sec-17-7-final-projects.xml)

Flag: Use the generated reference label once; title references already name the linked subsection.

**Before**

> Section [cross-reference]

**After**

[cross-reference]

## 372. Additional topics: local existence and uniqueness

Source: [source\chapters\ch17-complex-numbers-fourier-ideas-and-the-road-ahead\sections\sec-additional-local-existence-uniqueness.xml](../../source\chapters\ch17-complex-numbers-fourier-ideas-and-the-road-ahead\sections\sec-additional-local-existence-uniqueness.xml)

Flag: Use the generated reference label once; title references already name the linked subsection.

**Before**

> Chapter [cross-reference]

**After**

[cross-reference]

## 373. Power series

Source: [source\chapters\ch16-power-series-taylor-polynomials-and-taylor-series\sections\sec-16-1-power-series.xml](../../source\chapters\ch16-power-series-taylor-polynomials-and-taylor-series\sections\sec-16-1-power-series.xml)

Flag: Use the generated reference label once; title references already name the linked subsection.

**Before**

> Chapter [cross-reference]

**After**

[cross-reference]

## 374. Taylor’s theorem and remainders

Source: [source\chapters\ch16-power-series-taylor-polynomials-and-taylor-series\sections\sec-16-5-taylor-s-theorem-and-remainders.xml](../../source\chapters\ch16-power-series-taylor-polynomials-and-taylor-series\sections\sec-16-5-taylor-s-theorem-and-remainders.xml)

Flag: Use the generated reference label once; title references already name the linked subsection.

**Before**

> Section [cross-reference]

**After**

[cross-reference]

## 375. Taylor’s theorem and remainders

Source: [source\chapters\ch16-power-series-taylor-polynomials-and-taylor-series\sections\sec-16-5-taylor-s-theorem-and-remainders.xml](../../source\chapters\ch16-power-series-taylor-polynomials-and-taylor-series\sections\sec-16-5-taylor-s-theorem-and-remainders.xml)

Flag: Use the generated reference label once; title references already name the linked subsection.

**Before**

> Section [cross-reference]

**After**

[cross-reference]

## 376. Uniform convergence preview

Source: [source\chapters\ch16-power-series-taylor-polynomials-and-taylor-series\sections\sec-16-8-uniform-convergence-preview.xml](../../source\chapters\ch16-power-series-taylor-polynomials-and-taylor-series\sections\sec-16-8-uniform-convergence-preview.xml)

Flag: Use the generated reference label once; title references already name the linked subsection.

**Before**

> Section [cross-reference]

**After**

[cross-reference]

## 377. Additional topics: the Weierstrass M-test

Source: [source\chapters\ch16-power-series-taylor-polynomials-and-taylor-series\sections\sec-additional-weierstrass-m-test.xml](../../source\chapters\ch16-power-series-taylor-polynomials-and-taylor-series\sections\sec-additional-weierstrass-m-test.xml)

Flag: Use the generated reference label once; title references already name the linked subsection.

**Before**

> Chapter [cross-reference]

**After**

[cross-reference]

## 378. Sequences

Source: [source\chapters\ch15-sequences-and-infinite-series\sections\sec-15-1-sequences.xml](../../source\chapters\ch15-sequences-and-infinite-series\sections\sec-15-1-sequences.xml)

Flag: Use the generated reference label once; title references already name the linked subsection.

**Before**

> Chapter [cross-reference]

**After**

[cross-reference]

## 379. Trigonometric substitution

Source: [source\chapters\ch11-techniques-of-integration\sections\sec-11-3-trigonometric-substitution.xml](../../source\chapters\ch11-techniques-of-integration\sections\sec-11-3-trigonometric-substitution.xml)

Flag: Use the generated reference label once; title references already name the linked subsection.

**Before**

> Section [cross-reference]

**After**

[cross-reference]

## 380. Increasing and decreasing functions

Source: [source\chapters\ch06-shape-extremes-and-the-mean-value-theorem\sections\sec-6-1-increasing-and-decreasing-functions.xml](../../source\chapters\ch06-shape-extremes-and-the-mean-value-theorem\sections\sec-6-1-increasing-and-decreasing-functions.xml)

Flag: Use the generated reference label once; title references already name the linked subsection.

**Before**

> Section [cross-reference]

**After**

[cross-reference]

## 381. Rolle’s Theorem and the Mean Value Theorem

Source: [source\chapters\ch06-shape-extremes-and-the-mean-value-theorem\sections\sec-6-3-rolle-s-theorem-and-the-mean-value-theorem.xml](../../source\chapters\ch06-shape-extremes-and-the-mean-value-theorem\sections\sec-6-3-rolle-s-theorem-and-the-mean-value-theorem.xml)

Flag: Use the generated reference label once; title references already name the linked subsection.

**Before**

> Section [cross-reference]

**After**

[cross-reference]

## 382. Rolle’s Theorem and the Mean Value Theorem

Source: [source\chapters\ch06-shape-extremes-and-the-mean-value-theorem\sections\sec-6-3-rolle-s-theorem-and-the-mean-value-theorem.xml](../../source\chapters\ch06-shape-extremes-and-the-mean-value-theorem\sections\sec-6-3-rolle-s-theorem-and-the-mean-value-theorem.xml)

Flag: Use the generated reference label once; title references already name the linked subsection.

**Before**

> Section [cross-reference]

**After**

[cross-reference]

## 383. Average rate of change

Source: [source\chapters\ch04-the-derivative\sections\sec-4-1-average-rate-of-change.xml](../../source\chapters\ch04-the-derivative\sections\sec-4-1-average-rate-of-change.xml)

Flag: Use the generated reference label once; title references already name the linked subsection.

**Before**

> Section [cross-reference]

**After**

[cross-reference]

## 384. Limits from motion and approximation

Source: [source\chapters\ch03-limits-and-continuity\sections\sec-3-1-limits-from-motion-and-approximation.xml](../../source\chapters\ch03-limits-and-continuity\sections\sec-3-1-limits-from-motion-and-approximation.xml)

Flag: Use the generated reference label once; title references already name the linked subsection.

**Before**

> Section [cross-reference]

**After**

[cross-reference]

## 385. Chapter review and discovery problems

Source: [source\chapters\ch03-limits-and-continuity\sections\sec-3-9-chapter-review-and-discovery-problems.xml](../../source\chapters\ch03-limits-and-continuity\sections\sec-3-9-chapter-review-and-discovery-problems.xml)

Flag: Use the generated reference label once; title references already name the linked subsection.

**Before**

> Section [cross-reference]

**After**

[cross-reference]

## 386. Rolle’s Theorem and the Mean Value Theorem

Source: [source\chapters\ch06-shape-extremes-and-the-mean-value-theorem\sections\sec-6-3-rolle-s-theorem-and-the-mean-value-theorem.xml](../../source\chapters\ch06-shape-extremes-and-the-mean-value-theorem\sections\sec-6-3-rolle-s-theorem-and-the-mean-value-theorem.xml)

Flag: Explain what each theorem establishes, then give the motion example directly.

**Before**

> [cross-reference] gave us two tools. First, a continuous function on a closed interval reaches its absolute maximum and minimum. Second, a differentiable local extremum at an interior point must have derivative 0. Those two facts now combine into a theorem about motion. Suppose a car is at mile marker 10 at noon and mile marker 160 at 3{:}00. Its average velocity is \frac{160-10}{3-0}=50 miles per hour. The car may have driven slowly at first and quickly later. It may have stopped for a short time. But if its position changed continuously, and if its velocity existed during the trip, then at some instant the speedometer must have read 50\text{ miles per hour}. That is the meaning of the Mean Value Theorem.

**After**

Rolle’s Theorem combines the existence of absolute extrema with the zero-derivative condition at an interior extremum. The Mean Value Theorem extends the result to unequal endpoint values. For example, a car moving from mile marker 10 at noon to mile marker 160 at 3{:}00 has average velocity \frac{160-10}{3-0}=50 miles per hour. If its position is continuous throughout the trip and its velocity exists between the endpoint times, then at some instant its velocity is 50\text{ miles per hour}. The car’s velocity may vary during the trip. The Mean Value Theorem guarantees an instant when it equals the average velocity.

## 387. Chapter review and discovery problems

Source: [source\chapters\ch03-limits-and-continuity\sections\sec-3-9-chapter-review-and-discovery-problems.xml](../../source\chapters\ch03-limits-and-continuity\sections\sec-3-9-chapter-review-and-discovery-problems.xml)

Flag: Name the mathematical topic instead of using an editorial label.

**Before**

> End-of-chapter hook

**After**

The derivative as a limit

## 388. Polar coordinates

Source: [source\chapters\ch14-parametric-curves-polar-coordinates-and-conics\sections\sec-14-4-polar-coordinates.xml](../../source\chapters\ch14-parametric-curves-polar-coordinates-and-conics\sections\sec-14-4-polar-coordinates.xml)

Flag: Use the generated reference label once; title references already name the linked subsection.

**Before**

> Figure [cross-reference]

**After**

[cross-reference]

## 389. Direction fields

Source: [source\chapters\ch13-differential-equations-laws-written-as-derivatives\sections\sec-13-2-direction-fields.xml](../../source\chapters\ch13-differential-equations-laws-written-as-derivatives\sections\sec-13-2-direction-fields.xml)

Flag: Use the generated reference label once; title references already name the linked subsection.

**Before**

> Figure [cross-reference]

**After**

[cross-reference]

## 390. Rolle’s Theorem and the Mean Value Theorem

Source: [source\chapters\ch06-shape-extremes-and-the-mean-value-theorem\sections\sec-6-3-rolle-s-theorem-and-the-mean-value-theorem.xml](../../source\chapters\ch06-shape-extremes-and-the-mean-value-theorem\sections\sec-6-3-rolle-s-theorem-and-the-mean-value-theorem.xml)

Flag: Use the generated reference label once; title references already name the linked subsection.

**Before**

> Figure [cross-reference]

**After**

[cross-reference]

## 391. Derivatives of trigonometric functions

Source: [source\chapters\ch05-differentiation-rules-and-elementary-functions\sections\sec-5-5-derivatives-of-trigonometric-functions.xml](../../source\chapters\ch05-differentiation-rules-and-elementary-functions\sections\sec-5-5-derivatives-of-trigonometric-functions.xml)

Flag: Use the generated reference label once; title references already name the linked subsection.

**Before**

> Figure [cross-reference]

**After**

[cross-reference]

## 392. Chapter review and discovery problems

Source: [source\chapters\ch03-limits-and-continuity\sections\sec-3-9-chapter-review-and-discovery-problems.xml](../../source\chapters\ch03-limits-and-continuity\sections\sec-3-9-chapter-review-and-discovery-problems.xml)

Flag: Use the generated reference label once; title references already name the linked subsection.

**Before**

> Figure [cross-reference]

**After**

[cross-reference]
