# Miscellaneous Problems

1. Let $\alpha$ be a rational root of a monic polynomial in $\mathbb{Z}[x]$. Prove that $\alpha \in \mathbb{Z}$.

2. **Biquadratic extensions:** Let $k$ be a field, $\operatorname{char}(k) \neq 2$. Let $D_1, D_2 \in k$, neither a square. Prove that
   $$
   [k(\sqrt{D_1}, \sqrt{D_2}) : k] = 4 \quad \text{if } D_1, D_2 \text{ is not a square in } k
   $$
   and $= 2$ if otherwise. We call $k(\sqrt{D_1}, \sqrt{D_2})$ biquadratic in the first case.

3. A field $F$ is **formally real** if $-1$ is not a sum of squares in $F$. Let $F$ be formally real, $f(x) \in F[x]$ irreducible of odd degree, $\alpha$ a root of $f(x)$. Prove that $F(\alpha)$ is formally real.

4. Let $K_1, K_2$ be two finite extensions of a field $k$. We make $K_1 \otimes_k K_2$ a $k$-algebra by the unique product such that $(x_1 \otimes y_1) \cdot (x_2 \otimes y_2) = (x_1 x_2) \otimes (y_1 y_2)$. Prove that $K_1 \otimes_k K_2$ is a field $\iff [K_1 K_2 : k] = [K_1 : k][K_2 : k]$.

5. For any prime $p$, the polynomial $x^p - x - 1 \in \mathbb{F}_p[x]$ is irreducible. Find
   $$
   [\text{Split}(f(x); \mathbb{F}_p) : \mathbb{F}_p]
   $$
   where $\text{Split}(f(x); \mathbb{F}_p)$ is the splitting field of $f(x)$ over $\mathbb{F}_p$.

---

6. Let $p$ be a prime and $f(x_1, \ldots, x_n) \in \mathbb{Z}[x_1, \ldots, x_n]$. Prove that the polynomial
   $$
   g(x_1, \ldots, x_n) := f(x_1, \ldots, x_n)^p - f(x_1^p, \ldots, x_n^p)
   $$
   has all its coefficients divisible by $p$.

7. Find a primitive element for $\mathbb{Q}(\sqrt{2}, \sqrt{3}, \sqrt{5})/\mathbb{Q}$.

8. Let $F$ be a field contained in $M_n(k)$, where $k$ is a field. Assume $k \subseteq F$. Can you say something about $[F : k] =\; ?$

9. Let $K_1, K_2$ be algebraic extensions of a field $F$; $K_1, K_2$ both $\subseteq L$, $\operatorname{char}(L) = 0$. Prove that the $F$-algebra $K_1 \otimes_F K_2$ has no nonzero nilpotents. (Use (10) below).

10. Let $F \subseteq K \subseteq L$ be fields, $\theta \in L$ and $p(x) = \operatorname{Irr}(\theta; F)$. Prove that
    $$
    K \otimes_F F(\theta) \cong \frac{K[x]}{\langle p(x) \rangle}
    $$
    as $K$-algebras.

11. Let $q = p^n$, $p$ a prime. Let $\varphi_p : \mathbb{F}_q \to \mathbb{F}_q$ be the Frobenius automorphism $\alpha \mapsto \alpha^p$. Consider $\varphi_p$ as a linear transformation: $\mathbb{F}_q \to \mathbb{F}_q$ over $\mathbb{F}_p$. Prove: $\varphi_p$ is diagonalizable over $\mathbb{F}_p \iff n \mid (p-1)$ and diagonalizable over $\overline{\mathbb{F}}_p \iff \gcd(n, p) = 1$.