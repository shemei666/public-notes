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
(2) A vector $x^*$ is called *optimal* or a sol^n to op if it has the smallest objective score among all vectors satisfying the constraints.

**Examples**:
1. Least square optimization
Decision space: $(\beta_0, \beta_1) \in \mathbb{R}^2 \iff y = \beta_0 + \beta_1 x$
$f = \sum_{i=1}^m (Y_i - \beta_0 - \beta_1 Y_i)^2$

2. $\min c^T \vec{x}$
subject to $\vec{a}_i^T \vec{x} \leq b_i$
![[IMG_20260115_223557.jpg]]

3. **Optimal Transport**.
$C: M \times F \to \mathbb{R}_+$
Transport plan, $T: M \to F$
$C(T) = \sum_{m \in M} c(m, T(m))$

4. **Variational analysis** (Brachistochrone problem)
Decision space: space of smooth curves.
Objective: time taken.

5. **Convex Geometry**.
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
**Affine set**: A set $C \subseteq \mathbb{R}^n$ is said to be *affine* if the unique line through two distinct points in $C$ lies in $C$.
![[IMG_20260112_152624.jpg]]

$\vec{x} + \epsilon \vec{y} \quad \vec{x}$ is in the interior
$\vec{y} \in S^{n-1} \quad \vec{y} = \frac{\vec{c}}{\|\vec{c}\|}$
$\vec{c}^T(\vec{x} + \epsilon \vec{y}) = \vec{c}^T \vec{x} + \epsilon \vec{c}^T \vec{y}$

$$
aff(S) = \{ \theta_1 \vec{x}_1 + \dots + \theta_k \vec{x}_k : \vec{x}_1, \dots, \vec{x}_k \in S, \theta_1 + \dots + \theta_k = 1, k \text{ can vary} \}
$$
(set of all affine combinations of vectors in $S$)

**CONVEX SETS**
**Convex set**: A set $C \subseteq \mathbb{R}^n$ is said to be *convex* if the line segment joining any two distinct points in $C$, lies in $C$.
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
Qh: Is the closure of a convex set also convex? (Think about this)
$t x_n \to t x \quad 1-t y_n \to 1-t y$

**Convex hull** of $S \subseteq \mathbb{R}^n$: smallest convex set in $\mathbb{R}^n$ containing $S$.
$conv(S) = \{ \theta_1 \vec{x}_1 + \dots + \theta_k \vec{x}_k : \vec{x}_1, \dots, \vec{x}_k \in S, \theta_1 + \dots + \theta_k = 1, \theta_i \ge 0, k \text{ can vary} \}$
(set of all convex combinations of vectors in $S$)

$\vec{x}_1, \vec{x}_2 \in C_1 \cap C_2 \implies [\theta \vec{x}_1 + (1-\theta) \vec{x}_2] \in C_1 \cap C_2$
![[IMG_20260112_160506.jpg]]

**Cones in $\mathbb{R}^n$**
A set $C \subseteq \mathbb{R}^n$ is said to be a *cone* if for every $\vec{x} \in C$, and $\theta \ge 0$, we have $\theta \vec{x} \in C$.
It is said to be a *convex cone* if it is convex and a cone.
For any $\vec{x}_1, \vec{x}_2 \in C$ and $\theta_1, \theta_2 \ge 0 \implies \theta_1 \vec{x}_1 + \theta_2 \vec{x}_2 \in C$

| Type | Combination | Condition |
| :--- | :--- | :--- |
| Affine | $\theta_1 \vec{x}_1 + \theta_2 \vec{x}_2$ | $\theta_1 + \theta_2 = 1$ |
| Convex | $\theta_1 \vec{x}_1 + \theta_2 \vec{x}_2$ | $\theta_1 + \theta_2 = 1, \theta_1, \theta_2 \ge 0$ |
| Cone | $\theta_1 \vec{x}_1 + \theta_2 \vec{x}_2$ | $\theta_1, \theta_2 \ge 0$ |

$C$ is closed under non-negative linear combinations (conic combination).
*Conic hull* of $S \subseteq \mathbb{R}^n$: smallest convex cone containing $S$.


![[IMG_20260112_161514 1.jpg]]

$$
\begin{bmatrix} a & b \\ c & d \end{bmatrix} \begin{bmatrix} x \\ y \end{bmatrix} = \begin{bmatrix} 1 \\ 0 \end{bmatrix}
$$
$ad-bc \neq 0$
$ax + by = 1$
$cx + dy = 0$

