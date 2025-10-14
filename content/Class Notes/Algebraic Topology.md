---
title: Algebraic Topology
tags:
  - "#incomplete"
  - refactor
created: 2025-07-28
publish: true
---

**Recap**:
- Homotopy of maps $X\to Y$
- Path homotopy for maps $I\to X$
- Products of paths $f:I\to X, g:I\to X ,f*g$
- Loop at $x_0$ = path initial point and final point = $x_{0}$

## Fundamental Groups

**Theorem**:  path homotopy classes of loops at $x_{0}$ form a group $\pi_{1}(x_{0})$

X is called contractible if $\exists x_{0} \in X$ such that $1_{x}:X\to X$ is homotopic to $e_{x_{0}}$ = constant path at $x_{0}$ $\implies$ X is path connected.

**Exercise**: If X is contractible then $\pi_{1}(X,x)$ is trivial.

$\pi_{1}(X,x_{0})$ is trivial for any convex/ starlike subset in $\mathbb{R}^{n}$

Suppose $x_{0},x_{1} \in X$ and Suppose $\exists$ a path $\alpha:I \to X$ from $x_{0}$ to $x_{1}$ . Then we can relate $\pi_{1}(X,x_{0})$ to $\pi_{1}(X,x_{1})$ as follows:
$\tilde{\alpha}: \pi_{1}(X,x_{0})\to \pi_{1}(X,x_{1})$

![[Drawing 2025-07-28 14.16.43.excalidraw.svg]]
```tikz
\usepackage{tikz-cd}
\begin{document}
\begin{tikzcd}
x_0 \ar[loop below, "f"] \ar[r, "\alpha"] & x_1
\end{tikzcd}
\end{document}
```
$[f] \to [\alpha^{-1} * f * \alpha ]$

this is well defined because $f \cong g$ then $\alpha^{-1} * f * \alpha \cong  \alpha^{-1} * g * \alpha$ 

**Theorem:** $\tilde{\alpha}$ is an isomorphism of groups

**Proof:** First we check that it is a homomorphism 

Let f, g be loops at $x_{0}$

Then $$\tilde{\alpha}([f]*[g]) = \tilde{\alpha}([f*g]) = [\alpha^{-1} * f * \alpha]$$
$$
[\alpha^{-1} * f * \alpha * \alpha^{-1} * g * \alpha ]
$$
$$
[\bar{\alpha} * f * \alpha ] *[\bar{\alpha} * g * \alpha ]
$$
$$
\tilde{\alpha}([f])*\tilde{\alpha}([g])
$$


We check that $\tilde{\alpha}$ has a inverse, namely $\tilde{\bar{\alpha}} : \pi_{1}(X,x_{0})\to \pi_{1}(X,x_{1})$

$$
\tilde{\bar{\alpha}} \circ \tilde{\alpha} ([f]) = [\alpha * \bar{\alpha} * f* \alpha * \bar{\alpha}]a = [f]
$$
Similarly we can do the same of the other composition. $\quad \blacksquare$

Now from on we mostly assume X is path connected.

The isomorphism we produced is sensitive to the choice of $\alpha$

**Exercise:** $\alpha,\beta$ paths from $x_{0}$ to $x_{1}$. Then $\tilde{\alpha} = \tilde{\beta}$ iff $[\alpha * \bar{\beta}]$ ( loop at $x_{0}$) is in the centre of $\pi_{1}(X,x_{0})$

**Solution:** ($\implies$)
Given that $\tilde{\alpha} = \tilde{\beta}$ i.e. $[\bar{\alpha} * f* \alpha ] = [\bar{\beta} * f * \beta]$ We need to show that $[\alpha * \bar{\beta}]$ which is a loop at $x_{0}$ is in the center of the fundamental group $\pi_{1}(x_{0})$. 
So to prove $[\alpha * \bar{\beta} * f] = [\alpha * \bar{\beta} * f * \beta * \bar{\beta}]$ = $[\alpha * \bar{\alpha} * f * \alpha * \bar{\beta}]$ = $[f* \alpha * \bar{\beta}]$
Hence $[\alpha * \bar{\beta}]$ is in the center of $\pi_{1}(x_{0})$ 
($\impliedby$)
$$
[\bar{\alpha} * f * \alpha ] = [\bar{\alpha} *f*\alpha * \bar{\beta}*\beta ] = [\bar{\alpha}*\alpha*\bar{\beta}*f*\beta ] = [\bar{\beta} * f * \beta ]
$$


**Definition**: We call X simply connected if X is path connected and $\pi_{1}(X,x)$ is trivial for some $x \in X$ (and hence $\forall x \in X$)

Contractible $\implies$ simply connected by earlier exercise.

**Lemma**: X simply connected $\iff$ any 2 paths in X with same endpoints are path homotopic. 
**Proof**: $(\implies)$
Given f,g both from $x_{0}$ to $x_{1}$ we see that $f* \bar{g}$ $\cong e_{x_{0}}$
$$
f \sim f*e_{x_{1}} \sim f*\bar{g} * g \sim e_{x_{0}} *g \sim g
$$

$(\impliedby )$
Let h be a loop at $x_{0}$ Then $h \sim e_{x_{0}}$. Hence $[h]$ is trivial $\quad \blacksquare$

