---
title: Chapter 1 - Plane Conics
tags: [Algebraic Geometry, Conics, Projective Plane]
---

# Chapter 1: Plane Conics

I start by studying the geometry of conics as motivation for the projective plane $\mathbb{P}^2$. Projective geometry is usually mentioned in 2nd year undergraduate geometry courses, and I recall some of the salient features, with some emphasis on homogeneous coordinates, although I completely ignore the geometry of linear subspaces and the ‘cross-ratio’. The most important aim for the student should be to grasp the way in which geometric ideas (for example, the idea that ‘points at infinity’ correspond to asymptotic directions of curves) are expressed in terms of coordinates. The interplay between the intuitive geometric picture (which tells you what you should be expecting), and the precise formulation in terms of coordinates (which allows you to cash in on your intuition) is a fascinating aspect of algebraic geometry.

## Example of a parametrised curve

Pythagoras’ Theorem says that, in the diagram
$$ X^2 + Y^2 = Z^2 $$
(e.g. $(3, 4, 5)$ and $(5, 12, 13)$), as every ancient Egyptian knew. How do you find all integer solutions? The equation is homogeneous, so that $x = X/Z, y = Y/Z$ gives the circle $C : x^2 + y^2 = 1$ in $\mathbb{R}^2$, which can easily be seen to be parametrised as
$$ x = \frac{2\lambda}{\lambda^2+1}, \quad y = \frac{\lambda^2-1}{\lambda^2+1}, \quad \text{where } \lambda = \frac{x}{1-y} $$
so this gives all solutions:
$$ X = 2lm, \quad Y = l^2 - m^2, \quad Z = l^2 + m^2 \quad \text{with } l, m \in \mathbb{Z} \text{ coprime} $$
(or each divided by 2 if $l, m$ are both odd). Note that the equation is homogeneous, so that if $(X, Y, Z)$ is a solution, then so is $(\rho X, \rho Y, \rho Z)$.

Maybe the parametrisation was already familiar from school geometry, and in any case, it’s easy to verify that it works. However, if I didn’t know it already, I could have obtained it by an easy geometric argument, namely linear projection from a given point: $P = (0, 1) \in C$, and if $\lambda \in \mathbb{Q}$ is any value, then the line $L_\lambda$ through $P$ with slope $\lambda$ meets $C$ in a further point $Q_\lambda$. This construction of a map by means of linear projection will appear many times in what follows.

![Figure 1.1: Linear projection of a conic to a line](figure_1_1_placeholder.png)

### Similar example
$C : 2X^2 + Y^2 = 5Z^2$. The same method leads to the parametrisation $\mathbb{R} \to C$ given by
$$ x = \frac{1+2\lambda^2}{1+2\lambda^2}, \quad y = \frac{2\lambda^2 - 1}{1+2\lambda^2} $$
Only, wait, the text says:
$$ x = \frac{2\sqrt{5}\lambda^2}{\dots} \quad \text{no, scanning error likely.} $$
Let's deduce it. $P=(1, \sqrt{3})$? No.
If we project from a rational point...
The notes say: "This allows us to understand all about points of $C$ with coefficients in $\mathbb{R}$... what about $\mathbb{Q}$?"

> [!TIP] Proposition
> If $(a, b, c) \in \mathbb{Q}$ satisfies $2a^2 + b^2 = 5c^2$ then $(a, b, c) = (0, 0, 0)$.

> [!NOTE]- Proof
> Multiplying through by a common denominator and taking out a common factor if necessary, I can assume that $a, b, c$ are integers, not all of which are divisible by 5; also if $5 \nmid a$ and $5 \nmid b$ then $25 \nmid 5c^2$, so that $5 \nmid c$, which contradicts what I’ve just said. It is now easy to get a contradiction by considering the possible values of $a$ and $b \pmod 5$: since any square is 0, 1 or 4 mod 5, clearly $2a^2 + b^2$ is one of $0 + 1, 0 + 4, 2 + 0, 2 + 1, 2 + 4, 8 + 0, 8 + 1$ or $8 + 4 \pmod 5$, none of which can be of the form $5c^2$. Q.E.D.

