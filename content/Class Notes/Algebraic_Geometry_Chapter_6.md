---
title: Chapter 6 - Tangent space and nonsingularity, dimension
tags: [Algebraic Geometry, Tangent Space, Nonsingularity, Dimension, Blowup]
---

# Chapter 6: Tangent space and nonsingularity, dimension

## 6.1 Nonsingular points of a hypersurface

Suppose $f \in k[X_1, \dots, X_n]$ is irreducible, $f \notin k$, and set $V = V(f) \subset \mathbb{A}^n$; let $P = (a_1, \dots, a_n) \in V$, and $l$ be a line through $P$. Since $P \in V$, obviously $P$ is a root of $f|_l$.

**Question:** When is $P$ a multiple root of $f|_l$?

**Answer:** If and only if $l$ is contained in the affine linear subspace
$$ T_P V : \sum \frac{\partial f}{\partial X_i}(P) \cdot (X_i - a_i) = 0 \subset \mathbb{A}^n, $$
called the **tangent space** to $V$ at $P$.

To prove this, parametrise $l$ as
$$ l : X_i = a_i + b_i T, $$
where $P = (a_1, \dots, a_n)$ and $(b_1, \dots, b_n)$ is the slope or direction vector of $l$. Then $f|_l = f(\dots, a_i + b_i T, \dots) = g(T)$ is a polynomial in $T$, and we know that $(T = 0)$ is one root of $g$. Hence
$$ 0 \text{ is a multiple root of } g \iff \frac{\partial g}{\partial T}(0) = 0, $$
that is,
$$ \iff \sum b_i \frac{\partial f}{\partial X_i}(P) = 0 \iff l \subset T_P V. $$

> [!INFO] Definition
> $P \in V \subset \mathbb{A}^n$ is a **nonsingular point** of $V$ if $\frac{\partial f}{\partial X_i}(P) \neq 0$ for some $i$; otherwise $P$ is a **singular point**, or a **singularity** of $V$.

Obviously $T_P V$ is an $(n-1)$-dimensional affine subspace of $\mathbb{A}^n$ if $P$ is nonsingular, and $T_P V = \mathbb{A}^n$ if $P \in V$ is singular.

## 6.2 Remarks

(a) The derivatives $\frac{\partial f}{\partial X_i}(P)$ appearing above are formal algebraic operations (that is, $\frac{\partial}{\partial X_i}$ takes $X_i^n$ into $n X_i^{n-1}$); no calculus is involved.

(b) Suppose $k = \mathbb{R}$ or $\mathbb{C}$, and that $\frac{\partial f}{\partial X_i}(P) \neq 0$; for clarity let me take $i=1$. Then the map $p : \mathbb{A}^n \to \mathbb{A}^n$ defined by $(X_1, \dots, X_n) \mapsto (f, X_2, \dots, X_n)$ has nonvanishing Jacobian determinant at $P$, so that by the inverse function theorem, there exists a neighbourhood $P \in U \subset \mathbb{A}^n$ such that $p|_U : U \to p(U) \subset \mathbb{A}^n$ is a diffeomorphism of the neighbourhood $U$ with an open set $p(U)$ of $\mathbb{A}^n$ (in the usual topology of $\mathbb{R}^n$ or $\mathbb{C}^n$); that is, $p|_U$ is bijective, and both $p$ and $p^{-1}$ are differentiable functions of real or complex variables. In other words, $(f, X_2, \dots, X_n)$ form a new differentiable coordinate system on $\mathbb{A}^n$ near $P$; this implies that a neighbourhood of $P$ in $V : (f=0)$ is diffeomorphic to an open set in $\mathbb{A}^{n-1}$ with coordinates $(X_2, \dots, X_n)$. Thus near a nonsingular point $P$, $V$ is a **manifold** with $(X_2, \dots, X_n)$ as local parameters.

## 6.3 Proposition: $V_{nonsing}$ is dense

