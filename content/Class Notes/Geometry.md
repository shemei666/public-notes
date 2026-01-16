---
publish: true
---

**Def**: Affine Space $(\mathscr{A}, V, \theta)$
$\theta: \mathscr{A} \times \mathscr{A} \to V$, $\theta: (P, Q) \mapsto \overrightarrow{PQ}$
(i) For any point $P \in \mathscr{A}$, $\theta_P = \theta(P, \cdot): \mathscr{A} \to V$ is a bijection.
(ii) $\forall P, Q, R \in \mathscr{A}, \overrightarrow{PR} = \overrightarrow{PQ} + \overrightarrow{QR}$

**Def**:
(i) $V$ is the direction of the affine space.
(ii) elements of $\mathscr{A}$ are called *points* of $\mathscr{A}$.
(iii) $\dim(\mathscr{A}) = \dim(V)$

---

Let $V$ be a vector space. Take $\mathscr{A} := V$, $\theta: V \times V \to V$, $(v, w) \mapsto w - v$

**Vectorization of an affine space**
$B, C \in \mathscr{A}$, define $B+C=P$ if $\overrightarrow{AB} + \overrightarrow{AC} = \overrightarrow{AP}$



**Affine subspace**: Let $(\mathscr{A}, V, \theta)$ be an Affine space. Let $\mathscr{F} \subseteq \mathscr{A}$. $\mathscr{F}$ is called an *affine subspace* if either $\mathscr{F} = \emptyset$ or $\exists A \in \mathscr{F}$ s.t $\theta_A(\mathscr{F})$ is a vector subspace. Note: $\theta_A = \theta(A, \cdot)$

**Prop**: Let $(\mathscr{A}, V, \theta)$ be an affine space structure. Let $W$ be a vector subspace of $V$. Fix $A \in \mathscr{A}$. $\exists !$ Affine subspace $\mathscr{F} \subseteq \mathscr{A}$ passing through $A$.
**Proof**: $\mathscr{F} := \{ M \in \mathscr{A} : \overrightarrow{AM} \in W \}$

**Ex**: An affine space of dimension 0 contains a unique point.



**Thm**: Any intersection of affine subspaces is an affine subspace.
**Proof**: Let $(\mathscr{A}, V, \theta)$ be an affine space. $\{A_i\}_{i \in I}$ be affine. $\mathscr{F} = \bigcap A_i$, $\mathscr{F} \neq \emptyset$. Fix $A \in \mathscr{F}$. $\theta_A(A_i)$ is a vector subspace of $V$. Then $\theta_A(\mathscr{F})$ is also a vector subspace.



**Prop**: The image of an affine subspace by an affine mapping is an affine subspace.
**Proof**: $T(\theta_A(\mathscr{F})) \leftarrow$ vector subspace of $V' \implies \theta'_{\varphi(A)}(\varphi(\mathscr{F}))$ is also vector subspace $\implies \varphi(\mathscr{F})$ is an affine subspace.

**Corr**: Affine mappings sends straight line to straight line.

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

**Theorem:**  Affine transformation sends $\parallel$ lines to $\parallel$ lines.

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
$$ \frac{\overrightarrow{A_1 A_2}}{\overrightarrow{A_1 A_3}} = \frac{\overrightarrow{A_1' A_2'}}{\overrightarrow{A_1' A_3'}} $$
then the line $L_2$ is parallel to $L_1$ and $L_3$.
**Proof:** 
Let $\pi$ be the affine projection of $D_{1}$ onto $D_2$ parallel to $L_i$ , and let $P$ be the associated linear map.
The vectors $\overrightarrow{A_1 A_3}$ and $\overrightarrow{A_1 A_2}$ are projected as:
$$ P(\overrightarrow{A_1 A_3}) = \overrightarrow{\pi(A_3)  \pi(A_1)} = \overrightarrow{A_1' A_3'} $$
$$ P(\overrightarrow{A_1 A_2}) = \overrightarrow{\pi(A_2)\pi(A_1)} = \overrightarrow{A_1' A_2'} $$
Since $\overrightarrow{A_1 A_3} = \lambda \overrightarrow{A_1 A_2}$, linearity implies $P(\overrightarrow{A_1 A_3}) = \lambda P(\overrightarrow{A_1 A_2})$, hence $\overrightarrow{A_1' A_3'} = \lambda \overrightarrow{A_1' A_2'}$. 
Conversely, we can construct parallel lines to $L_{1}$ and see that they have the same ratio, and hence must coincide.

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

    % Annotation
    \node[red, align=center] at (3.5, 0.5) {Construct $L_4, L_5 \parallel L_1$. \\ $B_2 \in D_2 \cap L_4$, $B_3 \in D_2 \cap L_5$.};

\end{tikzpicture}
\end{document}
```

**Theorem (Pappus):** 

**Proof:**