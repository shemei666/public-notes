---
publish: true
---

![[IMG_20260115_223542.jpg]]

(1) decision space $X$
(2) Objective function ($f$) on $X$

**Optimization problem**:

1. minimize $f$ on $X$
2. Find $\arg \min_{x \in X} f(x)$

(1) minimize $f_0(x)$
$f_i(x) \leq b_i \quad x = (x_1, \dots, x_n)$
$f_0: \mathbb{R}^n \to \mathbb{R}, \quad f_i: \mathbb{R}^n \to \mathbb{R}$
(2) A vector $x^*$ is called _optimal_ or a sol^n to op if it has the smallest objective score among all vectors satisfying the constraints.

**Examples**:

1. **Least Square Optimization**:
   Fitting a linear model $y = \beta_0 + \beta_1 x$ to a set of data points $(x_i, Y_i)$.
   - **Decision Space**: $(\beta_0, \beta_1) \in \mathbb{R}^2$ represents the parameters of the line.
   - **Objective Function**: Minimize the sum of squared errors:
     $$
     f(\beta_0, \beta_1) = \sum_{i=1}^m (Y_i - \beta_0 - \beta_1 x_i)^2
     $$

2. **Linear Programming (LP)**:
   Optimizing a linear objective function subject to linear equality and inequality constraints.
   $$ \min\_{\vec{x}} c^T \vec{x} $$
   Subject to: $\vec{a}_i^T \vec{x} \leq b_i$ for $i=1,\dots,k$ (polyhedral constraints).

   ![[IMG_20260115_223557.jpg]]

3. **Optimal Transport**:
   Finding the most efficient way to transport mass from one distribution to another.
   - **Cost Function**: $c: M \times F \to \mathbb{R}_+$ (cost to move unit mass from $m \in M$ to $f \in F$).
   - **Transport Plan**: $T: M \to F$ (map indicating destination for each source point).
   - **Objective**: Minimize total transport cost $C(T) = \sum_{m \in M} c(m, T(m))$.

4. **Variational Analysis (Brachistochrone Problem)**:
   Finding the path between two points that a particle would slide down in the shortest time under gravity.
   - **Decision Space**: Space of smooth curves connecting points A and B.
   - **Objective**: Minimize the time taken for descent.

![[IMG_20260112_142612.jpg]]

$\min f_0(x_1, \dots, x_n)$
$c_1 x_1 + \dots + c_n x_n \quad (c_1, \dots, c_n \to \text{cost associated with the variable})$
subject to

$$
\begin{pmatrix} a_{11} x_1 + \dots + a_{1n} x_n \leq b_1 \\ \vdots \\ a_{m1} x_1 + \dots + a_{mn} x_n \leq b_m \end{pmatrix}
$$

LPP Linear programming program.
$C_n, \quad \{a_{ij}\}_{\substack{1 \le i \le m \\ 1 \le j \le n}}, \quad b_1, \dots, b_m$

**GOAL**: Understand the geometry of the decision space.
Affine set, convex sets, convex cones $\subseteq \mathbb{R}^n$
**Affine set**: A set $C \subseteq \mathbb{R}^n$ is said to be _affine_ if the unique line through two distinct points in $C$ lies in $C$.
![[IMG_20260112_152624.jpg]]

$\vec{x} + \epsilon \vec{y} \quad \vec{x}$ is in the interior
$\vec{y} \in S^{n-1} \quad \vec{y} = \frac{\vec{c}}{\|\vec{c}\|}$
$\vec{c}^T(\vec{x} + \epsilon \vec{y}) = \vec{c}^T \vec{x} + \epsilon \vec{c}^T \vec{y}$

$$
aff(S) = \{ \theta_1 \vec{x}_1 + \dots + \theta_k \vec{x}_k : \vec{x}_1, \dots, \vec{x}_k \in S, \theta_1 + \dots + \theta_k = 1, k \text{ can vary} \}
$$

(set of all affine combinations of vectors in $S$)

**CONVEX SETS**
**Convex set**: A set $C \subseteq \mathbb{R}^n$ is said to be _convex_ if the line segment joining any two distinct points in $C$, lies in $C$.
Equivalently, if $\vec{x}_1, \vec{x}_2 \in C$, then $\theta \vec{x}_1 + (1-\theta) \vec{x}_2 \in C$ for $\theta \in [0, 1]$.
(or $\theta_1 \vec{x}_1 + \theta_2 \vec{x}_2 \in C$ for $\theta_1, \theta_2 \ge 0, \theta_1 + \theta_2 = 1$)
![[IMG_20260112_154714.jpg]]

