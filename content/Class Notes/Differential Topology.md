**Theorem:(Embedding Theorem)** For an injective immersion $f:X\to Y$, TFAE

1. $f(X)$ is a submanifold of Y of dimension $\dim(X)$
2. The continuous bijection $X \to f(X)$ is a diffeomorphism.
3. The continuous bijection $X \to f(X)$ is a homeomorphism.
4. $\exists$ an open subset $Y' \subseteq Y$ containing $f(X)$ such that $X \to Y'$ is proper locally on $Y'$. Thus $f(X)$ is a closed subset of $Y'$
   **Proof:**  
   $2 \implies 1, 3$ is obvious,
   $1 \implies 2$: $X \to f(X)$ is a bijective immersion of manifolds of same dimension, hence a local diffeomorphism, which is a diffeomorphism
   $4 \implies 3$ Since $X\to Y'$ is locally proper, it is closed map, hence the same is true for the bijection $X\to f(X)$. Thus $X \to f(X)$ is a homeomorphism
   $3\implies 2,4$ we need the following claim:
   **Claim:** Under the hypothesis of $3$ around any $y=f(x) ,\exists$ an open subset $Y_{1} \subseteq Y$ such that for $X_{1}=f^{-1}(Y_{1})$ we have a commutative diagram

```tikz
\usepackage{tikz-cd}
\begin{document}
\begin{tikzcd}
X_1 \arrow[r, "f"] \arrow[d, "\phi"] & Y_1 \arrow[d, "\psi"] \\
U \arrow[r, "i"] & U \times V
\end{tikzcd}
\end{document}
```

where $\phi: X_1 \cong U \subseteq \mathbb{R}^{\dim X}$ and $\psi: Y_1 \cong U \times V \subseteq \mathbb{R}^{\dim Y}$ are charts such that $\psi \circ f \circ \phi^{-1} = i$, with $i(u) = (u, 0)$.

Assuming this claim, we see that $2$ holds as $U$ diffeomorphic to its image in $V \implies  X_{1} \xrightarrow{\sim } Y_{1}$ Since $X_{1} = f^{-1} f(X_{1})$, we see that $X\to f(X)$ is a bijective local diffeomorphism, hence $2$.
Similarly we see that **Claim** $\implies 4$. #todo 

**Def:** A map of manifolds $f:X\to Y$ is called an embedding if it is an injective immersion satisfying above equivalent conditions,

Thus $f:X\to Y$ embedding $\implies X \cong f(X)$ diffeo. and $f(X)$ is a locally closed subset of $Y$.

We call $Z \subseteq Y$ a locally closed set if $Z=$ intersection of a closed set and open set in $Y$. 

If $X$ is a submanifold of $Y$, then $X \hookrightarrow Y$ is an embedding. If $X$ is compact and $f:X\to Y$ is an injective immersion, then f is an embedding.