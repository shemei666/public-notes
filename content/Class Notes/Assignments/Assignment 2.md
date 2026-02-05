# Assignment 2 - BMATH 3

**28. Compute each of the following derivatives:**
(a) $\frac{\partial}{\partial z}(4\bar{z}^2 - z^3)$
(c) $\frac{\partial^3}{\partial x^2 \partial y}(3z^2\bar{z}^4 - 2z^3\bar{z} + z^4 - \bar{z}^5)$
(d) $\frac{\partial^5}{\partial\bar{z}^3\partial z^2}(\bar{z}^2 - z\bar{z} + 4z - 6z^2)$

**30. Let $f : \mathbb{C} \to \mathbb{C}$ be a polynomial. Suppose further that**
$\frac{\partial f}{\partial z} = 0 \quad \text{and} \quad \frac{\partial f}{\partial \bar{z}} = 0$
for all $z \in \mathbb{C}$. Prove that $f \equiv \text{constant}$.

**31. Let $F : \mathbb{C} \to \mathbb{C}$ be a polynomial. Suppose that**
$\frac{\partial^2}{\partial z^2} F = 0$
for all $z \in \mathbb{C}$. Prove that $F(z, \bar{z}) = z \cdot G(\bar{z}) + H(\bar{z})$ for some polynomials $G, H$ in $\bar{z}$ (i.e., they depend only on $\bar{z}$).

**32. Suppose that $F : \mathbb{C} \to \mathbb{C}$ is a polynomial. Suppose further that**
$\frac{\partial}{\partial \bar{z}} F^2 = 0$. What can you say about $F$?

**42. If $f$ and $\bar{f}$ are both holomorphic on a connected open set $U \subseteq \mathbb{C}$, then prove that $f$ is identically constant.**

**43. Prove that if $f$ is holomorphic on $U \subseteq \mathbb{C}$, then**
$\Delta(|f|^2) = 4 \left| \frac{\partial f}{\partial z} \right|^2$.

**46. Let $u$ be a $C^2$, real-valued harmonic function on an open set $U \subseteq \mathbb{C}$. Prove that $h(z) = \partial u/\partial y + i\partial u/\partial x$ is holomorphic on $U$.**

**49. Let $f$ and $g$ be $C^1$ functions and assume that $f \circ g$ is defined. Prove the following version(s) of the chain rule: With $w = g(z)$**
$$
\frac{\partial}{\partial z}(f \circ g) = \frac{\partial f}{\partial w} \cdot \frac{\partial g}{\partial z} + \frac{\partial f}{\partial \bar{w}} \cdot \frac{\partial \bar{g}}{\partial z}
$$
$$
\frac{\partial}{\partial \bar{z}}(f \circ g) = \frac{\partial f}{\partial w} \cdot \frac{\partial g}{\partial \bar{z}} + \frac{\partial f}{\partial \bar{w}} \cdot \frac{\partial \bar{g}}{\partial \bar{z}}
$$
How do these formulas simplify if (i) $f$ and $g$ are both holomorphic, (ii) only $f$ is holomorphic, (iii) only $g$ is holomorphic, (iv) $\bar{f}$ and $\bar{g}$ are both holomorphic? [Suggestion: Write everything out in real and imaginary parts and use the real variable chain rule from calculus.]

**50. Let $F$ be holomorphic on a connected open set $U \subseteq \mathbb{C}$. Suppose that $G_1, G_2$ are holomorphic on $U$ and that**
$\frac{\partial G_1}{\partial z} = F = \frac{\partial G_2}{\partial z}$. Prove that $G_1 - G_2 \equiv$ constant.

**56. Let $U_1 \subseteq U_2 \subseteq U_3 \subseteq \dots \subseteq \mathbb{C}$ be connected open sets and define $U = \bigcup_{j=1}^{\infty} U_j$.**
Let $f$ be a holomorphic function on $U$. Suppose that, for each $j$, $f|_{U_j}$ has a holomorphic antiderivative on $U_j$. Prove then that $f$ has a holomorphic antiderivative on all of $U$.
