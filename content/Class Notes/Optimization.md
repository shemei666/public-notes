---
publish: true
---

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
\text{non-zero lienar functionals } \longleftrightarrow  \text{(n-1)-dimensional subspace of $\mathbb{R}^{n}$}
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
> **Argument:** Let $\vec{x}_{0} \in H_{\vec{a},b}$. Consider points of the form $\vec{x} = \vec{x}_{0} + \epsilon \vec{a}$.
> $\vec{a}^{T}(\vec{x}_{0} + \epsilon \vec{a}) = \vec{a}^{T}\vec{x}_{0} + \epsilon \lVert \vec{a} \rVert^{2} = b + \epsilon \lVert \vec{a} \rVert^{2}$.
> For $\epsilon > 0$, $\vec{a}^{T}\vec{x} > b$ (strictly outside $H_{\vec{a},b}^{-}$).
> For $\epsilon < 0$, $\vec{a}^{T}\vec{x} < b$ (strictly inside $H_{\vec{a},b}^{-}$).
> Thus, any neighborhood of $\vec{x}_{0}$ contains points in $H_{\vec{a},b}^{-}$ and points in its complement.  
