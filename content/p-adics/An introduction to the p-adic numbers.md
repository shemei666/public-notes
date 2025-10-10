Paper by **Alexa Pomerantz**

**Def:** An absolute value on a field $K$ is a function $|\cdot|: K \to \mathbb{R}_{\geq 0}$ such that for all $x,y \in K$:
1. $|x| = 0$ if and only if $x = 0$
2. $|xy| = |x||y|$
3. $|x+y| \leq |x| + |y|$ (triangle inequality)
Moreover we say that $|\cdot|$ is non-Archimedean if it satisfies the stronger ultrametric inequality:
4. $|x+y| \leq \max(|x|, |y|)$

A set on which a metric is defined is a metric space. A set with a metric induced by a non-Archimedean absolute value is an ultrametric space.

**Lemma:** Let $\mathbb{K}$ be an ultrametric space, and let $x,y \in \mathbb{K}$. If $|x| \neq |y|$, then $|x+y| = \max(|x|, |y|)$.

**Proof:** Without loss of generality, assume $|x| > |y|$. Then by the ultrametric inequality, we have:
$$|x+y| \leq \max(|x|, |y|) = |x|.$$
On the other hand, we also have:
$$|x| = |(x+y) - y| \leq \max(|x+y|, |y|).$$
Since $|x| > |y|$, it follows that $|x| \leq |x+y|$. Combining these two inequalities, we get:
$$|x+y| \leq |x| \leq |x+y|,$$
which implies $|x+y| = |x| = \max(|x|, |y|)$. $\quad \blacksquare$

**Def:** The p-adic valuation on $\mathbb{Q}$ is defined by a function $v_{p}:\mathbb{Q} \to \mathbb{Z} \cup \{ \infty \}$. Let $x \in \mathbb{Q}$ where $x \neq 0$. We can write $x$ as $x = p^{k} \frac{a}{b}$ where $a,b \in \mathbb{Z}$ are not divisible by the prime $p$. Then we define $v_{p}(x) = k$. If $x = 0$, we define $v_{p}(0) = \infty$.

**Lemma:** The following properties holds for all $x,y \in \mathbb{Q}$:
1. $v_{p}(xy) = v_{p}(x) +v_{p}(y)$
2. $v_{p}(x+y) \geq \min(v_{p}(x), v_{p}(y))$ with equality if $v_{p}(x) \neq v_{p}(y)$

**Def:** Let the p-adic absolute value function $|\cdot|_{p}:\mathbb{Q} \to \mathbb{R}_{\geq 0}$ be defined as follows:
$$
|x|_{p} = \begin{cases}
p^{-v_{p}(x)} & x \neq 0 \\
0 & x = 0
\end{cases}
$$
**Lemma:** The p-adic absolute value is a non-Archimedean absolute value on $\mathbb{Q}$.

