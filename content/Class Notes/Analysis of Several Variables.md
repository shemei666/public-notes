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

### Matrix Operations and Vector Space Structure

For $A = (a_{ij}), B = (b_{ij}) \in M_n(\mathbb{R})$:
- **Addition**: $A + B = (a_{ij} + b_{ij})$
- **Scalar Multiplication**: $\lambda A = (\lambda a_{ij})$
- **Matrix Multiplication**: $AB = \left( \sum_{k=1}^n a_{ik} b_{kj} \right)$

**Lemma:** $M_n(\mathbb{R})$ is a vector space over $\mathbb{R}$ of dimension $n^2$.

- **Examples of Vector Subspaces of $M_n(\mathbb{R})$**:
  - **Symmetric Matrices**: $\{ A \in M_n(\mathbb{R}) \mid A^T = A \}$
  - **Skew-Symmetric Matrices**: $\{ A \in M_n(\mathbb{R}) \mid A^T = -A \}$
  - **Traceless Matrices**: $\{ A \in M_n(\mathbb{R}) \mid \text{trace}(A) = 0 \}$

---

### Matrix Groups and Subgroups

**Def (General Linear Group):**  
The **General Linear Group** of degree $n$ over $\mathbb{R}$ is defined as:
$$ GL_n(\mathbb{R}) := \{ A \in M_n(\mathbb{R}) \mid \det(A) \neq 0 \} \subseteq M_n(\mathbb{R}) $$

**Lemma:** For $A, B \in M_n(\mathbb{R})$, $\det(AB) = \det(A)\det(B)$.

**Lemma:** $(GL_n(\mathbb{R}), \cdot)$ with matrix multiplication forms a group.

- **Examples of Subgroups of $GL_n(\mathbb{R})$**:
  - **Special Linear Group**:  
    $$ SL_n(\mathbb{R}) := \{ A \in GL_n(\mathbb{R}) \mid \det(A) = 1 \} $$
  - **Orthogonal Group**:  
    $$ O_n(\mathbb{R}) := \{ A \in GL_n(\mathbb{R}) \mid A^T A = I_n \} $$

---

### Topological Properties of Matrix Groups

**Proposition (Topology of Matrix Subgroups):**  
1. **$SL_n(\mathbb{R})$ is Closed**:  
   The determinant map $\det : M_n(\mathbb{R}) \longrightarrow \mathbb{R}$ is continuous (as a polynomial in matrix entries). Since $\{1\}$ is a closed subset of $\mathbb{R}$, $SL_n(\mathbb{R}) = \det^{-1}(\{1\})$ is closed in $M_n(\mathbb{R}) \cong \mathbb{R}^{n^2}$.

2. **$O_n(\mathbb{R})$ is Compact**:  
   - **Closed**: The map $f : M_n(\mathbb{R}) \longrightarrow M_n(\mathbb{R})$ given by $f(A) = A^T A$ is continuous. Since $O_n(\mathbb{R}) = f^{-1}(\{I_n\})$ and $\{I_n\}$ is closed, $O_n(\mathbb{R})$ is closed. Alternatively, $O_n(\mathbb{R}) = \bigcap_{i=1}^k f_i^{-1}(\{e_i\})$.
   - **Bounded**: For any $A \in O_n(\mathbb{R})$, its column vectors $a_1, \dots, a_n$ satisfy $\|a_i\|_2 = 1$. Thus, the Hilbert-Schmidt norm is $\|A\|_{HS} = \sqrt{\sum_{i=1}^n \|a_i\|_2^2} = \sqrt{n}$. Since the norm is bounded by $\sqrt{n}$, $O_n(\mathbb{R})$ is a bounded subset of $\mathbb{R}^{n^2}$.
   - By the **Heine-Borel Theorem**, since $O_n(\mathbb{R})$ is closed and bounded in $\mathbb{R}^{n^2}$, it is **compact**. $\quad \blacksquare$

---

### Norms on $M_n(\mathbb{R})$

**Def (Hilbert-Schmidt Norm):**  
The **Hilbert-Schmidt norm** on $M_n(\mathbb{R})$ is defined as:
$$ \|A\|_{HS} = (\text{trace}(A^T A))^{1/2} = \left( \sum_{i,j=1}^n a_{ij}^2 \right)^{1/2} $$

