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
2. C[0,1] 
3. For compact metric space consider C(X) = $\{ f:X\to \mathbb{R}| \text{cont on X} \}$ with sup norm
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
Let us assume dim Y = 1

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
$|| z^{(p)} - z^{(p)}|| = || (y^{p}-y^{m}) + \alpha_{n}^{(p)}x_{n} - \alpha_{n}^{(m)}x_{n}||$
$$
= |\alpha_{m} - \alpha_{n}| || \frac{1}{|\alpha_{n}^{(p)}-\alpha_{n}^{(m)}|}(y^{(p)}-y^{(m)}) - x_{n}||
$$
$$
\geq |\alpha_{n}^{p} - \alpha_{n}^{m}| \text{dist}(x_{n,Y})
$$

since {z^(p)} is Cauchy for given $\epsilon>0$.
we have {$\alpha$} is Cauchy in $\mathbb{R}$


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
\begin{align}
\text{dist}(x_{r},Y) \leq & ||x_{r}-0|| \quad 0 \in Y \\
& ||x_{r}|| \\
&=1
\end{align}
$$
$$
\begin{align}
\text{dist}(x_{r},Y) =& \text{ dist}\left( \frac{x-y}{||x-y||},Y\right) \\
=&\frac{1}{||x-y||}\text{dist}(x-y,||x-y||Y) \\
=&\frac{1}{||x-y||} \text{dist}(x-y,Y) \\
=&\frac{1}{||x-y||}\text{dist}(X,Y) \\
\geq & \quad r \hspace{10em} \blacksquare  \\
 
\end{align}
$$



**Theorem**: Let $(X,||\cdot ||)$ be a infinite dimensional space. Let $B(0,1) = \{x \in X| ||x|| \leq  1\}$ be the closed unit ball in X. Then $B(0,1)$ is not compact.

**Proof**: let $\{ x_{1},x_{1},x_{3},\dots  \}$ be an infinite linearly independent set 
Define Zn : Span{$x_{1},x_{2},\dots,x_{n}$}
$Z_{1} \subset Z_{2} \subset \dots$
$Z_{n}$ are closed. for all n

By Riesz lemma we can choose $z_{n} \in Z_{n}$  such that $dist(z_{n},Z_{n-1}) > \frac{1}{2}$  then we can get that there cannot be any convergent subsequence in $\{ z_{n} \}$ hence X is not sequentially compact hence X is not compact.


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
\begin{align}
|f_{n}(x) - f_{m}(x) | &\leq |f_{n}(x)-f(x) + f(x) - f_{m}(x)|
\\ &\leq |f_{n}(x) - f(x)| + |f_{m}(x) - f(x)|  \\
&< \epsilon
\end{align}
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
\begin{align}
\{f_{1,n}\} &= f_{1,1} ,f_{1,2},\dots,f_{1,k} \\
\{f_{2,n}\} &= f_{2,1},f_{2,2},\dots,f_{2,k} \\
\vdots & \\ 
\{f_{m,n}\} &= f_{m,1},f_{m,2},\dots,f_{m,k}

\end{align}
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
\begin{align}
\lvert g_{n}(x) - g_{m}(x)\rvert \leq &\lvert g_{n}(x) - g_{n}(s) \rvert +& \\ 
& \lvert g_{n}(s) - g_{m}(s) \rvert +&  \\
&\lvert g_{m}(s)-g_{m}(x) \rvert   \\
\leq &\frac{\epsilon}{3} + \frac{\epsilon}{3} + \frac{\epsilon}{3} \\
=& \epsilon
\end{align}

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
**Theorem:** (Banach Contraction Principle) Let X be a complete metric space and $T:X\to X$ be a contraction then T has a  unique fixed point.

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
\begin{align}
\sup_{t \in J} \lvert x_{0} - Tf(t) \rvert \leq & \sup_{t \in J}\int_{t_{0}}^{t}\lvert g(s,f(s))ds \rvert \\
\leq & c \sup_{t \in J} \int_{t_{0}}^{t}ds \leq c\beta 
\end{align}
$$
So, $Tf \in X$

**Step 4**: T is a contraction
$\forall t \in [t_{0}-\beta,t_{0}+\beta]$ and $\forall f_{1},f_{2} \in X$ then
$$
\begin{align}
\lvert Tf_{1}(t) - Tf_{2}(t) \rvert =& \left\lvert  \int_{t_{0}}^{t}[g(s,f_{1}(s)-g(s,f_{2}(s)))]ds  \right\rvert  \\
\leq & k\int_{t_{0}}^{t}\lvert f_{1}(s)-f_{2}(s) \rvert ds \quad \text{(By the Lipschitz cond.)} \\
\leq & k\sup_{s \in J}\int_{t_{0}}^{t}ds \\
\leq & \beta k \rho_{\infty}(f_{1},f_{2})
\end{align}
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

