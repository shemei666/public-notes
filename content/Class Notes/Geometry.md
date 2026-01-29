---
publish: true
---
# Affine Geometry

**Def**: Affine Space $(\mathscr{A}, V, \theta)$ 
$\theta: \mathscr{A} \times \mathscr{A} \to V$, $\theta: (P, Q) \mapsto \overrightarrow{PQ}$
(i) For any point $P \in \mathscr{A}$, $\theta_P = \theta(P, \cdot): \mathscr{A} \to V$ is a bijection.
(ii) $\forall P, Q, R \in \mathscr{A}, \overrightarrow{PR} = \overrightarrow{PQ} + \overrightarrow{QR}$

**Def**:
(i) $V$ is the direction of the affine space.
(ii) elements of $\mathscr{A}$ are called _points_ of $\mathscr{A}$.
(iii) $\dim(\mathscr{A}) = \dim(V)$

**Examples:**
(2) Any vector space has the natural structure of an affine space: the mapping $\Theta: E \times E \to E$ is simply the mapping that associates with the ordered pair $(u, v)$ the vector $v - u$.
(3) If $\mathcal{E}_1$ and $\mathcal{E}_2$ are two affine spaces directed respectively by $E_1$ and $E_2$, the Cartesian product $\mathcal{E}_1 \times \mathcal{E}_2$ is an affine space directed by $E_1 \times E_2$: the mapping
$$ \Theta: (\mathcal{E}_1 \times \mathcal{E}_2) \times (\mathcal{E}_1 \times \mathcal{E}_2) \to E_1 \times E_2 $$
is the one that associates, with the ordered pair $((A_1, A_2), (B_1, B_2))$, the ordered pair of vectors $(\overrightarrow{A_1 B_1}, \overrightarrow{A_2 B_2})$.



**Properties:** Chasles' relation gives directly $\overrightarrow{AA} = 0$ and $\overrightarrow{AB} = -\overrightarrow{BA}$.

**The parallelogram rule:** This says that the two equalities $\overrightarrow{AB} = \overrightarrow{A'B'}$ and $\overrightarrow{AA'} = \overrightarrow{BB'}$ are equivalent. It is proved using Chasles' relation:
$$ \overrightarrow{AB} = \overrightarrow{AA'} + \overrightarrow{A'B'} + \overrightarrow{B'B}, $$
which is also written
$$ \overrightarrow{AB} - \overrightarrow{A'B'} = \overrightarrow{AA'} - \overrightarrow{BB'}. $$

**Remark:** If $A$ is a point of the affine space $\mathcal{E}$ and if $u$ is a vector of the vector space $E$ underlying it, the unique point $B$ of $\mathcal{E}$ such that $\overrightarrow{AB} = u$ is sometimes denoted
$$ B = A + u. $$
## Vectorization of an affine space
Fix $A \in \mathcal{E}$. $\mathcal{E}$ becomes a vector space $\mathcal{E}_A$ via the bijection $M \mapsto \overrightarrow{AM}$.
$M+N=Q \iff \overrightarrow{AM} + \overrightarrow{AN} = \overrightarrow{AQ}$, and hence $\overrightarrow{AA}$ becomes $0$

**Affine subspace**: Let $(\mathscr{A}, V, \theta)$ be an Affine space. Let $\mathscr{F} \subseteq \mathscr{A}$. $\mathscr{F}$ is called an _affine subspace_ if either $\mathscr{F} = \emptyset$ or $\exists A \in \mathscr{F}$ s.t $\theta_A(\mathscr{F})$ is a vector subspace. Note: $\theta_A = \theta(A, \cdot)$

**Proposition**: Let $(\mathscr{A}, V, \theta)$ be an affine space structure. Let $W$ be a vector subspace of $V$. Fix $A \in \mathscr{A}$. $\exists !$ Affine subspace directed by $W$, $\mathscr{F} \subseteq \mathscr{A}$ passing through $A$.
**Proof**: Let  $\mathscr{F} := \{ M \in \mathscr{A} : \overrightarrow{AM} \in W \}$
Clearly $\mathscr{F}$ is an affine space with $W$ as the vector space and passing through $A$.

**Ex**: An affine space of dimension 0 contains a unique point.

**Theorem**: Any intersection of affine subspaces is an affine subspace.
**Proof**: Let $(\mathscr{A}, V, \theta)$ be an affine space. $\{A_i\}_{i \in I}$ be affine.  $\mathscr{F} = \bigcap A_i$, If $\mathscr{F}= \varnothing$,then we are done, Otherwise if $\mathscr{F} \neq \emptyset$, fix $A \in \mathscr{F}$. $\theta_A(A_i)$ is a vector subspace of $V$. Then $\theta_A(\mathscr{F})$ is also a vector subspace.

