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

**Definition**: A function $f$ is said to be **analytic** at a point $z_0$ if it can be represented by a convergent power series in a neighborhood of $z_0$. 

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
3. $$
\frac{1}{R} = \lim \sup \lvert a_{n} \rvert ^{1/n}
$$ where $R$ is the radius of convergence
**Cauchy-Hadamard Theorem**:
   For the power series $\sum a_n (z-z_0)^n$, let $\alpha = \limsup_{n \to \infty} |a_n|^{1/n}$. Then the radius of convergence is $R = 1/\alpha$ (with conventions $1/0 = \infty, 1/\infty = 0$).
   Since $\limsup \lvert a_{n} \rvert ^{1/n} = \frac{1}{R}$ then $\limsup \lvert a_{n}(z-z_{0})^{n} \rvert ^{1/n} =  \frac{\lvert z-z_{0} \rvert}{R}$
   
   **Proof**:
   Apply Root Test to $\sum |a_n (z-z_0)^n|$. Let $L = \limsup |a_n (z-z_0)^n|^{1/n} = |z-z_0|/R$.
   *   If $|z-z_0| < R \implies L < 1$, series converges absolutely.
   *   If $|z-z_0| > R \implies L > 1$, then $|a_n (z-z_0)^n| > 1$ for infinitely many $n$, so terms don't vanish. Series diverges.
**Exercise:**  $R  = \lim_{ n \to \infty } \left\lvert  \frac{a_{n}}{a_{n+1}}  \right\rvert$ whenever it exists
**Examples:**
$\sum_{n\geq 0}^{} z^{n} = \frac{1}{1-z}$ $R=1$
$\sum_{n\geq{1}}^{} \frac{z^{n}}{n}$  $R=1$ 
$\sum_{n\geq 1}^{} \frac{z^{n}}{n!}$ $R = \infty$
4. **Abel's Test**:
   If the series $\sum_{n=0}^\infty a_n$ converges and $\{b_n\}$ is a bounded, monotonic sequence of real numbers, then the series $\sum_{n=0}^\infty a_n b_n$ converges.
5. Differentiation of power series:$$ \begin{align}
P(z) = \sum_{}^{} a_{n} z^{n} \\
P'(z) = \sum_{n}^{} na_{n} z^{n-1}
\end{align}
$$
we see that if $P$ converges in radius $R$ then we have $$
 \lim \sup \lvert n a_{n} \rvert ^{1/n-1} = \lim \sup \lvert (n+1) a_{n+1} \rvert ^{1/n} = \lim \sup \lvert n a_{n} \rvert  ^{1/n} = \frac{1}{R}
$$
