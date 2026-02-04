# Stein and Shakarchi Functional Analysis

To simplify the notation, we write $L^p(X, \mu)$, or $L^p(X)$, or simply $L^p$ when the underlying measure space has been specified. Then, if $f \in L^p(X, \mathcal{F}, \mu)$ we define the $L^p$ **norm** of $f$ by
$$
\|f\|_{L^p(X, \mathcal{F}, \mu)} = \left( \int_X |f(x)|^p \, d\mu(x) \right)^{1/p} .
$$
We also abbreviate this to $\|f\|_{L^p(X)}$, $\|f\|_{L^p}$, or $\|f\|_p$.

## 1.1 The Hölder and Minkowski inequalities

If the two exponents $p$ and $q$ satisfy $1 \le p, q \le \infty$, and the relation
$$ \frac{1}{p} + \frac{1}{q} = 1 $$
holds, we say that $p$ and $q$ are **conjugate** or **dual** exponents. Here, we use the convention $1/\infty = 0$. Later, we shall sometimes use $p'$ to denote the conjugate exponent of $p$. Note that $p=2$ is self-dual, that is, $p=q=2$; also $p=1, \infty$ corresponds to $q=\infty, 1$ respectively.

**Theorem 1.1 (Hölder)**. *Suppose $1 < p < \infty$ and $1 < q < \infty$ are conjugate exponents. If $f \in L^p$ and $g \in L^q$, then $fg \in L^1$ and*
$$ \|fg\|_{L^1} \le \|f\|_{L^p} \|g\|_{L^q}. $$

*Proof.* The proof of the theorem relies on a simple generalized form of the arithmetic-geometric mean inequality: if $A, B \ge 0$, and $0 \le \theta \le 1$, then
$$ A^\theta B^{1-\theta} \le \theta A + (1-\theta) B \tag{2} $$
Note that when $\theta = 1/2$, the inequality (2) states the familiar fact that the geometric mean of two numbers is majorized by their arithmetic mean.

To establish (2), we observe first that we may assume $B \neq 0$, and replacing $A$ by $AB$, we see that it suffices to prove that $A^\theta \le \theta A + (1-\theta)$. If we let $f(x) = x^\theta - \theta x - (1-\theta)$, then $f'(x) = \theta(x^{\theta-1} - 1)$. Thus $f(x)$ increases when $0 \le x \le 1$ and decreases when $1 \le x$, and we see that the continuous function $f$ attains a maximum at $x=1$, where $f(1)=0$. Therefore $f(A) \le 0$, as desired.

To prove Hölder's inequality we argue as follows. If either $\|f\|_{L^p} = 0$ or $\|g\|_{L^q} = 0$, then $fg = 0$ a.e. and the inequality is obviously verified. Therefore, we may assume that neither of these norms vanish, and after replacing $f$ by $f/\|f\|_{L^p}$ and $g$ by $g/\|g\|_{L^q}$, we may further assume that $\|f\|_{L^p} = \|g\|_{L^q} = 1$. We now need to prove that $\|fg\|_{L^1} \le 1$.

If we set $A = |f(x)|^p$, $B = |g(x)|^q$, and $\theta = 1/p$ so that $1-\theta = 1/q$, then (2) gives
$$ |f(x)g(x)| \le \frac{1}{p}|f(x)|^p + \frac{1}{q}|g(x)|^q. $$
Integrating this inequality yields $\|fg\|_{L^1} \le 1$, and the proof of the Hölder inequality is complete.
