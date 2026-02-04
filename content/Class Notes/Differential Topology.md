---
publish: true
---
## Embeddings
**Theorem:(Embedding Theorem)** For an injective immersion $f:X\to Y$, TFAE

1. $f(X)$ is a submanifold of Y of dimension $\dim(X)$
2. The continuous bijection $X \to f(X)$ is a diffeomorphism.
3. The continuous bijection $X \to f(X)$ is a homeomorphism.
4. $\exists$ an open subset $Y' \subseteq Y$ containing $f(X)$ such that $X \to Y'$ is proper locally on $Y'$. Thus $f(X)$ is a closed subset of $Y'$
   **Proof:**  
   $2 \implies 1, 3$ is obvious,
   $1 \implies 2$: $X \to f(X)$ is a bijective immersion of manifolds of same dimension, hence a local diffeomorphism, which is a diffeomorphism
   $4 \implies 3$ Since $X\to Y'$ is locally proper, it is a closed map, hence the same is true for the bijection $X\to f(X)$. Thus $X \to f(X)$ is a homeomorphism
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

Thus if $f:X\to Y$ is an embedding $\implies X \cong f(X)$ is a diffeomorphism and $f(X)$ is a locally closed subset of $Y$.

**Def:** We call $Z \subseteq Y$ a locally closed set if $Z=$ intersection of a closed set and open set in $Y$.

If $X$ is a submanifold of $Y$, then $X \hookrightarrow Y$ is an embedding. If $X$ is compact and $f:X\to Y$ is an injective immersion, then f is an embedding.

**Corollary to Lemma:** Let $X \subseteq Y$ be a submanifold with $\dim X =k,\dim Y =l$ Then for any point $p \in X$, $\exists$ a nbd $Y_{1} \subseteq Y$ such that $X \cap Y_{1}$ is given by the vanishing of $l-k$ functions from $l$ coordinate functions around $p$.
**Proof:** Use the bottom row of Key Lemma to define coordinate functions there $U$ is given by the $l-k$ coordinates functions for $W$

_suggested exercises:_ 3.9,3.10

## Local Submersion Theorem
**Theorem:** Let $f:X\to Y$ be a submersion at $x \in X$ Then, in local coordinates around $x$, $y=f(x)$, $f$ is a canonical submersion.

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

Clearly $G$ is smooth and $dG_{0} = \begin{bmatrix}I & 0 \\ 0  & I\end{bmatrix}$ and thus, by Inverse function theorem, $G$ is a local diffeomorphism around $0 \in U_{1}$. By shrinking we get open neighborhood $U \subseteq U_{1}$ of 0 such that $G(U)$ is of the form $V\times W$ for open sets $V \subseteq V_{1}$, $W \subseteq \mathbb{R}^{k-l}$ Now we have coordinate neighborhood.

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

**Corollary:** If $f:X\to Y$ is a submersion at $x$, then it is also one in an open neighborhood of $x$, moreover $f(X)$ contains an open neighborhood of $f(x)$ in $Y$. In particular if $f$ is a submersion everywhere then $f$ is an open map.
**Proof:** Follows from the above diagram.

**Corollary:** If $f:X\to Y$ is a submersion, then with $y =f(x)$, the set $f^{-1}(y)\subseteq X$ is a $k-l$ manifold around $x$, i.e $\exists$ an open nbd around $x$ in X over which it is given by vanishing of $l$ coordinate functions.
**Proof:** As before, in local coordinates, the coordinates functions on $V$ pull back to give $l$ coordinate functions on $V\times W$ whose vanishing gives $0 \times W \subseteq V \times W$

## Regular Values and Pre-Image Theorem
**Def:** Let $f:X \to  Y$ be a smooth map of manifolds, then $y \in Y$ is a regular value of $f$ if $\forall x \in f^{-1}(y), df_{x}$ onto. If $y \in Y$ is not a regular value, we call it a critical value of $f$.

**Theorem:(Pre-Image Theorem)** If $y \in Y$ is a regular value of $f$, then $f^{-1}(y)$ is either empty or a manifold of dimension $\dim(X)-\dim(Y)$.

