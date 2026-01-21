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

**Def:** We call $Z \subseteq Y$ a locally closed set if $Z=$ intersection of a closed set and open set in $Y$.

If $X$ is a submanifold of $Y$, then $X \hookrightarrow Y$ is an embedding. If $X$ is compact and $f:X\to Y$ is an injective immersion, then f is an embedding.

**Corollary to Lemma:** Let $X \subseteq Y$ be a submanifold with $\dim X =k,\dim Y =l$ Then for any point $p \in X$, $\exists$ a nbd $Y_{1} \subseteq Y$ such that $X \cap Y_{1}$ is given by the vanishing of $l-k$ functions from $l$ coordinate functions around $p$.
**Proof:** Use the bottom row of key lemma to define coordinate functions there $U$ is given by the $l-k$ coordinates functions for $W$

_suggested exercises:_ 3.9,3.10

**Theorem:(Local Submersion Theorem)** Let $f:X\to Y$ be a submersion at $x \in X$ Then, local coordinates around $x$, $y=f(x)$, $f$ is a canonical submersion.

**Proof:** Pick local coordinates around $x,y$ in $X,Y$

```tikz
\usepackage{tikz-cd}
\usepackage{amssymb}
\begin{document}
\begin{tikzcd}
X \arrow[r,"f"] & Y\\
U_1 \subseteq \mathbb{R}^{k} \arrow[u,"\varphi"] \arrow[r,"g"] & V_1 \subseteq \mathbb{R}^{l}\arrow[u,"\psi"]
\end{tikzcd}
\end{document}
```

Since $f$ is a submersion at $x$, $g$ is a submersion at $0$, i.e $dg_{0}$ is an onto map $\mathbb{R}^{k} \twoheadrightarrow \mathbb{R}^{l}.$ WLOG by change of coords,

$$
dg_{0} = \begin{pmatrix}
I_{l\times l} | 0
\end{pmatrix}
$$

Define a smooth function $U \xrightarrow{G} V_{1} \times \mathbb{R}^{k-l}$ by $G(x_{1},\dots,x_{k}) := (\underbrace{g_{1},\dots,g_l},x_{l+1},\dots,x_{k})$

Clearly $G$ is smooth and $dG_{0} = \begin{bmatrix}I & 0 \\ 0  & I\end{bmatrix}$ and thus, by Inverse function theorem, $G$ is a local diffeo. around $0 \in U_{1}$, By shrinking we get open nbd $U \subseteq U_{1}$ of 0 such that $G(U)$ is of the form $V\times W$ for open sets $V \subseteq V_{1}$, $W \subseteq \mathbb{R}^{k-l}$ Now we have coordinate nbd.

```tikz
\usepackage{tikz-cd}
\usepackage{amsmath}
\usepackage{amssymb}
\begin{document}
\begin{tikzcd}
X \ar[r,"f"] & Y \\
V \times W \ar[u,"\phi \circ G^{-1}"] \ar[r,"\text{std proj.}"] & V \ar[u,"\psi"]
\end{tikzcd}
\end{document}
```

Note that the composite $U \xrightarrow{G} V \times W \xrightarrow{\text{std proj}} V$ is $g$

**Corollary:** If $f:X\to Y$ is a submersion at $x$, then it is also one in an open nbd of $x$, moreover $f(X)$ contains an open nbd of $f(x)$ in $Y$. In particular if $f$ is a submersion everywhere then $f$ is an open map.
**Proof:** Follows from the above diagram.

**Corollary:** If $f:X\to Y$ is a submersion, then with $y =f(x)$, the set $f^{-1}(y)\subseteq X$ is a $k-l$ manifold around $x$, i.e $\exists$ an open nbd around $x$ in X over which it is given by vanishing of $l$ coordinate functions.
**Proof:** As before, in local coordinates, the coordinates functions on $V$ pull back to give $l$ coordinate functions on $V\times W$ whose vanishing gives $0 \times W \subseteq V \times W$

**Def:** Let $f:X \to  Y$  be a smooth map of manifolds, then $y \in Y$ is a regular value of $f$ if $\forall x \in f^{-1}(y), df_{x}$ onto. If $y \in Y$ is not a regular value, we call it a critical value of $f$.

**Theorem:(Pre-Image Theorem)** If $y \in Y$ is a regular value of $f$, then $f^{-1}(y)$ is either empty or a manifold of dimension $\dim(X)-\dim(Y)$.

If $y$ is a critical value, $f^{-1}(y)$ may or may not be a manifold.

**Examples:** 
1. **Sphere in $\mathbb{R}^{n+1}$** $f:\mathbb{R}^{n+1}\to \mathbb{R}$ smooth function, given by $x \mapsto \lvert x \rvert^{2}$, then $df$ at $p=(a_{1},\dots,a_{n+1})$ is given by $T_{p}\mathbb{R}^{n+1} = \mathbb{R}^{n+1} \xrightarrow{[2a_{1},\dots,2a_{n+1}]} \mathbb{R}$ which is submersion iff it is non zero. i.e if it is not $a_{1}=\dots=a_{n+1} =0$, Thus $c \in \mathbb{R}$ is regular iff $c\neq 0$. Since $c<0,f^{-1}(c) = \varnothing, c>0, f^{-1}(c)$ is a sphere.
2. More generally, for any smooth function $f:U\to \mathbb{R}$, $U \subseteq  \mathbb{R}^{n}$ $df$ determines whether $f$ is a submersion at $p \in U$, namely iff $df_{p} \neq 0$.
3. $f:\mathbb{R}^{2}\to \mathbb{R}$ $f(x,y)= x^{2}-y^{2}$, $df = (2x,-2y)$. So it fails to be a submersion at $p=(0,0)$.
4. Bad examples: $f = (x^{2}+y^{2}-1)^{2}$, On $S^{1}$, $df = 0$, Here $0$ is a critical value for $f$ but $f^{-1}(0)$ is  $S^{1}$ which is a manifold.

Let us work with more functions: Consider a map $U\subseteq \mathbb{R}^{k}\to \mathbb{R}^{l}$ or more generally, $X \xrightarrow{g}\mathbb{R}^{l}$ where $X$ is a manifold. If $0 \in \mathbb{R}^{l}$ is a regular value of $g$, then $g^{-1}(0)$ is a manifold in $X$ of dimension $k-l$.

**Linear algebra lemma:** Let $V \xrightarrow{\phi}\mathbb{R}^{l}$ be a linear map with $\phi = (\phi_{1},\dots,\phi_{l})$, $\phi_{i} \in V^{*}$. Then $\phi$ is onto $\iff$ $\phi_{1},\dots,\phi_{l}$ are linearly independent in $V^{*}$.

$$
c_{1}\phi_{1} + \dots+c_{l}\phi_{l} = 0 \implies \phi(v) \in (c_{1},\dots,c_{l})^{\perp } \subset neq
$$