$a_{11} x_1 + \dots + a_{1n} x_n \leq b_1, \quad a_{11} y_1 + \dots + a_{1n} y_n \leq b_1$
$a_{1\cdot}(\theta x_1 + (1-\theta) y_1) + \dots + a_{1n} (\theta x_n + (1-\theta) y_n)$
$\theta \vec{x} + (1-\theta) \vec{y} \le \theta b_1 + (1-\theta) b_1 = b_1 \quad (\text{since } \theta \ge 0)$

"Question about the converse:
Is every convex subset of $\mathbb{R}^n$ given by a collection of linear inequalities?
Yes, as long as you allow collection being infinite."
![[IMG_20260112_155516.jpg]]

every convex function is a supremum of linear function
Qh: Is the closure of a convex set also convex?
$t x_n \to t x \quad 1-t y_n \to 1-t y$

**Convex hull** of $S \subseteq \mathbb{R}^n$: smallest convex set in $\mathbb{R}^n$ containing $S$.
$conv(S) = \{ \theta_1 \vec{x}_1 + \dots + \theta_k \vec{x}_k : \vec{x}_1, \dots, \vec{x}_k \in S, \theta_1 + \dots + \theta_k = 1, \theta_i \ge 0, k \text{ can vary} \}$
(set of all convex combinations of vectors in $S$)

$\vec{x}_1, \vec{x}_2 \in C_1 \cap C_2 \implies [\theta \vec{x}_1 + (1-\theta) \vec{x}_2] \in C_1 \cap C_2$
![[IMG_20260112_160506.jpg]]

**Cones in $\mathbb{R}^n$**
A set $C \subseteq \mathbb{R}^n$ is said to be a _cone_ if for every $\vec{x} \in C$, and $\theta \ge 0$, we have $\theta \vec{x} \in C$.
It is said to be a _convex cone_ if it is convex and a cone.
For any $\vec{x}_1, \vec{x}_2 \in C$ and $\theta_1, \theta_2 \ge 0 \implies \theta_1 \vec{x}_1 + \theta_2 \vec{x}_2 \in C$

| Type   | Combination                               | Condition                                           |
| :----- | :---------------------------------------- | :-------------------------------------------------- |
| Affine | $\theta_1 \vec{x}_1 + \theta_2 \vec{x}_2$ | $\theta_1 + \theta_2 = 1$                           |
| Convex | $\theta_1 \vec{x}_1 + \theta_2 \vec{x}_2$ | $\theta_1 + \theta_2 = 1, \theta_1, \theta_2 \ge 0$ |
| Cone   | $\theta_1 \vec{x}_1 + \theta_2 \vec{x}_2$ | $\theta_1, \theta_2 \ge 0$                          |

$C$ is closed under non-negative linear combinations (conic combination).
_Conic hull_ of $S \subseteq \mathbb{R}^n$: smallest convex cone containing $S$.

![[IMG_20260112_161514 1.jpg]]

![[IMG_20260112_161522.jpg]]
**Convex hull** of $S \subseteq \mathbb{R}^n$ smallest convex set in $\mathbb{R}^n$ containing $S$
$conv(S) = \{ \theta_1 \vec{x}_1 + \dots + \theta_k \vec{x}_k \dots \}$

**Def:** Proper cone $K \subseteq \mathbb{R}^{n}$ is a cone such that,

1. K is convex
2. K has non-empty interior
3. K only has rays from the origin ( no lines)

We have a $\leq_{K}$ partial ordering on $\mathbb{R}^{n}$, by $\vec{x}\leq_{K} \vec{y}$ if $\vec{y} - \vec{x} \in K$
If $\vec{x} \leq_{K} \vec{y}$

1. $\vec{x} + \vec{z} \leq_{K} \vec{y} + \vec{z}$ for all $\vec{z} \in \mathbb{R}^{n}$
2. $\alpha \vec{x} \leq_{K} \alpha \vec{y}$ for all $\alpha \geq 0$

Example:
(1) $K = [0, \infty)$ is a proper cone in $\mathbb{R}$ ($\le_K$ is same as $\le$)
(2) $K = [0, \infty)^n$ is a proper cone in $\mathbb{R}^n$
$\vec{x} \le_K \vec{y}$ if $x_i \le y_i \forall 1 \le i \le n$

