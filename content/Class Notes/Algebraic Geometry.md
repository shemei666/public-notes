---
publish: false
---

**(2.5) Lemma.** Suppose that $k$ is an infinite field, and let $F \in S_d$.
(i) Let $L \subset \mathbb{P}^2_k$ be a line; if $F \equiv 0$ on $L$, then $F$ is divisible in $k[X, Y, Z]$ by the equation of $L$. That is, $F = H \cdot F'$ where $H$ is the equation of $L$ and $F' \in S_{d-1}$.
(ii) Let $C \subset \mathbb{P}^2_k$ be a non-empty non-degenerate conic; if $F \equiv 0$ on $C$, then $F$ is divisible in $k[X, Y, Z]$ by the equation of $C$. That is, $F = Q \cdot F'$ where $Q$ is the equation of $C$ and $F' \in S_{d-2}$.

**Theorem (Mordell-Weil).** Let $K$ be a number field and let $E$ be an elliptic curve defined over $K$. The group of $K$-rational points $E(K)$ is a finitely generated abelian group.
That is, $E(K) \cong \mathbb{Z}^r \oplus T$, where $r \ge 0$ is the rank and $T$ is the finite torsion subgroup.

## Assignments: Chapter 1

1.2, 1.5, 1.7, 1.8,1.10
## Nullstellensatz
**Theorem (Hilbert's Nullstellensatz).** Let $k$ be an algebraically closed field and $k[x_1, \dots, x_n] = A$.

1.  **Weak Nullstellensatz:** Every maximal ideal $\mathfrak{m} \subset A$ is of the form $\mathfrak{m} = (x_1 - a_1, \dots, x_n - a_n)$ for some point $(a_1, \dots, a_n) \in \mathbb{A}^n_k$.
2.  **Existence of Zeros:** If $J \subsetneq A$ is a proper ideal, then its vanishing set is non-empty, i.e., $\mathcal{V}(J) \neq \emptyset$.
3.  **Strong Nullstellensatz:** For any ideal $I \subseteq A$, the ideal of its vanishing set is the radical of the ideal: $\mathcal{I}(\mathcal{V}(I)) = \sqrt{I}$.

**Lemma:** let $k$ be a infinite field, $A$ an f.g $k$-algebra Then $A$ is a field $\iff$ $A$ is algebraic over $k$

**Proof of Theorem:** Let $m$ be a max ideal, $K = k[x_{1},\dots,x_{n}] / m$ ,$K$ is a field, since $k \hookrightarrow K$ $\implies K$ is algebraic over $k$. but $k = \overline{k}$ $\implies k = K$
Let $b_{i} =$ image of $X_{i}$ under the map, #todo

**Def:(Finite algebra)** If $A \subseteq B$, $B$ is said to be finitely generated if $\exists b_{1},\dots,b_{n} \in B = A[b_{1},\dots,b_{n}]$, $B$ is said to be finite over $A$ if $B = Ab_{1}+\dots+Ab_{n}$
**Eg:** $A[X]$ is f.g but not finite.

**Proposition:**

1. If $A \subseteq B \subseteq C$ , $B$ a finite $A$-algebra $C$ a finite $B$-algebra $\implies  C$ is a finite $A$-algebra
2. If $A \subseteq B$, $B$ finite $A$-algebra $x \in B \implies x$ satisfies a monic polynomial over $A$
   $$
   x^{n} + a_{n-1}x^{n-1} + \dots + a_{0} = 0
   $$
3. If $x$ satisfies a monic poly over $A$ then $A[x]$ is a finite $A$-algebra.
   **Proof:**

4. $C = \sum_{j=1}^m B c_j = \sum_{j=1}^m (\sum_{i=1}^n A b_i) c_j = \sum_{i,j} A b_i c_j$.
5. Let $B = \sum A b_i$. The map $m_x: B \to B$ defined by $m_x(b) = xb$ is $A$-linear. By the Cayley-Hamilton theorem, $m_x$ satisfies its characteristic polynomial $P(T) = \det(TI - [m_x])$, which is monic in $A[T]$.
6. If $x^n + a_{n-1}x^{n-1} + \dots + a_0 = 0$ with $a_i \in A$, then $x^n \in \sum_{i=0}^{n-1} A x^i$. By induction, $x^m \in \sum_{i=0}^{n-1} A x^i$ for all $m \ge n$.

**Theorem (Noether Normalization).** Let $k$ be a field and $A$ be a finitely generated $k$-algebra. Then there exists a subring $S = k[y_1, \dots, y_d] \subseteq A$ such that $y_1, \dots, y_d$ are algebraically independent over $k$ and $A$ is a finite $S$-algebra.

**Proof:**
Let $A = k[a_1, \dots, a_n]$.
$I = \text{Ker } k[X_1, \dots, X_n] \to A$.
Let $f \in I$, $f \neq 0$.

**Claim:** We can replace $X_1, \dots, X_{n-1}$ by $X'_1, \dots, X'_{n-1}$ such that $f$ is monic in $X_n$ over $k[X'_1, \dots, X'_{n-1}]$.
(Note: $A' = k[a'_1, \dots, a'_n]$).

Let $a'_i = a_i - \alpha_i a_n$ for some $\alpha_i$'s to be chosen later.
Then $a_i = a'_i + \alpha_i a_n$.

**Claim:** For a suitable choice of $\alpha$, $f(X'_1 + \alpha_1 X_n, \dots, X'_{n-1} + \alpha_{n-1} X_n, X_n)$ is monic in $X_n$.

**Proof of Claim:**
Let $d = \deg(f)$. We can write $f = f_d + f_{d-1} + \dots + f_0$, where $f_j$ is the homogeneous component of degree $j$.
Substituting $X_i = X'_i + \alpha_i X_n$ for $i < n$, the term of highest degree in $X_n$ comes from $f_d$.

$$
f_d(X'_1 + \alpha_1 X_n, \dots, X'_{n-1} + \alpha_{n-1} X_n, X_n) = f_d(\alpha_1, \dots, \alpha_{n-1}, 1)X_n^d + (\text{terms of lower degree in } X_n)
$$

Since $k$ is infinite, we can choose $\alpha_1, \dots, \alpha_{n-1} \in k$ such that $f_d(\alpha_1, \dots, \alpha_{n-1}, 1) \neq 0$. Dividing by this leading coefficient, we get a polynomial monic in $X_n$.
**Proof by induction on $n$.**
If $I=0$, then $A$ is a polynomial ring, so result holds (take $y_i = x_i$).

If $f \neq 0 \in I$, then by claim:

- $f$ gives a monic polynomial satisfied by $a_n$ over $A' = k[a'_1, \dots, a'_{n-1}]$.
- By induction $\exists y_1, \dots, y_m$ ($m \le n-1$) such that $A'$ is finite over $S = k[y_1, \dots, y_m]$ and $y_1, \dots, y_m$ are algebraically independent.

But $A = A'[a_n]$.
$A$ is finite over $A'$ (since $a_n$ is integral over $A'$), and $A'$ is finite over $S$.
$\implies A$ is finite over $S$.

**Proof of Lemma:**

---

Let $k$ be a field, If $V \subseteq \mathbb{A}^{n}_{k}$ is an algebraic set $V = V(I)$ and $I(V)$ is its ideal, then

$$
k[X_{1},\dots,X_{n}] / I(V) = k[V]
$$

is called the coordinate ring of $V$, A polynomial function $f: V\to k$ is a function given by $P \to F(P)$ where $F \in k[X_{1},\dots,X_{n}]$ is a poly

So $k[V] =$ ring of polynomial function on $V$. Smallest ring of function contrary the coordinate function $X_{1},\dots,X_{n}$

---

$X \subseteq \mathbb{A}^{n}$ is an algebraic set $X \subseteq V$, $\implies I(X) \supset I(V)$ and if $I \subset J$ then $V(J) \subseteq V = V(I)$

$$
\{  \text{Ideals I} \subset J \} \leftrightarrow \{ \text{Ideal of } k[V] \}
$$

**Proposition:** LEt $V$ be an algerbaic subset of $\mathbb{A}^{n}$
The following are equivalent

1. $V$ is irreducible
2. Any two non empy open subsets has nonempty intersection
3. Any nonempty open set is dense
   **Proof:**

A polynomial map $V \subseteq \mathbb{ A}^{n}, W \subseteq \mathbb{A}^{m}$

$$
f: V \to W
$$

is a map given by $F_{1},\dots,F_{m}$ poly in $k[X_{1},..,X^{n}]$

$$
 p \to f(p) = (F_{1}(p),\dots,F_m(p))
$$

$f$ is said to be an isomorphism if $\exists g$ such that $f \circ g = g \circ f = Id$

An irreducible algebraic set is called an Affine variety.
**Example:**

$$
\begin{align}
C: Y ^{2} = X^{3} \\
X = t^{2} \\
Y = t^{3} \\
\mathbb{A}^{1} \to C \subseteq \mathbb{A}^{2}
\end{align}
$$

**Theorem:** $V \subseteq \mathbb{A}^{n}, W \subseteq \mathbb{A}^{m}$

1. A poly map $f: V\to W$ induces a ring homomorphism $f^{*}: k[W]\to k[V]$
2. If $\varphi : k[W]\to k[V]$ is a ring hom, then $\varphi = f^{*}$ for some $f:V\to W$
3. $f:V\to W$, $g:W \to U$

```tikz
\usepackage{tikz-cd}
\begin{document}
\begin{tikzcd}
k[U] \arrow[r, "g^*"] \arrow[dr, "{(g \circ f)^*}"'] & k[W] \arrow[d, "f^*"] \\
& k[V]
\end{tikzcd}
\end{document}
```

Thus $(g \circ f)^* = f^* \circ g^*$.

**Proof Sketch:**

1.  **$f \implies f^*$**: Define $f^*(h) = h \circ f$. Since composition preserves algebraic operations (addition, multiplication), $f^*$ is valid ring homomorphism.
2.  **$\phi \implies f$**: Let $Y_1, \dots, Y_m$ be coordinate functions on $W$. Set $F_i = \phi(Y_i) \in k[V]$. Define $f: V \to \mathbb{A}^m$ by $p \mapsto (F_1(p), \dots, F_m(p))$. One can verify $f(V) \subseteq W$ and induced map is $\phi$.
3.  **Functoriality**: $(g \circ f)^*(h) = h \circ (g \circ f) = (h \circ g) \circ f = f^*(h \circ g) = f^*(g^*(h))$.

**Proof:** $f: V\to W$, $f^{*}: k[W]\to k[V]$, If $g \in k[W]$, we have

$$

f^{*}(g)(p) = g(f(p))

$$

$\phi :k[W] \to k[V]$ is a homomorphism #todo 

**Corollary:** $f:V\to W$ is an isomorphism $\iff$ $f ^{*}: k[W]\to k[V]$ is an isomorphism.
**Proof:**

---
$k[V]$ is an invariant of the isomorphism class of an affine variety. An affine variety over a field $k$ is a set $V$ along with a ring $k[V]$ of $k$-valued function of $k[V]$ is an f.g $k$-algebra, For some choice of $x_{1},\dots,x_{n}$ generatoes of $k[V] /k$ embeds $V$ as an irreducible algebraic set.

## Function Fields
If $V$ is an affine variety $\implies I(V)$ is aprime ideal $\implies$ $k[V] = k[X_{1},\dots,X_{n}] / I(V)$ is a domain, The **Function field** of $V$ is the quotient ffield of $k[V]$
$$
k(V) =  \left\{  \frac{f}{g} \mid f,g \in k[V] , g \neq 0  \right\}
$$

$f = \frac{g}{h}$ is called a rational "function since it is not a function on all of $V$, If $h(p) =0$ it is not defined

Let $f \in k(V), P \in V$, we say $f$ is regular at $p$ if  $\exists g,h$ such that $f = \frac{g}{h}$ and $h(p)\neq 0$

- The domain of  definitions of $f$
$$
dom(f) = \{  P \mid f \text{is regualr at } P\} 
$$
$$
\begin{align}
O_{V,P} = &  \{  f \in k(V) \mid f \text{ is regular at } P\} = S^{-1}k[V] \\
S = &  \{  h \in k[V] \mid h(p) \neq 0 \} \\
m_{p} = &  \{  h \mid h(p) = 0 \} \text{ is a max ideal}
\end{align}
$$
**Theorem:** 
1. $dom(f)$ is open and dense
2. If $k = \overline{k}$
$$
dom (f) = V \iff f \in k[V]
$$
3. Let $V_{h} = V - V(h) = \{  p \mid h(p) \neq 0 \}$
$$
dom(f) \supseteq V_{h} \iff f \in k[V][h^{-1}]
$$
$$
\begin{align}
D_{f}  & = \{  h \in k[V] \mid hf \in k[V]\} \\
 & = \left\{   h \in k[V] \mid f = \frac{g}{h} , g \in k[V]  \right\} \cup  \{  0 \}
\end{align}
$$

**Proof:** 
$D_{f}$ is an ideal $V- dom(f)= V(D_{f})$, so $dom(f)$ is open and dense,  since $V$ is irreducible)

$$
dom(f) = V \iff V(D_{f}) = \varnothing
$$
By **[[Algebraic Geometry#Nullstellensatz|Nullstellensatz]]** $V(D_{f}) = \varnothing \iff 1 \in D_{f}$
$$
\iff  1_{f} \in k[V] \iff f \in k[V]
$$


2.(1,2,3,7,8,10,11,12(read,no write))