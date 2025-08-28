---
title: Function Spaces
tags:
  - incomplete
created: 2025-07-25
draft: false
---

**Proposition**:
1. $\phi,X$ are closed
2. $F \subseteq X$ closed iff $X \setminus F$ is open
3. If $F_{i} \subseteq X$ are closed then $\bigcap F_{i}$ is also closed
4. If $F_{1}$ and $F_{2}$ are closed then so is $F_{1} \cup F_{2}$

**Proof**: Trivial

**Proposition**: Let $(X,\rho)$ be a metric space and $F \subseteq X$ Then F is closed iff whenever $\{ x_{n} \} \subseteq F \to x \in X$
Then $x \in F$
**Proof**: Exercise
### Continuous Functions
![[Drawing 2025-07-21 09.34.32.excalidraw.svg]]

**Def**: Let $(X,\rho)$ $(\gamma,\sigma)$ be metric spaces and $f:X\to Y$ be a function. Then F is said to be continuous at $x \in X$if for every $\epsilon > 0$, $\exists \delta >0$

such that  
$$
\sigma (f(x),f(z)) < \epsilon \quad \text{whenever} \rho(x,z) < \delta 
$$
We say f is continuous on X if it is continuous at each point in X

f is said to be uniformly continuous if for every $\epsilon > 0$ $\delta$ does not depend on X.

Ex: Lipschitz functions.

**Proposition**: Let $(X,\rho ), (Y,\sigma)$ be metric spaces and $f:X \to Y$ be a function. Then f is continuous at x iff $\forall \{ x_{n} \} \to x,\{ f(x_{n}) \}\to f(x)$

**Proof**: Trivial

**Proposition**: Let $(X,\rho),(Y,\sigma)$ be metric spaces and $f:X\to Y$ be a function Then f is continuous iff for every open set $E \subseteq Y, f^{-1}(E)$ is open in X.
**Proof**: Trivial

## Completeness

**Def**: Let $(X,\rho)$ be a metric space and $\{ x_{n} \} \subseteq X$ is said to be Cauchy sequence if for $\forall \epsilon > 0$ $\exists k_{\epsilon} \in \mathbb{N}$ such that
$$
\rho (x_{n},x_{m}) < \epsilon \quad \forall n,m \geq k_{\epsilon }
$$
$(X,\rho)$ is said to be complete if every Cauchy sequence converges to a point in X.

Example: 
1. $\mathbb{R},\mathbb{R}^{n}$
2. Any closed interval in $\mathbb{R}$ is complete

**Proposition**: Let $(X,\rho )$ be a complete metric space then closed set $\iff$ complete set.

**Def**: Let $(X,\rho)$ be a metric space and $E\subseteq X$ then $\text{diam}(E)$ is $\sup_{x,y \in E} \rho(x,y)$, $E$ is said to be bounded in the supremum is finite.
$\{E_{i}\}_{i \in \mathbb{N}}$ is a decreasing sequence of non-empty subsets of E is said to be contracting if $\text{diam} E_{n}\to 0$ as $n\to \infty$

**Theorem**: (Cantor Intersection) Let $(X,\rho)$ be a metric space, and X is complete iff whenever ${F_{i}}$ is a decreasing seq of non empty closed contracting subset of X, $\bigcap  F_{i}$ contains exactly one point.

**Proof**: $(\implies)$  Choose a point from each of $F_{i}$ then since the diameters are decreasing to 0, we have a Cauchy sequence, hence it converges to a point in X.
$(\impliedby)$ For each $k \in \mathbb{N}$ we have that there exists $N_{k}$ such that for $n,m > N_{k}$ $d(x_{n,x_{m}})< \frac{1}{k}$ . So we can choose a sequence of points such that they make up nested closed and contracting intervals, hence they have a common point. Hence the Cauchy sequence converges to that unique point.



25/07/25:
**Theorem**:(Lebesgue Covering Lemma) Let X be a compact metric space and {$E_{i}$} be an open cover. Then there exists $\epsilon > 0$. such that for any point x there is a ball of radius of $\epsilon$ contained in one of the $E_{i}$

**Proof**: Assume no such $\epsilon$ exists. Then $\forall n \in \mathbb{N} \ \exists x_{n}$ s.t $B\left( x_{n}, \frac{1}{n} \right)$  does not completely lie inside any of $E_{i}$
By compactness there should be a convergent subsequence for $x_{n}$. Now x $\in E_i$ for some i. and hence there is a $\delta >0$ such that $B(x,\delta) \subseteq E_{i}$ . But then as $x_{n}$ goes to x and as 1/n becomes smaller than $\delta$ we get a contradiction.

**Proposition**: Let $(X,\rho), (Y,\sigma)$ be metric space and X compact $f:X\to Y$ be continuous ,then f is uniformly continuous.

**Proof**: From continuity of f, for every $x_{0} \in X$ and $\epsilon > 0$ $\exists \delta > 0$ such that
$$
\sigma(f(x_{0}),f(x)) < \frac{\epsilon}{2} \quad \text{whenever } \rho(x_{0},x) < \delta_{x_{0}} 
$$
Now we have that every open ball of radius $\delta_{x_{0}}$ centered at $x_{0}$ $\{ B(x,\delta_{x}) \}_{x \in X}$ will cover X, and any 2 points $x,y$ in that ball will satisfy
$$
\sigma(f(x),f(y)) < \epsilon  
$$
From Lebesgue Covering Lemma we have that there exists a $\delta>0$ such that any open ball of radius $\delta$  will be completely contained in one of the open sets, hence any 2 points satisfying $\rho(x,y) < \delta$ will be inside one of them and hence will satisfy the uniform continuity condition.$\quad \blacksquare$


**Def**: let V be a vector space . A function || || : V -> R is said to be norm if
1. ||u|| >= 0 $\forall u \in V$ and $||u||=0$ iff u = 0
2. $||\lambda u|| = \lambda||u||$
3. $||u + v|| \leq ||u|| + ||v||$

Example:  $l^p = \left\{  x = (x_{1},\dots,x^n, \dots  ) :  ( \sum_{n=1}^{\infty}|x_{n}|^p \right)^{1/p}  )  \text{ converges}\}$

**Def**: a normed linear space is infinite dimensional if there is a infinite linearly independent set.

Example: 
1. $l^p$
2. $C[0,1]$
3. For compact metric space consider $C(X) = \{ f:X\to \mathbb{R}| f\text{ continuous on X} \}$ with sup norm
If the compact set has only finitely many elements then we can create
$$
f_{i}(x_{j}) =
\begin{cases}
0 & \text{if } i \neq j \\
1 & \text{if } i = j
\end{cases}
$$

**Proposition:** Let Y be a finite dimensional subspace of a normed linear space X then Y is complete

**Proof:**
we will prove by induction on the dimension of Y.
Let us assume $\dim Y = 1$

So, $\exists y \in X$ such that $Y = \{ ky|k\in \mathbb{R} \}$
let $\{ k_{n}y \}$ be a Cauchy sequence in Y.
For a given $\epsilon>0$ $\exists p \in \mathbb{N}$ such that
$$
\lvert k_{n}y - k_{m}y \rvert < \epsilon \quad\forall n,m\geq  p
$$
$$
\lvert k_{n}-k_{m} \rvert ||y|| < \epsilon
$$
$$
|k_{n} - k_{m} | < \frac{\epsilon}{||y||}
$$

so ${k_{n}}$ is a Cauchy sequence in $\mathbb{R}$ since $\mathbb{R}$ is complete implies $k_n$ converges. Hence $\{ k_{n}y \}$ converges to some $ky$

Now assume Y = $\text{span}\{ x_{1},x_{2},\dots,x_{n-1} \}$ and Y is complete
will show Z = $\text{span}\{x_{1},x_{2},\dots,x_{n-1},x_{n}\}$ is complete

Choose a Cauchy sequence
let $z^{(p)} = \alpha_{1}^{(p)}x_{1} + \dots + \alpha_{n-1}^{(p)}x_{n-1} + \alpha_{n}^{(p)}x_{n}$
$|| z^{(p)} - z^{(m)}|| = || (y^{p}-y^{m}) + \alpha_{n}^{(p)}x_{n} - \alpha_{n}^{(m)}x_{n}||$
$$
= |\alpha_{m} - \alpha_{n}| || \frac{1}{|\alpha_{n}^{(p)}-\alpha_{n}^{(m)}|}(y^{(p)}-y^{(m)}) - x_{n}||
$$
$$
\geq |\alpha_{n}^{p} - \alpha_{n}^{m}| \text{dist}(x_{n,Y})
$$

since $\{z^{(p)}\}$ is Cauchy for given $\epsilon>0$. we have {$\alpha$} is Cauchy in $\mathbb{R}$


