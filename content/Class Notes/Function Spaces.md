---
title: Function Spaces
tags:
  - incomplete
created: 2025-07-25
publish: true
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

**Def**: Let $(X,\rho)$ $(\gamma,\sigma)$ be metric spaces and $f:X\to Y$ be a function. Then F is said to be continuous at $x \in X$ if for every $\epsilon > 0$, $\exists \delta >0$

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

**Def**: Let $(X,\rho)$ be a metric space and $\{ x_{n} \} \subseteq X$ is said to be _Cauchy sequence_ if for $\forall \epsilon > 0$ $\exists k_{\epsilon} \in \mathbb{N}$ such that
$$
\rho (x_{n},x_{m}) < \epsilon \quad \forall n,m \geq k_{\epsilon }
$$
$(X,\rho)$ is said to be _complete_ if every Cauchy sequence converges to a point in X.

Example: 
1. $\mathbb{R},\mathbb{R}^{n}$
2. Any closed interval in $\mathbb{R}$ is complete

**Proposition**: Let $(X,\rho )$ be a complete metric space then closed set $\iff$ complete set.

**Def**: Let $(X,\rho)$ be a metric space and $E\subseteq X$ then $\text{diam}(E)$ is $\sup_{x,y \in E} \rho(x,y)$, $E$ is said to be bounded in the supremum is finite.
$\{E_{i}\}_{i \in \mathbb{N}}$ is a decreasing sequence of non-empty subsets of E is said to be contracting if $\text{diam} E_{n}\to 0$ as $n\to \infty$

**Theorem**: (Cantor Intersection) Let $(X,\rho)$ be a metric space, and X is complete iff whenever ${F_{i}}$ is a decreasing sequence of non empty closed contracting subsets of X, $\bigcap  F_{i}$ contains exactly one point.

**Proof**: $(\implies)$  Choose a point from each of $F_{i}$ then since the diameters are decreasing to 0, we have a Cauchy sequence, hence it converges to a point in X.
$(\impliedby)$ For each $k \in \mathbb{N}$ we have that there exists $N_{k}$ such that for $n,m > N_{k}$ $d(x_{n},x_{m})< \frac{1}{k}$ . So we can choose a sequence of points such that they make up nested closed and contracting intervals, hence they have a common point. Hence the Cauchy sequence converges to that unique point.



25/07/25:
**Theorem**:(Lebesgue Covering Lemma) Let X be a compact metric space and {$E_{i}$} be an open cover. Then there exists $\epsilon > 0$. such that for any point x there is a ball of radius of $\epsilon$ contained in one of the $E_{i}$s.

**Proof**:(Sketch) Assume no such $\epsilon$ exists. Then $\forall n \in \mathbb{N} \ \exists x_{n}$ s.t $B\left( x_{n}, \frac{1}{n} \right)$  does not completely lie inside any of $E_{i}$
By compactness there should be a convergent subsequence for $x_{n}$. Now $\lim_{ n \to \infty } x_{n}=x$ $\in E_i$ for some i and hence there is a $\delta >0$ such that $B(x,\delta) \subseteq E_{i}$ . But then as $x_{n}$ goes to x and as 1/n becomes smaller than $\delta$ we get a contradiction.

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
$|| z^{(p)} - z^{(q)}|| = || (y^{(p)}-y^{(q)}) + \alpha_{n}^{(p)}x_{n} - \alpha_{n}^{(q)}x_{n}||$
$$
= |\alpha _{m}^{(p)} - \alpha_{n}^{q}| \left| \frac{1}{|\alpha_{n}^{(p)}-\alpha_{n}^{(q)}|}(y^{(p)}-y^{(q)}) - x_{n}\right|
$$
$$
\geq |\alpha_{n}^{(p)} - \alpha_{n}^{(q)}| \text{dist}(x_{n,Y})
$$

since $\{z^{(p)}\}$ is Cauchy for given $\epsilon>0$. we have {$\alpha$} is Cauchy in $\mathbb{R}$ and hence we have convergent and hence $\{ z^{(p)} \}$ converges to some $z \in Z$ Hence $Z$ is complete.

