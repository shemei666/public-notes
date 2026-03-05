---
publish: true
---
# Optimization

## Basic Concepts

1. **Decision Space**: $X$
2. **Objective Function**: $f$ on $X$

### Optimization Problem
1. Minimize $f$ on $X$
2. Find $\arg \min_{x \in X} f(x)$

#### General Form
1. Minimize $f_0(x)$
2. Subject to:
   $$ f_i(x) \leq b_i, \quad x = (x_1, \dots, x_n) $$
   where $f_0: \mathbb{R}^n \to \mathbb{R}$ and $f_i: \mathbb{R}^n \to \mathbb{R}$.

> [!INFO] Definition: Optimal Solution
> A vector $x^*$ is called **optimal** or a **solution** to the optimization problem if it has the smallest objective score among all vectors satisfying the constraints.

## Examples

### 1. Least Square Optimization
Fitting a linear model $y = \beta_0 + \beta_1 x$ to a set of data points $(x_i, Y_i)$.
- **Decision Space**: $(\beta_0, \beta_1) \in \mathbb{R}^2$ represents the parameters of the line.
- **Objective Function**: Minimize the sum of squared errors:
  $$ f(\beta_0, \beta_1) = \sum_{i=1}^m (Y_i - \beta_0 - \beta_1 x_i)^2 $$

### 2. Linear Programming (LP)
Optimizing a linear objective function subject to linear equality and inequality constraints.

$$ \min_{\vec{x}} c^T \vec{x} $$

Subject to: $\vec{a}_i^T \vec{x} \leq b_i$ for $i=1,\dots,k$ (polyhedral constraints).

### 3. Optimal Transport
Finding the most efficient way to transport mass from one distribution to another.
- **Cost Function**: $c: M \times F \to \mathbb{R}_+$ (cost to move unit mass from $m \in M$ to $f \in F$).
- **Transport Plan**: $T: M \times F \to \mathbb{R}_+$ (map indicating destination for each source point).
- **Objective**: Minimize total transport cost $C(T) = \sum_{m \in M} c(m, T(m))$.

### 4. Variational Analysis (Brachistochrone Problem)
Finding the path between two points that a particle would slide down in the shortest time under gravity.
- **Decision Space**: Space of smooth curves connecting points A and B.
- **Objective**: Minimize the time taken for descent.

---

## Linear Programming Problem (LPP)

$$ \min f_0(x_1, \dots, x_n) = c_1 x_1 + \dots + c_n x_n $$
where $c_1, \dots, c_n$ are costs associated with the variables.

Subject to:
$$
\begin{pmatrix} a_{11} x_1 + \dots + a_{1n} x_n \leq b_1 \\ \vdots \\ a_{m1} x_1 + \dots + a_{mn} x_n \leq b_m \end{pmatrix}
$$

**Parameters**: $C_n$, $\{a_{ij}\}_{\substack{1 \le i \le m \\ 1 \le j \le n}}$, $b_1, \dots, b_m$.

**GOAL**: Understand the geometry of the decision space (Affine sets, convex sets, convex cones $\subseteq \mathbb{R}^n$).

---

## Geometry of Decision Space

### Affine Sets

> [!INFO] Definition: Affine Set
> A set $C \subseteq \mathbb{R}^n$ is said to be **affine** if the unique line through two distinct points in $C$ lies in $C$.

**Mathematical Characterization**:
If $\vec{x}, \vec{y} \in C$, then $\vec{x} + \epsilon (\vec{y}-\vec{x}) \in C$ for all $\epsilon \in \mathbb{R}$.
Alternatively, for $\vec{x}_1, \dots, \vec{x}_k \in S$:
$$ \text{aff}(S) = \{ \theta_1 \vec{x}_1 + \dots + \theta_k \vec{x}_k \mid \theta_1 + \dots + \theta_k = 1, k \in \mathbb{N} \} $$
This is the set of all **affine combinations** of vectors in $S$.

### Convex Sets

> [!INFO] Definition: Convex Set
> A set $C \subseteq \mathbb{R}^n$ is said to be **convex** if the line segment joining any two distinct points in $C$ lies in $C$.

**Mathematical Characterization**:
If $\vec{x}_1, \vec{x}_2 \in C$, then $\theta \vec{x}_1 + (1-\theta) \vec{x}_2 \in C$ for all $\theta \in [0, 1]$.
(Equivalently: $\theta_1 \vec{x}_1 + \theta_2 \vec{x}_2 \in C$ for $\theta_1, \theta_2 \ge 0, \theta_1 + \theta_2 = 1$)

![[IMG_20260112_154714.jpg]]

> [!EXAMPLE] Convexity of Linear Inequalities
> Consider the set defined by $a_{11} x_1 + \dots + a_{1n} x_n \leq b_1$.
> Let $\vec{x}, \vec{y}$ satisfy the inequality.
> Then for $\theta \in [0,1]$:
> $$ a_{1\cdot}(\theta x_1 + (1-\theta) y_1) + \dots + a_{1n} (\theta x_n + (1-\theta) y_n) $$
> $$ = \theta (\vec{a}^T \vec{x}) + (1-\theta) (\vec{a}^T \vec{y}) \le \theta b_1 + (1-\theta) b_1 = b_1 $$
> Thus, the set is convex.

> [!QUESTION] Converse Question
> Is every convex subset of $\mathbb{R}^n$ given by a collection of linear inequalities?
> **Answer**: Yes, as long as you allow the collection to be infinite.

Every convex function is a supremum of linear functions.

> [!QUESTION] Closure Property
> Is the closure of a convex set also convex?
> **Answer**: Yes. If $x_n \to x$ and $y_n \to y$ with $x_n, y_n \in C$, then limits of convex combinations remain in closure.

> [!INFO] Definition: Convex Hull
> The **convex hull** of $S \subseteq \mathbb{R}^n$, denoted $\text{conv}(S)$, is the smallest convex set in $\mathbb{R}^n$ containing $S$.
> $$ \text{conv}(S) = \{ \theta_1 \vec{x}_1 + \dots + \theta_k \vec{x}_k \mid \vec{x}_i \in S, \sum \theta_i = 1, \theta_i \ge 0 \} $$

**Intersection Property**:
$\vec{x}_1, \vec{x}_2 \in C_1 \cap C_2 \implies [\theta \vec{x}_1 + (1-\theta) \vec{x}_2] \in C_1 \cap C_2$.
(The intersection of convex sets is convex).

### Cones

> [!INFO] Definition: Cone
> A set $C \subseteq \mathbb{R}^n$ is said to be a **cone** if for every $\vec{x} \in C$ and $\theta \ge 0$, we have $\theta \vec{x} \in C$.

> [!INFO] Definition: Convex Cone
> A set is a **convex cone** if it is both convex and a cone.
> Equivalently: For any $\vec{x}_1, \vec{x}_2 \in C$ and $\theta_1, \theta_2 \ge 0 \implies \theta_1 \vec{x}_1 + \theta_2 \vec{x}_2 \in C$.

#### Summary of Combinations

| Type | Combination | Condition |
| :--- | :--- | :--- |
| **Affine** | $\theta_1 \vec{x}_1 + \theta_2 \vec{x}_2$ | $\theta_1 + \theta_2 = 1$ |
| **Convex** | $\theta_1 \vec{x}_1 + \theta_2 \vec{x}_2$ | $\theta_1 + \theta_2 = 1, \theta_1, \theta_2 \ge 0$ |
| **Cone** | $\theta_1 \vec{x}_1 + \theta_2 \vec{x}_2$ | $\theta_1, \theta_2 \ge 0$ |

> [!INFO] Definition: Conic Hull
> The **conic hull** of $S \subseteq \mathbb{R}^n$ is the smallest convex cone containing $S$.

> [!INFO] Definition: Proper Cone
> A cone $K \subseteq \mathbb{R}^{n}$ is a **proper cone** if:
> 1. $K$ is convex.
> 2. $K$ is closed.
> 3. $K$ has non-empty interior.
> 4. $K$ is pointed (contains no lines, only rays from origin).

**Generalized Inequalities**:
We can define a partial ordering $\leq_{K}$ on $\mathbb{R}^{n}$ by:
$$ \vec{x} \leq_{K} \vec{y} \iff \vec{y} - \vec{x} \in K $$

