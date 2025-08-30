---
draft: false
---

**Muhammed Shameel KV**
bmat2330@isibang.ac.in

$1.$ $(\implies )$ Consider any two sequence $\{ u_{n} \},\{ v_{n} \}$ with $\rho(v_{n},u_{n}) \to 0$ as $n \to \infty$. Since $f$ is uniformly continuous we have that $\exists \delta>0$ such that

$$
\sigma (f(x),f(y))< \epsilon  \quad \rho(x,y)< \delta
$$

Now we choose $N \in \mathbb{N}$ such that $\rho(v_{n},u_{n}) < \delta$ for $n \geq N$. Hence we have that

$$
\sigma(f(v_{n}),f(u_{n})) < \epsilon
$$

Hence

$$
\lim_{ n \to \infty } \sigma(f(v_{n}),f(u_{n})) = 0
$$

$(\impliedby )$ Assume the contrary that $f$ is not uniformly continuous. i.e. $\exists \epsilon>0$ such that for every $\delta >0$ we have $x_{\delta },y_{\delta }$ such that $\rho(x_{\delta},y_{\delta })<\delta$, but

$$
\sigma(f(x_{\delta}),f(y_{\delta })) \geq \epsilon \tag{1}
$$

Now we take $\delta = \frac{1}{n}, n \in \mathbb{N}$. Now we have 2 sequences $x_{\frac{1}{n}},y_{\frac{1}{n}}$ such that

$$
\rho \left( x_{\frac{1}{n}},y_{\frac{1}{n}} \right) \leq \frac{1}{n}
$$

Hence $\lim_{ n \to \infty } \rho\left( x_{\frac{1}{n}},y_{\frac{1}{n}} \right) = 0$. But by assumption we have that,

$$
\lim_{ n \to \infty } \sigma\left( f\left( x_{\frac{1}{n}} \right), f\left( y_{\frac{1}{n}} \right) \right) = 0
$$

But $(1)$ implies that,

$$
\lim_{ n \to \infty } \sigma\left( f\left( x_{\frac{1}{n}} \right),f\left( y_{\frac{1}{n}} \right) \right) \geq \epsilon
$$

Which is a contradiction. $\quad \blacksquare$

$2.$ Consider $A_{n} = [n,\infty ),n \in \mathbb{N}$. Then it is clear that $A_{1} \supsetneq A_{2} \supsetneq A_{3} \supsetneq \dots$ , Hence $A_{n}$ is a descending sequence of closed sets. Now,

$$
\bigcap_{n \in \mathbb{N}} A_{n} = \varnothing
$$

Since every $r \in \mathbb{R}, \exists N \in \mathbb{N}$ such that $N> r$ and hence $r \not\in A_{N}$.

$3.$
$(i)$ By **Weierstrass Approximation theorem** we have that $B_{n}\left( x,|x- \frac{1}{2}| \right)$, the Bernstein polynomials of $\left\lvert  x - \frac{1}{2}  \right\rvert$, converges uniformly to $|x- \frac{1}{2}|$, and since all polynomials are in $C^{\infty }$ we have that $B_{n}\left( x,|x- \frac{1}{2}| \right)$ is differentiable in $(0,1)$ for all $n \in \mathbb{N}$. But $|x - \frac{1}{2}|$ is not differentiable at $\frac{1}{2}$. So there is a sequence in $D$ which converges to an element outside it. Hence $D$ is not complete.

$(ii)$ We see that for any polynomial $f$ on $[0,1]$ since its derivative $f'$ is also continuous and hence bounded on $[0,1]$, a compact set. Hence it is Lipschitz since

$$
\lvert f(x) - f(y) \rvert = |f'(c)|\lvert x-y \rvert  \leq M \lvert x-y \rvert \quad \text{for some } c \in (x,y)
$$

So polynomials on $[0,1]$ are Lipschitz, then see that for $g = \sqrt{ x }$, we have $g' = \frac{1}{\sqrt{ x }}$ which goes to $\infty$ as $x \to 0$. So from mean value theorem we have,

$$
\frac{\lvert \sqrt{ x } - \sqrt{ y } \rvert} {x-y} = \frac{1}{\sqrt{ c }} > M \quad \text{if } x,y < \frac{1}{M^{2}}
$$

So $g$ is not Lipschitz in $[0,1]$, But like in $(i)$ we have that $\{ B_{n}(x,\sqrt{ x }) \}$, which is a sequence of polynomials, hence Lipschitz on $[0,1]$, converges to $\sqrt{ x }$ which is not Lipschitz, so $\mathcal{L}$ is not complete.

$4.$ If $y \in X\setminus K$ then we have that,