Note that this is a thoroughly arithmetic argument.

## Conics in $\mathbb{R}^2$

A conic in $\mathbb{R}^2$ is a plane curve given by a quadratic equation
$$ q(x, y) = ax^2 + bxy + cy^2 + dx + ey + f = 0 $$
Everyone has seen the classification of nondegenerate conics:
1. Ellipse
2. Parabola
3. Hyperbola

![Figure 1.2: The nondegenerate conics](figure_1_2_placeholder.png)

In addition, there are a number of peculiar cases:
- (d) single point given by $x^2 + y^2 = 0$;
- (e, f, g) empty set given by any of the 3 equations: (e) $x^2 + y^2 = -1$, (f) $x^2 = -1$ or (g) $0 = 1$. These three equations are different, although they define the same locus of zeros in $\mathbb{R}^2$; consider for example their complex solutions.
- line $x = 0$;
- line pair $xy = 0$;
- parallel lines $x(x-1) = 0$;
- ‘double line’ $x^2 = 0$; you can choose for yourself whether you’ll allow the final case:
- whole plane given by $0 = 0$.

## Projective plane

The definition ‘out of the blue’:
$$ \mathbb{P}^2_{\mathbb{R}} = \{ \text{lines of } \mathbb{R}^3 \text{ through origin} \} $$
$$ = \{ \text{ratios } X : Y : Z \} $$
$$ = (\mathbb{R}^3 \setminus \{0\}) / \sim, \quad \text{where } (X, Y, Z) \sim (\lambda X, \lambda Y, \lambda Z) \text{ if } \lambda \in \mathbb{R} \setminus \{0\}. $$

(The sophisticated reader will have no difficulty in generalising from $\mathbb{R}^3$ to an arbitrary vector space over a field, and in replacing work in a chosen coordinate system with intrinsic arguments.) To represent a ratio $X : Y : Z$ for which $Z \neq 0$, I can set $x = X/Z, y = Y/Z$; this simplifies things, since the ratio corresponds to just two real numbers. In other words, the equivalence class of $(X, Y, Z)$ contains a unique representative $(x, y, 1)$ with 3rd coordinate = 1. Unfortunately, sometimes $Z$ might be $= 0$, so that this way of choosing a representative of the equivalence class is then no good. This discussion means that $\mathbb{P}^2$ contains a copy of $\mathbb{R}^2$. A picture:
$$ \mathbb{R}^2 \hookrightarrow \mathbb{R}^3 \setminus \{0\} \to \mathbb{P}^2 \text{ by } (x, y) \mapsto (x, y, 1) $$
The general line in $\mathbb{R}^3$ through 0 is not contained in the plane $(Z = 0)$, so that it meets $(Z = 1)$ in exactly one point, which is a representative for that equivalence class. The lines in $(Z = 0)$ never meet $(Z = 1)$, so they correspond not to points of $\mathbb{R}^2$, but to asymptotic directions, or to pencils of parallel lines of $\mathbb{R}^2$; so you can think of $\mathbb{P}^2$ as consisting of $\mathbb{R}^2$ together with one ‘point at infinity’ for every pencil of parallel lines. From this point of view, you calculate in $\mathbb{R}^2$, try to guess what’s going on at infinity by some kind of ‘asymptotic’ argument, then (if necessary), prove it in terms of homogeneous coordinates. The definition in terms of lines in $\mathbb{R}^3$ makes this respectable, since it treats all points of $\mathbb{P}^2$ on an equal footing.

Groups of transformations are of central importance throughout geometry; properties of a geometric figure must be invariant under the appropriate kind of transformations before they are significant. An affine change of coordinates in $\mathbb{R}^2$ is of the form $T(x) = Ax+B$, where $x = (x, y) \in \mathbb{R}^2$, and $A$ is a $2 \times 2$ invertible matrix, $B$ a translation vector; if $A$ is orthogonal then the transformation $T$ is Euclidean. As everyone knows, every nondegenerate conic can be reduced to one of the standard forms (a–c) above by a Euclidean transformation. It is an exercise to the reader to show that every conic can be reduced to one of the forms (a–l) by an affine transformation.