Properties of $\leq_K$:
1. $\vec{x} + \vec{z} \leq_{K} \vec{y} + \vec{z}$ for all $\vec{z} \in \mathbb{R}^{n}$
2. $\alpha \vec{x} \leq_{K} \alpha \vec{y}$ for all $\alpha \geq 0$
3. If $\vec{x}_j \le_K \vec{y}_j \forall j$ and $\vec{x}_j \to \vec{x}, \vec{y}_j \to \vec{y}$, then $\vec{x} \le_K \vec{y}$.

> [!EXAMPLE] Examples of Proper Cones
> 1. $K = [0, \infty)$ is a proper cone in $\mathbb{R}$.
> 2. $K = [0, \infty)^n$ (Non-negative orthant) is a proper cone in $\mathbb{R}^n$.

**Relevance to LP**:
LP problems can be generalized to $A \vec{x} \le_{K} \vec{b}$.

### Hulls Summary
Let $S$ be a set in $\mathbb{R}^{r}$.
1. **Convex hull** of $S$: Smallest convex set containing $S$.
2. **Affine hull** of $S$: Smallest affine set containing $S$.
3. **Conic hull** (or Positive hull) of $S$: Smallest convex cone containing $S$.

**Question**: Let $C$ be a line-free closed convex set in $\mathbb{R}^{n}$. What is the smallest set $S$ such that $C = \text{conv}(S)$?

---

## Examples of Convex Sets

### Hyperplanes

> [!INFO] Definition: Hyperplane
> A hyperplane in $\mathbb{R}^{n}$ is a set of the form:
> $$ H_{\vec{a},b}= \{ \vec{x} \in \mathbb{R}^{n} \mid \vec{a}^{T}\vec{x} = b \} $$
> Geometrically, $H_{\vec{a},b}$ has normal vector $\vec{a}$, with offset $b$ from origin.

> [!TIP] Riesz Representation Theorem
> Every linear function on $\mathbb{R}^{n}$ is of the form $\vec{x} \mapsto \langle \vec{a}, \vec{x} \rangle$ for some $\vec{a} \in \mathbb{R}^{n}$.
>
> > [!NOTE]- Proof
> > Let $f: \mathbb{R}^n \to \mathbb{R}$ be a linear function. Let $\{\vec{e}_1, \dots, \vec{e}_n\}$ be the standard basis for $\mathbb{R}^n$. Any $\vec{x} \in \mathbb{R}^n$ can be written as $\vec{x} = \sum_{i=1}^n x_i \vec{e}_i$. By linearity:
> > $$f(\vec{x}) = f\left(\sum_{i=1}^n x_i \vec{e}_i\right) = \sum_{i=1}^n x_i f(\vec{e}_i)$$
> > Let $a_i = f(\vec{e}_i)$ and $\vec{a} = (a_1, \dots, a_n)^T$. Then:
> > $$f(\vec{x}) = \sum_{i=1}^n x_i a_i = \langle \vec{a}, \vec{x} \rangle$$

**Correspondence**:
$$ \text{Non-zero linear functionals} \longleftrightarrow (n-1)\text{-dimensional subspaces of } \mathbb{R}^{n} $$
$$ \rho \longleftrightarrow \ker \rho $$

> [!c] Exercise
> Let $P_{1}, P_{2}$ be linear functionals on $\mathbb{R}^{n}$ such that $\ker P_{1} = \ker P_{2}$. Prove that $P_{1} = \alpha P_{2}$ for some $\alpha \in \mathbb{R}\setminus \{ 0 \}$.

### Half-spaces

> [!INFO] Definition: Half-space
> A closed half-space in $\mathbb{R}^{n}$ is a set of the form:
> $$ H_{\vec{a},b}^- = \{ \vec{x} \in \mathbb{R}^{n} \mid \vec{a}^T\vec{x} \leq b \} $$
> $$ H_{\vec{a},b}^+ = \{ \vec{x} \in \mathbb{R}^{n} \mid \vec{a}^T\vec{x} \geq b \} $$

```tikz
\begin{document}
\begin{tikzpicture}[>=stealth, scale=1.2]
    % Define coordinates for the hyperplane (line)
    \coordinate (A) at (-2.5, 0.5);
    \coordinate (B) at (2.5, -1.5);

    % Shade the half-space {x | a^T x <= b}
    \fill[blue!10] (A) -- (B) -- (2.5, -2.5) -- (-2.5, -2.5) -- cycle;

    % Draw the hyperplane boundary
    \draw[thick, blue!80!black] (A) -- (B) node[midway, below left, blue] {$H_{\vec{a},b}$};

    % Draw the normal vector 'a'
    % The line vector is (5, -2). A perpendicular vector is (2, 5)
    \coordinate (M) at (0, -0.5); % A point on the line
    \draw[->, ultra thick, red!70!black] (M) -- ++(0.6, 1.5) node[above] {$\vec{a}$};

    % Right angle symbol
    \draw[gray] (M) ++(0.1, 0.25) -- ++(0.2, -0.08) -- ++(-0.1, -0.25);

    % Label the half-space
    \node[blue!80!black] at (-0.5, -1.5) {$\{\vec{x} \mid \vec{a}^T\vec{x} \leq b\}$};
\end{tikzpicture}
\end{document}
```

The normal vector $\vec{a}$ points in the direction of increasing values of the linear functional. The half-space $\vec{a}^T\vec{x} \leq b$ extends in the direction opposite to $\vec{a}$.

**Properties**:
- Hyperplanes are affine sets.
- Half-spaces are convex but not affine.
- Intersections of closed half-spaces are either empty or convex.
- The boundary of $H_{\vec{a},b}^{-}$ is $H_{\vec{a},b}$.

### Polyhedra

> [!INFO] Definition: Polyhedron
> A **polyhedron** is the solution set of a finite number of linear equalities and inequalities:
> $$ \mathcal{P} := \{ \vec{x} \in \mathbb{R}^{n} \mid \vec{a}_{i}^{T}\vec{x} \leq b_{i}, i = 1,\dots,m, \quad \vec{c}_{j}^{T}\vec{x} = d_{j}, j = 1,\dots,p \} $$

- A polyhedron is the intersection of a finite number of half-spaces and hyperplanes.
- **Polytope**: A bounded polyhedron (always compact).

> [!NOTE] Why are points and lines polyhedra?
> 1. **Point**: A single point in $\mathbb{R}^n$ is the intersection of $n$ independent hyperplanes.
> 2. **Line**: A line is an affine set, defined by the intersection of $n-1$ independent hyperplanes.

**Relevance to LP**: If the decision space is a polytope, the existence of an optimal solution is guaranteed.

### Supporting Hyperplanes

> [!INFO] Definition: Supporting Hyperplane
> A hyperplane $H$ **supports** a set $S \subseteq \mathbb{R}^n$ at $\vec{x} \in \text{bd}(S)$ if $\vec{x} \in S \cap H$ and $S$ is contained entirely in one of the closed half-spaces defined by $H$.

```tikz
\begin{document}
\begin{tikzpicture}[>=stealth, scale=1.3]
    % Draw Set S (Ellipse)
    \filldraw[fill=blue!10, draw=blue!80!black, thick] (0,0) ellipse (2 and 1.2);
    \node[blue!80!black] at (0,-0.2) {$S$};

    % Point x on boundary
    \coordinate (X) at (1.0, 1.039);
    \fill[black] (X) circle (1.5pt) node[below left] {$\vec{x}$};

    % Draw Supporting Hyperplane
    \draw[thick, red!80!black] (3.39, 0.32) -- (-1.39, 1.76) node[midway, above right, black] {$H_{\vec{a},b}$};

    % Draw Normal Vector a
    \draw[->, ultra thick, red!70!black] (X) -- (1.29, 2.00) node[right] {$\vec{a}$};

    % Label Half-spaces
    \node[red!80!black] at (1.43, 2.47) {$H_{\vec{a},b}^+$};
    \node[blue!80!black] at (0.57, -0.40) {$H_{\vec{a},b}^-$};
\end{tikzpicture}
\end{document}
```