**Definition 1.11.** The $k+1$ points $A_0, \dots, A_k$ are *affinely independent* if the dimension of the space $\langle A_0, \dots, A_k \rangle$ they span is $k$. If $k = \dim \mathcal{E}$, it is said that $(A_0, \dots, A_k)$ is an *affine frame* of $\mathcal{E}$.

## Affine Mappings
**Definition 2.1.** Let $\mathcal{E}$ and $\mathcal{F}$ be two affine spaces directed respectively by $E$ and $F$. A mapping $\varphi: \mathcal{E} \to \mathcal{F}$ is said to be *affine* if there exists a point $O$ in $\mathcal{E}$ and a linear mapping $f: E \to F$ such that
$$ \forall M \in \mathcal{E}, \quad f(\overrightarrow{OM}) = \overrightarrow{\varphi(O)\varphi(M)}. $$

(4) Assume that $\mathcal{E} = \mathcal{F}$. The affine mappings whose associated linear mapping is $\operatorname{Id}_E$ are the mappings
$$ \varphi: \mathcal{E} \to \mathcal{E} $$
such that $\overrightarrow{\varphi(A)\varphi(B)} = \overrightarrow{AB}$ for all $A$ and $B$ in $\mathcal{E}$. The parallelogram rule then gives $\overrightarrow{A\varphi(A)} = \overrightarrow{B\varphi(B)}$ for all $A$ and $B$. In other words, the vector $\overrightarrow{M\varphi(M)}$ is a constant vector $u$. It is said that $\varphi$ is the *translation* of vector $u$. It is denoted by $t_u$.

```tikz
\begin{document}
\begin{tikzpicture}[>=stealth, scale=1]
    % Translation
    \coordinate (A) at (0,0);
    \coordinate (B) at (1.5,1);
    \coordinate (u) at (3,1); % Vector u = (3,1)

    \coordinate (Ap) at ($(A)+(u)$);
    \coordinate (Bp) at ($(B)+(u)$);

    \draw (A) -- (B);
    \draw (Ap) -- (Bp);
    \draw[->] (A) -- (Ap) node[midway, below] {$u$};
    \draw[->] (B) -- (Bp);

    \filldraw (A) circle (1pt) node[below left] {$A$};
    \filldraw (B) circle (1pt) node[above left] {$B$};
    \filldraw (Ap) circle (1pt) node[right] {$\varphi(A)$};
    \filldraw (Bp) circle (1pt) node[right] {$\varphi(B)$};
\end{tikzpicture}
\end{document}
```

(5) Let $O$ be a point, $\lambda$ be a scalar and $\varphi$ be the mapping defined by $\overrightarrow{O\varphi(M)} = \lambda \overrightarrow{OM}$. This is an affine mapping. The associated linear mapping is the (linear) dilatation of ratio $\lambda$. The point $O$ is fixed, $\varphi$ is called the (central) *dilatation* of center $O$ and ratio $\lambda$ and it is denoted by $h(O, \lambda)$.

```tikz
\begin{document}
\begin{tikzpicture}[>=stealth, scale=1]
    % Dilatation
    \coordinate (O) at (0,0);
    \filldraw (O) circle (1pt) node[below] {$O$};

    \coordinate (A) at (2,0.5);
    \coordinate (B) at (1.5,2);

    \coordinate (Ap) at (4,1); % lambda = 2
    \coordinate (Bp) at (3,4);

    \draw (O) -- (Ap);
    \draw (O) -- (Bp);
    
    \draw[dashed] (A) -- (B);
    \draw (Ap) -- (Bp);

    \filldraw (A) circle (1pt) node[below right] {$A$};
    \filldraw (B) circle (1pt) node[left] {$B$};
    \filldraw (Ap) circle (1pt) node[below right] {$\varphi(A)$};
    \filldraw (Bp) circle (1pt) node[left] {$\varphi(B)$};
\end{tikzpicture}
\end{document}
```


**Proposition**: The image of an affine subspace by an affine mapping is an affine subspace.
**Proof**: $T(\theta_A(\mathscr{F})) \leftarrow$ vector subspace of $V' \implies \theta'_{\varphi(A)}(\varphi(\mathscr{F}))$ is also vector subspace $\implies \varphi(\mathscr{F})$ is an affine subspace.