If $\vec{x} \le_K \vec{y}$, then:
(i) $\vec{x} + \vec{z} \le_K \vec{y} + \vec{z}$ for all $\vec{z} \in \mathbb{R}^n$
(ii) $\alpha \vec{x} \le_K \alpha \vec{y}, \forall \alpha \ge 0$
(iii) $\vec{x}_j \le_K \vec{y}_j \forall j \in \mathbb{N}$ and $\vec{x}_j \to \vec{x}, \vec{y}_j \to \vec{y}$ then $\vec{x} \le_K \vec{y}$ (proper cones $\to$ generalized inequalities involving vectors)

**Relevance to LP**
$A \vec{x} \le \vec{b}$ "generalized inequalities"
**Goal 2:** To make a computer understand structure of the decision space.

let S be a set in $\mathbb{R}^{r}$

1. **Convex hull** of S is the smallest convex set containing S
2. **Affine hull** of S is the smallest affine set containing S
3. **Convex hull** of S is the smallest convex set containing S
4. **positive hull** of S is the smallest convex cone containing S

Let $C$ be a line-free closed convex set in $\mathbb{R}^{n}$. What is the smallest set S in $\mathbb{R}^{n}$ such that $C$ is the convex hull of S? $conv(S) = C$

## Some examples of convex sets

1. Hyperplanes and half-spaces
   A hyperplane in $\mathbb{R}^{n}$ is a set of the form, $H_{\vec{a},b}= \{ \vec{x} \in \mathbb{R}^{n} \mid \vec{a}^{T}\vec{x} = b \}$
   > [!Riesz representation theorem:]-
   > Every linear function on $\mathbb{R}^{n}$ is of the form $\vec{x} \mapsto \langle \vec{a}, \vec{x} \rangle$ for some $\vec{a} \in \mathbb{R}^{n}$
   > **Proof:** Let $f: \mathbb{R}^n \to \mathbb{R}$ be a linear function. Let $\{\vec{e}_1, \dots, \vec{e}_n\}$ be the standard basis for $\mathbb{R}^n$. Any $\vec{x} \in \mathbb{R}^n$ can be written as $\vec{x} = \sum_{i=1}^n x_i \vec{e}_i$. By linearity:
   > $$f(\vec{x}) = f\left(\sum_{i=1}^n x_i \vec{e}_i\right) = \sum_{i=1}^n x_i f(\vec{e}_i)$$
   > Let $a_i = f(\vec{e}_i)$ and $\vec{a} = (a_1, \dots, a_n)^T$. Then:
   > $$f(\vec{x}) = \sum_{i=1}^n x_i a_i = \langle \vec{a}, \vec{x} \rangle$$

$$
\text{non-zero lienar functionals } \longleftrightarrow  \text{$(n-1)$-dimensional subspace of $\mathbb{R}^{n}$}
$$

$$ \rho \longleftrightarrow \ker \rho$$
**Exercise:** Let $P_{1},P_{2}$ be linear functionals on $\mathbb{R}^{n}$ such that $\ker P_{1} = \ker P_{2}$. Prove that $P_{1} = \alpha P_{2}, \alpha \in \mathbb{R}$

Geometrically, $H_{\vec{a},b}$ has normal vector $\vec{a}$, with offset $b$ from origin
For $\alpha \in \mathbb{R}, H_{\alpha \vec{a} ,\alpha b} = H_{\vec{a},b}$ , So we assume $\lvert \vec{a} \rvert =1$

## Half-spaces

A closed half space in $\mathbb{R}^{n}$ is a set of the form $H_{\vec{a},b}:= \{  \vec{x} \in \mathbb{R}^{n} \mid \vec{a}^{T}\vec{x} \leq b \}$
We denote the typical lower and upper closed half-spaces as:
$$ H*{\vec{a},b}^- = \{ \vec{x} \in \mathbb{R}^{n} \mid \vec{a}^T\vec{x} \leq b \} \quad \text{and} \quad H*{\vec{a},b}^+ = \{ \vec{x} \in \mathbb{R}^{n} \mid \vec{a}^T\vec{x} \geq b \} $$

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

The normal vector $\vec{a}$ points in the direction of increasing values of the linear functional $f(\vec{x}) = \vec{a}^T\vec{x}$. Therefore, the half-space defined by $\vec{a}^T\vec{x} \leq b$ is the region extending in the direction opposite to $\vec{a}$ from the boundary hyperplane.