If $H_{\vec{a},b}$ supports $S$ and $S \subseteq H_{\vec{a},b}^{-}$, then $\vec{a}$ is called an **outer normal vector**.

> [!NOTE] Non-convex sets
> Not every point on the boundary of a closed set $S$ must have a supporting hyperplane.
>
> ```tikz
> \begin{document}
> \begin{tikzpicture}[>=stealth, scale=1.3]
>     % Non-convex set S (Heart/Kidney shape)
>     \filldraw[fill=blue!10, draw=blue!80!black, thick]
>         (1,0)
>         .. controls (0,0) and (-0.5, 1.5) .. (0, 2)
>         .. controls (0.5, 2.5) and (1, 1.5) .. (1, 1) % The Dent at (1,1)
>         .. controls (1, 1.5) and (1.5, 2.5) .. (2, 2)
>         .. controls (2.5, 1.5) and (2, 0) .. (1, 0);
>
>     \node[blue!80!black] at (1, 0.5) {$S$};
>
>     % The point x at the dent
>     \coordinate (X) at (1, 1);
>     \fill[black] (X) circle (1.5pt) node[below=3pt] {$\vec{x}$};
>
>     % Draw a candidate "tangent" line
>     \draw[thick, dashed, red!80!black] (-0.5, 1) -- (2.5, 1);
>     \node[red!80!black, font=\small] at (2.5, 1.2) {Intersects $S$};
>
>     \node[black, font=\small, align=center] at (1, -0.5) {No single hyperplane can\\contain $S$ entirely on one side};
> \end{tikzpicture}
> \end{document}
> ```

> [!c] Exercise
> Prove that for a smooth Jordan curve, there can be at most one supporting hyperplane at a point.

---

## Representation Theorems

> [!TIP] Theorem: Intersection of Half-spaces
> Each nonempty closed convex set in $\mathbb{R}^{n}$ is the intersection of its supporting half-spaces (hence given by a collection of linear inequalities).

> [!TIP] Theorem: Extremal Representation
> Each nonempty closed convex set $C \subseteq \mathbb{R}^n$ is of the form $C = C_{lf} \oplus V$, where:
> - $V$ is a linear subspace of $\mathbb{R}^n$.
> - $C_{lf}$ is a **line-free** closed convex set in a subspace complementary to $V$.
>
> Furthermore, each nonempty line-free closed convex set is the convex hull of its extreme points and extreme rays.

```tikz
\begin{document}
\begin{tikzpicture}[>=stealth, scale=1]
    % Draw V (Linear Subspace) - Vertical Axis
    \draw[->, ultra thick, blue] (0, -2.5) -- (0, 2.5) node[above] {$V$ (Subspace)};

    % Draw C_lf (Line-free part) - A horizontal disk/ellipse
    \filldraw[fill=green!20, draw=green!60!black, thick] (0,0) ellipse (1.5 and 0.4);

    % Annotation for C_lf
    \draw[->, thin, green!40!black] (2.0, 0) node[right] {$C_{lf}$ (Line-free part)} -- (1.55, 0);

    % Draw the full set C (Cylinder) = C_lf + V
    \draw[gray, dashed] (0, 2) ellipse (1.5 and 0.4);
    \draw[gray, dashed] (0, -2) ellipse (1.5 and 0.4);

    % Vertical sides
    \draw[gray, thick] (-1.5, -2) -- (-1.5, 2);
    \draw[gray, thick] (1.5, -2) -- (1.5, 2);

    % Shading for the cylinder (set C)
    \shade[left color=blue!10, right color=blue!5, opacity=0.3] (-1.5, -2) rectangle (1.5, 2);

    % Annotation for C
    \node[blue!80!black] at (-2.2, 1.5) {$C = C_{lf} \oplus V$};
    \node[font=\footnotesize, align=center, blue!80!black] at (-2.2, 1.0) {(Infinite Cylinder)};

    % Decomposition Vector Visualization
    \coordinate (O) at (0,0);
    \coordinate (c) at (1.2, -0.2); 
    \coordinate (v) at (0, 1.5);    
    \coordinate (sum) at (1.2, 1.3);

    \draw[->, red, thick] (O) -- (c) node[midway, below] {$c \in C_{lf}$};
    \draw[->, blue, thick] (c) -- (sum) node[midway, right] {$v \in V$};
    \fill[purple] (sum) circle (1.5pt) node[above right] {$x = c + v$};
\end{tikzpicture}
\end{document}
```

> [!INFO] Definition: Extreme Point
> Let $C$ be a nonempty closed convex set. A point $\vec{v} \in C$ is an **extreme point** if:
> $$ \vec{v} = \frac{\vec{x} + \vec{y}}{2}, \quad \text{with } \vec{x}, \vec{y} \in C \implies \vec{x} = \vec{y} = \vec{v} $$

> [!c] Exercise
> Prove that if $C \subseteq \mathbb{R}^{n}$ is a closed set such that midpoint convexity holds (i.e., $\vec{x}, \vec{y} \in C \implies (\vec{x} + \vec{y})/2 \in C$), then $C$ is a convex set.