**Lemma**: (Riesz's Lemma): Let $Y$ be a closed subspace of $X$ such that $Y \neq X$. Then for any $0<r<1$. $\exists x_{r}\in X$ such that $\lvert x_{r} \rvert = 1$ and $r\leq\text{dist}(x_{r},Y) \leq 1$

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



**Theorem**: Let $(X,||\cdot ||)$ be a infinite dimensional space. Let $B(0,1) = \{x \in X\mid \|x\| \leq  1\}$ be the closed unit ball in X. Then $B(0,1)$ is not compact.

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
\lim_{ n \to \infty } \lvert f_{n}(x)-f_{m}(x) \rvert = |f_{n}(x) - f(x)| \leq  \frac{\epsilon}{2} \quad \forall n > k_{2}
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

**Theorem:** (Arzela-Ascoli) Let X be a compact metric space. Let $\{ f_{n} \}_{n=1}^{\infty }$ be a sequence of functions in $(C(X),\rho_{\infty})$ such that $\{ f_{n} \}$ is uniformly bounded and uniformly equicontinuous. Then $\exists$ a subsequence $\{ f_{n_{k}} \}$ which converges in $C(X)$

**Proof:** Since X is compact, X is totally bounded we can create a countable dense subset S of X as follows:

$\forall n \in \mathbb{N}$ , $\exists S_{n}= \{ s_{1},\dots,s_{n_{k}} \}$ such that
$$
X = \bigcup_{i=1}^{n_{k}} B \left(s_{i},\frac{1}{n} \right)
$$
$$
S = \bigcup_{i=1}^{\infty} S_{i} = \{x_{1},x_{2},\dots,\}
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
Then if $\rho(x,s) < \delta$
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
Let $K \in C([a,b]\times [a,b]), g \in C[a,b]$
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

**Theorem:** (Picard- Lindelof) Let g be a continuous function on a R = $\{ (t,x)| |t - t_{0}\mid \leq a, |x-x_{0}|\leq b \}$  and exists c >0 such that $|g(t,x)|\leq c$ $\forall (t,x) \in \mathbb{R}$. Also assume g is Lipschitz on the second variable i.e. $\exists k >0$ such that 
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

### Baire Category Theorem
**Def:** A subset A of a metric space X is said to be nowhere dense if the interior of $\overline{A}$ is empty.

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

**Corollary:** Let X be complete and $\{ F_{n} \}$ be a sequence of closed sets. Then $\bigcup_{n=1}^{\infty}\partial F_{n}$ has no open ball inside it.

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
Take, $D=X\setminus \bigcup_{n,m=1}^{\infty} \partial E_{n,m}$. So, D is dense in X. So, D is dense in X. Let $x_{0} \in D$ and $\epsilon>0$ arbitrary. $\{ f_{n}(x_{0}) \}$ is convergent and hence a Cauchy sequence. Let $m \in \mathbb{N}$ such that $\frac{1}{m} < \frac{\epsilon}{4}$. $\exists N \in \mathbb{N}$
$$
\lvert f_{j}(x_{0}) - f_{k}(x_{0}) \rvert < \frac{1}{m} \quad \forall j,k \geq N
$$
So, $x_{0} \in E_{m,N}$. Hence, $x_{0} \in D \cap E_{m,n}$. $\exists r>0$ such that $B(x_{0},r) \subseteq E_{m,N}$. Since, $f_{N}$ is continuous at $x_{0}$, $\exists 0<\delta<r$ such that
$$
\lvert f_{N}(x_{0}) - f_{N}(x) \rvert < \frac{1}{m} \quad \forall x \in B(x_{0},\delta)
$$
So,$\forall x \in B(x_{0},\delta)$ and $\forall j\geq N$,
$$
\begin{align}
\lvert f_{j}(x_{0}) -f_{j}(x) \rvert \leq & \lvert f_{j}(x_{0}) - f_{N}(x_{0}) \rvert + \lvert f_{N}(x_{0})-f_{N}(x) \rvert +\lvert f_{N}(x)-f_{j}(x) \rvert  \\
<& \frac{3\epsilon }{4}
\end{align}
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
\frac{M}{2\delta^{2}n < \frac{\epsilon}{4}}  & \text{if } n >  2\frac{M}{\delta^{2}\epsilon} \\
\text{ if } k \in \mathbb{N} > \frac{2M}{\delta^{2}\epsilon} &  \text{ then} \lvert B_{n}(\xi,f) - f(\xi)  \rvert \leq  \frac{\epsilon}{4}+ \frac{\epsilon}{2}=\frac{3\epsilon}{4}
\end{cases}
$$
So, $\sup_{\xi \in [0,1]}\lvert B_{n}(\xi,f)-f(\xi) \rvert < \epsilon, \forall n\geq k$

**Def:** A collection of real valued functions $\mathscr{A}$ on a set X is said to be an algebra if $\forall f,g \in \mathscr{A}, f+g, f\cdot g, cf \in \mathscr{A} \quad (c \in \mathbb{R})$  

**Def:** An algebra $\mathscr{A}$ of real valued function on a set X in said to be _uniformly closed_ if for every seq $\{ f_{n} \}$ converging uniformly to some $f, f\in \mathscr{A}$

Example: $C(X)$ X is compact is uniformly closed algebra

**Def:** A set $\mathscr{B}$ is said to be uniform closure of an algebra $\mathscr{A}$ of  real valued functions of X if $\mathscr{B}$ is the set of all uniform limits of $\mathscr{A}$

```tikz
\begin{document}
\begin{tikzpicture}
% Draw a open set script B
\draw (0,0) circle (2cm);
% Draw the label to the open set script B
\node at (2,2) {\textbf{B}};
% Draw a closed set script A
\draw (0,0) circle (1cm);
% Draw the label to the closed set script A
\node at (0,0) {\textbf{A}};

\end{tikzpicture}
\end{document}
```


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
\begin{align}
g_{1}(x) = \frac{h(x)-h(t)}{h(s)-h(t)} \frac{h_{1}(x)}{h_{1}(s)}\\
g_{2}(x) = \frac{h(s)-h(x)}{h(s)-h(t)} \frac{h_{2}(x)}{h_{2}(t)}
\end{align}
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
\begin{align}
\sin nx \sin mx &  = \frac{1}{2}[\cos(n-m)x - \cos(n+m)x] \\
\sin nx \cos mx  & = \frac{1}{2}[\sin(n+m)x - \sin(n-m)x] \\
\cos nx \cos mx &  = \frac{1}{2}[\cos (n+m)x + \cos (n-m)x]
\end{align}
$$
We can check that $\mathscr{A}$ is an algebra in $C[0,\pi]$. If $x_{1}\neq x_{2} \in [0,\pi]$, then $\cos x_{1} \neq \cos x_{2}$. So $\mathscr{A}$ separates points. Since constants belong to $\mathscr{A}$ it does not vanish at any point on $[0,\pi]$. Hence we are done by Stone-Weierstrass theorem. $\quad \blacksquare$

**Theorem:** Let X be a compact metric space and $\mathscr{A} \subseteq C(X)$ be an algebra which satisfies all the hypothesis of the Stone-Weierstrass theorem. Then, for any $f \in C(X)$, $\exists$ a decreasing sequence of functions $\{ g_{n} \}$ which converges uniformly to $f$. 

**Proof:**
$\forall n \in \mathbb{N}$ we choose, $f_{n} = f(x) + \frac{2}{3^{n}}$. Since $f \in C(X), f_{n} \in C(X)$. By Stone-Weierstrass, $\exists \{ g_{k} \}$ which converge uniformly to $f_{n}$. Hence $\exists g_{n} \in \mathscr{A}$ such that
$$
\begin{align}
 & \lvert g_{n}(x) - f_{n}(x) \rvert < \frac{1}{3^{n}} \quad \forall x \in X \\
 \implies &    -\frac{1}{3^{n}}   < g_{n}(x) - f_{n}(x) < \frac{1}{3^{n}} \\
\implies &  f_{n}(x) - \frac{1}{3^{n}} < g_{n}(x) < f_{n}(x)+ \frac{1}{3^{n}} \\
 & f(x) + \frac{1}{3^{n}} < g_{n}(x)<f(x) + \frac{1}{3^{n-1}} \quad (*) \\
\dots &  < g_{n+1}(x) < f(x) + \frac{1}{3^{n}} < g_{n}(x) < f(x) + \frac{1}{3^{n-1}} < g_{n-1}(x)<\dots
\end{align}
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
f_{j}(x) = \rho(x,z_{j}) \quad \forall x \in X 
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
|f(x)-f(y)| <\epsilon \quad \forall |x-y| < \delta 
$$
If $|x-y| \leq \delta$ , $\implies (x-y)^{2}\leq\delta^{2}$. Also since $f \in C[a,b]$, f is bounded. i.e. $\exists M>0$ such that $|f(x)|\leq M ,\forall x \in [a,b]$ 
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
\begin{align}

-\epsilon p_{n}(f_{0}) - \frac{2M}{\delta^{2}}p_{n}(f_{y}) <& p_{n}(f)(x) - f(y) p_{n}(f_{0})(y)  \\
\leq& \frac{2M}{\delta^{2}}p_{n}(f_{y})(y)+\epsilon p_{n}(f_{0})(y) 
\end{align}
\tag{***}
$$
Now,
$$
\begin{align}
p_{k}(f_{y})(y) &= p_{k}(x^{2}-2xy+y^{2})(y) \\
&= p_{k}(f^{2})(y) - 2yp_{k}(f_{1}(y)) + p_{k}(f_{2})(y)  \\
&\to y^{2} - 2y^{2} + y^{2} = 0
\end{align}
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
2. If $\{  E_{i} \}$ is a disjoint collection of sets in $\mathscr{M}$ then:
$$
\mu\left( \bigcup_{i=1}^{\infty } E_{i} \right) = \sum_{i=1}^{\infty } \mu(E_{i})
$$
$(X,M,\mu)$ is called a measure space. Elements of M are called measurable sets.

**Def:** 
1. $(X,M,\mu)$ is a finite measure space if $\mu(X)<\infty$
2. $(X,M,\mu)$ is said to be a $\sigma$-finite measure space if $\exists$ a disjoint collection $\{ E_{i} \}_{i=1}^{\infty} \subseteq M$ such that $X = \bigcup_{i=1}^{\infty} E_{i}$  and $\mu(E_{i}) < \infty$.

**Examples**: add some examples of measures #addexample 

**Theorem:** Let $\mu$ be a measure on $\mathscr{M}$ then,
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
\begin{gather}
F_{1} := E_{1} \\
F_{2}:=E_{2}\setminus E_{1} \\
\vdots \\
F_{k} := E_{k} \setminus \left( \bigcup_{i=1}^{k-1} E_{i} \right)
\end{gather}
$$
$$
\bigcup F_{k} = \bigcup E_{k}
$$
and $\{ F_{k} \}$ is a disjoint family in $\mathscr{M}$. So,
$$
\mu\left( \bigcup E_{k} \right) = \mu\left( \bigcup F_{k} \right) = \sum_{}^{} \mu(F_{k}) \leq \sum_{}^{}\mu(E_{k})
$$
3.  Let $E_{0}=\varnothing$, we have
$$
\begin{align}
\mu\left( \bigcup E_{i} \right) = &  \mu\left( \bigcup(E_{i}\setminus E_{i-1}) \right) \\
 = &  \sum_{}^{ } \mu(E_{i}\setminus E_{I-1}) \\
=  & \lim_{ n \to \infty } \sum_{i=1}^{n} \mu(E_{i}\setminus E_{i-1}) \\
=  & \lim_{ n \to \infty } \mu\left( \bigcup_{i=1}^{n}(E_{i}\setminus E_{i-1}) \right) \\
=  &  \lim_{ n \to \infty } \mu(E_{n})
\end{align}
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
\begin{gather}
\mu(E_{1}) - \mu\left( \bigcap E_{i} \right) = \mu(E_{1}) - \lim_{ n \to \infty } \mu(E_{n}) \\
\implies \mu\left( \bigcap E_{i} \right) = \lim_{ n \to \infty } \mu(E_{n}) \quad \text{(Since $\mu(E_{1}) < \infty $)}
\end{gather}
$$
Instead of $\mu(E_{1})<\infty$ if we assume $\mu(E_{n})<\infty$ for some $n \in \mathbb{N}$. Then also $(iv)$ is true.

**Def:** $E \in M$ is said to be a null set (measure zero) if $\mu(E) = 0$. If a property holds on $X$ except a set of measure zero then we say that the property holds almost everywhere on $X$.

>[!info]
>$f = g$ on $E^{c}$ where $\mu(E)=0$, $\mu$ is some measure then we say $f=g \text{ a.s}$

**Def:** Let $(X,M,\mu)$ be a measure space $\mu$ is said to be _complete measure_ if whenever $F \subset N$ and $\mu (N) = 0$ then $F \in M$.

**Theorem:** Let $(X,M,\mu)$ be a measure space. Define,
$$
\overline{M} = \left\{  E \cup F | E \in M \text{ and } F \subset N, \text{where N is a null set}   \right\}
$$
Then, $\overline{M}$ is a $\sigma$-algebra and there is an extension of $\mu$ to $\overline{M}$, say $\bar{\mu}$ such that $\bar{\mu}$ is a complete measure.

**Proof:** 
$$
\bigcup (E_{i} U F_{i}) = \left( \bigcup E_{i} \right) \cup \left( \bigcup F_{i} \right)
$$
The first term in the RHS in in $\mathscr{M}$ while the other is a null set, so we have $\bigcup (E_{i} \cup F_{i}) \in \overline{M}$

We have to check for $E \in M, F \in N$, if $E \cup F \in \overline{M}$ then $(E \cup F)^{c} \in \overline{M}$. We can always assume $E \cap N = \varnothing$,
$$
E \cup F = E \cup (F\setminus E) \quad \text{Now $E \cap (N\setminus E)=\varnothing$}
$$
$$
\begin{align}
E\cup F = & (E \cup N) \setminus (N \setminus F) \\
= & (E \cup N) \cap [(N \cap F^{c})]^{c} = (E \cup N) \cap (F \cup N^{c}) \\
(E \cup F)^{c} = & (E \cup N)^{c} \cup (N \cap F^{c})
\end{align}
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
\begin{gather}
\implies \sum_{i=1}^{\infty}\sum_{k=1}^{\infty}p(E_{i,k}) \leq \sum_{i=1}^{\infty}\mu^{*}(A_{i}) + \varepsilon\left( \frac{1}{2} + \frac{1}{2^{2}} +\dots  \right) \\
\implies \mu^{*}\left( \bigcup_{i=1}^{\infty } A_{i} \right) \leq \sum_{i=1}^{\infty}\sum_{k=1}^{\infty}p(E_{i,k}) \leq \sum_{i=1}^{\infty } \mu^{*}(A_{i}) + \varepsilon 
\end{gather}
$$

Since $\varepsilon$ is arbitrary, we have,
$$
\implies \mu^{*}\left( \bigcup_{i=1}^{\infty} A_{i} \right) \leq \sum_{i=1}^{\infty} \mu^{*}(A_{i})
$$
$\quad \blacksquare$

**Def:** Let $\mu^{*}$ be an outer measure on $X$. A subset $A \subseteq X$ is said to be _$\mu^{*}$-measurable_ if
$$
\mu^{*}(E) = \mu^{*} (E \cap A) + \mu^{*}(E \cap A^{*}) \quad \forall E \subseteq X
$$

**Theorem:**(Caratheodory's Theorem) Let $\mu^{*}$ be an outer measure on $X$ and $\mathscr{M}$ be the collection of all $\mu^{*}$-measurable sets. Then $\mathscr{M}$ is a $\sigma$-algebra and $\mu^{*}$ is a measure on $\mathscr{M}$
**Proof.** If $A$ is $\mu^*$–measurable then so is $A^c$. For $A,B \in \mathcal{M}$ and $\forall\, E \subseteq X$ we have,

$$
\begin{align}
\mu^*(E)  & = \mu^*(E \cap A) + \mu^*(E \cap A^c)  \\
 & = \mu^*(E \cap A \cap B) + \mu^*(E \cap A \cap B^c) + \mu^*(E \cap A^c \cap B) + \mu^*(E \cap A^c \cap B^c) \\
 & \geq \mu^*(E \cap (A \cup B)) + \mu^*(E \cap (A \cup B)^c)
\end{align}
$$

Also we clearly have

$$
\mu^*(E) \leq \mu^*(E \cap (A \cup B)) + \mu^*(E \cap (A \cup B)^c) \implies A \cup B \in \mathscr{M}.
$$

If $A, B \in \mathscr{M}$ and $A \cap B = \varnothing$, then

$$
\mu^*(A \cup B) = \mu^*\left((A \cup B) \cap A\right) + \mu^*\left((A \cup B) \cap A^c\right) = \mu^*(A) + \mu^*(B).
$$
Now we will see $\mathscr{M}$ is closed under disjoint union. Let $\{E_i\} \subset \mathscr{M}$ be a countable disjoint collection set, define:

$$
B_n = \bigcup_{i=1}^n E_i, \quad B = \bigcup_{i=1}^\infty E_i.
$$

By the first part, $B_n$ is $\mu^*$–measurable, i.e., $\forall\, E \subseteq X$,

$$
\begin{align}
\mu^*(E)  & = \mu^*(E \cap B_n) + \mu^*(E \cap B_n^c) \\
 & = \mu^*(E \cap B_n \cap E_n) + \mu^*(E \cap B_n \cap E_n^c) + \mu^*(E \cap B_n^c) \\
 & = \mu^*(E \cap E_n) + \mu^*(E \cap B_{n-1}) + \mu^*(E \cap B_n^c) \\
 & = \sum_{i=1}^n \mu^*(E \cap E_i) + \mu^*(E \cap B_n^c)  \\
 & \geq  \mu^*(E \cap B_{n}) + \mu^*(E \cap B_n^c)
\end{align}
$$

Taking $n \to \infty$, we get

$$
\mu^*(E) \geq \sum_{i=1}^\infty \mu^*(E \cap E_i) + \mu^*(E \cap B^c) \geq \mu^*(E \cap B) + \mu^*(E \cap B^c) \geq \mu^*(E)
$$

Hence $B$ is $\mu^*$–measurable, also from above we have,

$$
\mu^*(E \cap B) = \sum_{i=1}^\infty \mu^*(E \cap E_i).
$$

In particular, take $E = B$,

$$
\mu^*(B) = \sum_{i=1}^\infty \mu^*(E_i) \quad
$$

Hence $\mu^*$ is a measure on $\mathscr{M}$. To show $\mu^{*}$ is a complete measure. Take $A \subseteq X$ such that $\mu^*(A) = 0$.

$$
\mu^*(E) \leq \mu^*(E \cap A) + \mu^*(E \cap A^c) = \mu^*(E \cap A^c) \leq \mu^*(E).
$$

Therefore

$$
\mu^*(E) = \mu^*(E \cap A) + \mu^*(E \cap A^c) \quad \forall\, E \subseteq X
$$

$\implies  A \in \mathscr{M}$. By the above, all the subsets $B \subseteq A$ also belong to $\mathscr{M}$. Therefore $\mu^*$ is a complete measure on $\mathscr{M}$. $\quad \blacksquare$


**Def:** Let $\mathscr{A} \subseteq \mathscr{P}(X)$ be an algebra. A _premeasure_ $\mu_{0}$ is a function, $\mu_{0}:\mathscr{A} \to [0,\infty]$ such that
1. $\mu_{0}(\varnothing) = 0$
2. If $\{ A_{i} \}$ is a disjoint collection of sets in $\mathscr{A}$ such that $\bigcup_{i=1}^{\infty} A_{i} \in \mathscr{A}$ then,
$$
\mu_{0}\left( \bigcup_{i=1}^{\infty} A_{i} \right) = \sum_{i=1}^{\infty} \mu_{0}(A_{i})
$$

**Proposition:** Let $\mu_0$ be a premeasure on an algebra $\mathscr{A} \subseteq \mathscr{P}(X)$. Then there is an outer measure $\mu^*$ such that

1. $\mu^*|_{\mathscr{A}} = \mu_0$

2. Every set in $\mathscr{A}$ is $\mu^*$–measurable

**Proof:**
We can define an outer measure by following:

$$
\mu^*(E) = \inf \left\{ \sum_{i=1}^{\infty} \mu_0(A_i) \,\Big|\, E \subseteq \bigcup_{i=1}^{\infty} A_i,\, A_i \in \mathscr{A} \right\}.
$$
Now to check:
1. Suppose $E \in \mathcal{A}$. Then for any $\{ A_{i} \} \subseteq \mathscr{A}$ with $E \subseteq \bigcup_{i=1}^\infty A_i$ . Then $B_n := E \cap \left(A_n \setminus \bigcup_{i=1}^{n-1} A_i\right)$ is a disjoint collection and $E = \bigcup_{n=1}^\infty B_n$. So

$$
\mu_0(E) = \sum_{i=1}^{\infty} \mu_0(B_n) \leq \sum_{n=1}^{\infty} \mu_0(A_n).
$$

Therefore $\mu_0(E) \leq \mu^*(E)$. Taking $A_1 = E$ and $A_i = \emptyset$ for $i \ne 1$,

$$
\mu^*(E) = \mu_0(E).
$$

Thus $\mu^*(E) = \mu_0(E)$ $\forall\, E \in \mathcal{A}$.

2. Let $A \in \mathcal{A}$, $E \subseteq X$, $\epsilon > 0$. Then $\exists$ a sequence $\{B_i\}$ s.t. $E \subseteq \bigcup_{i=1}^\infty B_i$.

$$
\sum_{i=1}^\infty \mu_0(B_i) \leq \mu^*(E) + \epsilon \implies \sum_{i=1}^\infty \mu_0(B_i \cap A) + \sum_{i=1}^\infty \mu_0(B_i \cap A^c) \leq \mu^*(E) + \epsilon
$$

$$
\implies \mu^*(E \cap A) + \mu^*(E \cap A^c) \leq \sum_{i=1}^\infty \mu_0(B_i \cap A) + \sum_{i=1}^\infty \mu_0(B_i \cap A^c) \leq \mu^*(E) + \epsilon
$$

$$
\implies \mu^*(E \cap A) + \mu^*(E \cap A^c) \leq \mu^*(E) \quad \text{(for some arbitrary $\epsilon$).}
$$

So

$$
\mu^*(E) = \mu^*(E \cap A) + \mu^*(E \cap A^c)
$$

or $A$ is $\mu^*$–measurable. $\quad \blacksquare$


**Theorem:** Let $\mathscr{A} \subseteq \mathscr{P}(X)$ be an algebra, $\mu_{0}$ be a premeasure on $\mathscr{A}$ and $\mathscr{M}$ be the $\sigma$-algebra generated by $\mathscr{A}$. Then
1. There exists a measure $\mu$ on $\mathscr{M}$ such that $\mu = \mu_{0}$ on $\mathscr{A}$.
2. If $\nu$ is another measure on $\mathscr{M}$ that extends $\mu_{0}$ then $\nu  \leq \mu$ on $\mathscr{M}$.
3. The equality holds above if $\nu(X) = \mu(X) < \infty$.
4. if $\mu_{0}$ is $\sigma$-finite on $\mathscr{A}$ then the extension is unique.

**Proof:** 
1. Let $\mu^{*}$ be the outer measure as in the Proposition above. Let $\mathscr{M}'$ be the set of all $\mu^*$–measurable sets. Then by Caratheodory’s theorem, $\mu^*|_{\mathscr{M}'} = \mu_0$. By previous proposition,

$$
\mu^*|_{\mathscr{A}} = \mu_0 \impliedby  \mu^*|_{\mathscr{M}'} = \mu_0
$$
Since by previous proposition we have that $\mathscr{A} \subseteq \mathscr{M'}$.

2. Let $E \in \mathscr{M}$ and $E = \bigcup_{i=1}^\infty A_i$, $A_i \in \mathscr{A}$. Then

$$
\nu(E) \leq \sum_{i=1}^\infty \nu(A_i) = \sum_{i=1}^\infty \mu_0(A_i)
$$

$$
\implies \nu(E) \leq \mu^*(E) = \mu(E).
$$

3. If $A = \bigcup_{i=1}^\infty A_i$,

$$
\nu(A) = \lim_{n \to \infty} \nu\left( \bigcup_{i=1}^n A_i \right ) = \lim_{n \to \infty} \mu \left( \bigcup_{i=1}^n A_i \right ) = \mu(A) \tag{*}
$$
If $M(E)<\infty$ then we can choose $A_{i}$'s such that $A = \bigcup_{i=1}^{\infty} A_{i}$ and $\mu(A\setminus E )<\varepsilon$
$$
\mu(E) \leq \mu(A) \stackrel{*}{=} \nu(A) = \nu(E) + \nu(A\setminus E) < \nu(E)+\varepsilon 
$$
Since $\varepsilon$ is arbitrary $\mu(E)\leq \nu(E)$, combined with $(ii)$ we have $\mu(E)= \nu(E)$

4. $X = \bigcup_{i=1}^n A_i$ s.t. $\{A_i\}_{i \in \mathbb{N}}$ is a disjoint collection and $\mu_0(A_i) < \infty$. Then for $E \in \mathscr{M}$ we have from above,
$$ 
\mu(E) = \sum_{i=1}^\infty \mu(E \cap A_i) = \sum_{i=1}^\infty \nu(E \cap A_i) = \nu(E)
$$
## Construction of Lebesgue Measure

Let $A = \{\text{finite disjoint union of } (a,b] \text{intervals in } \mathbb{R}\} \subseteq \mathcal{B}_\mathbb{R}.$
**Exercise:** A is an algebra
**Solution:**

**Proposition 16.2.** Let $((a_i, b_i]]_{i=1}^n$ be any disjoint collection in $A$. Define
$$
\mu_0\left(\bigcup_{i=1}^n (a_i, b_i]\right) = \sum_{i=1}^n (b_i - a_i), \quad \mu_0(\emptyset)=0 \implies
$$
$\mu_0$ is a premeasure on $A$.

**Proof.** Let $\{I_i\}_1^n$ and $\{J_j\}_1^m$ be two disjoint collections of h-intervals. Then
$$
\sum_{i=1}^n I_i = \sum_{j=1}^m J_j \implies \mu_0\left(\bigcup_{i=1}^n I_i\right) = \sum_{i=1}^n \mu_0(I_i) = \sum_{i=1}^n \mu_0(I_i \cap \bigcup_{j=1}^m J_j)
$$
$$
= \sum_{j=1}^m \mu_0(J_j) = \mu_0\left(\bigcup_{j=1}^m J_j\right).
$$

So $\mu_0$ is well-defined. From the definition of $\mu_0$, it is clear that $\mu_0$ is finitely additive.
Remains to prove, if $\bigcup_{i=1}^\infty I_i \in A$ then $\mu_0\left(\bigcup_{i=1}^\infty I_i\right) = \sum_{i=1}^\infty \mu_0(I_i)$. Since $\bigcup_{i=1}^\infty I_i \in A$, $\bigcup_{i=1}^\infty I_i$ is the finite disjoint union of h-intervals $\{J_j\}_{j=1}^m$, i.e.,
$$
J_j = \sum_{i=1}^\infty I_{j_i} \quad \forall \ j \leq m
$$
where $\{J_{j_i}\}_{i=1}^\infty$ is some subsequence of $\{I_i\}_{i=1}^\infty$. Then
$$
\mu_0\left(\bigcup_{i=1}^\infty I_i\right) = \mu_0\left(\bigcup_{j=1}^m J_j\right) = \sum_{j=1}^m \mu_0(J_j) \quad \left(\mu_0(J_j) = \sum_{i=1}^\infty \mu_0(I_{j_i})\right)
$$
$$
\in A
$$
$$
\geq \mu_0\left(\bigcup_{i=1}^\infty I_{j_i}\right) = \mu\left(J_j \setminus \bigcup_{i=1}^n I_{j_i}\right) \geq \sum_{i=1}^n \mu_0(I_{j_i}) \quad \forall \ n
$$
$$
\implies \mu_0(J_j) \geq \sum_{i=1}^\infty \mu_0(I_{j_i}) \quad \text{as} \ n \to \infty. \quad \blacksquare
$$
We extend $\mu_0$ on $A$ to $M$ to $\mu^*$ on $\mathcal{P}(X)$ where
$$
\mu^*(A) = \inf\left\{\sum_i \mu_0(A_i) \ | \ A \subseteq \bigcup_i A_i, A_i \in \mathcal{A}\right\}.
$$
Then $M'$ = {collection of $\mu^*$-measure sets}. We have that $\mu^*|_{M'}$ is a measure, $A \subseteq M'$. Let $M = \mathcal{M}(A) \implies M \subseteq M'$. Then $\mu^*$ is a measure on $M$ which returns $\mu_0$ if $\mu_0$ is $\sigma$-finite on $X$. Then $\mu^*|_M$ is a unique measure which extends $\mu_0$. An h-interval is of the form $(-\infty, b], (a, b], (a, \infty)$, $a, b \in \mathbb{R}$ and $A = \{\text{finite disjoint unions of h-intervals}\}$ is an algebra.

**Proposition 17.1.** On $A$ define $\mu_0$ by
$$
\mu_0\left(\bigcup_{i=1}^n (a_i, b_i]\right) = \sum_{i=1}^n (b_i - a_i).
$$
Then $\mu_0$ is a premeasure on $A$.

**Proof.** Let $\{A_i\}_{i=1}^\infty$ is a countable disjoint collection of sets in $A$ if $\bigsqcup_{i=1}^\infty A_i\in A.$ We need to prove that $\mu_0(\bigsqcup_{i=1}^\infty A_i)=\sum_{i=1}^\infty\mu_0(A_i).$ Let $\bigsqcup_{i=1}^\infty A_i=\bigsqcup_{j=1}^k(a_i,b_j]$ where $(a_i,b_j]=\bigsqcup_{i,j}^\infty C_{ij}$ where $A_i=\bigsqcup_{j=1}^\infty C_{ij}.$ It is enough to show that 
$$
\mu_0(a_i,b_j]=\sum_{i=1}^\infty \mu_0(a_{j_i},b_{j_i})
$$ 
Basically if $[a,b]=\bigsqcup_{i=1}^\infty (a_i,b_i]$ then $\mu_0(a,b]=\sum_{j=1}^\infty\mu_0(a_i,b_i].$ Then 
$$
\bigsqcup_{i=1}^\infty (a_i,b_i]=\bigsqcup_{i=1}^N (a_i,b_i]+\bigsqcup_{i=N+1}^\infty (a_i,b_i]\implies \mu_0(\bigsqcup_{i=1}^\infty (a_i,b_i])\geq \mu_0(\bigsqcup_{i=1}^N (a_i,b_i])=\sum_{i=1}^N\mu_0(a_i,b_i]
$$
Taking $N\to\infty,$ $$\mu_0(a,b]=\mu_0(\bigsqcup_{i=1}^\infty(a_i,b_i])\geq\sum_{i=1}^\infty\mu_0(a_i,b_i].$$
Choose $\epsilon>0$ and take $\delta,\delta_i$ s.t $\delta<\epsilon,\ \delta_i< \frac{\epsilon}{2^{i}}$ Then $[a+\delta,b]\subseteq\bigcup_{i=1}^\infty (a_i,b_i+\delta_i).$ Since $[a+\delta,b]$ is compact, $[a+\delta,b]=\bigcup_{i=1}^N(a_i,b_i+\delta_i).$ Now, 
$$
\begin{align}
\mu_0(a,b] & =(b-a)\leq b-(a+\delta)+\epsilon\leq b_N+\delta_N-a_1+\epsilon \\
 & =b_N+\delta_N-a_N+\sum_{i=1}^{N-1}[a_{i+1}-a_i]+\epsilon\leq b_N+\delta_N-a_N+\sum_{i=1}^{N-1}[b_i+\delta_i-a_i] \\
 & <\sum_{i=1}^N(b_i-a_i)+\sum_{i=1}^\infty\delta_N+\epsilon<\sum_{i=1}^\infty (b_i-a_i)+\underbrace{\sum_{i=1}^\infty \frac{\epsilon}{2^{i}}+\epsilon}_{=2\epsilon}
\end{align}
$$

 As $\epsilon$ was arbitrary, $(b-a)\leq \sum_{i=1}^\infty (b-i-a_i).$ Therefore, $\mu_0(a,b]=\sum_{i=1}^\infty \mu_0(a_i,b_i].$ For intervals of type $(-\infty,b],\ \forall\ M<\infty$ we look at $(-M,b)$ intervals. Let $(-\infty,b]=\sum_{i=1}^N(a_i,b_i]\implies (-M,b)\subseteq \bigsqcup_{i=1}^\infty a_i,b_i].$ Taking $M\to\infty,$ 
$$
\mu_0(-\infty,b]\leq\sum_{i=1}^\infty\mu_0(a_i,b_i)
$$
Let $\mathcal{L} := \{\mu^*\text{-measurable sets}\}$, a Lebesgue $\sigma$-algebra. Lebesgue measure: Complete measure $m = \mu^*|_{\mathcal{L}}$ and $\mu = m|_{\mathscr{B}_\mathbb{R}}$. Then $\mathcal{B}_\mathbb{R} \subseteq \mathcal{L} \implies \overline{\mathscr{B_{\mathbb{R}}}}$  as $\mathcal{A} \subseteq \mathcal{L} \implies \mathscr{B}_\mathbb{R} = \mathscr{M}(A) \subseteq \mathcal{L}$.
**Question:** Is $\overline{\mathscr{B}_\mathbb{R}} = \mathcal{L}$?

**Proposition 17.2.** Let $E \in \mathcal{L}$. Then
$$
m(E) = \inf\left\{\sum_{i=1}^\infty m(a_i, b_i] \ | \ E \subseteq \bigcup_{i=1}^\infty (a_i, b_i]\right\}.
$$
**Proof.** Let
$$
\nu(E) := \inf\left\{\sum_{i=1}^\infty m(a_i, b_i] \ | \ E \subseteq \bigcup_{i=1}^\infty (a_i, b_i]\right\}.
$$
Now
$$
(a_i, b_i) = \bigsqcup_{k=1}^\infty (c_k^i, c_{k+1}^i] \implies E \subseteq \bigsqcup_{k=1}^\infty (c_k^i, c_{k+1}^i].
$$
Then $$\sum_{i=1}^\infty m(a_i,b_i)=\sum_{i,k=1}^\infty m(c_k^i,c_{k+1}^i]\implies m(E)=\mu^*(E)\leq\nu(E).$$ We need to show that $\nu(E)\leq m(E).$ Given $\epsilon>0,\ \exists\ \{(a_i,b_i]\}_{i=1}^\infty$ such that $$\sum_{i=1}^\infty m(a_i,b_i]\leq m(E)+\epsilon.$$ Take $\delta_i<\frac\epsilon{2^i}.$  Then $$\sum_{i=1}^\infty m(a_i,b_i+\delta_i)\leq\sum_{i=1}^\infty m(a_i,b_i]+\epsilon\leq m(E)+2\epsilon.$$ Since $\epsilon>0$ arbitrary, $\nu(E)\leq m(E).$ Therefore $\nu(E)=m(E).$

**Theorem:** If $E \in \mathcal{L}$, Then

$$
m(E) = \inf \left\{ m(U) \mid U \text{ is open and } E \subseteq U \right\}
$$

$$
= \sup \left\{ m(K) \mid K \text{ is compact and } K \subseteq E \right\}
$$

**Proof:**

Let $\lambda(E) = \inf \left\{ m(U) \mid U \text{ is open and } E \subseteq U \right\}$
Since $m(E) \leq m(U)$, Thus, $m(E) \leq \lambda(E)$

We already have seen, for $E \in \mathcal{L}$:

$$
m(E) = \inf \left\{ \sum_{i=1}^n m(a_i, b_i) \mid E \subseteq \bigcup_{i=1}^n (a_i, b_i) \right\}
$$

$$
\geq \inf \left\{ m(U) \mid U \text{ is open and } E \subseteq U \right\}
$$

$$
= \lambda(E)
$$

$$
\left(m\left(\bigcup_{i=1}^n (a_i, b_i)\right) \leq \sum_{i=1}^n m(a_i, b_i)\right)
$$

Therefore,
$$
m(E) = \lambda(E)
$$
Let $E$ be bounded. If E is closed there is nothing to prove. If E is not closed then consider for $F = \overline{E}\setminus E$. For any $\varepsilon>0$, $\exists U \supseteq F$ such that $m(U)\leq m(F)+\varepsilon$. Take,
$$
K = \overline{E}\setminus U \implies E = K \sqcup (E \cap U) \implies m(K) = m(E) - [m(U) - m(U\setminus E)] 
$$
$$
\begin{gather}
\overline{E} = (\overline{E} \setminus U) \sqcup U \\
m(\bar{E})=m(\bar{E}\setminus U)+m(U)\leq m(\bar{E}\setminus E)+\epsilon+m(K)=m(\bar{E})-m(E)+\epsilon+m(K)
\end{gather}
$$
$$
\implies m(E)\leq m(K)+\epsilon\implies m(E)=\sup\{\mu(K)|K\subseteq E, K\text{ compact}\}
$$
If $E$ is not bounded, 

$$
\begin{gather}
E=\bigsqcup_{i=0}^\infty (E\ \cap\ (i,i+1]) \\
\text{Let }E_i=E\ \cap\ (i,i+1]
\end{gather}
$$
Therefore for $\epsilon>0,\exists\ K_i$ such that  
$$
m(E_i)\leq m(K_i)+\frac \epsilon{2^i}
$$
Take $H_n=\bigcup_{i=-N}^N K_i,$ then: 

$$
\begin{gather}
m\left(\bigcup_{i=-N}^N E_i\right)\leq m\left(\bigcup_{i=-N}^N H_i\right)+\epsilon\implies m\left(\bigcup_{i=-\infty}^\infty E_i\right)=\lim_{N\to\infty} m\left(\bigcup_{i=-N}^N E_i\right) \\
= \lim_{N\to\infty}\sup\left\{m(K)| K\subseteq \bigcup_{i=-N}^N E_i\right\} \quad \blacksquare
\end{gather}
$$ 

**Proposition:** If $E \subseteq \mathbb{R}$ TFAE
1. $E \in \mathcal{L}$
2. $E = V\setminus N_{1}$ where $V$ is a $G_{\delta}$ set and $N_{1}$ is a null set.
3. $E = W \cup N_{2}$ where $W$ is an $F_{\sigma}$ set and $N_{2}$ is a null set.

**Proof:** 1$\implies$ 2 and 3:
Let $m(E)<\infty.$ Then for all $i\in \mathbb{N},$ $\exists$ an open set $U_i\supseteq E$ and a compact set $K_i\subseteq E$ such that 
$$
m(U_i)-\frac 1i\leq m(E)<m(K_i)+\frac 1i
$$
Now take $V=\bigcap_{i=1}^\infty U_i$ and $W=\bigcup_{i=1}^\infty K_i.$ Then $m(V)=m(E)=m(W).$ Consider $N_1=V\setminus E$ and $N_2=E\setminus W.$ Then 
$$
m(N_1)=m(N_2)=0
$$
If $m(E)=\infty$ write $E=\bigcup_{k\in \mathbb{Z}}\underbrace{E\ \cap\ (k,k+1)}_{E_k}.$ Now $m(E_k)<\infty,\ \exists$ some $V_\delta$ set $V_k$ and $F_\delta$ set $W_k$ such that $m(N_1^k)=m(N_2^k)=0$ and  $E_k=V_k\setminus N_1^k$ and $E_k=W_k\ \cup\ N_2^k.$ Take 
$$
\begin{gather}
V=\bigcup_{k\in \mathbb{Z}} V_k \\
W=\bigcup_{k\in \mathbb{Z}}W_k  \\
N_1=\bigcup_{k\in \mathbb{Z}} N_1^k \\
N_2=\bigcup_{k\in \mathbb{Z}}N_2^k
\end{gather}
$$ 
Then we are done as $(2 \implies 1)$ and $(3 \implies 1)$ are obvious.

**Remark:** L is the completion of $B_{\mathbb{R}}$ where
$$m(E)=\inf\left\{\sum_{i=1}^\infty m(a_i,b_i)\mid E\subset \bigcup_{i=1}^\infty (a_i,b_i)\right\}$$
and any element $F\in\mathcal{L}$ can be written as $F=E \cup N$ where $E\in\mathscr{B}_\mathbb{R}$ and $N\subseteq N_1$ where $m|_{\mathscr{B}_\mathbb{R}} (N_1)=0.$

**Def:** $f:(X,\mathscr{M}) \to (Y,\mathscr{N})$ then f is said to be $(\mathscr{M},\mathscr{N})$ **measurable** if $f^{-1}(N) \in \mathscr{M}, \forall N \in \mathscr{N}$. If $f:(X,\mathscr{M}) \to (\mathbb{R},\mathscr{B}_{\mathbb{R}})$ and f  in $(\mathscr{M},\mathscr{B}_{\mathbb{R}})$-measurable then f is simply called as $\mathscr{M}$-measurable function.
**Exercise:** Let $f:X\to (Y,\mathscr{N})$ be a function then $\{f^{-1}(E)|E\in\mathscr{N}\}$ is an algebra on $X.$

**Solution:**

**Theorem:** Let $E \in \mathcal{L}$ Then $\forall s,r \in \mathbb{R}$, $E + s \in \mathcal{L}$ and $rE \in \mathcal{L}$ . Now, $m(E + r) = m(E)$ and $m(rE) = \lvert r \rvert m(E)$.

**Proof:** Let $I$ be an open interval then $I +s$ and $rI$ are also open intervals. Also, $m(I+s) = m(I)$ and $m(rI)= \lvert r \rvert m(I)$.

If $E \in \mathscr{B}_{\mathbb{R}}$ and since $E$ is generated by open intervals then $E + s \in \mathscr{B}_{\mathbb{R}}, rE \in \mathscr{B}_{\mathbb{R}}$, $m(E+s)=m(E), m(rE)=\lvert r \rvert m(E)$.

Let $N \in \mathscr{B}_{\mathbb{R}}$ and $m(N)=0$ by premeasure $N +r \in \mathscr{B}_{\mathbb{R}}, rN \in \mathscr{B}_{\mathbb{R}}$. $m(N + s)=0,m(rN)=\lvert r \rvert m(N)=0$
If $F \subseteq N$ then $m(F)=0$, Also, $F+r \subseteq N+s$, $rF \subseteq rN$.
$$
\begin{gather} \\
m(F+r) \leq m(N+s) = 0 \\
m(rF) \leq m(rF) \leq m(rN) = 0
\end{gather}
$$
for general $E \in \mathcal{L}$, $E = G \cup F$ where $G \in \mathscr{B}_{\mathbb{R}}, F$ is a null set. $E + r = (G +r) \bigsqcup (F+s)$. So $E + r \in \mathcal{L}$ and $m(E + r) = m(E)$. Similarly for $rE \in \mathcal{L}$ and $m(rE) = \lvert r \rvert m(E)$

**Exercise:** Let $f:(X,\mathscr{M})\to (Y,\mathscr{N})$ and $g:(Y,\mathscr{N})\to (Z,\mathscr{G})$ be $(\mathscr{M},\mathscr{N})$ and $(\mathscr{N},\mathscr{G})$-measurable respectively. Then $g\circ f$ is $(\mathscr{M},\mathscr{G})$-measurable.

**Solution:**

**Proposition:** Let $f:(X, \mathscr{M})\to (Y,\mathscr{N})$ and $\mathscr{N}$ is generated by $E$, Then f is measurable iff $f^{-1}(\mathscr{E}) \in \mathscr{M},\forall E \in \mathscr{E}$.
**Proof:** $(\implies)$ Trivial
$(\impliedby )$ 
$$
f^{-1}\left( \bigcup_{E \in \mathscr{E}^{}} E \right) = \bigcup_{E \in \mathscr{E}^{}} f^{-1}(E) \in \mathscr{M}
$$
Hence we are done.

**Corollary:** Let $f:X \to Y$ are continuous then f is $(\mathscr{B}_X,\mathscr{B}_{Y})$-measurable
**Proof:**

**Proposition:** Let $f:(X, \mathscr{M})\to \mathbb{R}$ be a function. The following are equivalent:

1. $f$ is measurable
2. $f^{-1}((a,\infty))\in \mathscr{M}$ for all $a\in\mathbb{R}$
3. $f^{-1}((-\infty,b))\in \mathscr{M}$ for all $b\in\mathbb{R}$
4. $f^{-1}([a,\infty))\in \mathscr{M}$ for all $a\in\mathbb{R}$
5. $f^{-1}((-\infty,b])\in \mathscr{M}$ for all $b\in\mathbb{R}$

**Proof:** Easy to see.

**Proposition:** Let $f,g:(X,\mathscr{M})\to\mathbb{R}$ be measurable and $\phi:\mathbb{R}^2\to Y$ be a continuous function. Define $h:X\to Y$ by $h(x)=\phi(f(x),g(x))$. Then $h$ is measurable.

**Proof:** Let $R$ be an open rectangle in $\mathbb{R}^2$ whose sides are parallel to the $X$ and $Y$ axes. Define $K:X\to\mathbb{R}^2$ by $K(x)=(f(x),g(x))$. Then $h=\phi\circ K$. We only need to show that $K$ is measurable.
Now,
$$
K^{-1}(R)=f^{-1}(I_1) \cap g^{-1}(I_2).
$$
Since $f,g$ are measurable, $f^{-1}(I_1)$ and $g^{-1}(I_2)\in\mathscr{M}$ and so $K^{-1}(R)\in\mathscr{M}$. Any open set $E\in\mathbb{R}^2$ can be written as the countable union of such rectangles, i.e., $E=\bigcup_{i=1}^\infty R_i$. So
$$
K^{-1}(E)=K^{-1}\left(\bigcup_{i=1}^\infty R_i\right)=\bigcup_{i=1}^\infty K^{-1}(R_i)\implies K^{-1}(E)\in\mathscr{M}.
$$
**Corollary:** 
1. Let $f:(X,\mathscr{M})\to\mathbb{C}$ be measurable. Then so is $\text{Re}(f), \text{Im}(f), |f|$. Conversely, if $\text{Re}(f), \text{Im}(f)$ are measurable then so is $f$.
2. Let $f,g:(X,\mathscr{M})\to\mathbb{R}/\mathbb{C}$ be measurable. Then so is $f+g, fg$.

**Proof:**
2. Use $\phi(x,y) = x +y , \phi(x,y)= xy$ in the above proposition.
**Remark:** $f: X \to \mathbb{\overline{R}}$, convention $0 \cdot \infty = 0$

**Proposition:** Let $\{f_i\}_{i\in\mathbb{N}}$ be a sequence of measurable functions. Then $\sup_{i\in\mathbb{N}} f_i$, $\inf_{i\in\mathbb{N}}f_i$, $\limsup f_i$, $\liminf f_i$ are also measurable functions.

**Proof:** Let $g(x)=\sup_{i\in\mathbb{N}}f_i(x)$. Then $g^{-1}((a,\infty])=\bigcup_{i=1}^\infty f_i^{-1}((a,\infty])$ for all $a\in\mathbb{R}$. So $g$ is measurable as $f_i$'s are. Let $h(x)=\inf_{i\in\mathbb{N}}f_i(x)$. Then
$$
h^{-1}([-\infty,b))=\bigcap_{i=1}^\infty f_i^{-1}([-\infty,b)).
$$
Then $h$ is measurable. Similarly, $\limsup f_i=\inf_k\sup_{i\geq k} f_i$ and $\liminf f_i=\sup_k\inf_{i\geq k} f_i$. By the previous part, $\limsup$ and $\liminf$ are also measurable.

**Corollary:**
1. Let $f,g:(X,\mathscr{M})\to\mathbb{R}$ be measurable functions then so are $\min(f,g)$ and $\max(f,g)$.
2. $f:(X,\mathscr{M})\to\mathbb{R}$ and $f=f^+-f^-$. So $f$ is measurable if $f^+$ and $f^-$ are measurable.

**Def:** **(Characteristic Function)**
Let $(X,\mathscr{M})$ be a measure space and $E\in\mathscr{M}$. Then the function $\chi_E:X\to\mathbb{R}$ defined by
$$
\chi_E(x)=\begin{cases}
1, & x\in E\\
0, & \text{else}
\end{cases}
$$
is called the **characteristic** function on the set $E$.

**Remark:** $\chi_E$ is measurable.

**Def:** **(Simple Function)**
A function $\phi:(X,\mathscr{M})\to\mathbb{R}$ is called a **simple** function if $\text{img}(\phi)$ has only finitely many points. Let $\text{img}(\phi)=\{a_1,\ldots,a_n\}$. Then
$$
\phi=\sum_{i=1}^n a_i\chi_{E_i} \text{ where } E_i=\phi^{-1}(a_i).
$$

**Remark:**
Simple functions are measurable iff $E_i$'s are measurable.

**Notation:** $\mathcal{L^+}=$ Set of all measurable functions $f:(X,\mathscr{M})\to [0,\infty]$.

Let $\phi=\sum_{i=1}^\infty a_i\chi_{E_i}\in \mathcal{L^+}$. Then
$$
\int_X\phi d\mu:=\sum_{i=1}^\infty a_i\mu(E_i).
$$

**Proposition:**
Let $\phi,\psi\in \mathcal{L^+}$ be simple. Then
1. $\int(\phi+\psi)d\mu=\int\phi d\mu+\int\psi d\mu$
2. $c\int\phi d\mu=\int c\phi d\mu$
3. If $\phi\leq\psi$ then $\int\phi d\mu\leq \int\psi d\mu$
4. The function $\lambda:A\to \int_A\phi d\mu$ is a measure on $X \equiv\int\phi\chi_A d\mu$

**Def:** Let $f\in \mathcal{L^+}$. Then
$$
\int fd\mu=\sup\left\{\int\phi d\mu|0\leq\phi\leq f\right\}.
$$
Observe that if $f,g\in L^+$ and $f\leq g$ then $\int f d\mu\leq\int g d\mu$. Also for all $c>0$, $c\int f d\mu=\int cf d\mu$.

**Proposition:** Let $f \in L^{+}$ then, $\exists \{ \phi_{n} \} \subseteq L^{+}$ such that $\phi_{n} \uparrow f$ pointwise.
**Proof:** For $n=1,2,\dots$ and $\forall 0\leq k\leq 2^{2n}-1$
$$
\begin{gather}
E_{n}^{k} = f^{-1}((2^{-n},2^{-n}(k+1)]) \\
F_{n} = f^{-1}((2^{n},\infty ]) \\
\phi_{n} = \sum_{k=1}^{2^{2n}-1} 2^{-n}k \chi_{E_{n}^{k}} + 2^{n}\chi_{F_{n}}
\end{gather}
$$
Then clearly $\phi_{n}\leq \phi_{n+1} \forall n \in \mathbb{N}$ and $f(x) = \lim_{ n \to \infty } \phi_{n}(x) \forall x \in X$

**Theorem:** **(Monotone Convergence Theorem)** Let $\{f_n\}_{n\in\mathbb{N}}\subseteq \mathcal{L^+}$, $f_n\leq f_{n+1}$ for all $n\in\mathbb{N}$ and $f=\lim f_n$. Then $\int f d\mu=\lim_{n\to\infty}\int f_n d\mu$.

**Proof:**
Since $f_n\leq f$ for all $n\in\mathbb{N}$,
$$
\int f_n d\mu\leq \int f d\mu\implies\lim_{n\to\infty}\int f_n d\mu\leq\int f d\mu.
$$
For the convergence part, let $0\leq\phi\leq f$ and $\alpha<1$ such that $\alpha\phi<f$. Consider
$$
E_n=\{x\in X|f_n(x)\geq \alpha\phi(x)\}.
$$
Then $X=\bigcup_{n=1}^\infty E_n$, $E_n\uparrow X$. Then $\int_{E_n}f_n d\mu\geq \int_{E_n}\alpha\phi d\mu =\alpha\int_{E_n}\phi d\mu$. Since $\lambda:A\to\int_A\phi d\mu$ is a measure,
$$
\int_X\phi d\mu=\lim\int_{E_n}\phi d\mu.
$$
Suppose $\lambda:A\to\int_A\phi d\mu$ is a measure. Since $E_1\subseteq E_2\subseteq\ldots$, $\mu\left(\bigcup E_i\right)=\lim_{i\to\infty}\mu(E_i)\implies \lambda(X)=\lim_{n\to\infty}\lambda(E_i)$. Then $\int_X\phi d\mu=\lim\int_{E_n}\phi d\mu$. From,
$$
\int f_n d\mu\geq\int_{E_n}f_n d\mu\geq\alpha\int_{E_n}\phi d\mu\implies \int f_n d\mu\geq\alpha\int \phi d\mu
$$
$$
\implies \lim_{n\to\infty}\int f_n d\mu\geq\alpha\int \phi d\mu \text{ for all } \alpha<1
$$
$$
\begin{gather}

\implies \lim_{n\to\infty}\int f_n d\mu\geq \int \phi d\mu \text{ for all } 0\leq \phi\leq f \\
\implies \lim_{n\to\infty}\int f_n d\mu\geq \sup\left\{\int\phi d\mu|0\leq \phi\leq f\right\}=\int f d\mu.
\end{gather}
$$

**Proposition:** Let $\{f_i\}_{i\in\mathbb{N}}\subseteq \mathcal{L^+}$. Then $\int \left(\sum_{i=1}^\infty f_n\right)d\mu=\sum_{i=1}^\infty \int f_n d\mu$.
**Proof:** Let $f_{1}, f_{2} \in \mathcal{L}^{+}$ then $\int f_{1} + f_{2} = \int f_{1} + \int f_{2}$. $\exists$ a sequence of simple functions $\{ \phi _{i} \} \uparrow f_{1}, \{ \varphi_{i} \} \uparrow f_{2} \implies \{ \phi_{i} + \varphi_{i} \} \uparrow f_{1}+f_{2}$, then by MCT
$$
\int f_{1} + f_{2} = \lim_{ n \to \infty } \int \phi_{i} + \lim_{ n \to \infty } \int \varphi_{i}
$$

By induction we have 
$$
\int \sum_{n=1}^{N} f_{n} d\mu = \sum_{n=1}^{N} \int f_{n} d\mu 
$$
So $\left\{  \sum_{n=1}^{N}f_{n}  \right\} \uparrow \sum_{n=1}^{\infty} f_{n}$ Then,
$$
\begin{align}
\int \sum_{n=1}^{\infty} f_{n}d\mu = & \lim_{ N \to \infty } \int \sum_{n=1}^{N} f_{n} d\mu \\
 =& \lim_{ N \to \infty } \sum_{n=1}^{N} \int f_{n} d\mu \\
= & \sum_{n=1}^{\infty } \int f_{n} d\mu  \quad \blacksquare
\end{align}
$$

**Lemma:(Fatou)** $\{ f_{n} \} \subseteq L^{+}$ Then,
$$
\int \lim \inf f_{n} \leq \lim \inf \int f_{n} d\mu 
$$
**Proof:** $\inf_{n\geq k} f_{n} \uparrow \sup_{k} \inf_{n\geq k} f_{n}$ Hence by MCT we have
$$
\int \lim \inf f_{n} d\mu = \int \sup_{k} \inf_{n\geq k} f_{n} d\mu = \sup_{k} \int \inf_{n\geq k} f_{n} d\mu 
$$
 Now,
$$
\begin{gather}
\inf_{n\geq k} f_{n} \leq f_{j} \quad \forall j \geq k \\
\implies \int \inf_{n\geq k} f_{n} d\mu \leq \int f_{j} d\mu \quad \forall j \geq k  \\
\implies \int \inf_{n\geq k } f_{n} d\mu \leq \inf_{j\geq k} \int f_{j} d\mu \\
\implies \int \lim \inf f_{n} d\mu \leq \sup_{k} \inf_{j\geq k} \int f_{j} d\mu = \lim \inf \int f_{n} d\mu  \quad \blacksquare
\end{gather}
$$
**Def:** Let $f:X\to \mathbb{\overline{R}}$ measurable and $f = f^{+} - f^{-}$, if one of $\int f^{+},\int f^{-}$ is finite,
$$
\int f d\mu = \int f^{+} d\mu - \int f^{-} d\mu 
$$

**Def:** Let $(X,\mathscr{M},\mu)$ be a measure space denote $L^{1}(\mu)$ as the set of all measurable functions $f : X\to \mathbb{C}$ such that
$$
\int \lvert f \rvert d\mu < \infty 
$$
Let $f = u + iv$, then $u\leq \lvert f \rvert, v\leq \lvert f \rvert$ hence we define,
$$
\int f d\mu = \int u^{+} d\mu - \int u^{-} d\mu + i\left[ \int v^{+}d\mu - \int v^{-} d\mu \right]
$$
**Proposition:** If $f,g \in L^{1}(\mu)$, then $\forall \alpha, \beta \in \mathbb{C}$
$$
\alpha f + \beta g \in L^{1} (\mu)
$$

**Proof:** **Exercise**

**Theorem:** **(Dominated Convergence Theorem (DCT))**
Let $(X,\mathscr{M},\mu)$ be a measure space. Let $\{f_n\}$ be a sequence of measurable functions on $X$ such that $f_n\to f$ pointwise. Suppose there exists a function $g\in L^1(\mu)$ such that $|f_n|\leq g$ for all $n\in\mathbb{N}$.
Then $f\in L^1(\mu)$,
$$
\lim_{n\to\infty}\int |f_n - f| d\mu = 0
$$
and
$$
\lim_{n\to\infty}\int f_n d\mu = \int f d\mu \iff \lim_{n\to\infty}\int |f_n - f|d\mu=0.
$$
**Proposition:** Let $f \in L^1(\mu)$. Then
$$
\left|\int f d\mu\right| \leq \int |f| d\mu.
$$
**Proof:** Let $z = \int f d\mu$. There exists an $\alpha \in \mathbb{C}$ such that $\alpha z = |z|$ and $|\alpha|=1$.
Let $u$ be the real part of $\alpha f$. Then $u \le |\alpha f| = |f|$.
$$
\left|\int f d\mu\right| = \alpha \int f d\mu = \int \alpha f d\mu = \int u d\mu \le \int |f| d\mu.
$$
**Proof:(DCT)** 
$|f_n|\leq g \implies |f|\leq g \implies \int |f|d\mu\leq \int g d\mu < \infty$, so $f\in L^1(\mu)$.
Take $2g - |f_n - f| \to 2g$.
$|f_n - f| \leq |f_n| + |f| \leq g+g = 2g$.
$$
\int \liminf (2g - |f_n - f|) d\mu \leq \liminf \int (2g - |f_n - f|) d\mu.
$$
$$
\implies \int 2g d\mu \leq \liminf \int 2g d\mu + \liminf \int (-|f_n - f|) d\mu
$$
$$
= \int 2g d\mu - \limsup \int |f_n - f| d\mu.
$$
$$
\implies \limsup \int |f_n - f| d\mu \leq 0 \leq \liminf \int |f_n - f| d\mu.
$$
$$
\implies \limsup \int |f_n - f| d\mu = \liminf \int |f_n - f| d\mu
$$
$$
= \lim_{n\to\infty} \int |f_n - f| d\mu = 0.
$$
## Role played by measure zero sets

**Proposition:** $(X,M,\mu)$ complete measure space
1. Let $f = g$ a.e then f is measurable iff g is
2. Let $\{ f_n \}$ be a seq of measurable functions such that $\{ fn \}\to f$ pointwise a.e then f is measurable.
**Proof:** **Exercise**

**Theorem:** Let $(X,M,\mu)$ be a measure space,
1. Let $f:X\to[0,\infty]$ and $E \in M$
Then 
$$
\int_{E} d\mu = 0 \iff f=0 \text{ a.e on } E
$$
2. Let $f \in L^{1}(\mu )$
$$
\int_{E}f d\mu = 0\quad \forall E \in M \text{ then } f=0 \text{ a.e on } X
$$

**Proof:** 
1. Let $E_{n} = \left\{  x \in E\mid f(x) > \frac{1}{n} \right\}$, let $F = \{  x \in E \mid f(x)>0 \}$, then we have $F = \bigcup_{n=1}^{\infty} E_{n}$
$$
\begin{gather}
\implies \int_{E_{n}} f d\mu \leq \int_{E} f d\mu = 0 \\
\frac{1}{n} \mu(E_{n}) \leq \int_{E_{n}} f d\mu = 0 \\
\implies \mu(E_{n}) = 0 \implies \mu(F) = 0 \implies f = 0 \text{ a.e on } E
\end{gather}
$$
2. $f = u+iv$ Then we have that $\int u d\mu = 0 , \int v d\mu = 0$, hence from above we have $f = 0$ a.e on X. 

## $L^{p}$ spaces

We say that $f \sim g$ if $f = g$ a.e on $X$.
$$
L^{1}(\mu) = \left\{  [f] \mid \int_{X} \lvert f \rvert d\mu < \infty  \right\}
$$
similarly, $\forall 0<p<\infty$
$$
L^{p}(\mu) = \left\{  [f] \mid \int_{X} \lvert f \rvert^{p} d\mu < \infty  \right\}
$$
Also we have,
$$
L^{\infty} (\mu) = \{[f]\mid \text{essential supremum of $|f|$ exists}\}
$$
**Def:** **(Essential supremum)** Let $g : X\to [0,\infty]$ 
$$
S = \{  \alpha \mid \mu(g ^{-1}((\alpha,\infty])) = 0 \}
$$
If $S\neq \varnothing$, $\beta = inf S$. Prove that $\beta \in S$
If $S = \varnothing$, $\beta  = \infty$
$$
\beta + \frac{1}{n} \in S \implies \mu ( g^{-1}\left( \beta+\frac{1}{n},\infty] \right) = 0
$$
hence,
$$
0=\mu ( g^{-1} (\beta,\infty ]) = \bigcup_{n=1}^{\infty} \mu\left( g^{-1}\left( \beta+\frac{1}{n},\infty  \right] \right)
$$

**Theorem:** $1\leq p\leq \infty$, $L^{p}(\mu)$ is a normed linear space.

**Proof:** We will show that $||\cdot||_p$ is a norm on $L^p(\mathcal{M})$. (i) If $1 \le p < \infty$, $||f||_p = 0 \implies \int |f|^p d\mu = 0 \implies |f|^p = 0$ a.e. $\implies f=0$ a.e. If $p = \infty$, $||f||_\infty = 0 \implies f=0$ a.e. $\implies [f]=0$. (ii) If $1 \le p < \infty$, $\forall \lambda \in \mathbb{C}$ $$ ||\lambda f||_p = \left(\int |\lambda f|^p d\mu\right)^{1/p} = \left(\int |\lambda|^p |f|^p d\mu\right)^{1/p} $$ $$ = |\lambda| \left(\int |f|^p d\mu\right)^{1/p} = |\lambda| ||f||_p. $$ For $p=\infty$, $\text{ess sup } |\lambda f| = |\lambda| (\text{ess sup } |f|)$. 
$$
\implies ||\lambda f||_\infty = |\lambda| ||f||_\infty 
$$
(iii) we use Minkowski's inequality to prove the triangle inequality for $1 < p < \infty$.
If $1 < p < \infty$,
$$
\int |f+g|^p d\mu \leq \int |f|^p d\mu + \int |g|^p d\mu
$$
$$
||f+g||_p^p = \int |f+g|^p d\mu \leq \int |f|^p d\mu + \int |g|^p d\mu
$$
$$
\geq ||f||_p^p + ||g||_p^p
$$
$$
\implies ||f+g||_p \leq ||f||_p + ||g||_p.
$$
For $p=1$ and $p=\infty$, it is easy to verify.

**Theorem:** For $1 \le p \le \infty$, $L^p(\mu)$ is a complete normed linear space.

**Proof:** We skip the proof.

**Remark:** If $X$ is countable and $\mu$ is a counting measure, then
$$
L^p(\mu) \equiv l^p(\mu).
$$

**Correspondence:** $\{ (f(x_1), \ldots, f(x_n), \ldots) \mid \sum_{i=1}^\infty |f(x_i)|^p < \infty \}$.
Let $f \in L^p(\mu)$, $\int |f|^p d\mu<\infty \implies \sum_{i=1}^\infty |f(x_i)|^p < \infty$.
Then we have a corresponding sequence in $l^{p}$
$l^p(\mu) = \{ (\lambda_1, \lambda_2, \ldots) \mid \lambda_i \in \mathbb{C} \text{ s.t. } \sum |\lambda_i|^p < \infty \}$.
$$
\begin{align}
f(x_1)  & =  \lambda_1 \\
f(x_2)  & =  \lambda_2 \\
 & \vdots   \\
f(x_n)  & =   \lambda_n
\end{align}
$$
$\forall \ 1 \le p \le q \le \infty$, $L^p(\mu) \subseteq L^q(\mu)$ if $\mu(X) < \infty$. (check it)
**Theorem:** If $\mu(X)<\infty$, then $1\le p \le q \implies L^q(\mu)\subseteq L^p(\mu)$.

$L^{\infty}(\mu)\subseteq\cdots\subseteq L^q(\mu)\subseteq L^p(\mu)\subseteq\cdots\subseteq L^1(\mu)$.

**Def:** Let $X$ be a topological space. $C_c(X)=\{ \text{compactly supported continuous functions on X} \}$.

**Theorem:** For $1\le p<\infty$, $C_c(\mathbb{R})$ is dense in $L^p(\mathbb{R},m)$.where $m$ is the Lebesgue measure.

Let $f\in C_c(X)$. $\int_X |f|^p dm = \int_{K}\lvert f \rvert^{p}dm\leq M^{p}\int_{K}1dm <\infty$

## Fourier Analysis

If $f\in L^1(\mathbb{R},m)$ or in particular if $f$ is Riemann integrable.
$f$ is a periodic function of period $L$.

$$ f \sim \sum_{n=-\infty}^{\infty} (a_n \cos \frac{2\pi nx}{L} + b_n \sin \frac{2\pi nx}{L}). $$ $f:\mathbb{R}\to\mathbb{C}$ $f:[a,b]\to\mathbb{C}$, $(b-a)=L$. $f$ is $L$-periodic. $f \sim \sum_n (a_n \cos\frac{2\pi nx}{L} + b_n \sin\frac{2\pi nx}{L})$. Let $f:[a,b]\to\mathbb{C}$ be integrable and $(b-a)=L$. Then the $n^{th}$ Fourier coefficient of $f$ is 
$$ 
\hat{f}(n) = \frac{1}{L} \int_a^b f(x)e^{-2\pi in x/L} dx. 
$$

### Primary goals of Fourier Analysis

1. Whether $S_{n}(f)(x)$ in convergent for all x?
2. Whether $S_{N}(f)\to f$ pointwise $\forall x \in [a,b]$
3. Even if f is continuous $S_{N}(f)$ may not converges to f pointwise $\forall x \in [a,b]$.
4. if f is differentiable and $f'$ is continuous then $S_{N}(f)\to f$ pointwise and uniformly
5. If f is continuous at  $x \in [a,b]$ then $S_{N}(f)\to f$ is continuous in Cesaro means.
6. $S_{N}(f)\to f$ in $\|\cdot \|_{2}$ i.e. $\int \lvert S_{n}(t)-f \rvert^{2}dx\to 0$ as $n\to \infty$.


**Examples:**  $f(\theta) = \theta, \forall -\pi\leq \theta\leq \pi$ ,$\forall n \in \mathbb{Z}, n \neq 0$
$$
\begin{gather}
\hat{f}(n) = \frac{1}{2\pi}\int f(\theta)e^{-in \theta } d\theta  \\
=\begin{cases}
\frac{(-1)^{n+1}}{in}  & n\neq 0 \\
0  & \text{o.w}
\end{cases}
\end{gather}
$$
$$
f \sim \sum_{n\neq 0}^{} \frac{(-1)^{n+1}}{in}e^{in \theta} = 2 \sum_{i=1}^{\infty} \frac{\sin n\theta}{n}
$$
**(Dirichlet kernel):** $-\pi\leq \theta\leq \pi$
The $N$-th Dirichlet kernel is defined as follows
$$
D_{N}(\theta) = \sum_{n=-N}^{N}e^{in \theta }
$$
nth Fourier coefficient of $D_{N}(\theta)$ is
$$
\begin{gather}
\frac{1}{2\pi}\int_{-\pi}^{\pi} \left( \sum_{n=_{N}}^{N}e^{in \theta } \right) e^{ik \theta } d\theta  \\
\sum_{n=-N}^{N} \frac{1}{2\pi} \int_{-\pi}^{\pi } e^{i(n-k)\theta } \\
\frac{1}{2\pi} \int_{-\pi}^{\pi} e^{im \theta} d\theta = 0 \quad \text{if }m\neq 0 \\
= \frac{1}{2\pi} \left[ \frac{e^{im \theta }}{im} \right]_{-\pi}^{\pi } = 0
\end{gather}
$$
So, kth Fourier coefficient of $D_{N}$
$$
\text{kth coeff. of }D_{N}(\theta) =
\begin{cases}
1 & \forall \lvert k \rvert \leq N \\
0  & \forall \lvert k \rvert  > N
\end{cases}
$$

$D_N(\theta) = \frac{\sin((N+\frac{1}{2})\theta)}{\sin(\theta/2)}$ Take $w=e^{i\theta}$ 
$$
D_N(\theta) = \sum_{n=-N}^{N}w^n = \sum_{n=0}^{N}w^n + \sum_{n=-N}^{-1}w^n
$$
$$
= \frac{1-w^{N+1}}{1-w} + \frac{w^{-N}-1}{1-w} = \frac{w^{-N}-w^{N+1}}{1-w} 
$$

**(Poisson Kernel):** $-\pi \leq \theta \leq \pi, 0\leq r <1$
$$
P_{r} = \sum_{n=-\infty}^{\infty} r^{\lvert n \rvert } e^{in \theta }
$$
The sequence converges absolutely and uniformly

$K^{th}$ Fourier of $P_r(\theta)$ $\frac{1}{2\pi}\int_{-\pi}^{\pi} (\sum_{n=-\infty}^{\infty}r^{|n|}e^{in\theta})e^{-ik\theta}d\theta$

$$ 
= \frac{1}{2\pi}\sum_{n=-\infty}^{\infty}\int_{-\pi}^{\pi} r^{|n|}e^{in\theta}e^{-ik\theta}d\theta 
$$
$$
= r^{|k|} 
$$

$P_r(\theta) = \frac{1-r^2}{1-2r\cos\theta + r^2}$ Take $w = re^{i\theta}$ $P_r(\theta) = \sum_{n=0}^{\infty}w^n + \sum_{n=1}^{\infty}\bar{w}^n$ 
$$ 
= \frac{1}{1-w} + \frac{\bar{w}}{1-\bar{w}} = \frac{(1-\bar{w}) + \bar{w}(1-w)}{(1-w)(1-\bar{w})} = \frac{1-\bar{w}+\bar{w}-\bar{w}w}{1-w-\bar{w}+w\bar{w}} = \frac{1-|w|^2}{1-(w+\bar{w})+|w|^2} 
$$

$$ 
= \frac{1-r^2}{|1-re^{i\theta}|^2} = \frac{1-r^2}{|(1-r\cos\theta)-ir\sin\theta|^2} 
$$
$$
= \frac{1-r^2}{(1-r\cos\theta)^2 + (r\sin\theta)^2} 
$$
$$
= \frac{1-r^2}{1-2r\cos\theta+r^2\cos^2\theta+r^2\sin^2\theta} = \frac{1-r^2}{1-2r\cos\theta+r^2} 
$$

**Question:** Let $f, g$ on $[-\pi, \pi]$, integrable $\text{and } \hat{f}(n) = \hat{g}(n) \ \forall n \in \mathbb{Z}$.
Is $f=g$ everywhere?

**Theorem:** Let $f$ be a function on circle that is integrable $\text{and } \hat{f}(n)=0 \ \forall n \in \mathbb{Z}$. Let $f$ be continuous at $\theta_{0}$ Then $f(\theta_0)=0$.

**Proof:** Let $f$ be real valued $\text{and } \theta_0=0$. If possible, let $f(0)>0$. We will find a seq. of trigonometric polynomials $P_k$ such that
$$
\int P_k(\theta) f(\theta) d\theta = 0 \text{ but } \lim_{k\to\infty} \int P_k(\theta) f(\theta) d\theta = \infty 
$$
Observe that, since $f$ is cont. at $0$ $\text{and } f(0)>0$, $\exists \delta>0$ such that
$$
f(\theta) > \frac{f(0)}{2} \quad \forall |\theta|<\delta.
$$
$$
\cos\theta = \frac{e^{i\theta} + e^{-i\theta}}{2}
$$
We define
$$
P(\theta) = \epsilon + \cos\theta 
$$
for some $\epsilon > 0$ such that $|P(\theta)| < 1 - \epsilon/2 \quad \forall \delta \le |\theta| \le \pi$ 
$\exists 0 < \eta < \delta \le \pi$ such that
$$
P(\theta) > 1 + \epsilon/2 \quad \forall 0 \le |\theta| < \eta.
$$
Define $P_k(\theta) = [P(\theta)]^k$ where $P_k$ are **trigonometric polynomials**.
Let $P_N(\theta) = \sum_{n=-N}^N a_n e^{in\theta}$
$$
\int_{-\pi}^\pi P_k(\theta) f(\theta) d\theta = \int_{-\pi}^\pi \left( \sum_{n=-N}^N a_n e^{in\theta} \right) f(\theta) d\theta
$$
$$
= \sum_{n=-N}^N a_n \int_{-\pi}^\pi e^{in\theta} f(\theta) d\theta = \sum_{n=-N}^N a_n \hat{f}(-n) = 0.
$$
$$
\left| \int_{\delta \le |\theta| \le \pi} P_k(\theta) f(\theta) d\theta \right| \le (1-\epsilon/2)^k \cdot B \cdot 2\pi \to 0 \quad \text{as } k \to \infty.
$$
($f$ integrable, $\int |f| < \infty$, $|f| \le B$)

$$
\int_{|\theta| \ge \delta} P_k(\theta) f(\theta) d\theta \to 0 \quad \forall k \in \mathbb{N}
$$

$$
\int_{\eta \le |\theta| < \delta} P_k(\theta) f(\theta) d\theta \ge \left(1+\frac{\epsilon}{2}\right)^k \frac{f(0)}{2} 2\eta \to \infty \quad \text{as } k \to \infty.
$$
$$
\begin{align}
\int_{-\pi}^\pi P_k(\theta) f(\theta) d\theta  & = \int_{|\theta|<\eta} P_k(\theta) f(\theta) d\theta  \\
 & + \int_{\eta \le |\theta| < \delta} P_k(\theta) f(\theta) d\theta \\
  & + \int_{\delta \le |\theta| \le \pi} P_k(\theta) f(\theta) d\theta 
\end{align}
$$
The first term $\to \infty$ as $k \to \infty$.
The third term $\to 0$ as $k \to \infty$.
The middle term $\to 0$ as $k \to \infty$.

Which is a contradiction therefore $f(0)=0$
Now for the general case let $f = u+iv$
$$
u(\theta) = \frac{f(\theta) + \overline{f(\theta)}}{2}, \quad v(\theta) = \frac{f(\theta) - \overline{f(\theta)}}{2i}
$$
Denote $\overline{f}(\theta) = \overline{f(\theta)}$
$$
\widehat{\overline{f}}(n) = \frac{1}{2\pi}\int_{-\pi}^{\pi} \overline{f(\theta)} e^{-in\theta} d\theta = \frac{1}{2\pi}\int_{-\pi}^{\pi} \overline{f(\theta) e^{in\theta}} d\theta = \overline{\hat{f}(-n)}.
$$
$\hat{u}(n) = \frac{1}{2}(\hat{f}(n) + \widehat{\overline{f}}(n)) = 0$ only if $\hat{v}(n) = 0 \quad \forall n \in \mathbb{Z}$.

Applying previous assertion $\implies u(\theta)$ or $v(\theta)$ is $0$ at the point of continuity. So, $f(\theta)=0$ at the point of continuity. $\quad \blacksquare$

**Corollary:** If $f$ is cont. on circle and $\hat{f}(n)=0 \ \forall n \in \mathbb{Z}$, then $f=0$.

**Corollary:** If $f$ is cont. on circle and $\sum_{n=-\infty}^\infty |\hat{f}(n)| < \infty$, then $S_N(f)(\theta) \to f(\theta)$ uniformly $\text{and}$ absolutely.

**Proof:** $\sum_{n=-\infty}^\infty \hat{f}(n) e^{in\theta}$ converges uniformly $\text{and}$ absolutely.
Take $g(\theta) = \sum_{n=-\infty}^\infty \hat{f}(n) e^{in\theta}$.
Since partial sums converge to $g(\theta)$ uniformly, so $g$ is continuous.
$$
\hat{g}(k) = \frac{1}{2\pi}\int_{-\pi}^{\pi} \left(\sum_{n=-\infty}^\infty \hat{f}(n) e^{in\theta}\right) e^{-ik\theta} d\theta
$$
$$
= \frac{1}{2\pi} \sum_{n=-\infty}^\infty \hat{f}(n) \int_{-\pi}^{\pi} e^{i(n-k)\theta} d\theta
$$
$$
= \hat{f}(k) \quad \forall k \in \mathbb{Z}.
$$
$\therefore f=g$ $\quad \blacksquare$

6/10/25
**Corollary:** If $f$ is cont. on circle $\text{and } \sum |\hat{f}(n)| < \infty$, then the Fourier Series of $f$ converges absolutely $\text{and}$ uniformly on the circle.

**Notation:** $f(x) = O(g(x))$ as $x \to a$ means $|f(x)| \le C|g(x)|$ when $x$ approaches $a$.

**Corollary:** Let $f$ be twice, continuously differentiable on the circle. Then $\hat{f}(n) = O(\frac{1}{n^2})$ as $|n| \to \infty$. Consequently, Fourier Series of $f$ converges absolutely $\text{and}$ uniformly on the circle.

**Proof:** $\forall n \ge 1$,  we have,
$$
2\pi \hat{f}(n) = \int_{-\pi}^{\pi} f(\theta) e^{-in\theta} d\theta
$$
I.B.P. (Integration by Parts)
$$
= \left[ \frac{f(\theta) e^{-in\theta}}{-in} \right]_{-\pi}^{\pi} + \int_{-\pi}^{\pi} \frac{f'(\theta) e^{-in\theta}}{in} d\theta
$$

Since $f$ is on the circle, $f(\pi)=f(-\pi)$ and $e^{-in\pi} = e^{in\pi}$ (since $n \in \mathbb{Z}$), so the first term is 0.

Again I.B.P.
$$
= \left[ \frac{f'(\theta) e^{-in\theta}}{(-in)^2} \right]_{-\pi}^{\pi} + \int_{-\pi}^{\pi} \frac{f''(\theta) e^{-in\theta}}{(-in)^2} d\theta
$$
The first term is $0$ since $f$ is $2\pi$-periodic, so is $f'$.
$f''(\theta)$ is cont. $\implies \left| \int_{-\pi}^{\pi} f''(\theta) e^{-in\theta} d\theta \right| \le \int_{-\pi}^{\pi} |f''(\theta)| d\theta \le M$.
$$
\implies 2\pi |\hat{f}(n)| \le \frac{M}{n^2}.
$$
$$
\implies \hat{f}(n) = O\left(\frac{1}{n^2}\right) \text{ as } |n| \to \infty \quad \blacksquare
$$
For second part,
$$
\sum_{n=-\infty}^\infty |\hat{f}(n)| \le \sum_{\substack{n \in \mathbb{Z} \\ \lvert n \rvert >a}} \frac{M}{n^2} \leq  2M \sum_{n=1}^\infty \frac{1}{|n|^2} < \infty
$$

Using the previous corollary, we conclude the Fourier series of $f$ converges absolutely and uniformly on the circle. $\quad \blacksquare$
### Convolution
Let $f,g$ be two $2\pi$ periodic integrable functions on $\mathbb{R}$ then, the convolution of $f,g$, denoted by $f*g$ is 
$$
f *g = \frac{1}{2\pi} \int_{-\pi}^{\pi} f(y) g(x-y) dy 
$$

If, $f,g$ are Riemann integrable then so is $F_{x}(y) = f(y)g(x-y)$. For general $f,g \in L^{1}$ we use **Fubini-Tonelli** theorem to show the integration makes sense.
$$
\int_{-\pi}^{\pi} \lvert  f* g \rvert dx = \frac{1}{2\pi} \int_{-\pi}^{\pi} \left( \int_{-\pi}^{\pi} \lvert f(y)g(x-y) \rvert dy\right)dx \leq \frac{1}{2\pi}\int_{-\pi}^{\pi}
$$

**Proposition:** Let $f,g$ be $2\pi$-periodic integrable functions on $\mathbb{R}$ then the following holds:
1. $f * (g+h) = f * g + f* h$
2. $(cf)*g = c(f*g)$
3. $(f*g)*h = f*(g*h)$
4. $f*g = g*f$
5. $\widehat{f*g}(n) = \hat{f}(n)*\hat{g}(n)$
6. $f *g$ is continuous 

**Proof:** 1. and 2. are easy to see
3. Let $f,g,h$ be continuous
$$
\begin{gather}
(f+g)*h(x) = \frac{1}{2\pi } \int_{-\pi}^{\pi} (f*g)(y)h(x-y)dy \\
= \frac{1}{(2\pi)^2} \int_{-\pi}^\pi \int_{-\pi}^\pi f(\xi) g(y-\xi) h(x-y) d\xi dy \\= \frac{1}{(2\pi)^2} \int_{-\pi}^\pi \int_{-\pi}^\pi f(\xi) g(y-\xi) h(x-y) d\xi dy  \\
= \frac{1}{(2\pi)^2} \int_{-\pi}^\pi f(\xi) \left( \int_{-\pi}^\pi g(y-\xi) h(x-y) dy \right) d\xi \text{ (by Change of Variable)}  \\
= \frac{1}{2\pi} \int_{-\pi}^\pi f(\xi) (g * h)(x-\xi) d\xi  \\
= (f * (g * h))(x)
\end{gather}
$$
4. 
$$
(f*g)(x) = \frac{1}{2\pi}\int_{-\pi}^\pi f(y)g(x-y)dy
$$
$$
= \frac{1}{2\pi}\int_{-\pi}^\pi f(x-z)g(z)dz \quad (x-y=z, dy=-dz)
$$
$$
= \frac{1}{2\pi}\int_{-\pi}^\pi f(x-z)g(z)dz = (g*f)(x)
$$
_5 and 6 we first prove for continuous functions._
 5. 
$$
\widehat{(f*g)}(n) = \frac{1}{2\pi} \int_{-\pi}^{\pi} (f*g)(x)e^{-inx} dx
$$
($f, g$ continuous) 
$$
= \frac{1}{(2\pi)^2} \int_{-\pi}^{\pi} \left( \int_{-\pi}^{\pi} f(y)g(x-y)dy \right) e^{-inx} dx
$$
$$
= \frac{1}{(2\pi)^2} \int_{-\pi}^{\pi} f(y)e^{-iny} \left( \int_{-\pi}^{\pi} g(x-y)e^{-in(x-y)}dx \right) dy
$$
$$
= \frac{1}{2\pi} \int_{-\pi}^{\pi} \hat{g}(n) \hat{f}(n)e^{-iny} dy = \hat{g}(n)\hat{f}(n)
$$
6. g is continuous on $\mathbb{R}$ and $2\pi$ periodic, so g is uniformly continuous on $\mathbb{R}$.
g continuous on $[-\pi, \pi]$

>[!info]
>g is continuous on $[-\pi,\pi]$ $\implies$ g is uniformly continuous on $[-\pi, \pi]$
>g is $2\pi$-periodic $\implies$ g is uniformly continuous on $\mathbb{R}$.

Given $\epsilon > 0, \exists \delta > 0$ such that
$|g(x_1)-g(x_2)| < \epsilon \quad \forall |x_1-x_2|<\delta$.
$\forall |x_1-x_2|<\delta$, $|(f*g)(x_1) - (f*g)(x_2)|$
$$ = \left|\frac{1}{2\pi}\int_{-\pi}^\pi (f(y)g(x_{1}-y) - f(y){g}(x_{2}-y))dy\right| $$ $$ \leq \frac{1}{2\pi}\int_{-\pi}^\pi |f(y)||g(x_{1}-y)-{g}(x_{2}-y)|dy $$
$$
= \frac{1}{2\pi} \int_{-\pi}^\pi |f(y)| |g(x_{1})-g(z_{2})| dy
$$
$$
\leq \frac{\epsilon}{2\pi} \cdot B \quad \text{where } \int_{-\pi}^{\pi} |f|dx = B
$$
$\implies f*g$ is continuous.

**Lemma:** Let $f$ be integrable on the circle and bounded by $B$. Then there exists a sequence of continuous functions $\{f_k\}_{k=1}^\infty$ on the circle such that $\{f_k\} \to f$ in $L^1$, i.e., $\int_{-\pi}^{\pi} |f(x) - f_k(x)| dx \to 0$ as $k \to \infty$ and $\sup_{x\in[- \pi,\pi]} |f_k(x)| \leq B \quad \forall k$.

**Proof:** We skip this proof😴(Refer Stein and Shakarchi)

Now we show 5 and 6 for $f,g$ integrable on the circle.

We know that $f*g$ is $2\pi$ periodic and integrable. There exist sequences of continuous functions, $\{f_k\}$ and $\{g_k\}$, such that $\{f_k\} \to f$ in $L^1$ and $\{g_k\} \to g$ in $L^1$. i.e., $\int_{-\pi}^{\pi} |f_k(x)-f(x)|dx \to 0$ and $\int_{-\pi}^{\pi} |g_k(x)-g(x)|dx \to 0$ as $k\to\infty$.

We will show that $\{f_k * g_k\} \to f*g$ uniformly. We have,
$$
f*g - f_k*g_k = (f-f_k)*g + f_k*(g-g_k)
$$
We will show that the first term goes to zero uniformly. 
$$
\begin{align}
|(f-f_k)*g(x)|  & \leq \frac{1}{2\pi} \int_{-\pi}^\pi |(f-f_k)(y)| |g(x-y)| dy  \\
 & \leq \frac{1}{2\pi} \sup_{y\in[-\pi,\pi]} |g(y)| \int_{-\pi}^\pi |f(y)-f_k(y)| dy \to 0 \quad \text{as} \ k\to\infty
\end{align}
$$

$f - f_k \to 0$ uniformly. ($\implies ||f-f_k||_\infty \to 0$). (The RHS of the inequality above is independent of $x$)
Similarly $f_{k} * (g - g_{k}) \to 0$ uniformly,
$$
\implies f_k*g_{k} \to f*g \text{ uniformly}
$$
$$
\implies f*g \text{ is continuous.}
$$
$$
\begin{matrix}
\widehat{f_k*g_k}(n) &  = &  \hat{f}_k(n) \hat{g}_k(n) \\
\downarrow &  & \downarrow \\
\widehat{f*g}(n)  & =  & \hat{f}(n) \hat{g}(n)
\end{matrix}
$$
$$
\begin{align}
\lim_{k\to\infty} \widehat{f_k*g_{k}}(x)  & = \lim_{k\to\infty} \frac{1}{2\pi} \int_{-\pi}^\pi (f_k*g_{k})(y) e^{-in\theta} d\theta  \\
 & = \frac{1}{2\pi} \int_{-\pi}^{\pi} (f * g) e^{-inx}dx  \\
 & = \widehat{f*g} (n)
\end{align}
$$
Also,
$$
|\hat{f}(n) - \hat{f}_k(n)| = \left| \frac{1}{2\pi} \int_{-\pi}^\pi (f(x) - f_k(x)) e^{-inx} dx \right|
$$
$$
\le \frac{1}{2\pi} \int_{-\pi}^\pi |f(x) - f_k(x)| dx \to 0 \quad \text{as } k \to \infty.
$$
$$
\implies \hat{f}_k(n) \to \hat{f}(n) \quad \forall k.
$$
Therefore, $\widehat{f_k*g_k}(n) \to \hat{f}(n) \hat{g}(n) \widehat{f*g}(n)$. So, $\widehat{f*g}(n) = \hat{f}(n) \hat{g}(n) \quad \forall n \in \mathbb{Z}$.

---
### Good Kernels:
A family of functions $\{K_n(x)\}$ on the circle is called a **family of good kernels** if:
i) $\frac{1}{2\pi} \int K_n(x) dx = 1 \quad \forall n \in \mathbb{Z}^+$.
ii) $\frac{1}{2\pi} \int |K_n(x)| dx \le M \quad \forall n \ge 1$.
iii) $\frac{1}{2\pi} \int_{\delta \le |x| \le \pi} |K_n(x)| dx \to 0 \quad \text{as } n \to \infty \text{ for any } 0 < \delta \le \pi$.

**Theorem:** Let $f$ be an integrable function on the circle, then
$$
\lim_{n\to\infty} f*K_n(x) \to f(x)
$$
when $f$ is cont. at $x$. If $f$ is cont. on the circle, then $f*K_n \to f$ uniformly.

**Proof:** Let $f$ be cont. at $x \text{ and } \epsilon > 0$. Then $\exists \delta > 0$ s.t.
$|f(x-y) - f(x)| < \epsilon$ when $|y| \le \delta$.
$$
|f*K_n(x) - f(x)| = \left| \frac{1}{2\pi} \int_{-\pi}^\pi K_n(y) f(x-y) dy - \frac{1}{2\pi} \int_{-\pi}^\pi K_n(y) f(x) dy \right|
$$
$$
\le \frac{1}{2\pi} \int_{-\pi}^\pi |K_n(y)| |f(x-y) - f(x)| dy
$$
$$
= \frac{1}{2\pi} \left[ \int_{|y| \le \delta} |K_n(y)| |f(x-y) - f(x)| dy + \int_{|y| > \delta} |K_n(y)| |f(x-y) - f(x)| dy \right]
$$
$$
\le \frac{1}{2\pi} \left[ \epsilon \int_{|y| \le \delta} |K_n(y)| dy + 2B \int_{|y| > \delta} |K_n(y)| dy \right]
$$
$$
< \frac{\epsilon M}{2\pi} + \frac{2B\epsilon}{2\pi} \quad \text{for } n \ge N(\delta, \epsilon) \text{ (since } f \text{ is bounded)}
$$
$$
= \frac{C\epsilon}{2\pi}
$$
$\implies f*K_n(x) \to f(x)$ as $n \to \infty$.

If $f$ is cont. on the circle, then $f$ is uniformly continuous. Then $\delta$ is independent of $x$. Therefore, $f*K_n \to f$ uniformly.

**Note:** $S_N(\theta)$ is not a family of good kernels. One can show
$$
\frac{1}{2\pi} \int_{-\pi}^\pi |D_N(\theta)| d\theta \ge C \log N \quad \text{for large } N.
$$

### Cesàro Summability

Let $\sum a_k$ be any series
$$
S_n = \sum_{k=0}^n a_k, \quad \sigma_N = \frac{S_0 + S_1 + \cdots + S_{N-1}}{N}
$$
If $\sigma_N \to S$, then we say $\sum a_n$ is **Cesàro summable** and $S$ is the Cesàro sum.

### Fejér Kernel

Let $S_n(f)(\theta)$ be the partial sums of the Fourier series of $f$.
$$
\sigma_N(f)(x) = \frac{S_0(f)(x) + S_1(f)(x) + \cdots + S_{N-1}(f)(x)}{N}
$$
$$
= \frac{f * D_0(x) + f * D_1(x) + \cdots + f * D_{N-1}(x)}{N}
$$
$$
= f * \left( \frac{D_0(x) + D_1(x) + \cdots + D_{N-1}(x)}{N} \right)
$$
Take $F_N(x) = \frac{D_0(x) + \cdots + D_{N-1}(x)}{N}$.
$f * F_N(x) \to f(x)$
$f * F_N \to f$ unif.

$D_N(x) = \frac{\sin((N+1/2)x)}{\sin(x/2)}$
$$
F_N(x) = \frac{1}{N} \sum_{k=0}^{N-1} \frac{\sin((k+1/2)x)}{\sin(x/2)} = \frac{1}{N \sin(x/2)} \sum_{k=0}^{N-1} \sin((k+1/2)x)
$$
$$
= \frac{1}{N \sin^2(x/2)} \sum_{k=1}^{N} (\cos(kx) - \cos((k+1)x))
$$
$$
= \frac{1}{N \sin^2(x/2)} (1 - \cos(Nx)) = \frac{\sin^2(Nx/2)}{N \sin^2(x/2)}.
$$

**Proposition:** $F_N$ is a good kernel.
(i) $\frac{1}{2\pi} \int F_N(x) dx = \frac{1}{2\pi} \int \frac{D_0(x) + \cdots + D_{N-1}(x)}{N} dx = 1$

(ii) For any $n$, $\frac{1}{2\pi} \int_{-\pi}^\pi |F_N(x)| dx = \frac{1}{2\pi} \int_{-\pi}^\pi F_N(x) dx = 1$.

(iii) For each $0 < \delta \le \pi$, $\sin^2(x/2) \ge C_\delta > 0 \quad \forall \delta \le |x| \le \pi$.
$$
\frac{1}{2\pi} \int_{\delta \le |x| \le \pi} |F_N(x)| dx = \frac{1}{2\pi} \int_{\delta \le |x| \le \pi} \frac{\sin^2(Nx/2)}{N \sin^2(x/2)} dx \le \frac{1}{2\pi} \int_{\delta \le |x| \le \pi} \frac{1}{N C_\delta} dx < \frac{1}{N C_\delta} \cdot \frac{1}{2\pi} 2\pi \to 0 \quad \text{as } N \to \infty.
$$

**Fejér's Theorem:** If $f$ is an integrable function on the circle, the Fourier Series of $f$ is Cesàro summable to $f(x)$ at the point of continuity. If $f$ is cont. on the circle, then the Fourier Series of $f$ uniformly Cesàro summable to $f$.

**Corollary:** Let $f$ be a continuous function on the circle, then $f$ can be approximated uniformly by a sequence of trigonometric polynomials.

### Abel Summability

$\sum_{k=0}^{\infty} c_k$ is called **Abel summable** to some value $S$ if for each $0 \le r < 1$,
$$
A(r) = \sum_{k=0}^{\infty} c_k r^k
$$
converges and
$$
S = \lim_{r \to 1^-} A(r).
$$
**Example:** $1 - 2 + 3 - 4 + 5 - \cdots = \sum_{k=0}^{\infty} (-1)^k (k+1)$.

$$
A(r) = \sum_{k=0}^{\infty} (-1)^k (k+1) r^k = \frac{1}{(1+r)^2}.
$$
$$
\lim_{r \to 1^-} A(r) = \frac{1}{(1+1)^2} = \frac{1}{4}.
$$
But the above series is **not** Cesàro summable.

If $\sum_{k=0}^{\infty} c_k$ is **Cesàro summable** then $c_n/n \to 0$ as $n \to \infty$.

---

$$
\frac{S_0 + \cdots + S_{n-1}}{n} \to a \quad (\text{Cesàro})
$$
$$
\frac{S_0 + \cdots + S_n}{n} \to a
$$
$$
\implies \frac{S_0 + \cdots + S_n}{n} - \frac{S_0 + \cdots + S_{n-1}}{n} = \frac{\sigma_n}{n} \to 0
$$
$$
\implies \frac{c_n}{n} \to 0 \quad \text{as } n \to \infty \text{ is not enough.}
$$
**Theorem:** Cesàro Summability $\implies$ Abel Summability

---

**Recall:** $0 \le r < 1$.
$$
P_r(\theta) = \sum_{n=-\infty}^{\infty} r^{|n|} e^{in\theta} = \frac{1-r^2}{1-2r\cos\theta+r^2}.
$$
$$
f \sim \sum_{n=-\infty}^{\infty} \hat{f}(n) e^{in\theta}
$$
$$
A_r(f)(\theta) = \sum_{n=-\infty}^{\infty} r^{|n|} \hat{f}(n) e^{in\theta} = \sum_{n=-\infty}^{\infty} r^{|n|} \left(\frac{1}{2\pi} \int_{-\pi}^{\pi} f(t)e^{-int} dt\right) e^{in\theta}
$$

---

$$
\frac{1}{2\pi} \sum_{n=-\infty}^{\infty} r^{|n|} \left| \int_{-\pi}^{\pi} f(t)e^{-int} dt \right| e^{in\theta}
$$
$$
\le \frac{1}{2\pi} \sum_{n=-\infty}^{\infty} r^{|n|} \int_{-\pi}^{\pi} |f(t)| dt \le B \sum_{n=-\infty}^{\infty} r^{|n|} < \infty.
$$
$\implies (*)$ converges absolutely $\text{and}$ uniformly.
So, we can interchange $\sum \text{ and } \int$.
Therefore, $(*)$ implies:
$$
A_r(f)(\theta) = \frac{1}{2\pi} \int_{-\pi}^{\pi} f(t) \left( \sum_{n=-\infty}^{\infty} r^{|n|} e^{in(\theta-t)} \right) dt
$$
$$
= f * P_r(\theta) \quad \left(f * P_r(\theta) \to f(\theta)\right)
$$


**Prop:** $\{P_r(\theta)\}_{0<r<1}$ is a family of **good kernels** as $r \to 1^-$.

**Proof:**
$$
P_r(\theta) = \frac{1-r^2}{1-2r\cos\theta+r^2}
$$
$1-2r\cos\theta+r^2 = (1-r)^2 + 2r(1-\cos\theta)$. So $P_r(\theta) \ge 0$
$\forall \ 0 \le r < 1$
$$
\frac{1}{2\pi} \int_{-\pi}^\pi P_r(\theta) d\theta = \frac{1}{2\pi} \int_{-\pi}^\pi |P_r(\theta)| d\theta
$$
$$
= \frac{1}{2\pi} \int_{-\pi}^\pi \sum_{n=-\infty}^\infty r^{|n|} e^{in\theta} d\theta.
$$
$$
= \frac{1}{2\pi} \sum_{n=-\infty}^\infty r^{|n|} \int_{-\pi}^\pi e^{in\theta} d\theta = 1.
$$
Properties (i) and (ii) of good kernels have been verified.

---

Let $\delta > 0$. For $\frac{1}{2} \le r < 1$ and $\delta \le |\theta| \le \pi$, then
$$
(1-r)^2 + 2r(1-\cos\theta) > C_\delta > 0.
$$
$$
\frac{1}{2\pi} \int_{\delta \le |\theta| \le \pi} |P_r(\theta)| d\theta = \frac{1}{2\pi} \int_{\delta \le |\theta| \le \pi} \frac{1-r^2}{1-2r\cos\theta+r^2} \le \frac{1-r^2}{C_\delta} \to 0 \quad as \ r \to 1^-
$$
So, $\{P_r(\theta)\}_{0<r<1}$ is a good kernel as $r \to 1^-$.

---

Therefore, if $f$ is continuous at $\theta$,
$$
f * P_r(\theta) \to f(\theta).
$$
$\implies A_r(f)(\theta) \to f(\theta)$.
$\implies$ Fourier Series of $f$ is Abel summable to $f$ at the point of continuity.

Moreover, if $f$ is continuous on the circle, then the Fourier Series of $f$ uniformly Abel summable to $f$.

**Next goal:**
$$
\int_{-\pi}^{\pi} |S_N(f)(\theta) - f(\theta)|^2 d\theta \to 0 \quad as \ N \to \infty.
$$
Mean Square Convergence or convergence in $L^2$ norm.

### Inner Product

Let $V$ be a vector space over $\mathbb{C}$.
A map $\langle \cdot, \cdot \rangle: V \times V \to \mathbb{C}$ is called an **inner product** if:

i) **(Positive definite norm)**
$$
\langle x, x \rangle \ge 0 \quad \forall x \in V
$$
$$
\langle x, x \rangle = 0 \quad \text{iff } x = 0
$$

