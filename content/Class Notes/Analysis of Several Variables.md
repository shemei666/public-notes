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

---

## Exercises and Solutions

**Exercise 1.** In $(\mathbb{R}^n, d_2)$:
1. Show that an arbitrary union of open sets is open.
2. Show that if $V_1, \dots, V_k$ are open in $\mathbb{R}^n$, then $\bigcap_{i=1}^k V_i$ is open in $\mathbb{R}^n$.
3. Find an example to show that a countable intersection of open sets need not be open.

**Solution:**
1. If $B(x, \varepsilon) \subseteq U_i$ for some $i \in I$, then $B(x, \varepsilon) \subseteq \bigcup_{i \in I} U_i$. Thus, the arbitrary union of open sets is open.
2. If $x \in \bigcap_{i=1}^k V_i$, then for each $i = 1, \dots, k$, there exists $d_i > 0$ such that $B(x, d_i) \subseteq V_i$. Taking $d = \min \{d_1, \dots, d_k\} > 0$, we have $B(x, d) \subseteq \bigcap_{i=1}^k V_i$, showing the finite intersection is open.
3. Consider the open intervals $U_n = (-1/n, 1/n)$ in $\mathbb{R}$ for $n = 1, 2, \dots$. The countable intersection is:
   $$ \bigcap_{n=1}^\infty \left(-\frac{1}{n}, \frac{1}{n}\right) = \{0\} $$
   which is a closed set (not open). $\quad \blacksquare$

---

**Exercise 2 (Continuity of Coordinate Functions).**
Let $f : \mathbb{R}^m \longrightarrow \mathbb{R}^n$ with $f = (f_1, \dots, f_n)$. Show that $f$ is continuous if and only if each coordinate function $f_i : \mathbb{R}^m \longrightarrow \mathbb{R}$ is continuous.
*(Note: $f_i = \pi_i \circ f$, where $\pi_i : \mathbb{R}^n \to \mathbb{R}$ is the $i$-th projection map).*

**Solution:**
- $(\implies)$ Assume $f$ is continuous at $x \in \mathbb{R}^m$. For any $\varepsilon > 0$, there exists $\delta > 0$ such that for all $y \in \mathbb{R}^m$ with $\|x - y\|_2 < \delta$, we have $\|f(x) - f(y)\|_2 < \varepsilon$.
  Observe that:
  $$ \|f(x) - f(y)\|_2^2 = \sum_{k=1}^n |f_k(x) - f_k(y)|^2 < \varepsilon^2 $$
  Thus, for each $k = 1, \dots, n$:
  $$ |f_k(x) - f_k(y)|^2 \leq \|f(x) - f(y)\|_2^2 < \varepsilon^2 \implies |f_k(x) - f_k(y)| < \varepsilon $$
  Hence, each coordinate function $f_k$ is continuous.

- $(\impliedby)$ Assume each coordinate function $f_k : \mathbb{R}^m \to \mathbb{R}$ is continuous at $x \in \mathbb{R}^m$. Given $\varepsilon > 0$, for each $k = 1, \dots, n$ there exists $\delta_k > 0$ such that whenever $\|x - y\|_2 < \delta_k$:
  $$ |f_k(x) - f_k(y)| < \frac{\sqrt{\varepsilon}}{\sqrt{n}} $$
  Set $\delta = \min\{\delta_1, \dots, \delta_n\} > 0$. Then for all $y \in \mathbb{R}^m$ with $\|x - y\|_2 < \delta$:
  $$ \|f(x) - f(y)\|_2^2 = \sum_{k=1}^n |f_k(x) - f_k(y)|^2 \leq n \times \left(\frac{\sqrt{\varepsilon}}{\sqrt{n}}\right)^2 = \varepsilon $$
  Thus $\|f(x) - f(y)\|_2 \leq \sqrt{\varepsilon}$, which proves that $f$ is continuous. $\quad \blacksquare$

---

**Exercise 3.**
Consider the function $f : \mathbb{R}^2 \longrightarrow \mathbb{R}$ defined by:
$$ f(x, y) = \begin{cases} \frac{xy}{x^2 + y^2} & \text{if } (x, y) \neq (0, 0) \\ 0 & \text{if } (x, y) = (0, 0) \end{cases} $$
Show that $f$ is not continuous at $(0, 0)$.

**Solution:**
Consider a sequence of points $(x_n, m x_n)$ along the line $y = mx$, where $x_n \to 0$ and $m \in \mathbb{R}$. Evaluating $f$ along this sequence:
$$ f(x_n, m x_n) = \frac{x_n(m x_n)}{x_n^2 + (m x_n)^2} = \frac{m}{1 + m^2} $$
Notice that $f(x_n, m x_n)$ is constant along the direction $y = mx$ and non-zero for any $m \neq 0$.
Since the limit depends on the path / slope $m$ (for instance, $f(x_n, x_n) = \frac{1}{2} \neq f(0,0)$), the limit as $(x,y) \to (0,0)$ does not exist.
$\therefore f$ is not continuous at $(0, 0)$. $\quad \blacksquare$