> [!TIP] Corollary (Minkowski's Theorem)
> Each nonempty compact convex set $K \subseteq \mathbb{R}^{n}$ is the convex hull of its extreme points.

---

## Nearest Point Map (Metric Projection)

> [!TIP] Lemma: Existence and Uniqueness
> Let $K$ be a nonempty closed convex set. For each $\vec{x} \in \mathbb{R}^{n}$, there is a unique point $P_{K}(\vec{x}) \in K$ satisfying:
> $$ \lVert \vec{x} - P_{K}(\vec{x}) \rVert \leq \lVert \vec{x} - \vec{y} \rVert \quad \forall \vec{y} \in K $$

> [!NOTE]- Proof
> **Existence**: Follows from the fact that $K$ is closed (distance function is continuous and attains minimum on closed sets).
> **Uniqueness**: Suppose $\vec{y}_{1}, \vec{y}_{2} \in K$ are distinct points with minimal distance $d = d(\vec{x}, K)$.
> By Parallelogram Law:
> $$ 2 \lVert \vec{y}_1 - \vec{x} \rVert^2 + 2 \lVert \vec{y}_2 - \vec{x} \rVert^2 = \lVert \vec{y}_1 - \vec{y}_2 \rVert^2 + 4 \left\lVert \frac{\vec{y}_1+\vec{y}_2}{2} - \vec{x} \right\rVert^2 $$
> $$ 4d^2 = \lVert \vec{y}_1 - \vec{y}_2 \rVert^2 + 4 \left\lVert \frac{\vec{y}_1+\vec{y}_2}{2} - \vec{x} \right\rVert^2 $$
> Since $K$ is convex, $\frac{\vec{y}_1+\vec{y}_2}{2} \in K$, so $\left\lVert \frac{\vec{y}_1+\vec{y}_2}{2} - \vec{x} \right\rVert \ge d$.
> It follows that $\lVert \vec{y}_1 - \vec{y}_2 \rVert^2 \le 0$, so $\vec{y}_1 = \vec{y}_2$.

> [!INFO] Definition: Metric Projection
> The map $P_{K}: \mathbb{R}^{n} \to K$ is called the **metric projection** or nearest point map.
> Define $u(K, \vec{x}) := \frac{\vec{x} - P_{K}(\vec{x})}{d(K, \vec{x})}$ for $\vec{x} \notin K$.
>
> The **ray** through $\vec{x}$ is:
> $$ R(K, \vec{x}) := \{ P_{K}(\vec{x}) + \lambda u(K, \vec{x}) \mid \lambda \geq 0 \} $$

### Contractive Property

> [!TIP] Theorem:
> $P_{K}$ is a contractive type mapping:
> $$ \lVert P_{K}(\vec{x}) - P_{K}(\vec{y}) \rVert \leq \lVert \vec{x} - \vec{y} \rVert \quad \forall \vec{x}, \vec{y} \in \mathbb{R}^{n} $$

```tikz
\begin{document}
\begin{tikzpicture}[>=stealth, scale=1.3]
    % Draw Convex Set K
    \filldraw[fill=blue!10, draw=blue!80!black, thick] (-1, -1) rectangle (3.5, 0);
    \node[blue!80!black] at (3, -0.5) {$K$};

    % Points x and y
    \coordinate (X) at (0, 1.5);
    \coordinate (Y) at (2.5, 2.0);

    \fill[black] (X) circle (1.5pt) node[above left] {$\vec{x}$};
    \fill[black] (Y) circle (1.5pt) node[above right] {$\vec{y}$};

    % Projections Px and Py
    \coordinate (Px) at (0, 0);
    \coordinate (Py) at (2.5, 0);

    \fill[black] (Px) circle (1.5pt) node[below] {$P_K(\vec{x})$};
    \fill[black] (Py) circle (1.5pt) node[below] {$P_K(\vec{y})$};

    % Projection lines
    \draw[dashed, thin, gray] (X) -- (Px);
    \draw[dashed, thin, gray] (Y) -- (Py);

    % Distance lines
    \draw[<->, thick, red!80!black] (X) -- (Y) node[midway, above, sloped] {$|\vec{x} - \vec{y}|$};
    \draw[<->, thick, green!40!black] (Px) -- (Py) node[midway, above, sloped] {$|P_K(\vec{x}) - P_K(\vec{y})|$};
\end{tikzpicture}
\end{document}
```

> [!NOTE]- Proof
> Define:
> $$ \phi(t) = \lVert \vec{x} - ((1-t)P_{K}(\vec{x}) + tP_{K}(\vec{y})) \rVert^2 $$
> Maps $\phi: [0,1] \to \mathbb{R}_{\ge 0}$.
> Expanding:
> $$
> \begin{align*}
> \phi(t) &= \lVert \vec{x} - P_{K}(\vec{x}) + t(P_{K}(\vec{x}) - P_{K}(\vec{y})) \rVert^2 \\
> &= \lVert \vec{x} - P_{K}(\vec{x}) \rVert^2 + 2t \langle \vec{x} - P_{K}(\vec{x}), P_{K}(\vec{x}) - P_{K}(\vec{y}) \rangle + t^2 \lVert P_{K}(\vec{x}) - P_{K}(\vec{y}) \rVert^2
> \end{align*}
> $$
> Differentiating:
> $$ \phi'(t) = 2 \langle \vec{x} - P_{K}(\vec{x}), P_{K}(\vec{x}) - P_{K}(\vec{y}) \rangle + 2t \lVert P_{K}(\vec{x}) - P_{K}(\vec{y}) \rVert^2 $$
> Since $P_K(\vec{x})$ minimizes distance, $\phi(t)$ is minimized at $t=0$, so $\phi'(0) \ge 0$:
> $$
> \begin{gather}
> 2 \langle \vec{x} - P_{K}(\vec{x}), P_{K}(\vec{x}) - P_{K}(\vec{y}) \rangle \ge 0 \\
> \implies \langle \vec{x} - P_{K}(\vec{x}), P_{K}(\vec{y}) - P_{K}(\vec{x}) \rangle \le 0
> \end{gather}
> $$
> A symmetric argument for $\vec{y}$ gives:
> $$
> \begin{gather}
> \langle \vec{y} - P_{K}(\vec{y}), P_{K}(\vec{x}) - P_{K}(\vec{y}) \rangle \le 0 \\
> \langle P_{K}(\vec{x}) - P_{K}(\vec{y}), P_{K}(\vec{y}) - \vec{y} \rangle \ge 0 \implies \langle P_{K}(\vec{y}) - \vec{y}, P_{K}(\vec{x}) - P_{K}(\vec{y}) \rangle \ge 0 \\
>  \langle P_{K}(\vec{y}) - \vec{y}, P_{K}(\vec{y}) - P_{K}(\vec{x}) \rangle \le 0 \text{)}
> \end{gather}
> $$
> Adding the two inequalities:
> $$
> \begin{gather}
> \langle \vec{x} - \vec{y}, P_{K}(\vec{y}) - P_{K}(\vec{x}) \rangle \le \langle P_{K}(\vec{x}) - P_{K}(\vec{y}), P_{K}(\vec{y}) - P_{K}(\vec{x}) \rangle \\
> \langle \vec{x} - \vec{y}, P_{K}(\vec{x}) - P_{K}(\vec{y}) \rangle \ge \lVert P_{K}(\vec{x}) - P_{K}(\vec{y}) \rVert^2
> \end{gather}
> $$
> By Cauchy-Schwarz:
> $$ 
> \lVert P_{K}(\vec{x}) - P_{K}(\vec{y}) \rVert^2 \le \lVert \vec{x} - \vec{y} \rVert \lVert P_{K}(\vec{x}) - P_{K}(\vec{y}) \rVert 
> $$
> If $P_{K}(\vec{x}) \neq P_{K}(\vec{y})$, dividing gives:
> $$ 
> \lVert P_{K}(\vec{x}) - P_{K}(\vec{y}) \rVert \le \lVert \vec{x} - \vec{y} \rVert 
> $$

### Projection of Sphere

> [!TIP] Lemma
> Let $S$ be a sphere containing $K$ in its interior. Then $P_{K}(S) = \partial K$.

> [!NOTE]- Proof of Lemma
> ($P(S) \subseteq \partial K$): Immediate from the definition of the metric projection onto $K$.
>
> ($\partial K \subseteq P(S)$): Let $\vec{v} \in \partial K$. For each $n \in \mathbb{N}$, choose $\vec{x}_{n} \in \text{int}(S) \setminus K$ such that $\lVert \vec{x}_{n} - \vec{v} \rVert < \frac{1}{n}$.
>
> Consider the ray $R_{K}(\vec{x}_{n})$ emanating from $P_{K}(\vec{x}_{n})$ through $\vec{x}_{n}$. Since $S$ encloses $K$, this ray intersects $S$ at a unique point $\vec{y}_{n}$.
>
> **Claim**: The projection of the entire ray $R_{K}(\vec{x}_{n})$ onto $K$ is the singleton $\{P_{K}(\vec{x}_{n})\}$.
> *Proof*: Let $\vec{r}$ be any point on the ray $R_K(\vec{x}_n)$. If $P_K(\vec{r}) \neq P_K(\vec{x}_n)$, then we form a triangle with vertices $P_K(\vec{x}_n)$, $P_K(\vec{r})$ and $\vec{r}$ having two obtuse angles, which is impossible.
>  We have,
> 1. $\langle \vec{x}_n - P_K(\vec{x}_n), P_K(\vec{r}) - P_K(\vec{x}_n) \rangle \le 0$
> 2. $\langle \vec{r} - P_K(\vec{r}), P_K(\vec{x}_n) - P_K(\vec{r}) \rangle \le 0$
>
> Since $\vec{r}$ lies on the ray from $P_K(\vec{x}_n)$ through $\vec{x}_n$, we have $\vec{r} - P_K(\vec{r}) = P_K(\vec{x}_n) - P_K(\vec{r}) + \lambda(\vec{x}_n - P_K(\vec{x}_n))$ for some $\lambda > 0$. Substituting into (2):
> $$ \langle P_K(\vec{x}_n) - P_K(\vec{r}) + \lambda(\vec{x}_n - P_K(\vec{x}_n)), P_K(\vec{x}_n) - P_K(\vec{r}) \rangle \le 0 $$
> $$ \| P_K(\vec{x}_n) - P_K(\vec{r}) \|^2 + \lambda \langle \vec{x}_n - P_K(\vec{x}_n), P_K(\vec{x}_n) - P_K(\vec{r}) \rangle \le 0 $$
> $$ \| P_K(\vec{x}_n) - P_K(\vec{r}) \|^2 - \lambda \langle \vec{x}_n - P_K(\vec{x}_n), P_K(\vec{r}) - P_K(\vec{x}_n) \rangle \le 0 $$
> From (1), we have that both terms are non-negative, their sum can only be $\le 0$ if both are zero.
> Thus $\| P_K(\vec{x}_n) - P_K(\vec{r}) \|^2 = 0$, implying $P_K(\vec{r}) = P_K(\vec{x}_n)$. In particular $P_K(\vec{y}_n) = P_K(\vec{x}_n)\quad \blacksquare$
>
> Since $S$ is compact, $(\vec{y}_n)$ has a convergent subsequence $\vec{y}_{n_k} \to \vec{y} \in S$. By continuity of $P_K$:
> $$ P_K(\vec{y}) = \lim_{k \to \infty} P_K(\vec{y}_{n_k}) = \lim_{k \to \infty} P_K(\vec{x}_{n_k}) $$
> Since $\vec{x}_{n} \to \vec{v}$ and $\vec{v} \in \partial K \subseteq K$, we have $P_K(\vec{x}_{n}) \to \vec{v}$.
> Thus $P_K(\vec{y}) = \vec{v}$, implying $\vec{v} \in P_K(S)\quad \blacksquare$