A projectivity, or projective transformation of $\mathbb{P}^2$ is a map of the form $T(X) = M X$, where $M$ is an invertible $3 \times 3$ matrix. It’s easy to understand the effect of this transformation on the affine piece $\mathbb{R}^2 \subset \mathbb{P}^2$: as a partially defined map $\mathbb{R}^2 \dashrightarrow \mathbb{R}^2$, it is the fractional-linear transformation
$$ \begin{pmatrix} x \\ y \end{pmatrix} \mapsto \begin{pmatrix} \frac{ax+by+c}{a'x+b'y+c'} \\ \frac{dx+ey+f}{d'x+e'y+f'} \end{pmatrix} $$
(reconstruction from text $T$ is of course not defined when denominator = 0).

Projective transformations are used implicitly throughout these notes, usually in the form ‘by a suitable choice of coordinates, I can assume . . . ’.

## Equation of a conic

The inhomogeneous quadratic polynomial
$$ q(x, y) = ax^2 + bxy + cy^2 + dx + ey + f $$
corresponds to the homogeneous quadratic
$$ Q(X, Y, Z) = aX^2 + bXY + cY^2 + dXZ + eYZ + fZ^2; $$
the correspondence is easy to understand as a recipe, or you can think of it as the bijection $q \leftrightarrow Q$ given by
$$ q(x, y) = Q(X/Z, Y/Z, 1) \quad \text{with } x = X/Z, y = Y/Z $$
and inversely,
$$ Q = Z^2 q(X/Z, Y/Z). $$
A conic $C \subset \mathbb{P}^2$ is the curve given by $C : (Q(X, Y, Z) = 0)$, where $Q$ is a homogeneous quadratic expression; note that the condition $Q(X, Y, Z) = 0$ is well defined on the equivalence class, since $Q(\lambda X) = \lambda^2 Q(X)$ for any $\lambda \in \mathbb{R}$. As an exercise, check that the projective curve $C$ meets the affine piece $\mathbb{R}^2$ in the affine conic given by $(q = 0)$.

### ‘Line at infinity’ and asymptotic directions

Points of $\mathbb{P}^2$ with $Z = 0$ correspond to ratios $(X : Y : 0)$. These points form the line at infinity, a copy of $\mathbb{P}^1 = \mathbb{R} \cup \{\infty\}$ (since $(X : Y) \mapsto X/Y$ defines a bijection $\mathbb{P}^1 \to \mathbb{R} \cup \{\infty\}$).

A line in $\mathbb{P}^2$ is by definition given by $L : (aX + bY + cZ = 0)$, and
$$ L \text{ passes through } (X, Y, 0) \iff aX + bY = 0. $$
In affine coordinates the same line is given by $ax + by + c = 0$, so that all lines with the same ratio $a : b$ pass through the same point at infinity. This is called ‘parallel lines meet at infinity’.

> [!EXAMPLE]
> (a) The hyperbola $(x^2/a^2 - y^2/b^2 = 1)$ in $\mathbb{R}^2$ corresponds in $\mathbb{P}^2$ to $C : (X^2/a^2 - Y^2/b^2 = Z^2)$; clearly this meets $(Z = 0)$ in the two points $(a, \pm b, 0) \in \mathbb{P}^2$, corresponding in the obvious way to the asymptotic lines of the hyperbola.
>
> Note that in the affine piece $(X \neq 0)$ of $\mathbb{P}^2$, the affine coordinates are $u = Y/X, v = Z/X$, so that $C$ becomes the ellipse $(u^2/b^2 + v^2 = 1/a^2)$. See Ex. 1.7 for an artistic interpretation.
>
> (b) The parabola $(y = mx^2)$ in $\mathbb{R}^2$ corresponds to $C : (YZ = mX^2)$ in $\mathbb{P}^2$; this now meets $(Z = 0)$ at the single point $(0, 1, 0)$. So in $\mathbb{P}^2$, the ‘two branches of the parabola meet at infinity’.