---

## Completeness, Cantor Intersection, and Bolzano-Weierstrass

**Proposition (Completeness of $(\mathbb{R}^n, d_2)$).**
The metric space $(\mathbb{R}^n, d_2)$ is complete, i.e., every Cauchy sequence in $\mathbb{R}^n$ is convergent.

**Def (Cauchy Sequence in $\mathbb{R}^n$):**
A sequence $\{\alpha^k\}$ is **Cauchy** in $(\mathbb{R}^n, d_2)$ if for any $\varepsilon > 0$, there exists $N \in \mathbb{N}$ such that:
$$ \|\alpha^n - \alpha^m\| < \varepsilon \quad \forall n, m \geq N $$

**Proof Sketch:**
Follows from component-wise convergence and the completeness of $\mathbb{R}$. $\quad \blacksquare$

---

**Theorem (Cantor's Intersection Theorem).**
Let $C_1 \supseteq C_2 \supseteq C_3 \supseteq \dots$ be a nested sequence of non-empty closed subsets of $\mathbb{R}^n$ such that $\text{diam}(C_n) \longrightarrow 0$ as $n \to \infty$. Then the intersection contains exactly one point:
$$ \bigcap_{n=1}^\infty C_n = \{p\} \quad \text{for some } p \in \mathbb{R}^n $$

**Def (Diameter of a Set):**
The diameter of a subset $S \subseteq \mathbb{R}^n$ is defined as:
$$ \text{diam}(S) := \sup \{ \|x - y\| \mid x, y \in S \} $$

**Proof Sketch:**
Choose $x_n \in C_n$. Since $C_n$ are nested and $\text{diam}(C_n) \to 0$, $\{x_n\}$ forms a Cauchy sequence in $\mathbb{R}^n$. By completeness of $\mathbb{R}^n$, $x_n \to p$. Since each $C_n$ is closed, $p \in \bigcap_{n=1}^\infty C_n$. Uniqueness follows from $\text{diam}(C_n) \to 0$. $\quad \blacksquare$

---

**Theorem (Bolzano-Weierstrass Theorem).**
Any bounded infinite subset $S \subseteq \mathbb{R}^n$ contains a convergent sequence.

**Proof Sketch:**
Consider a sequence of distinct points $\{x_k\} \subseteq S$. Define $F_n = \overline{\{x_k \mid k \geq n\}}$. Apply Cantor's Intersection Theorem on the nested closed sets $F_n$ to construct a convergent subsequence. $\quad \blacksquare$

---

## Compactness and Heine-Borel Theorem

**Exercise 4.**
Let $S \subseteq \mathbb{R}^n$ be an uncountable set. Show that $S$ has a limit point.

**Solution:**
Cover $\mathbb{R}^n$ using a countable collection of open balls $\{B_i\}_{i=1}^\infty$ (e.g., balls with rational centers and rational radii). Then:
$$ S = \bigcup_{i=1}^\infty (S \cap B_i) $$
Since $S$ is uncountable and a countable union of countable sets is countable, at least one subset $S \cap B_k$ must be uncountable.
Since $B_k$ is bounded, $S \cap B_k$ is a bounded uncountable (and hence infinite) set. By the Bolzano-Weierstrass Theorem, $S \cap B_k$ (and therefore $S$) must contain a limit point. $\quad \blacksquare$

---

**Def (Compactness):**
A subset $S \subseteq \mathbb{R}^n$ is **compact** if and only if every open cover of $S$ admits a finite subcover.

**Theorem (Heine-Borel Theorem).**
A subset $S \subseteq \mathbb{R}^n$ is compact if and only if $S$ is closed and bounded.

---

## $l_p$ Norms on $\mathbb{R}^n$

Besides the standard Euclidean norm ($l_2$ norm), other common norms on $\mathbb{R}^n$ include:

- **$l_1$ Norm**:
  $$ \|x\|_1 = \sum_{i=1}^n |x_i| $$

- **$l_2$ Norm** (Euclidean Norm):
  $$ \|x\|_2 = \sqrt{\sum_{i=1}^n x_i^2} $$

- **$l_\infty$ Norm** (Maximum Norm):
  $$ \|x\|_\infty = \max \{ |x_1|, \dots, |x_n| \} $$

- **$l_p$ Norm** ($p \ge 1$):
  $$ \|x\|_p = \left( \sum_{i=1}^n |x_i|^p \right)^{1/p} $$

```tikz
\begin{document}
\begin{tikzpicture}[>=stealth, scale=1.0]

  % l1 open ball
  \begin{scope}[shift={(0,0)}]
    \filldraw[fill=blue!10, draw=blue, thick, dashed] (1,0) -- (0,1) -- (-1,0) -- (0,-1) -- cycle;
    \draw[->] (-1.5,0) -- (1.5,0) node[right] {$x$};
    \draw[->] (0,-1.5) -- (0,1.5) node[above] {$y$};
    \node at (0,-1.8) {$l_1$ ball: $|x|+|y| < 1$};
  \end{scope}
  
  % l2 open ball
  \begin{scope}[shift={(4,0)}]
    \filldraw[fill=blue!10, draw=blue, thick, dashed] (0,0) circle (1);
    \draw[->] (-1.5,0) -- (1.5,0) node[right] {$x$};
    \draw[->] (0,-1.5) -- (0,1.5) node[above] {$y$};
    \node at (0,-1.8) {$l_2$ ball: $\sqrt{x^2+y^2} < 1$};
  \end{scope}

  % l3 open ball
  \begin{scope}[shift={(0,-4)}]
    \filldraw[fill=blue!10, draw=blue, thick, dashed] 
      plot[domain=0:1, samples=50] ({\x}, {(1-\x^3)^(1/3)}) -- 
      plot[domain=1:0, samples=50] ({\x}, {-(1-\x^3)^(1/3)}) -- 
      plot[domain=0:-1, samples=50] ({\x}, {-(1-(-\x)^3)^(1/3)}) -- 
      plot[domain=-1:0, samples=50] ({\x}, {(1-(-\x)^3)^(1/3)}) -- cycle;
    \draw[->] (-1.5,0) -- (1.5,0) node[right] {$x$};
    \draw[->] (0,-1.5) -- (0,1.5) node[above] {$y$};
    \node at (0,-1.8) {$l_3$ ball: $|x|^3+|y|^3 < 1$};
  \end{scope}

  % l_infinity open ball
  \begin{scope}[shift={(4,-4)}]
    \filldraw[fill=blue!10, draw=blue, thick, dashed] (-1,-1) rectangle (1,1);
    \draw[->] (-1.5,0) -- (1.5,0) node[right] {$x$};
    \draw[->] (0,-1.5) -- (0,1.5) node[above] {$y$};
    \node at (0,-1.8) {$l_\infty$ ball: $\max(|x|,|y|) < 1$};
  \end{scope}

\end{tikzpicture}
\end{document}
```

---

## Equivalent Metrics

Note that the open sets of $(\mathbb{R}^n, d_2)$ coincide with the open sets of $(\mathbb{R}^n, d_\infty)$.

**Def (Equivalent Metrics):**  
Two metrics $d$ and $\sigma$ on $\mathbb{R}^n$ are said to be **equivalent** if there exist constants $c, C > 0$ such that:
$$ c \, \sigma(x, y) \le d(x, y) \le C \, \sigma(x, y) \quad \forall x, y \in \mathbb{R}^n $$

---

**Exercise 5.**  
1. Show that $\tau(d) = \tau(\sigma)$ (i.e., equivalent metrics induce the same topology).  
2. Show that the $l_1$, $l_2$, and $l_\infty$ topologies on $\mathbb{R}^n$ are the same.

**Question:**  
If $B_\sigma(x; s) \subseteq B_d(x; r)$, how are the radii $r$ and $s$ related?

---

## Matrix Spaces $M_n(\mathbb{R})$ and Norms

**Def (Space of Matrices):**  
Let $M_n(\mathbb{R})$ denote the set of all $n \times n$ matrices over $\mathbb{R}$.

The vector space isomorphism $\Phi : \mathbb{R}^{n^2} \longrightarrow M_n(\mathbb{R})$ is defined by mapping a vector to a matrix column-by-column:
$$ (x_1, \dots, x_{n^2}) \longmapsto \begin{pmatrix} x_1 & x_{n+1} & \dots & x_{n^2-n+1} \\ \vdots & \vdots & \ddots & \vdots \\ x_n & x_{2n} & \dots & x_{n^2} \end{pmatrix} $$
$\Phi$ is a linear isomorphism.

### Matrix Operations
For $A = (a_{ij}), B = (b_{ij}) \in M_n(\mathbb{R})$:
- **Addition**: $A + B = (a_{ij} + b_{ij})$
- **Scalar Multiplication**: $\lambda A = (\lambda a_{ij})$
- **Matrix Multiplication**: $AB = \left( \sum_{k=1}^n a_{ik} b_{kj} \right)$

---

### Norms on $M_n(\mathbb{R})$

**Def (Hilbert-Schmidt Norm):**  
The **Hilbert-Schmidt norm** on $M_n(\mathbb{R})$ is defined as:
$$ \|A\|_{HS} = (\text{trace}(A^T A))^{1/2} = \left( \sum_{i,j=1}^n a_{ij}^2 \right)^{1/2} $$

**Def (Operator Norm):**  
The **operator norm** on $M_n(\mathbb{R})$ is defined as:
$$ \|A\|_{op} = \sup_{\|x\|_2 = 1} \|Ax\|_2 = \sup_{\|x\|_2 \leq 1} \|Ax\|_2 $$
*(Note: $\|A\|_{op}$ is finite as the continuous image of a compact set $\{x \in \mathbb{R}^n \mid \|x\|_2 = 1\}$ under the map $x \mapsto \|Ax\|_2$ is compact).*

**Corollary (Action on Vectors):**  
For any matrix $A \in M_n(\mathbb{R})$ and $z \in \mathbb{R}^n$:
$$ \|Az\|_2 \le \|A\|_{op} \|z\|_2 $$

**Proof:**  
- If $z = 0$, both sides are $0$, so the inequality holds trivially.
- If $z \neq 0$, set $x = \frac{z}{\|z\|_2}$. Since $\|x\|_2 = 1$, by definition of operator norm:
  $$ \left\| A \left(\frac{z}{\|z\|_2}\right) \right\|_2 \le \|A\|_{op} \implies \frac{\|Az\|_2}{\|z\|_2} \le \|A\|_{op} \implies \|Az\|_2 \le \|A\|_{op} \|z\|_2 \quad \blacksquare $$

---

**Corollary (Sub-multiplicativity of Operator Norm):**  
For any $A, B \in M_n(\mathbb{R})$:
$$ \|AB\|_{op} \le \|A\|_{op} \|B\|_{op} $$

**Proof:**  
For any $z \in \mathbb{R}^n$:
$$ \|ABz\|_2 \le \|A\|_{op} \|Bz\|_2 \le \|A\|_{op} \|B\|_{op} \|z\|_2 $$
Taking the supremum over all $z \in \mathbb{R}^n$ with $\|z\|_2 = 1$:
$$ \|AB\|_{op} = \sup_{\|z\|_2 = 1} \|ABz\|_2 \le \sup_{\|z\|_2 = 1} \|A\|_{op} \|B\|_{op} \|z\|_2 = \|A\|_{op} \|B\|_{op} \quad \blacksquare $$

---

**Proposition (Equivalence of Norms on $M_n(\mathbb{R})$):**  
The operator norm $\|\cdot\|_{op}$ and the Hilbert-Schmidt norm $\|\cdot\|_{HS}$ are equivalent norms on $M_n(\mathbb{R})$.

**Lemma:**  
For any $A \in M_n(\mathbb{R})$:
$$ \|A\|_{op} \le \|A\|_{HS} \quad \text{and} \quad \|A\|_{HS} \le \sqrt{n} \|A\|_{op} $$

**Proof of First Inequality ($\|A\|_{op} \le \|A\|_{HS}$):**  
Let $\{e_1, \dots, e_n\}$ be the standard Euclidean basis of $\mathbb{R}^n$.  
For any $v = \sum_{i=1}^n v_i e_i \in \mathbb{R}^n$ with $\|v\|_2 = 1$ (so $\sum_{i=1}^n v_i^2 = 1$):
$$ \|Av\|_2^2 = \left\| \sum_{i=1}^n v_i A e_i \right\|_2^2 \le \left( \sum_{i=1}^n |v_i| \|Ae_i\|_2 \right)^2 $$
By Cauchy-Schwarz inequality:
$$ \left( \sum_{i=1}^n |v_i| \|Ae_i\|_2 \right)^2 \le \left(\sum_{i=1}^n v_i^2\right) \left(\sum_{i=1}^n \|Ae_i\|_2^2\right) = \sum_{i=1}^n \|Ae_i\|_2^2 $$
Taking the supremum over all $\|v\|_2 = 1$:
$$ \|A\|_{op}^2 = \sup_{\|v\|_2 = 1} \|Av\|_2^2 \le \sum_{i=1}^n \|Ae_i\|_2^2 = \|A\|_{HS}^2 $$
Taking square roots yields $\|A\|_{op} \le \|A\|_{HS}$. $\quad \blacksquare$

**Proof of Second Inequality ($\|A\|_{HS} \le \sqrt{n} \|A\|_{op}$):**  
Since $\{e_1, \dots, e_n\}$ is the standard basis with $\|e_i\|_2 = 1$, we have:
$$ \|Ae_i\|_2 \le \|A\|_{op} \|e_i\|_2 = \|A\|_{op} \quad \forall i = 1, \dots, n $$
Thus:
$$ \|A\|_{HS}^2 = \sum_{i=1}^n \|Ae_i\|_2^2 \le \sum_{i=1}^n \|A\|_{op}^2 = n \|A\|_{op}^2 $$
Taking square roots yields $\|A\|_{HS} \le \sqrt{n} \|A\|_{op}$. $\quad \blacksquare$