> [!TIP] Corollary
> Let $K$ be a nonempty closed convex proper subset of $\mathbb{R}^{n}$. Then $P_{K}(\mathbb{R}^{n} \setminus K) = \partial K$.

> [!c] Exercise
> Prove that $\phi(t) = \lVert \vec{x} - ((1-t)P_{K}(\vec{x}) + t\vec{z}) \rVert$ for $\vec{z} \not\in K$ is a strictly increasing function on $[0,1]$.

```tikz
\begin{document}
\begin{tikzpicture}[>=stealth, scale=1]
    % Sphere S
    \draw[thick, blue] (0,0) circle (3cm);
    \node[blue] at (2.5, 2.5) {$S$};

    % Convex Set K
    \filldraw[fill=gray!10, draw=black, thick] (0,0) ellipse (1.5cm and 1cm);
    \node at (0,0) {$K$};

    % Point v on boundary
    \coordinate (v) at (1.3, 0.5);
    \fill[red] (v) circle (1.5pt) node[left] {$\vec{v}$};

    % Point P(x_n) near v
    \coordinate (Pxn) at (1.4, 0.34);
    \fill[black] (Pxn) circle (1.5pt) node[below left] {$P(\vec{x}_n)$};

    % Ray R_K(x_n)
    \coordinate (yn) at (2.8, 1.0);
    \draw[thick, ->, orange!80!black] (Pxn) -- (yn) node[midway, above] {$R_K(\vec{x}_n)$};
    \fill[black] (yn) circle (1.5pt) node[right] {$\vec{y}_n$};
\end{tikzpicture}
\end{document}
```



### Support Density

> [!TIP] Theorem
> Let $K \subseteq \mathbb{R}^{n}$ be a nonempty closed convex set. If $K$ is bounded, then to each vector $\vec{u} \in \mathbb{R}^{n} \setminus \{0\}$ there corresponds a support plane to $K$ with exterior normal vector $\vec{u}$.
> That is, the map $U_{K}: \mathbb{R}^{n} \setminus \{0\} \to S^{n-1}$ is surjective.



## Separation Properties of Convex Sets

> [!INFO] Definition: Separation
> Let $A, B \subseteq \mathbb{R}^n$ and $H_{\vec{a},b} \subseteq \mathbb{R}^n$ be a hyperplane. We say $H_{\vec{a},b}$ **separates** $A$ and $B$ if:
> $$ A \subseteq H_{\vec{a},b}^- \quad \text{and} \quad B \subseteq H_{\vec{a},b}^+ \quad (\text{or vice versa}) $$
>
> 1. The separation is said to be **proper** if $A, B$ both do not lie in $H_{\vec{a},b}$.
> 2. $A, B$ are **strictly separated** if:
>    $$ A \subseteq \text{int}(H_{\vec{a},b}^-) \quad \text{and} \quad B \subseteq \text{int}(H_{\vec{a},b}^+) \quad (\text{or vice versa}) $$
> 3. $A, B$ are **strongly separated** by $H_{\vec{a},b}$ if there is an $\epsilon > 0$ such that $H_{\vec{a},b-\epsilon}$ and $H_{\vec{a},b+\epsilon}$ both separate $A$ and $B$.

> [!TIP] Theorem: Separation of Point and Convex Set
> Let $K \subseteq \mathbb{R}^n$ be a nonempty closed convex proper subset of $\mathbb{R}^n$ and let $\vec{x} \notin K$. Then $K$ and $\{\vec{x}\}$ can be strongly separated.

> [!NOTE]- Proof
> 1. The hyperplane through $P_K(\vec{x})$ ($\in K$) and orthogonal to $u(K, \vec{x}) = \frac{\vec{x}-P_K(\vec{x})}{\|\vec{x}-P_K(\vec{x})\|}$ supports $K$.
> 2. The parallel hyperplane through $\frac{\vec{x}+P_K(\vec{x})}{2}$ **strongly separates** $K$ and $\vec{x}$.

---

## Representation Theorem 1

> [!TIP] Theorem
> Each nonempty proper closed convex set in $\mathbb{R}^n$ is the intersection of its supporting halfspaces.

> [!NOTE]- Proof
> Let $\mathcal{K}$ be the collection of supporting halfspaces for $K$.
> Clearly $K \subseteq \bigcap_{A \in \mathcal{K}} A$.
   If possible let $\vec{x} \in \left(\bigcap_{A \in \mathcal{K}} A\right) \setminus K$.
> This leads to a **Contradiction**! (see previous theorem: Separating Hyperplane Theorem).
> Thus, $K = \bigcap \{ H_{\vec{a},b}^- \mid H_{\vec{a},b} \text{ supports } K \}$.
>
%% > $$ K = \{ \vec{x} \in \mathbb{R}^n \mid \langle \vec{a}, \vec{x} \rangle \leq b, \quad \forall \vec{a} \in \mathbb{R}^n, b \in \mathbb{R} \text{ defining support} \} $$ %%

 > [!c] Exercise
 > Show that the indexing set can be chosen to be countable.

> [!TIP] Lemma
> Let $A, B \subseteq \mathbb{R}^n$ be nonempty subsets. $A, B$ can be separated (strictly separated, resp.) if and only if $A-B$ and $\{0\}$ can be separated (strictly separated, resp.).
> $$ A-B := \{ \vec{x} - \vec{y} \mid \vec{x} \in A, \vec{y} \in B \} $$
>

 > [!NOTE]- Proof Sketch
 > There is a linear functional $\rho$ such that $\rho(\vec{x}) \le b$ for  all$\vec{x} \in A-B$.
 > $0 = \rho(\vec{0}) \ge b$

#todo

---
> [!TIP] Lemma
> If $K \subseteq \mathbb{R}^{n}$ is closed  convex set with $K\neq conv(relbd K)$ then $K$ is either an affine set or half space in an affine space.

> [!NOTE]- Proof
> WLOG Assume $aff(K) = \mathbb{R}^{n}$
> $K = int(K) \cup \partial K \subseteq int(K) \cup \overline{conv(\partial K)} \subseteq K$
> [refer convex bodies]


> [!INFO] Definition: 
> A set $A \subseteq  \mathbb{R}^{n}$ is said to be line-free if A contains no affine lines, In particular it does not contain a non-trivial affine set. 

> [!INFO] Definition: Recession Cone 
> Let $K\subseteq \mathbb{R}^{n}$  be a closed convex set $rec(K) = \{  u \in \mathbb{R}^{n}\mid K + u \subseteq K \}$ 
>
> > [!EXAMPLE] Examples
> > 1. **Bounded Set**: Let $D$ be a disk (or any compact set). Then $\text{rec}(D) = \{\vec{0}\}$.
> > 2. **Ray**: Let $R_{\vec{x}} = \{ \vec{x} + \lambda \vec{u} \mid \lambda \ge 0 \}$ be a ray starting at $\vec{x}$ in direction $\vec{u}$.
> >    Then $\text{rec}(R_{\vec{x}}) = \{ \lambda \vec{u} \mid \lambda \ge 0 \}$ (The ray starting at the origin in direction $\vec{u}$). 

> [!QUESTION] Exercise
> The recession cone of a closed convex set is a convex cone
> 

> [!TIP] Lemma
> Each closed convex set $K \subseteq \mathbb{R}^{n}$ can be represented in the form $K = \overline{K} \oplus V$, where $V$ is a linear subspace of $\mathbb{R}^{n}$ and $K$ is a line-free closed convex set in a complementary subspace to $V$

> [!NOTE]- Proof
> $V := rec(K) \cap (- rec(K))$,  linear subspace of $\mathbb{R}^{n}$ containing all vector that are parallel to some line in $K$. Let $U$ be a complementary subspace of $V$ (passing through $K$)

