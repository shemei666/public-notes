---
publish: true
---

# Complex Analysis

## Holomorphic Functions

**Definition**: A complex-valued function $f$ of a complex variable $z$ is said to be **holomorphic** at a point $z_0$ if it is differentiable in a neighborhood of $z_0$. 

That is, the limit
$$ f'(z_0) = \lim_{h \to 0} \frac{f(z_0 + h) - f(z_0)}{h} $$
exists. 

A function is **holomorphic on an open set $U$** if it is differentiable at every point in $U$. Functions that are holomorphic on the entire complex plane $\mathbb{C}$ are called **entire functions**.


> [!TIP] Proposition
> If $f$ and $g$ are holomorphic in $\Omega$, then:
> 1. $f + g$ is holomorphic in $\Omega$ and $(f + g)' = f' + g'$.
> 2. $fg$ is holomorphic in $\Omega$ and $(fg)' = f'g + fg'$.
> 3. If $g(z_0) \neq 0$, then $f/g$ is holomorphic at $z_0$ and
>    $$ (f/g)' = \frac{f'g - fg'}{g^2} $$
>
> Moreover, if $f : \Omega \to U$ and $g : U \to \mathbb{C}$ are holomorphic, the chain rule holds
> $$ (g \circ f)'(z) = g'(f(z))f'(z) \quad \text{for all } z \in \Omega. $$

### Examples of Holomorphic Functions

1.  **Polynomials**: 
    Any polynomial $P(z) = a_n z^n + a_{n-1} z^{n-1} + \dots + a_0$ is holomorphic on all of $\mathbb{C}$.
    *   Example: $f(z) = z^3 - 2z + 5$

2.  **Exponential Function**:
    The function $f(z) = e^z$ is holomorphic everywhere.
    *   Derivative: $\frac{d}{dz} e^z = e^z$

3.  **Trigonometric Functions**:
    Functions like $\sin z$ and $\cos z$ are entire.
    *   Example: $\sin z = \sum_{n=0}^{\infty} \frac{(-1)^n}{(2n+1)!} z^{2n+1}$

4.  **Rational Functions**:
    The quotient of two polynomials $P(z)/Q(z)$ is holomorphic wherever the denominator $Q(z) \neq 0$.
    *   Example: $f(z) = \frac{1}{1-z}$ is holomorphic on $\mathbb{C} \setminus \{1\}$.

### Non-Examples of Holomorphic Functions

1.  **Complex Conjugate**:
    The function $f(z) = \bar{z}$ is not holomorphic anywhere.
    *   Reason: The limit of the difference quotient depends on the direction of approach. It also fails the Cauchy-Riemann equations.

2.  **Modulus**:
    The function $f(z) = |z|^2 = z\bar{z}$ is complex differentiable *only* at $z=0$, and nowhere else. Therefore, it is not holomorphic on any open set.
    
3.  **Real/Imaginary Parts**:
    Functions like $f(z) = \text{Re}(z)$ or $f(z) = \text{Im}(z)$ are nowhere holomorphic.

## Analytic Functions

> [!INFO] Definition: 
> A function $f$ is said to be analytic at neighbourhood of $z_{0}$ if $f'$ exists and is continuous.


## Power series

A power series $P$ around a point $z_{0} \in \mathbb{C}$ is 
$$
\sum_{n=0}^{\infty} a_{n} (z-z_{0})^{n}
$$
### Radius of convergence of power series

$\infty \geq R \geq 0$ is said to be radius of convergence of $P$ if $\sum_{n\geq_{0}}^{} a_{n}(z-z_{0})^{n}$ converges in $D_{R} = \{ z \in \mathbb{C} \mid \lvert z-z_{0} \rvert < R \}$ 

```tikz
\begin{document}
\begin{tikzpicture}[>=stealth]
    % Axes
    \draw[->] (-1,0) -- (5,0) node[right] {Re};
    \draw[->] (0,-1) -- (0,5) node[above] {Im};
    
    % Define center and radius
    \coordinate (Z0) at (2,2);
    \def\R{1.5}
    
    % Draw the disk region (open disk, so dashed boundary)
    \draw[dashed, fill=blue!10] (Z0) circle (\R);
    
    % Draw center point
    \filldraw[blue] (Z0) circle (2pt) node[below left] {$z_0$};
    
    % Draw radius line
    \draw[->, blue] (Z0) -- ++(30:\R) node[midway, above] {$R$};
    
    % Label the region
    \node[blue] at (2, 1.2) {$D_R$};
    
    % Annotate the condition
    \node[right, align=left] at (4, 4) {$|z - z_0| < R$};

\end{tikzpicture}
\end{document}
```

## Some results from analysis

1. $\sum_{n\geq 0 }^{} a_{n}$ converges if $\sum_{n\geq}^{} \lvert a_{n} \rvert$ converges.
2. $f_{n}: \Omega \subseteq \mathbb{C} \to \mathbb{C}$ for $n\geq{1}$ then $S_{N}= \sum_{n=1}^{N} f_{n}$  Let $\lvert f_{n}(z) \rvert \leq M_{n} \forall z \in \Omega$ and $\sum_{n\geq}^{M_{n}}$ converges then $S_{N}$ converges absolutely and uniformly.
3. 
$$
\frac{1}{R} = \lim \sup \lvert a_{n} \rvert ^{1/n}
$$
where $R$ is the radius of convergence

> [!TIP] Theorem 2.5 (Cauchy-Hadamard)
> Given a power series $\sum_{n=0}^\infty a_n z^n$, there exists $0 \le R \le \infty$ such that:
> 1. If $|z| < R$, the series converges absolutely.
> 2. If $|z| > R$, the series diverges.
>
> Moreover, using the convention $1/0 = \infty$ and $1/\infty = 0$, $R$ is given by:
> $$ 1/R = \limsup_{n \to \infty} |a_n|^{1/n} $$

> [!NOTE]- Proof
> Let $L = 1/R$. Suppose $L \neq 0, \infty$.
> If $|z| < R$, choose $\epsilon > 0$ so small that $(L+\epsilon)|z| = r < 1$.
> By definition of $L$, $|a_n|^{1/n} \le L+\epsilon$ for all large $n$.
> Therefore $|a_n||z|^n \le \{(L+\epsilon)|z|\}^n = r^n$.
> Comparison with geometric series $\sum r^n$ shows $\sum a_n z^n$ converges absolutely.
>
> If $|z| > R$, then a similar argument proves that there exists a sequence of terms where absolute value goes to infinity, hence the series diverges.


**Exercise:**  $R  = \lim_{ n \to \infty } \left\lvert  \frac{a_{n}}{a_{n+1}}  \right\rvert$ whenever it exists
**Examples:**
$\sum_{n\geq 0}^{} z^{n} = \frac{1}{1-z}$ $R=1$
$\sum_{n\geq{1}}^{} \frac{z^{n}}{n}$  $R=1$ 
$\sum_{n\geq 1}^{} \frac{z^{n}}{n!}$ $R = \infty$
4. **Abel's Test**:
   If the series $\sum_{n=0}^\infty a_n$ converges and $\{b_n\}$ is a bounded, monotonic sequence of real numbers, then the series $\sum_{n=0}^\infty a_n b_n$ converges.

## Differentiation of Power Series


> [!TIP] Theorem 2.6
> The power series $f(z) = \sum_{n=0}^\infty a_n z^n$ defines a holomorphic function in its disc of convergence.
> The derivative of $f$ is also a power series obtained by differentiating term by term the series for $f$, that is,
> $$ f'(z) = \sum_{n=0}^\infty n a_n z^{n-1} $$
> Moreover, $f'$ has the same radius of convergence as $f$.

