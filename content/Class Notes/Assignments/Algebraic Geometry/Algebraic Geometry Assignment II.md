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

To ensure the result holds for a general field $k$, we used the fact that if a polynomial vanishes for all $t \in k$, it must be the zero polynomial. This property holds if $k$ is an **infinite field**.

**Solution (Part 2):**
Considering $Y^2 - X^3 - X^2$ as a polynomial in $Y$, we can write
$$g(X,Y) = (Y^2 - X^3 - X^2)Q(X,Y) + YP(X) + T(X)$$
Now, substitute $X = t^2 - 1$ and $Y = t^3 - t$. Note that $Y^2 - X^3 - X^2 = (t^3-t)^2 - (t^2-1)^3 - (t^2-1)^2 = 0$.
$$0 = g(t^2-1, t^3-t) = (t^3-t) P(t^2-1) + T(t^2-1)$$
$$0 = t(t^2-1) P(t^2-1) + T(t^2-1)$$
The term $t(t^2-1) P(t^2-1)$ contains only odd powers of $t$ (since $P(t^2-1)$ is a polynomial in $t^2$).
The term $T(t^2-1)$ contains only even powers of $t$.
Comparing odd and even degrees, we get $P \equiv 0$, $T \equiv 0$.
$\implies Y^2 - X^3 - X^2 | g$.






**2.7)** Let $C : (y^2 = x^3 + ax + b) \subset k^2$; if $A = (x_1, y_1)$ and $B = (x_2, y_2)$, show how to give the coordinates of $A + B$ as rational functions of $x_1, y_1, x_2, y_2$.

**Solution:**
The line passing through $A$ and $B$ has equation $y = m(x-x_1) + y_1$, where $m = \frac{y_2-y_1}{x_2-x_1}$ (if $x_1 \neq x_2$).
Substituting into the curve equation $y^2 = x^3 + ax + b$:
$$(m(x-x_1) + y_1)^2 = x^3 + ax + b$$
$$m^2(x-x_1)^2 + y_1^2 + 2m(x-x_1)y_1 = x^3 + ax + b$$
This is a cubic equation in $x$. The sum of the roots is $x_1 + x_2 + x_3 = m^2$.
$$x_3 = m^2 - (x_1 + x_2)$$
To find the y-coordinate of the intersection point $(x_3, y_3)$:
$$y_3 = m(x_3 - x_1) + y_1$$
$$y_3 = m(m^2 - (x_1 + x_2) - x_1) + y_1$$
$$y_3 = m(m^2 - 2x_1 - x_2) + y_1$$
$$y_3 = m^3 - 2m x_1 - m x_2 + y_1$$
The sum $A+B$ is the point $(x_3, -y_3)$.
So, $A+B = (m^2 - x_1 - x_2, -(m^3 - 2m x_1 - m x_2 + y_1))$.


**2.10)** Let $C \subset \mathbb{P}^2_k$ be a plane cubic, and suppose that $P \in C$ is an inflexion point; prove that a change of coordinates in $\mathbb{P}^2_k$ can be used to bring $C$ into the normal form
$$Y^2Z = X^3 + aX^2Z + bXZ^2 + cZ^3.$$

**Solution:**
A general cubic form in $\mathbb{P}^2_k$ is given by a homogeneous polynomial of degree 3:
$$
\begin{aligned}
F(X, Y, Z) = \ &a_{1}X^3 + a_{2}X^2Y + a_{3}X^2Z + a_{4}XY^2 + a_{5}XYZ \\
&+ a_{6}XZ^2 + a_{7}Y^3 + a_{8}Y^2Z + a_{9}YZ^2 + a_{10}Z^3 = 0
\end{aligned}
$$
Since $Z=0$ is the tangent to the inflexion point, we see that $a_{1}X^3 + a_{2}X^2Y +  a_{4}XY^2 +   a_{7}Y^3$ needs to have a triple root at $(0,1)$ hence we have $a_2 = a_4 = a_7 = 0$.
$$
F(X, Y, Z) = a_{1}X^3 + a_{3}X^2Z + a_{5}XYZ + a_{6}XZ^2 + a_{8}Y^2Z + a_{9}YZ^2 + a_{10}Z^3 = 0
$$
Grouping the terms involving $Y$:
$$ Z(a_8 Y^2 + Y(a_5 X + a_9 Z)) + a_1 X^3 + a_3 X^2 Z + a_6 X Z^2 + a_{10} Z^3 = 0 $$
Completing the square for $Y$ (assuming $a_8 \neq 0$):
$$ Z a_8 \left( Y + \frac{a_5 X + a_9 Z}{2a_8} \right)^2 - Z a_8 \left( \frac{a_5 X + a_9 Z}{2a_8} \right)^2 + a_1 X^3 + \dots + a_{10} Z^3 = 0 $$
Let $Y_1 = Y + \frac{a_5 X + a_9 Z}{2a_8}$. Then the equation becomes:
$$ a_8 Z Y_1^2 = \frac{Z(a_5 X + a_9 Z)^2}{4a_8} - (a_1 X^3 + a_3 X^2 Z + a_6 X Z^2 + a_{10} Z^3) $$
Multiplying by $4a_8$:
$$ 4a_8^2 Z Y_1^2 = Z(a_5 X + a_9 Z)^2 - 4a_8(a_1 X^3 + \dots) $$
This is of the form $Y_1^2 Z = \text{cubic in } X, Z$.