## Extreme Points and Rays

> [!INFO] Definition: Face
> Let $K \subseteq \mathbb{R}^n$ be a convex set.
> A **face** of $K$ is a convex subset $F \subseteq K$ such that each line segment $[\vec{x}, \vec{y}] \subseteq K$ with $(\vec{x}, \vec{y}) \cap F \neq \emptyset$ must be contained in $F$.
>
> Equivalently, for $\vec{x}, \vec{y} \in K$, if $\frac{\vec{x}+\vec{y}}{2} \in F$, then $\vec{x}, \vec{y} \in F$.

> [!INFO] Definition: Extreme Point
> If $\{\vec{z}\}$ is a face of $K$, then $\vec{z}$ is called an **extreme point**.
> The set of all extreme points of $K$ is denoted by $\text{ext}(K)$.

> [!INFO] Definition: Extreme Ray
> An **extreme ray** of $K$ is a ray in $K$ that is a face of $K$.
> $\text{extr}(K)$ denotes the set of all extreme rays of $K$.

> [!TIP] Theorem: Representation of Line-Free Sets
> Each line-free closed convex set $K \subseteq \mathbb{R}^n$ is the convex hull of its extreme points and extreme rays.

> [!TIP] Lemma
> Let $H$ be a supporting hyperplane of $K$.
> Every face of $H \cap K$ is a face of $K$.

> [!NOTE]- Proof
> $F$ - face of $H \cap K$. To Prove: $F$ is a face of $K$.
> $\vec{x}, \vec{y} \in K$ and $(\vec{x}, \vec{y}) \cap F \neq \emptyset$.
> $(\implies \text{To show } \vec{x}, \vec{y} \in F)$
>
> $(\vec{x}, \vec{y}) \cap H \neq \emptyset$
> [ $\rho(\vec{z}) = c$ ]
> $\implies \vec{x} \in H, \vec{y} \in H \implies \vec{x} \in H \cap K, \vec{y} \in H \cap K$
> $\implies \vec{x}, \vec{y} \in F$. (Since $F$ is a face of $H \cap K$)
> $\blacksquare$

> [!NOTE]- Proof of Representation Theorem
> **Case 1**: $\dim(K) = 1$.
> Since $K$ is line-free, $K$ cannot be a line.
> Thus $K$ is either a **line segment** (bounded) or a **ray** (unbounded).
>
> | $\inf K$ | $\sup K$ | Type | Representation |
> | :--- | :--- | :--- | :--- |
> | $> -\infty$ | $< \infty$ | Line Segment $[a,b]$ | $\text{conv}(\{a,b\})$ |
> | $> -\infty$ | $= \infty$ | Ray $[a, \infty)$ | $\text{conv}(\{a\} \cup \vec{r})$ |
> | $= -\infty$ | $< \infty$ | Ray $(-\infty, b]$ | $\text{conv}(\{b\} \cup \vec{r})$ |
> | $= -\infty$ | $= \infty$ | Line $(-\infty, \infty)$ | (Not line-free) |
>
> **Induction Step**: Assume true for $\dim(K) < n$.
> Let $\dim(K) = n$.
> We want to show $K \subseteq \text{conv}(\text{ext}(K) \cup \text{extr}(K))$.
> [WLOG $K$ has non-empty interior]
>
> Let $\vec{v} \in K$.
> If $\vec{v} \in \text{int}(K)$, take any line through $\vec{v}$. It intersects $\partial K$ at two points (since $K$ is line-free).
> Thus $\vec{v}$ is a convex combination of points in $\partial K$.
> So it suffices to show $\partial K \subseteq \text{conv}(\text{ext}(K) \cup \text{extr}(K))$.
>
> Let $\vec{x} \in \partial K$. By the Supporting Hyperplane Theorem, there exists a supporting hyperplane $H$ of $K$ containing $\vec{x}$.
> Consider $K \cap H$.
> $H$ is a supporting hyperplane of $K$.
> $K \cap H$ is a face of $K$ (and a line-free closed convex set).
> $\dim(K \cap H) < n$.
>
> By induction hypothesis:
> $$ K \cap H = \text{conv}(\text{ext}(K \cap H) \cup \text{extr}(K \cap H)) $$
> By the Lemma, $\text{ext}(K \cap H) \subseteq \text{ext}(K)$ and $\text{extr}(K \cap H) \subseteq \text{extr}(K)$.
> Thus:
> $$ K \cap H \subseteq \text{conv}(\text{ext}(K) \cup \text{extr}(K)) $$
> Since this holds for any $\vec{x} \in \partial K$ and any supporting hyperplane $H$ at $\vec{x}$, we have:
> $$ \partial K \subseteq \text{conv}(\text{ext}(K) \cup \text{extr}(K)) $$
>
> Now, since $K = \text{conv}(\partial K)$ (for line-free closed convex sets), we have:
> $$ K \subseteq \text{conv}(\text{ext}(K) \cup \text{extr}(K)) $$
> The reverse inclusion is trivial. $\blacksquare$

> [!TIP] Corollary: Minkowski's Theorem
> Each nonempty compact convex set $K \subseteq \mathbb{R}^n$ is the convex hull of its extreme points.

> [!QUESTION] Exercise
> Prove or disprove $K\subseteq \mathbb{R}^{n}$ is a closed convex set with non-empty interior (unless affine or affine halfspace) $K= conv(\partial K)$

---
#todo  Fridays class LPS starting.

---
> [!TIP] Theorem: 
> In LPS, let $w \in \mathbb{R}^{n}$. Then $w$ is an extreme point of feasible set $F$ iff $w$ is a bfs (w.r.t some $J$)

> [!TIP] Corollary
> The feasible set in LPS has finitely many extreme points

> [!NOTE]- Proof
> Each extreme point is a bfs, hence determined by some n-element subset of the columns of $A$.
> No. of extreme points $\leq {n \choose m}$

> [!INFO] Definition: 
> A basic feasible solution is degenerate if it has strictly more than $n-m$ zeroes

> [!TIP] Proposition
> If two different bases $(J_{1},J_{2})$ correspond to a single b.f.s $v$, then it is degenerate