> [!NOTE]- Proof
> The assertion about the radius of convergence of $f'$ follows from Hadamard's formula. Indeed, $\lim_{n \to \infty} n^{1/n} = 1$, and therefore
> $$ \limsup |a_n|^{1/n} = \limsup |n a_n|^{1/n} $$
> so that $\sum a_n z^n$ and $\sum n a_n z^n$ have the same radius of convergence, and hence so do $\sum a_n z^n$ and $\sum n a_n z^{n-1}$.
>
> To prove the first assertion, we must show that the series $g(z) = \sum_{n=0}^\infty n a_n z^{n-1}$ gives the derivative of $f$.
> Let $R$ denote the radius of convergence of $f$, and suppose $|z_0| < r < R$. Write
> $$ f(z) = S_N(z) + E_N(z), \quad \text{where } S_N(z) = \sum_{n=0}^N a_n z^n \text{ and } E_N(z) = \sum_{n=N+1}^\infty a_n z^n $$
>
> Then, if $h$ is chosen so that $|z_0+h| < r$, we have
> $$ \frac{f(z_0+h)-f(z_0)}{h} - g(z_0) = \left( \frac{S_N(z_0+h)-S_N(z_0)}{h} - S_N'(z_0) \right) + (S_N'(z_0) - g(z_0)) + \left( \frac{E_N(z_0+h)-E_N(z_0)}{h} \right) $$
>
> Using $a^n - b^n = (a-b)(a^{n-1} + \dots + b^{n-1})$, we bound the error terms.
> $$ \left| \frac{E_N(z_0+h)-E_N(z_0)}{h} \right| \le \sum_{n=N+1}^\infty |a_n| n r^{n-1} $$
> This is the tail of a convergent series. Given $\epsilon > 0$, we can find $N_1$ such that this is $< \epsilon$.
> Also, since $S_N'(z_0) \to g(z_0)$, we can find $N_2$ such that $|S_N'(z_0) - g(z_0)| < \epsilon$.
> Fixing $N$, we can find $\delta$ such that for $|h| < \delta$, the first term is $< \epsilon$.
> Combining these gives the result.

> [!TIP] Corollary 2.7
> A power series is infinitely complex differentiable in its disc of convergence, and the higher derivatives are also power series obtained by termwise differentiation.



**Proposition:** Let $P(z)= \sum_{n\geq_{0}}^{} a_{n}(z-z_0)^{n}$ be a power series in $\mathbb{C}$ with radius of convergence  $R>0$. Let $w_{0} \in D(z_{0},R)$.