**Def (Operator Norm):**  
The **operator norm** on $M_n(\mathbb{R})$ is defined as:
$$ \|A\|_{op} = \sup_{\|x\|_2 = 1} \|Ax\|_2 = \sup_{\|x\|_2 \leq 1} \|Ax\|_2 $$
*(Note: $\|A\|_{op}$ is finite as the continuous image of a compact set $\{x \in \mathbb{R}^n \mid \|x\|_2 = 1\}$ under the map $x \mapsto \|Ax\|_2$ is compact).*

---

**Lemma (Operator Norm Axioms).**  
The operator norm $\|\cdot\|_{op}$ is a norm on $M_n(\mathbb{R})$.

**Proof:**  
Since $\|Az\|_2 \ge 0$ for all $\|z\|_2 = 1$, we have $\|A\|_{op} \ge 0$, and:
$$ \|A\|_{op} = 0 \iff \sup_{\|z\|_2 = 1} \|Az\|_2 = 0 \iff 0 \le \|Az\|_2 \le 0 \quad \forall \|z\|_2 = 1 \iff Az = 0 \quad \forall z \iff A = 0 $$

Likewise, for any $\lambda \in \mathbb{R}$:
$$ \|\lambda A\|_{op} = \sup_{\|z\|_2 = 1} \|\lambda A z\|_2 = |\lambda| \sup{\|z\|_2 = 1} \|Az\|_2 = |\lambda| \|A\|_{op} $$

Finally, to verify the triangle inequality:
$$
\begin{aligned}
\|A + B\|_{op} &= \sup_{\|z\|_2 = 1} \|(A + B)z\|_2 \\
&\le \sup_{\|z\|_2 = 1} \left( \|Az\|_2 + \|Bz\|_2 \right) \quad (\text{by triangle inequality on } d_2) \\
&\le \sup_{\|z\|_2 = 1} \|Az\|_2 + \sup_{\|z\|_2 = 1} \|Bz\|_2 \quad (\text{by subadditivity of } \sup) \\
&= \|A\|_{op} + \|B\|_{op} \quad \blacksquare
\end{aligned}
$$

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

---

## Sequences of Functions and Uniform Convergence

**Def (Pointwise and Uniform Convergence):**  
Let $\{f_k\}_{k=1}^\infty$ be a sequence of functions $f_k : \mathbb{R}^m \longrightarrow \mathbb{R}$.
- **Pointwise Convergence**: $\{f_k\}$ converges pointwise to $f$ on a subset $S \subseteq \mathbb{R}^m$ if for every $x \in S$:
  $$ f_k(x) \longrightarrow f(x) \quad \text{as } k \to \infty $$
- **Uniform Convergence**: $\{f_k\}$ converges uniformly to $f$ on $S \subseteq \mathbb{R}^m$ if for every $\varepsilon > 0$, there exists $N \in \mathbb{N}$ such that:
  $$ |f_k(x) - f(x)| < \varepsilon \quad \forall x \in S \text{ and } \forall k \ge N $$

**Theorem (Uniform Limit Theorem):**  
If $\{f_k\}$ is a sequence of continuous functions on $S \subseteq \mathbb{R}^m$ and $f_k \longrightarrow f$ uniformly on $S$, then the limit function $f$ is continuous on $S$.

---

## Matrix Exponential and Series in $M_n(\mathbb{R})$

**Def (Matrix Exponential):**  
For $A \in M_n(\mathbb{R})$, the **matrix exponential** is defined as:
$$ \exp(A) = \sum_{n=0}^\infty \frac{A^n}{n!} $$

---

**Exercise 6.**  
1. **Absolute Convergence Test for Matrix Series**: Show that a series $\sum_{n=0}^\infty A_n$ is convergent in $M_n(\mathbb{R})$ if the series of operator norms $\sum_{n=0}^\infty \|A_n\|_{op}$ is convergent.
2. **Exponential of Commuting Matrices**: Show that if $A, B \in M_n(\mathbb{R})$ commute ($AB = BA$), then:
   $$ \exp(A + B) = \exp(A) \exp(B) $$
   *(Hint: Use the Cauchy product for power series).*
3. **Invertibility of Matrix Exponential**: Show that $\exp(0) = I$ and $\exp(A - A) = \exp(A) \exp(-A)$, concluding that $\exp(A)$ is always invertible with $(\exp(A))^{-1} = \exp(-A)$.
4. **Continuity of Matrix Exponential**: Show that the function $\exp : M_n(\mathbb{R}) \longrightarrow M_n(\mathbb{R})$ is continuous.

---

### Well-Definedness of Matrix Exponential

