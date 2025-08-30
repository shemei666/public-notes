---
draft: false
---

# Part A  
**Muhammed Shameel KV**
**bmat2330@isibang.ac.in**

---

1. Determine (with justification) whether the following statements are true or false:

$(i)$ Every continuous function $f \in C[1, 2]$ can be uniformly approximated by a sequence of even polynomials.  

**Answer:** The statement is true since even polynomials form an algebra. We can see this as follows: if $f,g$ are 2 even polynomials then,
$$
\begin{gather*}
f \cdot g = \sum_{i=0}^n a_i x^{2i} \cdot \sum_{j=0}^m b_j x^{2j} = \sum_{k=0}^{n+m} c_k x^{2k}, \\
f + g = \sum_{i=0}^n a_i x^{2i} + \sum_{j=0}^m b_j x^{2j} = \sum_{k=0}^{\max(n,m)} d_k x^{2k}, \\ \\
cf = c \cdot \sum_{i=0}^n a_i x^{2i} = \sum_{i=0}^n (c a_i) x^{2i},
\end{gather*}
$$
Hence even polynomials on $[1,2]$ form an algebra

Since even polynomials contain the constant function (the polynomial $P(x) = 1$) and separate points on $[1,2]$ (for any $x,y \in [1,2]$, $x \neq y$, the polynomial $P(x) = x^2$ is even and separates $x$ and $y$), by the **Stone-Weierstrass theorem**, the set of even polynomials is dense in $C[1,2]$. Thus, every continuous function on $[1,2]$ can be uniformly approximated by a sequence of even polynomials.

---

$(ii)$ Every continuous function $f \in C[1, 2]$ can be uniformly approximated by a sequence of odd polynomials.  

**Answer:**  This statement is also true. If $f:[1,2] \to \mathbb{R}$ is any continuous function, we can consider a function $g:[1,2], g(x) =\frac{f(x)}{x}$. Now this is also continuous since $x\neq0$ in $[1,2]$. Hence by $(i)$ we have that $g$ can be uniformly approximated by a sequence of even polynomials $\{P_n\}$. Now consider the sequence of odd polynomials $\{Q_n\}$ where $Q_n(x) = x P_n(x)$. $\exists N \in \mathbb{N}$ such that, $\|g -P_{n}\|_{\infty} < \frac{\varepsilon}{2}$ for $n\geq N$
$$
\begin{align*}
\|f - Q_n\|_\infty =& \|f - x P_n\|_\infty = \|xg - xP_n\|_\infty  \\
 =& \|x(g-P_n)\|_\infty  \leq  2\|g - P_{n}\|_{\infty } < \frac{2\varepsilon}{2} = \varepsilon  
\end{align*}
\quad \text{for } n\geq N
$$

---

$(iii)$ Every continuous function $f \in C[0, 1]$ can be uniformly approximated by a sequence of even polynomials.  

**Answer:**  This statement is also true. The same argument as in $(i)$ goes through.

---

$(iv)$ Every continuous function $f \in C[0, 1]$ can be uniformly approximated by a sequence of odd polynomials.  

**Answer:**  This statement is false since all odd polynomials needs to be $0$ at $0$. Hence any sequence $\{ q_{n} \}$ of odd polynomials should converge pointwise at $0$ to $0$ i.e. $\lim_{ n \to \infty }q_{n}(0) = 0$. So continuous functions with $f(0) \neq 0$ cannot be uniformly approximated. 

---

2. Fix some function $f : \mathbb{R} \to \mathbb{R}$. Define a sequence of functions $f_n : \mathbb{R} \to \mathbb{R}$ by  

$$
f_n(x) = f(nx), \quad (x \in \mathbb{R})
$$  

If $\{ f_n \}$ forms an equicontinuous family then show that $f$ is constant.  

**Answer:** By assumption of equicontinuity we have, $\forall\varepsilon>0, \exists \delta>0$ such that,
$$
\begin{gather*}
|f_{n}(0) - f_{n}(y)| < \varepsilon \quad \text{for } |y|<\delta, \forall n \in \mathbb{N} \\
|f(0) - f(ny)| < \varepsilon
\end{gather*}
$$
Since $\exists N_{0} \in \mathbb{N}$ such that  $\forall r \in \mathbb{R},\left\lvert  \frac{r}{N_{0}}  \right\rvert < \delta$. So we get for $f_{N_{0}}$,
$$
\left\lvert   f(0) - f\left( N_{0} \frac{r}{N_{0}} \right)  \right\rvert= \lvert f(0) - f(r) \rvert   < \varepsilon  
$$
Here $r$ is arbitrary so we have that,
$$
\lvert f(0) - f(r)\rvert < \varepsilon \quad \forall r \in \mathbb{R}
$$
and since $\varepsilon$ is also arbitrary, we have $f(0) = f(r),\forall r\in \mathbb{R}$. Hence $f$ is a constant function. 

---

