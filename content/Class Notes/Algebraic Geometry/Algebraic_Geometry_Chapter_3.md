---
title: Chapter 3 - Affine Varieties and the Nullstellensatz
tags:
---

# Chapter 3: Affine Varieties and the Nullstellensatz

Much of the first half of this section is pure commutative algebra; note that throughout these notes, ring means a commutative ring with a 1.

## Definition of Noetherian ring

> [!TIP] Proposition-Definition
> The following conditions on a ring $A$ are equivalent:
> (i) Every ideal $I \subset A$ is finitely generated; that is, for every ideal $I \subset A$, there exist $f_1, \dots, f_k \in I$ such that $I = (f_1, \dots, f_k)$.
> (ii) Every ascending chain $I_1 \subset \dots \subset I_m \subset \dots$ of ideals of $A$ terminates (the ascending chain condition, or a.c.c.).
> (iii) Every nonempty set of ideals of $A$ has a maximal element.
>
> If they hold, $A$ is a **Noetherian ring**.

> [!TIP] Proposition 3.2
> (i) Suppose that $A$ is Noetherian, and $I \subset A$ an ideal; then the quotient ring $B = A/I$ is Noetherian.
> (ii) Let $A$ be a Noetherian integral domain, and $K$ its field of fractions; let $0 \notin S \subset A$ be a subset, and set $B = A[S^{-1}]$. Then $B$ is again Noetherian.

> [!TIP] Theorem 3.3 (Hilbert Basis Theorem)
> For a ring $A$,
> $A$ Noetherian $\implies A[X]$ Noetherian.

> [!TIP] Corollary
> For $k$ a field, a finitely generated $k$-algebra is Noetherian.

## The correspondence $V$

$k$ is any field, and $A = k[X_1, \dots, X_n]$. I write $\mathbb{A}^n = k^n$ for the $n$-dimensional affine space over $k$.
Define a correspondence
$$ \{ \text{ideals } J \subset A \} \to \{ \text{subsets } X \subset \mathbb{A}^n \} $$
by
$$ J \mapsto V(J) = \{ P \in \mathbb{A}^n \mid f(P) = 0 \quad \forall f \in J \}. $$

> [!INFO] Definition
> A subset $X \subset \mathbb{A}^n$ is an **algebraic set** if $X = V(I)$ for some $I$.
> Since $A$ is Noetherian, $I = (f_1, \dots, f_r)$, so $V(I) = \{ P \mid f_i(P) = 0 \text{ for } i=1,\dots,r \}$.

### Definition: the Zariski topology

> [!TIP] Proposition-Definition
> The correspondence $V$ satisfies:
> (i) $V(0) = \mathbb{A}^n$; $V(A) = \emptyset$;
> (ii) $I \subset J \implies V(I) \supset V(J)$;
> (iii) $V(I_1 \cap I_2) = V(I_1) \cup V(I_2)$;
> (iv) $V(\sum_{\lambda \in \Lambda} I_\lambda) = \bigcap_{\lambda \in \Lambda} V(I_\lambda)$.
>
> Hence the algebraic subsets of $\mathbb{A}^n$ form the closed sets of a topology on $\mathbb{A}^n$, the **Zariski topology**.

The Zariski topology induces a topology on any algebraic set $X \subset \mathbb{A}^n$.

## The correspondence $I$

As a kind of inverse to $V$ there is a correspondence
$$ \{ \text{subsets } X \subset \mathbb{A}^n \} \to \{ \text{ideals } J \subset A \} $$
by
$$ X \mapsto I(X) = \{ f \in k[V] \mid f(P) = 0 \quad \forall P \in X \}. $$

> [!TIP] Proposition
> (a) $X \subset Y \implies I(X) \supset I(Y)$;
> (b) $X \subset V(I(X))$, with equality if and only if $X$ is an algebraic set;
> (c) $J \subset I(V(J))$; the inclusion may well be strict.

## Irreducible algebraic set

An algebraic set $X \subset \mathbb{A}^n$ is **irreducible** if there does not exist a decomposition $X = X_1 \cup X_2$ with $X_1, X_2 \subsetneq X$ strictly.

> [!TIP] Proposition
> (a) Let $X \subset \mathbb{A}^n$ be an algebraic set. Then $X$ is irreducible $\iff I(X)$ is prime.
> (b) Any algebraic set $X$ has a (unique) expression
> $$ X = X_1 \cup \dots \cup X_r $$
> with $X_i$ irreducible and $X_i \not\subset X_j$ for $i \neq j$.
> The $X_i$ are the **irreducible components** of $X$.

## Preparation for the Nullstellensatz

> [!IMPORTANT] Hard Fact
> Let $k$ be a (infinite) field, and $A = k[a_1, \dots, a_n]$ a finitely generated $k$-algebra. Then
> $A$ is a field $\implies A$ is algebraic over $k$.

### Definition: radical ideal