> [!TIP] Proposition
> $V_{nonsing} = \{ P \in V \mid P \text{ is nonsingular} \}$ is a dense open set of $V$ for the Zariski topology.

**Proof**: The complement of $V_{nonsing}$ is the set $V_{sing}$ of singular points, which is defined by $\frac{\partial f}{\partial X_i}(P) = 0$ for all $i$, that is
$$ V_{sing} = V(f, \frac{\partial f}{\partial X_1}, \dots, \frac{\partial f}{\partial X_n}) \subset \mathbb{A}^n, $$
which is closed by definition of the Zariski topology. Since $V$ is irreducible (by (3.11, a)), to show that the open $V_{nonsing}$ is dense, I only have to show it's nonempty (by Proposition 4.2); arguing by contradiction, suppose that it's empty, that is, suppose $V = V(f) = V_{sing}$. Then each of the polynomials $\frac{\partial f}{\partial X_i}$ must vanish on $V$, therefore (by (3.11) once more) they must be divisible by $f$ in $k[X_1, \dots, X_n]$; but viewed as a polynomial in $X_i$, $\frac{\partial f}{\partial X_i}$ has degree strictly smaller than $f$, so that $f$ divides $\frac{\partial f}{\partial X_i}$ implies that in fact $\frac{\partial f}{\partial X_i} = 0$ as a polynomial. Over $\mathbb{C}$, this is obviously only possible if $X_i$ does not appear in $f$, and if this happens for all $i$ then $f = \text{const.} \in \mathbb{C}$, which is excluded. Over a general field $k$, $\frac{\partial f}{\partial X_i} = 0$ is only possible if $f$ is an inseparable polynomial in $X_i$, that is, char $k = p$, and $X_i$ only appears in $f$ as the $p$th power $X_i^p$. If this happens for each $i$, then by the argument given in (3.16), $f$ is a $p$th power in $k[X_1, \dots, X_n]$; this contradicts the fact that $f$ is irreducible. Q.E.D.

## 6.4 Tangent space

> [!INFO] Definition
> Let $V \subset \mathbb{A}^n$ be a subvariety, with $P = (a_1, \dots, a_n) \in V$. For any $f \in k[X_1, \dots, X_n]$, write
> $$ f^{(1)}_P = \sum \frac{\partial f}{\partial X_i}(P) \cdot (X_i - a_i). $$
> This is an affine linear polynomial (that is, linear plus constant), the 'first order part' of $f$ at $P$. Now define the **tangent space** to $V$ at $P$ by
> $$ T_P V = \bigcap_{f \in I(V)} \{ f^{(1)}_P = 0 \} \subset \mathbb{A}^n, $$

## 6.5 Proposition: dim $T_P V$ is upper semicontinuous

> [!TIP] Proposition
> The function $V \to \mathbb{N}$ defined by $P \mapsto \dim T_P V$ is an upper semicontinuous function (in the Zariski topology of $V$). In other words, for any integer $r$, the subset
> $$ S(r) = \{ P \in V \mid \dim T_P V \ge r \} \subset V $$
> is closed.

**Proof**: Let $(f_1, \dots, f_m)$ be a set of generators of $I(V)$; it is easy to see that for any $g \in I(V)$, the linear part $g^{(1)}_P$ of $g$ is a linear combination of those of the $f_i$, so that the definition of $T_P V$ simplifies to
$$ T_P V = \bigcap_{i=1}^m \{ f^{(1)}_{i,P} = 0 \} \subset \mathbb{A}^n. $$
Then by elementary linear algebra,
$$ P \in S(r) \iff \text{the matrix } \left( \frac{\partial f_i}{\partial X_j}(P) \right)_{\substack{i=1,\dots,m \\ j=1,\dots,n}} \text{ has rank } \le n-r $$
$$ \iff \text{every } (n-r+1) \times (n-r+1) \text{ minor vanishes.} $$
Now each entry $\frac{\partial f_i}{\partial X_j}(P)$ of the matrix is a polynomial function of $P$; thus each minor is a determinant of a matrix of polynomials, and so is itself a polynomial. Hence $S(r) \subset V \subset \mathbb{A}^n$ is an algebraic subset. Q.E.D.

