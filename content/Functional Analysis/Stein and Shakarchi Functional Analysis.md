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

> [!NOTE]
> **Theorem (Dominated Convergence)**
> Let $\{g_n\}$ be a sequence of measurable functions such that $g_n \to g$ a.e. If there exists $G \in L^1$ such that $|g_n| \le G$ a.e. for all $n$, then $g_n \to g$ in $L^1$, i.e., $\int |g_n - g| \to 0$ (and consequently $\int g_n \to \int g$).

$$ |f(x) - S_K(f)(x)|^p \le (2 \max(|f|, |S_K(f)|))^p \le 2^{p+1} |g(x)|^p $$
By Dominated Convergence Theorem, $\|f - f_{n_k}\|_p \to 0$.

Since $\{f_n\}$ is Cauchy and a subsequence converges to $f$, the full sequence converges to $f$.

> [!IMPORTANT]
> **Proposition 1.4**
> If $\mu(X) < \infty$ and $1 \le p_0 \le p_1 \le \infty$, then $L^{p_1}(X) \subset L^{p_0}(X)$ and
> $$ \frac{1}{\mu(X)^{1/p_0}} \|f\|_{p_0} \le \frac{1}{\mu(X)^{1/p_1}} \|f\|_{p_1} $$

### Proof

Without loss of generality, assume $p_1 > p_0$ (if equal, statement is trivial).
Let $f \in L^{p_1}$. Apply Hölder's inequality (Theorem 1.1) to $|f|^{p_0}$ and $1$ with
exponents: $p = p_1/p_0 > 1$ and its conjugate $q$ (where $1/p + 1/q = 1$, so $1/q = 1 - p_0/p_1$).
$$ \int |f|^{p_0} \cdot 1 \le \left( \int (|f|^{p_0})^p \right)^{1/p} \left( \int 1^q \right)^{1/q} $$
Substitute $p = p_1/p_0$:
$$ \|f\|_{p_0}^{p_0} \le \left( \int |f|^{p_1} \right)^{p_0/p_1} (\mu(X))^{1 - p_0/p_1} $$
$$ \|f\|_{p_0}^{p_0} \le \|f\|_{p_1}^{p_0} \mu(X)^{1 - p_0/p_1} $$
Take the $p_0$-th root:
$$ \|f\|_{p_0} \le \|f\|_{p_1} \mu(X)^{1/p_0 - 1/p_1} $$
Rearranging gives the desired inequality. Thus $f \in L^{p_0}$ and the inclusion holds.

> [!IMPORTANT]
> **Proposition 1.5**
> If $X = \mathbb{Z}$ (counting measure), then the reverse inclusion holds: $L^{p_0}(\mathbb{Z}) \subset L^{p_1}(\mathbb{Z})$ if $p_0 \le p_1$. Also,
> $$ \|f\|_{p_1} \le \|f\|_{p_0} $$

### Proof

Let $f = \{f(n)\}_{n \in \mathbb{Z}}$. $\sum |f(n)|^{p_0} = \|f\|_{p_0}^{p_0}$.
Note that $\sup_n |f(n)| \le \|f\|_{p_0}$ (since sum includes each term).
If $p_1 \ge p_0$:
$$ \sum |f(n)|^{p_1} = \sum |f(n)|^{p_0} |f(n)|^{p_1-p_0} $$
$$ \le (\sup_n |f(n)|)^{p_1-p_0} \sum |f(n)|^{p_0} $$
$$ \le \|f\|_{p_0}^{p_1-p_0} \|f\|_{p_0}^{p_0} = \|f\|_{p_0}^{p_1} $$
Taking $p_1$-th root: $\|f\|_{p_1} \le \|f\|_{p_0}$.

## The Case $p = \infty$

$L^\infty(X, \mathcal{F}, \mu)$ consists of essentially bounded measurable functions.

**Essential Supremum**:
There exists $0 < M < \infty$ with $|f(x)| \le M$ a.e.
$$ \|f\|_\infty = \inf \{M : |f(x)| \le M \text{ a.e.} \} $$

**Note**: $|f(x)| \le \|f\|_\infty$ a.e.
*Proof*: Let $E = \{x : |f(x)| > \|f\|_\infty\}$.
$E = \bigcup E_n$ where $E_n = \{x : |f(x)| > \|f\|_\infty + 1/n\}$.
By definition of infimum, $\mu(E_n) = 0$, so $\mu(E) = 0$.

> [!IMPORTANT]
> **Theorem 2.1**
> The vector space $L^\infty$ equipped with $\|\cdot\|_{L^\infty}$ is a complete vector space.

