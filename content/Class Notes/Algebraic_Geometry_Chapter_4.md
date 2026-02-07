---
title: Chapter 4 - Functions on Varieties
tags: [Algebraic Geometry, Functions, Morphisms, Rational Maps]
---

# Chapter 4: Functions on Varieties

In this section I work over a fixed field $k$; from (4.8, II) onwards, $k$ will be assumed to be algebraically closed. The reader who assumes throughout that $k = \mathbb{C}$ will not lose much, and may gain a psychological crutch.

## Polynomial functions

Let $V \subset \mathbb{A}^n$ be an algebraic set, and $I(V)$ its ideal. Then the quotient ring
$$ k[V] = k[X_1, \dots, X_n]/I(V) $$
is in a natural way a ring of functions on $V$.
Define a **polynomial function** on $V$ to be a map $f : V \to k$ of the form $P \mapsto F(P)$, with $F \in k[X_1, \dots, X_n]$.
By definition of $I(V)$, two elements $F, G$ define the same function on $V$ if and only if $F - G \in I(V)$.
Thus the coordinate ring $k[V]$ is just the ring of polynomial functions on $V$.

### $k[V]$ and algebraic subsets of $V$

An algebraic set $X \subset \mathbb{A}^n$ is contained in $V$ if and only if $I(X) \supset I(V)$.
Ideals of $k[X_1, \dots, X_n]$ containing $I(V)$ are in bijection with ideals of $k[V]$.
Hence the $I$ and $V$ correspondences work for subsets of $V$ and ideals of $k[V]$.

> [!TIP] Proposition
> Let $V \subset \mathbb{A}^n$ be an algebraic subset. The following conditions are equivalent:
> (i) $V$ is irreducible;
> (ii) any two open subsets $\emptyset \neq U_1, U_2 \subset V$ have $U_1 \cap U_2 \neq \emptyset$;
> (iii) any nonempty open subset $U \subset V$ is dense.

## Polynomial maps

Let $V \subset \mathbb{A}^n$ and $W \subset \mathbb{A}^m$ be algebraic sets.

> [!INFO] Definition
> A map $f : V \to W$ is a **polynomial map** if there exist $m$ polynomials $F_1, \dots, F_m \in k[X_1, \dots, X_n]$ such that
> $$ f(P) = (F_1(P), \dots, F_m(P)) \in \mathbb{A}^m \quad \text{for all } P \in V. $$

A map $f$ is a polynomial map iff for all $j$, the composite map $f_j = Y_j \circ f \in k[V]$.

> [!INFO] Definition
> A polynomial map $f : V \to W$ is an **isomorphism** if there exists a polynomial map $g : W \to V$ such that $f \circ g = g \circ f = \text{id}$.

### Polynomial maps and $k[V]$

> [!TIP] Theorem
> Let $V \subset \mathbb{A}^n$ and $W \subset \mathbb{A}^m$ be algebraic sets.
> (I) A polynomial map $f : V \to W$ induces a ring homomorphism $f^* : k[W] \to k[V]$, defined by composition: $f^*(g) = g \circ f$.
> (II) Conversely, any $k$-algebra homomorphism $\Phi : k[W] \to k[V]$ is of the form $\Phi = f^*$ for a uniquely defined polynomial map $f : V \to W$.
> (III) $(g \circ f)^* = f^* \circ g^*$.

Thus there is a bijection between Polynomial Maps $V \to W$ and $k$-Algebra Homomorphisms $k[W] \to k[V]$.

> [!TIP] Corollary 4.5
> A polynomial map $f : V \to W$ is an isomorphism if and only if $f^* : k[W] \to k[V]$ is an isomorphism.

## Affine variety

> [!INFO] Definition
> An **affine variety** over a field $k$ is a set $V$, together with a ring $k[V]$ of $k$-valued functions such that:
> (a) $k[V]$ is a finitely generated $k$-algebra, and
> (b) generators embed $V$ as an irreducible algebraic set.

