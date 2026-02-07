---
publish: true
tags: [math, algebraic-geometry, notes]
---
# Undergraduate Algebraic Geometry

Based on the notes by Miles Reid.

## Chapter 1: Plane Conics

### 1.1 Parametrized Curves

> [!EXAMPLE] The Unit Circle
> Consider the circle $C: \{x^2 + y^2 = 1\} \subset \mathbb{R}^2$.
> We can parametrize it using the slope $\lambda$ of a line through the point $(0,1)$.
> Setting $y-1 = \lambda x$, we find intersection points:
> $$ x^2 + (\lambda x + 1)^2 = 1 \implies x^2 (1+\lambda^2) + 2\lambda x = 0 $$
> The roots are $x=0$ (the point $P$) and:
> $$ x = \frac{-2\lambda}{1+\lambda^2}, \quad y = \frac{1-\lambda^2}{1+\lambda^2} $$
> **Inverse map**: $\lambda = \frac{x}{1-y}$.

### 1.2 A Conic with No Rational Points

> [!TIP] Proposition
> The conic $C: \{2x^2 + y^2 = 5z^2\}$ has no rational points except $(0,0,0)$.

> [!NOTE]- Proof
> Suppose there is a rational solution. We can scale to coprime integers $(x,y,z)$.
> Considering modulo 5:
> $$ 2x^2 + y^2 \equiv 0 \pmod 5 $$
> Since 2 is not a quadratic residue modulo 5, we must have $x \equiv 0$ and $y \equiv 0 \pmod 5$.
> Then $x=5x', y=5y'$. Substituting back:
> $$ 2(25x'^2) + 25y'^2 = 5z^2 \implies 10x'^2 + 5y'^2 = z^2 $$
> This implies $z^2$ is divisible by 5, so $z$ is divisible by 5.
> Thus $x, y, z$ are all divisible by 5, contradicting the assumption that they are coprime.
> Therefore, no non-trivial integer (and hence rational) solutions exist.

### 1.3 Conics in $\mathbb{R}^2$

The general quadratic equation is:
$$ q(x, y) = ax^2 + bxy + cy^2 + dx + ey + f = 0 $$

> [!INFO] Definition: Types of Conics
> 1. **Nondegenerate**: Ellipse, Parabola, Hyperbola.
> 2. **Degenerate**: Pair of lines (intersecting or parallel), single line, point, or empty set.

### 1.4 The Projective Plane $\mathbb{P}^2$

> [!INFO] Definition: Projective Plane
> $\mathbb{P}^2_{\mathbb{R}}$ is the set of lines in $\mathbb{R}^3$ passing through the origin.
> A point is represented by homogeneous coordinates $(X:Y:Z)$, not all zero.
> $$ (X:Y:Z) \sim (\lambda X : \lambda Y : \lambda Z) \quad \text{for } \lambda \neq 0 $$

> [!TIP] Theorem
> Every nondegenerate conic in $\mathbb{P}^2$ is isomorphic to $\mathbb{P}^1$.

> [!TIP] Theorem: Unique Conic
> There is a unique conic passing through any 5 points in $\mathbb{P}^2$, provided no 4 are collinear.

## Chapter 2: Cubics and the Group Law

### 2.1 Examples of Cubics

> [!EXAMPLE] Nodal Cubic
> Equation: $y^2 = x^3 + x^2$.
> Singularity: Node at $(0,0)$.
> Parametrization: $t = y/x \implies x = t^2-1, y = t(t^2-1)$.

> [!EXAMPLE] Cuspidal Cubic
> Equation: $y^2 = x^3$.
> Singularity: Cusp at $(0,0)$.
> Parametrization: $x = t^2, y = t^3$.

### 2.2 Non-parametrization of Elliptic Curves

> [!TIP] Theorem
> The smooth cubic curve $y^2 = x(x-1)(x-\lambda)$ for $\lambda \neq 0,1$ cannot be parametrized by rational functions.

### 2.8 Group Law

> [!INFO] Definition: Group Law
> For a smooth cubic curve $C \subset \mathbb{P}^2$, we can define an abelian group structure.
> **Rule**: $P + Q + R = 0$ if and only if $P, Q, R$ are collinear.
> **Identity**: Usually an inflection point $\mathcal{O}$.

> [!TIP] Theorem: Associativity
> The group law is associative: $(P+Q)+R = P+(Q+R)$.
> **Proof Idea**: Follows from the **Cayley-Bacharach Theorem**, which states that if two cubics intersect in 9 points, any cubic passing through 8 of them also passes through the 9th.

## Chapter 3: Affine Varieties and the Nullstellensatz

### 3.1 Noetherian Rings

> [!INFO] Definition: Noetherian Ring
> A ring $A$ is **Noetherian** if it satisfies the Ascending Chain Condition (ACC) on ideals:
> $I_1 \subseteq I_2 \subseteq \dots$ stabilizes.
> Equivalently, every ideal $I \subseteq A$ is finitely generated.

### 3.3 Hilbert Basis Theorem

> [!TIP] Hilbert Basis Theorem
> If $A$ is a Noetherian ring, then the polynomial ring $A[x]$ is Noetherian.
> **Corollary**: $k[x_1, \dots, x_n]$ is a Noetherian ring.

### 3.5 Zariski Topology

> [!INFO] Definition: Algebraic Set
> Examples of closed sets in the Zariski topology on $\mathbb{A}^n$:
> $$ V(S) = \{ P \in \mathbb{A}^n \mid f(P) = 0 \quad \forall f \in S \} $$

### 3.10 Hilbert's Nullstellensatz

> [!TIP] Weak Nullstellensatz
> If $k$ is algebraically closed and $J \subsetneq k[x_1, \dots, x_n]$ is a proper ideal, then:
> $$ V(J) \neq \emptyset $$

> [!TIP] Strong Nullstellensatz
> For any ideal $J \subseteq k[x_1, \dots, x_n]$ where $k$ is algebraically closed:
> $$ I(V(J)) = \sqrt{J} $$
> where $\sqrt{J} = \{ f \mid f^r \in J \text{ for some } r \ge 1 \}$.

## Chapter 4: Functions on Varieties

### 4.1 Polynomial Maps

> [!INFO] Definition: Morphism
> A map $f: V \to W$ between algebraic sets is a **morphism** (or polynomial map) if it is given by polynomials in the coordinates.

> [!INFO] Definition: Coordinate Ring
> The coordinate ring of an affine variety $V \subseteq \mathbb{A}^n$ is:
> $$ k[V] = k[x_1, \dots, x_n] / I(V) $$

### 4.5 Isomorphism

> [!TIP] Theorem
> An isomorphism of varieties $f: V \xrightarrow{\sim} W$ induces an isomorphism of coordinate rings $f^*: k[W] \xrightarrow{\sim} k[V]$.
> This functorial correspondence is an equivalence of categories between affine varieties and finitely generated reduced $k$-algebras.

### 4.8 Rational Maps

> [!INFO] Definition: Rational Map
> A **rational map** $f: V \dashrightarrow W$ is a map defined by rational functions. It is defined on a non-empty open subset of $V$.
> **Dominant**: The image of $f$ is dense in $W$ (equivalent to $f^*: k(W) \hookrightarrow k(V)$ being a field extension).

## Chapter 5: Projective and Birational Geometry

### 5.1 Graded Rings and Homogeneous Ideals

> [!INFO] Definition: Projective Variety
> A subset $V \subseteq \mathbb{P}^n$ is a projective variety if it is the zero set of a collection of **homogeneous polynomials**.

### 5.3 Projective Nullstellensatz

> [!TIP] Theorem
> Let $J$ be a homogeneous ideal in $k[X_0, \dots, X_n]$.
> $V(J) = \emptyset$ if and only if $\sqrt{J}$ contains the **irrelevant ideal** $\mathfrak{m} = \langle X_0, \dots, X_n \rangle$.
> Otherwise, $I(V(J)) = \sqrt{J}$.

### 5.8 Birational Equivalence

> [!INFO] Definition: Birational Equivalence
> Two varieties $V$ and $W$ are **birationally equivalent** if there exist rational maps $f: V \dashrightarrow W$ and $g: W \dashrightarrow V$ that are inverses where defined.
> Equivalently, their function fields are isomorphic: $k(V) \cong k(W)$.

> [!EXAMPLE]
> The line $\mathbb{P}^1$ and the conic $xy = z^2$ are birationally equivalent (and isomorphic).
> The Cuspidal cubic $y^2 = x^3$ is birationally equivalent to $\mathbb{P}^1$ (via $t \mapsto (t^2, t^3)$), but NOT isomorphic.
