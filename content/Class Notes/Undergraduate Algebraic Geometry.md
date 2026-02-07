---
publish: false
tags:
  - math
  - algebraic-geometry
  - notes
---
# Undergraduate Algebraic Geometry

Based on the notes by Miles Reid.

## Chapter 1: Plane Conics

### 1.1 Example of a parametrized curve

Pythagoras' Theorem $X^2 + Y^2 = Z^2$ has integer solutions like $(3,4,5)$ and $(5,12,13)$.
The homogeneous equation corresponds to the circle $C: x^2 + y^2 = 1$ in $\mathbb{R}^2$ (where $x=X/Z, y=Y/Z$).

**Parametrization**:
We can parametrise it using the slope $\lambda$ of a line through the point $P=(0,1)$.
$$ x = \frac{2\lambda}{1+\lambda^2}, \quad y = \frac{\lambda^2-1}{1+\lambda^2} \quad \text{where } \lambda = \frac{x}{1-y} $$
This gives all integer solutions:
$$ X = 2\ell m, \quad Y = \ell^2 - m^2, \quad Z = \ell^2 + m^2 $$
where $\ell, m \in \mathbb{Z}$ are coprime.

### 1.2 Similar example

Consider $C: 2X^2 + Y^2 = 5Z^2$.
Parametrization $\mathbb{R} \to C$:
$$ x = \frac{2\sqrt{5}\lambda}{1+2\lambda^2}, \quad y = \frac{2\lambda^2 - 1}{1+2\lambda^2} $$
However, over $\mathbb{Q}$, the situation is different.

> [!TIP] Proposition
> If $(a,b,c) \in \mathbb{Q}$ satisfies $2a^2 + b^2 = 5c^2$, then $(a,b,c) = (0,0,0)$.