$$
\begin{align}
\vec{a}^{T}\vec{x_{0}} = b \\
\vec{a}^{T} (\vec{x} - \vec{x_{0}}) = 0 \\
\implies  \vec{a}^{T}\vec{x} \leq b = \vec{a}^{T}\vec{x_{0}} \iff  \vec{a}^{T} (\vec{x} - \vec{x_{0}}) \leq 0
\end{align}
$$

- Hyperplane are affine set
- Half-spaces are convex but not affine. Intersection of closed half-spaces are either empty of convex.

The boundary of $H_{\vec{a} ,b}^{+},H_{\vec{a},b}^{-}$ is $H_{\vec{a},b}$  
Let $\vec{x}_{0} \in H_{\vec{a},b}$. Consider points of the form $\vec{x} = \vec{x}_{0} + \epsilon \vec{a}$.
$\vec{a}^{T}(\vec{x}_{0} + \epsilon \vec{a}) = \vec{a}^{T}\vec{x}_{0} + \epsilon \lVert \vec{a} \rVert^{2} = b + \epsilon \lVert \vec{a} \rVert^{2}$.
For $\epsilon > 0$, $\vec{a}^{T}\vec{x} > b$ (strictly outside $H_{\vec{a},b}^{-}$).
For $\epsilon < 0$, $\vec{a}^{T}\vec{x} < b$ (strictly inside $H_{\vec{a},b}^{-}$).
Thus, any neighborhood of $\vec{x}_{0}$ contains points in $H_{\vec{a},b}^{-}$ and points in its complement.

## Polyhedron

A polyhedron is a solution set of a finite number of linear equalities and inequalities.

$$
\begin{align}
\mathcal{P} := \{ \vec{x} \in \mathbb{R}^{n} \mid \vec{a}_{i}^{T}\vec{x} \leq b_{i}, i = 1,\dots,m, \quad \vec{c}_{j}^{T}\vec{x} = d_{j}, j = 1,\dots,p \}
\end{align}
$$

- A polyhedron is the intersection of a finite number of half-spaces and hyperplanes.
- Affine sets, rays, line segments, half-spaces, hyperplanes are all polyhedra.

![[Assets/IMG_20260115_124838.jpg]]
**Why are points and lines polyhedra?**

1. **Point**: A single point $\{P\}$ in $\mathbb{R}^n$ is a polyhedron.
   Example in $\mathbb{R}^2$: The intersection of two non-parallel lines defines a unique point.

   $$
   \begin{bmatrix} a & b \\ c & d \end{bmatrix} \begin{bmatrix} x \\ y \end{bmatrix} = \begin{bmatrix} 1 \\ 0 \end{bmatrix}
   $$

   With $ad-bc \neq 0$, the solution is unique. Thus, a point is defined by a finite number of linear equalities (hyperplanes).

2. **Line**: A line is an affine set. As every affine set is an intersection of hyperplanes, it is a polyhedron.
   A line in $\mathbb{R}^n$ can be defined as the intersection of $n-1$ independent hyperplanes:
   $$ \langle \vec{x}, \vec{v}\_i \rangle = c_i, \quad i=1,\dots,n-1 $$

**Polytope**: A bounded polyhedron is said to be a polytope. (Polytope is always compact)

![[IMG_20260115_130759.jpg]]

**Relevance to LP**
If the decision space is a polytope, existence of a (max) minimum of the objective function is guaranteed.
$\min f_0(x)$ subject to ...

**Def**: $S \subseteq \mathbb{R}^n$. $cl(S)$ closure, $int(S)$ interior, $bd(S)$ boundary.
The sets $relint(S)$, $relbd(S)$ are the _relative interior_ and _relative boundary_, with respect to the _affine hull_ of $S$.

- every convex set has non-empty relative interior.