```tikz
\begin{document}
\begin{tikzpicture}[>=stealth]
    % Define points
    \coordinate (Z0) at (0,0);
    \coordinate (W0) at (1.5, 1);
    \def\R{3}
    
    % Draw Disk D(z0, R)
    \draw[dashed] (Z0) circle (\R);
    \node[blue] at (-2, 2) {$D(z_0, R)$};
    
    % Draw Center z0 (Blue)
    \filldraw[blue] (Z0) circle (2pt) node[below left] {$z_0$};
    \draw[->, blue] (Z0) -- (0:\R) node[midway, below] {$R$};
    
    % Calculate distance and R'
    \pgfmathsetmacro{\dist}{sqrt(1.5*1.5 + 1*1)}
    \pgfmathsetmacro{\Rprime}{\R - \dist}
    
    % Draw Disk D(w0, R')
    \draw[dashed, blue!80!black] (W0) circle (\Rprime);
    %\node[blue!80!black] at (2.2, 1.5) {$D_{w_0}(R')$};

    % Draw Point w0 (Blue)
    \filldraw[blue] (W0) circle (2pt) node[left] {$w_0$};
    \draw[->, blue] (W0) -- ++(-45:\Rprime) node[midway, below right] {$R'$};
    
    % Optional: Draw vector/distance
    \draw[dotted, blue] (Z0) -- (W0);
\end{tikzpicture}
\end{document}
```
Then $P$ has the power series expansion
$$
P(z) = \sum_{n\geq{1}}^{} \frac{P^{(n)}(w_{0})}{n!}(z-w_{0})^{n}
$$
where $z \in D_{w_{0}}(R')$, $R' = R - \lvert z_{0} - w_{0} \rvert$

> [!NOTE]- Proof
> We write $z - z_0 = (z - w_0) + (w_0 - z_0)$.
> Since $z \in D(w_0, R')$, we have $|z - w_0| < R - |w_0 - z_0|$, so $|z - w_0| + |w_0 - z_0| < R$.
> Thus, the series converges absolutely, and we can rearrange terms.
> $$
> \begin{align*}
> P(z) &= \sum_{n=0}^\infty a_n (z - z_0)^n \\
> &= \sum_{n=0}^\infty a_n ((z - w_0) + (w_0 - z_0))^n \\
> &= \sum_{n=0}^\infty a_n \sum_{k=0}^n \binom{n}{k} (z - w_0)^k (w_0 - z_0)^{n-k}
> \end{align*}
> $$
> By absolute convergence, we can swap the order of summation:
> $$
> \begin{align*}
> P(z) &= \sum_{k=0}^\infty (z - w_0)^k \sum_{n=k}^\infty a_n \binom{n}{k} (w_0 - z_0)^{n-k} \\
> &= \sum_{k=0}^\infty c_k (z - w_0)^k
> \end{align*}
> $$
> where $c_k = \sum_{n=k}^\infty a_n \binom{n}{k} (w_0 - z_0)^{n-k}$.
>
> Now consider the derivatives of $P(z) = \sum_{n=0}^\infty a_n (z-z_0)^n$.
> $$ P^{(k)}(z) = \sum_{n=k}^\infty a_n n(n-1)\dots(n-k+1) (z-z_0)^{n-k} $$
> At $z = w_0$:
> $$ P^{(k)}(w_0) = \sum_{n=k}^\infty a_n \frac{n!}{(n-k)!} (w_0 - z_0)^{n-k} $$
> Notice that $\binom{n}{k} = \frac{n!}{k!(n-k)!}$, so:
> $$ c_k = \frac{1}{k!} \sum_{n=k}^\infty a_n \frac{n!}{(n-k)!} (w_0 - z_0)^{n-k} = \frac{P^{(k)}(w_0)}{k!} $$
> Thus, $P(z) = \sum_{k=0}^\infty \frac{P^{(k)}(w_0)}{k!} (z - w_0)^k$.
> Since this rearrangement is valid for all $z \in D(w_0, R')$, the radius of convergence of the new series is at least $R'$.
> $\blacksquare$



## Cauchy-Riemann Equations

If $f(z) = u + iv$ is differentiable, then $u, v$ satisfy:
$$ u_x = v_y, \quad u_y = -v_x $$

**Derivation:**
To find these relations, consider the limit $f'(z_0)$ when $h$ is first real, say $h = h_1 + i0$. Then, if we write $z = x+iy$, $z_0 = x_0+iy_0$, and $f(z) = f(x,y)$, we find that
$$
\begin{align*}
f'(z_0) &= \lim_{h_1 \to 0} \frac{f(x_0+h_1, y_0) - f(x_0, y_0)}{h_1} \\
&= \frac{\partial f}{\partial x}(z_0)
\end{align*}
$$
where $\partial/\partial x$ denotes the usual partial derivative in the $x$ variable. Now taking $h$ purely imaginary, say $h = ih_2$, a similar argument yields
$$
\begin{align*}
f'(z_0) &= \lim_{h_2 \to 0} \frac{f(x_0, y_0+h_2) - f(x_0, y_0)}{ih_2} \\
&= \frac{1}{i} \frac{\partial f}{\partial y}(z_0)
\end{align*}
$$
where $\partial/\partial y$ is partial differentiation in the $y$ variable. Therefore, if $f$ is holomorphic we have shown that
$$ \frac{\partial f}{\partial x} = \frac{1}{i} \frac{\partial f}{\partial y} $$
Writing $f = u + iv$ and using $1/i = -i$, we find after separating real and imaginary parts that
$$ \frac{\partial u}{\partial x} = \frac{\partial v}{\partial y} \quad \text{and} \quad \frac{\partial u}{\partial y} = -\frac{\partial v}{\partial x} $$

### Complex Differential Operators

We define 2 differential operators
$$
\frac{\partial}{\partial z} = \frac{1}{2} \left( \frac{\partial}{\partial x} - i \frac{\partial}{\partial y} \right) \quad \text{and} \quad \frac{\partial}{\partial \bar{z}} = \frac{1}{2} \left( \frac{\partial}{\partial x} + i \frac{\partial}{\partial y} \right)
$$
If $f = u + iv$ is analytic, it satisfies the Cauchy-Riemann equations $u_x = v_y$ and $u_y = -v_x$. Hence we get,


$$
\begin{align*}
\frac{\partial f}{\partial \bar{z}} &= \frac{1}{2} \left( (u_x + i v_x) + i (u_y + i v_y) \right) \\
&= \frac{1}{2} \left( (u_x - v_y) + i (v_x + u_y) \right) \\
&= 0 \\
\frac{\partial f}{\partial z} &= \frac{1}{2} \left( (u_x + i v_x) - i (u_y + i v_y) \right) \\
&= \frac{1}{2} \left( (u_x + v_y) + i (v_x - u_y) \right) \\
&= u_x + i v_x \\
&= f'(z)
\end{align*}
$$

> [!TIP] Theorem 2.4 (Converse of Cauchy-Riemann)
> Suppose $f = u + iv$ is a complex-valued function defined on an open set $\Omega$. If $u$ and $v$ are continuously differentiable and satisfy the Cauchy-Riemann equations on $\Omega$, then $f$ is holomorphic on $\Omega$ and $f'(z) = \partial f / \partial z$.

> [!NOTE]- Proof
> Write
> $$ u(x+h_1, y+h_2) - u(x,y) = \frac{\partial u}{\partial x} h_1 + \frac{\partial u}{\partial y} h_2 + |h|\psi_1(h) $$
> and
> $$ v(x+h_1, y+h_2) - v(x,y) = \frac{\partial v}{\partial x} h_1 + \frac{\partial v}{\partial y} h_2 + |h|\psi_2(h) $$
> where $\psi_j(h) \to 0$ (for $j=1,2$) as $|h| \to 0$, and $h = h_1 + i h_2$. Using the Cauchy-Riemann equations we find that
> $$ f(z+h) - f(z) = \left( \frac{\partial u}{\partial x} - i \frac{\partial u}{\partial y} \right) (h_1 + i h_2) + |h|\psi(h) $$
> where $\psi(h) = \psi_1(h) + \psi_2(h) \to 0$, as $|h| \to 0$. Therefore $f$ is holomorphic and
> $$ f'(z) = 2 \frac{\partial u}{\partial z} = \frac{\partial f}{\partial z}. $$


## Branches of Logarithm

Let $\Omega \subseteq \mathbb{C}$ be a domain. Let $f: \Omega \to \mathbb{C}$ be continuous such that
$$ \exp(f(z)) = z \quad \forall z \in \Omega $$
Then $f$ is a **branch of logarithm**.
If $f$ and $g$ are 2 branches of logarithm, then $e^{f(z)} = e^{g(z)} = z$ for all $z \in \Omega$.
$$ \implies e^{f(z)-g(z)} = 1 \implies e^{i(\text{Im}(f) - \text{Im}(g))} = 1 $$
This implies $f(z) - g(z) = 2\pi i k$ for some $k \in \mathbb{Z}$.
By continuity of the functions, $k$ has to be independent of $z$ since $\Omega$ is connected.

Thus:
$$ \text{Re } f(z) = \text{Re } g(z) $$
$$ \text{Im } f(z) = \text{Im } g(z) + 2\pi k $$

> [!EXAMPLE] Principal Branch
> Let $\Omega = \mathbb{C} \setminus \{ z=x+iy \mid x \le 0, y=0 \}$.
> Define the principal branch:
> $$ f(z) = \log|z| + i \text{Arg } z, \quad -\pi < \text{Arg } z < \pi $$
>
> ```tikz
> \begin{document}
> \begin{tikzpicture}[>=stealth]
>     % Axes
>     \draw[->] (-3,0) -- (3,0) node[right] {Re};
>     \draw[->] (0,-3) -- (0,3) node[above] {Im};
>     
>     % Branch Cut
>     \draw[ultra thick, red] (0,0) -- (-3,0);
>     \node[red, above] at (-1.5, 0) {Cut};
>
>     % Domain Omega
>     \node at (2,2) {$\Omega$};
> \end{tikzpicture}
> \end{document}
> ```

> [!QUESTION] Question
> Is there a log branch with $\Omega = \mathbb{C} \setminus \{0\}$?

### Branch of Complex Differentiable Function

Let $\Omega \subseteq \mathbb{C}$ be a domain, and let $g: \Omega \to \mathbb{C}$ be complex differentiable.
Let $f: \Omega \to \mathbb{C}$ be a continuous function such that $e^{f(z)} = g(z)$ for all $z \in \Omega$.

> [!TIP] Theorem
> Let $\Omega \subseteq \mathbb{C}$ be simply connected and $g: \Omega \to \mathbb{C}$ be a non-vanishing complex differentiable function.
> Then there exists $f: \Omega \to \mathbb{C}$ such that $e^{f(z)} = g(z)$ for all $z \in \Omega$.


## Harmonic Functions

$$
f: \Omega \to \mathbb{C} \text{ analytic}
$$
$$
f = u + iv
$$
$$
\frac{\partial u}{\partial x} = \frac{\partial v}{\partial y} \implies \frac{\partial^2 u}{\partial x^2} = \frac{\partial^2 v}{\partial x \partial y}
$$
$$
\frac{\partial u}{\partial y} = -\frac{\partial v}{\partial x} \implies \frac{\partial^2 u}{\partial y^2} = -\frac{\partial^2 v}{\partial y \partial x}
$$
Thus,
$$
\frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2} = 0 \quad \text{if } \frac{\partial^2 v}{\partial x \partial y} \text{ and } \frac{\partial^2 v}{\partial y \partial x} \text{ are continuous.}
$$
Similarly $\frac{\partial^2 v}{\partial x^2} + \frac{\partial^2 v}{\partial y^2} = 0$.

**Harmonic Functions**
Let $u: \Omega \to \mathbb{R}$ and let partial derivatives of $u$ up to 2nd order exist, then $u$ is *harmonic* if $\frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2} = 0$ on $\Omega$.

Let $\Omega = \mathbb{D} = \{ z \in \mathbb{C} : |z| < 1 \}$.
$u: \mathbb{D} \to \mathbb{R}$ is harmonic $\implies \frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2} = 0$ on $\Omega$.

Let assume $\exists v: \Omega \to \mathbb{R}$ s.t. $f = u + iv$ is analytic.
$$ g = f' = u_x + i v_x = u_x - i u_y \quad (\text{using CR}) $$

