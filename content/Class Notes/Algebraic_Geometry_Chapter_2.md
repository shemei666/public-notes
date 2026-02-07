---
title: Chapter 2 - Cubics and the Group Law
tags: [Algebraic Geometry, Cubics, Group Law, Genus]
---

# Chapter 2: Cubics and the Group Law

## Examples of parametrised cubics

Some plane cubic curves can be parametrised, just as the conics:

### Nodal cubic
$C : y^2 = x^3 + x^2$ in $\mathbb{R}^2$ is the image of the map $\phi : \mathbb{R}^1 \to \mathbb{R}^2$ given by
$$ t \mapsto (t^2 - 1, t^3 - t) $$
(check it and see).

### Cuspidal cubic
$C : y^2 = x^3$ in $\mathbb{R}^2$ is the image of $\phi : \mathbb{R}^1 \to \mathbb{R}^2$ given by
$$ t \mapsto (t^2, t^3) $$

![Figure 2.1: Parametrised cubic curves](figure_2_1_placeholder.png)

Think about the singularities of the image curve, and of the map $\phi$. These examples will occur throughout the course, so spend some time playing with the equations; see Ex. 2.1–2.

The curve $y^2 = x(x-1)(x-\lambda)$ has no rational parametrisation.

Parametrised curves are nice; for example, if you’re interested in Diophantine problems, you could hope for a rule giving all $\mathbb{Q}$-valued points, as in (1.1). The parametrisation of (1.1) was of the form $x = f(t), y = g(t)$, where $f$ and $g$ were rational functions, that is, quotients of two polynomials.

> [!TIP] Theorem
> Let $k$ be a field of characteristic $\neq 2$, and let $\lambda \in k$ with $\lambda \neq 0, 1$; let $f, g \in k(t)$ be rational functions such that
> $$ f^2 = g(g-1)(g-\lambda). \quad (*)$$
> Then $f, g \in k$ (are constants).

This is equivalent to saying that there does not exist any nonconstant map $\mathbb{R}^1 \dashrightarrow C : (y^2 = x(x-1)(x-\lambda))$ given by rational functions. This reflects a very strong ‘rigidity’ property of varieties.

> [!NOTE]- Proof
> Using the fact that $k[t]$ is a UFD, I write
> $f = r/s$ with $r, s \in k[t]$ and coprime,
> $g = p/q$ with $p, q \in k[t]$ and coprime.
> Clearing denominators, (*) becomes
> $$ r^2q^3 = s^2p(p-q)(p-\lambda q). $$
> Then since $r$ and $s$ are coprime, the factor $s^2$ on the right-hand side must divide $q^3$, and in the same way, since $p$ and $q$ are coprime, the left-hand factor $q^3$ must divide $s^2$. Therefore,
> $s^2 \mid q^3$ and $q^3 \mid s^2$, so that $s^2 = a q^3$ with $a \in k$ ($a$ is a unit of $k[t]$, therefore in $k$).
> Then $aq = (s/q)^2$ is a square in $k[t]$.
> Also, $r^2 = ap(p-q)(p-\lambda q)$, so that by considering factorisation into primes, there exist nonzero constants $b, c, d \in k$ such that
> $bp, c(p-q), d(p-\lambda q)$ are all squares in $k[t]$.
> If I can prove that $p, q$ are constants, then it follows from what’s already been said that $r, s$ are also, proving the theorem. To prove that $p, q$ are constants, set $K$ for the algebraic closure of $k$; then $p, q \in K[t]$ satisfy the conditions of the next lemma.

> [!TIP] Lemma 2.3
> Let $K$ be an algebraically closed field, $p, q \in K[t]$ coprime elements, and assume that 4 distinct linear combinations (that is, $\lambda p + \mu q$ for 4 distinct ratios $(\lambda : \mu) \in \mathbb{P}^1_K$) are squares in $K[t]$; then $p, q \in K$.

> [!NOTE]- Proof (Fermat’s method of ‘infinite descent’)
> See text for details. Uses contradiction on degrees.

## Linear systems