ii) **(Conjugate symmetry)**
$$
\langle x, y \rangle = \overline{\langle y, x \rangle}
$$

iii) **(Linearity in the first variable)** $\forall x, y, z \in V, \lambda \in \mathbb{C}$
$$
\langle \lambda x + y, z \rangle = \lambda \langle x, z \rangle + \langle y, z \rangle
$$

---

Define $||\cdot||$ on $V$ by $||x|| = \sqrt{\langle x,x \rangle}$.
We will show that $||x||$ is a norm on $V$. If $V$ is complete with respect to the norm, then $V$ is said to be a **Hilbert space**.

**Ex:** $\mathbb{C}^n$ with the below inner product
$$
\langle x, y \rangle = \sum_{i=1}^n x_i \overline{y_i}.
$$
$x = (x_1, \ldots, x_n)$, $y = (y_1, \ldots, y_n)$.
$$
||x|| = \sqrt{\sum_{i=1}^n |x_i|^2}.
$$

**Def:** Let $V$ be an **Inner Product Space** and $x, y \in V$. $x$ and $y$ are said to be **orthogonal** (denoted by $x \perp y$) if
$$
\langle x, y \rangle = 0.
$$

**Theorem:**
(i) **(Pythagorean theorem)** If $x \perp y$, then $||x+y||^2 = ||x||^2 + ||y||^2$.