A based space is pair $(X,x_{0})$ where X is a topo space and $x_{0} \in X$. A map of based spaced $(X,x) \to (Y,y_{0}$ is a continuous function $h:X\to Y$ such that $h(x_{0}) = y_{0}$  which we also denote as h

Any loop $f:I\to X$ based on $x_{0}$ maps to the loop $h\circ f:I\to Y$ based at $y_{0}$. This process also preserves path homotopies. $f \sim g$ (loops at $x_{0}$) $\implies$ $h\circ f \sim h \circ g$

![[Drawing 2025-07-28 15.03.09.excalidraw.svg]]


Thus we get a well defined function on the fundamental group.

$\pi_{1}(X,x_{0}) \to \pi(Y,y_{0})$ denoted as $(h_{x_{0}})_{*}$ or simply $h_{*}$

If you have $f,g: X \to Y, \phi :Y\to Z$ 
$f \sim g \implies \phi \circ f \sim \phi \circ g$ 

If we change the basepoints, How does $h_{*}$ change?

Assume X path connected. Let $x_{0},x_{1} \in X$, $y_{i} = h(x_{i})$ 
Let $\alpha: I \to X$ be a path from $x_{0}$  to $x_{1}$  is a path from $y_{0}$ to $y_{1}$

```tikz
\usepackage{tikz-cd}
\begin{document}
\begin{tikzcd}
\pi_1(X,x_0) \ar[d ,"\hat{\alpha}"] \ar[r ,"h_*"] & \pi_1(Y,y_0) \ar[d ,"\widehat{h \circ \alpha}"]\\
\pi_1(X,x_1) \ar[r ,"h_*"] & \pi_1(Y,y_1)
\end{tikzcd}
\end{document}
```

This implies that $(h_{x_{0}})_{*}$   $(h_{x_{1}})_{*}$ have the same behavior. If one of them is injective/ surjective /bijective then so is the other. Their kernels and images have he same size etc.

Proof of commutativity of diagram: $\overline{(h\circ\alpha)} \circ (h_{x_{0}})_{*}$ = $(h_{x_{1}})_{*}\circ \bar{\alpha}$ . Indeed if $f:I\to X$ is a loop at $x_{0}$ then:

### Functorial Properties (natural)
1. If  $X \xrightarrow{h} Y  \xrightarrow{k} Z$ are maps then $k_{*}h_{*} =(k\circ h)_{*}$ as maps $\pi_{1}(X) \to \pi_{1}(Z)$
2. For the identity map $(X,x_{0}) \xrightarrow{1_{x}} (X,x_{0})$ we have  $(1_{x})_{*}$ identity map on the $\pi_{1}(X)$
3. From 1 and 2 it follows that if  $(X,x_{0}) \to (Y,y_{0}$ is a homeomorphism then $h_{*}$ is an isomorphism. Indeed $(h^{-1})_{*}$ is an inverse for $h_{*}$.

How can we compute $\pi_{1}$ Covering spaces
A covering space of X = a space where some of loops have been 'unwound'

## Covering Spaces

**Def:** Let $p:E \to B$ be a continuous surjection. An open subset $U \subseteq B$ is said to be evenly covered if the inverse image $p^{-1} (U)$ is a disjoint union of open subsets $\{ V_{\alpha } \}$ in E such that $p_{|_{V_{\alpha }}} : V_{\alpha}\to U$ is a homeomorphism $\forall \alpha$  We call $V_{\alpha }$ a partition of $p^{-1}U$ into slices, each slice being $V_{\alpha }$
If U is evenly covered by p, then so is W for every subspace W $\subseteq$ U.

**Def:** A map $p:E \to B$ is called a _covering map_ if it is surjective and every b $\in B$ has a open neighbourhood which is an evenly covered by p. (Equivalently , B admits a cover by open subsets that are evenly covered ). We also say E is a covering space of B by p.


### Basic Examples and Properties
1. $1_{x}:X\to X$ is a covering map. More generally if E = $X \times \{ 1,2,\dots,n \}$ . then the obvious projection map p(x,i) = x is a covering space. In fact E = $X\times A$ (with discrete topology for A) works. This is the trivial covering map
2. If p:$E \to B$ is a covering map. then for any subspace $B_{0} \subseteq B$ , $p_{|_{E_{0}=p^{-1}B_{0}}} : E_{0} \to B_{0}$ is also a covering map. If $B_{0}$ is open we call his new map a localisation on the base. Any covering map is locally on the base a trivial covering map. 
3.  For a covering map $p: E \to B$, for any $b \in B$, the fiber $p^{-1}(b) \subseteq E$ has the discrete topology. If B is connected, then $|p^{-1}(b)|$ is constant. We call this the degree of p.
**Exercise**: Use the fact that $|p^{-1}(b)|$ is locally constant
4.  A covering map is an open map
Sketch: 
$p : E \to B$ $V \subseteq E$ open, pick any $e \in V$ set b= p(e). We have a open nbd U of b which is evenly covered by p. $p^{-1}U = \bigcup V_{\alpha }$ choose $V_{\alpha_{0} }$ so that $e \in V_{\alpha_{0}}$ Then $p(V \cap V_{\alpha_{0}})$ is open as p is an homeomorphism when restricted to any one of the $V_{\alpha }$s.

Thus we have found a open subset inside the image of V under p containing b $\quad \blacksquare$

**Exercise:**  p has finite degree (B connected) $\iff$ $p^{-1}k$ is compact for any compact subset $K \subseteq B$. In this case P is a closed map.

**Solution:**


5.  $p : \mathbb{R} \to S^1 \subseteq \mathbb{C} \cong \mathbb{R}^2$
	$t \to  e^{2\pi it}$ = $(\cos 2\pi t,\sin 2\pi t)$
	To prove that $S^1$ is evenly covered we use 4 open subsets $x>0,x < 0, y>0, y<0$. Take any one of them, 
	$U = {(x,y) | x>0}$ in $S^1$. Then $p^{-1}(U) = \bigcup (n - \frac{1}{4},n + \frac{1}{4})$
	Then $V_{n} \cong U$. A similar argument works for the other 3 open sets in S^1 .

6. For any nonzero integer m, the function $z \to z^m$ in $\mathbb{C}$ induces a covering map $S^{1} \to S^{1}$. ($S^1 \subseteq \mathbb{C}$) **Exercise**
7.  $X \xrightarrow{f} Y \xrightarrow{g} Z$ f,g covering $\implies$ $g\circ f$ covering if deg(g) < $\infty$.
8. If $p: E \to B$ and $p':E' \to B'$ are covering maps, then so is $p\times p': E \times E' \to B \times B'$ $(e,e') \to (p(e),p'(e'))$
	Proof: Pick $(b,b') \in B\times B'$ . Pick $U \subseteq B$ and $U' \subseteq B'$ evenly covered open nbds of $b,b'$ resp. Let $p^{-1}U = \bigcup V_{\alpha }$ , $p^{-1}U' = \bigcup V'_{\beta }$ Then $\bigcup V_{\alpha}\times V'_{\beta } = (p \times p')(U \times U')$ 
9. (Surface of revolution)Let T = $S^{1}\times S^{1}$. Then by (8) $p \times p: \mathbb{R} \times \mathbb{R} \to S^{1}\times S^{1}$ is a covering map $p(t) = e^{2\pi it}$. Each unit square $[n,n+1]$ maps onto the torus $\mathbb{T}$. Since $p\times p$ is an open surjection, we have that the map is a quotient map.
   To embed this in $\mathbb{R}^3$ we have given a curve $t \to  (r(t),z(t))$
   $(t,\theta )  \to (r(t)\cos \theta, r(t) \sin \theta, z(t))$
   For the torus we have $t \to (z+ \cos 2\pi t, \sin 2\pi t)$ and we have as the parametrization 
$$
\sigma(t,\theta ) = ((z+\cos 2\pi t)\cos \theta , (z+\cos 2\pi t)\sin  \theta , \sin 2\pi t)
$$

![[Drawing 2025-07-31 17.38.33.excalidraw.svg]]


```tikz
\usepackage{tikz-cd}
\usepackage{amssymb}
\begin{document}
\begin{tikzcd}
\mathbb{R}^2 \ar[d, dashed] \ar[r] & S^1 \times S^1 \ar[dl] \\
\mathbb{T}
\end{tikzcd}
\end{document}
```

- Any collection of open sets $\{ U_{\lambda } \}$ covering B such that each $U_{\lambda }$ is evenly covered will be called a trivialising cover for p. 

**Def:** (local homeomorphism)
$X \to  F$ for any $x \in X$ exists open nbd $V \subseteq X$ such that f(V) $\subseteq Y$  open and $V \to f(V)$ homeomorphism.

$X \xrightarrow{f} Y \xrightarrow{g} Z$ f, g being local homeomorphism then implies gf local homeo.

Covering map $\implies$ local homeomorphism $\iff$(**Exercise**) locally one-one + open map

**Exercise:**  Local homeomorphism + closed map implies covering map ( assume base Y is connected and f is onto)

**Solution:**

**Exercise:** $\mathbb{C} \to \mathbb{C}^\times$ is a covering map. $x \mapsto e^z$ 

**Ideas/Hints:** check that it is locally one-one, 

**Solution:**


### The lifting properties of covering spaces
**Def:** Let $p:E\to B$ be a continuous fn. For any continuous function $f:X\to B$ a lifting of f is a continuous map $\tilde{f}:X\to E$ such that $f= p \circ \tilde{f}$ In general $\tilde{f}$ is not uniquely determined

```tikz
\usepackage{tikz-cd}
\begin{document}
\begin{tikzcd}
& E \ar[d, "p"] \\
X \ar[ur, dashed , "\tilde{f}"] \ar[r, "f"] & B
\end{tikzcd}
\end{document}
```


Example : $p : \mathbb{R} \to S^{1}$
i) $f: I \to S^{1}$  ,$f(s) = (\cos \pi s, \sin \pi s)$ , $\tilde{f}(s) = \frac{s}{2}$ is a lift and so is $s \mapsto \frac{s}{2} + h$
ii) $g(s) = (\cos \pi s, -\sin \pi s)$ $\tilde{g}(s) = -\frac{s}{2} + n$
iii) $h(s) = (\cos 4\pi s, \sin 4 \pi s)$ $\tilde{h}(s) = 2s + n$

### Lifting theorems
**Theorem:** (Lifting of paths) Let $p:(E,e_{0}) \to (B,b_{0}$ be a covering map. Then any path $f: I \to B$ starting at $b_{0}$ lifts uniquely to a path $\tilde{f}:I\to E$ starting at $e_{0}$
```tikz
\usepackage{tikz-cd}
\begin{document}
\begin{tikzcd}
& (E,e_0) \ar[d , "p"] \\
I \ar[r, "f"] \ar[ur , dashed,"\tilde{f}"] & (B,b_0)
\end{tikzcd}
\end{document}
```

**Proof:**  Pick a trivialising open cover $\{ U_{\lambda } \}$ of B for p. Then $\{ f^{-1} U_{\lambda }\}$ is an open cover of I. 
As I is a compact metric space, by the Lebesgue number lemma, exists $\delta >0$ such that any interval of length less than $\delta$ is in some $f^{-1} U_{\lambda }$ . Hence we may choose $s_{i} \in I$ 
$0 = s_{0} < s_{1} < \dots <s_{n} =1$ such that $f([s_{i-1},s_{i}]) \subseteq U_{\lambda }$ for some $\lambda$

Say $f([s_{0},s_{1}]) \subseteq U$ (an evenly covered open set).
Now $p^{-1}(U) = \cup V_{\alpha }$.  since $f(0) = b_{0}$ so that $b_{0} \in U, \exists$ a unique slice V among $V_{\alpha }$ containing $e_{0}$ . Using the homeomorphism $V \to Y$ we lift  $f|_{[s_{0},s_{1}]}$ to $\tilde{f}|_{[s_{0},s_{1}]}$ .

We repeat this process inductively : Suppose f has been lifted toa continuous fn f tilde. Now $f[s_{}]$

To prove uniqueness we again argue by induction from left to right 
#incomplete 

**Theorem:** (lifting homotopies)  Let $p:(E,e_{0})  \to (B,b_{0})$ be a covering map, then any continuous map $F:I\times I \to B$ with $F(0,0) = b_{0}$ lifts uniquely to a continuous map$\widetilde{F} : I\times I \to E$ with $\widetilde{F}(0,0) = e_{0}$. 

**Proof:** As before by pulling back a trivialising open cover of B (for p) to the compact metric space $I\times I$ (via F). We use the Lebesgue covering lemma to find $0= s_{0} < s_{1}<\dots < s_{n} =1$ and $0 = t_{0}<t_{1}<\dots<t_{}n=1$ such that $F([s_{i},s_{i+1}] \times [t_{j},t_{j+1}])$  lives completely inside one of the $U_{\lambda }$. Also, using the previous theorem, we may assume that $F_{|I\times \{ 0 \}}$ and $F|_{\{ 0 \}\times I}$ have been lifted

Call $R_{ij}  =[s_{i},s_{i+1}] \times [t_{j},t_{j+1}]$ 

We will proceed inductively from left to right by giving a lexicographic ordering to the squares $R_{ij}$

Pick $(i_{0},j_{0})$
Assume that we have lifted F for the union of all $R_{ij} < R{i_{0}j_{0}}$ and the big L from the left and bottom edge of the square. Call this union A. then observe that $A \cap R_{ij}$ is always L-shaped
#incomplete 

**Theorem:** (Lifting of path homotopies) Let $p:(E,e_{0}) \to (B,b_{0})$ be a covering map. Let f,g be 2 paths in B with initial point $b_{0}$ and let $\tilde{f}, \tilde{g}$ denote the unique lifts in E starting at $e_{0}$. If $f , g$ are path homotopic with same final points, then so are $\tilde{f}$ and $\tilde{g}$ with same final points via the unique lift of the homotopy.

**Proof:** Assume that $F: I\times I \to B$ gives the path-homotopy from f to g with $f(1) = g(1) = b_{1}$. take the lift F and see that constant paths lift to constant paths, hence we can show that by uniqueness they have the same endpoint.
#refactor

Let $p:(E,e_{0}) \to (B,b_{0})$ be a covering map. we define the _lifting correspondence_ for p to be the function given by 
$$
\phi: \pi_{1}(B) \to p^{-1}(b_{0})
$$
given by $[f] \mapsto \tilde{f}(1)$ 

**Theorem:** For the covering map $pE \to B$ if E is path connected ( and hence , so is B as $E \twoheadrightarrow B$) . then the lifting correspondence is onto. If E is simply connected then the correspondence is bijective. 

**Proof:** If $e \in p^{-1}(b_{0})$ then for any path g from $e_{0}$ to e gives us a loop  $p \circ g$ at $b_{0}$
 whose lift is $g$. Hence the correspondence is onto.

Suppose $\phi([f])  = \phi([h])$ . Then $\widetilde{f}(1) = \widetilde{h}(1)$ i.e., $\widetilde{f}$ and $\widetilde{h}$ have the same endpoints. If E is simply connected, $\widetilde{f} \sim \widetilde{h}$.  Hence $f \sim h$ Thus $[f] = [h]$ in this case.

Remark: If E is path-connected we have a bijection.

**Exercise:** If E is path- connected we have a bijection
$$
\pi_{1}(B,b_{0}) \leftrightarrow \{ (e,[g]) | e \in p^{-1}(b_{0}), \text{g is a path from e to } e_{0}\}
$$


**Solution:** 

**Corollary:** For any $a \in S^{1}$ , $\pi_{1}(S^{1},a)$ is as a set bijection with $\mathbb{Z}$
**Proof:** Look at $(\mathbb{R},0) \to (S^{1},1), t \mapsto e^{2\pi it}$ Then $p^{-1}(1)=\mathbb{Z}$

The lifting correspondence doesn't say anything about the group structure on $\pi_{1}(B)$ The lifts $\widetilde{f}$all start at $e_{0}$ and hence we can't multiply them.
**Lemma:** Consider $p:\mathbb{R} \to S^{1}$ $t \mapsto e^{\pi it}$ . Let $f: I \to  S^{1}$ be a path with $f(0) =a \in S^{1}$ and let $\widetilde{f}$ be a lift of f with $\widetilde{f}(0) = x \in \mathbb{R}$ If $\widetilde{f}(1) = x+r$ for some $r \in \mathbb{R}$ then for any other lift $\tilde{f_{1}}$ of $f$ implies $\tilde{f_{1}}(0) = y \implies \tilde{f_{1}}(1) = y + r$ 

**Proof:** Since $\widetilde{f}$ and $\tilde{f_{1}}$ lift f, $p(x) = p(y) = a$. $\implies y -x \in \mathbb{Z}$ say $y = x+d$ for some $d \in \mathbb{Z}$. Then $s \mapsto \widetilde{f}(s)+d$ is also a lift of f starting at x+d = y.

$\implies f_{1} = \widetilde{f} + d$ by uniqueness. $\widetilde{f}(1) = \widetilde{f}(1) + d = x+r+d=y+r \quad \blacksquare$
**Theorem:** $\pi_{1}(S^{1},1) \cong (\mathbb{Z},+)$ as  groups

**Proof:** $(\mathbb{R},0) \xrightarrow{p} (S^{1},1)$ Consider $[f],[g] \in \pi_{1}(S^{1})$ Lift them to $\widetilde{f},\widetilde{g}$ starting at 0. Then $\widetilde{f}(1),\widetilde{g}(1) \in \mathbb{Z}$ say m,n resp. then $\widetilde{(f * g)}  = \widetilde{f} * \widetilde{g_{1}}$ where   $\widetilde{g_{1}}$ is the unique lift of g starting at m.

$\widetilde{f} * \widetilde{g_{1}}$ maps to $f * g$ under p. Now by the lemma $\widetilde{g_{1}}(1) = m+n$

therefore $\widetilde{f_{1}} * \widetilde{g_{1}}$ starts at 0 and ends at $m+n$
$\widetilde{(f * g)}(1)$ = m+n  , i.e lifting correspondence is a homeomorphism
$\phi([f] * [g]) = \phi[f] + \phi[g]$  $\quad \blacksquare$


**Exercise:**  Describe the lifting correspondence
$S^{1} \to S^{1} , z \mapsto z^{m}$ is this also a group homeomorphism?

**Solution:**

**Exercise:**  Identify $p_{*}$ for $(S^{1},1) \mapsto (S^{1},1)$ given $z \mapsto z^{m}$
$$
\pi_{1}(S^{1},1) \to \pi_{1}(S^{1},1)
$$
**Solution:**

**Def:** For a subset $A\subseteq X$ a _retraction_ of X onto A is a map, $r \twoheadrightarrow A$ such that $r_{|A}$ is identity on A. We say that A is a retract of X.

eg: $S^{1} \to \mathbb{R}^{2}\setminus \{ 0 \}$ is a retract using the retraction 
$$
r: \mathbb{R}^{2}-\{ 0 \} , r \mapsto \frac{r}{\lvert v \rvert }
$$

**Exercise:**  IF X is Hausdorff then A must be closed in K


**Solution:** 

**Lemma:** If $A \subseteq X$ is a retraction then $j: A \to X$ inclusive induces an injection homomorphism of  fundamental  groups.

**Proof:** Use functoriality:
$$
r\circ j = 1_{A} \implies r_{*}j_{*} = (1_{A})_{*} = \text{identity on } \pi_{1}(A)
$$
$\implies  j_{*}$ is injective $\quad \blacksquare$

**Theorem:** $S^{1}$ is not a retract of $\mathbb{R}^{2}$ or $\mathbb{B}^{2}$

**Proof:** $\pi(\mathbb{R}^{2}),\pi_{1}(B^{2})$  are trivial as 

$$
S^{1} \subseteq \mathbb{R} - \{ 0 \}
$$
is retract iff $p \in$  interior of $B^{2}$



For any 🗿-space $(X,x_{0})$ we have a one-one correspondence

$$
\{\text{loops} f:I\to X \text{ at }x_{0}\} \leftrightarrow \{ \text{maps }(S^{1},1) \to (X,x_{0}) \}
$$

Given $f:I\to X$ we have $\bar{f}:S^{1} \to X$ determined by
```tikz
\usepackage{tikz-cd}
\begin{document}
\begin{tikzcd}
I \ar[d, "f"] \ar[r,, "q"] & S^{1} \ar[dl, dashed, "\bar{f}"] \\
X
\end{tikzcd}
\end{document}
```

Given $g:S^{1} \to X$ we obtain $f:I\to X$ as the composite
$$
I \to S^{1} \to X
$$

It is easily seen to be a 1-1 correspondence

If $f_{1},f_{2}$ are 2 path homotopic loops at $x_{0}$ via $F:I\times I \to X$
then 
```tikz
\usepackage{tikz-cd}
\begin{document}
\begin{tikzcd}
I\times I \ar[r,"q\times Id"] \ar[d,"F"] & S^1 \times I \ar[dl,"\overline{F}"] \\
X
\end{tikzcd}
\end{document}
```
gives existence of $\overline{F}$  a base point fixing homotopy between $f_{1}:(S^{1},1) \to (X,x_{0})$ and $f_{2}(S_{1},1) \to (X,x_{0})$ 

![[Drawing 2025-08-07 17.25.22.excalidraw.svg]]
In general, given $(A,a) \xrightarrow{f,g} (B,b)$ maps of pointed spaces, a base point fixing homotoy from f to g is a map $A \times I \xrightarrow{H} B$ such that $H(x,0) = f(x)$ $H(x,1) = g(x)$ and $H(a,t) = b ,\forall t$

Conversely, if $G : S^{1}\times I \to X$ is a base point fixing homotopy between $f_{i}(S^{1,1}) \to (X,x_{0})$ for i =1,2, then $G \circ (q \times Id)$ is a path homotopy from $f_{1} \circ q$ to $f_{2} \circ q$

Given 2 pointed spaces $(A,a),(B,b)$ we define $[(A,a),(B,b)]$ or simply $[A,B]$ to be the set of base point fixing homotopy clases of maps from $(A,a)$ to $(B,b)$

Thus, in this notation $[(S^{1},1),(X,x_{0})] \leftrightarrow \pi_{1}(X,x_{0})$ where $[f] \mapsto [f \circ q]$
In particular, $[(S^{1},1),(S^{1},1)] \leftrightarrow \pi_{1}(S^{1},1) \cong \mathbb{Z}$ where $[id] \mapsto 1$ 

## Higher homotopy groups 
For $n\geq 0$ define $S^{n} \subseteq \mathbb{R}^{n+1}$ to be $\{ v: ||v|| = 1\}$  i.e. unit sphere

Fix a base point a $\in S^{n}$
$$
\pi_{n}(X,x_{0}) := [(S^{n},a), (X,x_{0})]
$$

**Exercise:**  $\pi_{0}(X,x_{0})$  = No. path components of X.


**Solution:**

Using $\frac{I^{n}}{dI^{n}} \cong S^{n}$ we also have $[(I^{n},dI^{n}),(X,x_{0})] = \pi_{n}(X,x_{0})$

**Facts**: 
1. For n>0 $\pi_{n}(X,x_{0})$ is a group
2. For n>1 $\pi_{n}(X,x_{0})$ is an abelian group
3. For n>0 $\pi_{n}(S^{n}) \cong \mathbb{Z}$

## Brouwer fixed point theorem
**Theorem:** (Brouwer fixed point theorem) Let $f: B^{2} \to B^{2}$ be a continuous map. Then there exists a point $x \in B^{n}$ such that $f(x) = x$.

**Proof:** Assume f has no fixed point. Then we'll obtain a retract $B^{2} \to S^{1}$ using this , a contradiction.

```tikz
\begin{document}
\begin{tikzpicture}
% Draw a circle
\draw[thick] (0,0) circle (2cm);
% Draw a point x and a point f(x) inside the circle
\filldraw[black] (0,0) circle (2pt) node[anchor=south] {$x$};
\filldraw[black] (1,1) circle (2pt) node[anchor=south] {$f(x)$};
% Draw an arrow starting from (0,0) and ending at (2,2)
\draw[->, thick] (0,0) -- (1.4,1.4);
\end{tikzpicture}
\end{document}
```
$$
\lVert tf(x) + (1-t)x \rVert =1
$$

This gives a quadratic equation in t, We look for the non positive root of this, which is a continuous function of x.

This continuous function is a retract of the disk to a circle, which is a contradiction. $\quad \blacksquare$

**Recall**: $(X,x_{0})$ 🗿-space
$$
\{ f:I \to X \text{ at } x_{0} \} \leftrightarrow  \{ \text{maps } (S^{1},1) \to (X,x_{0}) \}
$$

```tikz
\usepackage{tikz-cd}
\begin{document}
\begin{tikzcd}
% double headed arrow right from I to S^1 and arrow downwards from I to X named f and arrow from S^1 to X named bar{f}
I \ar[d, "f"] \ar[r, "q"] & S^{1} \ar[dl, dashed, "\bar{f}"] \\
X
\end{tikzcd}
\end{document}
```

This correspondence preserves base point fixed homotopy.

**Exercise:**  Show that the Brouwer fixed point theorem implies that every continuous map $f: S^{n} \to S^{n}$ has a fixed point.

**Lemma:** Let $h:S^{1} \to X$ be a map. Then the following are equivalent.
i) $h$ is null-homotopic.
ii) h extends to a map $k:B^{2} \to X$
iii) $h_{*} : \pi_{1}(S^{1}) \to \pi_{1}(X)$ is the trivial map

**Proof:** $(i) \implies (ii)$
```tikz
\begin{document}
\begin{tikzpicture}
%A cylinder,cone, circle with center with arrow from one to the next
% Draw the cylinder 
\draw[thick] (0,0) -- (0,2) arc[start angle=180, end angle=360, x radius=0.5, y radius=0.2];
\draw[thick] (0,0) arc[start angle=180, end angle=360, x radius=0.5, y radius=0.2] -- (1,2);
\node at (0,0) [left] {$t=0$};
\node at (0,2) [left] {$t=1$};
\draw[dashed] (0,2) arc[start angle=180, end angle=0, x radius=0.5, y radius=0.2]; 
\draw[dashed] (0,0) arc[start angle=180, end angle=0, x radius=0.5, y radius=0.2];
% Draw an arrow from the cylinder to the cone 
\draw[->, thick] (1.5,1) -- (2.5,1); 
% Draw the cone 
\draw[thick] (3,0) -- (3.5,2) -- (4,0); 
\draw[thick] (3,0) arc[start angle=180, end angle=360, x radius=0.5, y radius=0.2]; 
\draw[dashed] (3,0) arc[start angle=180, end angle=0, x radius=0.5, y radius=0.2]; % Draw an arrow from the cone to the circle 
\draw[->, thick] (4.5,1) -- (5.5,1); % Draw the circle with center 
\draw[thick] (7,1) circle(0.5); 
\filldraw (7,1) circle(1pt); % Center of the circle

\end{tikzpicture}
\end{document}
```