> [!NOTE]- Proof
> Multiply by denominators to get integers. Assume $a,b,c$ coprime.
> Modulo 5: $2a^2 + b^2 \equiv 0 \pmod 5$.
> Squares mod 5 are $0, 1, 4$.
> $2(0)+0=0$, $2(1)+1=3$, $2(1)+4=6$, $2(4)+1=9$, $2(4)+4=12$.
> Only solution is $a \equiv 0, b \equiv 0$.
> Then $a=5a', b=5b'$.
> $2(25a'^2) + 25b'^2 = 5c^2 \implies 10a'^2 + 5b'^2 = c^2$.
> So $5 \mid c^2 \implies 5 \mid c$.
> Thus $5$ divides $a,b,c$, contradiction.

### 1.3 Conics in $\mathbb{R}^2$

A conic is given by a quadratic equation:
$$ q(x,y) = ax^2 + bxy + cy^2 + dx + ey + f = 0 $$

**Classification**:
1.  **Nondegenerate**: Ellipse, Parabola, Hyperbola.
2.  **Degenerate**:
    *   Single point ($x^2 + y^2 = 0$)
    *   Empty set ($x^2 + y^2 = -1$)
    *   Line pair ($xy=0$ or parallel $x(x-1)=0$)
    *   Double line ($x^2=0$)
    *   Whole plane ($0=0$)

### 1.4 Projective plane

> [!INFO] Definition
> $\mathbb{P}^2_{\mathbb{R}} = \{ \text{lines in } \mathbb{R}^3 \text{ through origin} \}$
> $= (\mathbb{R}^3 \setminus \{0\}) / \sim$ where $(X,Y,Z) \sim (\lambda X, \lambda Y, \lambda Z)$.
> Points are ratios $(X:Y:Z)$.

**Affine chart**:
If $Z \neq 0$, $(X:Y:Z) = (X/Z : Y/Z : 1)$. This gives a copy of $\mathbb{R}^2$.
Points with $Z=0$ are "points at infinity" or asymptotic directions.

**Transformations**:
*   **Affine**: $T(\mathbf{x}) = A\mathbf{x} + B$.
*   **Projective**: $T(\mathbf{X}) = M\mathbf{X}$ where $M$ is invertible $3 \times 3$. $\mathbb{P}^2 \to \mathbb{P}^2$.

### 1.5 Equation of a conic

Homogeneous quadratic $Q(X,Y,Z)$.
Relation to affine: $q(x,y) = Q(x,y,1)$.
Line at infinity $L_\infty: Z=0$.
A line in $\mathbb{P}^2$ is $aX + bY + cZ = 0$.

**Examples**:
*   Hyperbola $\frac{x^2}{a^2} - \frac{y^2}{b^2} = 1$ meets $Z=0$ in 2 points $(a, \pm b, 0)$.
*   Parabola $y=mx^2$ meets $Z=0$ at $(0,1,0)$.

### 1.6 Classification of conics in $\mathbb{P}^2$

Bijective correspondence between homogeneous quadratic polynomials and symmetric bilinear forms.

> [!TIP] Theorem (Diagonalization)
> For a quadratic form $Q$, there exists a basis such that $Q = \varepsilon_1 x_1^2 + \dots + \varepsilon_n x_n^2$.

> [!INFO] Corollary: List of Conics in $\mathbb{P}^2_{\mathbb{R}}$
> 1.  **Nondegenerate conic**: $X^2 + Y^2 - Z^2 = 0$. (Ellipse/Hyperbola/Parabola are all isomorphic to this).
> 2.  **Empty set**: $X^2 + Y^2 + Z^2 = 0$.
> 3.  **Line pair**: $X^2 - Y^2 = 0$.
> 4.  **One point**: $X^2 + Y^2 = 0$ ($ (0,0,1) $).
> 5.  **Double line**: $X^2 = 0$.

### 1.7 Parametrisation of a conic

Let $C \subset \mathbb{P}^2_{\mathbb{R}}$ be a nondegenerate nonempty conic.
Projectively equivalent to $XZ = Y^2$.
Parametrisation $\Phi: \mathbb{P}^1 \to C$:
$$ (U:V) \mapsto (U^2 : UV : V^2) $$
**Inverse map** $\Psi: C \to \mathbb{P}^1$:
$$ (X:Y:Z) \mapsto (X:Y) = (Y:Z) $$
(Left ratio if $X \neq 0$, right if $Z \neq 0$).

### 1.8 Homogeneous form in 2 variables

Let $F(U,V)$ be a nonzero homogeneous polynomial of degree $d$.
Zeros of $F$ on $\mathbb{P}^1$ correspond to roots of $f(u) = F(u,1)$.
Multiplicity can be defined.
A form of degree $d$ has $d$ zeros on $\mathbb{P}^1$ (over algebraically closed field), counted with multiplicity.

### 1.9 Easy cases of Bézout's Theorem

> [!TIP] Theorem (Line and Curve)
> Let $L \subset \mathbb{P}^2_k$ be a line and $D \subset \mathbb{P}^2_k$ a curve of degree $d$, with $L \not\subset D$.
> Then $\# \{ L \cap D \} \le d$.
> If $k$ is algebraically closed, equality holds (counting multiplicities).

**Proof Idea**:
Parametrize $L$ as $X=a(U,V), Y=b(U,V), Z=c(U,V)$ (linear forms).
Substitute into equation of $D$: $G(a,b,c) = F(U,V) = 0$.
$F$ is form of degree $d$, so has $\le d$ zeros.

> [!TIP] Theorem (Conic and Curve)
> If $C$ is a nondegenerate conic and $D$ a curve of degree $d$, $C \not\subset D$.
> Then $\# \{ C \cap D \} \le 2d$.

### 1.10 Corollary: unique conic through 5 general points

> [!TIP] Corollary
> If $P_1, \dots, P_5 \in \mathbb{P}^2$ are distinct and no 4 are collinear, there exists **at most one** conic through them.

### 1.11 Space of all conics

The space of quadratic forms on $\mathbb{R}^3$ is isomorphic to the space of symmetric $3 \times 3$ matrices, which has dimension 6.
$$ S_2 \cong \mathbb{R}^6 $$
For a point $P_0$, the condition $Q(P_0) = 0$ is a linear equation on the coefficients.
$S_2(P_1, \dots, P_n)$ is the subspace of conics passing through $n$ points.
$$ \dim S_2(P_1, \dots, P_n) \ge 6-n $$

> [!INFO] Corollary
> If $n \le 5$ and no 4 points are collinear, $\dim S_2(P_1, \dots, P_n) = 6-n$.
> For $n=5$, dimension is 1, so there is a unique conic (up to scalar).

### 1.12 Intersection of two conics

Two conics $C_1, C_2$ generally meet in 4 points (by Bézout, $2 \times 2 = 4$).
Intersection points $P_1, P_2, P_3, P_4$.

### 1.13 Degenerate conics in a pencil

> [!INFO] Definition: Pencil
> A **pencil of conics** is a family $C_{(\lambda, \mu)}: \lambda Q_1 + \mu Q_2 = 0$.

A conic in the pencil is degenerate if $\det(\lambda Q_1 + \mu Q_2) = 0$.
This determinant is a homogeneous **cubic** polynomial in $\lambda, \mu$.
Thus, there are at most 3 degenerate conics in a pencil (over $\mathbb{R}$, at least one).

### 1.14 Worked example

Let $P_1, \dots, P_4$ be 4 points in generally position.
The pencil of conics through them has 3 degenerate elements (line pairs):
1.  $L_{12} \cup L_{34}$
2.  $L_{13} \cup L_{24}$
3.  $L_{14} \cup L_{23}$

Finding the intersection of two conics $Q_1=0, Q_2=0$ reduces to finding roots of the cubic equation $\det(\lambda Q_1 + \mu Q_2) = 0$.

## Chapter 2: Cubics and the Group Law

### 2.1 Examples of parametrized cubics

Some plane cubic curves can be parametrized, just as conics.

1.  **Nodal cubic** $C: y^2 = x^3 + x^2$.
    Image of map $\mathbb{R}^1 \to \mathbb{R}^2$ given by $t \mapsto (t^2-1, t^3-t)$.
    Has a node (self-intersection) at $(0,0)$.

2.  **Cuspidal cubic** $C: y^2 = x^3$.
    Image of map given by $t \mapsto (t^2, t^3)$.
    Has a cusp at $(0,0)$.

### 2.2 Non-rationality of elliptic curves

> [!TIP] Theorem
> The curve $y^2 = x(x-1)(x-\lambda)$ where $\lambda \neq 0,1$ has **no rational parametrisation**.
> That is, there are no non-constant rational functions $f,g \in k(t)$ such that $f^2 = g(g-1)(g-\lambda)$.

**Proof Strategy**:
Uses the fact that $k[t]$ is a Unique Factorization Domain (UFD).
Assume $f=r/s, g=p/q$.
Derive contradiction using "Fermat's method of infinite descent" (Lemma 2.3).
Show that if a solution exists, one with smaller degree must exist, which leads to contradiction.

### 2.3 Lemma (Infinite Descent)

Let $K$ be an algebraically closed field.
If $p, q \in K[t]$ are coprime and 4 distinct linear combinations ($\lambda p + \mu q$) are squares in $K[t]$, then $p, q \in K$.

### 2.4 Linear systems

Let $S_d = \{ \text{forms of degree } d \text{ in } X,Y,Z \}$.
This is a vector space of dimension $\binom{d+2}{2}$.
Basis can be formed by monomials $x^i y^j z^k$ with $i+j+k=d$.

**Dimensions**:
*   $d=1$: Plane lines, $\dim S_1 = 3$.
*   $d=2$: Plane conics, $\dim S_2 = 6$.
*   $d=3$: Plane cubics, $\dim S_3 = 10$.

For points $P_1, \dots, P_n \in \mathbb{P}^2$, let $S_d(P_1, \dots, P_n) = \{ F \in S_d \mid F(P_i) = 0 \}$.
Each point imposes one linear condition.
$$ \dim S_d(P_1, \dots, P_n) \ge \dim S_d - n $$

### 2.5 Lemma (Divisibility)

1.  Let $L \subset \mathbb{P}^2$ be a line. If $F \in S_d$ vanishes on $L$, then $F$ is divisible by the equation of $L$.
2.  Let $C \subset \mathbb{P}^2$ be a nondegenerate conic. If $F \in S_d$ vanishes on $C$, then $F$ is divisible by the equation of $C$.

> [!INFO] Corollary (Counting Constants)
> *   Through 8 general points, there is a pencil of cubics (dim $\ge 10-8=2$).
> *   Through 9 general points, there is a unique cubic (dim $\ge 10-9=1$).

### 2.6 Proposition

Let $P_1, \dots, P_8 \in \mathbb{P}^2$ be distinct points such that:
*   No 4 are collinear.
*   No 7 lie on a nondegenerate conic.
Then $\dim S_3(P_1, \dots, P_8) = 2$.

**Proof**: Cases involving general position, points on a line, points on a conic.

### 2.7 Corollary (Cayley-Bacharach Theorem for Cubics)

Let $C_1, C_2$ be two cubic curves meeting in exactly 9 distinct points $\{P_1, \dots, P_9\}$.
If a cubic $D$ passes through $P_1, \dots, P_8$, then it implies $D$ passes through $P_9$ as well.

### 2.8 Group law on a plane cubic

Let $C \subset \mathbb{P}^2$ be a nonsingular cubic. Fix a point $O \in C$ as the zero element.

**Construction of $A+B$**:
1.  Draw line $L$ through $A$ and $B$. Let $R$ be the 3rd point of intersection ($L \cap C = \{A, B, R\}$).
2.  Draw line $L'$ through $R$ and $O$. Let $S$ be the 3rd point of intersection.
3.  Define $A+B = S$.

**Negation**:
$-A$ is the 3rd intersection of the line $OA$ with $C$. (Assuming inflection point $O$, $-A$ is just $R$ above? Wait. The construction usually says $A+B+R = O$ in group law sense if line is $A,B,R$. But using the "chord and tangent" process: $AB$ meets $C$ at $R$. $OR$ meets $C$ at $A+B$. This matches the text description: $A+B = \bar{R}$ where $\bar{R}$ is 3rd point on $OR$. Wait, text says $A+B=\overline{R}$ where $\overline{R}$ is 3rd point of intersection of $OR$ with $C$. $\overline{R}$ usually denotes $-R$. So $A+B = -R = -(-(A+B))$. Yes.)

> [!TIP] Theorem
> This geometric operation defines an abelian group structure on the points of $C$.

### 2.9 Associativity "in general"

Proof uses the configuration of 9 points and Corollary 2.7.
Consider points forming intersection of two sets of 3 lines (cubics).
$(A+B)+C = A+(B+C)$ corresponds to two ways of resolving the pencil.

### 2.10 Proof by continuity

Alternative proof of associativity utilizing the topology of $\mathbb{C}$.
Since the group operations are given by rational functions, they are continuous.
Associativity holds for a dense open set of configurations, hence it holds everywhere by continuity.



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