**Lemma**: (Riesz's Lemma): Let Y be a closed subspace of X such that Y $\neq$X. Then for any $0<r<1$. $\exists x_{r}\in X$ such that $\lvert x_{r} \rvert = 1$ and $r<\text{dist}(x_{r},Y) \leq 1$

**Proof**:
Since $Y \neq  X$ . Fix an $x \in X-Y$ . Then there exists element $y \in Y$ (by the property of infimum) such that
$$
| x- y| \leq \frac{\text{dist}(x,Y)}{r}
$$
Choose, 
$$
x_{r} = \frac{x-y}{||x-y||}
$$
and we have,
$$
||x_{r}|| = 1
$$
$$
\begin{align*}
\text{dist}(x_{r},Y) \leq & ||x_{r}-0|| \quad 0 \in Y \\
& ||x_{r}|| \\
&=1
\end{align*}
$$
$$
\begin{align*}
\text{dist}(x_{r},Y) =& \text{ dist}\left( \frac{x-y}{||x-y||},Y\right) \\
=&\frac{1}{||x-y||}\text{dist}(x-y,||x-y||Y) \\
=&\frac{1}{||x-y||} \text{dist}(x-y,Y) \\
=&\frac{1}{||x-y||}\text{dist}(X,Y) \\
\geq & \quad r \hspace{10em} \blacksquare  \\
 
\end{align*}
$$



**Theorem**: Let $(X,||\cdot ||)$ be a infinite dimensional space. Let $B(0,1) = \{x \in X| ||x|| \leq  1\}$ be the closed unit ball in X. Then $B(0,1)$ is not compact.

**Proof**: let $\{ x_{1},x_{1},x_{3},\dots  \}$ be an infinite linearly independent set 
Define $Z_{n}$ : $\text{span}\{x_{1},x_{2},\dots,x_{n}\}$
$Z_{1} \subset Z_{2} \subset \dots$
$Z_{n}$ are closed. for all n

By Riesz lemma we can choose $z_{n} \in Z_{n}$  such that $\text{dist}(z_{n},Z_{n-1}) > \frac{1}{2}$  then we can get that there cannot be any convergent subsequence in $\{ z_{n} \}$ hence X is not sequentially compact hence X is not compact.


**Def**: Let $\{ f_{n} \}$ sequence of functions on a metric space. Then $\{ f_{n} \}$ is said to converge to f pointwise if for every x in X for a given $\epsilon>0$ $\exists k \in \mathbb{N}$.
$$
|f_{n}(x) - f(x)| <\epsilon \quad n\geq k
$$
$\{f_n\}\to f$ uniformly if k is uniform wrt x

Example: $f_{n}(x) = x^n$  converges to $f(x) = 0 \  for \ x \in [0,1), 1 \ o.w$

**Def**: $\{ f_{n} \}$ is said to be uniformly Cauchy if for a given $\epsilon>0$ $\exists$ k $\in \mathbb{N}$ such that $|f_{n}(x) - f_{m}(x)| < \epsilon$ for all $n,m \geq  k$ and $\forall x \in X$


**Prop**: Let $\{ f_{n} \}$ be a sequence of functions on X. Then $f_{n}$ converges to some $f$ uniformly iff $f_{n}$ is uniformly Cauchy

**Proof**: Let $f_{n} \to  f$ uniformly then  for given $\epsilon>0$ $\exists k \in \mathbb{N}$ such that
$$
|f_{n}(x)- f(x)| < \frac{\epsilon}{2}
$$

$$ 
\begin{align*}
|f_{n}(x) - f_{m}(x) | &\leq |f_{n}(x)-f(x) + f(x) - f_{m}(x)|
\\ &\leq |f_{n}(x) - f(x)| + |f_{m}(x) - f(x)|  \\
&< \epsilon
\end{align*}
$$

Therefore $f_{n}$ is uniformly Cauchy

Conversely, Suppose $f_{n}$ is uniformly Cauchy then for a given $\epsilon>0$ $\exists k \in \mathbb{N}$ such that
$$
|f_{n}(x) - f_{m}(x)| < \frac{\epsilon}{2}
$$
for $n,m > k_{1}$ over all $x \in X$

Let $f(x)$ be the pointwise limit of $f_n(x)$ since it converges in $\mathbb{R}$

$$
|f_{n}(x) - f(x)| < \frac{\epsilon}{2}
$$
for $n\geq k_{2}$

Now set $p = \text{max}(k_1,k_2)$
$$
|f_{n}(x)- f(x)| \leq |f_{n}(x) - f_{p}(x) | + |f_{p}(x) - f(x)| <\epsilon \quad \forall x \in X
$$
Hence $f_{n}$ converges uniformly $\quad \blacksquare$

**Proposition:** $\{ f_{n} \}$ be a uniformly convergent sequence of function on a a metric space X iff $\{ f_{n} \}$ is uniformly Cauchy

**Proof:** Result from #Analysis2 


**Proposition:** Let $\{ f_{n} \}$ be a sequence of function which converge pointwise to a function f. Then $\{ f_{n} \} \to f$ Uniformly iff exists a sequence of real numbers

**Proof:** Result from #Analysis2 
 **Proposition:** Let $\{ f_{n} \}$ be a sequence of continuous funs on a metric space X such that $\{ f_{}n \} \to f$ uniformly . Then f is continuous on X.

**Proof:** Result from #Analysis2  

**Theorem**: For a compact metric X, C(X) is complete

**Proof**: Let $\{ f_{n} \}$ be a Cauchy sequence in C(X) then given $\epsilon>0$ $\exists k \in \mathbb{N}$ such that
$$
\sup_{x \in X} |f_{m}(x) - f_{n}(x)| < \epsilon \quad \forall n,m \geq k
$$
That is $\{ f_{n} \}$ is uniformly Cauchy on X. 
So, $\{ f_{n} \}$ converges uniformly to some f on X.

By, Prop(3), the $f$ is continuous on X
Now, since, $\{ f_{n} \}\to f$ uniformly, $\exists \{ M_{n} \}$ such that $M_{n} \to 0$ and 
$$
\sup_{x \in X} |f_{n}(x) - f(x)| \leq M_{n} \quad \forall n
$$
Hence $\rho(f_{n},f) \to 0$ as $n \to \infty$

**Def:** A metric space is said to be separable if it has a countable dense subset.
E.g.: $\mathbb{R}^n$ has dense set $\mathbb{Q}$
$C[a,b]$ has dense set of polynomials

**Prop**: Compact metric space are separable
**Proof**: Let X be a compact metric space. Then X is totally bounded. So, for every $n \in N$ $\exists n_{k}$ number of points such that there are $n_{k}$ many balls of radius $\frac{1}{n}$ that covers X. Now consider all the centers of these balls. Now we have a countable union of finite sets. Now we claim that this set is dense. Consider any point p and a open ball $B(p,r)$ of radius r. Now take $\frac{1}{n_{0}} < r$ Now since balls of radius $\frac{1}{n_{0}}$ covers X, It also covers the point p. Hence the $B(p,r)$ intersects the ball of radius $\frac{1}{n_{0}}$. Hence every point is a limit point.

**Remark**: compact $\sim$ complete and totally bounded.

**Proposition:** Subspace of a separable metric space is separable.
**Proof**: Let X be separable.  Y$\subseteq X$
Let {$x_{n}$ | $n \in \mathbb{N}$} be the countable dense subset of X. $\forall k \in \mathbb{N}$ 
if $B(x_{n}, \frac{1}{k} ) \cap Y \neq \varnothing$  Then choose a point from the intersection.

Let 
$$
S = \left\{  y_{n,k} \vert \forall n,k \in \mathbb{N} \quad s.t  B\left( x_{n},\frac{1}{k} \right) \cap Y \neq \varnothing \right\}
$$
See that the balls around $x_{n}$ should intersect every element in Y taken in union. So taking an element from each ball $B(x_{n},\frac{1}{k})$ gives a dense set.

### Arzela Ascoli Theorem
**Def:** Let F be collection of  real valued function on a metric space X. F is said to be equicontinuous at $x_0 \in X$ if given $\epsilon>0$, there exists $\delta >0$ such that $\forall f \in F$ $|f(x_{0})-f(y)| < \epsilon$ whenever $\rho(x_{0},y)< \delta$.
* F is equicontinuous on X if F is equicontinuous at each $x \in X$
* F is said to be uniformly equicontinuous if $\delta$ in the above definition is uniform for all $x_{0},y \in X$

Examples: 
1.  Let X be a compact metric space $\{ f_{1},f_{2},\dots,f_{n} \}$ .Because , all the $f_{i}$ are uniformly continuous on X. So for each $f_{i}$ and for a given $\epsilon>0$
2. $f_{n}:[0,1] \to \mathbb{R}, f_{n}(x) = x^{n}$ is equicontinuous on $[0,1)$
3. $f \in C[a,b]$, f differentiable on $(a,b)$ and $\exists M>0$ such that
$$
|f'(x)| < M \quad \forall x \in[a,b]
$$
then the collection of f is uniformly equicontinuous

**Def:** A collection F of function on X is said to be uniformly bounded if $\exists M >0$ such that
$$
|f(x)| < M \quad \forall x \in X \text{ and } \forall f \in F
$$

**Theorem:** (Arzela-Ascoli) Let X be a compact metric space. Let $\{ f_{n} \}_{n=1}^{\infty }$ be a sequence of functions in $(C(X),\rho_{\infty})$ such that $\{ f_{n} \}$ is uniformly bounded and uniformly continuous. Then $\exists$ a subsequence $\{ f_{n_{k}} \}$ which converges in $C(X)$

**Proof:** Since X is compact, X is totally bounded

$\forall n \in \mathbb{N}$ , $\exists S_{n}= \{ s_{1},\dots,s_{n_{k}} \}$ such that
$$
X = \bigcup_{i=1}^{n_{k}} B \left(s_{i},\frac{1}{n} \right)
$$
$$
S = \bigcup_{i=1}^{n} = \{x_{1},x_{2},\dots,\}
$$
**Step I**:
Using uniformly boundedness of $\{ f_{n} \}$ we find a subsequence which converge pointwise

Take $x_{1} \in S$ and consider $\{ f_{n}(x_{1}) \}_{n=1}^{\infty }$ . Since $\{ f_{n} \}$ is uniformly bounded, $\{ f_{n}(x_{1}) \}$ is also uniformly bounded in $\mathbb{R}$

So it has convergent subsequence $\{ f_{1,n}(x_{1}) \}$. Consider ${f_{1,n}}$ and look at ${f_{1,n}(x_{2})}$ and repeat the same process to get
$$
\begin{align*}
\{f_{1,n}\} &= f_{1,1} ,f_{1,2},\dots,f_{1,k} \\
\{f_{2,n}\} &= f_{2,1},f_{2,2},\dots,f_{2,k} \\
\vdots & \\ 
\{f_{m,n}\} &= f_{m,1},f_{m,2},\dots,f_{m,k}

\end{align*}
$$

Consider $\{ f_{n,n} \}_{n=1}^{\infty}$ converge pointwise at each point of S. Define $g_{n} = f_{n,n} \forall n \in \mathbb{N}$ 

Using uniformly equicontinuous we show $g_{n}$ converges
Since $\{ g_{n} \}$ is uniformly equicontinuous, for  $\forall \epsilon >0, \exists \delta >0$ such that
$$
\lvert g_{n}(x) - g_{n}(y) \rvert < \frac{\epsilon}{3} \quad \forall \rho(x,y) < \delta \quad \forall n \in \mathbb{N}
$$

Choose $M \in \mathbb{N}$ such that $\frac{1}{M} < \delta$ . Consider $S_{M} \subseteq S, g_{n}$ pointwise converges at all points of $S_{M}$

Let $s \in S_{M}$, $\exists k_{s} \in \mathbb{N}$ such that
$$
\lvert g_{n}(s) - g_{m}(s) \rvert < \frac{\epsilon}{3} \quad \forall n,m\geq k_{s}
$$
Take $k = max\{ k_{s}  | s \in S_{M}\}$

$\forall n,m \geq k$ and $\forall s \in S_{M}$
$$
\lvert g_{n}(s) - g_{m}(s) \rvert < \frac{\epsilon}{3} \quad \forall n,m \geq k
$$
Then if $\rho(x,y) < \delta$
$$
\begin{align*}
\lvert g_{n}(x) - g_{m}(x)\rvert \leq &\lvert g_{n}(x) - g_{n}(s) \rvert +& \\ 
& \lvert g_{n}(s) - g_{m}(s) \rvert +&  \\
&\lvert g_{m}(s)-g_{m}(x) \rvert   \\
\leq &\frac{\epsilon}{3} + \frac{\epsilon}{3} + \frac{\epsilon}{3} \\
=& \epsilon
\end{align*}

$$

$\{ g_{n} \}$ is uniformly Cauchy on X and hence uniformly converges. $\quad \blacksquare$
### Banach Contraction principle

**Def:** let X be a metric space of $T:X \to X$ be a map . A point x in X is said to be fixed point if T(x) = x

Examples: Rotation of $\mathbb{R}^2$ around fixed point.

**Def:** Let $(X,\rho )$ be a metric space and $T:X\to X$ be a map T is said to be a contraction if $\exists 0<K<1$ such that
$$
\rho(T(x),T(y)) \leq k\rho(x,y)
$$
Example:
* $T:\mathbb{R} \to \mathbb{R}$ defined by $T(x) = \frac{x}{2}$
* Lipschitz with constant less than 1
**Theorem:** (Banach Contraction Principle) Let X be a complete metric space and $T:X\to X$ be a contraction then T has a unique fixed point.

**Proof:** fix $x_{0} \in X$ now consider $\{ x_{n} \}$ by 
$$
x_{n+1} = T(x_{n}) \quad \forall n=0,1,\dots 
$$
we will show 
1. $\{ x_{n} \}$ is a Cauchy sequence
2. T has a fixed point
3. the fixed point is unique

Let T be a contraction with constant 0<k <1
$\forall m \in \mathbb{N}$ we have
$$
\rho(x_{m-1},x_{m}) = \rho(T(x_{m-2}),T(x_{m-1})) \leq k\rho(x_{m},x_{m-1}) \leq \dots \leq k^m \rho(x_{1},x_{0})
$$
$\forall n \geq m$ we have
$$
\rho(x_{n},x_{m}) = \rho(x_{m},x_{m+1}) + \rho(x_{m+1},x_{m+2}) + \dots + \rho(x_{n-1},x_{n}) 
$$
$$
\leq k^m(1 + k + \dots + k^{n-m-1})\rho(x_{1},x_{0}) = \frac{k^{m}}{1-k} \rho(x_{1},x_{0}) \to 0 \quad \text{as} \quad m \to \infty 
$$

Hence $\{ x_{n} \}$ is a Cauchy sequence. Since X is complete. $x_{n}$ converges to some $x \in X$

Now to show that T has a fixed point
$$
\lim_{ n \to \infty } x_{n+1} = \lim_{ n \to \infty } T(x_{n}) 
$$
$\implies x = T(x)$
hence x is a fixed point

Now to check uniqueness of the fixed point, assume there is 2 fixed points x,y $x\neq y$
$$
\rho(x,y) = \rho(T(x),T(y)) \leq k\rho(x,y) < \rho(x,y)
$$
which is a contradiction. $\quad \blacksquare$


Remarks:
- $T: (0,\infty) \to (0,\infty)$ defined by $T(x) = \frac{x}{2}$ does not have fixed point hence completeness cannot be dropped
- consider $f(x) = \frac{1}{x} + x$ on $[1,\infty )$
### Applications of Banach fixed point theorem:
i) Integral equations
Let $K \in C([a,b]\times [a.b]), g \in C[a,b]$
$$
f(x) = \lambda \int_{a}^b K(x,y)f(y) dy + g(x) \quad \text{(I)}
$$
Q. For which $\lambda$ eq (I) has a sol in $(C[a,b],\rho_{\infty })$