$(ii) \implies (iii)$ Follows from functoriality $S^{1} \hookrightarrow B^{2} \xrightarrow{k} X$ 
$$
\pi_{1}(S^{1}) \to \pi_{1}(B^{2}) \xrightarrow{k_{*}} \pi_{1}(X)
$$
$(iii) \implies (i)$ Lets fix base points. Set $x_{0}=h(1)$. Now the element $1 \in \mathbb{Z} = \pi_{1}(S^{1})$ corresponds to the identity map in $[(S^{1,},1),(S^{1},1)]$. Thus $h_{*}(1)$ is the homotopy class of $(S^{1},1)\xrightarrow{Id} (S^{1},1) \xrightarrow{h}(X,x_{0})$ i.e., $[h]$ itself in $\pi_{1}(X,x_{0})$ Since this is trivial by assumption it is homotopic to the constant map $e_{x_{0}} \quad \blacksquare$

**Corollary:** $S^{1} \hookrightarrow \mathbb{R}^{2}\setminus \{ 0 \}$  , $S^{1} \xrightarrow{Id} S^{1}$ are not null homotopic.
**Proof:** Since  $j_{*}$ and $(Id)_{*}$ are injective and $\pi_{1}(S^{1}) \ncong \{ 0 \}$  hence by (iii) above j, Id are not null-homotopic. $\quad \blacksquare$

Recall that a (continuous,) vector field on $B^{2}$ is a continuous function $B^{2}\to \mathbb{R}^{2}$

E.g. $(x,y) \mapsto (x,0)$

**Theorem:** For any nowhere vanishing vector field $\alpha$ on $B^{2}, \exists$ a point in $S^{1}$ where $\alpha$ points inwards and a point in $S^{1}$ where $\alpha$ points outwards.

**Proof:**  
$$
\alpha : B^{2} \to \mathbb{R}^{2} \setminus \{ 0 \}.
$$
Then $\alpha_{|S^{1}} : S^{1} \to \mathbb{R}^{2}\setminus \{ 0 \}$ is null-homotopic by earlier lemma. Suppose $\alpha_{|S^{1}}$ does not point inwards anywhere. Then we'll find a homotopy $\alpha_{|S^{1}} \sim j$ ($j: S^{1} \hookrightarrow \mathbb{R}^{2} \setminus \{ 0 \}$) which will be a contradiction.
For this we use the straight line homotopy. Though $\mathbb{R}^{2}\setminus \{ 0 \}$ is not convex, it suffices to check that $t \alpha_{|S^{1}} + (1-t)$ is nonzero for all $t \in [0,1]$. 
$$
\begin{align}
F: S^{1}\times I \to & \mathbb{R}^{2} \setminus \{ 0 \}  \\
(x,t) \mapsto& t \alpha_{|S^{1}}(x) + (1-t)x
\end{align}
$$
Clearly RHS is nonzero for $t=0,1$. For $t \in (0,1)$ If RHS = 0, we get $\alpha(x) = -\frac{1-t}{t}x$ a contradiction to $\alpha$ not pointing inwards anywhere.

Similarly by assuming $\alpha$ does not point outwards anywhere and replacing $\alpha$ by $-\alpha$, we can show that there is a point in $S^{1}$ where $\alpha$ points outwards. $\quad \blacksquare$

Remark: This theorem is easily equivalent to Brouwer fixed theorem
$\implies$ Given $f:B^{2}\to B^{2}$ look at $\alpha(x):= f(x) - x$. If $\alpha(x) \neq 0 \forall x$, then $\exists x \in S^{1}$ such that, $\alpha(x) = \lambda x, \lambda >0$ a contradiction as $f(x) =x + \lambda x = (1 + \lambda)x \not\in B^{2}$ 

$\impliedby$ Given $\alpha \neq 0 \forall x$ consider the normal vector field and it maps from $\widetilde{\alpha}: B^{2} \to S^{1}\subseteq B^{2}$. Hence by Brouwer fixed point theorem we have that there is a fixed point on $S^{1}$. Hence there a vector pointing outwards. Similarly using $- \widetilde{\alpha}$ we have an vector pointing inward.

**Theorem:** Let A be a 3x3 real matrix with positive entries. Then A has a positive real eigenvalue.

**Proof:** Consider the first quadrant in $\mathbb{R}^{3}$, $Q$. Then A maps $Q$ to itself as entries of A are $\geq 0$. Consider $D = S^{2} \cap Q$. Then D is homeomorphic to $\{ (x,y)|x\geq 0,y\geq 0, x^{2}+y^{2}\leq 1 \}$ by projection. Hence homeomorphic to $B^{2}$.
 Now apply Brouwer's fixed point theorem to the map $f: D \to D$ given by $f(x) = \frac{Ax}{\lVert Ax \rVert}$. If u is the fixed point, then $u = \frac{Au}{||Au||} \implies Au = ||Au||u \implies ||Au||$ is the eigenvalue $\quad \blacksquare$


**Def:** Let $A \subseteq X$ be a subset. We say that $A \xhookrightarrow{j} X$ is a deformation retract if $\exists$ a retract $X \xrightarrow{r} A \subseteq X$ which is homotopic to the identity:

$\exists$ continuous $F:X\times I \to X$ such that
1. $F_{|X\times \{ 0 \}} = Id_{X}$
2. $F_{|X\times{\{ 1 \}}} = j \circ r$ 
3. $F(a,t) = a, \forall a \in A$

E.g.: $S^{1} \xhookrightarrow{j} \mathbb{R}^{2}\setminus \{ 0 \}$ is also a deformation retract. $r(v) = \frac{v}{||v||}$. For F, use the straight line homotopy $(v,t) \mapsto \frac{tv}{||v||} + (1-t)v$ keeping in mind that for $t \in [0,1]$ this segment does not pass through $0$ in $\mathbb{R}^{2}$. (All three conditions are satisfied.)

**Theorem:** Let $A \xhookrightarrow{j} X$ be a deformation retract. Then $j_{*}:\pi (A,a) \to \pi_{1}(X,a)$ is an isomorphism

**Proof:** Since j is a retract, $j_{*}$ is an injective homomorphism. Now we need to show that it is surjective. let $f: I\to X$ be a loop at a.

Let $F:X\times I \to X$ be a homotopy for the deformation retract. Consider $I\times I \xrightarrow{F\times Id} X\times I \xrightarrow{F} X$ then  the composite map $G:I\times I \to X$ satisfies
1. $G_{|I\times \{ 0 \}} = f$
2. $G_{|I\times \{ 1 \}} = (j \circ r)\circ f : I \xrightarrow{f} X \to A \hookrightarrow X$
3. $G(0,t) = a = G(1,t), \forall a \in A$ 

**Corollary:** $\pi_{1}(\mathbb{R}^{2} \setminus \{ 0 \},a) \cong \mathbb{Z}$
**Proof:** we have a deformation retract from $\mathbb{R}^{2} \setminus \{ 0 \}$ to the circle $S^{1}$.

**Exercise:**  $\pi_{1}(\mathbb{R}^{3} \setminus L,a) \cong \mathbb{Z}$ for any line $L \subseteq \mathbb{R}^{3}$

**Solution:**

14/08/25
**Recall**:
1) Brouwer fixed point theorem
2) Any non-vanishing vector field $\alpha:B^{2} \to \mathbb{R}^{2}\setminus \{ 0 \}$ has a point on $S^{1}$ where $\alpha$ points inwards and a point where it points outwards. (Equivalent to the Brouwer fixed point theorem.) (else $S^{1} \hookrightarrow B^{2} \xrightarrow{\alpha} \mathbb{R}^{2}\setminus \{ 0 \}$).
3) Deformation retract

## Homotopy equivalence

**Theorem:** Let $h,k$ be maps $(X,x_{0}) \to (Y,y_{0})$. If there exists a base point fixing homotopy fixing homotopy $h \sim k$. Then $h_{*} = k_{*}$ as maps $\pi_{1}(X,x_{0}) \to \pi_{1}(Y,y_{0})$.

**Proof:** Given the homotopy $H:X\times I \to Y$ and given a loop f at $x_{0}$ in $X$, we see that the composite G given by 
$$
I\times I \xrightarrow{f\times Id} X\times I \xrightarrow{H}Y 
$$
satisfies
$$
\begin{align}
G(s,0) =& H(f(s),0)=h \circ f (s) = \text{image of loop f in Y under } h \\
G(s,1) =& H(f(s),1) = k\circ f(s) = \text{image of loop f in Y under }  k \\
G(0,t) =& H(x_{0},t)=y_{0} \\
G(1,t) =& H(x_{0},t) = y_{0}
\end{align}
$$
Thus $h \circ f \sim k \circ f$ in Y i.e. $h_{*}[f] = k_{*}[f] \quad \blacksquare$

**Def:** Two maps $f:X\to Y$ and $g:Y\to X$ are said to be a homotopy equivalence if $g\circ f:X\to X$ is homotopic to the identity on X ($g \circ f \sim Id_{x}$) and $f \circ g:Y\to Y$ is homotopic to $Id_{y}$. We say that $f,g$ are homotopy inverses. We say that $X,Y$ are homotopically equivalent space or have the same homotopy type.

E.g.: A deformation retract $j:A\to X$ is a homotopy eq. Indeed with $\gamma:X\to A$ the retract, we have $\gamma \circ j = Id_{A}$ while $j \circ \gamma  \sim Id_{x}$ via the deformation retraction H.

If $f:X\to Y$ and $h:Y\to Z$ are homotopy equivalences with homotopy inverses $g:Y\to Z$ and $k:Z\to Y$ resp. then $h\circ f:X\to Z$ is also a homotopy eq with inverse $g\circ k$ 

Indeed $(g\circ k)\circ(h\circ f) = g \circ (k \circ h)\circ f \sim g \circ Id_{Y}\circ f = g \circ f \sim Id_{x}$
Similarly $(h \circ f)\circ (g\circ k) \sim Id_{Z}$

We say $X\ \approx  Y$ is they have the same homotopy type, it is an equivalence relation.

Deformation retracts are not symmetric: $\{p\} \hookrightarrow X$ is a deformation retract if X is contractible.

**Informal examples**: 
1. Consider $X = \mathbb{R}^{2}\setminus \text{2 points}$
	a) Figure 8.
	b) Figure $\theta$
	c) Figure dumbbell
	Then (a),(b),(c) are deformation retracts of X with the two missing points placed appropriately.


$S^{n} \hookrightarrow \mathbb{R}^{n+1} \setminus \{ 0 \}$ is a deformation retract. $v \mapsto \frac{v}{||v||}$.
$\{ p \} \hookrightarrow X$ with X contractible. Is this a deformation retract always?

Broom space $X\times I$ #incomplete 

### Invariance of homotopy

**Theorem:**(Invariance of $\pi_{1}$ under homotopy of maps) Let $h,k: X\to Y$ be maps,, $x_{0} \in X,y_{0} = h(x_{0}), y_{1}=k(x_{0})$. If $h,k$ are homotopic via $H:X\times I \to Y$(so that $\alpha(t) = H(x_{0},t)$ is a path in Y from $y_{0}$ to $y_{1}$) then the following diagram commutes
```tikz
\usepackage{tikz-cd}
\begin{document}
\begin{tikzcd}
\pi_1(X,x_0) \ar[d, "h_*"] \ar[dr, "k_*"] \\
\pi_1(Y,y_0) \ar[r, "\hat{\alpha}"] & \pi_1(Y,y_1)
\end{tikzcd}
\end{document}
```
![[Excalidraw/Drawing 2025-08-18 14.47.11.excalidraw.svg]]

**Proof:** Let $f:I\to X$ be a loop in X at $x_{0}$. It suffices to check that for any such arbitrary f, we have $\hat{\alpha}(h_{*}[f]) = k_{*}[f]$ 
i.e.
$$
\begin{align}
\bar{\alpha} * (h\circ f)*\alpha \sim_{p} k\circ f \text{ equivalently} \\
\bar{\alpha}*(h\circ f)*\alpha*\overline{(k\circ f)} \text{ is a path homotpic to the trivial homotopy}
\end{align}
$$

$I\times I \xrightarrow{f\times Id} X\times I \xrightarrow{H} Y$

$$
\begin{align}
&F(x,0) = H(f(s),0) = h\circ f(s)  \\
&F(1,t) = H(x_{0},t)= \alpha(t) \\
&F(1-s,1) = H(f(1-s),1) = k\circ \overline{f(s)}  = \overline{(k \circ f)}(s) \\
&F(0,1-t) = H(x_{0},1-t) = \overline{\alpha(t)}
\end{align}
$$

Since $I\times I$ is homeomorphic to the disc $D^{2}$ and the path $1*2*3*4$ goes to the boundary $S^{1}$ under such a homeomorphism we see that the loop has trivial image in $\pi_{1}(Y,y_{1}) \quad \blacksquare$

**Corollary:** If $h_{*}$ is inj/surj/bij then so is $k_{*}$
**Proof:** Obvious from diagram

**Corollary:** 
(a) If h is null-homotopic then $h_{*}$ is trivial.
(b) If h is homotopic to a homeomorphism $k$ then $h_{*}$ is an isomorphism. 

**Theorem:** (Invariance of $\pi_{1}$ under homotopy equivalence of spaces) If $f:X\to Y$ is a homotopy equivalence, then for any $x_{0} \in X$, $y_{0}=f(x)$ we have $\pi_{1}(X,x_{0}) \cong \pi_{1}(Y,y_{0})$ via $(f_{x_{0}})_{*}$ 

**Proof:** Let $g:Y \to X$ be a homotopy inverse. Let $x_{1}=g(y_{0})$. Let $y_{1}=f(x_{1})$. Now consider maps
```tikz
\usepackage{tikz-cd}
\begin{document}
\begin{tikzcd}
\pi_1(X,x_0) \ar[r,"(f_{x_0})_*"] & \pi_1(Y,y_0) \ar[dl,"(g_{y_0})"] \\
\pi_1(X,x_1) \ar[r,"(f_{x_1})_*"] & \pi_1(Y,y_1)
\end{tikzcd}
\end{document}
```

Since $g\circ f \sim Id_{x}$. $((g\circ f)_{x_{0}})_{*} = (g_{y_{0}})_{*}(f_{x_{0}})_{{*}}$ is an isomorphism. Similarly $f\circ g \sim Id_{Y} \implies (f_{x_{1}})_{*}(g_{y_{0}})_{*}$  is an isomorphism.

$(g_{y_{0}})_{*}$ is injective and surjective, i.e. an isomorphism, Hence, the same is true of $(f_{x_{1}})_{*} \quad \blacksquare$

**Theorem:** $S^{n}$ is simply connected for $n\geq{2}$ 

**Proof:** Let $f:I\to S^{n}$ be a loop at a basepoint $x_{0}$. 
(First Proof) #incomplete 

**Theorem:** Let X be a topological space covered by 2 open sets $U,V$ such that $U \cap V$ is nonempty and path connected. Then using the inclusions $i:U\hookrightarrow X$,$j:V \hookrightarrow X$. we obtain that for any $x_{0} \in U \cap V$, $\pi_{1}(X,x_{0})$ is generated by the images $i_{*}\pi_{1}(U,x_{0})$ and $j_{*}\pi_{1}(V,x_{0})$