> [!NOTE]- Proof
> Let $J_1, J_2$ be two distinct bases.
> We know $\vec{x}_{J_1^c} = \vec{0}_{n-m}$ and $\#(J_1) = m$.
> Similarly $\vec{x}_{J_2^c} = \vec{0}_{n-m}$ and $\#(J_2) = m$.
> The set of indices where $\vec{v}$ is zero includes $J_1^c \cup J_2^c$.
> Since $J_1 \neq J_2$, we have $J_1^c \neq J_2^c$.
> Two distinct sets of size $n-m$ must have a union of size strictly greater than $n-m$.
> $$ \#(J_1^c \cup J_2^c) \ge n-m+1 $$
> (Alternatively, $\#(J_1 \cap J_2) \le m-1$).
> Thus, the number of zero components in $\vec{v}$ is at least $n-m+1$.
> Therefore, $\vec{v}$ is degenerate. $\blacksquare$

> [!QUESTION] Exercise
> If $\vec{v}$ is degenerate, is it necessarily true that there are two different bases corresponding to $\vec{v}$? (Prove or provide counterexample)

> [!TIP] Lemma
> Suppose $P = \{ \vec{x} \in \mathbb{R}^n \mid A\vec{x} \le \vec{b} \}$ is a polyhedron. Then $\vec{v}$ is an extreme point of $P$ iff there are $n$ linearly independent active constraints among $A\vec{x} \le \vec{b}$ that are **tight** at $\vec{v}$, that is, satisfy equality at $\vec{v}$.
>
> **Note**: In LPs, $m$ of the constraints are always tight. Hence $\vec{v}$ is extreme iff $n-m$ of the constraints $\vec{x} \ge \vec{0}$ are tight ($A\vec{x}=\vec{b}, \vec{x} \ge \vec{0}$).

> [!NOTE]- Proof
> $(\implies)$ Let $\vec{v}$ be an extreme point. Let $B\vec{x} \le \vec{b}'$ be those constraints among $A\vec{x} \le \vec{b}$ that are tight at $\vec{v}$ (i.e., $B\vec{v} = \vec{b}'$).
>
> To show: $\text{rank}(B) \ge n$.
> On the contrary, assume $\text{rank}(B) \le n-1$.
> Choose $\vec{w} \in \text{nullspace}(B) \setminus \{\vec{0}\}$.
> Consider $\vec{v}' = \vec{v} + \epsilon \vec{w}$.
> Then $B\vec{v}' = B\vec{v} + \epsilon B\vec{w} = \vec{b}'$ (since $B\vec{w} = \vec{0}$).
> For a sufficiently small $\epsilon > 0$, both $\vec{v} + \epsilon \vec{w}$ and $\vec{v} - \epsilon \vec{w}$ satisfy the remaining strict inequalities (since strict inequality is an open condition).
> Thus, $\vec{v} \pm \epsilon \vec{w} \in P$.
> But $\vec{v} = \frac{(\vec{v} + \epsilon \vec{w}) + (\vec{v} - \epsilon \vec{w})}{2}$.
> Since $\vec{w} \neq \vec{0}$, these points are distinct. This contradicts that $\vec{v}$ is an extreme point.
> Thus, $\text{rank}(B) = n$, meaning there are $n$ linearly independent tight constraints.
>
> $(\impliedby)$ Let $B\vec{x} \le \vec{b}'$ be tight at $\vec{v}$ and $\text{rank}(B) = n$.
> Suppose $\vec{v} = \frac{\vec{v}_1 + \vec{v}_2}{2}$ where $\vec{v}_1, \vec{v}_2 \in P$.
> Then:
> $\vec{b}' = B\vec{v} = \frac{1}{2} B\vec{v}_1 + \frac{1}{2} B\vec{v}_2 \le \frac{1}{2} \vec{b}' + \frac{1}{2} \vec{b}' = \vec{b}'$
> Since $B\vec{v}_1 \le \vec{b}'$ and $B\vec{v}_2 \le \vec{b}'$ (as $\vec{v}_1, \vec{v}_2 \in P$), the only way the average is $\vec{b}'$ is if both are equal to $\vec{b}'$.
> $$ B\vec{v} = B\vec{v}_1 = B\vec{v}_2 = \vec{b}' $$
> Since $\text{rank}(B) = n$, the columns of $B$ are linearly independent, so the system $B\vec{x} = \vec{b}'$ has a unique solution.
> $\implies \vec{v} = \vec{v}_1 = \vec{v}_2$.
> $\implies \vec{v}$ is an extreme point of $P$. $\blacksquare$

### Geometry of Constraints

> [!NOTE] Remark
> Let $\vec{a}_1, \dots, \vec{a}_n$ be linearly independent vectors in $\mathbb{R}^n$ and $b_1, \dots, b_n \in \mathbb{R}$.
> Then the intersection of the hyperplanes is a single point:
> $$ \bigcap_{i=1}^n H_{\vec{a}_i, b_i} = \{\vec{v}\} $$
> This is equivalent to solving the system:
> $$ \begin{bmatrix} \vec{a}_1^T \\ \vdots \\ \vec{a}_n^T \end{bmatrix} \vec{x} = \begin{bmatrix} b_1 \\ \vdots \\ b_n \end{bmatrix} $$
> Since the matrix is invertible, there exists a unique solution $\vec{v}$.

## Unboundedness and Fundamental Theorem

> [!INFO] Definition: Unbounded Problem
> We say that a minimization problem is **unbounded** if for each real $B$, there is a feasible point of cost strictly less than $B$.

> [!TIP] Theorem
> In LPS, suppose that $\vec{p} \in F$ (feasible set). Then either the LPS instance is **unbounded** or there is a **extreme point** $\vec{v}$ of $F$ satisfying:
> $$ \langle \vec{c}, \vec{v} \rangle \le \langle \vec{c}, \vec{p} \rangle $$
> (i.e., either there is no optimal solution or there is an optimal extreme point).

> [!INFO] Definition: reduced cost
> $\bar{c_{j}} = c_{j}-\vec{c_{B}}^{T}B^{-1}A_{j}$  

> [!TIP] Theorem:
> If $\overline{x}$ is a b.f.s. w.r.t $B$ and $\overline{c}$ is the vector of reduced costs.
> 1. $\overline{c}_{1} \geq 0, \dots, \overline{c}_{n} \geq 0 \implies \overline{x}$ is optimal
> 2. $\overline{x}$ is optimal and non-degenerate $\implies \overline{c}_{1} \geq 0, \dots, \overline{c}_{n} \geq 0$ ($\overline{c} \ge \vec{0}$)

### Building a Feasible Direction

For a fixed non-basic variable index $j$, we build a feasible direction $\vec{d}$ such that it makes $x_{j}$ into a basic variable:

$$ \vec{d}_{B} = -B^{-1}A_{j} $$
$$ d_{j} = 1, \quad d_{i} = 0 \text{ for } i \in N \setminus \{j\} $$

### Cost Analysis and Reduced Cost

Let $\vec{c}^T \vec{x}$ be the cost at the current b.f.s. $\vec{x}$. If we move along a feasible direction $\vec{d}$ with step length $\theta \ge 0$, the new cost is:
$$ \vec{c}^T (\vec{x} + \theta \vec{d}) $$

The **rate of change** in the cost as we move along $\vec{d}$ starting at $\vec{x}$ is given by:
$$ \vec{c}^T \vec{d} = \vec{c}_B^T \vec{d}_B + \vec{c}_N^T \vec{d}_N $$

Since we chose $\vec{d}$ such that $d_j = 1$ and $d_i = 0$ for all other non-basic indices $i \in N \setminus \{j\}$, we have:
$$ \vec{c}_N^T \vec{d}_N = c_j $$

Substituting $\vec{d}_B = -B^{-1}A_j$:
$$ \vec{c}^T \vec{d} = \vec{c}_B^T (-B^{-1}A_j) + c_j = c_j - \vec{c}_B^T B^{-1}A_j $$

This is exactly the **reduced cost** $\overline{c}_j$:
$$ \overline{c}_j = c_j - \vec{c}_B^T B^{-1}A_j $$

### Determining the Step Length

We want to find the maximum possible step length $\theta^*$ such that we stay within the feasible set $P$:
$$ \theta^* = \max \{ \theta \ge 0 \mid \vec{x} + \theta \vec{d} \in P \} $$

The resulting change in cost when moving from $\vec{x}$ to $\vec{x} + \theta^* \vec{d}$ is $\theta^* \vec{c}^T \vec{d}$.

#### Case I: $\vec{d} \ge \vec{0}$
If all components of the direction vector $\vec{d}$ are non-negative, then:
$$ \vec{x} + \theta \vec{d} \ge \vec{0} \quad \forall \theta \ge 0 $$
Since $\vec{d}$ is a feasible direction, $A\vec{d} = \vec{0}$. Thus, $A(\vec{x} + \theta \vec{d}) = A\vec{x} + \theta A\vec{d} = \vec{b}$, so the constraints are always satisfied.
In this case, the feasible set is unbounded in direction $\vec{d}$ and:
$$ \theta^* = \infty $$

#### Case II: $d_i < 0$ for some $i$
To maintain feasibility ($x_i + \theta d_i \ge 0$), we must have $\theta \le -\frac{x_i}{d_i}$ for all $i$ such that $d_i < 0$. 

If $x_j$ is a non-basic variable ($j \in N$), it is either chosen as the **entering variable** ($d_j = 1$), or it is not the entering variable (in which case $d_j = 0$). Since $\vec{d}_B$ depends on the choice of $j$, the maximum step length is determined by the basic variables:

$$ \theta^* = \min_{1 \le i \le m, d_{B(i)} < 0} \left( -\frac{x_{B(i)}}{d_{B(i)}} \right) $$

This $\theta^*$ is used to move from the current b.f.s. $\vec{x}$ to a new b.f.s. where $x_j > 0$.

### Step II: Update and Pivoting

Assume $\theta^*$ is chosen and finite (recall that if $\vec{d}_B \ge \vec{0}$, $\theta^* = \infty$). Let $l$ be the minimizing index such that:
$$ \theta^* = -\frac{x_{B(l)}}{d_{B(l)}} $$