$$
\text{dist}(y,K) = \inf_{k \in K} \rho(y,k)
$$

We show that the function $f:K\to \mathbb{R}, f(x) = \rho(y,x)$ is continuous and hence attains a minimum on the compact set $K$. Now WLOG assume that $\rho(x_{1},y)\geq \rho(x_{2},y)$ otherwise rename $x_{1},x_{2}$.

$$
\begin{align*} \\
\rho(x_{1},y) &\geq \rho(x_{1},x_{2}) + \rho(x_{2},y) ) \\
\implies \rho(x_{1},y)-\rho(x_{2},y) &\leq \rho(x_{1},x_{2}) \\
\implies \lvert \rho(x_{1},y)-\rho(x_{2},y) \rvert  &\leq \rho(x_{1},x_{2})
\end{align*}
$$

Hence we have,

$$
\implies \lvert \rho(x_{1},y)-\rho(x_{2},y) \rvert  < \varepsilon \quad \text{for }\rho(x_{1},x_{2})< \varepsilon
$$

So $f(x)=\rho(y,x)$ is a continuous function on the metric space X. Hence it attains a minimum on any compact set. Hence $\exists x \in K$ such that $\rho(x,y) = \text{dist}(y,K)$.

Now to show that compactness is needed, we can consider the subspace $X = (0,1) \bigcup  \{ 2 \}$ and $K = (0,1)$ , then $K$ is not a compact subset by **Heine-Borel** as it is not closed in $\mathbb{R}$. Now let $y = 2$ and we see that $\text{dist}(y,K)=1$, but no point in $(0,1)$ can attain it as $|x-2| = |x-1|+|1-2| >1$ for $x \in (0,1)$. $\quad \blacksquare$

$5.$ Given that $A$ is compact and $B$ is closed and we suppose that $A \bigcap B=\varnothing$, Now assume for contradiction that $\text{dist}(A,B)=0$. Hence there exists a sequence of real numbers $\{ \rho(a_{n},b_{n}) \}$ such that $\lim_{ n \to \infty } \rho(a_{n},b_{n}) = 0$. Now since A is compact we have that $\{ a_{n} \}$ has a subsequence which will converge, say $\{ a_{n_{k}} \} \subseteq \{ a_{n} \}$ converges to $a$. Now we also have,

$$
\begin{gather*}
\lim_{ n \to \infty } \rho(a_{n_{k}},b_{n_{k}}) = 0 \\
\rho(b_{n_{k}},a_{n_{k}})+\rho(a_{n_{k}},a) \geq \rho(b_{n_{k}},a) \\
\implies \lim_{ n \to \infty } \rho(b_{n_{k}},a) \leq \lim_{ n \to \infty } \rho(b_{n_{k}},a_{n_{k}}) + \lim_{ n \to \infty } \rho(a_{n_{k}},a) = 0
\end{gather*}
$$

Hence the sequence $b_{n_{k}}$ converges to $a$. But $A \bigcap B = \varnothing$. Which is a contradiction.

Conversely, if $\text{dist}(A,B)>0$ and assume for contradiction that $A \bigcap B \neq \varnothing$. Then let $x \in A \bigcap B$ hence $\rho(x,x) = 0$ implies $\text{dist}(A,B) = 0\quad \blacksquare$

$6.$
![[SVG/tikzdiagram13.svg|diagram]]

Consider $V^{c}$ and $K$, $K$ is compact and $V^{c}$ is closed and since $K \subseteq V \implies K \bigcap V^{c}= \varnothing$. Hence we can use $(5.)$ above to say $\delta =\text{dist}(K,V^{c}) >0$. Now consider the open sets,

$$
\begin{gather*}
U = \bigcup_{k \in K} B\left(k,\frac{\delta}{3} \right) \\
W = \bigcup_{x \in V^{c}} B\left(x, \frac{\delta}{3}\right)
\end{gather*}
$$

Then $U \bigcap W = \varnothing$, since otherwise if $a \in U \bigcap W$ implies $\exists x_{0},k_{0}$ such that $\rho(x_{0},a) < \frac{\delta}{3}, \rho(x_{1},a)< \frac{\delta}{3}$. So we get

$$
\frac{2}{3}\delta > \rho(x_{0},a) + \rho(k_{0},a) \geq \rho(x_{0},k_{0}) \geq \text{dist}(K,V^{c}) = \delta
$$

So we get that $U \bigcap W = \varnothing$. Hence $U \subseteq W^{c} \implies \overline{U} \subseteq W^{c} \implies \overline{U}\bigcap W=\varnothing$ and since $V^{c} \subseteq W$ we have $\overline{U} \bigcap V^{c} = \varnothing \implies \overline{U} \subseteq V$. Hence $K \subseteq U \subseteq \overline{U} \subseteq V \quad \blacksquare$