**Def:** Let $S \subseteq \mathbb{R}^{n}$ and $H_{\vec{a},b} \subseteq \mathbb{R}^{n}$ be a hyperplane, and let $H_{\vec{a},b}^{-},H_{\vec{a},b}^{+}$, be the half-spaces bounded by $H_{\vec{a},b}$. We say that $H$ supports $S$ at at $\vec{x} \in \mathbb{R}^{n}$ if $\vec{x} \in S \cap H$ and either $S\subseteq H_{\vec{a},b}^{+}$ or $S\subseteq H_{\vec{a},b}^{-}$.

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
    % Endpoints calculated manually to implicitly use tangent direction
    % P1 = (3.39, 0.32), P2 = (-1.39, 1.76)
    \draw[thick, red!80!black] (3.39, 0.32) -- (-1.39, 1.76) node[midway, above right, black] {$H_{\vec{a},b}$};

    % Draw Normal Vector a
    % End point = (1.29, 2.00)
    \draw[->, ultra thick, red!70!black] (X) -- (1.29, 2.00) node[right] {$\vec{a}$};

    % Label Half-spaces
    \node[red!80!black] at (1.43, 2.47) {$H_{\vec{a},b}^+$};
    \node[blue!80!black] at (0.57, -0.40) {$H_{\vec{a},b}^-$};
\end{tikzpicture}
\end{document}
```

If $H_{\vec{a},b}$ supports S and $S\subseteq H_{\vec{a},b}^{-}$ then $H_{\vec{a},b}^{-}$ is called a **supporting half-space** for $S$ at $\vec{x}$ and $\vec{a}$ is called an **outer normal vector**

Not every point on the boundary of a closed set $S$ has to have a supporting hyperplane.

```tikz
\begin{document}
\begin{tikzpicture}[>=stealth, scale=1.3]
    % Non-convex set S (Heart/Kidney shape)
    % Start at bottom (1,0)
    % Left side
    \filldraw[fill=blue!10, draw=blue!80!black, thick]
        (1,0)
        .. controls (0,0) and (-0.5, 1.5) .. (0, 2)
        .. controls (0.5, 2.5) and (1, 1.5) .. (1, 1) % The Dent at (1,1)
        .. controls (1, 1.5) and (1.5, 2.5) .. (2, 2)
        .. controls (2.5, 1.5) and (2, 0) .. (1, 0);

    \node[blue!80!black] at (1, 0.5) {$S$};

    % The point x at the dent
    \coordinate (X) at (1, 1);
    \fill[black] (X) circle (1.5pt) node[below=3pt] {$\vec{x}$};

    % Draw a candidate "tangent" line that cuts through the set
    % Horizontal line y=1
    \draw[thick, dashed, red!80!black] (-0.5, 1) -- (2.5, 1);
    \node[red!80!black, font=\small] at (2.5, 1.2) {Intersects $S$};

    % Draw another candidate line (diagonal)
    \draw[thin, dotted, red!80!black] (0.5, 0.5) -- (1.5, 1.5);

    \node[black, font=\small, align=center] at (1, -0.5) {No single hyperplane can\\contain $S$ entirely on one side};

\end{tikzpicture}
\end{document}
```

**Exercise:** For smooth Jordan curve there can be at most one supporting hyperplane at a point

## Two main representation theorems

For non-empty closed convex sets on $\mathbb{R}^{n}$.

**Theorem:** Each nonempty closed convex set in $\mathbb{R}^{n}$ is the intersection of its supporting half-spaces ( hence given by a collection of linear inequalities).

**Theorem:** (**Extremal representation**)Each nonempty closed convex set $C \subseteq \mathbb{R}^n$ is of the form $C = C_{lf} \oplus V$, where $V$ is a linear subspace of $\mathbb{R}^n$ and $C_{lf}$ is a line-free closed convex set in a subspace complementary to $V$ (linear part + line-free part).

```tikz
\begin{document}
\begin{tikzpicture}[>=stealth, scale=1]
    % Draw V (Linear Subspace) - Vertical Axis
    \draw[->, ultra thick, blue] (0, -2.5) -- (0, 2.5) node[above] {$V$ (Subspace)};

    % Draw C_lf (Line-free part) - A horizontal disk/ellipse
    % We visually place it at "z=0"
    \filldraw[fill=green!20, draw=green!60!black, thick] (0,0) ellipse (1.5 and 0.4);

    % Annotation for C_lf
    \draw[->, thin, green!40!black] (2.0, 0) node[right] {$C_{lf}$ (Line-free part)} -- (1.55, 0);

    % Draw the full set C (Cylinder) = C_lf + V
    % Top and bottom ellipses (dashed/faded to imply infinity)
    \draw[gray, dashed] (0, 2) ellipse (1.5 and 0.4);
    \draw[gray, dashed] (0, -2) ellipse (1.5 and 0.4);

    % Vertical sides
    \draw[gray, thick] (-1.5, -2) -- (-1.5, 2);
    \draw[gray, thick] (1.5, -2) -- (1.5, 2);

    % Shading for the cylinder (set C)
    % Only shading the 'front' part partially to keep V visible or using opacity
    \shade[left color=blue!10, right color=blue!5, opacity=0.3] (-1.5, -2) rectangle (1.5, 2);

    % Annotation for C
    \node[blue!80!black] at (-2.2, 1.5) {$C = C_{lf} \oplus V$};
    \node[font=\footnotesize, align=center, blue!80!black] at (-2.2, 1.0) {(Infinite Cylinder)};

    % Decomposition Vector Visualization
    % c in C_lf, v in V
    \coordinate (O) at (0,0);
    \coordinate (c) at (1.2, -0.2); % point in base
    \coordinate (v) at (0, 1.5);    % vector in V
    \coordinate (sum) at (1.2, 1.3); % c + v

    \draw[->, red, thick] (O) -- (c) node[midway, below] {$c \in C_{lf}$};
    \draw[->, blue, thick] (c) -- (sum) node[midway, right] {$v \in V$};
    \fill[purple] (sum) circle (1.5pt) node[above right] {$x = c + v$};

