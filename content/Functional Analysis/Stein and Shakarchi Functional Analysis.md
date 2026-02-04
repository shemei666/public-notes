# Stein and Shakarchi Functional Analysis

## $L^p$ Spaces

**Notation**:
*   $L^p(X, \mu)$, $L^p(X)$, or $L^p$.
*   For $f \in L^p(X, \mathcal{F}, \mu)$, the $L^p$ norm is
$$ 
\|f\|_p = \|f\|_{L^p} = \left( \int_X |f(x)|^p \, d\mu(x) \right)^{1/p} 
$$

## Hölder and Minkowski Inequalities

**Conjugate Exponents**: $p, q \in [1, \infty]$ satisfying $\frac{1}{p} + \frac{1}{q} = 1$.
*   $1/\infty = 0$.
*   $p=2$ is self-dual.

> [!IMPORTANT]
> **Theorem 1.1 (Hölder's Inequality)**
> Let $1 < p, q < \infty$ be conjugate exponents. If $f \in L^p$ and $g \in L^q$, then $fg \in L^1$ and
> $$ \|fg\|_1 \le \|f\|_p \|g\|_q $$

### Proof

**Lemma (Arithmetic-Geometric Mean)**: For $A, B \ge 0, \theta \in [0, 1]$:
$$ A^\theta B^{1-\theta} \le \theta A + (1-\theta) B $$

*Proof of Lemma*:
Assume $B \neq 0$, set $x = A/B$. Equivalent to proving $x^\theta \le \theta x + (1-\theta)$.
Let $f(x) = x^\theta - \theta x - (1-\theta)$. Since $f'(x) = \theta(x^{\theta-1}-1)$, $f$ is maximized at $x=1$ with $f(1)=0$, so $f(x) \le 0$.

*Proof of Theorem*:
If $\|f\|_p = 0$ or $\|g\|_q = 0$, then $fg=0$ a.e.
Assume $\|f\|_p = \|g\|_q = 1$ by replacing $f$ with $f/\|f\|_p$.
Set $A = |f(x)|^p$, $B = |g(x)|^q$, $\theta = 1/p$. Then $1-\theta = 1/q$.
By the lemma:
$$ |f(x)g(x)| \le \frac{1}{p}|f(x)|^p + \frac{1}{q}|g(x)|^q $$
Integrate both sides:
$$ \|fg\|_1 \le \frac{1}{p}\|f\|_p^p + \frac{1}{q}\|g\|_q^q = \frac{1}{p} + \frac{1}{q} = 1 $$
Thus $\|fg\|_1 \le 1 = \|f\|_p \|g\|_q$.