**Corollary:** Affine mappings sends straight line to straight line.
**Proof:**

**Prop**: The only affine mapping of $n$ dim aff. space that fixes $n+1$ points is the Id map.
**pf**: Let $A_1, M_1, \dots, M_n \in \mathscr{A}$ be independent. Let $\varphi: \mathscr{A} \to \mathscr{A}$ be an affine map. $\varphi(A_1) = A_1, \varphi(M_1) = M_1, \dots$ but $T: V \to V$ be the ALM. $\overrightarrow{A_1 M_1}, \overrightarrow{A_2 M_2}, \dots, \overrightarrow{A_1 M_n} \in V$.

$T(\overrightarrow{A_1 M_i}) = \overrightarrow{A_1 M_i} \quad \forall i \implies T = Id \implies \varphi$ is translation. $\overrightarrow{M_i \varphi(M_i)} = const.$ but $\overrightarrow{M_i \varphi(M_i)} = \vec{0} \implies \varphi = Id$.

**Prop**: Composition of 2 aff maps is affine.
**Prop**: $\varphi$ is bijective iff the ALM, $T$ is bijective.
**Corr**: Affine transformations makes a group under composition. (denoted as $GL(\mathscr{A})$)
**Prop**: $GL(\mathscr{A}) \xrightarrow{\mathcal{L}} GL(V)$, $\varphi \mapsto T$ is surj. $\operatorname{Ker}(\mathcal{L}) =$ set of all translation.

$$ \overrightarrow{\phi(M)} = \vec{M} + u \quad \forall M \in \mathscr{A} \implies \overrightarrow{\phi(M)} - \vec{M} = u \implies \overrightarrow{M \phi(M)} = u \quad (\text{constant}) \quad \text{--- (2)} $$

**Translation**: $\phi: \mathscr{A} \to \mathscr{A}$ is called translation if the associated linear mapping (ALM), $T: V \to V$ is $Id_V$. Also, it is $\overrightarrow{M \phi(M)}$ is constant vector in $V, \forall M \in \mathscr{A}$.

**Scaling**: $\phi: \mathscr{A} \to \mathscr{A}$ is called a scaling if the ALM, $T$ is $\lambda Id_V$.

**Prop**: Fix $O \in \mathscr{A}$. Any affine mapping $\varphi: \mathscr{A} \to \mathscr{A}$ can be written in a unique way in the form $\varphi = \tau_v \circ \psi$, where $v \in V$ and $\psi(O) = O$.

**Theorem:** Affine transformations maps straight lines to straight lines

**Proof:** We prove for $n=2$, Let $T$ be an affine transformation,

$$
T(x) = Ax + b, A \in GL_{2\times 2}(\mathbb{R}),\quad b \in \mathbb{R}^{2}
$$

$L:= \{ p + \lambda v \mid \lambda \in \mathbb{R} \}$,

$$
\begin{align}

T(p+\lambda v ) = A(p + \lambda v) =  & A(p + \lambda v) + b \\
 =& A(p) + \lambda Av + b \\
=  & A(p) + v + \lambda A v \\
=  & T(p) + \lambda A v
\end{align}
$$

So we have $T(L) = \{  T(p) + \lambda A v \mid \lambda \in \mathbb{R} \}$ $\quad \blacksquare$

**Theorem:** Affine transformation sends $\parallel$ lines to $\parallel$ lines.

**Proof:** $l_{1},l_{2} , l_{1} \parallel l_{2} \implies l_1 = p_1 + \mathbb{R}v, l_2 = p_2 + \mathbb{R}v$.
From the previous theorem, $T(l_1) = T(p_1) + \mathbb{R}Av$ and $T(l_2) = T(p_2) + \mathbb{R}Av$.
Since both lines have the direction vector $Av$, $T(l_1) \parallel T(l_2)$. $\blacksquare$

**Theorem:** Affine transformation preserves ratios of lengths along a straight line

**Proof:**
Let $A, B$ be distinct points on a line, and let $C$ be a point on the segment $AB$.
Since $C$ is on the line determined by $A$ and $B$, we can write $C = (1-t)A + tB$ for some $t \in \mathbb{R}$.
The ratio of signed lengths (or vectors) is $\frac{C-A}{B-A} = t$.
Let $\varphi(x) = Tx + b$ be an affine transformation.
$$ \varphi(C) = T(C) + b = T((1-t)A + tB) + b = (1-t)T(A) + tT(B) + ((1-t)+t)b $$
$$ \varphi(C) = (1-t)(T(A)+b) + t(T(B)+b) = (1-t)\varphi(A) + t\varphi(B) $$
Thus, $\varphi(C)$ divides the segment $\varphi(A)\varphi(B)$ in the same ratio $t$.