## Classification of conics in $\mathbb{P}^2$

Let $k$ be any field of characteristic $\neq 2$; recall two results from the linear algebra of quadratic forms:

> [!TIP] Proposition (A)
> There are natural bijections
> \{homogeneous quadratic polys.\} $\leftrightarrow$ \{quad. forms $k^3 \to k$\} $\leftrightarrow$ \{symmetric bilinear forms on $k^3$\}
> given in formulas by
> $aX^2 + 2bXY + cY^2 + 2dXZ + 2eYZ + fZ^2 \leftrightarrow \begin{pmatrix} a & b & d \\ b & c & e \\ d & e & f \end{pmatrix}$

A quadratic form is nondegenerate if the corresponding bilinear form is nondegenerate, that is, its matrix is nonsingular.

> [!TIP] Theorem (B)
> Let $V$ be a vector space over $k$ and $Q : V \to k$ a quadratic form; then there exists a basis of $V$ such that
> $$ Q = \varepsilon_1 x_1^2 + \varepsilon_2 x_2^2 + \dots + \varepsilon_n x_n^2, \quad \text{with } \varepsilon_i \in k. $$

(This is proved by Gram-Schmidt orthogonalisation, if that rings a bell.) Obviously, for $\lambda \in k \setminus \{0\}$ the substitution $x_i \mapsto \lambda x_i$ takes $\varepsilon_i$ into $\lambda^{-2}\varepsilon_i$.

> [!TIP] Corollary
> In a suitable system of coordinates, any conic in $\mathbb{P}^2$ is one of the following:
>
> ($\alpha$) nondegenerate conic, $C : (X^2 + Y^2 - Z^2 = 0)$;
>
> ($\beta$) empty set, given by $(X^2 + Y^2 + Z^2 = 0)$;
>
> ($\gamma$) line pair, given by $(X^2 - Y^2 = 0)$;
>
> ($\delta$) one point $(0, 0, 1)$, given by $(X^2 + Y^2 = 0)$;
>
> ($\varepsilon$) double line, given by $(X^2 = 0)$.

(Optionally you have the whole of $\mathbb{P}^2$ given by $(0 = 0)$.)

> [!NOTE]- Proof
> Any real number $\varepsilon$ is either 0, or $\pm$ a square, so that I only have to consider $Q$ as in the theorem with $\varepsilon_i = 0$ or $\pm 1$. In addition, since I’m only interested in the locus $(Q = 0)$, I’m allowed to multiply $Q$ through by $-1$. This leads at once to the given list. Q.E.D.

## Parametrisation of a conic

Let $C$ be a nondegenerate, nonempty conic of $\mathbb{P}^2$. Then by Corollary 1.6, taking new coordinates $(X+Z, Y, Z-X)$, $C$ is projectively equivalent to the curve $(XZ = Y^2)$; this is the curve parametrised by
$$ \Phi: \mathbb{P}^1 \to C \subset \mathbb{P}^2, \quad (U : V) \mapsto (U^2 : UV : V^2). $$

Remarks:
1. The inverse map $\Psi: C \to \mathbb{P}^1$ is given by
   $(X : Y : Z) \mapsto (X : Y) = (Y : Z)$;
   here the left-hand ratio is defined if $X \neq 0$, and the right-hand ratio if $Z \neq 0$. In terminology to be introduced later, $\Phi$ and $\Psi$ are inverse isomorphisms of varieties.
2. Throughout §§1–2, nonempty nondegenerate conics are tacitly assumed to be projectively equivalent to $(XZ - Y^2)$; over a field of characteristic $\neq 2$, this is justified in Ex. 1.5.

### Homogeneous form in 2 variables