Write $S_d = \{ \text{forms of degree } d \text{ in } (X, Y, Z) \}$; (recall that a form is just a homogeneous polynomial).
$S_d$ is a $k$-vector space of dimension $\binom{d+2}{2}$.
For $P_1, \dots, P_n \in \mathbb{P}^2$, let
$$ S_d(P_1, \dots, P_n) = \{ F \in S_d \mid F(P_i) = 0 \text{ for } i = 1, \dots, n \} \subset S_d. $$
This is a vector space of dimension $\ge \binom{d+2}{2} - n$.

> [!TIP] Lemma 2.5
> Suppose that $k$ is an infinite field, and let $F \in S_d$.
> (i) Let $L \subset \mathbb{P}^2$ be a line; if $F \equiv 0$ on $L$, then $F$ is divisible in $k[X, Y, Z]$ by the equation of $L$. That is, $F = H \cdot F'$ where $H$ is the equation of $L$ and $F' \in S_{d-1}$.
> (ii) Let $C \subset \mathbb{P}^2$ be a nonempty nondegenerate conic; if $F \equiv 0$ on $C$, then $F$ is divisible in $k[X, Y, Z]$ by the equation of $C$. That is, $F = Q \cdot F'$ where $Q$ is the equation of $C$ and $F' \in S_{d-2}$.

> [!TIP] Corollary
> Let $L : (H = 0) \subset \mathbb{P}^2$ be a line (or $C : (Q = 0) \subset \mathbb{P}^2$ a nondegenerate conic); suppose that points $P_1, \dots, P_n \in \mathbb{P}^2$ are given.
> (i) If $P_1, \dots, P_a \in L, P_{a+1}, \dots, P_n \notin L$ and $a > d$, then
> $S_d(P_1, \dots, P_n) = H \cdot S_{d-1}(P_{a+1}, \dots, P_n)$.
> (ii) If $P_1, \dots, P_a \in C, P_{a+1}, \dots, P_n \notin C$ and $a > 2d$, then
> $S_d(P_1, \dots, P_n) = Q \cdot S_{d-2}(P_{a+1}, \dots, P_n)$.

> [!TIP] Proposition 2.6
> Let $k$ be an infinite field, and $P_1, \dots, P_8 \in \mathbb{P}^2$ distinct points; suppose that no 4 of $P_1, \dots, P_8$ are collinear, and no 7 of them lie on a nondegenerate conic; then
> $$ \dim S_3(P_1, \dots, P_8) = 2. $$

> [!TIP] Corollary 2.7
> Let $C_1, C_2$ be two cubic curves whose intersection consists of 9 distinct points, $C_1 \cap C_2 = \{P_1, \dots, P_9\}$. Then a cubic $D$ through $P_1, \dots, P_8$ also passes through $P_9$.

## Group law on a plane cubic

Suppose $k \subset \mathbb{C}$ is a subfield, and $F \in k[X, Y, Z]$ a cubic form defining a (nonempty) plane curve $C : (F = 0) \subset \mathbb{P}^2$. Assume that $F$ satisfies:
(a) $F$ is irreducible (so that $C$ does not contain a line or conic);
(b) for every point $P \in C$, there exists a unique line $L \subset \mathbb{P}^2$ such that $P$ is a repeated zero of $F|_L$.

Fix any point $O \in C$, and make the following construction:

### Construction
(i) For $A \in C$, let $\bar{A} = \text{3rd point of intersection of } C \text{ with the line } OA$;
(ii) for $A, B \in C$, write $R = \text{3rd point of intersection of } AB \text{ with } C$, and define $A + B$ by
$$ A + B = \bar{R} $$

> [!TIP] Theorem
> The above construction defines an Abelian group law on $C$, with $O$ as zero (= neutral element).

![Figure 2.3: Cubic curve and its group law](figure_2_3_placeholder.png)

