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

**Def:** Let $u:\Omega\to  \mathbb{R}$  harmonic, then $f$ $\exists v:\Omega \to \mathbb{R}$ such that $u + iv$ is analytic on $\Omega$ then $v$ is called a harmonic conjugate.

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
\int_{\mathscr{C}} f(z) = \int_{a}^{b} f(t) \gamma'(t) dt
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

**Theorem:(Cauchy's Integral Formula)**$f:\gamma \to \mathbb{C}$ analytic, let $a \in \Omega$, $\overline{D(a,R)} \subseteq \Omega$, where $\gamma$ is $a + R e^{2\pi it}$.
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


**Definition:** Let $f$ be analytic in a domain $\Omega$. A point $a \in \Omega$ is called a **zero of multiplicity $m$** (or order $m$) for $f$ if there exists an analytic function $g: \Omega \to \mathbb{C}$ such that $g(a) \neq 0$ and
$$
f(z) = (z-a)^m g(z)
$$
for all $z \in \Omega$. This is equivalent to saying that $f(a) = f'(a) = \dots = f^{(m-1)}(a) = 0$ and $f^{(m)}(a) \neq 0$.