$$
\begin{align*}
U &= \text{Re } g = u_x \\
V &= \text{Im } g = -u_y
\end{align*}
$$
$$
\begin{align*}
U_x &= u_{xx} \\
V_y &= -u_{yy}
\end{align*}
$$
We have $U_x = V_y$ because $u_{xx} + u_{yy} = 0$.

Define
$$ h(z) = \int_{[0,z]} g(w) dw $$
One can prove $h$ is analytic and $h'(z) = g(z)$.
$$ h = \text{Re } h + i \text{Im } h $$
$$ h' = g = u_x - i u_y $$
Also since $h$ is analytic, $h' = (\text{Re } h)_x - i (\text{Re } h)_y$.
Comparing the terms, we get:
$$ (\text{Re } h)_x = u_x \quad \text{and} \quad (\text{Re } h)_y = u_y $$
$$ \implies \text{Re } h - u = C \quad (\text{constant}) $$
$$ \implies u = \text{Re } h - C $$
Set $v = \text{Im } h$. Then
$$ u + i v = (\text{Re } h - C) + i \text{Im } h = h - C $$
Since $h$ is analytic, $f = u + iv$ is analytic.


**Def:** Let $u,v:\Omega\to  \mathbb{R}$  harmonic, then $f$ $\exists v:\Omega \to \mathbb{R}$ such that $u + iv$ is analytic on $\Omega$ then $v$ is called a harmonic conjugate.

**Exercise:**  If $v_{1}, v_{2}$ are two harmonic conjugate of $u:\Omega\to \mathbb{R}$, then $v_{1}-v_{2}=\text{const}$.
**Exercise:** Show that $\log \lvert z \rvert$ is harmonic in $\mathbb{C}\setminus \{ 0 \}$ and conclude that $\log \lvert z \rvert$ can't have any harmonic conjugate in $\mathbb{C} \setminus \{ 0 \}$ 

## Complex Integration

```tikz
\usepackage{tikz}
\usepackage{amssymb}
\begin{document}
\begin{tikzpicture}[>=stealth, scale=0.8]
    % Interval [a,b]
    \draw[-] (0,0) -- (3,0);
    \draw[thick] (0.5, 0.1) -- (0.5, -0.1) node[below] {$a$};
    \draw[thick] (2.5, 0.1) -- (2.5, -0.1) node[below] {$b$};
    \draw[thick] (0.5,0) -- (2.5,0);
    
    % Domain Omega
    \begin{scope}[shift={(6,1)}]
        \draw[smooth cycle, tension=0.7] plot coordinates {(-1,-1) (2,-1.5) (3,1) (1,2.5) (-1.5, 1.5)};
        \node at (2, 2) {$\Omega \subseteq \mathbb{C}$};
        
        % Curve
        \draw[thick] (-0.5, -0.5) .. controls (0.5, 0.5) and (1.5, -0.5) .. (2.5, 0.5);
        \filldraw (-0.5, -0.5) circle (1pt) node[left] {$\gamma(a)$};
        \filldraw (2.5, 0.5) circle (1pt) node[right] {$\gamma(b)$};
        \node at (1.2, 0.2) {$\gamma(I)$};
    \end{scope}

    % Mapping arrow
    \draw[->, cyan, thick] (1.5, 0.5) to[bend left=30] node[midway, above, black] {$\gamma$} (5.5, 1.5);

    % Text

\end{tikzpicture}
\end{document}
```
**Def:** We define integration on a path $\mathscr{C} \subseteq \Omega$ parametrized by a piecewise smooth $\gamma$ and $f'(t) \neq 0$,
$$
\int_{\mathscr{C}} f(z) = \int_{a}^{b} f(\gamma(t)) \gamma'(t) dt
$$



**Proposition:**
Let $f, g: \Omega \to \mathbb{C}$ be continuous and $a, b \in \mathbb{C}$.

1. **Linearity**:
   $$
   \int_{\mathscr{C}} (af + bg)(z) dz = a \int_{\mathscr{C}} f(z) dz + b \int_{\mathscr{C}} g(z) dz
   $$

2. **Additivity over paths**:
   Let $\mathscr{C} = \sum_{i=1}^n \mathscr{C}_i$ be a contour formed by joining smooth curves $\mathscr{C}_1, \dots, \mathscr{C}_n$ end-to-end. Then we define:
   $$
   \int_{\mathscr{C}} f(z) dz = \sum_{i=1}^n \int_{\mathscr{C}_i} f(z) dz
   $$

```tikz
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[>=stealth]
    % Define points for the path
    \coordinate (P0) at (0,0);
    \coordinate (P1) at (1.5, 1);
    \coordinate (P2) at (3.5, 1);
    \coordinate (P3) at (5, 0);
    \coordinate (P4) at (4, -1);
    
    % Draw the segments
    \draw[->, thick] (P0) -- (P1) node[midway, above left] {$\mathcal{C}_1$};
    \draw[->, thick] (P1) -- (P2) node[midway, above] {$\mathcal{C}_2$};
    \draw[->, thick] (P2) -- (P3) node[midway, above right] {$\mathcal{C}_3$};
    \draw[->, thick] (P3) -- (P4) node[midway, below right] {$\mathcal{C}_4$};
    
    % Draw points
    \filldraw (P0) circle (1.5pt);
    \filldraw (P1) circle (1.5pt);
    \filldraw (P2) circle (1.5pt);
    \filldraw (P3) circle (1.5pt);
    \filldraw (P4) circle (1.5pt);
    
    % Label the whole curve
    \node[blue] at (2.5, 2) {$\mathcal{C}$};
\end{tikzpicture}
\end{document}
```


> [!Winding numbers:]-
>$$
>n(\gamma, 0) = \frac{1}{2\pi i} \int_{\gamma} \frac{dz}{z}
>$$
>is the winding number of $\gamma$ around the origin


**Exercise:** 
$$
\frac{1}{2\pi i} \int_{\gamma} \frac{1}{z-p} = 1 \quad p \in D_{R} \quad \gamma(t) = R e^{ 2\pi it }
$$


## Fundamental theorem of Complex integration
**Theorem:** Let $\gamma$ be any curve and let $f$ be a continuous function on $\gamma$ and exists $F$ such that $F' = f$, then $\int_{\gamma}f = F(\beta)-F(\alpha )$, where $\gamma(1)=\beta,\gamma(0)=\alpha$

**Proof:** 


$$
\begin{align*}
\int_{\gamma} f &= \int_{\gamma} F' \\
&= \int_{0}^{1} F'(\gamma(t)) \gamma'(t) dt \\
&= \int_{0}^{1} (F \circ \gamma)'(t) dt \\
&= F(\gamma(1)) - F(\gamma(0)) \\
&= F(\beta) - F(\alpha)
\end{align*}
$$
In particular, if $\gamma$ is closed then $\int_{\gamma} f = 0$.

**Corollary:** Let $\Omega \subseteq \mathbb{C}$ be a domain and let $f: \Omega \to \mathbb{C}$ be analytic with $f' \equiv 0$ on $\Omega$. Then $f \equiv \text{const}$ on $\Omega$.