From this theorem it is easy to show the above result by using complements of 2 antipodal points.

**Proof:** Let $f: I \to X$ be a loop at $x_{0} \in U \cap V$. We claim $\exists \ 0=t_{0}<t_{1}<\dots<t_{n}=1$ such that 
1. $f(t_{i}) \in U\cap V \forall i$ and,
2. $f([t_{i},t_{i+1}])$ lies completely in $U$ or in $V$.

By the Lebesgue number lemma we first find $t_{i}$ such that (2) is satisfied now we can say that if images of $[t_{i},t_{i+1}], [t_{i-1},t_{i}]$  sit it the same open set we join them otherwise $f(t_{i})$ lies in $U \cap V$

Now let $f_{i}: [0,1] \to [t_{i},t_{i+1}] \xrightarrow{f} X$. Then $f = f_{1}*\dots*f_{n}$. Here $f_{i}$s are no longer loops. But since we have (1) we can say that there is a path from $x_{0} \to f(t_{i})$ call it $\alpha_{i}$. Hence,
$$
f \sim f_{1}*\overline{\alpha_{1}} *\alpha_{1}*f_{2}*\dots*\overline{\alpha_{n-1}}\alpha_{n-1}*f_{n}
$$
$\blacksquare$

**Theorem:** $x_{0}\in X,y_{0} \in Y$. Then,
$$
\pi_{1}(X\times Y,(x_{0},y_{0})) = \pi_{1}(X,x_{0}) \times \pi_{1}(Y,y_{0})
$$

**Proof:** Using the projection maps we get, $p_{*}:\pi_{1}(X\times Y)\to \pi_{1}(X)$ and $q_{*}:\pi_{1}(X\times Y)\to \pi_{1}(Y)$. Therefore we get a map of groups $\pi_{1}(X\times Y)\to \pi_{1}(X)\times \pi_{1}(Y)$. which sends the class $[f]$ of loops $f:I\to X\times Y$ to the class $([p\circ f],[q\circ f])$ of loops in X and Y respectively. We check this is one-one and onto.

**one-one**: If F is a path homotopy for $(p\circ f) \sim e_{x_{0}}$. and a path homotopy similarly for $(q \circ f)$. Now we can create a path homotopy for f to $e_{(x_{0},y_{0})}$

**onto**: Given $f:I\to X$ and $g:I\to Y$, we can construct a loop $h:I\to X\times Y$ given by $h(t) = (f(t),g(t))$. Then $[h] \mapsto ([f],[g])$ gives that it is onto.

**Examples**: 
1. $\pi_{1}(\mathbb{R}^{n} \setminus m \text{ points}),n\geq 3$ , taking an open cover
2. $\mathbb{R}^{n}\setminus \text{n-ball}$
![[IMG_20250819_170609.jpg]]

**Lemma:** Let $p:E\to B$ be a covering map Then
1. E is Hausdorff iff B is. The converse is true if $\deg(p)<\infty$
2. E is locally n-Euclidean (i.e., locally homeomorphic to an open subset of $\mathbb{R}^{n}$) iff B is
3. If E is second countable, then so is B

**Proof:**
1. Suppose B is Hausdorff. Given $x,y \in E$,if $x,y$ lie in the same fiber, then we can find distinct slices of some evenly covered open set. If $x,y$ lie in different fibers, then choose disjoint neighbourhoods around $p(x),p(y)$ and take inverse image.
   
   Now suppose E is Hausdorff and $\deg(p) \leq d$. Let $b_{1},b_{2} \in B,b_{1}\neq b_{2}$. Pick evenly covered neighbourhoods $U_{i}$ around $b_{i}$. Suppose 
$$
\begin{align} \\
p^{-1}U_{1} =& \bigsqcup V_{\alpha } \\
p ^{-1} U_{2} =& \bigsqcup W_{j} 
\end{align}
$$
   For each point $x_{i}$ in $p ^{-1}(b_{1})$ and for each $y_{j}$ in $p ^{-1}(b_{2})$ choose pairwise disjoint neighbourhoods $Y_{1,i},Y_{2,j}$. Now consider,
   ![[IMG_20250819_173804.jpg]]
   ![[IMG_20250819_174937 1.jpg]]
2. This is also clear since for any evenly covered $U \subseteq B$, $p^{-1}U = \bigcup V_{\alpha}, V_{\alpha} \to U$ homeomorphism
3. If $\{ V_{\lambda} \}$ is a countable base of $E$, then so is $p(V_{\lambda})$.

**Def:** A topological n-manifold is a topological space X that is Hausdorff, second countable and locally n-Euclidean. When $n=1$ we call it a curve, $n=2$ surface.

**Example**: 
1. $\mathbb{R}$, open interval, conic sections are curves
2. A 0-manifold is the same as a discrete countable space.
3. Line with 2 origins is locally Euclidean but not Hausdorff, hence not a manifold.
4. Closed/ Semi-closed intervals, Cantor set are not k-manifolds for any k.
5. Plane, torus, cylinder, open Mobius strip etc are surfaces 
6. ![[Excalidraw/Drawing 2025-08-21 16.51.12.excalidraw.svg]]
%%[[Drawing 2025-08-21 16.51.12.excalidraw.md|🖋 Edit in Excalidraw]]%% 
These are not manifolds

>[!info]
>A topological m-manifolds cannot be an n-manifold for $m\neq n$.

**Def:** 
$$
\mathbb{R}P^{n}:= \frac{S^{n}}{x\sim-x} \leftrightarrow  \frac{\mathbb{R}^{n+1}\setminus \{ 0 \}}{w \sim \lambda w}
$$

**Theorem:** The quotient maps $S^{n} \twoheadrightarrow \mathbb{R}P^{n}$ is a covering map of degree 2. Moreover $\mathbb{R}P^{n}$ is Hausdorff, and hence is a compact, path-connected surface with $\pi_{1}(\mathbb{R}P^{n})$ having exactly 2 elements, i.e. $\pi_{1} \cong \mathbb{Z} / 2\mathbb{Z}$ 

**Proof:** By construction p is onto. Next we see that p is open. $p ^{-1} p(V) = V \bigcup -V$ which shows that $p(V)$ is open if V is open. (similarly p is also a closed map.)

Given $x \in \mathbb{R}P^{n}$, let $y,-y$ be its preimage. Choose open set U around y lying in the hemisphere containing y 
![[IMG_20250821_171225.jpg]]
Now $U:= P(V) = P(-V)$ is evenly covered because $p ^{-1} U = V \bigsqcup -V$ and $V\xrightarrow{p} U, -V \xrightarrow{p} U$ are bijective and open, hence a homeomorphism.
By the earlier lemma. $\mathbb{R}P^{n}$ is Hausdorff and a surface. Compactness, path connectedness hold because they hold for $S^{n}$. Since $S^{n}$ is simply connected for $n\geq 2$ , $|\pi_{1}(\mathbb{R}P^{n})| = |p^{-2}(x)| = 2$. $\quad \blacksquare$

>[!info]
>$\mathbb{R}P^{0} = \text{1 point}$ 
>$\mathbb{R}P^{1} \cong S^{1}$ 

![[IMG_20250821_172923.jpg]]

![[IMG_20250821_173137.jpg]]

We see that to get a covering map from a quotient space, the following suffices:
**Lemma:** Let $f:X \twoheadrightarrow Y$ be an quotient map. If $\exists$ a basis $\mathscr{B}$ of open sets in X such that $\forall V \in \mathscr{B}$ we have $f^{-1}f(V) = \bigsqcup V_{\alpha }$ with $V_{\alpha }$ open and $V_{\alpha } \to  f(V)$ bijective, then f is a covering map (and hence also a quotient map)

**Proof:** Since $f ^{-1} f(V) = \bigsqcup V_{\alpha }$, we see that $f(V)$ is open for any $V \in \mathscr{B}$ since it is a quotient map. Since $\mathscr{B}$ is a basis, we see that f is an open map. Hence $V_{\alpha } \to f(V)$ is a homeomorphism. Hence $f(V)$ is evenly covered. Since $V \in \mathscr{B}$ cover X and f is onto, hence $\{ f(V) \mid V \in \mathscr{B}\}$ covers Y. $\quad \blacksquare$

---
**The Klein bottle**:
![[IMG_20250821_175132.jpg]]![[IMG_20250821_175310.jpg]]

![[IMG_20250821_180051.jpg]]![[IMG_20250821_180847.jpg]]
![[IMG_20250821_181228.jpg]]


**Theorem:** (Ultimate lifting theorem) $(\widetilde{X},\widetilde{x_{0}}) \to (X,x_{0})$ covering map, $(z,y_{0})$ path connected + locally path connected then $g:(Z,y_{0}) \to (X,x_{0})$ admits a lift $\widetilde{g}:(Z,y_{o})$  iff

**Proof:**

**Corollary:** if $(Z,z_{0})$ is simply connected and locally path connected then any $g:(Z,z_{0}) \to (X,x_{0})$ lifts to a $\widetilde{g}$. 
**Proof:**

**Corollary:** Any map $(S^{n},z_{0}) \xrightarrow{g} (S^{1},x_{0})$ (for $n>1$) is base point preserving homotopic to a constant map. (pointed null-homotopic)
**Proof:** As $S^{n}$ is simply connected and locally path connected for $n>1$ g lifts to $\widetilde{g}:(S^{n},z_{0}) \to (\mathbb{R}^{1},\tilde{x_{0}})$. As $\mathbb{R}^{1}$ is contractible, we got a pointed homotopy $\widetilde{g}\to \tilde{e_{x_{0}}}$. Apply $p:\mathbb{R} \to S^{1}$. $\quad \blacksquare$

#incomplete 
## Group theory Review

### Abelian groups (Z-Modules)

Let $\{ M_{i} \}_{i \in I}$ be a collection of abelian groups. Then

$$
\begin{gather}
\prod M_{i} = \text{cartesian product with componentwise operations}\\
\bigoplus  M_{i} = \text{submodule consisting of such elements with $a_{i}\neq_{0}$ for finitely many}
\end{gather}
$$
We also have the natural projection maps,
$$
\prod M_{i} \xrightarrow{p_{i}} M_{i}
$$

### Universal properties
$\prod M_{i}$: Given a $\mathbb{Z}$-module $N$ there is a bijection,
$$
\text{Maps}\left( N,\prod M_{i} \right) \leftrightarrow  \{ \text{Maps}(N,M_{i}) \}_{i \in I}
$$
```tikz
\usepackage{tikz-cd}
\begin{document}
\begin{tikzcd}
& N \ar[dl, "f_{i}"'] \ar[d, "f"] \ar[dr, "f_{j}"] & \\
M_{i} & \prod M_{i} \ar[l, "p_{i}"] \ar[r, "p_{j}"'] & M_{j}
\end{tikzcd}
\end{document}
```


$\bigoplus M_{i}:$ For any $\mathbb{Z}$-module N, $\exists$ a bijection
$$
\text{Maps}\left(\bigoplus M_{i},N\right) \leftrightarrow  \{ \text{Maps} (M_{i},N)\}_{i \in I}
$$
```tikz
\usepackage{tikz-cd}
\begin{document}
\begin{tikzcd}
M_{i} \ar[dr, "f_{i}"] \ar[hookrightarrow,r, "j_{i}"] & \bigoplus M_{i} \ar[d, "f"] & M_{j} \ar[hookrightarrow,l, "j_{j}"'] \ar[dl, "f_{j}"'] \\
& N &
\end{tikzcd}
\end{document}
```
$\bigoplus M_{i}$ is the smallest submodule of $\prod M_{i}$ containing $M_{i}$ and every element is uniquely a finite sum $\sum_{}^{} a_{i} a_{i} \in M_{i}, a_{i}= 0$ for almost all $i$.

---
Suppose $M$ is a module and $M_{i}\subseteq M$ submodules. Then we have a natural map $\bigoplus M_{i} \to M$. This map is neither one-one nor onto in general. 

- If it is onto, we say that ${M_{i}}$ generate M. 
- If it is one-one, we say that $\{ M_{i} \}$ are independent.
- If it is bijective, we say that M is an direct sum of $M_{i}$. ($M \cong \bigoplus M_{i}$)

and we also have,
$$
\begin{gather}
\left(\bigoplus M_{i}\right) \oplus  \left(\bigoplus M_{j}\right) \cong \bigoplus M_{k} \\
\bigoplus M_{(i,j) \in I\times J} \cong \bigoplus \left(\bigoplus  M_{i,j}\right)
\end{gather}
$$
**Lemma:** For a $\mathbb{Z}$-module $M$ the following are equivalent,
1. $M \cong \bigoplus \mathbb{Z}$
2. $M$ has a basis on $\mathbb{Z}$, i.e., $\exists$ subset $S = \{ m_{i} \}_{i \in I} \subseteq M$ such that any $x \in M$ can be uniquely written as $x  = \sum_{}^{} a_{i}m_{i},a_{i} \in \mathbb{Z}$
3. $\exists$ subset $S \subseteq M$ such that for any module $N$, $\exists$ a bijection $\text{Functions}(S,N) \leftrightarrow \text{Maps}(M,N)$ . i.e. any function $S\to N$ uniquely extends to a map $M\to N$.

**Proof:**

### Non-abelian groups

Given groups $\{ G_{\alpha} \}_{\alpha \in A}$ we define their abstract free product to be a group $G$ with natural maps $G_{\alpha} \xrightarrow{i_{\alpha}} G$ that satisfy the universal extension property: for any group $H$ and any maps $G_{\alpha} \xrightarrow{f_{\alpha }} H$ $\exists!$ map $G\xrightarrow{f }H$ such that $f_{\alpha}= f \circ i_{\alpha }$. i.e. via $i_{\alpha} G_{\alpha} \to G$ the natural function.
$$
\text{Maps}(G,H) \to \{ \text{Maps}(G_{\alpha},H) \}_{\alpha \in A}
$$
is a bijection.

Since this is a universal property, the data $\{ \{ i_{\alpha} \},G \}$ is uniquely determined upto a unique isomorphism. By choosing $H = G_{\alpha}$ for a fixed $\alpha$ and $f_{\beta} = \begin{cases}Id_{G_{\alpha}} & \alpha = \beta \\ \text{trivial} & \alpha \neq \beta  \end{cases}$ . We see that the existence of $f$ implies $f_{\alpha}i_{\alpha} =  Id_{G_{\alpha}}$. Thus if the universal object = $\{ \{ i_{\alpha} \}, G \}$ exists, then each $i_{\alpha}$ is injective.

---
**Def:** Given groups $\{ G_{\alpha} \}_{\alpha \in A}$, we define a word in $\bigsqcup G_{\alpha}$ to be sequence $w = (g_{1},g_{2},\dots,g_{n})$ with $g_{i} \in \bigsqcup G_{\alpha}$. empty word is the case when $n=0$. A word in $\bigsqcup G_{\alpha}$ is called reduced if it additionally satisfies the conditions:
1. $g_{i}\neq 1$ (in $G_{\alpha }$)
2. $\alpha _i \neq \alpha_{i+1}, \forall i$. Here $\alpha_{i}$ is the index for which $g_{i} \in G_{\alpha_{i}}$
---
**Examples:** $G_{1} = \{ 1,a \}$ with $a^{2} = 1$, $G^{2}= \{ 1,b \}$, with $b^{2} =1$.
Reduced word in $G_{1} \bigsqcup G_{2}$ are $(a,b,a,b,\dots ,b)$

Starting with an arbitrary word $w$, we get a reduced word of (possibly) smaller length by using one of 2 process:
1. if $g_{i} =1$ for some $i$, drop it and re-index
2. If $\alpha_{i}= \alpha_{i+1}$, then replace ith entry by $g_{i},g_{i+1}$, drop the (i+1)th entry and re-index.

**Lemma:** The reduced word obtained by using $1.$ and $2.$  successively is unique.