Define $T : C[a,b] \to C[a,b]$ By
$$
Tf(x) = g(x) + \lambda \int_{a}^{b} K(x,y)f(x) dy
$$
f is a fixed point if it is the solution of the equation.

Now, 
$$
\rho_{\infty }(Tf_{1},Tf_{2}) = \sup|Tf_{1}(x) - Tf_{2}(x)| = \sup\left| \lambda \int_{a}^{b} K(x,y)(f_{1}(y)-f_{2}(y)) \right|
$$
$$
\leq|\lambda|c (b-a)\rho_{\infty }(f_{1},f_{2})
$$
T is a contraction if $|\lambda| < \frac{1}{c(b-a)}$


ii) (In Newton Method for approximating roots of a function)
Let f be a differentiable. 
$$
x_{1} = x_{0} - \frac{f(x_{0})}{f'(x_{0})}
$$
$$
\vdots 
$$
$$
x_{n+1} = x_{n} - \frac{f(x_{n})}{f'(x_{n})}
$$

Example: $f(x) = x^{2} - 3$ on $\mathbb{R}$. $\pm \sqrt{ 3 }$ are the roots of f.

$$
T(x) = x - \frac{x^2 - 3} { 2x} = \frac{1}{2} \left( x + \frac{3}{x} \right)
$$

$$
|T(x) - T(y)| = \frac{|x-y|}{2} \left|1 - \frac{3}{xy}\right| \leq \frac{|x-y|}{2}
$$
Hence by Banach Contraction principle we have a unique fixed point on the range $[\sqrt{ 3 },\infty )$

iii) (In the differential equation)
Let $g: A \subseteq \mathbb{R} \to \mathbb{R}$ such that g is continuous let us consider the following IVP

$$
\begin{cases}
f'(t) = \frac{df}{dt} = g(t,f(t)) \\ \\
f(t_{0}) = x_{0}
\end{cases} \hspace{5em} \text{(p)}

$$

**Theorem:** (Picard- Lindelof) Let g be a continuous function on a R = $\{ (t,x)| |t - t_{0}| \leq a, |x-x_{0}|\leq b \}$  and exists c >0 such that $|g(t,x)|\leq c$ $\forall (t,x) \in \mathbb{R}$. Also assume g is Lipschitz on the second variable i.e. $\exists k >0$ such that 
$$
|g(t,x) - g(t,y)| \leq k|x-y| \quad (t,x),(t,y) \in R
$$
Then (p) has a unique sol on some interval $[t_{0}-\beta,t_{0}+\beta ]$ where $\beta < min(a,\frac{b}{c}, \frac{1}{k})$
**Proof:** 
**Step 1**: Equivalent formulation as a integral equation

$$
f(t) = x_{0} + \int_{t_{0}}^{t}g(s,t(s))ds \hspace{3em} \text{(p')}
$$
Conversely any sol of (p) will be of this form

**Step 2**: Finding a complete space X and a map T
Denote J  = $[t_{0}-\beta,t_{0}+\beta ]$ and
$$
X = \{ f \in C(J) | f(t_{0}) = x_{0} , \sup_{t \in J}\left|x_{0}- f(t) \right|\leq c \beta  \}
$$


Define T on X by
$$
Tf(t) = x_{0} + \int_{to}^{t}g(s,f(s))ds
$$
Since X is a closed subspace of $(C(J),\rho_{\infty })$ , X is complete
**Step 3**:  $\underline{T:X\to X}$
$$
Tf(t_{0}) = x_{0}
$$
Also, 
$$
\begin{align*}
\sup_{t \in J} \lvert x_{0} - Tf(t) \rvert \leq & \sup_{t \in J}\int_{t_{0}}^{t}\lvert g(s,f(s))ds \rvert \\
\leq & c \sup_{t \in J} \int_{t_{0}}^{t}ds \leq c\beta 
\end{align*}
$$
So, $Tf \in X$

**Step 4**: T is a contraction
$\forall t \in [t_{0}-\beta,t_{0}+\beta]$ and $\forall f_{1},f_{2} \in X$ then
$$
\begin{align*}
\lvert Tf_{1}(t) - Tf_{2}(t) \rvert =& \left\lvert  \int_{t_{0}}^{t}[g(s,f_{1}(s)-g(s,f_{2}(s)))]ds  \right\rvert  \\
\leq & k\int_{t_{0}}^{t}\lvert f_{1}(s)-f_{2}(s) \rvert ds \quad \text{(By the Lipschitz cond.)} \\
\leq & k\sup_{s \in J}\int_{t_{0}}^{t}ds \\
\leq & \beta k \rho_{\infty}(f_{1},f_{2})
\end{align*}
$$
So,
$$
\rho_{\infty}(Tf_{1},Tf_{2}) = \sup_{t \in J} \lvert Tf_{1}(t)-Tf_{2}(t) \rvert \leq \beta K \rho_{\infty}(f_{1},f_{2})
$$
Since $\beta k < 1$, T is a contraction on X.
**Step 5**: (Conclusion)
T has a unique fixed point say f, So f is a unique solution of **(p')** and hence of **(p)** $\blacksquare$

**Corollary:** (Picard iteration)
**Proof:** The sol of (p) can be written as a limit of the following iterative sequence:
$$
\begin{cases}
f_{0}(t)=x_{0} \\
f_{n+1}(t) = x_{0} + \int_{t_{0}}^{t}g(s,f_{n}(s))ds & \forall n=0,1,\dots 

\end{cases}
$$

**Theorem:**(Baire Category Theorem) Let X be a complete metric space and $E_n$ be a sequence of dense open sets
$$
\bigcap_{n=1}^{\infty } E_{n} \quad \text{is also dense in X}
$$

**Proof:** Let $x \in X$ and $r >0$ , Consider $B(x,r)$ 
We will form a contracting sequence of closed sets $\{ \overline{B_{n}} \}$ 
such that $\overline{B_{n}} \subseteq E_{n},\forall n \in \mathbb{N}$ and $B(x,r) \supseteq \overline{B_{1}}$

Then using Cantor intersection , $\exists$ a point $x_{0} \in \bigcap \overline{B_{n}}$ 
in particular $x_{0} \in \overline{B_{1}}$ and hence $x_{0} \in B(x,r)$

Now for the construction, $E_{1}$ is dense, exists a point $x_{1} \in B(x,r) \cap E_{1}$
Since $B(x,r)\cap E_{1}$ is open , there exists $r_{1} < 1$ such that $\overline{B(x_{1},r_{1})} \subseteq B(x,r)\cap E_{1}$

Since $E_{2}$ is open dense, $\exists r_{2} < \frac{1}{2}$ and a point $x_{2}$ such that $\overline{B(x_{2},r_{2})} \subseteq B_{1} \cap E_{2}$
Continuing like this, we have, for any $n, \exists r_{n+1}< \frac{1}{n+1}$ and a point $x_{n+1}$ such that $\overline{B(x_{n+1},r_{n+1})} \subseteq B_{n} \cap E_{n+1}$

Applying Cantor intersection , $\exists$ a point $x_{0} \in \bigcap \overline{B_{n}} \subseteq \bigcap E_{n}$   and $x_{0} \in \overline{B_{1}}$ and hence $x_{0} \in B(x,r)$, hence $B(x,r) \cap \bigcap E_{n} \neq \varnothing$ hence x is a limit point of $\bigcap E_{n}$. Since $x \in X$ is arbitrary we have that $\bigcap E_{n}$ is dense in X. $\quad \blacksquare$

**Theorem:**(B.C.T Closed Set Version) Let X be a complete metric space X and $\{ F_{n} \}$ be a countable collection of nowhere dense closed subsets of X then $\bigcup_{n=1}^{\infty } F_{n}$ has no open ball inside it.

**Corollary:** Let X be complete and $\{ F_{n} \}$ be a countable collection of closed sets in X. If $\bigcup_{n=1}^{\infty} F_{n}$ has non-empty interior then at least one of $F_{n}$ has non-empty interior.

**Corollary:** Let X be complete and $\{ F_{n} \}$ be a sequence of closed sets. Then $\bigcup_{n=1}^{\infty}\partial F_{n}$ is nowhere dense in X.

**Theorem:**(A non-linear uniform boundedness theorem) Let X be a complete metric space and $F$ be family of continuous functions on X such that F is pointwise bounded, i.e. for every $x \in X$, $\{ f(x) | f \in F \}$ is bounded. Then $\exists$ a ball in X on which F is uniformly bounded.

**Proof:** For $n \in \mathbb{N}$ set,
$$
E_{n} := \{ x \in X | |f(x) \leq n \forall f\in F|\}
$$
Observe that $E_{n}$ is a closed set $\forall n \in \mathbb{N}$. Now, for any $x \in X$, $\exists n$ such that,
$$
|f(x)| \leq n \quad \forall f\in F
$$
Therefore, $X = \bigcup_{n=1}^{\infty}E_{n},\exists k \in \mathbb{N}$ such that $E_{k}$ has an interior point $x_{0}$. So $\exists r>0$ such that $B(x_{0},r) \subseteq E_{k}$, Hence
$$
|f(x)|\leq k \quad \forall f \in F \text{ and } x \in B(x_{0},r)
$$
Therefore, F is uniformly bounded on $B(x_{0},r)$ $\quad \blacksquare$

**Theorem:** Let X be a complete metric space and ${f_{n}}$ be a sequence of continuous functions which converges pointwise to a function $f$ on X. Then $\exists$ a dense subset D of X on which $\{ f_{n} \}$ is equicontinuous and f is continuous on D.

**Proof:** $\forall n,m \in \mathbb{N}$ we define,
$$
E_{m,n} := \left\{  x \in X \middle  |f_{j}(x) - f_{k}(x)|\leq \frac{1}{m}   \forall j,k\geq n\right\}
$$
Take, $D=X\setminus \bigcup_{n,m=1}^{\infty} \partial E_{n,m}$. So, D is dense in X. So, D is dense in X. Let $x_{0} \in X$ and $\epsilon>0$ arbitrary. $\{ f_{n}(x_{0}) \}$ is convergent and hence a Cauchy sequence. Let $m \in \mathbb{N}$ such that $\frac{1}{m} < \frac{\epsilon}{4}$. $\exists N \in \mathbb{N}$
$$
\lvert f_{j}(x_{0}) - f_{k}(x_{0}) \rvert  \frac{<1}{m} \quad \forall j,k \geq N
$$
So, $x_{0} \in E_{m,n}$. Hence, $x_{0} \in D \cap E_{m,n}$. $\exists r>0$ such that $B(x_{0},r) \subseteq E_{m,N}$. Since, $f_{N}$ is continuous at $x_{0}$, $\exists 0<\delta<r$ such that
$$
\lvert f_{N}(x_{0}) - f_{N}(x) \rvert < \frac{1}{m} \quad \forall x \in B(x_{0},\delta)
$$
So,$\forall x \in B(x_{0},\delta)$ and $\forall j\geq N$,
$$
\begin{align*}
\lvert f_{j}(x_{0}) -f_{j}(x) \rvert \leq & \lvert f_{j}(x_{0}) - f_{N}(x_{0}) \rvert + \lvert f_{N}(x_{0})-f_{N}(x) \rvert +\lvert f_{N}(x)-f_{j}(x) \rvert  \\
<& \frac{3\epsilon }{4}
\end{align*}
$$
So, $\{ f_{n} \}_{n=N}^{\infty}$ is equicontinuous at $x_{0}$, Since $\{ f_{1},\dots,f_{N-1} \}$ is equicontinuous at $x_{0}$, So $\{ f_{n} \}_{n=1}^{\infty}$ is equicontinuous.

Now taking $j\to \infty$,
$$
\lvert f(x_{0})-f(x) \rvert \leq \frac{3\epsilon}{4} < \epsilon \quad \forall x \in B(x_{0},\delta)
$$
So, F is continuous at $x_{0}$. Since $x_{0}\in D$ arbitrary we are done. $\quad \blacksquare$

**Def:** A normal linear space $(X,||\cdot||)$ is called a Banach space if X is complete with respect to the metric coming from the norm $||\cdot||$

**Theorem:** An infinite dimensional Banach space X can not have a (Hamel) basis which is countable.
	**Lemma:** Let Y be a proper subspace of a normed linear space $(X,||\cdot||)$ then $Y^{\circ} = \varnothing$ 
	**Proof:** If possible let y be an interior point of Y. Then, $\exists r>0$ such that $B(y,r) \subseteq Y$ implies $\implies B(0,r) = B(y,r) - y \subseteq Y$.
	Now, take $x \in X$, $\left\lvert \left\lvert  \frac{r}{2} \frac{x}{\lvert \lvert x \rvert \rvert}  \right\rvert   \right\rvert = \frac{r}{2} <r$.  
	So $\frac{r}{2} \frac{x}{\lvert \lvert x \rvert \rvert} \in Y$ implies $x \in Y$, So $X=Y$. $\quad \blacksquare$

**Proof:** (of the theorem)
Let $\{ x_{1},x_{2},\dots, \}$ be a countable basis of X. Define $Y_{m} := \text{span}\{ x_{1},\dots,x_{m} \},\forall m \in \mathbb{N}$. So $Y_{m}$ is closed.
$$
X = \bigcup_{m=1}^{\infty} Y_{m}
$$
Since $Y_{m}$ is a proper subspace of X, $Y_{m}^{\circ} = \varnothing$. But by BCT X cannot be a countable union of nowhere dense sets. $\quad \blacksquare$
## Schauder basis
Let X be a normed linear space A countable linearly independent set $\{ x_{1},x_{2},\dots \}$ is said to be a Schauder basis of X if $||x_{i}||=1$ $\forall i$ and,
$$
x = \sum_{i=1}^{\infty} \alpha_{i}x_{i} \quad\forall x \in X,\text{for some } \alpha_{i} \in \mathbb{R}
$$
i.e.
$$
\lim_{ n \to \infty } \left\lVert x - \sum_{i=1}^{n} \alpha_{i}x_{i} \right\rVert = 0
$$
See that, $\left\{  \sum_{i=1}^{\infty} \alpha_{i}x_{i}  \mid n \in \mathbb{N}, \alpha_{i} \in \mathbb{Q} \right\}$ form a dense subset of X. Therefore X is separable.
Remark: Not every normed linear space has a Schauder basis. Not every separable normed linear space has a Schauder basis. $\ell^{p},1\leq p\leq \infty$ as a Schauder basis, $\{e_{i}| e_{i}=(0,\dots,1,0,\dots ) \text{ at the ith position}\}$.
## Stone Weierstrass Theorem

**Def:**(Bernstein Polynomial): For a function $f$ on some set X, the nth Bernstein polynomial is
$$
B_{n}(x,f) = \sum_{k=0}^{n} f\left( \frac{k}{n} \right) \binom{n}{k} x^{k}(1-x)^{n-k} \quad \forall x \in [0,1]
$$

**Lemma:**  
1. $B_{n}(x,1)=1$ , $B(x,x)=x,B_{n}(x,x^{r})=\frac{x}{n}+ \frac{n-1}{n}x^{r} ,x \in [0,1]$ 
2. for  $f \leq g$,  $B_{n}(x,f)\leq B_{n}(x,g)$

**Proof:** $\forall x,y \in \mathbb{R}$
$$
(x+y)^{n} = \sum_{k=0}^{n} \binom{n}{k} x^{k}y^{n-k} \tag{i}
$$
Taking partial derivative w.r.t $x$ in the both side of (i) we have,
$$
n(x+y)^{n-1} = \sum_{k=0}^{n} k\binom{n}{k} x^{k-1}y^{n-k} \tag{ii}
$$
Now, multiply both sides by $\frac{x}{n}$
$$
x(x+y)^{n-1} = \sum_{k=0}^{n} \binom{n}{k}\left(\frac{k}{n}\right) x^{k}(1-x)^{n-k} 
$$
Again taking partial derivatives w.r.t x in both sides of (ii) we have,
$$
(x+y)^{n-1} + (n-1)x(x+y)^{n-2} = \sum_{k=0}^{n}k\left( \frac{k}{n}\right)\binom{n}{k}x^{k-1}y^{n-k}
$$
Again multiply by $\frac{x}{n}$ in both sides we have
$$
\frac{x}{n}(x+y)^{n-1} + \frac{n-1}{n}x^{2}(x+y)^{n-2} = \sum_{k=0}^{n}\left( \frac{k}{n}\right)^{2}\binom{n}{k}x^{k}y^{n-k} \tag{iii}
$$

Replacing y by $(1-x)$ in (i),(ii),(iii) we have,
$B_{n}(x,1),B_{n}(x,x)=x,B_{n}(x,x^{2}) = \frac{x}{n} + \frac{n-1}{n}x^{2}$
### Weierstrass Approximation Theorem
**Theorem:** Let $f \in C[a,b]$ . Then $\exists$ a seq of polynomial ${p_{n}}$ such that $p_{n} \to f$ uniformly on $[a,b]$.

**Proof:** Let $f \in C[0,1]$ so f is uniformly continuous, Given $\epsilon >0$ , $\exists \delta >0$ such that,
$$
\lvert f(x)-f(y) \rvert <\frac{\epsilon}{2} \quad \forall \lvert x-y \rvert <\delta 
$$
 Since,  f is bounded, $\exists M>0$ such that $\sup_{x \in[0,1]} |f(x)|\leq M$
 Also if $|x-y| \geq \delta$ then $(\frac{x-y}{\delta })^{2} \geq 1$ 

$$
\lvert f(x) - f(y) \rvert  \leq 2M\left( \frac{x-y}{\delta } \right)^{2} + \frac{\epsilon}{2}  \quad \forall x,y \in [0,1]
$$

Fix $\xi \in [0,1]$
$$
\begin{align*}
B_{n}(x,f-f(\xi)) = \sum_{k=0}^{n} (f- f(\xi))\left( \frac{k}{n} \right) \binom{n}{k} x^{k}(1-x)^{n-k} \\
= B_{n}(x,f) - f(\xi)B_{n}(x,1)=B_{n}(x,f)-f(\xi)
\end{align*}
$$
Aim to show, $\sup_{\xi \in [0,1]} \lvert B_{n}(\xi,f)- f(\xi) \rvert \to 0$

$$
\begin{align*}
\lvert B_{n}(x,f) - f(\xi) \rvert = |B_{n}(x,f-f(\xi)) \\
\leq B_{n}\left( x, \frac{2M}{\delta^{2}}  (x-\xi)^{2} + \frac{\epsilon}{2} \right) \\
=B_{n}\left( x,\frac{2M}{\delta^{2}}[x^{2} - 2x \xi + \xi^{2}] + \frac{\epsilon}{2} \right) \\
= \frac{2M}{\delta} (x-\xi)^{2} + \frac{2M}{\delta^{2}n}\left( x-x^{2} \right)+ \frac{\epsilon}{2} \hspace{4em} \text{(*)}
\end{align*}
$$


Putting $x = \xi$ in $(*)$ we have,
$$
\begin{align*}
|B_{n}(\xi,\delta )  - f(\xi)| \leq & \frac{2M}{\delta^{2}n}(\xi - \xi^{2}) + \frac{\epsilon}{2} \\
\leq \frac{2M}{\delta^{2}n} \frac{1}{4} + \frac{\epsilon}{2} \\
=& \frac{M}{2\delta^{2}n} + \frac{\epsilon}{2} \\
\end{align*}
$$

$$
\begin{cases}
\frac{M}{2\delta^{2}n < \frac{\epsilon}{4}}  & \text{if } n >  2\frac{M}{\delta^{2}\epsilon} \\
\text{ if } k \in \mathbb{N} > \frac{2M}{\delta^{2}\epsilon} &  \text{ then} \lvert B_{n}(\xi,f) - f(\xi)  \rvert \leq  \frac{\epsilon}{4}+ \frac{\epsilon}{2}=\frac{3\epsilon}{4}
\end{cases}
$$
So, $\sup_{\xi \in [0,1]}\lvert B_{n}(\xi,f)-f(\xi) \rvert < \epsilon, \forall n\geq k$

**Def:** A collection of real valued functions $\mathscr{A}$ on a set X is said to be an algebra if $\forall f,g \in \mathscr{A}, f+g, f\cdot g, cf \in \mathscr{A} \quad (c \in \mathbb{R})$  

**Def:** An algebra $\mathscr{A}$ of real valued function on a set X in said to be _uniformly closed_ if for every seq $\{ f_{n} \}$ converging uniformly to some $f, f\in \mathscr{A}$

Example: $C(X)$ X is compact is uniformly closed algebra

**Def:** A set $\mathscr{B}$ is said to be uniform closure of an algebra $\mathscr{A}$ of  real valued functions of X if $\mathscr{B}$ is the set of all uniform limits of $\mathscr{A}$

![[SVG/tikzdiagram18.svg|diagram]]


**Theorem:** A uniform closure $\mathscr{B}$ of an algebra $\mathscr{A}$ of bounded functions on a metric space X is a uniformly closed algebra

**Proof:** we will first show $\mathscr{B}$ in a algebra

Take $f,g \in \mathscr{B}$ Then $\exists \{ f_{n} \} , \{ g_{n} \} \subseteq \mathscr{A}$ such that
$$
\{ f_{n} \} \to f \text{ uniformly and } \{ g_{n} \} \to g \text{ uniformly}
$$


Since $f_{n} , g_{n}$ are bounded so are $f,g$ we need to prove $f +g \in \mathscr{B} , fg \in \mathscr{B}, cf \in \mathscr{B} (\forall c \in \mathbb{R})$

1) Given $\epsilon >0 \exists n_{1},n_{2} \in \mathbb{N}$ such that
$$
\begin{align*}
\lvert f_{n}(x) - f(x) \rvert  <\frac{\epsilon}{2} \\
\lvert g_{n}(x) - g(x) \rvert  <\frac{\epsilon}{2}
\end{align*}
$$

$\forall  n\geq \max \{n_{1},n_{2}\}$
$$
\lvert f_{n}(x) + g_{n}(x)-f(x)-g(x) \rvert < \frac{\epsilon}{2} + \frac{\epsilon}{2 } = \epsilon
$$
So $f+g \in \mathscr{B}$
$\exists M_{1},M_{2} >0$ such that $\lvert f(x) \leq M_{1} \rvert$ and $\lvert g(x) \leq M_{2} \rvert$ $\forall x \in X$
Since $\{ f_{n} \} \to f$ uniformly $\exists n_{0} \in \mathbb{N}$ such that
$$
\lvert  f_{n}(x) - f(x) \rvert <1 \quad \forall n\geq n_{0},\forall x \in X
$$
$$
\begin{align*}
\implies \lvert f_{n}(x) \rvert < & 1 + f(x) \quad \forall n\geq n_{0},\forall x \in X \\
\leq & 1 + M
\end{align*}
$$

Now, Given $\epsilon>0$ , $\exists n_{1},n_{2} \in \mathbb{N}$ such that
$$
\begin{align*}
\lvert f_{n}(x) - f(x) \rvert  <\frac{\epsilon}{2M_{2}}  \\
\lvert g_{n}(x) - g(x) \rvert  <\frac{\epsilon}{2(1+M_{1})}
\end{align*}
$$

$\forall n \geq \max \{ n_{0},n_{1},n_{2} \}$ and $\forall x \in X$
$$
\begin{align*}
\lvert f_{n}(x)g_{n}(x) - f(x)g(x) \rvert &\leq \lvert f_{n}(x) - f(x) \rvert \lvert g_{n}(x) \rvert + \lvert g_{n}(x) - g(x) \rvert \lvert f(x) \rvert  \\
&< \frac{\epsilon}{2M_{2}}(M_{2}) + \frac{\epsilon}{2(1+M_{1})}(1 + M_{1})  \\
&= \frac{\epsilon}{2} + \frac{\epsilon}{2} = \epsilon 
\end{align*}
$$
Therefore $\{ f_{n}g_{n} \} \to fg$ uniformly on X
iii) $cf \in \mathscr{B}$ (Clear!)

Hence $\mathscr{B}$ is an algebra. Now we will show that $\mathscr{B}$ is uniformly closed.
i.e. To prove if $\{ h_{n} \} \subseteq \mathscr{B} \to h$ uniformly on X then $h \in \mathscr{B}$

Given $\epsilon>0$, $\exists n_{1} \in \mathbb{N}$ such that
$$
\begin{align*}
\lvert h_{n}(x) - h(x) \rvert < \frac{\epsilon}{2} \quad \forall n \geq n_{1}, \forall x \in X
\end{align*}
$$

Now, since $h_{n} \in \mathscr{B}$ and $\mathscr{B}$ in the unifrom closure of $\mathscr{A}, \exists \{ h_{n,i} \}_{i=1}^{\infty} \subseteq \mathscr{A}$ such that $\{ h_{n,i} \} \to h_{n}$ uniformly i.e. $e\xi st i_{n} \in \mathbb{N}$ such that
$$
\begin{align*}
\lvert h_{n,i}(x) - h_{n}(x) \rvert < \frac{\epsilon}{2} \quad \forall i \geq i_{n}, \forall x \in X
\end{align*}
$$

Now, for $n \geq n_{1}, \forall x \in X$
$$
\begin{align*}
\lvert h_{n,i}(x) - h(x) \rvert &\leq \lvert h_{n,i}(x) - h_{n}(x) \rvert + \lvert h_{n}(x) - h(x) \rvert \\
\end{align*}
$$
So, $f \in \mathscr{B}$ and we are done

**Proposition:** Let $\mathscr{B}$ be a uniformly  closed algebra of bounded functions on some metric space X then if $f,g \in \mathscr{B}$ then $|f|, \max \{ f,g \}, \min \{ f,g \} \in B$
**Proof:**
Since $f \in \mathscr{B}$ is bounded . So $\exists M>0$ such that $f(x) \in [-M,M] \forall x \in X$ 

Now consider the function $|\cdot|: [-M,M] \to \mathbb{R}$. By Weierstrass approximation theorem, $\exists$ a polynomial $p$ such that $|p(x) - |x|| < \epsilon$ for all $x \in [-M,M]$

Now, $f \in \mathscr{B}$, $f^{n} \in \mathscr{B} \quad \forall n \in \mathbb{N}$ , $cf^{n} \in \mathscr{B}, \quad \forall n \in \mathbb{N}$

Then $p \circ f \in \mathscr{B}$, So $(*) \implies$ 
$$
\lvert p \circ f(x)- \lvert f(x) \rvert  \rvert  < \epsilon 
$$
Therefore $|f| \in \mathscr{B}$
Similarly, we can show $\max \{ f,g \}, \min \{ f,g \} \in \mathscr{B}$ by
$$
\begin{align*}
\max \{ f,g \} = \frac{1}{2} \left( f + g + |f-g| \right) \\
\min \{ f,g \} = \frac{1}{2} \left( f + g - |f-g| \right)
\end{align*}
$$
$\quad \blacksquare$

### Algebra, Uniformly closed algebra, Uniform Closure
**Def:** A collection $\mathscr{A}$ of real valued functions on a set X is said to separate points of X if $\forall x\neq y \in X, \exists f \in \mathscr{A}$ such that $f(x)\neq f(y)$.

**Def:** A collection $\mathscr{A}$ of real valued functions on X is said to vanish at no point of X if $\forall x \in X, \exists f_{x} \in \mathscr{A}$. such that $f_{x}(x) \neq 0$.

**Example**: $\mathbb{R}[x] \subseteq C(\mathbb{R})$ . So, $\mathbb{R}[x]$ separates points. Let $P(x)=1, \forall x \in X$. Hence it doesn't vanish at any point. Also $P(x) = x$. separates points. Hence polynomials are such a collection.
### Stone Weierstrass Theorem

**Theorem:** Let $\mathscr{A}$ be an algebra of real valued function on some metric space X such that
1. $\mathscr{A}$ does not vanish at any point of X.
2. $\mathscr{A}$ separates points.
Then, $\forall$ distinct $s,t \in X$ and $\forall c_{1},c_{2} \in \mathbb{R},\exists$ a function $g \in \mathscr{A}$ such that $g(s)=c_{1},g(t)=c_{2}$.

**Proof:** Since $\mathscr{A}$ does not vanish at any point of X, for $s,t, \exists h_{1},h_{2} \in \mathscr{A}$ such that
$$
h_{1}(s)\neq 0 \quad \& \quad h_{2}(t) \neq 0
$$
Also, since $\mathscr{A}$ separates points, $\exists h \in \mathscr{A}$ such that $h(s) \neq h(t)$. Now define
$$
\begin{align*}
g_{1}(x) = \frac{h(x)-h(t)}{h(s)-h(t)} \frac{h_{1}(x)}{h_{1}(s)}\\
g_{2}(x) = \frac{h(s)-h(x)}{h(s)-h(t)} \frac{h_{2}(x)}{h_{2}(t)}
\end{align*}
$$
So, 
$$
\begin{cases}
g_{1}(s) = 1 & g_{1}(t) = 0 \\
g_{2}(s)=0  & g_{2}(t)=1
\end{cases}
$$
Easy to see that $g_{1},g_{2}$ belongs to the algebra. Now take $g = c_{1}g_{1}+c_{2}g_{2}$. Then $g(s) = c_{1}$ and $g(t)=c_{2}$. $\quad \blacksquare$

**Theorem:**(Stone-Weierstrass) Let X be a compact metric space and $\mathscr{A}\subseteq C(X)$ be an algebra such that $\mathscr{A}$ vanishes at no point of X and $\mathscr{A}$ separates points of X. Then, the uniform closure of $\mathscr{A}$ is $C(X)$.

**Proof:** 
Let $\mathscr{B}$ be the uniform closure of $\mathscr{A}$. We will show that $\mathscr{A} = C(X)$. That is to prove for any $f \in C(X)$ and for each $\epsilon>0$, $\exists$ a function $g \in \mathscr{B}$ such that,
$$
\lvert g(x)-f(x) \rvert <\epsilon \quad \forall x \in X
$$
Since, $\mathscr{B}$ is the uniform closure we will be done. Take $\epsilon >0$. $\forall s\neq t \in X$, $\exists$ $g_{s,t} \in \mathscr{B}$ such that $g_{s,t}(s) = f(s), g_{s,t}(t) = f(t)$ from previous theorem.

Since, $g_{s,t} \in \mathscr{B}$, it is continuous. Now, fix $s \in X$. Since, $g_{s,t}$ is continuous $\exists$ a neighbourhood $U_{s,t}$ around $t$ such that,
$$
g_{s,t}(x) > f(x) - \epsilon \quad \forall x \in U_{s,t}
$$
$\{ U_{s,t} \}_{t \in X}$ is an open cover of X. Since X is compact it has a finite subcover $\{ U_{s,t} \}_{t=1}^{n}$. Take, $g_{s} = \max_{1\leq i\leq n} g_{s,t_{i}}$ . Then, by a previous proposition $g_{s} \in \mathscr{B}$. Also, 
$$
g_{s}(x)\geq g_{s,t_{i}}(x)>f(x)-\epsilon \quad \forall x \in U_{s,t} \forall i=1,\dots,n
$$
So, 
$$
g_{s}(x)>f(x)-\epsilon \quad \forall x \in  X \tag{*}
$$

Observe that $g_{s}(s) = \max g_{s,t_{i}}(s) = f(s) < f(s) + \epsilon$. Since $g_{s}$ is continuous. $\exists$ a neighbourhood $U_{s}$ around $s$ such that
$$
g_{s}(x) < f(x) + \epsilon \quad \forall x \in U_{s}
$$
$\{ U_{s} \}_{s \in X}$ is an open cover of X, Hence has a finite subcover $\{ U_{s} \}_{i=1}^{k}$. Now take,
$$
g = \min_{1\leq i\leq k} g_{s_{i}}
$$
Since $g_{s_{i}} \in \mathscr{B}, g \in \mathscr{B}$ for a similar reason as above. Also, 
$$
g(x) < f(x) + \epsilon \quad x \in X
$$
Since, g is the minimum of finite collection of $g_{s}$ from $(*)$ $g(x)>f(x)-\epsilon,\forall x \in X$. So, $\lvert g(x)-f(x) \rvert < \epsilon \quad \blacksquare$

**Corollary:** Let $K \subseteq \mathbb{R}^{n}$ be compact and $\mathscr{P}$ be the collection of all n-variable polynomials. Then $\mathscr{P}$ is uniformly dense in $C(K)$
**Proof:**
$p \in \mathscr{P}$ has the form $\sum a_{k_{1},k_{2},\dots,k_{n}} x_{1}^{k_{1}}\dots x_n^{k_n}$ . $\mathscr{P}$ is an algebra. Let $P_{j}: K \to \mathbb{R}$ be defined by 
$$
P_{i}(x_{1},\dots,x_{n}) = x_{j}
$$
It is clear that $P_{j}$ are continuous $\forall j = 1,\dots,n$ . Any polynomial $p \in \mathscr{P}$ can be written as a linear combination of product of some $P_{j}$. Hence $P \in C(K)$.

Take $x\neq y \in \mathbb{R}^{n}$ then its value must be different in atleast one coordinate say j, then $P_{j}$ separates $x,y$. Also since there are constant polynomials in $\mathscr{P}$ we have that $\mathscr{P}$ does not vanish at any point. Hence by Stone-Weierstrass we have that $\mathscr{P}$ is uniformly dense in $C(K)$

Remark: For a compact subset $K \subseteq \mathbb{R}^{2}$, $C(K)$ is separable choose coefficient of the polynomials from $\mathbb{Q}$ and apply the previous corollary.

**Corollary:** Let $\mathscr{A}$ be the collection of set of polynomials in $C[0,\pi]$ such that the polynomials have the following form.
$$
a_{0} + \sum_{n=1}^{N} a_{n} \cos nx + b_{n}\sin nx \quad \text{for some } a_{n},b_{n} \in \mathbb{R} \text{ and } N \in \mathbb{N}
$$
Then, $\mathscr{A}$ is uniformly dense in $C[a,b]$
**Proof:**
Using the formulas,
$$
\begin{align*}
\sin nx \sin mx &  = \frac{1}{2}[\cos(n-m)x - \cos(n+m)x] \\
\sin nx \cos mx  & = \frac{1}{2}[\sin(n+m)x - \sin(n-m)x] \\
\cos nx \cos mx &  = \frac{1}{2}[\cos (n+m)x + \cos (n-m)x]
\end{align*}
$$
We can check that $\mathscr{A}$ is an algebra in $C[0,\pi]$. If $x_{1}\neq x_{2} \in [0,\pi]$, then $\cos x_{1} \neq \cos x_{2}$. So $\mathscr{A}$ separates points. Since constants belong to $\mathscr{A}$ it does not vanish at any point on $[0,\pi]$. Hence we are done by Stone-Weierstrass theorem. $\quad \blacksquare$

**Theorem:** Let X be a compact metric space and $\mathscr{A} \subseteq C(X)$ be an algebra which satisfies all the hypothesis of the Stone-Weierstrass theorem. Then, for any $f \in C(X)$, $\exists$ a decreasing sequence of functions $\{ g_{n} \}$ which converges uniformly to $f$. 

**Proof:**
$\forall n \in \mathbb{N}$ we choose, $f_{n} = f(x) + \frac{2}{3^{n}}$. Since $f \in C(X), f_{n} \in C(X)$. By Stone-Weierstrass, $\exists \{ g_{k} \}$ which converge uniformly to $f_{n}$. Hence $\exists g_{n} \in \mathscr{A}$ such that
$$
\begin{align*}
 & \lvert g_{n}(x) - f_{n}(x) \rvert < \frac{1}{3^{n}} \quad \forall x \in X \\
 \implies &    -\frac{1}{3^{n}}   < g_{n}(x) - f_{n}(x) < \frac{1}{3^{n}} \\
\implies &  f_{n}(x) - \frac{1}{3^{n}} < g_{n}(x) < f_{n}(x)+ \frac{1}{3^{n}} \\
 & f(x) + \frac{1}{3^{n}} < g_{n}(x)<f(x) + \frac{1}{3^{n-1}} \quad (*) \\
\dots &  < g_{n+1}(x) < f(x) + \frac{1}{3^{n}} < g_{n}(x) < f(x) + \frac{1}{3^{n-1}} < g_{n-1}(x)<\dots
\end{align*}
$$
So, $\{ g_{n} \}$ is a decreasing sequence of functions. From $(*)$ we get that
$$
\lvert g_{n}(x) - f(x) \rvert < \frac{1}{3^{n-1}}\quad \forall x \in X
$$
that is $\{ g_{n} \}$ converges uniformly to $f$. $\quad \blacksquare$


**Theorem:** Let X be a compact metric space. Then $C(X)$ is separable.

**Proof:** 
We assume that $X$ has more than 1 point otherwise it is trivial.
Since $X$ is compact, $X$ is separable. That is $\exists$ a collection of points $Z=\{ z_{1},z_{1},\dots  \}$  such that $Z$ is dense in X. Define $f_{j}:X\to \mathbb{R},\forall j$ such that
$$
F_{j}(x) = \rho(x,z_{j}) \quad \forall x \in X 
$$
implies $f_{j}\in C(X), \forall j$. Now let
$$
K = \{ h \in C(X) \mid h \text{ is a product of finitely many }f_{j} \}
$$
Now take,
$$
\mathscr{A} = \left\{  g = \sum_{k=1}^{N}a_{k}h_{k} \middle| a_{k} \in \mathbb{R}, h_{k} \in K, N \in \mathbb{N}  \right\}
$$
$\mathscr{A} \subseteq C(X)$ is an algebra. Let $x_{0} \neq y_{0} \in X$ $\rho(x_{0},x_{0}) = 0$ and $\rho(x_{0},y_{0}) \neq 0$. Then $\exists z_{j} \in Z$ such that $\rho(x_{0},z_{j}) \neq \rho(y_{0},z_{j})$. So $f_{j}(x_{0}) \neq f_{j}(y_{0})$.

Since $x_{0} \neq y_{0}$ arbitrary we say $\mathscr{A}$ separates points. Take $x_{0} \in X$ then $\exists z_{j} \in Z$ such that $x_{0} \neq z_{j}$ i.e. $f_{j}(x_{0}) >0$. Hence $\mathscr{A}$ does not vanish at any point. So we can apply Stone-Weierstrass theorem to get that $\mathscr{A}$ is uniformly dense in $C(X)$. Therefore,
$$
S = \left\{  \sum_{k=1}^{n}q_{k}h_{k} \middle| q_{k} \in \mathbb{Q}, h_{k} \in K, n \in \mathbb{N}  \right\}
$$
S is also uniformly dense in $C(X)$ and it is countable, hence $C(X)$ is separable. $\quad \blacksquare$

### Korovkin's Theorem(1953)
**Theorem:** Let $f_{0}(x)=1,f_{2}(x)=x,f_{2}(x)=x^{2}$ be the function in $C[a,b]$ and $\{p_{n}\}$ be a sequence of positive linear maps from $C[a,b] \to C[a,b]$ such that
$$
\{p_{n}(f_{i})\}_{n=1}^{\infty } \to f_{i} \quad \text{uniformly } \forall i=0,1,2
$$
Then $\{ p_{n}(f) \}_{n=1}^{\infty } \to f$ uniformly $\forall f \in C[a,b]$
**Proof:**
$f \in C[a,b]$. Then f is uniformly continuous and given $\epsilon>0$, $\exists$ $\delta>0$ such that
$$
|f(x)-f(y)| <\epsilon \quad \forall |x-y| < \epsilon
$$
If $|x-y| \leq \delta$ , $\implies (x-y)^{2}\geq\delta^{2}$. Also since $f \in C[a,b]$, f is bounded. i.e. $\exists M>0$ such that $|f(x)|\leq M ,\forall x \in [a,b]$ 
$\forall |x-y| <\delta$,
$$
|f(x)-f(y)|\leq \frac{2M(x-y)^{2}}{\delta^{2}}
$$
So, $\forall x,y \in [a,b]$
$$
|f(x)-f(y)| \leq \frac{2M(x-y)^{2}}{\delta^{2}} + \epsilon \tag{*}
$$
For a $y \in [a,b]$, Take, $f_{y}(x) = (x-y)^{2}$

Then $(*)$ implies,
$$
-\epsilon - \frac{2M}{\delta^{2}}f_y(x) < f(x) - f(y) < \frac{2M}{\delta^{2}}f_{y}(x) + \epsilon 
$$
We can check,
$$
\begin{align*}

-\epsilon p_{n}(f_{0}) - \frac{2M}{\delta^{2}}p_{n}(f_{y}) <& p_{n}(f)(x) - f(y) p_{n}(f_{0})(y)  \\
\leq& \frac{2M}{\delta^{2}}p_{n}(f_{y})(y)+\epsilon p_{n}(f_{0})(y) 
\end{align*}
\tag{***}
$$
Now,
$$
\begin{align*}
p_{k}(f_{y})(y) &= p_{k}(x^{2}-2xy+y^{2})(y) \\
&= p_{k}(f^{2})(y) - 2yp_{k}(f_{1}(y)) + p_{k}(f_{2})(y)  \\
&\to y^{2} - 2y^{2} + y^{2} = 0
\end{align*}
$$

Since $\{ p_{k}(f_{0})(y) \} \to 1$ uniformly $\forall y \in [a,b]$, by $(* * *)$ 

$$
\{ p_{k}(y) \}_{n=1}^{\infty} \to f(y) \quad \text{uniformly } \forall y \in [a,b]
$$
i.e. ${p_{k}(f)}_{k=1}^{\infty} \to f$ uniformly.

## Measure Theory

 **Def:** A collection $\mathscr{A} \subseteq \mathscr{P}(X)$ is called an algebra if
 1. $\mathscr{A}$ is closed under finite union.
 2. whenever $E \in \mathscr{A}$, $E^{c} \in \mathscr{A}$.

Remark: 
1. $\varnothing, X \in \mathscr{A}$
2. $\mathscr{A}$ is closed under finite intersection.
**Def:** An algebra $\mathscr{A}\subseteq \mathscr{P}(X)$ is called a $\sigma$-algebra if $\mathscr{A}$ is closed under countable union.

Example: 
1. $\mathscr{P}(X)$
2. $\{ \varnothing ,X\}$
3. $\mathscr{A} = \{ E \in \mathscr{P}(X) \mid \text{where} \text{ E is countable or } E^{c} \text{ is countable}\}$

**Def:** Let $S \subseteq \mathscr{P}(X)$. Then the smallest $\sigma$-algebra containing $S$ is called the $\sigma$-algebra generated by $S$, denoted by $M(S)$

**Lemma:** Let $S,F \subseteq \mathscr{P}(X)$ and $S\subseteq M(F)$, Then $M(S)\subseteq M(F)$

**Proof:** Trivial
### Borel sigma-algebra

**Def:**(Borel -algebra) Let X be a topological space and $S$ be the collection of all open sets of X. The $\sigma$-algebra generated by $S$ in the Borel $\sigma$-algebra on X. We denote it by $\mathscr{B}_{X}$.
So, $\mathscr{B}_{X}$ includes atleast the following sets,
1. All open subsets of X
2. All closed subsets of X
3. countable union of closed sets
4. countable intersection of open sets

**Proposition:** $\mathscr{B}_{\mathbb{R}}$ is generated by any of the following collections
1. $S_{1} = \{ (a,b)|a<b \}$
2. $S_{2}=\{ [a,b] \}$
3. $S_{3}= \{ (a,b] \}$
4. $S_{4}=\{ [a,b) \}$
5. $S_{5}=\{(-\infty,a)\}$
6. $S_{6}= \{ (a,\infty ) \}$
7. $S_{7}=\{ (-\infty,a] \}$
8. $S_{8}=\{ [a,\infty ) \}$

**Proof:**
Let S be the collection of all open sets of $\mathbb{R}$. $S_{1} \subseteq S \implies M(S_{1}) \subseteq M(S)= \mathscr{B}_{\mathbb{R}}$. $S \subseteq M(S_{1}) \implies M(S)\subseteq M(S_{1})$ Since open intervals are a countable basis for $\mathbb{R}$ .

### Measure spaces

**Def:** Let M be a $\sigma$-algebra on a set X. A function $\mu : M \to [0,\infty]$ is said to be a measure if
1. $\mu(\varnothing) = 0$
2. If $\{  E_{i} \}$ is a disjoint collection of sets in $M$ then:
$$
\mu\left( \bigcup_{i=1}^{\infty } E_{i} \right) = \sum_{i=1}^{\infty } \mu(E_{i})
$$
$(X,M,\mu)$ is called a measure space. Elements of M are called measurable sets.

**Def:** 
1. $(X,M,\mu)$ is a finite measure space if $\mu(X)<\infty$
2. $(X,M,\mu)$ is said to be a $\sigma$-finite measure space if $\exists$ a disjoint collection $\{ E_{i} \}_{i=1}^{\infty} \subseteq M$ such that $X = \bigcup_{i=1}^{\infty} E_{i}$  and $\mu(E_{i}) < \infty$.

**Examples**: add some examples of measures #addexample 

**Theorem:** Let $\mu$ be a measure on $M$ then,
1. (monotonicity) if $E,F \in M$ and $E \subseteq F$ then
$$
\mu(E) \leq \mu(F)
$$
2. (countable subaddition) If $\{ E_{i} \} \subseteq M$ then,
   $$
   \mu\left( \bigcup E_{i} \right) \leq \sum_{i=1}^{\infty} \mu(E_{i})
   $$
3. (continuity from below) If $E_{1} \subseteq E_{2} \subseteq\dots$ and $E_{i} \in M$ then,
   $$
   \mu\left( \bigcup_{i=1}^{\infty } E_{i} \right) = \lim_{ n \to \infty } \mu (E_{n})
   $$
4. (continuity from above) If $E_{1} \supseteq E_{2} \supseteq\dots$ and $E_{i} \in M$ then,
   $$
   \mu\left( \bigcap_{i=1}^{\infty } E_{i} \right) = \lim_{ n \to \infty } \mu (E_{n})
   $$


**Proof:** 
1. $F=E \bigcup (F \setminus E) \implies \mu(F) = \mu(E) + \mu(F\setminus E) \geq \mu(E)$
2. 
$$
\begin{gather*}
F_{1} := E_{1} \\
F_{2}:=E_{2}\setminus E_{1} \\
\vdots \\
F_{k} := E_{k} \setminus \left( \bigcup_{i=1}^{k-1} E_{i} \right)
\end{gather*}
$$
$$
\bigcup F_{k} = \bigcup E_{k}
$$
and $\{ F_{k} \}$ is a disjoint family in $M$. So,
$$
\mu\left( \bigcup E_{k} \right) = \mu\left( \bigcup F_{k} \right) = \sum_{}^{} \mu(F_{k}) \leq \sum_{}^{}\mu(E_{k})
$$
3.  Let $E_{0}=\varnothing$, we have
   $$
   \begin{align*}
\mu\left( \bigcup E_{i} \right) = &  \mu\left( \bigcup(E_{i}\setminus E_{i-1}) \right) \\
 = &  \sum_{}^{ } \mu(E_{i}\setminus E_{I-1}) \\
=  & \lim_{ n \to \infty } \sum_{i=1}^{n} \mu(E_{i}\setminus E_{i-1}) \\
=  & \lim_{ n \to \infty } \mu\left( \bigcup_{i=1}^{n}(E_{i}\setminus E_{i-1}) \right) \\
=  &  \lim_{ n \to \infty } \mu(E_{n})
\end{align*}
$$

4. Define $F_{i} = E_{i}\setminus E_{i} \forall i$ 
   $$
F_{1} \subseteq F_{2} \subseteq F_{3} \subseteq\dots 
$$
$$
\mu(F_{1}) = \mu(E_{1}) - \mu(E_{i})
$$
So, $\mu(E_{1}) = \mu(F_{i}) + \mu(E_{i})$ , hence
$$
\mu\left( \bigcup F_{i} \right) = \lim_{ n \to \infty } [\mu(E_{i}) - \mu(E_{n})] 
$$
Also,  $\bigcup F_{i} = E_{1} \setminus \bigcap E_{i}$, $\implies \mu\left( \bigcup F_{i} \right) + \mu\left( \bigcap E_{i} \right) = \mu(E_{1})$. So from $(*)$,
$$
\begin{gather*}
\mu(E_{1}) - \mu\left( \bigcap E_{i} \right) = \mu(E_{1}) - \lim_{ n \to \infty } \mu(E_{n}) \\
\implies \mu\left( \bigcap E_{i} \right) = \lim_{ n \to \infty } \mu(E_{n}) \quad \text{(Since $\mu(E_{1}) < \infty $)}
\end{gather*}
$$
Instead of $\mu(E_{1})<\infty$ if we assume $\mu(E_{n})<\infty$ for some $n \in \mathbb{N}$. Then also $(iv)$ is true.

**Def:** $E \in M$ is said to be a null set (measure zero) if $\mu(E) = 0$. If a property holds on $X$ except a set of measure zero then we say that the property holds almost everywhere on $X$.

>[!info]
>$f = g$ on $E^{c}$ where $\mu(E)=0$, $\mu$ is some measure then we say $f=g \text{ a.s}$

**Def:** Let $(X,M,\mu)$ be a measure space $\mu$ is said to be complete measure if whenever $F \subset N$ and $\mu (N) = 0$ then $F \in M$.

**Theorem:** Let $(X,M,\mu)$ be a measure space. Define,
$$
\overline{M} = \left\{  E \cup F | E \in M \text{ and } F \subset N, \text{where N is a null set}   \right\}
$$
Then, $\overline{M}$ is a $\sigma$-algebra and there is an extension of $\mu$ to $\overline{M}$, say $\bar{\mu}$ such that $\bar{\mu}$ is a complete measure.

**Proof:** 
$$
\bigcup (E_{i} U F_{i}) = \left( \bigcup E_{i} \right) \cup \left( \bigcup F_{i} \right)
$$
The first term in the RHS in in $M$ while the other is a null set, so we have $\bigcup (E_{i} \cup F_{i}) \in \overline{M}$

We have to check for $E \in M, F \in N$, if $E \cup F \in \overline{M}$ then $(E \cup F)^{c} \in \overline{M}$. We can always assume $E \cap N = \varnothing$,
$$
E \cup F = E \cup (F\setminus E) \quad \text{Now $E \cap (N\setminus E)=\varnothing$}
$$
$$
\begin{align*}
E\cup F = & (E \cup N) \setminus (N \setminus F) \\
= & (E \cup N) \cap [(N \cap F^{c})]^{c} = (E \cup N) \cap (F \cup N^{c}) \\
(E \cup F)^{c} = & (E \cup N)^{c} \cup (N \cap F^{c})
\end{align*}
$$
So, $\overline{M}$ is a $\sigma$-algebra. Define $\bar{\mu}(E \cup F) = \mu(E), \forall E\cup F \in \overline{M}$
**Well definedness of $\bar{\mu}$**:
Let $E_{1} \cup  F_{1} = E_{2} \cup F_{2}$, where the $E_{i},F_{i}$ are from there their usual collections, $E_{1} \subseteq E_{2} \cup F_{2}, E_{2} \cup N_{2}$, Hence we have $\mu(E_{1}) \leq \mu(E_{2})+\mu(N_{2}) = \mu(E_{2})$, Similarly we get the other direction. We can also easily check it is measure also.

### Outer measure
**Def:** Let $X$ be a set. A function $\mu^{*}:\mathscr{P}(X) \to [0,\infty]$ is called an outer measure if
1. $\mu^{*}(\varnothing) = 0$
2. if $A \subseteq B$ then $\mu^{*}(A)\leq \mu^{*}(B)$
3. $\mu^{*}$ is countably subadditive i.e. $\mu\left( \bigcup E_{i} \right)\leq \sum_{i=1}^{\infty} \mu (E_{i})$

**Proposition:** Let $\mathscr{E} \subseteq \mathscr{P}(X)$ and $p:\mathscr{E} \to [0,\infty]$ such that $\varnothing,X \in \mathscr{E}$ and $p(\varnothing)=0$. Define $\forall E \subset X$ 
$$
\mu^{*}(E) = \inf \left\{  \sum_{i=1}^{\infty} p(E_{i}) \mid E  \subset \bigcup_{i=1}^{\infty} E_{i}, E_{i} \in \mathscr{E}    \right\}
$$
Then, $\mu^{*}$ is an outer measure of $X$.

**Proof:** 
The definition of $\mu^{*}$ make sense, $\mu^{*}(\varnothing) = 0$. $\mu^{*}(A) \leq \mu^{*}(B)$ when $A\subseteq B$. Let $\{ A_{i} \} \subseteq \mathscr{P}(X)$ we need to show,
$$
\mu^{*}\left( \bigcup_{_{i=1}}^{\infty} A_{i} \right) \leq \sum_{i=1}^{\infty} \mu^{*}(A_{i})
$$
Let $\varepsilon>0$. For each $i \in \mathbb{N}, \exists \{ E_{i,k}\}_{k=1}^{\infty}$ such that
$$
\sum_{ki=1}^{\infty} p(E_{i,k}) \leq \mu^{*}(A_{i}) + \frac{\varepsilon}{2^{i}}
$$
$$
\begin{gather*}
\implies \sum_{i=1}^{\infty}\sum_{k=1}^{\infty}p(E_{i,k}) \leq \sum_{i=1}^{\infty}\mu^{*}(A_{i}) + \varepsilon\left( \frac{1}{2} + \frac{1}{2^{2}} +\dots  \right) \\
\implies \mu^{*}\left( \bigcup_{i=1}^{\infty } A_{i} \right) \leq \sum_{i=1}^{\infty}\sum_{k=1}^{\infty}p(E_{i,k}) \leq \sum_{i=1}^{\infty } \mu^{*}(A_{i}) + \varepsilon 
\end{gather*}
$$

Since $\varepsilon$ is arbitrary, we have,
$$
\implies \mu^{*}\left( \bigcup_{i=1}^{\infty} A_{i} \right) \leq \sum_{i=1}^{\infty} \mu^{*}(A_{i})
$$
$\quad \blacksquare$

**Def:** Let $\mu^{*}$ be an outer measure on $X$. A subset $A \subseteq X$ is said to be $\mu^{*}$-measurable if
$$
\mu^{*}(E) = \mu^{*} (E \cap A) + \mu^{*}(E \cap A^{*}) \quad \forall E \subseteq X
$$
**Theorem:**(Caratheodory's Theorem) Let $\mu^{*}$ be an outer measure on $X$ and $M$ be the collection of all $\mu^{*}$-measurable sets. Then $M$ is a $\sigma$-algebra and $\mu^{*}$ is a measure on $M$

**Proof:**
