
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