## Schauder basis


### Stone Weierstrauss Theorem

**Def:**(Bernstein Polynomial)

**Lemma:**  
1. $B_{n}(x,1)=1$ , $B(x,x)=x,B_{n}(x,x^{r})=\frac{x}{n}+ \frac{n-1}{n}x^{r} ,x \in [0,1]$ 
2. for  $f \leq g$ $B_{n}(x,f)\leq B_{n}(x,g)$

**Proof:** $\forall x,y \in \mathbb{R}$
$(x+y)^{n}$ = $\sum_{k=0}^{n} $

### Weierstrauss Approximation Theorem
**Theorem:** Let $f \in C[a,b]$ . Then $\exists$ a seq of polynomial ${p_{n}}$ such that $p_{n} \to f$ uniformly on $[a,b]$.

**Proof:** Let $f \in C[0,1]$ so f is uniformly continuous, Given $\epsilon >0$ , $\exists \delta >0$ such that,
$$
\lvert f(x)-f(y) \rvert \frac{<\epsilon}{2} \quad \forall \lvert x-y \rvert <\delta 
$$
 Since,  f is bounded, $\exists M>0$ such that $\sup_{x \in[0,1]} |f(x)\leq M$
 Also if $|x-y| \geq \delta$ then $(\frac{x-y}{\delta })^{2} \geq 1$

$$
\lvert f(x) - f(y) \rvert  \leq 2M\left( \frac{x-y}{\delta } \right)^{2} + \frac{\epsilon}{2} ) \quad \forall x,y \in [0,1]
$$

Fix $\xi \in [0,1]$
$$
\begin{align}
B_{n}(x,f-f(\xi)) = \sum_{k=0}^{n} (f- f(\xi))\left( \frac{k}{n} \right) \binom{n}{k} x^{k}(1-x)^{n-k} \\
= B_{n}(x,f) - f(\xi)B_{n}(x,1)=B_{n}(x,f)-f(\xi)
\end{align}
$$
Aim to show, $\sup_{\xi \in [0,1]} \lvert B_{n}(\xi,f)- f(\xi) \rvert \to 0$

$$
\begin{align}
\lvert B_{n}(x,f) - f(\xi) \rvert = |B_{n}(x,f-f(\xi)) \\
\leq B_{n}\left( x, \frac{2M}{\delta^{2}}  (x-\xi)^{2} + \frac{\epsilon}{2} \right) \\
=B_{n}\left( x,\frac{2M}{\delta^{2}}[x^{2} - 2x \xi + \xi^{2}] + \frac{\epsilon}{2} \right) \\
= \frac{2M}{\delta} (x-\xi)^{2} + \frac{2M}{\delta^{2}n}\left( x-x^{2} \right)+ \frac{\epsilon}{2} \hspace{4em} \text{(*)}
\end{align}
$$


Putting $x = \xi$ in $(*)$ we have,
$$
\begin{align}
|B_{n}(\xi,\delta )  - f(\xi)| \leq & \frac{2M}{\delta^{2}n}(\xi - \xi^{2}) + \frac{\epsilon}{2} \\
\leq \frac{2M}{\delta^{2}n} \frac{1}{4} + \frac{\epsilon}{2} \\
=& \frac{M}{2\delta^{2}n} + \frac{\epsilon}{2} \\
\end{align}
$$

$$
\begin{cases}
\frac{M}{2\delta^{2}n < \frac{\epsilon}{4}}  & \text{if } n > 2\frac{M}{\delta^{2}\epsilon} \\
\text{ if } k \in \mathbb{N} > \frac{2M}{\delta^{2}\epsilon} &  \text{ then} \lvert  \rvert 
\end{cases}
$$
#incomplete 

**Def:** A collection of real valued functions $\mathscr{A}$ on a set X is said to be an algebra if $\forall f,g \in \mathscr{A}, f+g, f\cdot g, cf \in \mathscr{A} \quad (c \in \mathbb{R})$  

**Def:** An algebra $\mathscr{A}$ of real valued function on a set X in said to be uniformly closed if for every seq $\{ f_{n} \}$ converging uniformly to some $f, f\in \mathscr{A}$

Example: $C(X)$ X is compact is uniformly closed algebra