Let $F(U, V)$ be a nonzero homogeneous polynomial of degree $d$ in $U, V$, with coefficients in a fixed field $k$:
$$ F(U, V) = a_d U^d + a_{d-1} U^{d-1} V + \dots + a_0 V^d. $$
$F$ has an associated inhomogeneous polynomial in 1 variable,
$$ f(u) = a_d u^d + a_{d-1} u^{d-1} + \dots + a_0. $$
Clearly for $\alpha \in k$,
$$ f(\alpha) = 0 \iff (u - \alpha) \mid f(u) \iff (U - \alpha V) \mid F(U, V) \iff F(\alpha, 1) = 0; $$
so zeros of $f$ correspond to zeros of $F$ on $\mathbb{P}^1$ away from the point $(1, 0)$, the ‘point $\alpha = \infty$’. What does it mean for $F$ to have a zero at infinity?
$$ F(1, 0) = 0 \iff a_d = 0 \iff \deg f < d. $$
Now define the multiplicity of a zero of $F$ on $\mathbb{P}^1$ to be:
- the multiplicity of $f$ at the corresponding $\alpha \in k$; or
- $d - \deg f$ if $(1, 0)$ is the zero.

So the multiplicity of zero of $F$ at a point $(\alpha, 1)$ is the greatest power of $(U - \alpha V)$ dividing $F$, and at $(1, 0)$ it is the greatest power of $V$ dividing $F$.

> [!TIP] Proposition
> Let $F(U, V)$ be a nonzero form of degree $d$ in $U, V$. Then $F$ has at most $d$ zeros on $\mathbb{P}^1$; furthermore, if $k$ is algebraically closed, then $F$ has exactly $d$ zeros on $\mathbb{P}^1$ provided these are counted with multiplicities as defined above.

## Easy cases of Bézout’s Theorem

Bézout’s theorem says that if $C$ and $D$ are plane curves of degrees $\deg C = m, \deg D = n$, then the number of points of intersection of $C$ and $D$ is $mn$, provided that (i) the field is algebraically closed; (ii) points of intersection are counted with the right multiplicities; (iii) we work in $\mathbb{P}^2$ to take right account of intersections ‘at infinity’.

> [!TIP] Theorem
> Let $L \subset \mathbb{P}^2$ be a line (respectively $C \subset \mathbb{P}^2$ a nondegenerate conic), and let $D \subset \mathbb{P}^2$ be a curve defined by $D : (G_d(X, Y, Z) = 0)$, where $G$ is a form of degree $d$ in $X, Y, Z$. Assume that $L \not\subset D$ (respectively, $C \not\subset D$); then
> $$ \#\{L \cap D\} \leq d \quad (\text{respectively } \#\{C \cap D\} \leq 2d). $$
> In fact there is a natural definition of multiplicity of intersection such that the inequality still holds for ‘number of points counted with multiplicities’, and if $k$ is algebraically closed then equality holds.

> [!NOTE]- Proof
> A line $L \subset \mathbb{P}^2$ is given by an equation $\lambda = 0$, with $\lambda$ a linear form; for my purpose, it is convenient to give it parametrically as
> $$ X = a(U, V), \quad Y = b(U, V), \quad Z = c(U, V), $$
> where $a, b, c$ are linear forms in $U, V$.
> Similarly, a nondegenerate conic can be given parametrically as
> $$ X = a(U, V), \quad Y = b(U, V), \quad Z = c(U, V), $$
> where $a, b, c$ are quadratic forms in $U, V$.
> Then the intersection of $L$ (respectively $C$) with $D$ is given by finding the values of the ratios $(U : V)$ such that
> $$ F(U, V) = G_d(a(U, V), b(U, V), c(U, V)) = 0. $$
> But $F$ is a form of degree $d$ (respectively $2d$) in $U, V$, so the result follows by (1.8). Q.E.D.

> [!TIP] Corollary 1.10
> If $P_1, \dots, P_5 \in \mathbb{P}^2$ are distinct points and no 4 are collinear, there exists at most one conic through $P_1, \dots, P_5$.

### Space of all conics

