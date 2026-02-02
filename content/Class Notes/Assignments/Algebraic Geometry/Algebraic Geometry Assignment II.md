**2.2)** Let $\varphi: \mathbb{R}^1 \to \mathbb{R}^2$ be the map given by $t \mapsto (t^2, t^3)$; prove directly that any polynomial $f \in \mathbb{R}[X,Y]$ vanishing on the image $C = \varphi(\mathbb{R}^1)$ is divisible by $Y^2 - X^3$. Determine what property of a field $k$ will ensure that the result holds for $\varphi: k \to k^2$ given by the same formula.

Do the same for $t \mapsto (t^2 - 1, t^3 - t)$.

**Solution:**
Considering $Y^2 - X^3$ as a polynomial in $Y$, we can write
$$f(X,Y) = (Y^2 - X^3)Q(X,Y) + YP(X) + T(X)$$
Now, $0 = f(t^2, t^3) = t^3 P(t^2) + T(t^2)$ for all $t \in \mathbb{R}$.
$$0 = t^3 P(t^2) + T(t^2)$$
RHS is a polynomial in $t \implies$ It can only have finitely many roots, but $\mathbb{R}$ is an infinite field and $t$ is a root for all $t \in \mathbb{R}$.
Hence $t^3 P(t^2) + T(t^2) \equiv 0$
Comparing odd and even degrees we get $P \equiv 0$, $T \equiv 0$.
$\implies Y^2 - X^3 | f$






**2.7)** Let $C : (y^2 = x^3 + ax + b) \subset k^2$; if $A = (x_1, y_1)$ and $B = (x_2, y_2)$, show how to give the coordinates of $A + B$ as rational functions of $x_1, y_1, x_2, y_2$.

**2.10)** Let $C \subset \mathbb{P}^2_k$ be a plane cubic, and suppose that $P \in C$ is an inflexion point; prove that a change of coordinates in $\mathbb{P}^2_k$ can be used to bring $C$ into the normal form
$$Y^2Z = X^3 + aX^2Z + bXZ^2 + cZ^3.$$