## 6.6 Corollary-Definition: Dimension and Nonsingularity

> [!INFO] Corollary-Definition
> There exists an integer $r$ and a dense open subset $V_0 \subset V$ such that
> $\dim T_P V = r$ for $P \in V_0$, and $\dim T_P V \ge r$ for all $P \in V$.
>
> Define $r$ to be the **dimension** of $V$, and write $\dim V = r$; and say that $P \in V$ is **nonsingular** if $\dim T_P V = r$, and **singular** if $\dim T_P V > r$. A variety $V$ is **nonsingular** if it is nonsingular at each point $P \in V$.

**Proof**: Let $r = \min \{ \dim T_P V \}$, taken over all points $P \in V$. Then clearly
$$ S(r-1) = \emptyset, \quad S(r) = V, \quad \text{and} \quad S(r+1) \subsetneq V; $$
therefore $S(r) \setminus S(r+1) = \{ P \in V \mid \dim T_P V = r \}$ is open and nonempty. Q.E.D.

## 6.7 dim $V$ = tr deg $k(V)$ -- the hypersurface case

It follows from Proposition 6.3 that if $V = V(f) \subset \mathbb{A}^n$ is a hypersurface defined by some nonconstant polynomial $f$, then $\dim V = n-1$. On the other hand, for a hypersurface, $k[V] = k[X_1, \dots, X_n]/(f)$, so that, assuming that $f$ involves $X_1$ in a nontrivial way, the function field of $V$ is of the form
$$ k(V) = k(X_2, \dots, X_n)[X_1]/(f), $$
that is, it is built up from $k$ by adjoining $n-1$ algebraically independent elements, then making a primitive algebraic extension.

> [!INFO] Definition
> If $k \subset K$ is a field extension, the **transcendence degree** of $K$ over $k$ is the maximum number of elements of $K$ algebraically independent over $k$. It is denoted $\text{tr deg}_k K$.

The elementary theory of transcendence degree of a field extension $K/k$ is formally quite similar to that of the dimension of a vector space: given $\alpha_1, \dots, \alpha_m \in K$, we know what it means for them to be **algebraically independent** over $k$ (see (3.13)); they **span** the transcendental part of the extension if $K/k(\alpha_1, \dots, \alpha_m)$ is algebraic; and they form a **transcendence basis** if they are algebraically independent and span. Then it is an easy theorem that a transcendence basis is a maximal algebraically independent set, and a minimal spanning set, and that any two transcendence bases of $K/k$ have the same number of elements (see Ex. 6.1).

Thus for a hypersurface $V \subset \mathbb{A}^n$, $\dim V = n-1 = \text{tr deg}_k k(V)$. The rest of this section is concerned with proving that the equality $\dim V = \text{tr deg}_k k(V)$ holds for all varieties, by reducing to the case of a hypersurface. The first thing to show is that for a point $P \in V$ of a variety, the tangent space $T_P V$, which so far has been discussed in terms of a particular coordinate system in the ambient space $\mathbb{A}^n$, is in fact an intrinsic property of a neighbourhood of $P \in V$.

## 6.8 Intrinsic nature of $T_P V$

From now on, given $P = (a_1, \dots, a_n) \in V \subset \mathbb{A}^n$, I take new coordinates $X_i' = X_i - a_i$ to bring $P$ to the origin, and thus assume that $P = (0, \dots, 0)$. Then $T_P V \subset \mathbb{A}^n$ is a vector subspace of $k^n$.

**Notation**: Write $m_P$ = ideal of $P$ in $k[V]$, and
$$ M_P = \text{the ideal } (X_1, \dots, X_n) \subset k[X_1, \dots, X_n]. $$
Then of course $m_P = M_P / I(V) \subset k[V]$.