$7.$ See that $f(x) = \rho(x,T(x))$ is continuous, since for any convergent sequence $\{ x_{n} \} \to x$, and since $T$ is continuous, seen easily from the given condition, so $\{ T(x_{n}) \}\to T(x)$ we have,

$$
\begin{gather*}
\rho(x_{n},T(x_{n})) \leq \rho(x_{n},x) + \rho(x,T(x)) + \rho(T(x),T(x_{n})) \\
\rho(x,T(x)) \leq \rho(x,x_{n}) + \rho(x_{n},T(x_{n})) + \rho(T(x_{n}),T(x)) \\
\implies \lvert  \rho(x_{n},T(x_{n})) -\rho(x,T(x) \rvert \leq \rho(x_{n},x)  + \rho(T(x),T(x_{n})) \to 0
\end{gather*}
$$

Hence there exists $f(x_{0})$ which is minimum of $f$ over $X$. Then if the minimum is 0, we are done. Otherwise if $\inf_{x \in X} \rho(x,T(x)) = \delta$ and let $x_{0}$ be the point such that $\rho(x_{0},T(x_{0})) = \delta$ is attained. Then we should have,

$$
\rho(T(x_{0}),T^{2}(x_{0})) < \rho(x_{0},T(x_{0})) = \delta
$$

But this is a contradiction since we assumed that $\inf_{x \in X} \rho (x,T(x)) = \delta$. So we get that $\inf_{x \in X} \rho(x,T(x)) = 0$. Hence there exists $x_{1} \in X$ such that $T(x_{1}) = x_{1}$.

Now to show the uniqueness of the fixed point we see that if $T(x)=x \neq y =T(y)$ for $x,y \in X$. Then $\rho(T(x),T(y)) = \rho(x,y) <\rho(x,y)$ which is again a contradiction. So the fixed point is unique. $\quad \blacksquare$

$8.$ Consider $X = (0,1)$, Now we take the functions,

$$
f_{n}(x) =
\begin{cases}
n  & \text{if } x < \frac{1}{n} \\
\frac{1}{x} & \text{otherwise}
\end{cases}
$$

For any subset $A$ of $X$, we have that since $X$ is bounded $A$ is also bounded and hence has a infimum $a = \inf A$, but $A$ is also closed in $\mathbb{R}$ hence it will contain its infimum, which implies $a \in X=(0,1)$. So we now prove that $\{ f_{n} \}$ is uniform convergent in $[a,1)$ and hence uniform convergent in $A \subseteq []a,1)$. Now there exists $N \in \mathbb{N}$, such that $\frac{1}{N} < a$, hence by the definition of $f_{n}$ we have,

$$
\left\lvert  f_{n}(x) - \frac{1}{x}  \right\rvert = 0  \quad \forall x \in [a,1), \text{for }n>N
$$

Hence $f_{n}$ uniformly converges to $\frac{1}{x}$ in any closed set in $X$. So the statement is not true.

$9.$
$(i)$ Consider $f_{n}(x) = x+ \frac{1}{n}$ and $g(x) = x^{2}$, Now we have $g\circ f_{n} = x^{2} + \frac{2x}{n}+\frac{1}{n^{2}}$ and $g \circ f = x^{2}$ Hence for any $\varepsilon>0$ and any $n$ we can choose $x$ such that,

$$
\begin{gather*}
x > \frac{\varepsilon n}{2} \\
\implies \left\lvert \left( x^{2} + \frac{2x}{n} + \frac{1}{n^{2}} \right) - x^{2} \right\rvert = \left\lvert  \frac{2x}{n} + \frac{1}{n^{2}}  \right\rvert > \varepsilon
\end{gather*}
$$

So we can see that $g \circ f_{n}$ is not uniformly convergent. Hence the statement is false.

$(ii)$ Since we have the uniform convergence of $\{ f_{n} \}$, $\forall \varepsilon>0,\exists N \in \mathbb{N}$ such that

$$
\lvert f_{n}(x) - f(x) \rvert < \varepsilon \quad \forall n\geq N,\forall x \in \mathbb{R}
$$

Since this is true for all $x \in \mathbb{R}$, It is also true for all $g(x),x \in \mathbb{R}$. We have,

$$
\lvert f_{n}(g(x)) - f(g(x)) \rvert < \varepsilon \quad \forall n\geq N,\forall x \in \mathbb{R}
$$

So $f_{n} \circ g$ uniformly converges to $f \circ g$. Hence the statement is true.$\quad \blacksquare$