> [!INFO] Definition
> If $I$ is an ideal of $A$, the **radical** of $I$ is
> $$ \text{rad } I = \sqrt{I} = \{ f \in A \mid f^n \in I \text{ for some } n \}. $$
> An ideal $I$ is **radical** if $I = \text{rad } I$. Note that a prime ideal is radical.

> [!TIP] Nullstellensatz 3.10 (Hilbert’s zeros theorem)
> Let $k$ be an algebraically closed field.
> (a) Every maximal ideal of the polynomial ring $A = k[X_1, \dots, X_n]$ is of the form $m_P = (X_1 - a_1, \dots, X_n - a_n)$ for some point $P = (a_1, \dots, a_n) \in \mathbb{A}^n$; that is, it’s the ideal $I(P)$.
> (b) Let $J \subset A$ be an ideal, $J \neq (1)$; then $V(J) \neq \emptyset$.
> (c) For any $J \subset A$, $I(V(J)) = \text{rad } J$.

> [!TIP] Corollary
> The correspondences $V$ and $I$ induce bijections
> $$ \{ \text{radical ideals} \} \leftrightarrow \{ \text{algebraic subsets} \} $$
> and
> $$ \{ \text{prime ideals} \} \leftrightarrow \{ \text{irreducible alg. subsets} \}. $$

> [!NOTE]- Proof of NSS
> (a) Uses "Hard Fact": $K = k[X_1, \dots, X_n]/m$ is a field and f.g. k-algebra $\implies K=k$ since $k$ is alg. closed.
> (b) Follows from (a).
> (c) Requires "Rabinowitsch trick": introduce variable $Y$ and ideal $J_1 = (J, fY - 1)$. If $f$ vanishes on $V(J)$, then $V(J_1) = \emptyset$, so $1 \in J_1$, which implies $f^N \in J$.

## Worked examples

### Hypersurfaces
$V(f) : (f = 0) \subset \mathbb{A}^n$. If $k$ is alg. closed, irreducible $f$ corresponds to irreducible hypersurface.

### Curve in $\mathbb{A}^3$
$J = (uw - v^2, u^3 - vw)$.
$V(J) = V(J, u) \cup V(J, w^2 - u^2v)$.
$V(J, u)$ is the w-axis.
The other component $C$ is given by $uw = v^2, u^3 = vw, w^2 = u^2v$.
This is the image of $t \mapsto (t^3, t^4, t^5)$.

## Finite algebras

$B$ is a **finite $A$-algebra** if $B$ is finitely generated as $A$-module (linear combinations).
Contrast with **finitely generated $A$-algebra** (polynomial expressions).

> [!TIP] Proposition
> (i) $A \subset B \subset C$. $B$ finite over $A$, $C$ finite over $B \implies C$ finite over $A$.
> (ii) If $A \subset B$ is finite $A$-algebra and $x \in B$, then $x$ satisfies a monic equation over $A$.
> (iii) Conversely, if $x$ satisfies a monic equation, $A[x]$ is finite over $A$.

## Noether normalisation

> [!TIP] Theorem (Noether normalisation lemma)
> Let $k$ be an infinite field, and $A = k[a_1, \dots, a_n]$ a finitely generated $k$-algebra. Then there exist $m \le n$ and $y_1, \dots, y_m \in A$ such that
> (i) $y_1, \dots, y_m$ are algebraically independent over $k$;
> (ii) $A$ is a finite $k[y_1, \dots, y_m]$-algebra.

Geometric interpretation: finite projection to $\mathbb{A}^m$.

## Proof of (3.8)
Lemma: If $A$ is a field, and $B \subset A$ a subring such that $A$ is a finite $B$-algebra, then $B$ is a field.
Proof uses finiteness to show inverses exist in $B$.

## Separable addendum
If $k$ is algebraically closed and $A$ integral domain, can choose $y_i$ such that extension is separable.

## Reduction to a hypersurface

> [!TIP] Theorem (Primitive element theorem)
> Let $K$ be an infinite field, and $L$ a finite separable field extension; then $L = K(x)$ for some $x$.

> [!TIP] Corollary
> Under Noether Normalisation hypotheses, field of fractions $K$ of $A$ is generated over $k$ by $y_1, \dots, y_{m+1}$.
> i.e. $K = k(y_1, \dots, y_{m+1})$ with one relation. Geometrically, birational to a hypersurface.

## Exercises to Chapter 3
1. Show PID implies ACC.
2. UFD criteria.
3. Gauss's lemma and UFD for polynomial rings.
4. Localisation is Noetherian.
5. Analyze $J = (XY, XZ, YZ)$.
6. $I(V(J)) \setminus J$ examples.
7. Uniqueness of irreducible components.
8. Component examples.
9. Variety in $\mathbb{A}^1$ is finite or all.
10. $V(f, g)$ in $\mathbb{A}^2$ is finite if $f, g$ coprime.
11. $V(f) \neq \mathbb{A}^n$ if $f$ nonconstant.
12. Failure of Noether Normalisation over finite field.
13. Nakayama's Lemma simple case.
14. Geometric interpretation of fibers of projection.
