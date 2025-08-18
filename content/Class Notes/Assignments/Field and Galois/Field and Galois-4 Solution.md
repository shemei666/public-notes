---
title: draft note
draft: true
---
1. Let $E = \mathbb{Q}(\sqrt{ 2 },\sqrt{3  },\dots,\sqrt{ p_{k} },\dots )$ p a prime. Prove that $E /Q$ is not a finite extension. Let $L \subseteq E$ be a finite subextension of $\mathbb{Q}$. Prove that $[L:\mathbb{Q}]=2^{r}$ for some $r\geq 1$.

We prove that $[\mathbb{Q}(\sqrt{ 2 },\sqrt{ 3 },\dots,\sqrt{ p_{k} }):\mathbb{Q}(\sqrt{ 2 },\sqrt{ 3 },\dots,\sqrt{ p_{k} })(\sqrt{ p_{k+1} })] =2$ for every k.
We assume this to be true for all $k\leq n$. Now for $k=n+1$, we have a 2 degree polynomial with root $\sqrt{ p }$ in $\mathbb{Q}[x]$ for all p. Hence we assume for contradiction that,
$$
\mathbb{Q}(\sqrt{ 2 },\sqrt{ 3 },\dots,\sqrt{ p_{n} })(\sqrt{ p_{n+1} }) = \mathbb{Q}(\sqrt{ 2 },\sqrt{ 3 },\dots,\sqrt{ p_{n} }))
$$
We know that the basis of the LHS are the products $P = \{ \sqrt{ p_{\alpha_{1}}p_{\alpha_{2}}\dots p_{\alpha_{m}}} \}$. Hence the above equality would imply:
$$
\sqrt{ p_{n+1} } = \sum_{b \in P}^{} a_{b}b \tag{1}
$$
$$
\implies p_{n+1} = \left( \sum_{b \in P}^{} a_{b}b \right)^{2} \tag{2}
$$
Clearly on the right hand side on (1) we have basis elements that are not 1. Hence on (2) there will be basis elements that are not 1. Hence we have a linear combination of basis elements of $\mathbb{Q}(\sqrt{ 2 },\sqrt{ 3 },\dots,\sqrt{ p_{n} })$  which is 0. This is a contradiction.

2. Let R be an integral domain containing a field $k$. Assume, with the natural scalar action of $k$ on R, $\dim_{k} R < \infty$. Prove that R is a field.
Let $\dim R = b$. Consider any element $a$ of $R$ which is not 0. Then we have that $1,a,a^{2},a^{3},\dots ,a^{n}$ are linearly dependent over k and non-zero, hence we have that there exists $c_{0},c_{1},\dots,c_{n} \in k$, not all zero, such that:
$$
c_{0} + c_{1}a + c_{2}a^{2} + \dots + c_{n}a^{n} = 0
$$
WLOG we can assume that $c_{0} \neq 0$. Hence we have:
$$
a(c_{1} + c_{2}a + \dots + c_{n}a^{n-1})c_{0}^{-1} = 1 
$$
Hence a has an inverse. 

3. Let $K_1,K_2$ be subfields of a field $K$, both containing a field $k$. Assume $\gcd([K_{1}:k],[K_{2}:k]) = 1$. Prove that $[K_{1}K_{2}:k]=[K_{1}:k][K_{2}:k]$
We show this by constructing a basis for $K_{1}K_{2}$ that is 

4. Let k be a field and $k(X)$ be the function field in 1-variable. Let $k \subsetneq L \subseteq k(X)$  be a subextension. Prove that $k(X)$ is algebraic over L.

5. Let $f_{1}(X),\dots,f_{m}(X) \in k[X]$. Prove that $\exists$ a finite extension L of k where all the $f_{i}$ have a root. Hence or otherwise prove that $\exists$ a field $E /K$, $[E:K]<\infty$, splitting all the $f_{i}$ simultaneously.

6. Call a field extension $K /k$ simple if $K = k(\alpha )$ for some $\alpha \in K$. Suppose $K$ is a finite extension of k and that the set $\{ L \subseteq K| L \text{ a subextension of } k\}$ is totally ordered with $\subseteq$. Prove $K /k$ is simple.

7. Prove that $\mathbb{\overline{Q}} := \{\alpha \in \mathbb{C}|\alpha  \text{ is algebraic over } \mathbb{Q}\}$ is algebraically closed.
8. Prove that a field extension $K / k$ is algebraic if and only if every ring $R$ such that $k \subseteq R \subseteq K$ is a field.
9. Prove that $\mathbb{\overline{Q}}$ is countable. This proves $\mathbb{R}$ is a transcendental extension of $\mathbb{Q}$ same for $\mathbb{C} /\mathbb{Q}$
10. Is it possible to have a finite field $\mathbb{F}$ that is algebraically closed? Explain.
11. Let $K = k(\alpha )$ be finite extension with $[k(\alpha):k]$ odd. Prove $K = k(\alpha^{2} )$
12. For every $n \in \mathbb{N}$, $\exists$ an extension $L /\mathbb{Q}$ with $[L:\mathbb{Q}] = n$.
13. Let $K = \mathbb{Q}(\alpha_{1},\dots,\alpha_{n})$ with $\alpha_{i}^{2} \in \mathbb{Q}, 1\leq i\leq n$ . Can $2^{\frac{1}{3}} \in K$ ? Explain.
14. Let k be a field, $\text{char}(k) \neq 2$. Let $\alpha,\beta \in k\setminus \{ 0 \}$ but both $\alpha,\beta \not\in k^{2}$. Prove that $k(\sqrt{ \alpha },\sqrt{ \beta })$ is of degree 4 over k if $\alpha \beta$ is not a square in k and is of degree 2 otherwise.
15. Let k be a field; $\alpha$ algebraic over k. Let $L_{\alpha}:k(\alpha ) \to k(\alpha )$ be the map $L_{\alpha } = \alpha x, \forall x \in k(\alpha )$. Clearly $L_{\alpha }$ is k-linear. Prove that $\det(xI-L_{\alpha }) = \text{Irr}(\alpha,k)$

