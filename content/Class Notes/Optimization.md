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
>  \langle P_{K}(\vec{x}) - \vec{y}, P_{K}(\vec{y}) - P_{K}(\vec{x}) \rangle \le 0 \text{)}
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
> $$ \lVert P_{K}(\vec{x}) - P_{K}(\vec{y}) \rVert^2 \le \lVert \vec{x} - \vec{y} \rVert \lVert P_{K}(\vec{x}) - P_{K}(\vec{y}) \rVert $$
> If $P_{K}(\vec{x}) \neq P_{K}(\vec{y})$, dividing gives:
> $$ \lVert P_{K}(\vec{x}) - P_{K}(\vec{y}) \rVert \le \lVert \vec{x} - \vec{y} \rVert $$

### Projection of Sphere

> [!TIP] Lemma
> Let $S$ be a sphere containing $K$ in its interior. Then $P_{K}(S) = \partial K$.

> [!NOTE]- Proof of Lemma
> $P(S) \subseteq \partial K$, Let $\vec{v} \in \partial K$, for $n \in \mathbb{N}$, choose $x_{n} \in Int(S)\setminus K$ such that $\lVert  \vec{x_{n}} - \vec{v} \rVert < \frac{1}{n}$, $\lVert  \vec{v} - P(x_{n}) \rVert \leq \lVert  \vec{v} - \vec{x_{n}} \rVert \leq \frac{1}{n}$ , $R_{K}(\vec{x_{n}})$ intersects $S$ at a point $\vec{y_{n}}$
> 

Also since $S$ is a compact set we have that $\vec{y_{n}}$ has a convergent subsequence, let $y_{n_{k}}\to y$ be the convergent subsequence. Also see that the projection of any point in the ray $R_{K}(x_{n})$ will have the same image under the projection. Hence $P_{K}(y_{n_{k}})\to $



> [!TIP] Corollary
> Let $K$ be a nonempty closed convex proper subset of $\mathbb{R}^{n}$. Then $P_{K}(\mathbb{R}^{n} \setminus K) = \partial K$.

> [!c] Exercise
> Prove that $\phi(t) = \lVert \vec{x} - ((1-t)P_{K}(\vec{x}) + t\vec{z}) \rVert$ for $\vec{z} \in K$ is a strictly increasing function on $[0,1]$.

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

> [!TODO] Proof
> Prove the surjectivity of the normal map for bounded convex sets.

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