```tikz
\begin{document}
\begin{tikzpicture}[>=stealth, scale=0.85]
    % Original Line
    \coordinate (A) at (0,0);
    \coordinate (B) at (3,0);
    \coordinate (C) at (2.25,0); % t = 0.75

    \draw[thick] (A) -- (B);
    \filldraw (A) circle (2pt) node[below] {$A$};
    \filldraw (B) circle (2pt) node[below] {$B$};
    \filldraw (C) circle (2pt) node[below] {$C$};
    \node at (1.5, -0.6) {$AC/AB = t$};

    % Transformation Arrow
    \draw[->, thick, bend left] (3.5, 0.5) to node[above] {$\varphi$} (5, 0.5);

    % Transformed Line
    \coordinate (Ap) at (5.5, 1);
    \coordinate (Bp) at (8.5, 2.5);
    \coordinate (Cp) at (7.75, 2.125); % (1-0.75)Ap + 0.75Bp

    \draw[thick] (Ap) -- (Bp);
    \filldraw (Ap) circle (2pt) node[above left] {$\varphi(A)$};
    \filldraw (Bp) circle (2pt) node[above right] {$\varphi(B)$};
    \filldraw (Cp) circle (2pt) node[above left] {$\varphi(C)$};
    \node[right, align=left] at (6.5, 3.2) {$\frac{\varphi(C)-\varphi(A)}{\varphi(B)-\varphi(A)}$ \\ $= t$};
\end{tikzpicture}
\end{document}
```

$\quad \blacksquare$

## Fundamental theorem of Affine geometry

**Theorem:** Any triangle can be mapped onto any other triangle by a unique affine transformation.

```tikz
\begin{document}
\begin{tikzpicture}[scale=0.8, >=stealth]
    % Triangle 1
    \coordinate (A) at (0,0);
    \coordinate (B) at (2,0.5);
    \coordinate (C) at (0.5,2);
    \draw[thick, fill=blue!10] (A) -- (B) -- (C) -- cycle;
    \filldraw (A) circle (2pt) node[below left] {$A$};
    \filldraw (B) circle (2pt) node[below right] {$B$};
    \filldraw (C) circle (2pt) node[above] {$C$};

    % Mapping
    \draw[->, thick, bend left] (2.5, 1) to node[above] {$\varphi$} (4.5, 1);

    % Triangle 2
    \coordinate (Ap) at (5,0);
    \coordinate (Bp) at (7,0);
    \coordinate (Cp) at (6,2);
    \draw[thick, fill=red!10] (Ap) -- (Bp) -- (Cp) -- cycle;
    \filldraw (Ap) circle (2pt) node[below left] {$A'$};
    \filldraw (Bp) circle (2pt) node[below right] {$B'$};
    \filldraw (Cp) circle (2pt) node[above] {$C'$};
\end{tikzpicture}
\end{document}
```

**Proof:**

**Theorem(Thales):** Let $L_1, L_2, L_3$ be three parallel lines in an affine plane. Let $D_1, D_2$ be two transversals intersecting these lines at $A_1, A_2, A_3$ and $A_1', A_2', A_3'$ respectively. Then:
$$ \frac{\overrightarrow{A_1 A_2}}{\overrightarrow{A_1 A_3}} = \frac{\overrightarrow{A_1' A_2'}}{\overrightarrow{A_1' A_3'}} $$

```tikz
\begin{document}
\begin{tikzpicture}[>=stealth, scale=1.2]
    % Horizontal Parallel Lines
    \draw[blue, thick] (-0.5, 3) -- (6, 3) node[right] {$L_1$};
    \draw[blue, thick] (-0.5, 1.5) -- (6, 1.5) node[right] {$L_2$};
    \draw[blue, thick] (-0.5, 0) -- (6, 0) node[right] {$L_3$};

    % Transversal 1 (Slope -3)
    \draw[thick] (0.83, 3.5) -- (2.17, -0.5) node[below] {$D_1$};
    \filldraw (1, 3) circle (2pt) node[above left] {$A_1$};
    \filldraw (1.5, 1.5) circle (2pt) node[above left] {$A_2$};
    \filldraw (2, 0) circle (2pt) node[below left] {$A_3$};

    % Transversal 2 (Slope -1.5, slightly non-parallel)
    \draw[thick] (2.67, 3.5) -- (5.33, -0.5) node[below] {$D_2$};
    \filldraw (3, 3) circle (2pt) node[above right] {$A_1'$};
    \filldraw (4, 1.5) circle (2pt) node[above right] {$A_2'$};
    \filldraw (5, 0) circle (2pt) node[below right] {$A_3'$};
\end{tikzpicture}
\end{document}
```