(ii) **(Cauchy-Schwarz inequality)** $\forall x, y \in V$
$$
|\langle x, y \rangle| \le ||x|| \cdot ||y||.
$$

**Proof:** (i)
$$
||x+y||^2 = \langle x+y, x+y \rangle
$$
$$
= \langle x, x \rangle + \langle y, x \rangle + \langle x, y \rangle + \langle y, y \rangle
$$
Since $x \perp y$, $\langle x, y \rangle = 0$, and by conjugate symmetry, $\langle y, x \rangle = \overline{\langle x, y \rangle} = 0$.
$$
= ||x||^2 + 0 + 0 + ||y||^2
$$
$$
= ||x||^2 + ||y||^2
$$

#incomplete 



![[IMG_20251024_141426.jpg]]

$\mathcal{R} = \text{Set of all Riemann}$
$L^2([-a, a])$
$$
\langle f, g \rangle_2 = \frac{1}{2\pi} \int_{-\pi}^\pi f(\theta) \overline{g(\theta)} d\theta
$$

**Theorem:** Let $f$ be integrable on the circle. Then
i) $||f - S_N(f)||_2 \to 0$ as $N \to \infty$. In other words,
$$
\frac{1}{2\pi} \int_{-\pi}^\pi |f(\theta) - S_N(f)(\theta)|^2 d\theta \to 0 \quad \text{as } N \to \infty.
$$
ii) **(Parseval's Equality):**
$$
\sum_{n=-\infty}^\infty |\hat{f}(n)|^2 = ||f||_2^2 = \frac{1}{2\pi} \int_{-\pi}^\pi |f(\theta)|^2 d\theta.
$$

**Proof:**
For $n \in \mathbb{Z}$, let $\{e_n = e^{in\theta}\}$ be an orthonormal set in $R$.
Because,
$$
\langle e_n, e_m \rangle = \frac{1}{2\pi} \int_{-\pi}^\pi e^{in\theta} e^{-im\theta} d\theta = \frac{1}{2\pi} \int_{-\pi}^\pi e^{i(n-m)\theta} d\theta
$$
$$
= \begin{cases} 1 & \text{if } n=m \\ 0 & \text{otherwise} \end{cases}
$$

![[IMG_20251024_141610.jpg]]

Let $a_n = \langle f, e_n \rangle$. So, $S_N(f) = \sum_{|n|\le N} a_n e_n$.
$$
(f - S_N(f)) \perp e_n \quad \forall |n| \le N.
$$
$$
\langle f - \sum_{|k|\le N} a_k e_k, e_n \rangle = \langle f, e_n \rangle - a_n \langle e_n, e_n \rangle = a_n - a_n = 0 \quad \forall |n| \le N.
$$
Therefore,
$$
(f - S_N(f)) \perp \sum_{|n|\le N} b_n e_n.
$$

---

**Conclusion 1:**
$$
f = f - S_N(f) + \sum_{|n|\le N} a_n e_n
$$
$$
\implies ||f||^2 = ||f - S_N(f)||^2 + \left|\left|\sum_{|n|\le N} a_n e_n\right|\right|^2 \quad \text{(Using Pythagoras)}
$$
$$
= ||f - S_N(f)||^2 + \sum_{|n|\le N} |a_n|^2.
$$
$$
\implies \sum_{|n|\le N} |a_n|^2 \le ||f||^2.
$$
$$
\implies \sum_{n=-\infty}^\infty |a_n|^2 \le ||f||^2.
$$

![[IMG_20251024_142526.jpg]]

Let $\{\phi_n\}_{n\in\mathbb{Z}}$ be an orthonormal set and set $c_n = \langle f, \phi_n \rangle$.
Then
$$
\sum_{n=-\infty}^\infty |c_n|^2 \le ||f||^2 \quad \text{(Bessel's Inequality)}
$$
**Conclusion 2:** For some complex number $\alpha$,
$$
||f - \sum_{|n|\le N} c_n \phi_n|| = ||f - S_N(f) + \sum_{|n|>N} c_n \phi_n|| \quad \text{where } c_n = \hat{f}(n).
$$
Using Pythagoras,
$$
||f - \sum_{|n|\le N} c_n \phi_n||^2 = ||f - S_N(f)||^2 + ||\sum_{|n|>N} c_n \phi_n||^2
$$
$$
\implies ||f - S_N(f)|| \le ||f - \sum_{|n|\le N} c_n \phi_n||
$$
(Best approximation theorem)

![[IMG_20251024_143604.jpg]]


Let $f$ be continuous. For $\epsilon > 0$, $\exists$ a trigonometric polynomial $P$ ($\text{deg } P = M, \text{ say}$) s.t.
$$
|f(\theta) - P(\theta)| < \epsilon \quad \forall \theta \in [-\pi, \pi]
$$
$$
\implies \frac{1}{2\pi} \int_{-\pi}^\pi |f(\theta) - P(\theta)|^2 d\theta < \epsilon^2 \quad \left(P = \sum_{|n|\le M} c_n e_n\right)
$$
$$
\implies ||f - P||_2^2 < \epsilon^2.
$$

![[IMG_20251024_143627.jpg]]

By Best Approximation Theorem,
$$
||f - S_N(f)||_2 \le ||f - P||_2 \le \epsilon \quad \forall N \ge M.
$$
$$
\implies ||f - S_N(f)||_2 \to 0 \quad \text{as } N \to \infty \quad (\text{Since } \epsilon > 0 \text{ is arbitrary}).
$$
Now, if $f$ is Riemann integrable on $[-\pi, \pi]$, then for $\epsilon > 0$, $\exists$ a cont. function $g$ on $[-\pi, \pi]$ s.t.
$$
\sup_{\theta \in [-\pi, \pi]} |g(\theta)| \le \sup_{\theta \in [-\pi, \pi]} |f(\theta)| \quad \text{and } \frac{1}{2\pi} \int_{-\pi}^\pi |f(\theta) - g(\theta)| d\theta < \epsilon.
$$

---

$$
||f - g||_2^2 = \frac{1}{2\pi} \int_{-\pi}^\pi |f(\theta) - g(\theta)|^2 d\theta
$$
$$
\le \frac{1}{2\pi} \int_{-\pi}^\pi |f(\theta) - g(\theta)| |f(\theta) - g(\theta)| d\theta
$$
$$
\le \frac{2B}{2\pi} \int_{-\pi}^\pi |f(\theta) - g(\theta)| d\theta \quad (\text{where } 2B = \sup |f(\theta)-g(\theta)| \le 2 \sup |f|)
$$
$$
\le \frac{B \epsilon}{2\pi}
$$

![[IMG_20251024_150508.jpg]]

Let $P$ be the trigonometric polynomial which approximates $g$.
i.e., $||g - P||_2 < \epsilon$.
$$
||f - P||_2 \le ||f - g||_2 + ||g - P||_2
$$
$$
\le \frac{B\epsilon}{2\pi} + \epsilon = \left(\frac{B}{2\pi} + 1\right)\epsilon.
$$
Using Best Approximation Theorem,
$$
||f - S_N(f)||_2 \le ||f - P||_2 < \left(\frac{B}{2\pi} + 1\right)\epsilon.
$$
Since $\epsilon$ is arbitrary, $||f - S_N(f)||_2 \to 0 \quad \text{as } N \to \infty$.

---

ii)
$$
||f||^2 = ||f - S_N(f)||^2 + \sum_{|n|\le N} |a_n|^2 \quad \left(\text{where } a_n = \langle f, e_n \rangle = \frac{1}{2\pi} \int_{-\pi}^\pi f(\theta) \overline{e_n(\theta)} d\theta\right)
$$
As $N \to \infty$, $||f - S_N(f)||^2 \to 0$.
$$
\implies \sum_{n=-\infty}^\infty |a_n|^2 = ||f||^2.
$$
$$
\implies \sum_{n=-\infty}^\infty |\hat{f}(n)|^2 = ||f||_2^2 = \frac{1}{2\pi} \int_{-\pi}^\pi |f(\theta)|^2 d\theta.
$$

![[IMG_20251024_150522.jpg]]

**Remark:**
$$
\sum_{n \in \mathbb{Z}} |\hat{f}(n)|^2 = ||f||^2 < \infty.
$$
$\{ \hat{f}(n) \}_{n \in \mathbb{Z}} \in l^2(\mathbb{Z})$.

**Riemann-Lebesgue Lemma:** Let $f$ be integrable on the circle. Then
$$
\hat{f}(n) \to 0 \quad \text{as } |n| \to \infty.
$$
**Proof:** Follows from the previous theorem.

$S_N(f) \to f$ in $L^2$.
$f \in L^2$. $f \in \mathcal{R}$. $\{e_n = e^{in\theta}\}$ is P.C.

---

For any inner product space the following result holds:

**Prop:** Let $X$ be an **inner product space** and $\{u_n\}_{n=1}^\infty$ be an **orthonormal set** in $X$. Then
$$
\sum | \langle x, u_n \rangle |^2 \le ||x||^2 \quad \forall x \in X.
$$
Equality in the above holds iff
$$
x = \sum_{n=1}^\infty \langle x, u_n \rangle u_n.
$$
#incomplete 

![[IMG_20251027_100058.jpg]]
![[IMG_20251027_100506.jpg]]

![[IMG_20251027_102243.jpg]]

![[IMG_20251027_102759.jpg]]

![[IMG_20251027_105204.jpg]]
![[IMG_20251027_105214.jpg]]