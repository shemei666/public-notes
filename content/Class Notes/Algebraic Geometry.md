---
publish: true
---

**(2.5) Lemma.** Suppose that $k$ is an infinite field, and let $F \in S_d$.
(i) Let $L \subset \mathbb{P}^2_k$ be a line; if $F \equiv 0$ on $L$, then $F$ is divisible in $k[X, Y, Z]$ by the equation of $L$. That is, $F = H \cdot F'$ where $H$ is the equation of $L$ and $F' \in S_{d-1}$.
(ii) Let $C \subset \mathbb{P}^2_k$ be a non-empty non-degenerate conic; if $F \equiv 0$ on $C$, then $F$ is divisible in $k[X, Y, Z]$ by the equation of $C$. That is, $F = Q \cdot F'$ where $Q$ is the equation of $C$ and $F' \in S_{d-2}$.

**Theorem (Mordell-Weil).** Let $K$ be a number field and let $E$ be an elliptic curve defined over $K$. The group of $K$-rational points $E(K)$ is a finitely generated abelian group.
That is, $E(K) \cong \mathbb{Z}^r \oplus T$, where $r \ge 0$ is the rank and $T$ is the finite torsion subgroup.

## Assignments: Chapter 1

1.2, 1.5, 1.7, 1.8,1.10

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
