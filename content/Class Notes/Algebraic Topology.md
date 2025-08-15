---
title: Algebraic Topology
tags:
  - "#incomplete"
  - refactor
created: 2025-07-28
draft: false
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
![[SVG/tikz1755255104.130486.svg|diagram]]
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

![[SVG/tikz1755255105.7454216.svg|diagram]]

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


![[SVG/tikz1755255107.3686643.svg|diagram]]

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

![[SVG/tikz1755255108.9625883.svg|diagram]]


Example : $p : \mathbb{R} \to S^{1}$
i) $f: I \to S^{1}$  ,$f(s) = (\cos \pi s, \sin \pi s)$ , $\tilde{f}(s) = \frac{s}{2}$ is a lift and so is $s \mapsto \frac{s}{2} + h$
ii) $g(s) = (\cos \pi s, -\sin \pi s)$ $\tilde{g}(s) = -\frac{s}{2} + n$
iii) $h(s) = (\cos 4\pi s, \sin 4 \pi s)$ $\tilde{h}(s) = 2s + n$

### Lifting theorems
**Theorem:** (Lifting of paths) Let $p:(E,e_{0}) \to (B,b_{0}$ be a covering map. Then any path $f: I \to B$ starting at $b_{0}$ lifts uniquely to a path $\tilde{f}:I\to E$ starting at $e_{0}$
![[SVG/tikz1755255110.5278277.svg|diagram]]

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
**Lemma:** Consider $p:\mathbb{R} \to S^{1}$ $t \mapsto e^{\pi it}$ . Let $f: I \to  S^{1}$ be a path with $f(0) =a \in S^{1}$ and let $\widetilde{f}$ be a lift of f with $\widetilde{f}(0) = x \in \mathbb{R}$ If $\widetilde{f}(1) = x+r$ for some $r \in \mathbb{R}$ then for any other lift $\tilde{f_{1}}$ of $f$ implies $\tilde{f_{1}}(0) = y \implies tilde{f_{1}}(1) = y + r$ 

**Proof:** Since $\widetilde{f}$ and $\tilde{f_{1}}$ lift f, $p(x) = p(y) = a$. $\implies y -x \in \mathbb{Z}$ say $y = x+d$ for some $d \in \mathbb{Z}$. Then $s \mapsto \widetilde{f}(s)+d$ is also a lift of f starting at x+d = y.

$\implies f_{1} = \widetilde{f} + d$ by uniqueness. $\widetilde{f}(1) = \widetilde{f}(1) + d = x+r+d=y+r \quad \blacksquare$
**Theorem:** $p_{1}(S^{1},1) \cong (\mathbb{Z},+)$ as  groups

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
![[SVG/tikz1755255112.0316463.svg|diagram]]

Given $g:S^{1} \to X$ we obtain $f:I\to X$ as the composite
$$
I \to S^{1} \to X
$$

It is easily seen to be a 1-1 correspondence

If $f_{1},f_{2}$ are 2 path homotopic loops at $x_{0}$ via $F:I\times I \to X$
then 
![[SVG/tikz1755255113.5982847.svg|diagram]]
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

![[SVG/tikz1755255115.0343058.svg|diagram]]
$$
\lVert tf(x) + (1-t)x \rVert =1
$$

This gives a quadratic equation in t, We look for the non positive root of this, which is a continuous function of x.

This continuous function is a retract of the disk to a circle, which is a contradiction. $\quad \blacksquare$

**Recall**: $(X,x_{0})$ 🗿-space
$$
\{ f:I \to X \text{ at } x_{0} \} \leftrightarrow  \{ \text{maps } (S^{1},1) \to (X,x_{0}) \}
$$

![[SVG/tikz1755255116.5445564.svg|diagram]]

This correspondence preserves base point fixed homotopy.

**Exercise:**  Show that the Brouwer fixed point theorem implies that every continuous map $f: S^{n} \to S^{n}$ has a fixed point.

**Lemma:** Let $h:S^{1} \to X$ be a map. Then the following are equivalent.
i) $h$ is null-homotopic.
ii) h extends to a map $k:B^{2} \to X$
iii) $h_{*} : \pi_{1}(S^{1}) \to \pi_{1}(X)$ is the trivial map

**Proof:** $(i) \implies (ii)$
![[SVG/tikz1755255117.9958138.svg|diagram]]


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

E.g.: A deformation retract $j:A\to X$ is a homotopy eq. Indeed with $\gamma:X\to A$ the retract, we have $r\circ j = Id_{A}$ while $j \circ r \sim Id_{x}$ via the deformation retraction H.

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
a)
![[SVG/tikz1755255119.2643483.svg|diagram]]



![[out.svg]]