To verify that the matrix exponential map
$$ \exp : M_n(\mathbb{R}) \longrightarrow M_n(\mathbb{R}), \quad A \longmapsto \sum_{n=0}^\infty \frac{A^n}{n!} = \exp(A) $$
is well-defined, we must verify that the defining series converges for every $A \in M_n(\mathbb{R})$.

**Lemma (Sub-power Inequality for Operator Norm).**  
For any matrix $A \in M_n(\mathbb{R})$ and integer $n \ge 0$:
$$ \|A^n\|_{op} \le \|A\|_{op}^n $$

**Proof:**  
Follows by induction using the sub-multiplicativity property $\|AB\|_{op} \le \|A\|_{op} \|B\|_{op}$. $\quad \blacksquare$

---

**Proposition (Convergence of Matrix Exponential).**  
The series $\sum_{n=0}^\infty \frac{A^n}{n!}$ is convergent in $M_n(\mathbb{R})$ for every $A \in M_n(\mathbb{R})$, and hence $\exp(A)$ is well-defined.

**Proof:**  
Let $S_m = \sum_{n=0}^m \frac{A^n}{n!}$ denote the $m$-th partial sum of the matrix series in $M_n(\mathbb{R})$, and set $\alpha = \|A\|_{op}$. For any integers $m > k \ge 0$, using the triangle inequality and sub-multiplicativity of the operator norm $\|A^n\|_{op} \le \alpha^n$:
$$ \|S_m - S_k\|_{op} = \left\| \sum_{n=k+1}^m \frac{A^n}{n!} \right\|_{op} \le \sum_{n=k+1}^m \frac{\|A^n\|_{op}}{n!} \le \sum_{n=k+1}^m \frac{\alpha^n}{n!} = s_m - s_k $$
where $s_m = \sum_{n=0}^m \frac{\alpha^n}{n!}$ is the sequence of partial sums of the real power series $\sum_{n=0}^\infty \frac{\alpha^n}{n!} = e^\alpha$. Since $\sum_{n=0}^\infty \frac{\alpha^n}{n!}$ converges in $\mathbb{R}$, its sequence of partial sums $\{s_m\}$ is Cauchy. Thus, for any $\varepsilon > 0$, there exists $N \in \mathbb{N}$ such that for all $m > k \ge N$:
$$ |s_m - s_k| = \sum_{n=k+1}^m \frac{\alpha^n}{n!} < \varepsilon \implies \|S_m - S_k\|_{op} < \varepsilon $$
This shows that $\{S_m\}_{m=0}^\infty$ is a Cauchy sequence in the metric space $(M_n(\mathbb{R}), \|\cdot\|_{op})$. Since $M_n(\mathbb{R}) \cong \mathbb{R}^{n^2}$ is complete, every Cauchy sequence in $M_n(\mathbb{R})$ converges to a limit in $M_n(\mathbb{R})$. Therefore, the limit $\lim_{m\to\infty} S_m = \sum_{n=0}^\infty \frac{A^n}{n!} = \exp(A)$ exists in $M_n(\mathbb{R})$. $\quad \blacksquare$

---

**Theorem:**  
Let $A, B \in M_n(\mathbb{R})$. If $A$ and $B$ commute ($AB = BA$), then:
$$ \exp(A + B) = \exp(A) \exp(B) $$

**Proof:**  
Since the series for $\exp(A) = \sum_{j=0}^\infty \frac{A^j}{j!}$ and $\exp(B) = \sum_{k=0}^\infty \frac{B^k}{k!}$ are absolutely convergent, their matrix product is given by the Cauchy product of the series:
$$ \exp(A)\exp(B) = \sum_{n=0}^\infty \sum_{k=0}^n \frac{A^{n-k}}{(n-k)!} \frac{B^k}{k!} = \sum_{n=0}^\infty \frac{1}{n!} \sum_{k=0}^n \frac{n!}{(n-k)!\, k!} A^{n-k} B^k = \sum_{n=0}^\infty \frac{1}{n!} \sum_{k=0}^n \binom{n}{k} A^{n-k} B^k $$
Since $A$ and $B$ commute ($AB = BA$), the matrix binomial expansion holds:
$$ (A + B)^n = \sum_{k=0}^n \binom{n}{k} A^{n-k} B^k $$
Substituting this identity into the series yields:
$$ \exp(A)\exp(B) = \sum_{n=0}^\infty \frac{(A + B)^n}{n!} = \exp(A + B) \quad \blacksquare $$