**Proof:** We argue by case, start with $w = (g_{1},\dots,g_{n})$. Use induction on n. Suppose there are 2 ways of applying $1.$ and $2.$ to $w$. If they have non-overlapping indices, we may perform them in either order to get some result of length n-2. By induction we're done. If they overlap, then one of them must be $(1)$. If $g_{i} = 1$, then we can drop it and re-index. Now the other operation must be either $1.$ or $2.$ on the re-indexed word. Again by induction we're done. $\quad \blacksquare$ 

#### Construction of free product
```tikz
\usepackage{tikz-cd}
\begin{document}
\begin{tikzcd}
G_{\alpha} \ar[r, "i_{\alpha}"] \ar[dr, "f_{\alpha}"] & G \ar[d, "f"] & G_{\beta} \ar[l, "i_{\beta}"] \ar[dl, "f_{\beta}"] \\
& H &
\end{tikzcd}
\end{document}
```
Let us construct $G$ and $i_{\alpha}: G_{\alpha} \to G$ as follows: Let $G$ be the set of all reduced words in $\bigsqcup G_{\alpha}$. Define $i_{\alpha}: G_{\alpha} \to G$ by $g \mapsto (g)$ if $g\neq 1$ and $1 \mapsto ()$.

For any $w = (g_{1},\dots,g_{m})$ and $v=(h_{1},\dots,h_{n})$ we define 
$$
w *  v = \text{reduced word obtained from } (g_{1},\dots,g_{m},h_{1},\dots,h_{n})
$$
To check associativity: $w = (g_{1},\dots,g_{m},v=(h_{1},\dots,h_{n})$ and $u=(k_{1},\dots,k_{p})$. Then
$$
(w*v)*u = \text{reduced word from }(g_{1},\dots,g_{m},h_{1},\dots,h_{n},k_{1},\dots,k_{p}) = w*(v*u)
$$
By the uniqueness of the reduction, hence they are equal.
The identity is the empty word. The inverse of $w=(g_{1},\dots,g_{m})$ is $\overline{w} = (\overline{g_{m}},\dots,\overline{g_{1}})$ where $\overline{g_{i}}$ is the inverse in $G_{\alpha_{i}}$. We see that $w*\overline{w} = ()$ by using the reduction process. 

Hence $(G,*)$ is a group. Hence we can also see that $i_{\alpha}:G_{\alpha} \to G$ is a homomorphism since $i_{\alpha}(g)*i_{\alpha}(h) = (g)*(h) = (gh)$ if $gh \neq 1$ and $()$ otherwise.

Now we check the universal property: Given any group H and maps $G_{\alpha} \xrightarrow{f_{\alpha}} H$ we define $f:G\to H$ by sending the reduced word $w = (g_{1},\dots,g_{n})$ to $f_{\alpha_{1}}(g_{1})\dots f_{\alpha_{n}}(g_{n})$. We see that this is a homomorphism since  $w=(g_{1},\dots,g_{m}), v=(h_{1},\dots,h_{n})$ then 
$$
\begin{align}
f(w * v) &= f(\text{reduced word from }(g_{1},\dots,g_{m},h_{1},\dots,h_{n}))  \\
&= f_{\alpha_{1}}(g_{1}) \dots f_{\alpha_{m}}(g_{m})f_{\beta_{1}}(h_{1})\dots f_{\beta_{n}}(h_{n})) = f(w)f(v)
\end{align}
$$ 
Note that $f$ is uniquely determined by $f_{\alpha}$ since $G$ is generated by $i_{\alpha}(G_{\alpha})$ (i.e. by words of length 1)

---
Let $G$ be a group. For any set of normal subgroups $\{ N_{i} \}_{i \in I}$ $\bigcap_{I}^{} N_{i}$ is also normal in $G$. For any subgroup $H \subseteq G$, $\bigcap_{x \in G}^{}xHx ^{-1}$ is also normal in G. For a subset $S \subseteq G$, the smallest subgroup containing $S$ is $\bigcap_{S \subseteq H}^{}H$ and in fact consists of finite products $s_{1}^{i_{1}}\dots s_{n}^{i_{n}}$ where $i_{k} \in \mathbb{Z}$. The smallest normal subgroup of G containing $S$ is $\bigcap_{S\subseteq N}^{}N$ and consists of finite products $x_{1}s_{1}^{i_{1}}x_{1}^{-1}\dots x_{n}s_{n}^{i_{n}}x_{n}^{-1}$ where $s_{k} \in S, x_{k} \in G,i_{k} \in \mathbb{Z}$.

**Lemma:** Let $G = G_{1} * G_{2}$. We think of $G_{i}$ as subgroups of $G$. Let $N_{i} \trianglelefteq G_{i}$ be normal subgroups and let $N$ be the normal subgroup of $G$ generated $N_{1},N_{2}$. Then $G /N \cong G_{1} /N_{1} * G_{2} / N_{2}$.

**Proof:** We'll show that $G_{1} /N_{1}, G_{2} / N_{2}$ satisfy the universal property of $G/N$. We have natural maps $G_{i} \to G \to G/N$ which factor through $G_{i} /N_{i} \to G/N$ since $N_{i}$ goes to identity in $G/N$. Now given any group H and maps $G_{i} /N_{i} \xrightarrow{f_{i}} H$, we get maps $G_{i} \xrightarrow{f_{i}} H$ which extend to a map $G\xrightarrow{f}H$. Since $N$ is generated by $N_{1},N_{2}$, it follows that $f(N) = 1$. Hence f factors through $G/N \xrightarrow{\tilde{f}} H$. $\tilde{f}$ is unique since f is unique. $\quad \blacksquare$ 

**Exercise:** Show uniqueness (Use that $G \twoheadrightarrow G/N$ and $G$ is generated by $G_{1},G_{2}$)

**Solution:**

**Corollary:** Let $N$ denote the smallest normal subgroup of $G= G_{1}*G_{2}$ containing $G_{1}$. Then $G/ N \cong G_{2}$.
**Proof:** Get $N_{1} = N,N_{2} = \{ 1 \}$ in the lemma. $\quad \blacksquare$

**Example:** $G_{1}=\{ 1,a \}$, $a^{2} =1$, $G_{2}=\{ 1,b \}$, $b^{2}=1$. Then $G_{1}*G_{2}$ is the infinite dihedral group $D_{\infty}$. It has a presentation $\langle a,b \mid a^{2},b^{2} \rangle$.
The smallest normal subgroup $N$ containing $G_{1}$ contains all words of odd lengths that are palindromic with middle letter a. The map $G \twoheadrightarrow G_{2}$ sends a word $w$ to $b^{m}$ where $m$ is the number of occurrences of b in $w$. 

Similarly, in the general case, the map $G \twoheadrightarrow G_{2}$ is obtained by sending a word $w$ to the product of all letters in $w$ that lie in $G_{2}$.

**Def:** A presentation of a group G is a pair $(S,R)$ where S is a set and $R \subseteq F(S)$ such that $G \cong F(S)/N(R)$ where $N(R)$ is the smallest normal subgroup containing R. We write $G = \langle S \mid R \rangle$.

**Example:** $G_{1} = \{ a^{n}|n \in \mathbb{Z} \}$, $G_{2} = \{ b^{n}|n \in \mathbb{Z} \}$ both infinite cyclic. Then $G_{1} * G_{2}$ is all the words of the form $(a^{n_{1}},b^{m_{1}},\dots,a^{n_{k}},b^{m_{k}})$ with $n_{i},m_{j} \neq 0$. This is the free group on 2 generators $a,b$.
Again we can define $G \twoheadrightarrow G_{2}$ by collapsing all occurrences of a to 1. Check that the kernel is the smallest normal subgroup containing $G_{1}$.

**Theorem:** Let $G$ be a group then the following are equivalent:
1. $G$ is free product of infinite cyclic groups, $G \cong \prod_{\alpha \in A}^{*} C_{\alpha}$ , $C_{\alpha} \cong \mathbb{Z}$
2. $\exists$ subset $S \subseteq G$ such that every element of $G$ is uniquely the protect of reduced words in  $G_{s} := \{ s^{i} |i \in \mathbb{Z}\}$, $s \in  S$. 
3. $\exists S \subseteq G$ such that for any group $H$ any function $S \to H$ extends uniquely to a homomorphism $G \to H$. 
Moreover, if these conditions hold, then for any group $H$, any function $S \to H$ extends uniquely to a homomorphism $G \to H$.
In this case, we call G a free group on S.

**Proof:** $(i) \implies (ii)$
Let $C_{\alpha} = \{ a_{\alpha}^{n} | n \in \mathbb{Z}\}$. Since $C_{\alpha} \subseteq \prod_{\alpha \in N}C_{\alpha}$, we may view each $a_{\alpha}$ as an element of G. Now take $S = \{ a_{\alpha} \}$. Then, by construction of the free product, we see that every element of $G$ is uniquely a product coming from a reduced word in $C_{\alpha }$'s.

$(ii) \implies (i)$
Here $G_{s}=$ cyclic subgroup generated by $s \in S$. it then follows that the natural map $\prod_{s \in S}^{*} G_{s}\to G$ (By universal property of free products) is bijective.

Finally, if $(i),(ii)$ holds, then any function $S \xrightarrow{\phi} H$, uniquely give rise to maps $G_{s}\to H, s ^{i} \mapsto \phi(s)^{i}$ and hence give rise to a map $G \cong \prod ^{*} G_{s} \to H$ by the universal property. This map is uniquely determined by the individual maps $G_{s}\to H$, which in turn are uniquely determined by $\phi$. 

$(iii) \implies (ii), (i)$ because each $s \in S$ has infinite order( choose $H=\mathbb{Z}$, $S \to \mathbb{Z}$ sends $s \mapsto 1,$ others to 0.) and then we just use the universal property for $G_{s} \subseteq G$ (any function $S \to H$ uniquely corresponds to maps $G_{s}\to H$)$\quad \blacksquare$ 

---

Let $A$ be a set. Consider infinite cyclic groups indexed by $A$, Want to compare $\prod ^{*}C_{\alpha }$ with $\bigoplus_{A} \mathbb{Z}$. First note that we have a natural map by the universal property of free products,

$$
\prod^{*} C_{\alpha }  \to  \bigoplus_{A} \mathbb{Z}
$$

because we have $C_{\alpha} \cong \mathbb{Z} \hookrightarrow \bigoplus_{A} \mathbb{Z}$. Since $\bigoplus_{A} \mathbb{Z}$ is abelian, we got a natural map,
$$
\left( \prod^{*} C_{\alpha } \right) / \left[ \prod^{*} C_{\alpha },\prod^{*} C_{\alpha } \right] \xrightarrow{\psi }   \bigoplus_{A} \mathbb{Z}
$$
In fact it is an isomorphism, because if $\overline{w} \in \ker(\psi )$ for some word $w$ in $C_{\alpha}$'s, then $\overline{w}$ has to have equal number of $C_{\alpha}$ and $C_{\alpha}^{-1}$ for each $\alpha$. Hence we can pair them up and write $\overline{w}$ as a product of commutators.

---
### Pushout diagrams

**Proposition:** Suppose there are homomorphisms of groups as in the diagram below,
```tikz
\usepackage{tikz-cd}
\begin{document}
\begin{tikzcd}
G_{12} \ar[r,"k_1"] \ar[d,"k_2"] & G_1 \\
G_2 &
\end{tikzcd}
\end{document}
```
$(i)$ If $G_{i}, G_{12}$ are abelian, then $\exists$ a unique triple $(G,G_{1}\xrightarrow{j_{1}} G, G_{2}\xrightarrow{j_{2}}G)$ which is universal for other abelian groups:

```tikz
\usepackage{tikz-cd}
\begin{document}
\begin{tikzcd}
G_{12} \ar[r,"k_1"] \ar[d,"k_2"] & G_1 \ar[d,"j_1"] \ar[ddr,bend left=15,"f_1"] & \\
G_2 \ar[r,"j_2"] \ar[drr,bend right=15,"f_2"'] & G \ar[dr,dashed,"\exists ! f"] & \\
& & H
\end{tikzcd}
\end{document}
```

and given an abelian group $H$ and maps $G_{i}\xrightarrow{j_{i}} H$ such that $f_{1}k_{1} = f_{2}k_{2}$ then $\exists!$ $f:G\to H$ such that $f_{i} = fj_{i}$

$(ii)$ In general with $G_{i}$ not necessarily abelian, we have a similar universal triple for testing against a general group H.

**Remark:** If $G_{12}$ is the trivial group, then $(i)$ gives the direct sum and $(ii)$ gives the free product (Any map from $G_{12}$ is trivial then.)

**Proof:**
$(i)$ Use additive notation for the groups. Now check that $G:= (G_{1} \oplus G_{2})/N$ where $N = \{ (k_{1}(x),-k_{2}(x))|x \in G_{12} \}$ together with the maps $G_{i} \to G_{1}\bigoplus G_{2} \twoheadrightarrow G_{1} \bigoplus G_{2} /N$ satisfy the universal property. (**Exercise**)

$(ii)$ Let $G = G_{1} * G_{2}$ and let $N$ be the smallest normal subgroup of $G$ containing $\{ k_{1}(x)*k_{2}(x)^{-1}|x \in G_{12} \}$. Then $G/N$ together with the natural maps $j_{i}:G_{i} \to G \to G/N$. Now note that $j_{1}k_{1} = j_{2}k_{2}$, i.e. for any $x \in G_{12}$,we have $j_{1}k_{1}(x) = j_{2}k_{2}(x)$ because identifying elements of $G_{i}$ in $G_{1}*G_{2}$ we have $k_{1}(x) *k_{2}(x)^{-1}$ so that its image in $G$ is 1. Image of $k_{i}(x)$ in $G$ is $j_{i}k_{i}(x)$. Therefore $j_{1}k_{1}(x)*(j_{2}k_{2}(x))^{-1} = 1$.

Universal property: Suppose we have $f_{i}:G_{i}\to H$ such that $f_{1}k_{1}f_{2}k_{2}$. By universal property of free products, we have a map $G_{1}*G_{2}\xrightarrow{\widetilde{f}}H$ such that $\widetilde{f}$ extends $f_{i}$. Now observe that $N$ lies in the kernel of $\widetilde{f}$ because $f_{1}k_{1} = f_{2}k_{2}$. 
$$
\widetilde{f}(k_{1}(x)*k_{2}(x)^{-1}) =\widetilde{f}k_{1}(x)\cdot (\widetilde{f}k_{2}(x))^{-1} = f_{1}k_{1}(x) \cdot f_{2}k_{2}(x)^{-1} =1
$$
This induces a map  

$$
\frac{G_1 * G_2}{N} = G \xrightarrow{f} H
$$

which also satisfies $f_i = f \circ j_i$.

Finally note that $f$ is unique since $G$ is generated by the images of $G_1$ and $G_2$, and the value of $f$ on these images is forced because we want $f_i = f \circ j_i$. $\quad \blacksquare$

---

**Remarks:** 
1. $f:I \to X$ path Suppose $\exists$ a continuous map $I \xrightarrow{g} I$ such that $g(0)=0,g(1)=1$. (therefore $g$ is onto). Then $f \circ g \sim_{p} f$
   Simply use the fact that $g \sim id_{I}$ via the straight line homotopy on the convex set $I$.
2. Inserting /deleting a loop to/from a loop given $f:I\to X$ loop at $x_{0}$, given a point $x = f(s)$ on the loop and a homotopically trivial loop $g:I\to X$ at $x$, we get a new loop at $x_{0}$ obtained by concatenating the paths $f_{1}*g*f_{2}$.
   (via any convenient reparameterization in the time domain as in $(i)$) and this loop is path homotopic to $f$. We call this insertion of a loop at x. The reverse process is called deletion.
