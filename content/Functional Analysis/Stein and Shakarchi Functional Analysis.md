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

> [!IMPORTANT]
> **Theorem 1.2 (Minkowski's Inequality)**
> If $1 \le p < \infty$ and $f,g \in L^p$, then $f+g \in L^p$ and
> $$ \|f+g\|_p \le \|f\|_p + \|g\|_p $$

### Proof

Case $p=1$: Follows quickly from $|f+g| \le |f| + |g|$.

Case $p>1$:
First show $f+g \in L^p$.
$$ |f(x) + g(x)|^p \le 2^p (|f(x)|^p + |g(x)|^p) $$
Since $|f+g| \le |f| + |g| \le 2 \max(|f|, |g|)$, we have $|f+g|^p \le 2^p \max(|f|^p, |g|^p) \le 2^p(|f|^p + |g|^p)$.

Now use the inequality:
$$ |f+g|^p \le |f| |f+g|^{p-1} + |g| |f+g|^{p-1} $$
Since $(p-1)q = p$ and $f+g \in L^p$, we have $(f+g)^{p-1} \in L^q$. Apply Hölder ($p, q$):
$$ \|f+g\|_p^p \le (\|f\|_p + \|g\|_p) \|(f+g)^{p-1}\|_q $$
Note that $\|(f+g)^{p-1}\|_q = \|f+g\|_p^{p/q}$. Since $p - p/q = 1$:
$$ \|f+g\|_p^p \le (\|f\|_p + \|g\|_p) \|f+g\|_p^{p-1} $$
Divide by $\|f+g\|_p^{p-1}$ (if $>0$) to conclude.

## Completeness

> [!IMPORTANT]
> **Theorem 1.3**
> The space $L^p(X, \mathcal{F}, \mu)$ is complete in the norm $\|\cdot\|_p$.

### Proof

Let $\{f_n\}$ be a Cauchy sequence in $L^p$.
Choose a subsequence $\{f_{n_k}\}$ such that $\|f_{n_{k+1}} - f_{n_k}\|_p \le 2^{-k}$.
Define
$$ g(x) = |f_{n_1}(x)| + \sum_{k=1}^\infty |f_{n_{k+1}}(x) - f_{n_k}(x)| $$
By Minkowski's inequality, partial sums satisfy $\|S_K(g)\|_p \le \|f_{n_1}\|_p + \sum 2^{-k} \le C$.
Monotone Convergence Theorem implies $\int g^p < \infty$, so $g \in L^p$ and the series converges a.e.
Thus, $f_{n_k}(x) \to f(x)$ a.e. for some $f$. Since $|f| \le g \in L^p$, $f \in L^p$.

To show convergence in norm ($f_{n_k} \to f$ in $L^p$):
$$ |f(x) - S_K(f)(x)|^p \le (2 \max(|f|, |S_K(f)|))^p \le 2^p |g(x)|^p $$
By Dominated Convergence Theorem, $\|f - f_{n_k}\|_p \to 0$.

Since $\{f_n\}$ is Cauchy and a subsequence converges to $f$, the full sequence converges to $f$.