(This intrinsic definition is slightly pedantic; usually we work with embedded varieties).

## Function field

Let $V$ be an affine variety; $k[V]$ is an integral domain.

> [!INFO] Definition
> The **function field** $k(V)$ of $V$ is the field of fractions $k(V) = \text{Quot}(k[V])$. An element $f \in k(V)$ is a **rational function** on $V$.

$f = g/h$ is **regular** at $P \in V$ if there exists an expression $f = g/h$ with $h(P) \neq 0$.
Domain of definition: $\text{dom } f = \{ P \in V \mid f \text{ is regular at } P \}$.
Local ring at $P$: $\mathcal{O}_{V,P} = \{ f \in k(V) \mid f \text{ is regular at } P \}$.

> [!TIP] Theorem 4.8
> (I) $\text{dom } f$ is open and dense in the Zariski topology.
> Suppose $k$ is algebraically closed; then:
> (II) $\text{dom } f = V \iff f \in k[V]$ (polynomial function = regular rational function).
> (III) $\text{dom } f \supset V_h \iff f \in k[V][h^{-1}]$.
> where $V_h = V \setminus V(h)$.

## Rational maps

> [!INFO] Definition
> A **rational map** $f : V \dashrightarrow \mathbb{A}^n$ is a partially defined map given by rational functions $f_1, \dots, f_n$.
> Domain of definition is $\bigcap \text{dom } f_i$.

A rational map $V \dashrightarrow W$ is a rational map to $\mathbb{A}^m$ whose image lies in $W$.

### Composition of rational maps

Composition $g \circ f$ is defined if $f(\text{dom } f) \cap \text{dom } g \neq \emptyset$.

> [!INFO] Definition
> $f : V \dashrightarrow W$ is **dominant** if $f(\text{dom } f)$ is dense in $W$.
> Algebraically: $f$ is dominant $\iff f^* : k[W] \to k(V)$ is injective.

> [!TIP] Theorem 4.11
> (I) A dominant rational map $f : V \dashrightarrow W$ defines a field homomorphism $f^* : k(W) \to k(V)$.
> (II) Conversely, a $k$-homomorphism $k(W) \to k(V)$ comes from a unique dominant rational map.
> (III) $(g \circ f)^* = f^* \circ g^*$.

## Morphisms from an open subset

Let $U \subset V$ be an open subset.
A **morphism** $f : U \to W$ is a rational map $f : V \dashrightarrow W$ such that $U \subset \text{dom } f$.

### Standard open subsets
For $f \in k[V]$, $V_f = V \setminus V(f)$.
$V_f$ is isomorphic to an affine variety, and $k[V_f] = k[V][f^{-1}]$.
$V_f$ form a basis for the Zariski topology.

## Worked example
The group law on a cubic curve $C_0 : y^2 = x^3 + ax + b$ defines a rational map $\phi : C_0 \times C_0 \dashrightarrow C_0$.
It is a morphism wherever $A + B \neq O$.

## Exercises to Chapter 4
1. Validity of statements over any field.
2. $\phi : \mathbb{A}^1 \to \mathbb{A}^3$ by $t \mapsto (t, t^2, t^3)$.
3. $\phi_n : \mathbb{A}^1 \to \mathbb{A}^2$ by $t \mapsto (t^2, t^n)$.
4. Isomorphism of $X$ with subvariety of $Y$.
5. Parametrisation of $Y^2 = X^3$ and its inverse.
6. Domain of $g \circ f$.
7. Function $xy/(x^2+y^2)$ analogy.
8. Nodal curve parametrisation issues.
9. $Y^3 = X^4 + X^3$ parametrisation.
10. $XT = YZ$ in $\mathbb{A}^4$, $k[V]$ not UFD.
11. Composite not defined anywhere.
12. Product of algebraic sets $V \times W$.
13. Function on $\mathbb{A}^2 \setminus (0,0)$ not extending to affine plane.