```tikz
\begin{document}
\begin{tikzpicture}
\draw (0,0) .. controls (1,2) and (3,2) .. (4,0) .. controls (3,-2) and (1,-2) .. (0,0);
\filldraw (0,0) circle (2pt) node[anchor=north] {$x$};
\draw (4,0) .. controls (4.5,1) and (5,1) .. (5.5,0) .. controls (5,-1) and (4,-1) .. (4,0);
\filldraw (4,0) circle (2pt) node[anchor=north] {$x_{0}$};

\end{tikzpicture}
\end{document}
```


## Seifert-Van Kampen theorem (for 2 open sets)

**Theorem:** Suppose $X = U \cup V$ where $U,V, U\cap V$ are path connected. Then for any $x_{0} \in U \cap V$, 
```tikz
\usepackage{tikz-cd}
\begin{document}
\begin{tikzcd}
\pi_{1}(U \cap V,x_{0}) \ar[r,"j_{1*}"] \ar[d,"j_{2*}"] & \pi_{1}(U,x_{0}) \ar[d,"k_{1*}"] \ar[rdd,bend left=15,"\phi_{1}"] & \\
\pi_{1}(V,x_{0}) \ar[drr,bend right=15,"\phi_{2}"] \ar[r,"k_{2*}"] & \pi_{1}(X,x_{0})
\ar[dr,dashed,"\exists ! \phi"] & \\
& & H 
\end{tikzcd}
\end{document}
```
is a push-out square.

**Proof:** **Uniqueness of $\phi$**
Since $\pi_{1}(X)$ is generated by the images of $\pi_{1}(U)$ and $\pi_{1}(V)$ in it, the conditions $\phi_{i} = \phi \circ k_{i*}$ imply that $\phi$ is determined by the values of $\phi_{i}$. This also suggests how to define $\varphi$:  

Given an element in $\pi_1(X)$, write it as a product of loop classes coming from $\pi_1(U), \pi_1(V)$ and apply $\varphi_i$ accordingly and multiply.

**Problem: show it's well-defined!**

Recall the process of factorizing:  

Fix an element in $\pi_1(X, x_0)$.  

Choose a loop $f_0$ representing the homotopy class in $\pi_1(X, x_0)$,  

$$
f : I \to X
$$

Choose points $0 = t_0 < t_1 < \dots < t_n = 1$ such that $x_i := f(t_i) \in U \cap V$, and the path  

$$
f|_{[t_i, t_{i+1}]} \subseteq U \ \text{or} \ V
$$  

for $1 \leq i \leq n-1$.  

Choose paths $\alpha_i : I \to X$  
from $x_0$ to $x_i$  
for $1 \leq i \leq n-1$ (trivial for $i=0, n$)  
in $U \cap V$.

Now $f \sim f_1 * \alpha_1^{-1} * \alpha_1 * f_2 * \alpha_2^{-1} * \alpha_2 * f_3$  
(loops in $U$ or in $V$ at $x_0$).

To define $\phi(([g]))$ we need to set it as  
$\phi_{1,2}([g_1]), \phi_{1,n}([g_n]), \ldots$

The choice of $\phi_1$ or $\phi_2$ depends on whether $g_i$ lies in $U$ or in $V$ and $[g_i]$ is interpreted accordingly. If $g_j$ lies in $U \cap V$ (i.e., in $U \cap V$) then $[g_j]$ stands for its image from
$$
\pi_1(U \cap V) \longrightarrow \pi_1(U) \quad \text{or} \quad \pi_1(V)
$$
but the value of $\varphi_j$ remains the same for either choice, because $\varphi_{j*} = \varphi_{2*} \circ \varphi_{1*}$.

**Claim**: $\varphi([g])$ is independent of all these choices.
In particular, $\varphi$ gets defined at the level of loops themselves and not just at the loop classes. This also implies that $\varphi$ is a homomorphism because doing this process for loops $f, f'$ at $x_{0}$ also does it for $f * f'$.

**Proof:**

Independence of choice of $\alpha_i$.

Suppose we used $\beta_i$ as a path from $x_0$ to $x_i$.

$g_i * g_{i+1}$
$$
= (\alpha_{i-1} * f_i * \alpha_i^{-1}) * (\alpha_i * f_{i+1} * \alpha_{i+1}^{-1})
$$
(in $U \cup V$)
$$
\simeq (\alpha_{i-1} * f_i *  \overline{\beta}_i*\beta_i  * \alpha_i^{-1}) * (\alpha_i *  \overline{\beta}_i*\beta_i  * f_{i+1} * \alpha_{i+1}^{-1})
$$
$$
\simeq (\alpha_{i-1} * f_i * \beta_i) * (\overline{\beta}_i * \alpha_i^{-1} * \alpha_i * \beta_i) * (\overline{\beta}_i * f_{i+1} * \alpha_{i+1}^{-1})
$$
$$
\simeq (\alpha_{i-1} * f_i * \overline{\beta_i}) * (\overline{\beta}_i * f_{i+1} * \alpha_{i+1}^{-1})
$$
(new loops in $U \cup V$) #recheck

We see that $\varphi_{1 \alpha_i} ([g_j'] * [g_{j+1}']) = \varphi_{1 \alpha_i}([g_j'] * [g_{j+1}'])$ because $\alpha_i * \alpha_i'$ is in $U \cap V$.

Independence of the choice of $x_i = f(t_i)$.

It suffices to check this by just adding one point $s \in [0,1]$ such that $y = f(s)$ is in $U \cap V$. For then we can do it finitely many times.
Then given 2 such choices, we may work with their union & compare.

Pick $\beta$ a path in $U \cup V$ from $x_0$ to $y$.

$$
g_{i+1} = \alpha_i * f_{i+1} * \overline{\alpha}_{i+1}
$$

$$
\sim \alpha_i * f_{i+1}'' * \overline{\alpha}_{i+1}
$$

$$
\sim (\alpha_i * f_{i+1} * \overline{\beta}) * (\beta * f_{i+1}'' * \overline{\alpha}_{i+1})
$$
#recheck
$g_{i+1} \hspace{2em} g_{i+1}''$

(diagram: $x_0$ connected to $x_i$, $y$ via $\alpha_i$, $\beta$; loops $f_{i+1}$, $f_{i+1}''$ at $x_i$, $y$)
[see for reference munkres]


3. $\sigma$ is compact and convex (Closed and bounded) and convex. Use the homeomorphism to standard simplex. 
$$
\sum_{}^{} t_{i}a_{i} \leftarrow (t_{0},t_{1},\dots,t_{n},0,\dots,0)
$$
4. For a simplex $\sigma$, $\exists$ one and only one geometrically independent set whose convex span is $\sigma$.
**Proof:** Suppose $\sigma$ is convex span of $\{ a_{0},\dots,a_{n} \}$ and $\{ b_{0},\dots,b_{n} \}$. Suppose,
$$
\begin{gather}
b_{i}= \sum_{}^{} t_{ij} a_{j} \\
a_{k} = \sum_{}^{  } s_{kl}b_{l}
\end{gather}
$$
two of them non-zero
$$
a_{k} = \sum_{l}^{}s_{kl}\left(\sum_{j}^{}t_{lj}aj\right)
$$
**Exercise:** this 

**Solution:**


5. More definitions:
   $(i)$ For a simplex $\sigma$, define its vertices to be the geometric independent set $\{ a_{0},\dots,a_{n} \}$ whose convex span is  $\sigma$. Similarly one can define the edges of $\sigma$ to be the convex span of any 2 vertices in $\sigma$.
   $(ii)$ A face of $\sigma$ more generally, is the convex span of any subset of $\{ a_{0},\dots a_{n} \}$. If the subset has $k$ elements, we call it a $k$-face. The empty set $\varnothing$ is also considered a face. Intersection of any 2 faces is also a faces is also a face, namely the one spanned by the common vertices to the two faces.
   $x \in \sigma$, $x = \sum_{}^{}t_{i}a_{i}, \sum_{}^{}t_{i}=1,t_{i}\geq_{0}$, $t_{i}$ unique.
   $(iii)$ Some times an $(n-1)$-face is called a facet the span of $\{ a_{1},\dots,a_{n} \}$ is the face/facet opposite $a_{0}$.
   $(iv)$ All the faces of $\sigma$ except $\sigma$ itself are called proper faces.
   $(v)$ The boundary of $\sigma$ denoted $Bd(\sigma)=$Union of all proper faces.
   $(vi)$ Interior of $\sigma=$ $\sigma\setminus \partial \sigma$, denoted as $Int(\sigma)$ Thus 
$$
\partial \sigma= \left\{  x = \sum_{}^{}t_{i}a_{i} \mid t_{i}=0 \text{ for atleast one }i \right\}
$$
$$
Int(\sigma) = \left\{  x = \sum_{}^{}t_{i}a_{i} \mid t_{i}>0  \right\}
$$
$(vii)$ Any $x \in \sigma$ lies in the interior of a unique face of $\sigma$ namely, if $x = \sum_{i=0}^{n}t_{i}a_{i}$, then let $\tau$ be the face spanned by the $a_{i}$s for which $t_{i}\neq_{0}$ (i.e., $t_{i}>0$)
Thus,
$$
\sigma = \bigsqcup_{\tau \subseteq \sigma } Int(\tau)
$$
6. $Int(\sigma)$ is convex and open in the affine span of $\{ a_{i} \}$. The closure of $Int(\sigma)$ is $\sigma$. $Int(\sigma) =$ disjoint union of open line segments joining $a_{o}$ to points of the opposite face.
7. $\sigma$ homeomorphic to $B^{n}$ with $\partial \sigma \cong S^{n-1}$ . Given $u \in \mathbb{R}^{N}$, define a ray from u, along $V \in \mathbb{R}^{N}$ to be $\mathscr{R}= \{ u+tv\mid t\geq 0, t \in \mathbb{R} \} \cong \mathbb{R} \geq0$ 
We prove (7) by a more general lemma:
Let $U \subseteq \mathbb{R}^{N}$ be an open bounded convex subset. Let $u \in U$.
(a) Any ray from u intersects $\partial U = \overline{U}\setminus U$ in a unique point.
(b) This induces a homeomorphism $\overline{U} \cong B^{n}$ with $\partial U \cong S^{n-1}$
**Proof:** (a) Under the identification $\mathscr{R}\leftrightarrow \mathbb{R}_{>0}$, we see that $\mathscr{R} \cap U$ corresponds to an open, convex (hence connected) bounded subset of $\mathbb{R}_{\geq0}$, i.e. an interval $[0,a)$ for some $a>0$.	Therefore $u + av \in \overline{U} \setminus U$. Assume WLOG that boundary point is $0$, $v=-u,a=1$ 
Now the open set $W:= \mathbb{R}_{<0}\cdot U$ is disjoint from $U$ because if $-\lambda u_{1} = u_{2}$. $u_{i}  \in U, \lambda >0$.

$$
0 = \frac{\lambda u_{1} + u_{2}}{\lambda + 1}
$$
contradicting the convexity.
Since $u + tv \in W(open)$ for $t>1$ we see that $u + tv \not\in \overline{U}$ for $t>1$ as $U \cap W = \varnothing$. Thus $\mathscr{R} \cap \partial U = \{ 0 \}$.
(b) For the homeomorphism $\overline{U} \cong B^{n}$ we first assume that $0 \in U$
Then $x \mapsto \frac{x}{\lvert x \rvert}$ restricts to a bijective map $\partial U \to S^{n-1}$ by (a) using the ray $\mathscr{R}$ $0+tx$. It is a homeomorphism since $\partial U$ is closed and bounded.
Let $g :S^{n-1} \to \partial U$ denote the inverse map. Now define $G: B^{n}\to \overline{U}$ by 
$$
G(x) = \begin{cases}
\|g\left( \frac{x}{\|x\|} \right)\|x &\text{if }x\neq 0 \\
0  & \text{if } x=0
\end{cases}
$$
G is continuous at $x \neq 0$ in $B^{n}$ clearly. Near $x = 0$ we see that if $\lvert g \rvert< M$ and $\lvert x \rvert<M \delta$. Since G is bijection along each ray (we are also stretching along each ray). It is a bijection. Hence $G$ is a homeomorphism as $\overline{U}$ is compact. $\quad \blacksquare$

**Def:** A simplicial complex $K$ in $\mathbb{R}^{N}$ is a collection of simplices $K= \{ \sigma_{i} \}_{i \in I}$ in $\mathbb{R}^{N}$ such that:
1. Every face of any $\sigma \in K$ is also in K.
2. Intersection of 2 simplices in $K$ is a face of each of them.

**Examples:** 
1. If $\sigma$ is a simplex, then $\sigma$ together with all its faces forms a simplicial complex.
2. ![[Drawing 2025-09-19 16.55.16.excalidraw.svg]]
%%[[Drawing 2025-09-19 16.55.16.excalidraw.md|🖋 Edit in Excalidraw]]%%
3. ![[Drawing 2025-09-19 16.55.58.excalidraw.svg]]
%%[[Drawing 2025-09-19 16.55.58.excalidraw.md|🖋 Edit in Excalidraw]]%%
Not a simplex

#incomplete 

$$
g\left( \sum_{}^{}t_{i}a_{i} \right) = \sum_{}^{} t_{i}g(a_{i}) = \sum_{}^{} t_{i}f(a_{i})
$$
We call the map $g:\lvert K \rvert \to \lvert L \rvert$ defined above as the linear simplicial map induced by the vertex map $f:K^{(0)} \to L^{(0)}$. Here g extends f and it is the unique convex-linear map induced by f.
**Examples:** 
![[IMG_20250926_154625.jpg]]

**Observation:** Composition of 2 linear simplicial maps (induced by suitable vertex maps) is also linear simplicial.
$$
K^{(0)} \xrightarrow{f_{1}} L^{(0)}\xrightarrow{f_{2}} M
$$
maps friendly vertices to friendly vertices
$$
\implies \lvert K \rvert \xrightarrow{g_{1}}  \lvert L \rvert \xrightarrow{g_{2}} \lvert M \rvert 
$$
$g_{2}g_{1}$ is the convex linear map induced by $f_{2}f_{1}$.

The formula $g\left( \sum_{}^{} t_{i}a_{i} \right)= \sum_{}^{} t_{i}g(a_{i})$ holds even if $a_{i}$ are repeated. (the conditions $\sum_{}^{}t_{i} = 1, t\geq 0$ hold after collecting terms)

**Corollary:** If $f:K^{(0)} \to L^{(0)}$ is bijective and both $f,f^{-1}$friendly then the induced map $g:\lvert K \rvert \to \lvert L \rvert$ is a homeomorphism.
(Use $f \circ f^{-1} = Id_{L^{(0)}}$, $f^{-1}\circ f = Id_{K^{(0)}}$)

In this case we call $g$ a simplicial homeomorphism/isomorphism.

**Proposition:** Any finite simplicial complex with M vertices is isomorphic to a subcomplex of a simplicial complex $\Delta^{M}$ consisting of an M-simplex and its faces.

**Proof:** Let $K^{(0)} = \{ v_{0},\dots,v_{M} \}$. Consider any $M$-simplex in $\mathbb{R}^{M}$, e.g the one given by the basis vectors $e_{i}$ in $\mathbb{R}^{M}$ as vertices. Call $\Delta^{M}$ the corresponding simplicial complex. We have a vertex map $f:K^{(0)} \to \{ e_{0},\dots,e_{M} \}$ sending $v_{i}$ to $e_{i}$ which is clearly friendly since $\{ e_{i} \}$ are geometrically independent. We look at the subcomplex of $\Delta^{M}$ given by the simplices spanned by $f(v_{0}),\dots,f(v_{n})$ whenever $v_{0},\dots,v_{n}$ are friendly. ( This clearly gives a subcomplex of $\Delta^{M}$) It is clear that $K$ is isomorphic to the subcomplex $L$.