### Associativity
Associativity is the hardest part.
Proof by continuity:
I sketch one version of the argument ‘by continuity’, which uses the fact that $k \subset \mathbb{C}$. Write $C_{\mathbb{C}} \subset \mathbb{P}^2$ for the complexified curve. If the associative law holds for all $A, B, C \in C_{\mathbb{C}}$, then obviously also for all points in $C$. Therefore, I can assume that $k = \mathbb{C}$.
The addition law is a map $\phi : C \times C \to C$. By lemma, $\phi$ is continuous.
The subset $U \subset C \times C \times C$ consisting of triples where the 9 points are distinct is dense; the maps $(A, B, C) \mapsto (A+B)+C$ and $A+(B+C)$ coincide on $U$.

## Pascal’s Theorem (The Mystic Hexagon)

The diagram consists of a hexagon $ABCDEF$ in $\mathbb{P}^2$ with pairs of opposite sides extended until they meet in points $P, Q, R$. Assume that the nine points and the six lines of the diagram are all distinct; then
$$ A,B,C,D,E,F \text{ are conconic} \iff P,Q,R \text{ are collinear}. $$

![Figure 2.4: The mystic hexagon](figure_2_4_placeholder.png)

## Inflexion, normal form

Every cubic in $\mathbb{P}^2$ or $\mathbb{R}^2$ can be put in the normal form (Weierstrass normal form):
$$ C : Y^2Z = X^3 + aXZ^2 + bZ^3 \quad (\text{projective}) $$
$$ C : y^2 = x^3 + ax + b \quad (\text{affine}) $$

An inflexion point $P$ on a curve $C$ is defined by the condition that there is a line $L \subset \mathbb{P}^2$ such that $F|_L$ has a zero of multiplicity $\ge 3$ at $P$.
It can be shown that conversely, if a plane cubic $C$ has an inflexion point, then its equation can be put in normal form.

### Simplified group law

The normal form is extremely convenient for the group law: take the inflexion point $O = (0, 1, 0)$ as the neutral element.
$C = O \cup \text{affine curve } C_0 : (y^2 = x^3 + ax + b)$.
The inverse is given by $(x, y) \mapsto (x, -y)$.
For all $P, Q, R \in C$,
$$ P + Q + R = O \iff P, Q, R \text{ are collinear}. $$

![Figure 2.6: Minus as reflexion in the x-axis](figure_2_6_placeholder.png)

## Exercises to Chapter 2

1. Parametrise $y^2 = x^3 + x^2$.
2. Prove that any polynomial vanishing on the image of $t \mapsto (t^2, t^3)$ is divisible by $Y^2 - X^3$.
3. Tangent line formula.
4. Point of order 4 on $y^2 = x^3 + 4x$.
5. Points of order 2 on $y^2 = x^3 + ax + b$.
6. Geometric construction of points of order 4.
7. Computer program for group law.
8. Rational function formula for $A+B$.
9. Formula for $2A$.
10. Conditions on coefficients for $P=(0,0)$ to be inflexion point.
11. Reducing cubic with inflexion point to normal form.
12. Group law on cuspidal cubic.
13. Fibonacci (1220): $u^2+v^2$ and $u^2-v^2$ squares implies $v=0$.

## Appendix: Curves and their genus

### Topology of a nonsingular cubic
A nonsingular plane cubic $C_{\mathbb{C}} \subset \mathbb{P}^2$ is topologically a torus.
The map $\pi : C \to \mathbb{P}^1$ by $(X, Y, Z) \mapsto (X, Z)$ exhibits $C$ as a double cover of the Riemann sphere $\mathbb{P}^1$ branched in the roots of the cubic and $\infty$.
Cutting the sphere along slits reveals the topology.

### Discussion of genus
A nonsingular projective curve $C$ over $\mathbb{C}$ has just one topological invariant, its genus $g = g(C)$.
Genus of nonsingular plane curve $C_d \subset \mathbb{P}^2$ of degree $d$ is given by
$$ g = \frac{(d-1)(d-2)}{2} $$

Trichotomy:
- $g = 0$: Parametrisable by rational functions (e.g. conics, if they have a point).
- $g = 1$: Elliptic curves, group law.
- $g \ge 2$: Finite number of rational points (Faltings' Theorem).

Over $\mathbb{C}$, a curve of genus 1 is $C \cong \mathbb{C}/(\mathbb{Z} \oplus \mathbb{Z} \cdot \tau)$.
The period $\tau$ is a modulus.