3. Let $f_n : [0, 1] \to \mathbb{R}$ be a sequence of continuous functions such that  

$$
|f_n(x)| \leq 1 \quad \forall x \in [0, 1], \ \forall n \in \mathbb{N}.
$$  

Define a sequence of functions $F_n : [0, 1] \to \mathbb{R}$ by  

$$
F_n(x) = \int_0^x f_n(t) \, dt \quad \forall n \in \mathbb{N}, \ x \in [0, 1].
$$  

Show that $\{ F_n \}$ has a subsequence that converges uniformly on $[0, 1]$.  

**Answer:**  We have that
$$
\lvert F_{n}(x) - F_{n}(y) \rvert  = |x-y|F'_{n}(c) = |x-y||f_{n}(c)| \leq |x-y| 
$$

We see that for any $\varepsilon>0$ we have $\delta = \varepsilon$ such that for $|x-y| < \delta$ we have $\lvert F_{n}(x) - F_{n}(y) \rvert| < \varepsilon$, for all $n \in \mathbb{N}$. Hence $\{ F_{n} \}$ is uniformly equicontinuous. Now,
$$
\lvert F_{n}  \rvert = \left\lvert  \int_{0}^{x}f_{n}(t) dt  \right\rvert \leq \int_{0}^{x} \lvert f_{n}(t) \rvert dt \leq \int_{0}^{x} 1 dt = x \leq  1
$$
Hence $\{ F_{n} \}$ is uniformly bounded, and  $[0,1]$ is compact. So by **Arzela-Ascoli theorem** we have that $\{ F_{n} \}$ has a convergent subsequence $\{ F_{n_{k}} \}$ which converges uniformly on $[0,1]$.

---

4. Let $f$ be a continuously differentiable function on $[a, b]$. Show that there is a sequence of polynomials $\{ P_n \}$ such that  

$$
P_n \to f \quad \text{uniformly}, \quad P_n' \to f' \quad \text{uniformly on } [a, b].
$$  

**Answer:** By **Weierstrass approximation theorem** we have that $\exists \{ P_{n} \}$ such that $P_{n} \to f$ uniformly. Now we have that $f'$ is continuous on $[a,b]$ so by **Weierstrass approximation theorem** again we have $\exists \{ Q_{n} \}$ such that $Q_{n} \to f'$ uniformly. Now define,
$$
R_{n}(x) = f(a) + \int_{a}^{x} Q_{n}(t) dt
$$
We see that since $Q_{n}(t) \to f'(t)$ uniformly implies,
$$
\lim_{ n \to \infty }\int_{a}^{x} Q_{n}(t) dt = \int_{a}^{x} f'(t) dt = f(x) - f(a)
$$  
Hence we have that $R_{n}(x)$ converges pointwise to $f(x)$. Also we have,
$$
R'_{n}(x) = Q_{n}(x) \to f'(x) \quad \text{uniformly}
$$
Now by the **Differentiable limit theorem** we have that $R_{n}$ converges uniformly to $f$.

---

5. Give an example (with justification) of a continuous function $f : \mathbb{R} \to \mathbb{R}$ which cannot be approximated by any sequence of polynomials on $\mathbb{R}$.  

**Answer:** Every non-constant polynomial is unbounded. Hence if we choose any non-constant bounded continuous function we have $N \in \mathbb{N}$ such that
$$
\begin{gather*}
\lvert \lvert P_{n}(x)  \rvert  - M \rvert \leq \lvert f(x) - P_{n}(x) \rvert  < 1 \\
\implies \lvert P_{n}(x) \rvert < M + 1
\end{gather*}

\quad \text{for } n \geq N
$$
Hence we have that $P_{n}$ is bounded for $n \geq N$, i.e. $P_{n}$ is constant for $n\geq N$. Hence it can only converge to a constant function. So any non-constant bounded continuous function cannot be approximated by polynomials on $\mathbb{R}$. For example, $f(x) = \sin x$ is a continuous bounded function which cannot be approximated by polynomials on $\mathbb{R}$.

---
 
# Part B
**Function Spaces**  
*(Some Additional Practice Problems)*

---

1. Give an example of an infinite family of non-constant functions that is equicontinuous at a point.  

**Answer:**  

---

2. Give an example of a metric space $X$ and an algebra in $C(X)$ that fails to separate points and also vanishes at some point.  

**Answer:**  

---

3. There are three main hypotheses of the Arzelà–Ascoli theorem, namely:  

(a) The domain of the functions in the sequence $\{ f_n \}$ is compact.  
(b) The sequence $\{ f_n \}$ is uniformly bounded.  
(c) The sequence $\{ f_n \}$ is uniformly equicontinuous.  

Show that the theorem is not true by giving a counter-example for each of the following cases:  

(i) (a) and (b) hold, but not (c).  

**Answer:**  

---

(ii) (b) and (c) hold, but not (a).  

**Answer:**  

---

(iii) (a) and (c) hold, but not (b).  

**Answer:**  

---
