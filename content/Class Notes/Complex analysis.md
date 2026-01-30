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

## Differentiation of Power Series
   
   **Theorem**: The power series $f(z) = \sum_{n=0}^\infty a_n (z-z_0)^n$ has the same radius of convergence $R$ as its derived series $g(z) = \sum_{n=1}^\infty n a_n (z-z_0)^{n-1}$. Furthermore, $f'(z) = g(z)$ for all $|z-z_0| < R$.

   **Proof**:
   1.  **Same Radius of Convergence**:
       Using $\lim_{n \to \infty} n^{1/n} = 1$, we have:
       $$ \limsup_{n \to \infty} |n a_n|^{1/n} = \lim_{n \to \infty} n^{1/n} \cdot \limsup_{n \to \infty} |a_n|^{1/n} = 1 \cdot \frac{1}{R} = \frac{1}{R} $$
       Thus, the derived series converges for the same $R$.
   
   2.  **Term-by-Term Differentiation**:
       We want to show $f'(z) = g(z)$. Fix $z \in D_R(z_0)$ and let $h$ be small enough so $z+h \in D_R(z_0)$.
       Consider the difference quotient:
%%        $$ \Delta = \left| \frac{f(z+h) - f(z)}{h} - g(z) \right| = \left| \sum_{n=0}^\infty a_n \left( \frac{(z-z_0+h)^n - (z-z_0)^n}{h} - n(z-z_0)^{n-1} \right) \right| $$
       Using the inequality $\left| \frac{(a+b)^n - a^n}{b} - n a^{n-1} \right| \le \frac{n(n-1)}{2} (|a|+|b|)^{n-2} |b|$, we set $a=z-z_0, b=h$.
       For $|z-z_0| \le r < R$ and small $|h|$, we can bound the terms by a convergent series (related to $f''$).
       As $h \to 0$, the tail sums vanish, proving $\lim_{h \to 0} \Delta = 0$. Thus $f'(z) = g(z)$.

**Theorem (Infinite Differentiability)**:
A power series $f(z) = \sum a_n (z-z_0)^n$ is infinitely complex differentiable inside its radius of convergence $R$. %%

%% **Proof**:
From the theorem above, $f'(z)$ exists and is given by a power series with the same radius $R$.
Since $f'(z)$ is itself a power series with radius $R$, it is also holomorphic on $D_R(z_0)$.

Applying the result recursively:
1.  $f$ is holomorphic $\implies f'$ exists and is a power series with radius $R$.
2.  $f'$ is holomorphic $\implies f'' = (f')'$ exists and is a power series with radius $R$.
3.  By induction, $f^{(k)}$ exists for all $k \in \mathbb{N}$ and is a power series with radius of convergence $R$.
Thus, $f$ is infinitely differentiable.
 %%

**Proposition:** Let $P(z)= \sum_{n\geq_{0}}^{} a_{n}(z-z_0)^{n}$ be a power series in $\mathbb{C}$ with radius of convergence  $R>0$. Let $w_{0} \in D(z_{0},R)$.

```tikz
\begin{document}
\begin{tikzpicture}[>=stealth]
    % Define points
    \coordinate (Z0) at (0,0);
    \coordinate (W0) at (1.5, 1);
    \def\R{3}
    
    % Draw Disk D(z0, R)
    \draw[dashed, fill=blue!5] (Z0) circle (\R);
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
P(z) = \sum_{n\geq{1}}^{} \frac{P^{n}(w_{0})}{n!}(z-w_{0})^{n}
$$
where $z \in D_{w_{0}}(R')$, $R' = R - \lvert z_{0} - w_{0} \rvert$

**Proof:**

---
LOG + CR

---

We define 2 differential operators
$$
\frac{\partial}{\partial z} = \frac{1}{2} \left( \frac{\partial}{\partial x} - i \frac{\partial}{\partial y} \right) \quad \text{and} \quad \frac{\partial}{\partial \bar{z}} = \frac{1}{2} \left( \frac{\partial}{\partial x} + i \frac{\partial}{\partial y} \right)
$$
If $f = u + iv$ is analytic, it satisfies the Cauchy-Riemann equations $u_x = v_y$ and $u_y = -v_x$.

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

## Harmonic Functions

![[IMG_20260130_144714.jpg]]
![[Pasted image 20260130144802.png]]