# Problem 2

**Statement:** Let $\mathscr{A}$ be an affine space. Let $A, B, C, D$ be four points on $\mathscr{A}$ such that for every affine transformation $T$ on $\mathscr{A}$, the images $T(A), T(B), T(C), T(D)$ are concyclic (i.e., they lie on a circle). Then, show that $A, B, C, D$ are affinely dependent.

**Proof:**

We proceed by contradiction.

1.  **Assumption:** Assume that $A, B, C, D$ are *affinely independent*.
    This means that the dimension of the affine subspace spanned by these four points is exactly 3. Let $\mathscr{S} = \langle A, B, C, D \rangle$ be this 3-dimensional subspace.

2.  **Affinely Independent Sets:**
    Since $A, B, C, D$ form an affine frame for $\mathscr{S}$, we can define an affine transformation within this subspace (or extend it to the whole space $\mathscr{A}$) that maps these points to any other set of 4 affinely independent points in a 3-dimensional Euclidean space.

3.  **Construction of a Counter-example:**
    Let us choose a coordinate system for $\mathscr{S}$ such that we identify $\mathscr{S} \cong \mathbb{R}^3$.
    Consider the canonical affine transformation $T$ (or simply the coordinate map) that maps $A, B, C, D$ to the vertices of the standard tetrahedron in $\mathbb{R}^3$:
    *   $A' = T(A) = (0, 0, 0)$
    *   $B' = T(B) = (1, 0, 0)$
    *   $C' = T(C) = (0, 1, 0)$
    *   $D' = T(D) = (0, 0, 1)$

4.  **Verification of Concyclicity:**
    By the hypothesis of the problem, the points $A', B', C', D'$ must be concyclic.
    By definition, a set of points is **concyclic** if they all lie on a single common circle.
    Any circle lies entirely within a single plane (a circle is a plane curve).
    Therefore, a necessary condition for points to be concyclic is that they must be **coplanar**.

5.  **Contradiction:**
    The points $(0, 0, 0)$, $(1, 0, 0)$, $(0, 1, 0)$, and $(0, 0, 1)$ are clearly **not coplanar**.
    (The equation of any plane passing through the first three is $z=0$, but the fourth point has $z=1 \neq 0$).
    Since $A', B', C', D'$ are not coplanar, they cannot lie on a circle.
    This contradicts the given condition that *for every* affine transformation $T$, the images are concyclic.

6.  **Conclusion:**
    The assumption that $A, B, C, D$ are affinely independent must be false.
    Therefore, $A, B, C, D$ are **affinely dependent**. $\blacksquare$