Line in a polyhedron:
$\langle \vec{x}, \vec{v}_i \rangle = 0$

**Polytope**: A bounded polyhedron is said to be a polytope. (Polytope is always compact)
![[IMG_20260112_161522.jpg]]

**Relevance to LP**
$A \vec{x} \le \vec{b}$ "generalized inequalities"

A cone $K \subseteq \mathbb{R}^n$ is called a *proper cone* if:
(1) K is convex
(2) K is closed
(3) K has non-empty interior
(4) K contains no lines (pointed)

A proper cone defines a partial ordering $\le_K$:
$\vec{x} \le_K \vec{y}$ if $\vec{y} - \vec{x} \in K$

Example:
(1) $K = [0, \infty)$ is a proper cone in $\mathbb{R}$ ($\le_K$ is same as $\le$)
(2) $K = [0, \infty)^n$ is a proper cone in $\mathbb{R}^n$
$\vec{x} \le_K \vec{y}$ if $x_i \le y_i \forall 1 \le i \le n$

**Def:** Proper cone $K \subseteq \mathbb{R}^{n}$ is a cone such that,
1. K is convex
2. K has non-empty interior
3. K only has rays from the origin ( no lines)

We have a $\leq_{K}$ partial ordering on $\mathbb{R}^{n}$, by $\vec{x}\leq_{K} \vec{y}$ if $\vec{y} - \vec{x} \in K$
If $\vec{x} \leq_{K} \vec{y}$
1. $\vec{x} + \vec{z} \leq_{K} \vec{y} + \vec{z}$ for all $\vec{z} \in \mathbb{R}^{n}$
2. $\alpha \vec{x} \leq_{K} \alpha \vec{y}$ for all $\alpha \geq 0$

**Goal 2:** To make a computer understand structure of the decision space.

let S be a set in $\mathbb{R}^{r}$
1. **Convex hull** of S is the smallest convex set containing S
2. **Affine hull** of S is the smallest affine set containing S
3. **Convex hull** of S is the smallest convex set containing S
4. **positive hull** of S is the smallest convex cone containing S

Let $C$ be a line-free closed convex set in $\mathbb{R}^{n}$. What is the smallest set S in $\mathbb{R}^{n}$ such that $C$ is the convex hull of S? $conv(S) = C$

## Some examples of convex sets
1. Hyperplanes and half-spaces
    A hyperplane in $\mathbb{R}^{n}$ is a  set of the form, $H_{\vec{a},b}= \{ \vec{x} \in \mathbb{R}^{n} \mid \vec{a}^{T}\vec{x} = b \}$
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
$$ H_{\vec{a},b}^- = \{ \vec{x} \in \mathbb{R}^{n} \mid \vec{a}^T\vec{x} \leq b \} \quad \text{and} \quad H_{\vec{a},b}^+ = \{ \vec{x} \in \mathbb{R}^{n} \mid \vec{a}^T\vec{x} \geq b \} $$
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

**Convex hull** of $S \subseteq \mathbb{R}^n$ smallest convex set in $\mathbb{R}^n$ containing $S$
$conv(S) = \{ \theta_1 \vec{x}_1 + \dots + \theta_k \vec{x}_k \dots \}$

If $\vec{x} \le_K \vec{y}$, then:
(i) $\vec{x} + \vec{z} \le_K \vec{y} + \vec{z}$ for all $\vec{z} \in \mathbb{R}^n$
(ii) $\alpha \vec{x} \le_K \alpha \vec{y}, \forall \alpha \ge 0$
(iii) $\vec{x}_j \le_K \vec{y}_j \forall j \in \mathbb{N}$ and $\vec{x}_j \to \vec{x}, \vec{y}_j \to \vec{y}$ then $\vec{x} \le_K \vec{y}$ (proper cones $\to$ generalized inequalities involving vectors)

![[IMG_20260115_130759.jpg]]

**Relevance to LP**
If the decision space is a polytope, existence of a (max) minimum of the objective function is guaranteed.
$\min f_0(x)$ subject to ...

**Def**: $S \subseteq \mathbb{R}^n$. $cl(S)$ closure, $int(S)$ interior, $bd(S)$ boundary.
The sets $relint(S)$, $relbd(S)$ are the *relative interior* and *relative boundary*, with respect to the *affine hull* of $S$.
* every convex set has non-empty relative interior.