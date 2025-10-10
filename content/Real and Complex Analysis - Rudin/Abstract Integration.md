A collection $\mathscr{M}$ of subsets of a set X is said to be $\sigma$-algebra in X if $\mathscr{M}$ has the following properties

i) $X \in \mathscr{M}$
ii) If $A \in \mathscr{M}$ then $A^c \in \mathscr{M}$ 
iii) If A = $\bigcup_{n=1} ^\infty A_{n}$ and if $A_{n} \in \mathscr{M}$ then $A \in \mathscr{M}$

If $\mathscr{M}$ is a sigma algebra in X, then X is called a measurable space and $\mathscr{M}$ is the measurable sets in X

If X is a measurable space, Y is a topological space and f is a mapping of X into Y, then f is said to be measurable provided that $f^{-1}(V)$ is a measurable set in X for every open set V in Y.

#### Some comments
a) since $\varnothing = X^c \implies \varnothing \in \mathscr{M}$
b) we can now get the finite version of iii using a.
c) also by using complement we also get 
$$
\bigcap_{n=1}^\infty  A_{n} \in \mathscr{M}
$$
d) $A-B \in \mathscr{M}$ if A and B in $\mathscr{M}$


**Theorem**: Let Y and Z be topological spaces, and let $g:Y\to Z$ be continuous 
b) if X is measurable space, if $f:X\to Y$ and $h = g \circ f$, then $h:X \to Z$ is measurable.

proof: $h^{-1}(V) =f^{-1}(g^{-1}(V))$
$g^{-1}$ is continuous hence $g^{-1}(V)$ is open given V is open. and since f is measurable $h^{-1}(V)$ is a measurable set.

**Theorem:** Let u and v be real measurable fns on a measurable space X, let $\Phi$ be a continuous mapping of the plane into a topological space Y, and define
$$
h(x) = \Phi(u(x),v(x))
$$
for x $\in X$ Then $h:X\to Y$ is measurable
**Proof:**  Let f(x) = (u(x),v(x)) , Then f maps X to the plane. h = $\Phi \circ f$ . $\Phi$ is continuous so only need to check whether $f$ is measurable.
If R is an open rectangle
$$
f^{-1}(R) = u^{-1}(I_{1}) \cap v^{-1}(I_{2})
$$
where $I_1,I_2$ are open intervals. Hence we have that f is measurable since open intervals make up a basis for the plane.$\quad \blacksquare$

**Theorem:** Let X be a measurable space.
a) If f = u + iv where u,v are measurable then f is measurable.
b) If f = u+iv is a complex measurable function on X, then u,v and |f| are real measurable fns on X
c) If f,g are measurable then so are f+g and fg
d) If E is a measurable set in X and 
$$
\chi_{E}(x) = 
\begin{cases}
1 & \text{if} \quad x \in E \\
0 & \text{if} \quad x \not\in E 
\end{cases}
$$
then $\chi$ is a measurable function
e) If f is a complex measurable function on X, there is a complex measurable function $\alpha$ on  X such that $|\alpha| = 1$ and $f = \alpha|f|$ 
**Proof:**
a) 






