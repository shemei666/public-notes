---
publish: true
---

# Analysis of Several Variables

## Euclidean Inner Product and Norm

**Def (Euclidean Inner Product):** 
The Euclidean inner product on $\mathbb{R}^n$ is a map
$$ \langle \cdot, \cdot \rangle : \mathbb{R}^n \times \mathbb{R}^n \longrightarrow \mathbb{R} $$
defined for $x = (x_1, \dots, x_n)$ and $y = (y_1, \dots, y_n)$ by
$$ (x, y) \mapsto \langle x, y \rangle = \sum_{i=1}^n x_i y_i $$

### Properties

- **Bilinearity & Positive Definiteness**:
  - $\langle x + u, y \rangle = \langle x, y \rangle + \langle u, y \rangle \quad \forall x, y, u \in \mathbb{R}^n$
  - $\langle x, \lambda y \rangle = \lambda \langle x, y \rangle \quad \forall \lambda \in \mathbb{R}$
  - $\langle x, x \rangle \geq 0 \quad \forall x \in \mathbb{R}^n \quad \text{and} \quad \langle x, x \rangle = 0 \iff x = 0$

- **Induced Norm Structure**:
  When given an inner product on $\mathbb{R}^n$, we can define a norm structure on $\mathbb{R}^n$:
  $$ \|\cdot\| : \mathbb{R}^n \longrightarrow \mathbb{R}_{\geq 0}, \quad \|x\| = \sqrt{\langle x, x \rangle} $$
  *(The norm obtained from the Euclidean inner product is called the **Euclidean norm**).*

  **Properties of the norm:**
  1. $\|x\| \geq 0$, and $\|x\| = 0 \iff x = 0$
  2. $\|\lambda x\| = |\lambda| \|x\| \quad \forall \lambda \in \mathbb{R}$ *(Homogeneity)*
  3. $\|x + y\| \leq \|x\| + \|y\|$ *(Triangle Inequality)*

- **Euclidean Metric**:
  The metric induced by the Euclidean norm is a map $d : \mathbb{R}^n \times \mathbb{R}^n \longrightarrow \mathbb{R}_{\geq 0}$ defined by
  $$ d(x, y) = \|x - y\| $$
  This metric is often denoted as $d_2$.

---

**Theorem (Cauchy-Schwarz Inequality).**
For all $x, y \in \mathbb{R}^n$,
$$ |\langle x, y \rangle| \leq \|x\| \|y\| $$

**Proof:**
For any $\lambda \in \mathbb{R}$:
$$ \langle x - \lambda y, x - \lambda y \rangle \geq 0 $$

Expanding by bilinearity and symmetry:
$$ \langle x, x \rangle + \langle x, -\lambda y \rangle + \langle -\lambda y, x \rangle + \langle -\lambda y, -\lambda y \rangle \geq 0 $$
$$ \|x\|^2 - 2\lambda \langle x, y \rangle + \lambda^2 \|y\|^2 \geq 0 $$

Rearranging as a quadratic expression in $\lambda$:
$$ \lambda^2 \|y\|^2 - 2\lambda \langle x, y \rangle + \|x\|^2 \geq 0 $$

Since this quadratic in $\lambda$ is non-negative for all $\lambda \in \mathbb{R}$, its discriminant must be less than or equal to $0$:
$$ 4 \langle x, y \rangle^2 - 4 \|x\|^2 \|y\|^2 \leq 0 $$
$$ \implies \langle x, y \rangle^2 \leq (\|x\| \|y\|)^2 $$

Taking the square root on both sides yields:
$$ |\langle x, y \rangle| \leq \|x\| \|y\| \quad \blacksquare $$

---

## Topology on $(\mathbb{R}^n, d_2)$

**Def (Balls and Spheres):**
In the metric space $(\mathbb{R}^n, d_2)$ for $r > 0$ and $x \in \mathbb{R}^n$:
- **Open Ball**:
  $$ B(x; r) := \{ y \in \mathbb{R}^n \mid \|x - y\| < r \} $$
- **Sphere of radius $r$ centered at $x$**:
  $$ S(x; r) := \{ y \in \mathbb{R}^n \mid \|x - y\| = r \} $$
- **Closed Ball**:
  $$ \bar{B}(x; r) := \{ y \in \mathbb{R}^n \mid \|x - y\| \leq r \} = B(x; r) \cup S(x; r) $$

**Def (Open Sets and Metric Topology):**
- **Open Sets**: A subset $S \subseteq \mathbb{R}^n$ is open in $(\mathbb{R}^n, d_2)$ if $S$ is a union of open balls in $(\mathbb{R}^n, d_2)$.
- **Metric Topology $\tau(d_2)$**: The set of all open sets in $(\mathbb{R}^n, d_2)$ forms the topology induced by the metric $d_2$, denoted as $\tau(d_2)$.

---

**Lemma (Countable Basis for $\tau(d_2)$).**
The collection of open balls
$$ \mathcal{B} := \{ B(x; r) \mid x \in \mathbb{Q}^n, r \in \mathbb{Q}^+ \} $$
is a countable collection of open balls. They form a basis of $\tau(d_2)$, i.e., every open set in $\tau(d_2)$ can be represented as a union of sets in $\mathcal{B}$.

---

## Limit Points, Continuity, and Sequences

**Def (Limit Point and Closure):**
Let $S \subseteq \mathbb{R}^n$.
- A point $x \in \mathbb{R}^n$ is called a **limit point** of $S$ if every open ball around $x$ intersects $S$ in a point other than $x$.
- The **closure** of $S$, denoted $\bar{S}$, is defined as:
  $$ \bar{S} := S \cup \{ \text{limit points of } S \} $$

**Def (Continuous Functions):**
- **Global Continuity**: A function $f : \mathbb{R}^m \longrightarrow \mathbb{R}^n$ is **continuous** if for every open subset $V \subseteq \mathbb{R}^n$, the preimage $f^{-1}(V)$ is open in $\mathbb{R}^m$.
- **Continuity at a Point**: $f$ is continuous at $x \in \mathbb{R}^m$ if for every open set $V \subseteq \mathbb{R}^n$ containing $f(x)$, $f^{-1}(V)$ is open in $\mathbb{R}^m$.
- **$\varepsilon$-$\delta$ Characterization (Equivalent)**: $f$ is continuous at $x \in \mathbb{R}^m$ if and only if for any $\varepsilon > 0$, there exists $\delta > 0$ such that for all $y \in \mathbb{R}^m$:
  $$ d(x, y) < \delta \implies d(f(x), f(y)) < \varepsilon $$

**Def (Sequence Convergence in $\mathbb{R}^n$):**
Let $\{\alpha^k\}_{k \in \mathbb{N}}$ be a sequence in $\mathbb{R}^n$ with $\alpha^k = (x_{k_1}, \dots, x_{k_n}) \in \mathbb{R}^n$.
We say $\{\alpha^k\}$ **converges to** $\alpha \in \mathbb{R}^n$ (denoted $\{\alpha^k\} \to \alpha$) if for any $\varepsilon > 0$, there exists $N \in \mathbb{N}$ such that for all $k \geq N$:
$$ d_2(\alpha^k, \alpha) < \varepsilon $$

---

**Lemma (Sequential Continuity).**
A function $f : \mathbb{R}^m \longrightarrow \mathbb{R}^n$ is continuous at $\alpha \in \mathbb{R}^m$ if and only if for every sequence $\{\alpha^k\} \to \alpha$ in $\mathbb{R}^m$, we have:
$$ \{f(\alpha^k)\} \longrightarrow f(\alpha) \quad \text{in } \mathbb{R}^n $$