**Theorem:** (Ostrowski's Theorem) Every nontrivial absolute value on $\mathbb{Q}$ is equivalent to either the usual absolute value or a p-adic absolute value for some prime $p$.

## Construction of $\mathbb{Q}_{p}$ and $\mathbb{Z}_{p}$
**Theorem:** Let $\mathbb{K}$ be a field with an absolute value $|\cdot |$. Then there exists a complete field $\hat{\mathbb{K}}$ containing $\mathbb{K}$ such that the absolute value on $\mathbb{K}$ extends to an absolute value on $\hat{\mathbb{K}}$. Moreover, this completion is unique up to isomorphism.

**Def:** The field $\mathbb{Q}_{p}$ is the completion of $\mathbb{Q}$ with respect to the p-adic absolute value $|\cdot|_{p}$.

**Def:** Let the ring of p-adic integers $\mathbb{Z}_{p}$ be defined as:
$$\mathbb{Z}_{p} = \{ x \in \mathbb{Q}_{p} : |x|_{p} \leq 1 \}.$$
**Remark**: We note that for all $x \in \mathbb{Z},v_{p}(x)\geq 0 \implies |x|_{p}\leq 1$. Thus $\mathbb{Z} \subset \mathbb{Z}_{p}$.

## Sequences and series in $\mathbb{Q}_{p}$

There are some nice results in p-adic metrics that are not true in the real space.

**Theorem:** Let $(a_{n})$ be a sequence in $\mathbb{Q}_{p}$. Then $(a_{n})$ is Cauchy iff for every $\varepsilon>0$, there exists an $N$ such that for all $n \geq  N$, $|a_{n+1}-a_{n}|_{p} < \varepsilon$.
**Proof:** $(\implies )$
Suppose $(a_{n})$ is Cauchy. Then for every $\varepsilon > 0$, there exists an $N$ such that for all $m,n \geq N$, $|a_{n}-a_{m}|_{p} < \varepsilon$. In particular, for $m = n+1$, we have $|a_{n+1}-a_{n}|_{p} < \varepsilon$ for all $n \geq N$.

$(\impliedby )$ Suppose that for every $\varepsilon > 0$, there exists an $N$ such that for all $n \geq N$, $|a_{n+1}-a_{n}|_{p} < \varepsilon$. We want to show that $(a_{n})$ is Cauchy. Let $\varepsilon > 0$ be given. Choose $N$ such that for all $n \geq N$, $|a_{n+1}-a_{n}|_{p} < \varepsilon$. Then for any $m,n \geq N$ with $m > n$, we have:
$$|a_{m}-a_{n}|_{p} = |(a_{m}-a_{m-1}) + (a_{m-1}-a_{m-2}) + \ldots + (a_{n+1}-a_{n})|_{p}.$$
By the ultrametric inequality, we have:
$$|a_{m}-a_{n}|_{p} \leq \max(|a_{m}-a_{m-1}|_{p}, |a_{m-1}-a_{m-2}|_{p}, \ldots, |a_{n+1}-a_{n}|_{p}).$$
Since each term on the right-hand side is less than $\varepsilon$, we have $|a_{m}-a_{n}|_{p} < \varepsilon$. Thus, $(a_{n})$ is Cauchy. $\quad \blacksquare$

**Corollary:** Let $(a_{n})$ be a sequence in $\mathbb{Q}_{p}$. Then $\sum_{n=0}^{\infty}$ converges iff $\lim_{n \to \infty} a_{n} = 0$.

**Proof:** ($\implies$) Suppose $\sum_{n=0}^{\infty} a_{n}$ converges in $\mathbb{Q}_{p}$, i.e. sequence of partial sums $S_{N} = \sum_{n=0}^{N} a_{n}$ converges. Therefore, for every $\varepsilon > 0$, there exists an $N$ such that for all $m,n \geq N$, we have:
$$|S_{m} - S_{n}|_{p} < \varepsilon.$$
In particular, for $m = n+1$, we have:
$$|S_{n+1} - S_{n}|_{p} = |a_{n+1}|_{p} < \varepsilon.$$
This shows that $\lim_{n \to \infty} a_{n} = 0$.

$(\impliedby )$ Given that $\lim_{ n \to \infty } a_{n} = 0$. We have $N \in N$ such that $|a_{n}|_{p} < \varepsilon$ for all $n\geq N$. Then also $|a_{n+1}|_{p} <\varepsilon$. Hence 
$$
|S_{n+1}-S_{n}|_{p} = |a_{n+1}|_{p} < \varepsilon 
$$
So the sum converges. $\quad \blacksquare$

**Remark:** This is very different from the real case, where a series can have terms that go to zero but still diverge (e.g. the harmonic series).

## p-adic Expansions

There are some counterintuitive results such as $-1 = 1 + 2 + 4+\dots$ in $\mathbb{Q}_{2}$. We can try to make sense of this by looking at p-adic expansions.

**Proposition:** Any series in the form $\sum_{n=n_{0}}^{\infty}a_{n}p^{n}$, with $a_{n} \in \{ 0,1,\dots,p-1 \}$ and $n_{0} \in \mathbb{Z}$ converges in $\mathbb{Q}_{p}$. 

**Proof:** We know that $\lim_{ n \to \infty } p^{n} = 0$. We suppose that $0\leq a_{n}<p$ for all $n\geq n_{0}$. Hence it also follows that $\lim_{ n \to \infty } a_{n}p^{n} = 0$ as well so the sum converges. $\quad \blacksquare$

**Def:** The p-adic expansion of a number $x \in \mathbb{Q}_{p}$ is a series of the form $\sum_{n=n_{0}}^{\infty}a_{n}p^{n}$, where $a_{n} \in \{ 0,1,\dots,p-1 \}$ and $n_{0} \in \mathbb{Z}$ such that $x = \sum_{n=n_{0}}^{\infty}a_{n}p^{n}$.

**Theorem:** Every $x \in \mathbb{Q}_{p}$ has a unique p-adic expansion.

**Exercise:** Let $\alpha \in \mathbb{Q}$ and let $\sum_{n=n_{0}}^\infty a_{n}p^{n}$ be the p-adic expansion of $\alpha$. Show that $v_{p}(\alpha) = n_{0}$. 

**Solution:** Since $\alpha \in \mathbb{Q}$, we can write $\alpha$ as $\alpha = p^{k} \frac{a}{b}$ where $a,b \in \mathbb{Z}$ are not divisible by the prime $p$. Then we define $v_{p}(\alpha) = k$. We know that the p-adic expansion of $\alpha$ is given by $\sum_{n=n_{0}}^{\infty}a_{n}p^{n}$, where $a_{n} \in \{ 0,1,\dots,p-1 \}$ and $n_{0} \in \mathbb{Z}$. We can factor out $p^{n_{0}}$ from the series:
$$\alpha = p^{n_{0}} \sum_{n=0}^{\infty} a_{n+n_{0}} p^{n}.$$
Since $a_{n+n_{0}} \in \{ 0,1,\dots,p-1 \}$, the series $\sum_{n=0}^{\infty} a_{n+n_{0}} p^{n}$ converges to a p-adic integer, which is not divisible by $p$. Hence $v_{p}(\alpha) = n_{0}$. $\quad \blacksquare$

To make computation of p-adic expansions we can use,

**Lemma:** Let $\alpha \in \mathbb{Z}_{p}$ with p-adic expansion $\sum_{n=n_{0}}^{\infty}$, and let $k \in \mathbb{N}$. Then $\alpha \equiv \sum_{n=n_{0}}^{k} a_{n}p^{n} (\mod p^{k+1})$. 

**Theorem:** A p-adic number has an eventually periodic p-adic expansion iff it is rational.

## The topology on $\mathbb{Q}_{p}$

**Theorem:** In $\mathbb{Q}_{p}$ any open ball is also closed ball.(and vice versa)
**Corollary:** The ring $\mathbb{Z}_{p}$ is both closed and open in $\mathbb{Q}_{p}$.
**Corollary:** $\mathbb{Q}_{p}$ is totally disconnected.
**Theorem:** The ring $\mathbb{Z}_{p}$ is compact.
#todo 