**Converse of Thales Theorem:**
Let $L_1, L_2, L_3$ be three distinct lines intersecting two transversals $D_1, D_2$ at $A_1, A_2, A_3$ and $A_1', A_2', A_3'$ respectively.
If $L_1 \parallel L_3$ and the ratios of the intercepts are equal, i.e.,
$$ \frac{\overrightarrow{A*1 A_2}}{\overrightarrow{A_1 A_3}} = \frac{\overrightarrow{A_1' A_2'}}{\overrightarrow{A_1' A_3'}} $$
then the line $L_2$ is parallel to $L_1$ and $L_3$.
**Proof:**
Let $\pi$ be the affine projection of $D*{1}$ onto $D_2$ parallel to $L_i$ , and let $P$ be the associated linear map.
The vectors $\overrightarrow{A_1 A_3}$ and $\overrightarrow{A_1 A_2}$ are projected as:
$$ P(\overrightarrow{A*1 A_3}) = \overrightarrow{\pi(A_3) \pi(A_1)} = \overrightarrow{A_1' A_3'} $$
$$ P(\overrightarrow{A_1 A_2}) = \overrightarrow{\pi(A_2)\pi(A_1)} = \overrightarrow{A_1' A_2'} $$
Since $\overrightarrow{A_1 A_3} = \lambda \overrightarrow{A_1 A_2}$, linearity implies $P(\overrightarrow{A_1 A_3}) = \lambda P(\overrightarrow{A_1 A_2})$, hence $\overrightarrow{A_1' A_3'} = \lambda \overrightarrow{A_1' A_2'}$.
Conversely, we can construct parallel lines to $L*{1}$ and see that they have the same ratio, and hence must coincide.

```tikz
\begin{document}
\begin{tikzpicture}[>=stealth, scale=1.0]
    % Lines L1 and L3 (Parallel)
    \draw[blue, thick] (-0.5, 3) -- (6, 3) node[right] {$L_1$};
    \draw[blue, thick] (-0.5, 0) -- (6, 0) node[right] {$L_3$};

    % Transversals
    \draw[thick] (0.83, 3.5) -- (2.17, -0.5) node[below] {$D_1$};
    \draw[thick] (2.67, 3.5) -- (5.33, -0.5) node[below] {$D_2$};

    % Points A_i on D1
    \filldraw (1, 3) circle (2pt) node[above left] {$A_1$};
    \filldraw (1.5, 1.5) circle (2pt) node[above left] {$A_2$};
    \filldraw (2, 0) circle (2pt) node[below left] {$A_3$};

    % Points A_i' on D2
    \filldraw (3, 3) circle (2pt) node[above right] {$A_1'$};
    \filldraw (5, 0) circle (2pt) node[below right] {$A_3'$};

    % A2' placed off-parallel to show L2 isn't necessarily parallel
    \coordinate (A2p) at (4.0, 1.25);
    \filldraw (A2p) circle (2pt) node[right] {$A_2'$};

    % Line L2 (connecting A2 and A2')
    \draw[thick] (-0.5, 1.45) -- (5.5, 1.2) node[right] {$L_2$};
    \draw[dotted] (1.5, 1.5) -- (A2p);

    % Construction Lines L4, L5 parallel to L1
    % L4 through A2
    \draw[red, dashed, thick] (-0.5, 1.5) -- (6, 1.5) node[right] {$L_4$};
    \coordinate (B2) at (4.0, 1.5); % Intersection with D2
    \filldraw[red] (B2) circle (2pt) node[above right] {$B_2$};

    % L5 through A3 (coincides with L3 since L1 || L3)
    % We draw it slightly offset or just label it to indicate the construction logic
    \node[red, below] at (6, 0) {$L_5$};
    \coordinate (B3) at (5, 0); % Intersection with D2
    % B3 is same as A3'
    \node[red, below right] at (5.1, -0.2) {$B_3$};

\end{tikzpicture}
\end{document}
```

**Theorem (Pappus):** Given $AB' \parallel BA'$, $BC' \parallel CB'$, then $AC'\parallel CA'$