> [!TIP] Theorem
> In the above notation,
> (a) there is a natural isomorphism of vector spaces
> $$ (T_P V)^* \cong m_P / m_P^2, $$
> where $( )^*$ denotes the dual of a vector space.
> (b) If $f \in k[V]$ is such that $f(P) \neq 0$, and $V_f \subset V$ is the standard affine open as in (4.13), then the natural map
> $$ T_P(V_f) \to T_P V $$
> is an isomorphism.

**Proof of (a)**: Write $(k^n)^*$ for the vector space of linear forms on $k^n$; this is the vector space with basis $X_1, \dots, X_n$. Since $P = (0, \dots, 0)$, for any $f \in k[X_1, \dots, X_n]$, the linear part $f_P^{(1)}$ is naturally an element of $(k^n)^*$; define a map $d : M_P \to (k^n)^*$ by taking $f \in M_P$ into $df = f_P^{(1)}$.

Now $d$ is surjective, since the $X_i \in M_P$ go into the natural basis of $(k^n)^*$; also $\ker d = M_P^2$, since
$$ f_P^{(1)} = 0 \iff f \text{ starts with quadratic terms in } X_1, \dots, X_n $$
$$ \iff f \in M_P^2. $$
Hence $M_P / M_P^2 \cong (k^n)^*$. This is statement (a) for the special case $V = \mathbb{A}^n$. In the general case, dual to the inclusion $T_P V \subset k^n$, there is a restriction map $(k^n)^* \to (T_P V)^*$, taking a linear form $\lambda$ on $k^n$ into its restriction to $T_P V$; composing then defines a map
$$ D : M_P \xrightarrow{d} (k^n)^* \to (T_P V)^*. $$
The composite $D$ is surjective since each factor is. I claim that the kernel of $D$ is just $M_P^2 + I(V)$, so that
$$ m_P / m_P^2 = M_P / (M_P^2 + I(V)) \cong (T_P V)^*, $$
as required. To prove the claim,
$$ f \in \ker D \iff f_P^{(1)}|_{T_P V} = 0 $$
$$ \iff f_P^{(1)} = \sum a_i g_{i,P}^{(1)} \text{ for some } g_i \in I(V) $$
(since $T_P V \subset k^n$ is the vector subspace defined by $(g_P^{(1)} = 0)$ for $g \in I(V)$)
$$ \iff f - \sum a_i g_i \in M_P^2 \text{ for some } g_i \in I(V) \iff f \in M_P^2 + I(V). $$
The proof of (b) of Theorem 6.8 is left to the reader (see Ex. 6.2). Q.E.D.

> [!TIP] Corollary 6.9
> $T_P V$ only depends on a neighbourhood of $P \in V$ up to isomorphism. More precisely, if $P \in V_0 \subset V$ and $Q \in W_0 \subset W$ are open subsets of affine varieties, and $\phi : V_0 \to W_0$ an isomorphism taking $P$ into $Q$, there is a natural isomorphism $T_P V_0 \cong T_Q W_0$; hence $\dim T_P V_0 = \dim T_Q W_0$.
>
> In particular, if $V$ and $W$ are birationally equivalent varieties then $\dim V = \dim W$.

**Proof**: By passing to a smaller neighbourhood of $P$ in $V$, I can assume $V_0$ is isomorphic to an affine variety (Proposition 4.13). Then so is $W_0$, and $\phi$ induces an isomorphism $k[V_0] \cong k[W_0]$ taking $m_P$ into $m_Q$. The final sentence holds because by (5.8), $V$ and $W$ contain dense open subsets which are isomorphic.

> [!TIP] Theorem 6.10
> For any variety $V$, $\dim V = \text{tr deg}_k k(V)$.

**Proof**: This is known if $V$ is a hypersurface. On the other hand, every variety is birational to a hypersurface (by (5.10)), and both sides of the required relation are the same for birationally equivalent varieties. Q.E.D.

## 6.11 Nonsingularity and projective varieties

