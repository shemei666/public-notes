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

**Proof:** Let $m$ be a max ideal, $K = k[x_{1},\dots,x_{n}] / m$ ,$K$ is a field, since $k \hookrightarrow K$ $\implies K$ is algebraic over $k$. but $k = \overline{k}$ $\implies k = K$ 
Let $b_{i} =$ image of $X_{i}$ under the map