For any $i$ where $d_{B(i)} < 0$, we know $\theta^* \le -\frac{x_{B(i)}}{d_{B(i)}}$, which implies:
$$ x_{B(i)} + \theta^* d_{B(i)} \ge 0 $$

For the minimizing index $l$, this inequality is tight:
$$ x_{B(l)} + \theta^* d_{B(l)} = 0 $$

Thus, as we move to the new point $\vec{y} = \vec{x} + \theta^* \vec{d}$, the variable $x_{B(l)}$ becomes zero ($x_{B(l)} \to 0$). The variable $x_{B(l)}$ leaves the basis (the **leaving variable**), while $x_j$ enters the basis.

> [!TIP] Theorem
> (a) The columns $A_{B(i)}$ ($i \neq l$) and $A_j$ are linearly independent (the new matrix $\overline{B}$ is a basis matrix).
> (b) $\vec{y} = \vec{x} + \theta^* \vec{d}$ (where $\vec{d}_B = -B^{-1}A_j$) is a basic feasible solution associated with $\overline{B}$.

> [!NOTE]- Proof of Theorem (a)
> Let $\overline{B}$ be the new matrix formed by replacing $A_{B(l)}$ with $A_j$. Let $\lambda_i$ be scalars such that:
> $$ \sum_{i=1}^m \lambda_i A_{\overline{B}(i)} = \vec{0} $$
> Since $A_{\overline{B}(l)} = A_j$ and $A_{\overline{B}(i)} = A_{B(i)}$ for $i \neq l$, we have:
> $$ \sum_{i \neq l} \lambda_i A_{B(i)} + \lambda_l A_j = \vec{0} $$
> Multiplying on the left by $B^{-1}$:
> $$ \sum_{i \neq l} \lambda_i (B^{-1} A_{B(i)}) + \lambda_l B^{-1} A_j = \vec{0} $$
> Since $B^{-1} A_{B(i)} = \vec{e}_i$ (the $i$-th standard basis vector) and $B^{-1} A_j = -\vec{d}_B$, we get:
> $$ \left[ \begin{smallmatrix} \lambda_1 \\ \vdots \\ \lambda_{l-1} \\ 0 \\ \vdots \\ \lambda_m \end{smallmatrix} \right] + \lambda_l (B^{-1}A_j) = \vec{0} $$
> Looking at the $l$-th component of this vector equation, the first vector has a $0$. Since $\vec{d}_B = -B^{-1}A_j$, the $l$-th component of $B^{-1}A_j$ is $-d_{B(l)}$. From the pivoting step, we know $d_{B(l)} < 0$, so $-d_{B(l)} > 0$. 
> Thus, the $l$-th equation is:
> $$ 0 + \lambda_l (-d_{B(l)}) = 0 \implies \lambda_l = 0 $$
> Since $\lambda_l = 0$, the remaining sum is $\sum_{i \neq l} \lambda_i \vec{e}_i = \vec{0}$, which immediately implies $\lambda_i = 0$ for all $i \neq l$.
> Therefore, the columns of $\overline{B}$ are linearly independent, and $\overline{B}$ is a valid basis matrix. $\blacksquare$

> [!NOTE]- Proof of Theorem (b)
> To show $\vec{y} = \vec{x} + \theta^* \vec{d}$ is a basic feasible solution (b.f.s.) associated with $\overline{B}$, we must show:
> 1. $\vec{y}$ is feasible ($A\vec{y} = \vec{b}$ and $\vec{y} \ge \vec{0}$).
> 2. The non-basic variables associated with $\overline{B}$ are zero.
>
> First, feasibility:
> Since $\vec{d}$ is a feasible direction, $A\vec{d} = \vec{0}$. Thus:
> $$ A\vec{y} = A(\vec{x} + \theta^* \vec{d}) = A\vec{x} + \theta^* A\vec{d} = \vec{b} + \vec{0} = \vec{b} $$
> By the choice of $\theta^*$, we ensured that $x_i + \theta^* d_i \ge 0$ for all $i$. Thus:
> $$ \vec{y} = \vec{x} + \theta^* \vec{d} \ge \vec{0} $$
> So $\vec{y}$ is feasible.
>
> Second, basic variables constraint:
> By our choice of minimizing index $l$, the leaving basic variable becomes exactly 0:
> $$ y_{B(l)} = x_{B(l)} + \theta^* d_{B(l)} = 0 $$
> Also, for non-basic indices $i \in N \setminus \{j\}$:
> $$ y_i = x_i + \theta^* d_i = 0 + \theta^*(0) = 0 $$
> Thus, all variables not in the new basis $\overline{B}$ (which is exactly $N \setminus \{j\} \cup \{B(l)\}$) are zero.
> (Note: $y_{\overline{B}(i)}$ is not necessarily 0 for $i \neq l$, as $y_{B(i)} = x_{B(i)} > 0$ if non-degenerate).
>
> Since $\overline{B}$ is a valid basis matrix (by part a) and $\vec{y} \ge 0, A\vec{y}=\vec{b}$ with non-basis components 0, $\vec{y}$ is a b.f.s. associated with $\overline{B}$. $\blacksquare$

---
### Algorithm Pseudocode:

**Step I.** $\vec{x}$ - b.f.s. w.r.t. basis matrix $B = [A_{B(1)} \mid \dots \mid A_{B(m)}]$.

**Step II.** Compute reduced costs $\overline{c}_j = c_j - \vec{c}_B^T B^{-1} A_j$ ($j \in N$). If they are all non-negative the current b.f.s. ($\vec{x}$) is optimal, and the algorithm terminates. Else, choose some $j$ for which $\overline{c}_j < 0$.

**Step III.** Compute $\vec{u} = B^{-1} A_j$. If no component of $\vec{u}$ is (strictly) positive, we have $\theta^* = \infty$, and the optimal cost is $-\infty$ (unbounded LP instance). Terminate the algorithm.

**Step IV.** If some component of $\vec{u}$ is (strictly) positive, set:
$$ \theta^* = \min_{1 \le i \le m,\, u_i > 0} \frac{x_{B(i)}}{u_i} $$

**Step V.** Let $l$ be such that $\frac{x_{B(l)}}{u_l} = \theta^*$. Form a new basis by replacing $A_{B(l)}$ with $A_j$. The new solution is $\vec{y} = \vec{x} - \theta^* \vec{u}$, and the values of the new basic variables are:
$$ y_{B(i)} = x_{B(i)} - \theta^* u_i $$

> [!NOTE] Remark
> Two different basis matrices can correspond to the same b.f.s.
> If $\vec{x}$ is non-degenerate, then it corresponds to a unique basis matrix, since:
> $$ x_{B(i)} > 0 \quad \forall i \in B \implies \vec{x}_B = B^{-1}\vec{b} $$

> [!TIP] Theorem: Termination of Simplex Algorithm
> Assume that the feasible set is non-empty and that every b.f.s. is non-degenerate. Then the simplex algorithm (just described) terminates after finitely many iterations. At termination, either:
> - **(a)** We have an optimal basis $B$ and an associated b.f.s. $\vec{x}$ (termination in Step II of the final iteration).
> - **(b)** The LP is unbounded (termination in Step III of the final iteration).

> [!NOTE] Remark: Cycling
> If the feasible set has degenerate b.f.s., one may return to the same basis — a phenomenon known as **"cycling"**.
>
> **Anti-cycling rules**: The algorithm (so far) does not specify what $j$ to pick in Step II, and what $l$ to pick in Step V.

> [!NOTE] Pivoting Rules: Smallest Subscript Rule
> Choose the smallest subscript $j$ for which $\overline{c}_j < 0$, and the smallest index $l$ for which $x_{B(l)} = \theta^*$. By following this rule, cycling can be avoided.

### Computational Complexity of Each Iteration

**Step II**: Computing reduced costs $\overline{c}_j = c_j - \vec{c}_B^T B^{-1} A_j$ ($j \in N$):
- Finding $B^{-1}$: $O(m^3)$ (Gaussian elimination, solving $AB = I$)
- Computing each reduced cost: $O(m)$ per $j$, so $O(mn)$ total for all $j \in N$