Although the above results were discussed in terms of affine varieties, the idea of nonsingularity and of dimension applies directly to any variety $V$: a point $P \in V$ is nonsingular if it is a nonsingular point of an affine open $V_0 \subset V$ containing it; by Corollary 6.9, this notion does not depend on the choice of $V_0$. On the other hand, for a projective variety $V \subset \mathbb{P}^n$, it is sometimes useful to consider the tangent space to $V$ at $P$ as a projective subspace of $\mathbb{P}^n$. I give the definition for a hypersurface only: if $V = V(f)$ is a hypersurface defined by a form (= homogeneous polynomial) $f \in k[X_0, \dots, X_n]$ of degree $d$, and $V \ni P = (a_0, \dots, a_n)$, then $\sum \frac{\partial f}{\partial X_i}(P) \cdot X_i = 0$ is the equation of a hyperplane in $\mathbb{P}^n$ which plays the role of the tangent plane to $V$ at $P$. If $P \in \mathbb{A}^n \cong U_0$, then this projective hyperplane is the projective closure of the affine tangent hyperplane to $V \cap U_0$ at $P$, as can be checked easily using Euler's formula:
$$ \sum X_i \cdot \frac{\partial f}{\partial X_i} = d f \quad \text{for } f \in k[X_0, \dots, X_n] \text{ homogeneous of degree } d. $$
Because of this formula, to find out whether a point $P \in \mathbb{P}^n$ is a singular point of $V$, we only have to check $(n + 1)$ out of the $(n + 2)$ conditions
$$ f(P) = 0, \quad \frac{\partial f}{\partial X_i}(P) = 0 \text{ for } i = 0, \dots, n, $$
so that for example, if the degree of $f$ is not divisible by char $k$,
$$ \frac{\partial f}{\partial X_i}(P) = 0 \text{ for } i = 0, \dots, n \implies f(P) = 0, $$
and $P \in V$ is a singularity.

## 6.12 Worked example: blowup

Let $B = \mathbb{A}^2$ with coordinates $(u, v)$, and $\sigma : B \to \mathbb{A}^2$ the map $(u, v) \mapsto (x = u, y = uv)$; clearly, $\sigma$ is a birational morphism: it contracts the $v$-axis $l : (u = 0)$ to the origin $0$ and is an isomorphism outside this exceptional set. Let's find out what happens under $\sigma$ to a curve $C : (f = 0) \subset \mathbb{A}^2$; the question will only be of interest if $C$ passes through $0$.

Clearly $\sigma^{-1}(C) \subset B$ is the algebraic subset defined by $(f \circ \sigma)(u, v) = f(u, uv) = 0$; since $0 \in C$ by assumption, it follows that $l : (u = 0)$ is contained in $\sigma^{-1}(C)$, or equivalently, that $u \mid f(u, uv)$. It's easy to see that the highest power $u^m$ of $u$ dividing $f(u, uv)$ is equal to the smallest degree $m = a + b$ of the monomials $x^a y^b$ occurring in $f$, that is, the **multiplicity** of $f$ at $0$; so $\sigma^{-1}(C)$ decomposes as the union of the exceptional curve $\sigma^{-1}(0) = l$ (with multiplicity $m$), together with a new curve $C_1$ defined by $f_1(u, v) = f(u, uv) / u^m$. Consider the examples

(a) $f = \alpha x - y + \dots$;
(b) $f = y^2 - x^2 + \dots$;
(c) $f = y^2 - x^3$,
where $\dots$ denotes terms of higher degree. Clearly in (a) $f$ has multiplicity 1, and $f_1 = \alpha - v + \dots$ (where $\dots$ consists of terms divisible by $u$), so $C_1$ is again nonsingular, and meets $l$ transversally at $(0, \alpha)$; thus $\sigma$ replaces $0 \in \mathbb{A}^2$ with the line $l$ whose points correspond to tangent directions at $0$ (excluding $(x=0)$). In (b) $f_1 = v^2 - 1 + \dots$, so $C_1$ has two nonsingular points $(0, \pm 1)$ above $0 \in C$; thus the blowup $\sigma$ 'separates the two branches' of the singular curve $C$. In (c) $f_1 = v^2 - u$, so that $C_1$ is nonsingular, but above $0$ it is tangent to the contracted curve $l$.