**Def:** A set $\mathscr{B}$ is said to be uniform closure of an algebra $\mathscr{A}$ of  real valued functions of X if $\mathscr{B}$ is the set of all uniform limits of $\mathscr{A}$

![[SVG/tikz1755255127.190391.svg|diagram]]


**Theorem:** A uniform closure $\mathscr{B}$ of an algebra $\mathscr{A}$ of bounded functions on a metric space X is a uniformly closed algebra

**Proof:** we will first show $\mathscr{B}$ in a algebra

Take $f,g \in \mathscr{B}$ Then $\exists \{ f_{n} \} , \{ g_{n} \} \subseteq \mathscr{A}$ such that
$$
\{ f_{n} \} \to f \text{ uniformly and } \{ g_{n} \} \to g \text{ uniformly}
$$


Since $f_{n} , g_{n}$ are bounded so are $f,g$ we need to prove $f +g \in \mathscr{B} , fg \in \mathscr{B}, cf \in \mathscr{B} (\forall c \in \mathbb{R})$

1) Given $\epsilon >0 \exists n_{1},n_{2} \in \mathbb{N}$ such that
$$
\begin{align}
\lvert f_{n}(x) - f(x) \rvert  <\frac{\epsilon}{2} \\
\lvert g_{n}(x) - g(x) \rvert  <\frac{\epsilon}{2}
\end{align}
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
\begin{align}
\implies \lvert f_{n}(x) \rvert < & 1 + f(x) \quad \forall n\geq n_{0},\forall x \in X \\
\leq & 1 + M
\end{align}
$$

Now, Given $\epsilon>0$ , $\exists n_{1},n_{2} \in \mathbb{N}$ such that
$$
\begin{align}
\lvert f_{n}(x) - f(x) \rvert  <\frac{\epsilon}{2M_{2}}  \\
\lvert g_{n}(x) - g(x) \rvert  <\frac{\epsilon}{2(1+M_{1})}
\end{align}
$$

$\forall n \geq \max \{ n_{0},n_{1},n_{2} \}$ and $\forall x \in X$
$$
\begin{align}
\lvert f_{n}(x)g_{n}(x) - f(x)g(x) \rvert &\leq \lvert f_{n}(x) - f(x) \rvert \lvert g_{n}(x) \rvert + \lvert g_{n}(x) - g(x) \rvert \lvert f(x) \rvert  \\
&< \frac{\epsilon}{2M_{2}}(M_{2}) + \frac{\epsilon}{2(1+M_{1})}(1 + M_{1})  \\
&= \frac{\epsilon}{2} + \frac{\epsilon}{2} = \epsilon 
\end{align}
$$
Therefore $\{ f_{n}g_{n} \} \to fg$ uniformly on X
iii) $cf \in \mathscr{B}$ (Clear!)

Hence $\mathscr{B}$ is an algebra. Now we will show that $\mathscr{B}$ is uniformly closed.
i.e. To prove if $\{ h_{n} \} \subseteq \mathscr{B} \to h$ uniformly on X then $h \in \mathscr{B}$

Given $\epsilon>0$, $\exists n_{1} \in \mathbb{N}$ such that
$$
\begin{align}
\lvert h_{n}(x) - h(x) \rvert < \frac{\epsilon}{2} \quad \forall n \geq n_{1}, \forall x \in X
\end{align}
$$

Now, since $h_{n} \in \mathscr{B}$ and $\mathscr{B}$ in the unifrom closure of $\mathscr{A}, \exists \{ h_{n,i} \}_{i=1}^{\infty} \subseteq \mathscr{A}$ such that $\{ h_{n,i} \} \to h_{n}$ uniformly i.e. $e\xi st i_{n} \in \mathbb{N}$ such that
$$
\begin{align}
\lvert h_{n,i}(x) - h_{n}(x) \rvert < \frac{\epsilon}{2} \quad \forall i \geq i_{n}, \forall x \in X
\end{align}
$$

Now, for $n \geq n_{1}, \forall x \in X$
$$
\begin{align}
\lvert h_{n,i}(x) - h(x) \rvert &\leq \lvert h_{n,i}(x) - h_{n}(x) \rvert + \lvert h_{n}(x) - h(x) \rvert \\
\end{align}
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
\begin{align}
\max \{ f,g \} = \frac{1}{2} \left( f + g + |f-g| \right) \\
\min \{ f,g \} = \frac{1}{2} \left( f + g - |f-g| \right)
\end{align}
$$
$\quad \blacksquare$
