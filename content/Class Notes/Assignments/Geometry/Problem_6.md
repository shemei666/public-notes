# Problem 6

**Statement:** Let $\mathscr{A}$ be an affine space of dimension at least 2 and $\varphi: \mathscr{A} \to \mathscr{A}$ be an affine mapping such that the image of any line under $\varphi$ is a line that is parallel to it. Prove that $\varphi$ is a translation or a dilatation.

**Proof:**

Let $f: V \to V$ be the associated linear map of $\varphi$, where $V$ is the underlying vector space of $\mathscr{A}$.

1.  **Characterization of the linear map $f$:**
    Let $D$ be a line in $\mathscr{A}$ with direction spanned by a non-zero vector $v \in V$.
    The image $\varphi(D)$ is a line parallel to $D$.
    The direction of $\varphi(D)$ is the subspace spanned by $f(v)$.
    Since $\varphi(D) \parallel D$, their directions must be the same (or contained in one another, but here they are 1-dimensional).
    Thus, $f(v)$ must be a scalar multiple of $v$.
    So, for every $v \in V \setminus \{0\}$, there exists a scalar $\lambda_v \in \mathbb{K}$ such that $f(v) = \lambda_v v$.

    **Lemma:** If a linear map $f: V \to V$ has the property that every non-zero vector is an eigenvector, then $f$ is a scalar multiple of the identity, i.e., $f = \lambda \operatorname{Id}_V$ for some constant $\lambda$.
    
    *Proof of Lemma:*
    Let $v, w \in V$ be linearly independent vectors.
    We have $f(v) = \lambda_v v$ and $f(w) = \lambda_w w$.
    Consider $v+w$. We must have $f(v+w) = \lambda_{v+w}(v+w)$.
    By linearity, $f(v+w) = f(v) + f(w) = \lambda_v v + \lambda_w w$.
    Equating the two expressions:
    $$ \lambda_{v+w} v + \lambda_{v+w} w = \lambda_v v + \lambda_w w $$
    $$ (\lambda_{v+w} - \lambda_v) v + (\lambda_{v+w} - \lambda_w) w = 0 $$
    Since $v$ and $w$ are linearly independent, the coefficients must be zero.
    Thus, $\lambda_v = \lambda_{v+w} = \lambda_w$.
    So $\lambda_v$ is the same for all linearly independent vectors.
    If $\dim V \ge 2$, for any pair of dependent vectors, we can find a third vector independent of both to bridge the equality.
    Therefore, there exists a constant scalar $\lambda$ such that $f(v) = \lambda v$ for all $v \in V$.
    So $f = \lambda \operatorname{Id}_V$.

2.  **Case 1: $\lambda = 1$ (Translation)**
    If $\lambda = 1$, then $f = \operatorname{Id}_V$.
    By definition, an affine mapping whose associated linear map is the identity is a **translation**.
    For any $A, B \in \mathscr{A}$, $\overrightarrow{\varphi(A)\varphi(B)} = f(\overrightarrow{AB}) = \overrightarrow{AB}$.
    This implies $\overrightarrow{A\varphi(A)} = \overrightarrow{B\varphi(B)} = u$ (constant vector), so $\varphi = t_u$.

3.  **Case 2: $\lambda \neq 1$ (Dilatation/Homothety)**
    If $\lambda \neq 1$, the map $f - \operatorname{Id}_V = (\lambda - 1)\operatorname{Id}_V$ is invertible.
    Fix an origin $O \in \mathscr{A}$. Any affine map is determined by its action on a point and its linear part.
    We look for a fixed point $C \in \mathscr{A}$ (center of dilatation).
    $\varphi(C) = C \iff \overrightarrow{O\varphi(C)} = \overrightarrow{OC}$.
    We know $\overrightarrow{O\varphi(C)} = \overrightarrow{O\varphi(O)} + \overrightarrow{\varphi(O)\varphi(C)} = \overrightarrow{O\varphi(O)} + f(\overrightarrow{OC})$.
    So we want to solve for $C$:
    $$ \overrightarrow{OC} = \overrightarrow{O\varphi(O)} + \lambda \overrightarrow{OC} $$
    $$ (1 - \lambda)\overrightarrow{OC} = \overrightarrow{O\varphi(O)} $$
    $$ \overrightarrow{OC} = (1 - \lambda)^{-1} \overrightarrow{O\varphi(O)} $$
    Since $\lambda \neq 1$, such a point $C$ uniquely exists.
    With $C$ as the new origin, for any point $M$:
    $$ \overrightarrow{C\varphi(M)} = f(\overrightarrow{CM}) = \lambda \overrightarrow{CM} $$
    This is precisely the definition of a **dilatation** (or homothety) of center $C$ and ratio $\lambda$.

**Conclusion:**
In all cases, $\varphi$ is either a translation (if $\lambda=1$) or a dilatation (if $\lambda \neq 1$). $\blacksquare$