**Theorem:(Cauchy's Integral Formula)**$f:\Omega  \to \mathbb{C}$ analytic, let $a \in \Omega$, $\overline{D(a,R)} \subseteq \Omega$, where $\gamma$ is $a + R e^{2\pi it}$.
$$
f(z) = \frac{1}{2\pi i} \int_{\gamma} \frac{f(w)}{w-z} dw \quad z \in D(a,R)
$$
**Proof:**
WLOG we take $a=0$ and $\gamma(t) = e^{2\pi i t}$.

We want to show:
$$
\frac{1}{2\pi i} \int_{\gamma} \frac{f(w)}{w-z} dw - f(z) = 0
$$
Let $w = e^{is}$.
$$
\begin{align*}
&\impliedby \frac{1}{2\pi i} \int_{0}^{2\pi} \frac{f(e^{is})}{e^{is}-z} i e^{is} ds - \frac{1}{2\pi} \int_{0}^{2\pi} f(z) ds \\
&\impliedby \frac{1}{2\pi} \int_{0}^{2\pi} \left[ \frac{f(e^{is})e^{is}}{e^{is}-z} - f(z) \right] ds = 0
\end{align*}
$$

To prove this, we construct $\phi$. Notice that the expression in the brackets corresponds to the value at $t=1$ of the function $\phi(s,t)$ defined below.

Let
$$
\phi(s,t) = \frac{f(z + t(e^{is}-z)) e^{is}}{e^{is}-z} - f(z)
$$
Then
$$
\phi(s,0) = \frac{f(z)}{e^{is}-z} e^{is} - f(z)
$$
$$
\int_0^{2\pi} \phi(s,0) ds = \int_0^{2\pi} \left[ \frac{e^{is} f(z)}{e^{is}-z} - f(z) \right] ds = 0
$$
Define $g(t) = \int_0^{2\pi} \phi(s,t) ds$. We want to show $g'(t) \equiv 0$.

$$
\frac{\partial \phi}{\partial t} = f'(z + t(e^{is}-z)) e^{is}
$$
On the other hand,
$$
\frac{\partial}{\partial s} \left( f(z + t(e^{is}-z)) \right) = f'(z + t(e^{is}-z)) \cdot t(ie^{is})
$$
Thus
$$
\frac{\partial \phi}{\partial t} = \frac{1}{it} \frac{\partial}{\partial s} \left( f(z + t(e^{is}-z)) \right)
$$
Therefore
$$
g'(t) = \int_0^{2\pi} \frac{\partial \phi}{\partial t} ds = \frac{1}{it} \int_0^{2\pi} \frac{\partial}{\partial s} \left( f(z + t(e^{is}-z)) \right) ds
$$
$$
= \frac{1}{it} \left[ f(z + t(e^{is}-z)) \right]_{s=0}^{2\pi} = 0
$$
Since the function is periodic in $s$ with period $2\pi$.
Thus $g(t)$ is constant, so $g(1) = g(0) = 0$, which concludes the proof.

## Power Series Expansion

Let $f$ be analytic in $D(a, R)$. Let $z \in D(a, R)$. Choose $r$ such that $|z-a| < r < R$. Let $\gamma(t) = a + r e^{it}$.
By Cauchy's Integral Formula:
$$
f(z) = \frac{1}{2\pi i} \int_{\gamma} \frac{f(w)}{w-z} dw
$$
We can rewrite the integrand as:
$$
\frac{1}{w-z} = \frac{1}{(w-a) - (z-a)} = \frac{1}{w-a} \cdot \frac{1}{1 - \frac{z-a}{w-a}}
$$
Since $w \in \gamma$, $|w-a| = r$ and $|z-a| < r$, so $\left| \frac{z-a}{w-a} \right| < 1$.
Thus we can expand it as a geometric series:
$$
\frac{1}{w-z} = \frac{1}{w-a} \sum_{n=0}^\infty \left( \frac{z-a}{w-a} \right)^n = \sum_{n=0}^\infty \frac{(z-a)^n}{(w-a)^{n+1}}
$$
Substituting this back into the integral:
$$
f(z) = \frac{1}{2\pi i} \int_{\gamma} f(w) \left[ \sum_{n=0}^\infty \frac{(z-a)^n}{(w-a)^{n+1}} \right] dw
$$
Since the series converges uniformly on $\gamma$ (compact set), we can swap the sum and the integral:
$$
f(z) = \sum_{n=0}^\infty \left[ \frac{1}{2\pi i} \int_{\gamma} \frac{f(w)}{(w-a)^{n+1}} dw \right] (z-a)^n
$$
Defining $c_n = \frac{1}{2\pi i} \int_{\gamma} \frac{f(w)}{(w-a)^{n+1}} dw$, we get the power series expansion:
$$
f(z) = \sum_{n=0}^\infty c_n (z-a)^n
$$
This proves that analytic functions are analytic in the sense of power series.

## Cauchy's Integral Formula for Derivatives

**Theorem**: If $f$ is analytic in a domain $\Omega$ containing the closed disk $\overline{D(a,R)}$, and $\gamma$ is the circle $|z-a|=R$ traversed counter-clockwise, then for any $z \in D(a,R)$:
$$
f^{(n)}(z) = \frac{n!}{2\pi i} \int_{\gamma} \frac{f(w)}{(w-z)^{n+1}} dw
$$
In particular, for $z=a$:
$$
f^{(n)}(a) = \frac{n!}{2\pi i} \int_{\gamma} \frac{f(w)}{(w-a)^{n+1}} dw
$$

## Cauchy's Estimates

From the formula for $f^{(n)}(a)$, we can derive an estimate for the magnitude of the derivatives.
Let $M = \sup_{w \in \gamma} |f(w)|$. Then:
$$
\begin{align*}
|f^{(n)}(a)| &= \left| \frac{n!}{2\pi i} \int_{\gamma} \frac{f(w)}{(w-a)^{n+1}} dw \right| \\
&\le \frac{n!}{2\pi} \int_{\gamma} \frac{|f(w)|}{|w-a|^{n+1}} |dw| \\
&\le \frac{n!}{2\pi} \frac{M}{R^{n+1}} \cdot 2\pi R \\
&= \frac{n! M}{R^n}
\end{align*}
$$
**Corollary:**
$$
|f^{(n)}(a)| \le \frac{n! M}{R^n}
$$

**Theorem(Liouville's Theorem):** Any bounded entire function is constant.
**Proof:** 
$$
\lvert f^{(n)} \rvert (z) \leq \frac{n!M}{R^{n}}  \to 0 \text{ as } R \to \infty  
$$
implies the power series is a constant term.$\quad \blacksquare$

**Corollary (Exercise):** Let $\gamma$ be a closed smooth curve in $\Omega$ and let $f: \Omega \to \mathbb{C}$ be analytic. Then $\int_{\gamma} f = 0$.

**Exercise:** For any $P$ non-const polynomial $\exists a_{1},\dots,a_{n} \in \mathbb{C}$ and $m_{1},\dots,m_{n} \in \mathbb{Z}_{+}$ such that 
$$
P(z) = A\prod_{j=1}^{n} (z-a_{j})^{m_{j}}  \quad A \in \mathbb{C}
$$

## Zeros of Analytic Functions

**Definition:** Let $f$ be analytic in a domain $\Omega$. A point $a \in \Omega$ is called a **zero of multiplicity $m$** (or order $m$) for $f$ if there exists an analytic function $g$ in a neighborhood of $a$ such that $g(a) \neq 0$ and
$$
f(z) = (z-a)^m g(z)
$$
for all $z$ in that neighborhood. This is equivalent to saying that $f(a) = f'(a) = \dots = f^{(m-1)}(a) = 0$ and $f^{(m)}(a) \neq 0$.


**Theorem:** Let $\Omega \subseteq \mathbb{C}$ be a domain and $f:\Omega \to \mathbb{C}$ analytic TFAE:
1. $f \equiv 0$ on $\Omega$
2. $\exists$ a point $a \in \Omega$ such that $f^{(n)} (a) = 0, \forall n\geq 0$ 
3. $\{ z \in \Omega : f(z)=0 \}$ has a limit point in $\Omega$

**Proof:** 
$(1)\implies (2)$ Trivial
$(2) \implies (1)$ Consider $a \in \{ z \mid f(z)^{(n)} = 0, \forall n\geq 0 \}$, then we get the set is closed and open since at every point there is a power series converging.
$(2) \implies (3)$ Trivial
$(3) \implies (2)$ Let $Z = \{ z \in \Omega : f(z)=0 \}$. Let $a$ be a limit point of $Z$ in $\Omega$. Since $f$ is continuous, $f(a)=0$.
Suppose $(2)$ is false at $a$, i.e., not all derivatives vanish. Let $m$ be the smallest integer such that $f^{(m)}(a) \neq 0$. Since $f(a)=0$, we have $m \ge 1$.
Then we can write $f(z) = (z-a)^m g(z)$ where $g$ is analytic in a neighborhood of $a$ and $g(a) \neq 0$.
By continuity of $g$, there exists $\epsilon > 0$ such that $g(z) \neq 0$ for all $z \in D(a, \epsilon)$.
Thus for $z \in D(a, \epsilon) \setminus \{a\}$, we have $f(z) = (z-a)^m g(z) \neq 0$.
This implies $a$ is an isolated zero of $f$, which contradicts the assumption that $a$ is a limit point of $Z$.
Therefore, we must have $f^{(n)}(a) = 0$ for all $n \ge 0$. $\quad \blacksquare$ 

## Maximum Modulus principle

> [!TIP] Theorem 3.11: Maximum Modulus Theorem
> If $G$ is a region and $f: G \to \mathbb{C}$ is an analytic function such that there is a point $a$ in $G$ with $|f(a)| \ge |f(z)|$ for all $z$ in $G$, then $f$ is constant.

> [!NOTE]- Proof
> Let $\bar{B}(a; r) \subset G$, $\gamma(t) = a + re^{it}$ for $0 \le t \le 2\pi$
> $$
> f(a) = \frac{1}{2\pi i} \int_\gamma \frac{f(w)}{w - a} \, dw = \frac{1}{2\pi} \int_0^{2\pi} f(a + re^{it}) \, dt
> $$
> Hence
> $$
> |f(a)| \le \frac{1}{2\pi} \int_0^{2\pi} |f(a + re^{it})| \, dt \le |f(a)|
> $$
> since $|f(a + re^{it})| \le |f(a)|$ for all $t$. This gives that
> $$
> 0 = \int_0^{2\pi} \left[ |f(a)| - |f(a + re^{it})| \right] dt;
> $$
> but since the integrand is non-negative it follows that $|f(a)| = |f(a + re^{it})|$ for all $t$. Moreover, since $r$ was arbitrary, we have that $f$ maps any disk $B(a; R) \subset G$ into the circle $|z| = |\alpha|$ where $\alpha = f(a)$. But this implies that $f$ is constant on $B(a; R)$. In particular $f(z) = \alpha$ for $|z - a| < R$. $f \equiv \alpha$.
> $\blacksquare$


## Homotopic versions of Cauchy's Theorem

> [!INFO] Definition: Homotopy (Fixed Endpoints)
> Let $\gamma_1, \gamma_2 : [0,1] \to \Omega$ be two paths in a domain $\Omega \subseteq \mathbb{C}$ such that they share the same initial point $\alpha = \gamma_1(0) = \gamma_2(0)$ and final point $\beta = \gamma_1(1) = \gamma_2(1)$. 
> $\gamma_1$ is said to be **homotopic** to $\gamma_2$ in $\Omega$ (with fixed endpoints), denoted by $\gamma_1 \sim \gamma_2$, if there exists a continuous function $F: [0,1] \times [0,1] \to \Omega$ such that:
> 1.  $F(s, 0) = \gamma_1(s)$ for all $s \in [0,1]$ (Initial curve)
> 2.  $F(s, 1) = \gamma_2(s)$ for all $s \in [0,1]$ (Final curve)
> 3.  $F(0, t) = \alpha$ for all $t \in [0,1]$ (Fixed start point)
> 4.  $F(1, t) = \beta$ for all $t \in [0,1]$ (Fixed end point)
>
> Intuitively, $F$ represents a continuous "deformation" of the curve $\gamma_1$ into $\gamma_2$ while keeping the endpoints fixed.

```tikz
\begin{document}
\begin{tikzpicture}[>=stealth, scale=0.8]
    % Draw Domain Omega
    \draw[thick, black] plot [smooth cycle, tension=0.7] coordinates {(-3,-2) (3,-2.5) (3.5,2) (-2.5,2.5) (-4,0)};
    \node at (2.5, 1.5) {$\Omega$};

    % Fixed endpoints
    \coordinate (Alpha) at (-2, 0);
    \coordinate (Beta) at (2, 0);

    % Draw Gamma 1 (Upper curve)
    \draw[thick, blue] (Alpha) .. controls (-1, 1.5) and (1, 1.5) .. (Beta);
    \node[blue, above] at (0, 1.2) {$\gamma_1$};

    % Draw Gamma 2 (Lower curve)
    \draw[thick, red] (Alpha) .. controls (-1, -1.5) and (1, -1.5) .. (Beta);
    \node[red, below] at (0, -1.2) {$\gamma_2$};

    % Draw intermediate curves (deformation)
    \draw[dashed, gray!70] (Alpha) .. controls (-1, 0.8) and (1, 0.8) .. (Beta);
    \draw[dashed, gray!70] (Alpha) .. controls (-1, -0.8) and (1, -0.8) .. (Beta);
    \draw[dashed, gray!70] (Alpha) -- (Beta);

    % Points
    \filldraw[black] (Alpha) circle (2pt) node[left] {$\alpha$};
    \filldraw[black] (Beta) circle (2pt) node[right] {$\beta$};

    % Arrow indicating deformation
    \draw[->, black, thick] (0, 1.0) -- (0, 0.2);
    \node[right] at (0, 0.6) {$F(s,t)$};

\end{tikzpicture}
\end{document}
```


> [!TIP] Theorem: Homotopy Version 1 (Fixed Endpoints)
> Let $f: \Omega \to \mathbb{C}$ be analytic. Let $\gamma_1, \gamma_2$ be paths in $\Omega$ from $\alpha$ to $\beta$ such that $\gamma_1 \sim \gamma_2$ (homotopic with fixed endpoints). Then:
> $$ \int_{\gamma_1} f(z) dz = \int_{\gamma_2} f(z) dz $$

> [!NOTE]- Proof
> **Will be proved in class later**

> [!TIP] Theorem: Homotopy Version 2 (Closed Curves)
> Let $f: \Omega \to \mathbb{C}$ be analytic. Let $\gamma$ be a closed curve in $\Omega$ such that $\gamma \sim 0$ (null-homotopic) in $\Omega$. Then:
> $$ \int_{\gamma} f(z) dz = 0 $$

> [!TIP] Corollary
> Let $\Omega \subseteq \mathbb{C}$ be a simply connected domain and let $\gamma$ be a closed curve in $\Omega$. Then $\int_{\gamma} f(z) dz = 0$.


> [!INFO] Definition: Simply Connected Domain
> A domain $\Omega \subseteq \mathbb{C}$ is said to be **simply connected** if any closed curve $\gamma$ in $\Omega$ is null-homotopic ($\gamma \sim 0$) in $\Omega$.

> [!TIP] Theorem: Existence of Primitives
> Let $\Omega$ be simply connected and let $f: \Omega \to \mathbb{C}$ be analytic.
> Then $f$ has a primitive in $\Omega$, i.e., there exists $F$ analytic in $\Omega$ such that $F' = f$ in $\Omega$.

> [!NOTE]- Proof (Sketch)
> Let $z_{0} \in \Omega$, Define $F(w) = \int_{\gamma} f dz$, where $\gamma$ is a smooth curve from $z_{0}$ to  $w$, since $\Omega$ is simply connected we have that $\int_{\gamma} f dz = \int_{\gamma'}f dz$ if $\gamma'$ is another path from $z_{0}$ to $w$. Hence $F$ is a well defined function. Now take $r$ small enough such that $z+h \in \Omega,\forall \lvert h \rvert<r$
> $$
> \frac{F(z+h) - F(z)}{h} = \frac{1}{h} \int_{[z,z+h]} f(\zeta) \, d\zeta = \frac{1}{h} \int_{0}^{1} f(z+th) h \, dt = \int_{0}^{1} f(z+th) \, dt
> $$
> where $[z,z+h]$ is the straight line path.
> Since $f$ is continuous, $f(z+th) \to f(z)$ as $h \to 0$. Thus,
> $$
> \lim_{h \to 0} \frac{F(z+h) - F(z)}{h} = \int_{0}^{1} f(z) \, dt = f(z)
> $$
> Hence, $F$ is holomorphic and $F'(z) = f(z)$. $\blacksquare$
> 


> [!TIP] Theorem: (Morera's Theorem)
> Let $\Omega \subseteq \mathbb{C}$ be a domain and $f: \Omega\to \mathbb{C}$ continuous. Assume $\int_{T}f=0$ for all triangle $T$ in $\Omega$, then $f$ is analytic.

> [!NOTE]- Proof
> Let $D(a,r) \subseteq \Omega$. For any $z \in D(a,r)$, define
> $$ F(z) = \int_{[a,z]} f(\zeta) \, d\zeta $$
> where $[a,z]$ denotes the straight line segment from $a$ to $z$.
> Let $z \in D(a,r)$ and $h \in \mathbb{C}$ such that $z+h \in D(a,r)$. By the hypothesis, the integral over the triangle with vertices $a, z, z+h$ is zero:
> $$ \int_{[a,z]} f(\zeta) \, d\zeta + \int_{[z,z+h]} f(\zeta) \, d\zeta + \int_{[z+h,a]} f(\zeta) \, d\zeta = 0 $$
> $$ \implies F(z) + \int_{[z,z+h]} f(\zeta) \, d\zeta - F(z+h) = 0 $$
> $$ \implies F(z+h) - F(z) = \int_{[z,z+h]} f(\zeta) \, d\zeta $$
> Now consider the difference quotient:
> $$ \frac{F(z+h) - F(z)}{h} = \frac{1}{h} \int_{[z,z+h]} f(\zeta) d\zeta =\int_{0}^{1} f(z+th) dt$$
> Taking the limit we see that $F$ is holomorphic and $F' = f$, since holomorphic functions are infinitely differentiable.
> $\blacksquare$

## Winding Number / Index of a curve

Let $\gamma$ be a closed curve $\gamma \subseteq \Omega$. Then we define winding number of $\gamma$ around $a$ as.
$$
\eta (\gamma, a) = \frac{1}{2\pi i} \int_{\gamma} \frac{dz}{z-a} \quad a \not\in  \gamma 
$$

1. $\eta(\gamma,a) \in \mathbb{Z}$
2. $\eta(\boldsymbol{\gamma},\cdot) : \mathbb{C} \setminus \{ \gamma \} \to \mathbb{Z}$ is a continuous function.

$$
\begin{align}
\eta(\gamma,a)  & = \frac{1}{2\pi i} \int_{\gamma} \frac{dz}{z-a} \\
 & = \frac{1}{2\pi i} \int_{0}^{1} \frac{\gamma'(s)ds}{\gamma(s)-a} \\

\end{align}
$$
Define $g(t)= \int_{0}^{t} \frac{\gamma'(s)ds}{\gamma(s)-a}$. Note that $g(0)=0$ and $g(1)= 2\pi i \eta(\gamma,a)$.

Consider the function $G(t) = e^{-g(t)}(\gamma(t)-a)$.
Differentiating with respect to $t$:
$$
\begin{align*}
G'(t) &= e^{-g(t)}\gamma'(t) + (\gamma(t)-a) e^{-g(t)}(-g'(t)) \\
&= e^{-g(t)}\gamma'(t) - (\gamma(t)-a) e^{-g(t)} \frac{\gamma'(t)}{\gamma(t)-a} \\
&= e^{-g(t)}\gamma'(t) - e^{-g(t)}\gamma'(t) \\
&= 0
\end{align*}
$$
Thus, $G(t)$ is constant.
Equating the values at $t=0$ and $t=1$:
$$
\begin{align*}
G(0) &= e^{-g(0)}(\gamma(0)-a) = 1 \cdot (\gamma(0)-a) = \gamma(0)-a \\
G(1) &= e^{-g(1)}(\gamma(1)-a)
\end{align*}
$$
Since $\gamma$ is a closed curve, $\gamma(0) = \gamma(1)$. Also $\gamma(t) \neq a$ for all $t$.
$$
\gamma(0)-a = e^{-g(1)}(\gamma(0)-a) \implies e^{-g(1)} = 1
$$
This implies that $g(1)$ must be an integer multiple of $2\pi i$.
$$
g(1) = 2\pi i k \quad \text{for some } k \in \mathbb{Z}
$$
Since $\eta(\gamma, a) = \frac{1}{2\pi i} g(1)$, we have $\eta(\gamma, a) = k \in \mathbb{Z}$.

**Proof of (2): Continuity of $\eta(\gamma, \cdot)$**
Let $a \in \mathbb{C} \setminus \gamma$. Since $\gamma$ is a closed set (image of compact set), there exists $\delta > 0$ such that $D(a, \delta) \cap \gamma = \emptyset$.
Let $b \in D(a, \delta/2)$. Then for any $z \in \gamma$, $|z-a| \ge \delta$ and $|z-b| \ge \delta/2$.
Consider the difference:
$$
\begin{align*}
|\eta(\gamma, a) - \eta(\gamma, b)| &= \left| \frac{1}{2\pi i} \int_\gamma \left( \frac{1}{z-a} - \frac{1}{z-b} \right) dz \right| \\
&= \frac{1}{2\pi} \left| \int_\gamma \frac{a-b}{(z-a)(z-b)} dz \right| \\
&\le \frac{1}{2\pi} \int_\gamma \frac{|a-b|}{|z-a||z-b|} |dz| \\
&\le \frac{|a-b|}{2\pi} \frac{1}{\delta \cdot (\delta/2)} \text{length}(\gamma)
\end{align*}
$$
As $b \to a$, the right hand side goes to 0. Thus $\eta(\gamma, \cdot)$ is continuous at $a$.
Since $\eta$ is continuous and integer-valued, it must be constant on each connected component of $\mathbb{C} \setminus \gamma$. $\blacksquare$

### Covering spaces

> [!INFO] Definition: Covering Map
> Let $E$ and $X$ be topological spaces. A continuous surjective map $p: E \to X$ is called a **covering map** if for every $x \in X$, there exists an open neighborhood $U \subseteq X$ such that $p^{-1}(U)$ is a disjoint union of open sets $V_\alpha \subseteq E$:
> $$ p^{-1}(U) = \bigsqcup_{\alpha \in A} V_\alpha $$
> where for each $\alpha \in A$, the restriction $p|_{V_\alpha}: V_\alpha \to U$ is a homeomorphism. The neighborhood $U$ is said to be **evenly covered**. refer [[Algebraic Topology#Covering Spaces|Covering Spaces]]

$\gamma_{1},\gamma_{2}$  are two curves $\gamma_{1}\sim \gamma_{2}$ in $\mathbb{C}\setminus \{ a \}$
$$
\eta(\gamma_{1};a) = \frac{1}{2\pi i} \int_{\gamma_{1}} \frac{dz}{z-a} = \frac{1}{2\pi i} \int_{\gamma_{2}} \frac{dz}{z-a} = \eta(\gamma_{2};a)
$$

> [!QUESTION] Question
> Is the converse true?
> Does $\eta(\gamma_1; a) = \eta(\gamma_2; a)$ imply $\gamma_1 \sim \gamma_2$ in $\mathbb{C} \setminus \{a\}$?


### Lifting of Curves

> [!INFO] Definition: Lift of a Curve
> Let $p: \mathbb{C} \to \mathbb{C} \setminus \{a\}$ be the covering map $z \mapsto e^z + a$. Let $\gamma: [0,1] \to \mathbb{C} \setminus \{a\}$ be a curve. A curve $\tilde{\gamma}: [0,1] \to \mathbb{C}$ is called a **lift** of $\gamma$ if $p \circ \tilde{\gamma} = \gamma$.

```tikz
\usepackage{tikz-cd}
\usepackage{amssymb}
\begin{document}
\begin{tikzcd}
    & \mathbb{C} \arrow[d, "e^z + a"] \\
    {[0,1]} \arrow[ur, "\tilde{\gamma}", dashed] \arrow[r, "\gamma"] & \mathbb{C} \setminus \{a\}
\end{tikzcd}
\end{document}
```
$$
\eta(\gamma_1,a) = \eta(\gamma_{2},a) \quad a \not\in \gamma_{1} \cup \gamma_{2}
$$
Implies $\gamma_{1} \sim \gamma_{2}$ in $\mathbb{C}\setminus \{ a \}$.
$$
\begin{align*}
\eta(\gamma_j,a) &= \frac{1}{2\pi i} \int_{\gamma_j} \frac{dz}{z-a} \\
&= \frac{1}{2\pi i} \int_{0}^{1} \frac{1}{(e^{\tilde{\gamma}_j(t)} + a) - a} \cdot \frac{d}{dt}(e^{\tilde{\gamma}_j(t)} + a) \, dt \\
&= \frac{1}{2\pi i} \int_{0}^{1} \frac{ e^{\tilde{\gamma}_j(t)} \tilde{\gamma}_j'(t)}{e^{\tilde{\gamma}_j(t)}} dt \\
&= \frac{1}{2\pi i} \int_{0}^{1} \tilde{\gamma}_j'(t) dt \\
&= \frac{\tilde{\gamma}_j(1) - \tilde{\gamma}_j(0)}{2\pi i}
\end{align*}
$$
Then we have that $\gamma_{2}(1) = \gamma_{2}(1)$, hence $\tilde{\gamma}_{1},\tilde{\gamma}_{2}$ have the fixed endpoints, since $\mathbb{C}$ is simply connected, $\tilde{\gamma_{1}},\tilde{\gamma_{2}}$ are homotopic, hence its images are also homotopic. $\quad \blacksquare$

> [!NOTE] Note
> We are using the following results from [[Algebraic Topology#Lifting theorems|Algebraic Topology]]:
> 1. **Lifting Theorem**: For a covering map $p: E \to X$, paths can be lifted uniquely given a starting point such that $p(\tilde{\gamma}(0)) = \gamma(0)$.
> 2. The projection of a homotopy in the covering space gives a homotopy in the base space.

## Open mapping theorem

$$
f(z) = (z-a_{1})\dots(z - a_{n})g(z)\quad z \in \Omega 
$$
For some non-vanishing $g$ on $\Omega$. 
$$
\frac{f'(z)}{f(z)} = \frac{1}{z-a_{1}} + \dots + \frac{1}{z- a_{n}} + \frac{g'(z)}{g(z)}
$$
$$
\begin{align}

 \frac{1}{2\pi i} \int_{\gamma } \frac{f'(z)}{f(z)}  & = \frac{1}{2\pi i} \left[  \int_{\gamma} \frac{1}{z-a_{1}}  + \dots + \int_{\gamma} \frac{1}{z-a_{n}}\right] + \frac{1}{2\pi i}\int_{\gamma } \frac{g'(z)}{g(z)} \\
 & = \eta ( \gamma; a_{1}) + \dots + \eta(\gamma; a_{n}) + 0 \\
\end{align}
$$


> [!TIP] Theorem: 
> Let $\Omega \subseteq \mathbb{C}$ be a domain let $f:\Omega\to \mathbb{C}$ analytic and let $\gamma$ be a smooth curve in $\Omega$ such that $\gamma  \sim 0$. Let $a_{1},\dots,a_{n}$ are the zeroes of $f$ in $\Omega$ enclosed by the curve $\gamma$ then,
> $$
\frac{1}{2\pi i} \int_{\gamma } \frac{f'(z)}{f(z)-a} = \sum_{k=1}^{n} \eta(\gamma;\xi_{k}(\alpha ))
>$$
>where $\xi_{k}(\alpha)$ are the zeroes of $f(z)=\alpha$ enclosed by the curve $\gamma$.
> 

$\exists$ a small disc around $\alpha$, say $B(\alpha;\delta )$ and a small disc around $a$, say $B(a;\varepsilon )$ such that any point $\zeta \in B(\alpha,\delta)$ has exactly m solutions in the preimage 

$f(a) = \alpha$, $\exists$ a small nbd around a, lets say $B_{a}(\varepsilon )$ such that $f(z)=\alpha$. has exactly no other zero apart from $a$ in

> [!TIP] Theorem: Open mapping theorem
> Let $\Omega \subseteq \mathbb{C}$ be a domain and let $f:\Omega \to \mathbb{C}$ non-constant analytic function then $f(\Omega)$ is an open set of $\mathbb{C}$ 

> [!TIP] Corollary 
> $f:\Omega\to \mathbb{C}$ analytic ,if it is $1-1$ then $f^{-1}$ exists on $f(\Omega)$ and $f^{-1}$ is analytic on $f(\Omega )$ .

> [!TIP] Theorem: Goursat's theorem
> Any complex differentiable function is complex analytic

> [!NOTE]- Proof
> 

## Singularities
> [!INFO] Definition: 
> $\Omega \subseteq \mathbb{C}$ domain, $f:\Omega \setminus \{ p \}\to \mathbb{C}$ analytic. Then $p$ is called a singularity of $f$.

## Types of singularities

1. Removable singularity
2. Poles
3. Essential singularity

> [!INFO] Definition: Removable Singularity
> Let $f:D(p,R) \setminus \{ a \}\to \mathbb{C}$ be analytic. Then $p$ is called a removable singularity of $f$ if $\exists$ an analytic function $g:D(p,R)\to \mathbb{C}$ such that $g \equiv f$ on $D(p,R)\setminus \{ p \}$

**Example:** $\frac{\sin z} {z}$ on $D(0,1)$
$\sin z = z - \frac{z^{3}}{3!}+ \dots$
**Observations:** 
1. $zf(z) = \sin z$
2. $sinz/z$ is bounded near 0

> [!TIP] Theorem: 
> Let $f:D(p,R)\setminus \{ p \}\to \mathbb{C}$ be an analytic. Then $f$ has removable singularity at $p$ $\iff$ $\lim_{ z \to p } (z-p)f(z)=0$

> [!NOTE]- Proof
> $\implies$ Trivial
> $\impliedby$ Define $g(z) = (z-p)f(z)$ $z\neq p$. $g(p)=0$. Then $g$ is continuous.
> **Claim:** $g$ is also analytic
> We use Morera's thm to show that $g$ is analytic.
> 