If $y$ is a critical value, $f^{-1}(y)$ may or may not be a manifold.

**Examples:**

1. **Sphere in $\mathbb{R}^{n+1}$** $f:\mathbb{R}^{n+1}\to \mathbb{R}$ smooth function, given by $x \mapsto \lvert x \rvert^{2}$, then $df$ at $p=(a_{1},\dots,a_{n+1})$ is given by $T_{p}\mathbb{R}^{n+1} = \mathbb{R}^{n+1} \xrightarrow{[2a_{1},\dots,2a_{n+1}]} \mathbb{R}$ which is a submersion iff it is non zero. i.e if it is not $a_{1}=\dots=a_{n+1} =0$, Thus $c \in \mathbb{R}$ is regular iff $c\neq 0$. Since $c<0,f^{-1}(c) = \varnothing, c>0, f^{-1}(c)$ is a sphere.
2. More generally, for any smooth function $f:U\to \mathbb{R}$, $U \subseteq  \mathbb{R}^{n}$ $df$ determines whether $f$ is a submersion at $p \in U$, namely iff $df_{p} \neq 0$.
3. $f:\mathbb{R}^{2}\to \mathbb{R}$ $f(x,y)= x^{2}-y^{2}$, $df = (2x,-2y)$. So it fails to be a submersion at $p=(0,0)$.
4. Bad examples: $f = (x^{2}+y^{2}-1)^{2}$, On $S^{1}$, $df = 0$, Here $0$ is a critical value for $f$ but $f^{-1}(0)$ is $S^{1}$ which is a manifold.

Let us work with more functions: Consider a map $U\subseteq \mathbb{R}^{k}\to \mathbb{R}^{l}$ or more generally, $X \xrightarrow{g}\mathbb{R}^{l}$ where $X$ is a manifold. If $0 \in \mathbb{R}^{l}$ is a regular value of $g$, then $g^{-1}(0)$ is a manifold in $X$ of dimension $k-l$.

**Linear algebra lemma:** Let $V \xrightarrow{\phi}\mathbb{R}^{l}$ be a linear map with $\phi = (\phi_{1},\dots,\phi_{l})$, $\phi_{i} \in V^{*}$. Then $\phi$ is onto $\iff$ $\phi_{1},\dots,\phi_{l}$ are linearly independent in $V^{*}$.
**Proof:**

$$
c_{1}\phi_{1} + \dots+c_{l}\phi_{l} = 0 \implies \phi(v) \in (c_{1},\dots,c_{l})^{\perp } \subsetneq \mathbb{R}^{l}
$$

Conversely, if $\phi$ is not onto, pick $c_{1},\dots,c_{l} \in im(\phi)^{\perp }$ , then $c_{1}\phi_{1}+\dots+c_{l}\phi_{l} =0$

---

Back to $g=(g_{1},\dots,g_{l}):X\to \mathbb{R}^{l}$, we say that $g_{1},\dots,g_{l}$ are independent functions at $x$ if $dg_{x}:T_{x}X\to T_{g(x)}\mathbb{R}^{l}=\mathbb{R}^{l}$ is onto, i.e. if $dg_{1_{x}},\dots,dg_{l_{x}}$ are linearly independent functions of $(T_{x}X)^{*}$.

**Proposition:** Let $g_{1},\dots,g_{l}:X\to \mathbb{R}$ be smooth functions. Pick a point in $\mathbb{R}$, say $0\in \mathbb{R}$ Set $Z:= \bigcap_{i=1}^{l} \{ g_{i}=0 \}$. If $Z$ is non-empty and $g_{i}$ are independent at each point of $Z$, then $Z$ is a manifold of dimension $\dim(X)-l$.