> [!IMPORTANT]
> **Proposition 2.2**
> Suppose $f \in L^\infty$ is supported on a set of finite measure $E$ ($\mu(E) < \infty$). Then $f \in L^p$ for all $p < \infty$, and
> $$ \|f\|_p \to \|f\|_\infty \quad \text{as } p \to \infty $$

### Proof

If $\mu(E) = 0$, trivial. Otherwise:
$$ \|f\|_p = \left( \int_E |f|^p \right)^{1/p} \le \left( \int_E \|f\|_\infty^p \right)^{1/p} = \|f\|_\infty \mu(E)^{1/p} $$
As $p \to \infty$, $\mu(E)^{1/p} \to 1$, so $\limsup_{p \to \infty} \|f\|_p \le \|f\|_\infty$.

Given $\epsilon > 0$, let $S = \{x : |f(x)| \ge \|f\|_\infty - \epsilon\}$. By definition of essential supremum, $\mu(S) = \delta > 0$.
$$ \int_X |f|^p \ge \int_S |f|^p \ge \delta (\|f\|_\infty - \epsilon)^p $$
$$ \|f\|_p \ge \delta^{1/p} (\|f\|_\infty - \epsilon) $$
Taking $\liminf_{p \to \infty}$ gives $\liminf \|f\|_p \ge \|f\|_\infty - \epsilon$.
Since $\epsilon$ is arbitrary, result follows.

## Banach Spaces

**Normed Vector Space**: A vector space $V$ over scalars ($\mathbb{R}$ or $\mathbb{C}$) with a **norm** $\|\cdot\|: V \to \mathbb{R}^+$ satisfying:
*   $\|v\| = 0 \iff v = 0$.
*   $\|\alpha v\| = |\alpha| \|v\|$ for scalar $\alpha, v \in V$.
*   $\|v+w\| \le \|v\| + \|w\|$ (Triangle inequality) for $v, w \in V$.

**Definition**: A complete normed vector space is called a **Banach space**.

### Examples

**Example 3: Hölder (Lipschitz) Space $\Lambda^\alpha(\mathbb{R})$**
For $0 < \alpha \le 1$, the space of bounded functions on $\mathbb{R}$ satisfying:
$$ \sup_{t_1 \neq t_2} \frac{|f(t_1) - f(t_2)|}{|t_1 - t_2|^\alpha} < \infty $$
For $\alpha > 1$, functions are constant.
On $\mathbb{R}^d$, the norm is
$$ \|f\|_{\Lambda^\alpha(\mathbb{R}^d)} = \sup_{x} |f(x)| + \sup_{x \neq y} \frac{|f(x) - f(y)|}{|x - y|^\alpha} $$
$\Lambda^\alpha(\mathbb{R}^d)$ is a Banach space.

**Example 4: Sobolev Space $L^p_k(\mathbb{R}^d)$**
$f \in L^p(\mathbb{R}^d)$ has **weak derivatives** up to order $k$ if for every multi-index $\alpha$ with $|\alpha| \le k$, there exists $g_\alpha \in L^p$ such that:
$$ \int_{\mathbb{R}^d} g_\alpha(x) \phi(x) \, dx = (-1)^{|\alpha|} \int_{\mathbb{R}^d} f(x) \partial_x^\alpha \phi(x) \, dx $$
for all smooth $\phi$ with compact support.
Here $\partial_x^\alpha = (\partial/\partial x_1)^{\alpha_1} \dots (\partial/\partial x_d)^{\alpha_d}$.
We write $\partial_x^\alpha f = g_\alpha$.

The space $L^p_k(\mathbb{R}^d)$ (Sobolev Space) of all such functions is a Banach space with norm:
$$ \|f\|_{L^p_k} = \sum_{|\alpha| \le k} \|\partial_x^\alpha f\|_{L^p} $$

## Linear Functionals

Let $\mathcal{B}$ be a Banach space over $\mathbb{R}$.
A **linear functional** is a linear mapping $\ell: \mathcal{B} \to \mathbb{R}$, satisfying:
$$ \ell(\alpha f + \beta g) = \alpha \ell(f) + \beta \ell(g) $$

**Definitions**:
*   **Continuous**: Given $\epsilon > 0$, there exists $\delta > 0$ such that $|\ell(f) - \ell(g)| \le \epsilon$ whenever $\|f - g\| \le \delta$.
*   **Bounded**: There exists $M > 0$ such that $|\ell(f)| \le M \|f\|$ for all $f \in \mathcal{B}$.