In either case (b) or (c), $\sigma$ replaces a singular curve $C$ by a nonsingular one $C_1$ birational to $C$ (by introducing 'new coordinates' $u=x, v=y/x$). This is what is meant by a **resolution of singularities**. In the case of plane curves, a resolution can always be obtained by a chain of blowups (see Ex. 6.6 for examples, and [Fulton, pp. 162–171] for more details), and the process of resolution gives detailed information about the singularities. A famous theorem of H. Hironaka guarantees the possibility of resolving singularities by blowups (in any dimension, over a field of characteristic zero). This is a crucial theoretical result that reduces the birational study of varieties to nonsingular ones; however, the actual process of resolution by blowups is in general extremely complicated, and does not necessarily contribute very much to the understanding of the singularities or varieties concerned.

## Exercises to Chapter 6

1.  Let $k \subset K$ be a field extension, and $(u_1, \dots, u_r)$, $(v_1, \dots, v_s)$ two sets of elements of $K$; suppose that $(u_1, \dots, u_r)$ are algebraically independent, and that $(v_1, \dots, v_s)$ span the extension $k \subset K$ algebraically. Prove that $r \le s$. [Hint: the inductive step consists of assuming that $(u_1, \dots, u_i, v_{i+1}, \dots, v_s)$ span $K/k$ algebraically, and considering $u_{i+1}$.] Deduce that any two transcendence bases of $K/k$ have the same number of elements.

2.  Prove Theorem 6.8, (b). [Hint: $I(V_f) = (I(V), Y f - 1) \subset k[X_1, \dots, X_n, Y]$, so that if $Q = (a_1, \dots, a_n, b) \in V_f$, then $T_Q V_f \subset \mathbb{A}^{n+1}$ is defined by the equations for $T_P V \subset \mathbb{A}^n$, together with one equation involving $Y$.]

3.  Determine all the singular points of the following curves in $\mathbb{A}^2$.
    a. $y^2 = x^3 - x$;
    b. $y^2 = x^3 - 6x^2 + 9x$;
    c. $x^2 y^2 + x^2 + y^2 + 2xy(x + y + 1) = 0$;
    d. $x^2 = x^4 + y^4$;
    e. $xy = x^6 + y^6$;
    f. $x^3 = y^2 + x^4 + y^4$;
    g. $x^2 y + x y^2 = x^4 + y^4$.

4.  Find all the singular points of the surfaces in $\mathbb{A}^3$ given by
    a. $xy^2 = z^2$;
    b. $x^2 + y^2 = z^2$;
    c. $xy + x^3 + y^3 = 0$.
    (You will find it useful to sketch the real parts of the surfaces, to the limits of your ability; algebraic geometers usually can't draw.)

5.  Show that the hypersurface $V_d \subset \mathbb{P}^n$ defined by
    $$ X_0^d + X_1^d + \dots + X_n^d = 0 $$
    is nonsingular (if char $k$ does not divide $d$).

6.  (a) Let $C_n \subset \mathbb{A}^2$ be the curve given by $f_n : y^2 = x^{2n+1}$ and $\sigma : B \to \mathbb{A}^2$ be as in (6.12), with $l = \sigma^{-1}(0)$; show that $\sigma^{-1}(C_n)$ decomposes as the union of $l$ together with a curve isomorphic to $C_{n-1}$. Deduce that $C_n$ can be resolved by a chain of $n$ blowups.
    (b) Show how to resolve the following curve singularities by making one or more blowups:
    i. $y^3 = x^4$;
    ii. $y^3 = x^5$;
    iii. $(y^2 - x^2)(y^2 - x^5) = x^8$.

7.  Prove that the intersection of a hypersurface $V \subset \mathbb{A}^n$ (not a hyperplane) with the tangent hyperplane $T_P V$ is singular at $P$.