```tikz
\begin{document}
\begin{tikzpicture}[scale=1.0]
    % Line 1
    \draw (-0.5, 3) -- (5.5, 3);
    \node at (5.7, 3) {$D$};

    % Line 2
    \draw (-0.5, 0) -- (5.5, 0);
    \node at (5.7, 0) {$D'$};

    % Points
    \filldraw (0.5, 3) circle (2pt) node[above] {$A$};
    \filldraw (2.5, 3) circle (2pt) node[above] {$B$};
    \filldraw (4.5, 3) circle (2pt) node[above] {$C$};

    % Flipped order: C', B', A'
    \filldraw (1, 0) circle (2pt) node[below] {$C'$};
    \filldraw (3, 0) circle (2pt) node[below] {$B'$};
    \filldraw (5, 0) circle (2pt) node[below] {$A'$};

    % Connections
    % Pair 1: AB' || BA'
    \draw (0.5, 3) -- (3, 0); % A-B'
    \draw (2.5, 3) -- (5, 0); % B-A'

    % Pair 2: BC' || CB'
    \draw (2.5, 3) -- (1, 0); % B-C'
    \draw (4.5, 3) -- (3, 0); % C-B'

    % Pair 3: AC' || CA' (Result)
    \draw[dashed] (0.5, 3) -- (1, 0); % A-C'
    \draw[dashed] (4.5, 3) -- (5, 0); % C-A'
\end{tikzpicture}
\end{document}
```

**Proof:** Let $O \in D \cap D'$ Let $\varphi, \psi$ be the scaling of center $O$ such that $\varphi(A) = B, \psi(B) = C$

$$
\frac{\overrightarrow{OA}}{\overrightarrow{OB}} = \frac{\overrightarrow{OB'}}{\overrightarrow{OA'}} \implies \overrightarrow{OA'} = \frac{\overrightarrow{OB}}{\overrightarrow{OA}} \overrightarrow{OB'}
$$