$\lvert K \rvert \xrightarrow{\sim}  \lvert L \rvert \hookrightarrow \lvert \Delta^{M} \rvert$. This $\lvert K \rvert$ is identified isomorphically with a (closed) subcomplex of $\lvert \Delta^{M} \rvert$.

Thus $E^{J}$ is the subspace spanned by the linearly independent set $\{ e_{j} \}_{j \in J}$. We give $E^{J}$ the topology coming from the norm given by
$$
\| x\| = \max_{j \in J} \{ |x_{j} |\}
$$

We work with finite dimensional simplices in $E^{J}$: 
Clearly $E^{J}$ is preserved under convex linear combinations. Each $\mathbb{R}^{N}$ con be embedded in $E^{J}$ in the obvious way. Given finitely many points $a_{0},\dots ,a_{n} \in E^{J}$, the $a_{i}$'s and their convex linear combinations lie in $\mathbb{R}^{N}$ for some $N$. So we work with finite dimensional simplices in the usual way.
A simplicial complex $K$ in  $E^{J}$ could have infinitely may simplices of possibly unbounded dimensions. A subset $S \subseteq E^{J}$ is called geometrically independent if every finite subset is geometrically independent.
$$
\Delta^{J} := \text{all finte dim simplices in $\mathbb{E}^{J}$ on the vertices $\{ e_{j} \}_{j\in J}$}
$$
We also call $\Delta^{J}$ a simplex in $E^{J}$.
## Abstract Simplicial Complex

**Def:** An abstract simplicial complex is a collection $\mathscr{S}$ of non-empty finite sets such that $A \in \mathscr{S}$ and $B \subseteq A \implies B \in \mathscr{S}$.

Any $A \in \mathscr{S}$ is called a simplex in $\mathscr{S}$.  $\dim(A):= \lvert A \rvert - 1$. If $B \subseteq A, B \neq \varnothing \}$, then B is called a face of A. $\dim (\mathscr{S}):= \sup_{A \in \mathscr{S}} \{ dim(A) \}$, The vertex set of $\mathscr{S}$, $V(\mathscr{S}) =$ the union of all singletons in $\mathscr{S}$.
We make no distinction between v and $\{ v \}$ for vertices. Thus $\mathscr{S} \subseteq 2^{V(\mathscr{S})}$, $\mathscr{S'} \subseteq \mathscr{S}$ is called a subcomplex if it is preserved under taking subsets. $\mathscr{S,T}$ are called isomorphic if $\exists$ a bijection $f: V(\mathscr{S}) \to V(\mathscr{T})$ such that $\{  a_{0},\dots,a_{n} \} \in \mathscr{S}$ iff $\{ f(a_{0}),\dots,f(a_{n}) \} \in \mathscr{T}$.

Let $K$ be a simplicial complex in $E^{J}$ with vertex set $K^{(0)}$ then we may associate to $K$, an abstract simplicial complex $\mathscr{K}$ by using $K^{(0)}$ as its vertex set, i.e, $\{ a_{0},\dots,a_{n} \} \subseteq K^{0}$ is declared to be in $\mathscr{K}$ iff they span a simplex in K. We call $\mathscr{K}$ the vertex scheme of K.

**Theorem:**
1. Every abstract simplicial complex $\mathscr{S}$ is isomorphic to the vertex scheme of a simplicial complex K.
2. Two simplicial complexes K,L are isomorphic iff their vertex schemes are isomorphic (as abstract simplicial complex).

**Proof:**
1. Let $V = V(\mathscr{S})$, the vertex set. Then we look at $K \subseteq \Delta^{V}$($\subseteq E^{V}$) constructed by the condition $\sigma =$ convex span of $e_{v_{0}},\dots,e_{v_{n}} \in K$ iff $\{ v_{0},\dots,v_{n} \} \in \mathscr{S}$. By construction $K$ is a simplicial complex(satisfies conditions (1) and (2) ). The vertex scheme of $K$ is exactly $\mathscr{S}$ by construction.
2. $K \cong L \implies \mathscr{K} \cong \mathscr{L}$ by definition of $K$. Now conversely we have a bijection $K^{(0)} \leftrightarrow L^{(0)}$


**Simplicial complex vs. Abstract simplicial complex**
$K \rightsquigarrow V = \mathscr{K}^{(0)}\rightsquigarrow \mathcal{K} =$ all finite subsets of $V$ corresponding to simplices in $\mathcal{K}$. 

Subcomplex of $\Delta^V \subset \mathbb{R}^V$ corresponding to the elements of $\mathcal{S}$ (Geometric realization of $\mathcal{S}$)$\leftarrow V \leftarrow \mathcal{S}$

**Examples:** We'll cut open the top spaces we're interested in.
1. Hollow triangle $\cong S^{1}$.
2. Cylinder.
3. Mobius strip.
4. Torus.
5. Klein bottle.
6. **Exercise:** check below
Let L be a finite simplicial complex (e.g opened up rectangles as above). Suppose $\exists$ an onto function $V(L) \xtwoheadrightarrow{f} W(\text{ a set of labels for vertices of quotient figure})$

To define a new simplicial complex via f, we first construct an abstract simplicial complex $\mathscr{K} \subseteq 2^{W}$ by the condition:
$$
\{ f(v_{0}),\dots,f(v_{n}) \} \in \mathscr{K} \iff \{  v_{0},\dots,v_{n} \} \text{ spans a simplex in L}
$$
It is easy to check that $\mathscr{K}$ is an abstract simplicial complex. Set $K:=$ geometric realization of  $\mathscr{K}$. Then we have an onto map $V(L) = L^{(0)} \xtwoheadrightarrow{f} K^{(0)}=W$ which sends friendly vertices to friendly ones. This induces a linear map $\lvert L \rvert \xrightarrow{g} \lvert K \rvert$. This is a closed surjective map and hence a quotient map.
$$
\sum_{}^{} t_{v}v \mapsto \sum_{}^{} t_{v}f(v) 
$$
Thus for any $w \in W = K^{(0)}$, if $v_{0},\dots,v_{k}  \in f^{-1}(w)$, then the simplex $\sigma$ spanned by $v_{0},\dots,v_{l}$ maps to w under g.
Similarly, if $v_{1},v_{2} \in f^{-1}(w)$ and $v_{1}',v_{2}' \in f^{-1}(w')$ then the simplex spanned by $v_{1},v_{2},v_{1}'$ maps to the edge $\overline{w}w'$ and 

Sufficient criterion for $h_*(L)$ and $h_*(L_0)$ to be equal
**Def:** Let $L_0 \subseteq L$ be a subcomplex. We say $L_0$ to be a **full subcomplex** if whenever its vertex space simplex $\sigma$ in $L_0$, we also have $\tau \subseteq \sigma$.

**Def:** Let L be a complex and $v \in L^{(0)}$. We define subsets 
$$
\begin{gather}
St(v):= \bigcup_{v \in \sigma}^{} Int(\sigma ) \\
\overline{St(v)} := \text{closure of }St(v) &= \bigcup_{v \in \sigma }^{} \sigma \\
Lk(v) := \overline{St(v)} \setminus St(v)
\end{gather}
$$

Note that the complement of $St(v)$ is $\bigcup_{v \not \in \sigma }^{} \sigma$ which is also the underlying set of a subcomplex of $\sigma$ ($v \not\in \sigma \implies v \not\in \text{any face of } \sigma$)
**Example:**
![[IMG_20250929_160051.jpg]]

We observe that $St(v)$ is path-connected (as each $x$ is path-connected to $v$) and so is $\overline{St(v)}$. However, $Lk(v)$ may not be connected.

---

**Criterion:** Let $L$ be a complex and $f: |L| \to W$ a surjective function. Let $g: |L| \to |K|$ be the associated quotient map. Let $L_0$ be a full subcomplex such that for any $v_1, v_2 \in L$ lying in the same fiber on $g$, we have:
(i) $v_1v_2 \in L_0$
(ii) $St(v_1) \cap St(v_2) = \phi$

Then $\dim(g(\sigma)) = \dim(\sigma)$ for any $\sigma \in L$. Moreover, if $g(\sigma_1) = g(\sigma_2)$, then $\sigma_1, \sigma_2$ are disjoint simplices.

**Proof:** **Exercise**

## Simplicial homology groups
(Abelian groups associated to simplicial complexes)

Let $\sigma$ be a simplex with vertices $a_{0},\dots,a_n$, then the set of permutations of $\{ a_{1},\dots,a_{n} \}$ may be divided into 2 equal groups, namely odd and even permutations.

An orientation on $\sigma$ is the choice of anyone of these 2 classes. An oriented simplex is a simplex $\sigma$ with a choice of an orientation on it. For $n=0$ there is no choice and $\sigma$  is consider oriented by default.
![[IMG_20251006_142242.jpg]]

**Notation:** For simplex $\sigma$ with ordered vertices $(v_{0},\dots,v_{n})$ we use $[v_{0},\dots,v_{n}]$ to denote the corresponding oriented simplex. We often denote the oriented simplex also by $\sigma$. 

**Def:** Let $K$ be a simplicial complex geometric or abstract. For any integer $p$ (if $0\leq p\leq \dim(K)$) we define a $p$-chain on $K$ to be a function $c$ from the set of oriented $p$-simplices of $K$ to $\mathbb{Z}$ such that:

1. $c(\sigma) = - c(\sigma')$ for opposite oriented simplices $\sigma,\sigma'$
2. $c(\tau)=0$ for all but finitely many $p$-simplices $\tau$ in $K$

We define $C_{p}(K) =$ the set of all $p$-chains with obvious group structures coming from $\mathbb{Z}$ for $0\leq p\leq \dim(K)$. For other $p$, we set $C_{p}(K)=$ trivial group

Let $\sigma$ be an oriented simplex and $\sigma'$ the oppositely oriented one. We define the associated elementary $p$-chain to be the p-chain satisfying $c(\sigma)=1$ (Therefore $c(\sigma')=-1$), $c(\tau)=0, \forall \tau\neq \sigma,\sigma' \in K$.

By abuse of notation🫠 we call this elementary p-chain also as $\sigma$. We write the corresponding elementary p-chain of $\sigma'$, the oppositely oriented version of $\sigma$, as $-\sigma$ The following properties are easy to see:
1. $C_{p}(K)$ is a free abelian group with basis as elementary p-chains obtained by arbitrarily orienting each p-simplex on $K$. $\left[ c(\sigma_{i})=\lambda_{i},\forall i\implies c=\sum_{}^{}\lambda_{i}\sigma_{i} \right]$
2. Any function from the set of oriented p-simplices in $K$ to an abelian group $G$  uniquely extends to a homomorphism $g:C_{p}(K)\to G$ provided $f(\sigma) = -f(\sigma)$ whenever $\sigma,\sigma'$ are opposite orientation of the same simplex. ( Universal property of free abelian groups)

**Temporary Notation:** An n-simplex with ordered vertices $(v_0, \ldots, v_n)$, we define ${\sigma_{(i)}}$to be the face opposite to the $v_i$ with ordered vertices $(v_{0},\dots,\widehat{v_{i}},\dots,v_{n})$. Similarly $\sigma_{(i,j)}$ for $i<j$ is given by $(v_0, \dots, \hat{v_i}, \dots, \hat{v_j}, \dots, v_n)$.

**Definition:** $K$ = simplicial complex (abstract/geometric) We define a homomorphism $\partial_p: C_p(K) \to C_{p-1}(K)$ called the $p^{th}$ boundary operator defined for $0 \leq p \leq \dim(K)$ as follows. Let $\sigma$ be a p-simplex with ordered vertices $(v_0, \dots, v_p)$. Then $\partial_p \sigma := \sum (-1)^i \sigma_{(i)}$.

By condition (ii) above, this would define $\partial_p$ completely provided the above formula remains so over the equivalence class $[v_0, \dots, v_p]$ of $(v_0, \dots, v_p)$ and that at the level of oriented simplices $\partial_{p}\sigma' = -\partial_{p}\sigma$.

All of this amounts to proving that both sides of $(*)$ gets multiplied by $-1$ if we interchange 2 consecutive vertices $v_{j},v_{j+1}$

(The symmetric group $S_p$ is generated by such transpositions $(j, j+1)$.)
$$
(*) \quad \partial_p(v_0, \ldots, v_p) = \sum_{i=0}^p (-1)^i (v_0, \ldots, \hat{v_i}, \ldots, v_p)
$$
$$
= (v_1, \ldots, v_p) - (v_0, v_2, \ldots, v_p) + \ldots + (-1)^p (v_0, \ldots, v_{p-1}).
$$
We compare the R.H.S. of $(*)$ for
$\partial_p(v_0, \ldots, v_j, v_{j+1}, \ldots, v_p)$ vs $\partial_p(v_0, \ldots, v_{j+1}, v_j, \ldots, v_p)$.
For $i \neq j, j+1$ the RHS ith terms are negative of each other. The orders differ by a transposition, for $i=j$ of first simplex, we get same ordering as $i=j+1$ of 2nd simplex. Similarly for $i=j+1$ of first simplex and $i=j$ of second. Thus RHS of second simplex is $(-1)$ times RHS of first, Since the LHS also has the same property, we're done.

---
**Examples:** (We will often write $\partial_{p}$ as $\partial$)
1. $\sigma =[v_{0},v_{1}]$, $\partial \sigma = v_{1} - v_{0}$, where $\sigma \in C_{1}(K),v_{i}\in C_{0}(K)$.
$$ 
\begin{gather*} C_1(K) = \mathbb{Z}\sigma, \quad C_0(K) = \mathbb{Z}v_0 \oplus \mathbb{Z}v_1. \\ \partial_1: \mathbb{Z}\sigma \to \mathbb{Z}v_0\oplus\mathbb{Z}v_1. \\ n \mapsto (-n, n). \end{gather*} 
$$
2. $\sigma = [v_0, v_1, v_2]$, $\partial\sigma = [v_1, v_2] - [v_0, v_2] + [v_0, v_1]$. $$ = [v_1, v_2] + [v_2, v_0] + [v_0, v_1]. $$ $C_2(K) = \mathbb{Z}[v_0,v_1,v_2]$, $C_1(K) = \mathbb{Z}[v_0,v_1]+\mathbb{Z}[v_1,v_2]+\mathbb{Z}[v_2,v_0]$. $C_0(K) = \mathbb{Z}v_0\oplus\mathbb{Z}v_1\oplus\mathbb{Z}v_2$. 

$$ 
\mathbb{Z}\xrightarrow{n\mapsto(n,n,n)} \mathbb{Z}\oplus\mathbb{Z}\oplus\mathbb{Z} \xrightarrow{(a,b,c)\mapsto(b-a, c-b, a-c)} \mathbb{Z}\oplus\mathbb{Z}\oplus\mathbb{Z} 
$$
3. $\sigma$ = tetrahedron, $\sigma = [v_0, v_1, v_2, v_3]$
$$
\partial\sigma = [v_1, v_2, v_3] - [v_0, v_2, v_3] + [v_0, v_1, v_3] - [v_0, v_1, v_2]
$$
$$
0 \to C_3 \xrightarrow{\partial_3} C_2 \xrightarrow{\partial_2} C_1 \xrightarrow{\partial_1} C_0 \to 0
$$
$$
\mathbb{Z} \to \mathbb{Z}^4 \to \mathbb{Z}^6 \to \mathbb{Z}^4
$$

**Lemma:** $\partial_{p-1}\circ\partial_p = 0 \quad \forall p$ 
**Proof:** For $\sigma$ ordered by $(v_0, \ldots, v_p)$ we see that $$ (\partial_{p-1}\circ\partial_p)(\sigma) = \partial_{p-1}\left(\sum_{i=0}^p (-1)^i \sigma_{(i)}\right) = \sum_{i=0}^p (-1)^i \partial_{p-1}(\sigma_{(i)}) \quad \text{(by linearity)} $$ which expands to 
$$
\sum_{i=0}^p (-1)^i \left[ \sum_{j<i} (-1)^j \sigma_{(i,j)} + \sum_{j>i} (-1)^{j-1} \sigma_{(i,j)} \right] 
$$
We check that this is 0. Indeed the terms get cancelled in pairs (total $(p+1)p$ terms) as for $k<l$, $\sigma_{k,l}$ appears twice.
$$
(-1)^l(-1)^k \quad \text{if we remove } v_l \text{ first and then } v_k.
$$
$$
(-1)^{l-1}(-1)^k \quad \text{if we remove } v_k \text{ first and then } v_l.
$$
Therefore sum is 0. $\quad \blacksquare$

---

The sequence of maps $\cdots \to C_p(K) \xrightarrow{\partial_p} C_{p-1}(K) \xrightarrow{\partial_{p-1}} C_{p-2}(K) \to \cdots$ is called the (algebraic) **chain complex** of $K$.

For any $p \in \mathbb{Z}$, we define the group of **p-cycles** to be
$$
Z_p(K) = \{ c \in C_p(K) \mid \partial_p c = 0 \}.
$$
i.e., these p-chains whose boundary is 0.

The group of **p-boundaries** is
$$
B_p(K) = \{ \partial_{p+1}c \mid c \in C_{p+1}(K) \}.
$$
Thus $B_p(K) \subseteq Z_p(K) \subseteq C_p(K)$.

**Def:** We define the p-th **homology group** of $K$ to be
$$
H_p(K) := \frac{Z_p(K)}{B_p(K)} \quad \left[\text{Note that } \frac{C_p(K)}{Z_p(K)} \cong B_{p-1}(K) \right] \quad \text{Exercise.}
$$

**Examples**
1. **Hollow Triangle**
$K = \{ v_0, v_1, v_2, e_{01}, e_{12}, e_{20} \}$. $\dim(K)=1$.
The chain complex is
$$
0 \to C_1 \xrightarrow{\partial_1} C_0 \to 0
$$
$$
C_1 = \mathbb{Z}e_{01} \oplus \mathbb{Z}e_{12} \oplus \mathbb{Z}e_{20} \to C_0 = \mathbb{Z}v_0 \oplus \mathbb{Z}v_1 \oplus \mathbb{Z}v_2.
$$
The map is: 
$$ 
\partial_1 (a, b, c) = (c-a, a-b, b-c) 
$$
 $$
H_0(K) = \frac{Z_0(K)}{B_0(K)} = \frac{\{ (a, b, c) \mid c=b=a \}}{0} = a(1, 1, 1) 
$$

$$
\therefore \underbrace{ H_0(K) \cong \mathbb{Z} }_{ (1, 1, 1) \mapsto  1  } 
$$

$$
H_0(K) = \frac{Z_0(K)}{B_0(K)} = \frac{C_0}{\text{im}(\partial_1)}
$$

Now consider the map

$$
\phi: C_0 \to \mathbb{Z}
$$

$$
(x, y, z) \mapsto x+y+z
$$

Then we see that $\text{im}(\partial_1) \in \ker\phi$ and $\phi$ is onto. Finally observe that $\ker(\phi) \subseteq \text{im}(\partial_1)$ and hence they are equal. (Given $x+y+z=0$, try $c=0$, $a=-x$, $b=z$. )

Thus,
$$
H_0(K) = \frac{C_0}{\text{im}(\partial_1)} = \frac{C_0}{\ker(\phi)} \cong \mathbb{Z}
$$
$$
\overline{v_2} = \overline{v_1} = \overline{v_0} \quad \longleftarrow \quad 1
$$
2) Same triangle with one edge oriented the other way.
$K = \{ v_0, v_1, v_2, e_{01}, e_{12}, e_{20} \}$.
$$
\mathbb{Z}e_{01} \oplus \mathbb{Z}e_{12} \oplus \mathbb{Z}e_{20} \to \mathbb{Z}v_0 \oplus \mathbb{Z}v_1 \oplus \mathbb{Z}v_2.
$$
$$
(a, b, c) \mapsto (-c-a, a-b, b+c)
$$



