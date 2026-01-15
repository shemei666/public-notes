
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