\end{tikzpicture}
\end{document}
```

and each nonempty line free closed convex set $C \subseteq \mathbb{R}^{n}$ is the convex hull of its extreme points and extreme rays.

**Def:** $C$ nonempty closed convex set $\vec{v} \in C$ is said to be an extreme point for $C$ if $\frac{\vec{x} + \vec{y}}{2} = \vec{v}$ for $\vec{x},\vec{y} \in C$ then $\vec{x} = \vec{y} = \vec{v}$

**Exercise:** Prove that $C \subseteq  \mathbb{R}^{n}$ _closed_ set with the properties whenever $\vec{x},\vec{y} \in C$ $\vec{x}+ \vec{y} /2 \in C$, is a convex set.

**Corollary:(Minkowski's Theorem)** Each nonempty compact convex set $K\subseteq \mathbb{R}^{n}$ is the convex hull of its extreme points.

**Lemma:** $K$ nonempty closed convex set, for each $\vec{x} \in \mathbb{R}^{n}$, there is a unique point $P_{K}(\vec{x})$ ($P_{K}:\mathbb{R}^{n}\to K$) satisfying

$$
\lvert  \vec{x} -P_{k} (\vec{x})\rvert  \leq \lvert  \vec{x} - y \vec{} \rvert  \quad \forall \vec{y} \in K
$$

(unique closest point in $K$ from $\vec{x}$)

**Proof:** For any closed set $S$ in $\mathbb{R}^{n}$ for every $\vec{x} \in \mathbb{R}^{n}$ there is a point $P_{S}(\vec{x}) \in S$ such that $\lvert \vec{x} - P_{S}(\vec{x}) \rvert = d(\vec{x},S)$.
For uniqueness if we have 2 distinct points $\vec{y}_{1},\vec{y}_{2} \in K$ with same distance $d = d(\vec{x},K)$ from $\vec{x}$,  
$$
 \frac{\vec{y_{1}}  + \vec{y_{2}}}{2} - \vec{x}+ \vec{y_{1}} - \frac{\vec{y_{1}}  + \vec{y_{2}}}{2}
$$

**Def:** The mapping $P_{k}: \mathbb{R}^{n} \to K$ is called the metric projection or nearest point map of $K$, ($d(\vec{x},K) = \lvert  \vec{x} - P_{K}(\vec{x}) \rvert$) For $\vec{x} \in \mathbb{R}^{n} \setminus K$, $u(K,\vec{x}):= \frac{\vec{x} - P_{K}(\vec{x})}{d(K,\vec{x})}$. 

$P_{K}|_{\mathbb{R}^{n}\setminus K}$, what is the image? $\partial K$?
$$
R(K,\vec{x}) := \langle P_{K}(\vec{x}) + \lambda u(K,\vec{x}) \rangle \quad \lambda \geq 0
$$
ray through $\vec{x}$ with endpoint  $P_{K}(\vec{x})$

**Theorem:** $P_{k}$ is a contractive mapping
$$
\lvert  P_{K}(\vec{x}) - P_{K}(\vec{y})\rvert  \leq \lvert \vec{x} - y \vec{} \rvert  \quad \forall \vec{x}, \vec{y} \in \mathbb{R}^{n}
$$


**Proof:**