![[IMG_20251010_161556.jpg]]

**Exercise:** Check again that $H_0(K) \cong \mathbb{Z}$, $H_1(K) \cong \mathbb{Z}$.

3) $L=$ **solid triangle**
i.e., $L = \sigma$ 2-simplex (with faces).
The chain complex is
$$
0 \to C_2 \xrightarrow{\partial_2} C_1 \xrightarrow{\partial_1} C_0 \to 0
$$
$$
C_2 \cong \mathbb{Z}\sigma, \quad C_1 \cong \mathbb{Z}e_{01}\oplus\mathbb{Z}e_{12}\oplus\mathbb{Z}e_{20}, \quad C_0 \cong \mathbb{Z}v_0\oplus\mathbb{Z}v_1\oplus\mathbb{Z}v_2.
$$
The boundary of the 2-simplex $\sigma$:
$$
\partial_2 \sigma = [v_1, v_2] - [v_0, v_2] + [v_0, v_1] \quad \text{(i.e., the formal sum of the faces)}
$$

From earlier calculation, we saw that $H_0(L) \cong \mathbb{Z}$.

$Z_{1}(L) = Z_{1}(K)$ as before, while $B_{1}(L)=im(\partial_{2})=\mathbb{Z}(1,1,1)=Z_{1}(1)$. Thus $H_{1}(L)=0$. Finally, since $\partial_{2}$ is injective, we see that $Z_{2}(L)=0$. Therefore $H_{2}(L)=0$.


![[IMG_20251010_164039.jpg]]

4) $K = \text{solid tetrahedron}$
$= 3\text{-simplex}$

The chain complex is: #recheck 
$$
0 \to C_3 \xrightarrow{\partial_3} C_2 \xrightarrow{\partial_2} C_1 \xrightarrow{\partial_1} C_0 \to 0
$$
$$
\mathbb{Z} \xrightarrow{n \mapsto (-n, n, n, n)} \mathbb{Z}^4 \xrightarrow{(a,b,c,d) \mapsto (a+b, c-a, -b, a+d, b+d, c+d)} \mathbb{Z}^6 \xrightarrow{} \mathbb{Z}^4
$$
![[IMG_20251010_165537.jpg]]
Simplex basis for the chains:
$C_3$: $[0123]$
$C_2$: $[012], [013], [023], [123]$
$C_1$: $[01], [02], [03], [12], [13], [23]$
$C_0$: $0, 1, 2, 3$

$$
\partial_3 [0123] = [123] - [023] + [013] - [012]
$$

Easy to see that $H_3 \cong 0 \cong H_2$.
**Exercise:** $H_1 \cong 0, H_0 \cong \mathbb{Z}$.

Geometrically, when is a 1-chain a 1-cycle in a simplicial complex $K$?
![[IMG_20251010_170132.jpg]]


1-cycle is also a boundary, hence gives 0 element in the homology. Consider the 1-cycle $e_{1}+e_{2}+e_{3} +e_{4} = \partial(\sigma+\tau)$. It is a boundary because $\partial \sigma = e_{1} - e_{5} + e_{4}, \partial(\tau)= e_{5}+e_{2}+e_{3}$.
![[IMG_20251010_171522.jpg]]

**Heuristics:** 1-chain is a 1-cycle iff it is an abelian sum of simple 1-cycles = simple loops. 1-cycle gives the 0-element in $H_1$ if it can be filled, i.e., $\partial(\text{2-chain})$. $H_1$ measures the presence of **1-dim'l holes** in $|K|$.

Similarly one expects $H_n(K)$ to measure the size of $n$-dimensional holes in $|K|$.

We say that a $p$-chain $c \in C_p(K)$ is **homologous to 0** or $c$ **bounds** / is a **boundary** if $c = \partial_{p+1} d$ for some $(p+1)$-chain $d$. In this case $c$ is also a $p$-cycle and its image in $H_p(K)$ is $0$.
(In general, for a $p$-cycle $c$, its image in $H_p(K)$ is called its **homology class**.)

---

We say that 2 $p$-chains $c, c'$ are **homologous** (to each other) if $c-c'$ is homologous to 0.

We say that a $p$-chain $c$ is **carried by a subcomplex $L \subseteq K$** (or $c$ is **supported in $L$**) if $c$, thought of as a function on the set of oriented simplices in $K$, is 0 on the simplices not in $L$.

**Example**
![[IMG_20251013_144546.jpg]]
$M = \text{2-simplices}$ and its subsimplices.
We'll prove that $H_1(M) \cong \mathbb{Z} \cong H_2(M)$.

Let $\alpha$ be a 1-cycle on $M$. Then $\alpha = \sum_{i=1}^8 \lambda_i e_i$. We can knock down one of the coefficients. For example, $\alpha' = \alpha + \lambda \partial \sigma$.
$\partial \sigma$ has $0$ coefficients for $e_1$ and so $\alpha'$ and $\alpha$ are homologous $(\alpha'-\alpha = \lambda\partial\sigma)$.
Let $\alpha' = \sum_{i \geq2} \lambda'_i e_i'$.

Now consider $\alpha'' = \alpha' + \lambda_2 '\partial\sigma_2$. Then $\alpha''$ is homologous to $\alpha'$ (and $\alpha$) and $\alpha'' = \sum_{i \ne 3} \lambda_i e_i$ as $\partial\sigma_2$ has no coeff for $e_1$.

Finally $\alpha''' = \alpha'' + \lambda_3'' \partial\sigma_3$ is homologous to $\alpha'', \alpha'$ and $\alpha$.
And $\alpha'''$ is supported on the subcomplex.

(1-dimensional subcomplex).
Moreover, $\alpha$ is a 1-cycle if $\alpha', \alpha'', \alpha'''$ are.
Finally we see that if $\alpha''' = \sum_{i \geq 4} \lambda_i e_i$,
then $\lambda_4''' = 0$ because the coefficient of $\alpha$ in $\partial \alpha'''$ is $\lambda_4'''$ and $\partial \alpha''' = 0$ as $\alpha'''$ is a 1-cycle.
Thus every cycle $\alpha$ is homologous to a cycle supported on the outer square.

---

![[IMG_20251013_150850.jpg]]
Now, if $\alpha$ is a 1-cycle supported on the outer square, then with
$\alpha = \sum_{i \ne 5}^8 k_i e_i$, we see that $\lambda_5 = \lambda_6 = \lambda_7 = \lambda_8$.
$(\partial \alpha)(v_2) = \lambda_5 - \lambda_6$; $\lambda_5 = \lambda_6$ as $\partial \alpha = 0$.

Similarly $(\partial \alpha)(v_3) = \lambda_6 - \lambda_7 \implies \lambda_6 = \lambda_7$, etc...
Thus $\alpha = n (\sum_{i \ne 5}^8 e_i)$ which is in fact $\partial(\sigma_1 + \sigma_2 + \sigma_3 + \sigma_4)$
as $\partial (\sigma_i) = e_5 + e_6 - e_1 \ldots$ ($e_1, e_2, e_3$ get cancelled out).
Thus $H_1(M)=0$.

If $\beta$ is a 2-cycle, then $\beta = n_1 \sigma_1 + n_2 \sigma_2 + n_3 \sigma_3 + n_4 \sigma_4$.
Now $\partial \beta(e_1) = n_1 \implies n_1=0$.
$0$ (since $\beta$ is a 2-cycle).
Similarly $n_2=0$ because $\partial\beta(e_2)=0$.
$n_3=0$

---

**Lemma:** Let $L$ be the **simplicial complex** as shown
![[IMG_20251013_155608.jpg]]
$Bd(L)=$ outer rectangle (12 vertices, 12 edges).
We orient each 2-simplex $\sigma_i$ anticlockwise and 1-simplex arbitrarily. Then
1. Every 1-cycle $\alpha$ of $L$ is homologous to a 1-cycle supported on the boundary $Bd(L)$.
2. If $\beta$ is a 2-chain of $L$ such that $\partial \beta$ is supported on $Bd(L)$, then $\beta$ is a $\mathbb{Z}$-multiple of $\sum \sigma_i$.

**Proof:** This is similar to the previous example:
1. We first check that any 1-cycle $\alpha$ is homologous to a 1-cycle supported on the figure
![[IMG_20251013_160027.jpg]]
We may therefore assume that $\alpha$ is supported on the outer square. Next we see that the coefficients of $\alpha$ along the 4 inner hanging edges is $0$ since $\partial\alpha(v_i)=0$. This proves (1). (2) Since $\partial\beta$ is supported on $Bd(L)$, hence $\partial\beta(e)=0$ for any edge $e$ not in $Bd(L)$. But $e$ occurs in exactly 2 2-simplices, say $\sigma$ and $\xi$, and since $\sigma$ and $\xi$ are oriented anti-clockwise.

$\partial\sigma$ and $\partial\xi$ are negatives of each other and equal $\pm e$.

Therefore if $\beta = \sum n_i \sigma_i$, then $\partial\beta=0$ forces $n_1=n_2$.

Doing this for every edge not in $Bd(L)$ shows that all the $n_i$'s are equal. This proves (2). $\quad \blacksquare$

**Theorem** Let $L=$  with $T = L/\sim$ (Torus).
![[IMG_20251013_161332.jpg]]
The edges of the large square are identified according to the labels: $a, b, c, d$ along the top, bottom, left, and right sides.

Orient each 2-simplex $\sigma$ in $L$ anti-clockwise and induce this orientation on the 2-simplices of $T$.
Then
(a) $H_2(T) \cong \mathbb{Z}$, a generator being $\sum \sigma$.
(b) $H_1(T) \cong \mathbb{Z} \oplus \mathbb{Z}$, generators being cycles.
(c) $H_0(T) \cong \mathbb{Z}$, generated by any vertex.

**Proof:** Consider the induced map $g: |L| \to |T|$.
It is a quotient map. Then the outer rectangle $Bd(L)$ maps to a subset $A \subseteq T$ which looks like: [Diagram of two triangles joined by an edge, with vertices labeled and edges a, b, c labeled].
![[IMG_20251013_162648.jpg]]
Using the previous lemma, we get:
(1) Every 1-cycle on $T$ is homologous to a 1-cycle supported on $A$.
(2) If $\beta$ is a 2-chain such that $\partial\beta$ is supported on $A$, then $\beta$ is a $\mathbb{Z}$-multiple of $\sum \sigma$.
In addition we have:
1'. If $\alpha$ is a 1-cycle supported o A, then $\alpha=mw+mz$ for $m,n \in \mathbb{Z}$
(2') $\partial_{2}(\sum \sigma_{i}) = 0$.

Indeed for (1') we use that $A = \text{[Diagram of identified edges forming a square]}$
![[IMG_20251013_163732.jpg]]
and look at each vertex to get the desired form $(\partial\alpha=0)$.
While (2') holds because $(\partial_2(\sum \sigma_i))(e) = 0$ for all edges by direct calculation as all 2-simplices are oriented anti-clockwise.
Now we prove:
(a) If $\beta$ is a 2-cycle, then $\partial\beta = 0$, and hence by (2), $\beta = n \sum \sigma_i$, which is a 2-cycle. $\implies H_2(T)$ is generated by $\sum \sigma_i$.

---

Since there are no 3-cycles, the 2-boundaries are $0$.
$$
H_2(T) \cong \mathbb{Z} \quad \text{with generator } \sum \sigma_i.
$$
(b) If $\alpha \in H_1(T)$, by (1), $\alpha$ may be assumed to be supported on $A$. Hence by (1'), $\alpha = m\omega + n\xi$, etc.
$H_1(T)$ is generated by $\omega, \xi$. Now if $\alpha$ is homologous to $0$, then $\alpha = \partial_2 \sigma$ and by (2) $\beta = \sum_{}^{}\sigma_{i}$ and by (2') $\partial_{2}\beta = 0$.