Let $S_2 = \{ \text{quadratic forms on } \mathbb{R}^3 \} \cong \mathbb{R}^6$.
For $P_1, \dots, P_n \in \mathbb{P}^2$, define
$$ S_2(P_1, \dots, P_n) = \{ Q \in S_2 \mid Q(P_i) = 0 \text{ for } i = 1, \dots, n \}; $$
then there are $n$ linear equations in the 6 coefficients of $Q$.

> [!TIP] Proposition
> $\dim S_2(P_1, \dots, P_n) \geq 6 - n$.

> [!TIP] Corollary
> If $n \leq 5$ and no 4 of $P_1, \dots, P_n$ are collinear, then $\dim S_2(P_1, \dots, P_n) = 6 - n$.

## Intersection of two conics

As we have seen above, it often happens that two conics meet in 4 points.
Conversely, given 4 points $P_1, \dots, P_4 \in \mathbb{P}^2$ (under suitable conditions), choosing a basis $Q_1, Q_2$ for $S_2(P_1, \dots, P_4)$ gives 2 conics $C_1, C_2$ such that $C_1 \cap C_2 = \{P_1, \dots, P_4\}$.

### Degenerate conics in a pencil

> [!INFO] Definition
> A pencil of conics is a family of the form
> $$ C_{(\lambda, \mu)} : (\lambda Q_1 + \mu Q_2 = 0); $$
> each element is a plane curve, depending in a linear way on the parameters $(\lambda, \mu)$.

$C_{(\lambda, \mu)}$ is degenerate $\iff \det(\lambda Q_1 + \mu Q_2) = 0$.
The condition is a homogeneous cubic form in $\lambda, \mu$.

> [!TIP] Proposition
> Suppose $C_{(\lambda, \mu)}$ is a pencil of conics of $\mathbb{P}^2$, with at least one nondegenerate conic. Then the pencil has at most 3 degenerate conics. If $k = \mathbb{R}$ then the pencil has at least one degenerate conic.

## Worked example

Let $P_1, \dots, P_4$ be 4 points of $\mathbb{P}^2$ such that no 3 are collinear; then the pencil of conics $C_{(\lambda, \mu)}$ through $P_1, \dots, P_4$ has 3 degenerate elements, namely the line pairs $L_{12} + L_{34}, L_{13} + L_{24}, L_{14} + L_{23}$.

Example: $Q_1 = Y^2 + rY + sX + t$ and $Q_2 = Y - X^2$ (parabola). Intersection gives roots of quartic.
The 3 degenerate conics correspond to the auxiliary cubic of the quartic.

## Exercises to Chapter 1

1. Parametrise the conic $C : x^2 + y^2 = 5$ by considering a variable line through $(2, 1)$ and hence find all rational solutions.
2. Let $p$ be a prime; by experimenting with various $p$, guess a necessary and sufficient condition for $x^2 + y^2 = p$ to have rational solutions.
3. Prove that an affine transformation can be used to put any conic of $\mathbb{R}^2$ into one of the standard forms.
4. Make a detailed comparison of the affine conics with the projective conics.
5. Let $k$ be any field of characteristic $\neq 2$. Show that if a nondegenerate quadratic form has a zero, it represents everything.
6. Deduce that a nonempty, nondegenerate conic $C \subset \mathbb{P}^2$ is projectively equivalent to $(XZ = Y^2)$.
7. Let $k$ be a field with at least 4 elements. Prove that if $Q$ vanishes on $C : (XZ = Y^2)$ then $Q = \lambda(XZ - Y^2)$.
8. Perspective: In $\mathbb{R}^3$, consider planes $A : (Z = 1)$ and $B : (X = 1)$. Consider the map $\phi : A \to B$ defined by projection from the origin. What is the image of lines, parallel lines, circles?
9. Coordinate system uniqueness: Prove that there is a unique coordinate system in which 4 points (no 3 collinear) are $(1, 0, 0), (0, 1, 0), (0, 0, 1)$ and $(1, 1, 1)$.
10. Intersection types: Write down equations for different intersection types of two conics (e.g. 3P+Q, 4P).
11. Sylvester’s determinant: Resultant of quadratic and cubic forms.