**Proof:** Use [[#Regular Values and Pre-Image Theorem|preimage theorem]] for $X \xrightarrow{ g} \mathbb{R}^{l}$, $g=(g_{1},\dots,g_{l})$ then $0$ is a regular value for $g$ and $Z=g^{-1}(0)$.

**Proposition:**

1. Let $f:X\to Y$ be a smooth map with $y \in Y$ a regular value. Then $f^{-1}(y)$ is the common zero set of independent functions around $f^{-1}(y)$.
2. Any submanifold $Z \subseteq X$ is locally the common zero set of $\text{codim}_{X}(Z)$ independent functions.

**Proof:**
![[1769503249938.jpg]]

1. We already saw this when proving [[#Regular Values and Pre-Image Theorem|Pre-Image Thm]]. Since the condition is local, it suffices to check in local coordinates (by [[#Local Submersion Theorem|Submersion Thm]]), where $f$ looks like a projection. Thus locally $f^{-1}(y)$ is given by the vanishing of some coordinate functions, which are independent.
2. This follows immediately from the corollary to the key lemma (slice chart). Recall that locally $Z \subseteq X$ is given, in standard coordinates, as the vanishing of coordinate functions. And coordinate functions are always independent.

## Tangent Spaces of Level Sets
**Proposition:** $f: X \to Y$ smooth, $y \in Y$ regular value of $f$, then for any $x \in Z:= f^{-1}(y)$, $T_{x}Z =$ kernel $df_{x}:T_{x}X \to T_{y}Y$

**Proof:**
![[IMG_20260127_142539.jpg]]
The composite $f \circ i$ is a constant map:

```tikz
\usepackage{tikz-cd}
\begin{document}
\begin{tikzcd}
Z \arrow[r, "i"] \arrow[dr, "const"'] & X \arrow[d, "f"] \\
& Y
\end{tikzcd}
\end{document}
```

$\therefore$ By chain rule, $d(f \circ i)_x = 0$, i.e., $df_x \circ di_x = 0$.
Since $di_x: T_x Z \to T_x X$ is an inclusion, we get $df_x(T_x Z) = 0$.
Thus $T_x Z \subseteq \ker(df_x)$.

Comparing dimensions, we see that equality holds:

$$
\dim(T_x Z) = \dim Z = \dim(X) - \dim(Y) \quad (\text{by Preimage Theorem})
$$

As $y$ is regular, $df_x$ is onto, so:

$$
\dim(\ker(df_x)) = \dim(X) - \dim(Y)
$$

$\therefore T_x Z = \ker(df_x)$.
Q.E.D.

![[IMG_20260127_143309.jpg]]

**Example:** The tangent space of a hypersurface or level surface $f(x_{1},\dots,x_{n})-c=0$ (if $c$ is a regular value of $f$) is $(\nabla f)^{\perp}$ at any point.

$$
T_{p}\mathbb{R}^{n} \xrightarrow{\nabla f} T_{c}\mathbb{R} \quad f(p)=c
$$

Let $M(n) = n \times n$ matrices over $\mathbb{R} = \mathbb{R}^{n^{2}}$ Euclidean space.
$\forall A \in M(n)$, $T_{A}(M(n))$ is also $\mathbb{R}^{n^{2}}$ and we identify with $M(n)$ in the same way.

Consider the polynomial map

$$
\begin{align}
M(n) \to M(n) \\
A \mapsto AA^{t}
\end{align}
$$

The image lies in the subspace $S(n)$ of all symmetric matrices. We also identify the tangent space at any point of $S(n)$ with $S(n) \subseteq M(n)$ again

$$
\begin{align}
f : M(n) \to S(n) \\
A \mapsto AA^{t}
\end{align}
$$

Let us calculate $df_{A}:T_{A}(M(n)) = M(n) \to S(n) = T(S(n))$

$$
\begin{align}

df_{A}(B) = \lim_{ s \to 0} \frac{1}{s} [f(A + sB) - f(A)] \\
= \lim_{ s \to 0 }  \frac{1}{s} [(A+sB)(A + sB)^{T} - AA^{T}] \\
= AB^{T} + BA^{T}
\end{align}
$$

This is clearly not onto for some choices of $A$ (e.g $A=0$), for $A$ invertible this is onto: for any $C \in S(n)$, we use $AB^{t} = \frac{c}{2} = BA^{t}$. Then we get $B = \frac{1}{2} C(At)^{-1}$. Thus we can solve for $B$,

Thus $f$ is a submersion over the dense open subset $GL(n)$ ( the set of all invertible matrices) in $M(n)$. ==It follows that the image $f$ contains an open subset of $S(n)$==.

For any $D \in S(n)$, if $D$ is invertible, then $D$ is a regular value of $f$, either $f^{-1}D$ is empty or if $A \in f^{-1}(D)$, then $\det(A) \neq 0$.
![[IMG_20260127_145606.jpg]]
Thus $f^{-1}(D)$ is either empty or a manifold of $n^{2} - \frac{n(n+1)}{2} = \frac{n(n-1)}{2}$.

Pick $D=I$ identity matrix. Then $f^{-1}I = O(n)$ the set of all orthogonal matrices.

For any $P \in O(n)$, we get $T_{P}(O(n)) = \ker(df_{P})$
In particular, if $P = O(n)$, we get $T_{I}(O(n)) = \ker(B \mapsto B + B^{t}) = Sk(n)$

**Exercise:**

1. $T_{p}(O(n)) = Sk(n)P \subseteq M(n)$
2. For $D \in S(n)$, if $D$ is non-singular and $f^{-1}(D) = \varnothing$ then $f^{-1}(D)$ is a left coset of the subgroup $O(n) \subseteq GL(n)$
3. The image of $GL(n)$ under $f$ is the set of all positive definite matrices in $S(n)$

## Transversality

**Preimage theorem:** Given $f:X\to Y$ sufficient condition for $f^{-1}(y)$ to be a manifold is that $y$ be regular $\{ y \}=0 \dim$ manifold. (See [[#Regular Values and Pre-Image Theorem|Pre-Image Theorem]])

**Q:** Is there a similar condition for $Z \subseteq Y$ submanifold i.e. when is $f^{-1}Z$ a manifold.

Fix $y \in Z$ and pick $x \in f^{-1}(y)$ assumed nonempty, since $Z$ is locally given by vanishing of $\text{codim}(Z)=l$ independent functions near y, we may replace $Y$ by open set $Y_{1}$ to get,

$$
X_{1} = f^{-1}(Y_{1}) \xrightarrow{f}  Y_{1} \xrightarrow{ g}  \mathbb{R}^{l} \quad g =\underbrace{   (g_{1},\dots,g_{l}) }_{\text{ind. funcs going to 0}}
$$

where $Z \cap Y_{1} = g^{-1}(0)$

$$
T_{x}X \xrightarrow{df_{x}}  T_{y}Y \xtwoheadrightarrow{dg_{y}} T_{0} \mathbb{R}^{l} = \mathbb{R}^{l}
$$

It follows that $f^{-1} (Z \cap Y_{1} = Z_{1})  =f^{-1} g^{-1}(0) = (gf)^{-1} (0)$. Thus a sufficient criterion for $f^{-1} Z$ to be a manifold is $0$ being a regular value for $gf$, $d(gf)_{x}$ is onto for all $x \in f^{-1} Z_{1}$

**Linear algebra fact:** $U \xrightarrow{\alpha} V \xtwoheadrightarrow{\beta} W$ linear map then $\beta \circ \alpha$ is onto $\iff im(\alpha) + \ker(\beta) = V$

Thus we need $im(df_{x}) + \ker(dg_{y}) = T_{y}Y$ , Since $ker(dg_{y}) = T_{y}Z$, we get

$$
im(df_{x}) + T_{y}Z = T_{y}Y
$$

**Def:** Let $f:X\to Y$ be a smooth map and $Z \subseteq Y$ a submanifold, We say that $f$ is **transversal** to $Z$ if $f^{-1}Z$ is empty or $\forall x \in f^{-1}Z$, the condition $im(df_{x})+T_{y}Y$ holds.

**Theorem:** If $f:X\to Y$ is transversal to a submanifold $Z \subseteq Y$ then $f^{-1}Z$ is empty or a submanifold in $X$ of $\text{codim}_{Y}(Z)$.

**Proof:** Proved above.
**Notation**: $f \pitchfork Z$, when $Z$ is a point $\{ y \}$ then we have $f \pitchfork \{ y \}$, iff $y$ is regular value.

**Examples:**

1.  
$$
\begin{align}
Y = \mathbb{R}^{2}, Z = \text{X-axis in } \mathbb{R}^{2} \\
f:\mathbb{R} \to \mathbb{R}^{2} \quad t \mapsto (at,bt) \\
f^{-1} Z = \{  0 \}
\end{align}
$$
Note that $t \mapsto (at^{3},bt^{3})$, has the same image, but is not transversal to $Z$. (In this case $im(df_{0})$ is trivial)
2.  
$$
\begin{align}
g:\mathbb{R} \to \mathbb{R}^{2}  & \quad t \mapsto (t,t^{2}) \\
\end{align}
$$
is not transversal since $dg_{0}=\mathbb{R}e_{1}$

---

![[IMG_20260128_150228.jpg]]


We say that two submanifolds $X,Z \subseteq Y$ intersect transversally if $i :X \hookrightarrow Y$ is transversal to $Z$, or simply $\forall p \in X \cap Z$ we have $T_{p}X + T_{p}Z = T_{p}Y$ (or $X \cap Z = \varnothing$). We say $X \pitchfork_{Y} Z$.
**Theorem:** If $X \pitchfork_{Y} Z$ and $X \cap Z \neq \varnothing$, then $X \cap Z$ is a submanifold of $Y$ of codimension $\text{codim}_{Y}(X) + \text{codim}_{Y}(Z)$

**Proof:** Follows from previous theorem we have
$$

\text{codim}_{Y}(Z) = \text{codim}_{X}(Z \cap X) = \text{codim}_{Y}(Z \cap X) - \text{codim}_{Y}(X) \quad \blacksquare

$$

---
Thus if $X,Z$ intersect transversally in $Y$ and $X,Z$ are locally given by vanishing of $m,n$ functions respectively, then $X \cap  Z$ is locally given by vanishing of $m+n$ functions,

**Example:** Any 2 lines intersect transversally unless they are the same, Any 2 lines in $\mathbb{R}^{3}$ intersect transversally iff the intersection is empty ,any 2 planes in $\mathbb{R}^{3}$ intersect transversally unless they are the same.

## Local Properties
**Def:** We say that a property $P$ of smooth maps is local on the base/codomain if for any smooth map $f:X\to Y$ the following are equivalent:
1. $f$ satisfies $P$
2. $\forall$ open $Y_{1} \subseteq Y, f:X_{1}= f^{-1}Y_{1}\to Y_{1}$ satisfies $P$
3. $\exists$ an open cover $\{ Y_{i} \}$ of $Y$ such that $f^{-1}Y_{i} \to Y_{i}$ satisfies $P$.
---
Similarly we define a property $P$ to be local on the source/domain
1. $f$ satisfies $P$
2. $\forall$ open $U \subseteq X, f|_U:U \to Y$ satisfies $P$
3. $\exists$ an open cover $\{ U_{\alpha} \}$ of $X$ such that $f|_{U_{\alpha}} : U_{\alpha} \to Y$ satisfies $P$.
**Examples:**
- $P=$ immersion: local on source & base
- $P=$ submersion: local on source & base
- $P=$ diffeomorphism: local **only** on base
- $P=$ local diffeomorphism: local on base and source
- $P= f \pitchfork Z$ for a given $Z \subseteq Y$: local on base & source
- $P=$ embedding: local **only** on the base
- $P=$ one-one / onto / bijection: local **only** on the base
- $P=$ proper?
## Homotopy & Stability
We say a smooth function $f:X\to Y$ is smoothly homotopic to a smooth function $g:X\to Y$ if $\exists$ a smooth map $F:X\times \underbrace{ I }_{ \text{time domain} } \to Y$ such that
$$

F|_{X\times \{ 0 \}} = f \quad F|_{X\times \{ 1 \}} = g

$$
We also write $F(x,t)$ as $f_{t}(x)$. Then $f_{0}(x)=f,f_{1}(x)=g$ and $f_{t}(x)$ denote intermediate functions. Thus as $t$ goes from $0$ to $1$, $f$ deforms to $g$.

Fix $X,Y$. We write $f \sim g$ if such an $F$ exists. (refer **[[Algebraic Topology|Algebraic Topology]]**)
(We also write $f \overset{F}{\sim} g$)

We given the following properties:
1. $f \sim f$: Use $f_{t} \equiv f, \forall t$. ($X \times I \to Y, (x,t) \mapsto f(x)$)
2. $f \sim g \implies g \sim f$: Use $G(x,t) = F(x, 1-t)$ for going from $g$ to $f$.
3. $f \sim g \text{ \& } g \sim h \implies f \sim h$

### Bump functions
$$
\alpha(t) = \begin{cases}
e ^{- 1/t^{2}}  & t\geq 0  \\
0  & t \leq{0}
\end{cases}
$$
$\alpha$ is continuous and 
$$
\lim_{ t \to 0 } \frac{e^{-1/t^{2}}}{ t^{n}} = 0 \quad \forall n \in \mathbb{N}
$$
We have $\alpha^{(n)}(0) =0$ makes $\alpha$ smooth, from this we can produce $\rho(x)$ smooth
$$
\rho(x) = \begin{cases}
0  & x \leq \frac{1}{4} \\
1 & x\geq \frac{3}{4}
\end{cases}
$$
by 
$$
\rho(x) = \frac{\alpha(x-1/4)}{\alpha(x-1/4) + \alpha(3/4-x)}
$$

Given $F(x,t)$ we can also use $\widetilde{F}(x,t) = F(x,\rho(t))$ to compose 2 homotopies.


Some examples of homotopy (in $\mathbb{R}^n$):

*   $X \xrightarrow{f} \mathbb{R}^n$, $f_t(x) = f(x) + t\vec{v}$, with $\vec{v} \in \mathbb{R}^n$.
    This is a homotopy from $f_0 = f$ to $f_1 = f+\vec{v}$ (translation).
*   $f_t(x) = tf(x)$. This is a homotopy from $f_0=0$ to $f_1=f$ (dilation/scaling).
    (Note: The blackboard says $f_0=f$ to $f_1=0$ if it was $(1-t)f$, but $tf(x)$ goes from 0 to f. The blackboard text says "Straight line homotopy between f & g... $F(x,t) = (1-t)f + tg$". Let's stick to the straight line one for general case).
*   Straight line homotopy between $f$ and $g$:
    $$
    F(x,t) = (1-t)f + tg
    $$

$X=S^1 \hookrightarrow \mathbb{R}^2$.
Two circles corresponding to two embeddings of $S^1$ in $\mathbb{R}^2$.

```tikz
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}
    \draw (0,2) ellipse (0.5 and 0.2);
    \draw (0,0) ellipse (0.5 and 0.2);
    \draw (-0.5,2) -- (-0.5,0);
    \draw (0.5,2) -- (0.5,0);
    \node at (0, -0.5) {Translation};
    \draw[->, dotted] (0.7, 0.5) -- (0.7, 1.5);
\end{tikzpicture}
\end{document}
```

Homotopy between two circles one inside the other

```tikz
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}
    \draw (0,0) circle (1);
    \draw (0,0) circle (0.7);
    \draw (0,0) circle (0.4);
    \draw (0,0) circle (0.1);
    \node at (0, -1.5) {Dilation};
\end{tikzpicture}
\end{document}
```

A property $P$ of maps (of manifolds) is said to be stable (under homotopy) if for any smooth map $f:X\to Y$ satisfying $P$, whenever $f_t:X\to Y$ is a smooth homotopy with $f_0=f$, there exists an $\varepsilon > 0$ such that $f_t$ satisfies $P$ $\forall t < \varepsilon$.

Quick Observation: Thus $f$ satisfies $P \implies$ 'small' deformation of $f$ satisfies $P$.
Given $F(x,t) = f_t(x)$ on $U \subseteq \mathbb{R}^k$ open $(df_t)$.

### Homotopy & Stability Theorem
The following classes of smooth maps from a **compact manifold** $X$ to a manifold $Y$ are stable:
(a) immersions
(b) submersions
(c) local diffeomorphisms
(d) maps transversal to a fixed **closed submanifold** $Z \subseteq Y$
(e) embeddings
(f) diffeomorphisms

**Proof:** Let $k = \dim(X)$, $l = \dim(Y)$. Then (a) follows from (b) & (c) with $k=l$.

**Proof of (a), (b):** Suppose $f$ satisfies (a) or (b). It suffices to prove the claim:
$$
\begin{cases}
\text{For any smooth family } F: X \times I \to Y \text{ with } f_0 = f, \\
\text{and for any } p \in X, \exists \text{ open nbd } U \subseteq X \text{ of } p \text{ and } \epsilon > 0 \\
\text{such that } f_t|_U \text{ satisfies (a) or (b) } \forall t < \epsilon.
\end{cases}
$$
Indeed, if the claim holds, then by varying $p$ over $X$ we get an open cover of $X$ by the $U$'s and hence by compactness, we get finitely many $U_i$ and $\epsilon_i$. Set $\epsilon = \min\{\epsilon_i\}$. Then $f_t$ satisfies (a) or (b) on all of $X$ $\forall t < \epsilon$.

<!-- **Proof of claim:** $\left[ f_0 \text{ satisfies (a) or (b) at } p \implies F \text{ satisfies at } (p,0) \implies F \text{ satisfies in an open box} \right]$

Since the claim is local in nature and properties (b), (c) are local on domain, codomain, we may work with coordinate neighborhood $V$ of $f(p)$ in $Y$ and a neighborhood $U_1 \times [0, \epsilon_1)$ of $(p,0)$ in $X \times I$. -->

**Proof of claim:**
Now $f=f_0=F(-,0)$. By choosing local coordinates around $p$, we may assume that $X, Y$ are open in $\mathbb{R}^k, \mathbb{R}^l$ and $F$ is defined over some subinterval of $I$.
(Pick an open nbd $V$ around $f_0(p) \in Y$ and use a box $U \times [0, \epsilon)$ around $(p,0)$ in $F^{-1}(V)$).

Now we see that the matrix of $(df_t)_x$ is a submatrix of $(dF)_{(x,t)}$.
i.e., if $F = (\varphi_1(x,t), \dots, \varphi_l(x,t))$, then
$$
(dF)_{(x,t)} = \begin{bmatrix}
\frac{\partial \varphi_1}{\partial x_1} & \dots & \frac{\partial \varphi_1}{\partial x_k} & \frac{\partial \varphi_1}{\partial t} \\
\vdots & \ddots & \vdots & \vdots \\
\frac{\partial \varphi_l}{\partial x_1} & \dots & \frac{\partial \varphi_l}{\partial x_k} & \frac{\partial \varphi_l}{\partial t}
\end{bmatrix}
$$
The matrix for $(df_t)_x$ consists of the first $k$ columns of $(dF)_{(x,t)}$.

Now, if $f_0$ satisfies (a) at $p$, then $(df_0)_p$ is injective, i.e., $k \le l$ and $\text{rk}(df_0)_p = k$.
Hence $\exists$ a $k \times k$ minor with non-zero determinant. Hence the same minor in $(dF)_{(p,0)}$ is invertible. By continuity the same holds at all $(x,t)$ in a nbd of $(p,0)$. Hence, the same minor is invertible for all $(df_x)_t$ in that nbd, i.e., (a) holds over that nbd.

The proof for (b) is the same with $k \ge l$ and rank = $l$ everywhere.
Thus the claim is proved. Q.E.D for (a), (b)

(d) If $f_0^{-1}(Z) = \varnothing$, then the complement of $F^{-1}(Z)$ is an open neighborhood of $X \times \{0\}$. By compactness of $X$, this neighborhood contains a box $X \times [0, \epsilon)$.
Clearly $f_t \pitchfork Z, \forall t < \epsilon$ as $f_t^{-1}(Z) = \varnothing$.

Now assume $f_0^{-1}Z \ne \varnothing$. Let $W$ be any open nbd of $f_0^{-1}Z \times \{0\}$ in $X \times I$.
Then we see that $\exists \epsilon > 0$ such that
$f_t^{-1}Z \subseteq W, \forall t < \epsilon$.

> [!Proof of claim]-
> If not, then $\exists (x_i, t_i) \notin W, t_i \to 0$ such that $f_{t_i}(x_i) \in Z$.
> By compactness of $W^c$ we may assume that $\lim(x_i, t_i)$ exists, say $(x,0) \notin W$. Then $f(x)=F(x,0)=\lim F(x_i, t_i) \in Z$ as $Z$ is closed. Contradiction.

Now we may localize the problem. Let $x \in f_0^{-1}Z, y=f(x)$.
Let us localize around $x \in X, y \in Y$.

```tikz
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}
    % Domain X x I
    \draw (0,0) rectangle (2,2);
    \node at (-0.2, 1) {$I$};
    \node at (1, -0.2) {$X$};
    
    % Neighborhood W
    \draw[dashed] (0.5, 0) arc (180:0:0.5cm and 0.3cm);
    \node at (1, 0.5) {$W$};
    
    % Mapping F
    \draw[->] (2.5, 1) -- (4, 1) node[midway, above] {$F$};
    
    % Codomain Y
    \draw (4.5, 0) rectangle (6.5, 2);
    \node at (6.3, 0.2) {$Y$};
    
    % Submanifold Z
    \draw (5, 1) -- (6, 1.5) node[right] {$Z$};
\end{tikzpicture}
\end{document}
```


Now we may localize the problem. Let $x \in f_0^{-1}Z, y=f(x)$.
Let us localize around $x \in X, y \in Y$, so that
```tikz
\usepackage{tikz-cd}
\usepackage{amssymb}
\begin{document}
\begin{tikzcd}
X' \arrow[r, "f_0"] & Y' \arrow[r, "g"] & \mathbb{R}^d \\
x & y & \vec{0}
\end{tikzcd}
\end{document}
```
is a map with $g$ submersion at $y$.
We may also assume that $g f_0$ is a submersion at $x$ since $f_0 \pitchfork Z$ at $x$ ($Z = g^{-1}(0)$ locally).

Since $d(g f_0)_x$ is, as before, a part of $d(g F)_{(x,t)}$...

#todo 

---

**Proof ($P=\text{embedding}$)**
Since $X$ is compact it suffices to check for $P=$ one-one immersion and hence $P=$ one-one.

It will be more convenient to work with $G: X \times I \to Y \times I$ where $G(x, t) = (f_t(x), t)$. Now we see that around any $(p, 0) \in X \times I$, $G$ is one-one in a nbhd.
Indeed, $dG_{(p,t)}$ in local coordinates is a matrix that contains $(df_t)_p$.
$$
\begin{bmatrix}
\frac{\partial \varphi_1}{\partial x_1} & \dots & \frac{\partial \varphi_1}{\partial x_k} & \frac{\partial \varphi_1}{\partial t} \\
\vdots & & \vdots & \vdots \\
\frac{\partial \varphi_l}{\partial x_1} & \dots & \frac{\partial \varphi_l}{\partial x_k} & \frac{\partial \varphi_l}{\partial t} \\
0 & \dots & 0 & 1
\end{bmatrix}
$$
Since $(df_0)_p$ is one-one, we have $k \le l$ and $(df_0)_p$ has rank $k$. Hence $dG_{(p,0)}$ has rank $k+1$, i.e., $G$ is an immersion near $(p, 0)$ and hence is one-one near $(p, 0)$.