**Claim:** $\varphi(B') = A'$
Since $\varphi$ is a centered scaling at $O$ with ratio $k_\varphi = \frac{\overrightarrow{OB}}{\overrightarrow{OA}}$, and the Thales condition gives $\overrightarrow{OA'} = k_\varphi \overrightarrow{OB'}$, we have $\varphi(B') = A'$.
Similarly, for the pair $BC' \parallel CB'$, the scaling $\psi$ (mapping $B \to C$) satisfies $\psi(C') = B'$.
Now consider the composition $\psi \circ \varphi$. Since scalings with the same center commute:
$$ (\psi \circ \varphi)(B') = \psi(\varphi(B')) = \psi(A') $$
$$ (\varphi \circ \psi)(B') = \varphi(\psi(B')) = \varphi(C') $$
Thus $\psi(A') = \varphi(C')$.
Also $(\psi \circ \varphi)(A) = \psi(B) = C$. and $\varphi \circ \psi(C') = A'$, the result then follows from converse of Thales.

**Theorem(Desargues):** If two triangles $ABC$ and $A'B'C'$ correspond such that their sides are parallel ($AB \parallel A'B'$, $BC \parallel B'C'$, $AC \parallel A'C'$), then the lines joining corresponding vertices ($AA', BB', CC'$) intersect at a common point (or are parallel).

```tikz
\begin{document}
\begin{tikzpicture}[scale=0.8]
    % Center O
    \coordinate (O) at (0, 0);
    \filldraw (O) circle (2pt) node[below left] {$O$};

    % Triangle 1 (Small)
    \coordinate (A) at (2, 1);
    \coordinate (B) at (3, 3);
    \coordinate (C) at (4, 1.5);

    \draw (A) -- (B) -- (C) -- cycle;
    \filldraw (A) circle (2pt) node[left] {$A$};
    \filldraw (B) circle (2pt) node[left] {$B$};
    \filldraw (C) circle (2pt) node[below] {$C$};

    % Triangle 2 (Large)
    \coordinate (Ap) at (4, 2);   % 2*A
    \coordinate (Bp) at (6, 6);   % 2*B
    \coordinate (Cp) at (8, 3);   % 2*C

    \draw (Ap) -- (Bp) -- (Cp) -- cycle;
    \filldraw (Ap) circle (2pt) node[left] {$A'$};
    \filldraw (Bp) circle (2pt) node[right] {$B'$};
    \filldraw (Cp) circle (2pt) node[right] {$C'$};

    % C'' shifted slightly for visual distinction
    \coordinate (Cpp) at (8.15, 2.85);
    \filldraw[red] (Cpp) circle (2pt) node[below right] {$C''$};
    %% \draw[->, red, thin] (Cpp) -- (Cp); %%
    \draw[red, thin] (Cpp) -- (Ap);
    \draw[red, thin] (Cpp) -- (Bp);

    % Connecting lines
    \draw[dashed] (O) -- (Bp);
    \draw[dashed] (O) -- (Cp);
    \draw[dashed] (O) -- (Ap);

\end{tikzpicture}
\end{document}
```

**Proof:**
Let $AA'$ and $BB'$ intersect at $O$, let $\varphi$ be the dilation that maps $A \mapsto A', B \mapsto B'$, Let $\lambda$ be the corresponding scaling. Let $\varphi(C) = C''$

From Thales,

$$
\frac{\overrightarrow{OA'}}{\overrightarrow{OA}} = \frac{\overrightarrow{OB'}}{\overrightarrow{OB}} = \frac{\overrightarrow{A'B'}}{\overrightarrow{AB}}  = \lambda
$$

$$
\frac{\overrightarrow{OC''}}{\overrightarrow{OC}  } = \frac{\overrightarrow{OA'}}{\overrightarrow{OA}} =  \frac{\overrightarrow{AC''}}{\overrightarrow{AC}} = \lambda
$$

$$
\frac{\overrightarrow{OC''}}{\overrightarrow{OC}} = \frac{\overrightarrow{OB'}}{\overrightarrow{OB}} = \frac{\overrightarrow{B'C''}}{\overrightarrow{BC}} = \lambda
$$

## Convex set

**Def:** $A \subseteq \mathscr{E}$, affine space, is a convex set if the segment $AB \subseteq  \mathscr{A}$, $\forall AB \in \mathscr{A}$.

**Proposition:** Any intersection of convex sets in convex.
**Note:** It is not true for union
**Proposition:** Image of a convex set under an affine mapping is convex.
**Proof:** seen before

**Proposition:** Inverse image of an convex set under an affine mapping is convex
**Proof:** $\phi:\mathscr{E}\to \mathscr{F}$, Let $C \subseteq \mathscr{F}$ is a convex set, $A,B \in \phi ^{-1}(C)$ we have to show $AB \subseteq \phi ^{-1}(C)$.

$$
\begin{align}
A' = \phi(A)  \\
B' = \phi(B) \\
A',B' \in C \implies A'B' \in C \\
A,B \in \phi ^{-1}(A'B') \implies AB \subseteq \phi ^{-1}(A'B') \implies AB \text{is convex}
\end{align}
$$

## Euclidean Vector space

**Def:** (Convex hull) Intersection of all the convex sets containing $S$ is the convex hull of $S$
**Def:** A vector space with an inner product $\langle\cdot ,\cdot \rangle$ is called a Euclidean vector space.

**Def:** (Euclidean Affine space) $\mathscr{E}$ is an Euclidean affine space if its associated v.s is an Euclidean v.s

$$
d(A,B) = \lvert \overrightarrow{AB} \rvert
$$

**Exercise:** Check $d$ is a metric.
**Def:** $T:V\to W$ a linear map is called a **linear isometry** if $\lvert T(u) \rvert = \lvert u \rvert, \forall u \in V$.
**Def:** $\phi:\mathscr{E}\to \mathscr{F}$ is an **affine isometry** if $d(\phi(A),\phi(B)) = d(A,B),\forall A,B \in \mathscr{E}$.

**Note:** An affine mapping $\phi: \mathscr{E}\to \mathscr{F}$ is an affine isometry iff the ALM is linear isometry.

**Theorem:** The set $\underbrace{ Isom }_{ \text{affine isom.} }$ forms a group under the compositions of mapping.
**Proof:** Let $\varphi \in Isom(\mathscr{E}) \implies$ the ALM $T$ is a linear isom. $T^{-1}$ is an linear isom. $\implies \varphi ^{-1}$ is an affine isom.

**Note:** Euclidean v.s are assumed finite dimensional unless mentioned.
**Reflections** It is orthogonal symmetries about hyperplanes, Let $H$ be a hyperplane in an Euclidean vector space $V$, Let $x_{0} \in H^{\perp}$. The reflection $S_{H}(x)= x - \frac{2\langle x,x_{0} \rangle}{\lVert x_{0} \rVert^{2}}x_{0}$

**Theorem:** Let V be a Euclidean v.s of dim n. Any affine linear isometry of V can be written as the composition of p reflections, where $p\leq n$.

**Proof:** #todo

**Theorem:** Let $\mathscr{E}$ be an affine space of dimension $n$, every affine isometry of $\mathscr{E}$ can be written as composition of $p$ reflections, where $p\leq n$
**Proof:**

**Def:** An affine isometry is called a rigid motion if the determinant of the ALM is +1. Class of rigid motion is denoted by $Isom^{+}(\mathscr{E})$,

$$
Isom(\mathscr{E})\xrightarrow{\det } \{ \pm 1 \} \quad \ker = Isom^{+}(\mathscr{E})
$$

$\implies Isom^{+}(\mathscr{E})$ is a normal subgroup.

**Proposition:** Let $\phi$ be an affine isometry of the affine Euclidean space $\mathscr{E}$, $\exists$ a isometry $\psi$ is a translation $t_{v}$ of $\mathscr{E}$ such that $\phi = t_{v} \circ \psi$ such that $\psi$ has fixed points.

**Proof:**

---

Let $\mathscr{A}$ be the Euclidean affine space of $\dim$ 3.

$$
S^{2}(a,r) := \{  x \in \mathscr{A} \mid d(x,a) =r \}
$$

**Def:(Great circle)** Intersection of the plane passing through the center of the sphere with the sphere.

```tikz
\begin{document}
\begin{tikzpicture}[scale=1.2]
    % Sphere radius
    \def\r{2}

    % Sphere ball shading
    \shade[ball color = gray!10, opacity = 0.3] (0,0) circle (\r);
    \draw (0,0) circle (\r);

    % Center
    \filldraw (0,0) circle (1.5pt) node[below] {$O$};

    % Plane (Visually a parallelogram) passing through center
    % We tilt the plane perspective slightly
    \filldraw[fill=blue!10, opacity=0.4, draw=blue!60]
        (-2.8, -0.5) -- (2.0, -1.5) -- (2.8, 0.5) -- (-2.0, 1.5) -- cycle;
    \node[blue!80] at (2.2, 1.2) {Plane $\Pi$};

    % Great Circle
    % The "front" part
    \draw[thick, red] (2, 0) arc (0:-180: 2cm and 0.6cm);
    % The "back" part (dashed)
    \draw[thick, red, dashed] (2, 0) arc (0:180: 2cm and 0.6cm);

    \node[red, below right] at (1.7, -0.2) {Great Circle};

    % Mark radius/intersection
    \draw[->] (0,0) -- (1.4, -0.42); % Radius vector to the circle
    \node[scale=0.8] at (0.8, -0.1) {$R$};

\end{tikzpicture}
\end{document}
```

**Def(Time Zone):** Part of the sphere limited by two great circles.

**Theorem:** Let $T$ be a spherical triangle of angle $\alpha,\beta$ and $\gamma$, then $area(T) = \alpha + \beta + \gamma - \pi \implies \alpha + \beta + \gamma = area(T) + \pi$

```tikz
\usepackage{tikz}
\usetikzlibrary{calc}
\begin{document}
\begin{tikzpicture}[scale=2]
    % Sphere outline
    \draw (0,0) circle (2cm);

    % Great Circles
    \draw[gray, thin] (0,0) ellipse (2cm and 0.6cm);
    \draw[gray, thin, rotate=60] (0,0) ellipse (2cm and 0.6cm);
    \draw[gray, thin, rotate=-60] (0,0) ellipse (2cm and 0.6cm);

    % Vertices (approximate based on intersections)
    \coordinate (A) at (0, 0.75);
    \coordinate (B) at (-0.95, -0.4);
    \coordinate (C) at (0.95, -0.4);

    % Triangle Edges
    \draw[blue, thick] (A) to[bend right=20] (B);
    \draw[blue, thick] (B) to[bend right=20] (C);
    \draw[blue, thick] (C) to[bend right=20] (A);

    % Labels
    \node[above] at (A) {$A$};
    \node[below left] at (B) {$B$};
    \node[below right] at (C) {$C$};

    % Angles
    \draw[red] ($(A)+(0,-0.2)$) arc (-110:-70:0.4);
    \node[red, below] at ($(A)+(0,-0.25)$) {$\alpha$};

    \draw[red] ($(B)+(0.2,0.1)$) arc (10:70:0.3);
    \node[red, right] at ($(B)+(0.1,0.25)$) {$\beta$};

    \draw[red] ($(C)+(-0.2,0.1)$) arc (170:110:0.3);
    \node[red, left] at ($(C)+(-0.1,0.25)$) {$\gamma$};

    \node[blue] at (0, 0) {$T$};
\end{tikzpicture}
\end{document}
```

**Proof:** Let $D$ be the half-sphere containing $T$ determined by the great circle opposite to the angle $\alpha$.