> [!IMPORTANT]
> **Proposition 3.1**
> A linear functional on a Banach space is continuous if and only if it is bounded.

### Proof

Note that $\ell$ is continuous iff $\ell$ is continuous at the origin.

($\Rightarrow$) If $\ell$ is continuous, choose $\epsilon=1, g=0$. Then $|\ell(f)| \le 1$ whenever $\|f\| \le \delta$ for some $\delta > 0$.
For any non-zero $h \in \mathcal{B}$, the vector $\delta h / \|h\|$ has norm $\delta$, so $|\ell(\delta h / \|h\|)| \le 1$.
Thus $|\ell(h)| \le (1/\delta) \|h\|$, so $\ell$ is bounded with $M = 1/\delta$.

($\Leftarrow$) If $\ell$ is bounded, it is clearly continuous at the origin ($f \to 0 \implies \ell(f) \to 0$), hence continuous everywhere by linearity.

### Dual Space

The set of all continuous linear functionals on $\mathcal{B}$ forms a vector space.

**Norm**: The norm $\|\ell\|$ of a continuous linear functional is the infimum of all $M$ such that $|\ell(f)| \le M \|f\|$.
$$ \|\ell\| = \sup_{\|f\| \le 1} |\ell(f)| = \sup_{\|f\|=1} |\ell(f)| = \sup_{f \neq 0} \frac{|\ell(f)|}{\|f\|} $$

**Definition**: The vector space of all continuous linear functionals on $\mathcal{B}$ equipped with $\|\cdot\|$ is called the **dual space** of $\mathcal{B}$, denoted by $\mathcal{B}^*$.

> [!IMPORTANT]
> **Theorem 3.2**
> The vector space $\mathcal{B}^*$ is a Banach space.

### Proof

We verify that $\mathcal{B}^*$ is complete with respect to $\|\cdot\|$.
Let $\{\ell_n\}$ be a Cauchy sequence in $\mathcal{B}^*$.
For each $f \in \mathcal{B}$, $|\ell_n(f) - \ell_m(f)| \le \|\ell_n - \ell_m\| \|f\|$.
Thus $\{\ell_n(f)\}$ is a Cauchy sequence in $\mathbb{R}$ (which is complete), so it converges to a limit $\ell(f)$.
The mapping $f \mapsto \ell(f)$ is linear.
Since Cauchy sequences are bounded, there exists $M$ such that $\|\ell_n\| \le M$ for all $n$.
$$ |\ell(f)| \le |(\ell - \ell_n)(f)| + |\ell_n(f)| \le |(\ell - \ell_n)(f)| + M\|f\| $$
In the limit $n \to \infty$, $|\ell(f)| \le M\|f\|$, so $\ell$ is bounded.

To show $\ell_n \to \ell$ in $\mathcal{B}^*$:
Given $\epsilon > 0$, choose $N$ such that $\|\ell_n - \ell_m\| < \epsilon/2$ for $n, m > N$.
For $n > N$ and any $f$:
$$ |(\ell - \ell_n)(f)| \le |(\ell - \ell_m)(f)| + |(\ell_m - \ell_n)(f)| \le |(\ell - \ell_m)(f)| + \frac{\epsilon}{2} \|f\| $$
For fixed $f$, choose $m$ large enough so $|(\ell - \ell_m)(f)| \le (\epsilon/2) \|f\|$.
Then $|(\ell - \ell_n)(f)| \le \epsilon \|f\|$ for all $f$.
Thus $\|\ell - \ell_n\| \le \epsilon$ for $n > N$, so $\ell_n \to \ell$ in norm.

## The Dual Space of $L^p$ ($1 \le p < \infty$)

Let $1 \le p \le \infty$ and $q$ be the conjugate exponent ($1/p + 1/q = 1$).

Every function $g \in L^q$ defines a bounded linear functional $\ell$ on $L^p$ by:
$$ \ell(f) = \int_X f(x)g(x) \, d\mu(x) $$
By Hölder's inequality, $|\ell(f)| \le \|f\|_p \|g\|_q$. Thus $\|\ell\| \le \|g\|_q$.
Associating $g$ to $\ell$ gives the inclusion $L^q \subset (L^p)^*$ for $1 \le p \le \infty$.

**Main Result**:
For $1 \le p < \infty$, every linear functional on $L^p$ is of this form for some $g \in L^q$.
Thus, $(L^p)^* = L^q$ when $1 \le p < \infty$.

**Note**:
This result does **not** hold for $p = \infty$. The dual of $L^\infty$ contains $L^1$ but is strictly larger.
