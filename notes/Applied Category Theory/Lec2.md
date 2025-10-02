**Def:** A preorder is a relation (P,$\le$) such that
a) $x \le x$ (reflexive)
b) if $x \le y , y\le z \implies x\le z$ (transitive)

A preorder is a category with at most one morphism between objects
fancily a Bool-enriched category.

**Def:** Let A $\subseteq P$ then $p \in P$ is a meet($\wedge$) of A if
a) $\forall a \in A, p \leq a$
b) p is greatest lower bound $\forall q \in P$ such that $\forall a \in A, q \le a$ then $q \le p$

in a similar way we can also define join($\vee$)
### Examples:
1. Bool {T,F} T <-- F
see that the truth table for AND
	AND | T | F
	T       | T | F
	F       | F | F

 so AND is meet in Bool with the relation T $\le$ F
 similarly OR is join in Bool

2. Power sets (P(X),$\subseteq$)
so the meet here is just intersection and the join is union in this case
3.  Partitions, here a partition is less than another is there is a surjection of one to the other
4. $(\mathbb{N},|)$ here it will be GCD is the meet while LCM is the join
5. $(\mathbb{N},\le)$. min and max in this case

Remark: meets and joins need not always exists. for example if the set has no lower bound. It can also be because the second condition fail.

![[Pasted image 20250707051919.png]]

consider the set containing ${B,C}$ then both A and D are lower bounds but there is no greatest lower bound.

Also meet and join need not be unique see the case: A $\le$ B and B$\le$ A . Then A and B both are the meet and join of the set $\{A,B\}$.

**Proposition:** Suppose $(P,\le)$ is a preorder and $A \subseteq B \subseteq P$ are subsets that have meets. Then $\bigwedge B \leq \bigwedge A$ and if A and B have joins then $\bigvee A \leq \bigvee B$

**Proof:** Clearly $\bigwedge B$ is a lower bound for A, since A is a subset of B. Now from the fact that A has a meet we have  $\bigwedge B \leq \bigwedge A$


### Monotone maps
**Def:** A monotone map f :(P,$\le$) $\to$ (Q, $\le$)  such that 
if $p \le p'$ in P then $f(p) \le_{Q} f(p')$ 

for example for finite set X, X $\to$ |X|

**Contagion**: $\phi:$Part({M,C,F,K}) $\to$ Bool, map to True based on if C,F connected
![[Pasted image 20250707054015.png]]

**Def**: a monotone map f:P$\to Q$ preserves joins if $\forall A \subseteq P, f(\bigvee a) = \bigvee f(a)$
**Def:** similarly f preserves meets if $f(\bigwedge  a) = \bigwedge$

**Def:** We say a monotone map $f:P \to Q$ has generative effect if there exists elements $a,b \in P$ such that 
$$
f(a) \vee f(b) \neq f(a \vee b)
$$
The reason for this naming is that  if we consider the map f to be an observation or measurement of the system we see that observing the systems a and b separately does not give us the value when observing the combined system.

if a and b have a join and their image under a monotone map f also has a join then
$$
a \leq a \vee b \quad b \leq a \vee b \implies f(a) \vee f(b) \leq f(a \vee b)
$$


now is $\phi$ a join preserving map? see that $\phi (DAY) \vee \phi(NIGHT) = F$ while $\phi( DAY \vee NIGHT) = T$

### Galois connection
**Def:** Galois connection is a pair of preorders
  ![[Pasted image 20250707060127.png]]
  
f,g monotone maps such that $f(p) \le q$ iff $p \le g(q)$
f is called the left adjoint and g is the right adjoint.

**Examples**:
1. f: $x \to 3x$  $\mathbb{Z}\to \mathbb{R}$
g : $y \to \left\lfloor  \frac{y}{3}   \right\rfloor$ $\mathbb{R} \to \mathbb{Z}$

2. there exists and for all f:X -> Y 
![[Drawing 2025-07-07 13.09.40.excalidraw]]
there is an obvious map that takes subset of Y to subset of X i.e.  $f^*(B) = f^{-1}(B)$ 

Now $f_{!}(A) = \{y \in Y| \exists a,  f(a) = y\}$. Which is just the direct image of A
and $f_{*} = \{y \in Y| \forall a \in X \ s.t \ f(a)=y, a \in A\}$

![[Drawing 2025-07-07 13.25.29.excalidraw]]

Given any function g: S-> T we can show that it induces a Galois connection $g_{!}$: Prt(S) $\leftrightarrows$ Prt(T): $g^{*}$. Where Prt is the partition of the set.
The first image below describes $g_{!}$ and the other $g^{*}$
![[Pasted image 20250707211048.png]]
![[Pasted image 20250707211104.png]]

**Exercise:** Prove the validity of the claim that the above maps are left and right adjoints.

**Ideas/Hints:**
![[Pasted image 20250707211525.png]]
**Solution:** #todo

### Basic theory of Galois connections
**Proposition:** Suppose that $f:P \to Q$ and $g:Q \to P$ are monotone maps. 
TFAE:
1. f and g form a Galois connection where f is left adjoint to g.
2. for every $p \in P$ and $q \in Q$ we have
$$
p \leq g(f(p)) \quad \text{and} \quad f(g(q)) \leq q
$$

**Proof:**
$\implies$ 
$$
f(p) \leq f(p) \implies p \leq g(f(p))
$$
similarly for the other.
$\impliedby$
Given that $f(p) \leq  q$ . We have, $p \leq g(f(p)) \leq g(q)$ . Similarly for the other direction, $p \leq g(q) \implies f(p) \leq f(g(q))\leq  q \quad \blacksquare$

**Exercise:**  ![[Pasted image 20250707221539.png]]

**Ideas/Hints:**

**Solution:**
1. $$
f(g'(q)) \leq q \implies g'(q) \leq g(f(g'(q))) \leq g(q)
$$
We get the above from the equivalent definition given above.
Similarly we also get that $g(q) \leq  g'(q)$. Hence $g(q) \cong g'(q)$ for all q.
2. ![[Drawing 2025-07-07 23.56.29.excalidraw]]
See that there are 2 possible left adjoints for h.

**Proposition:**(Right adjoints preserve meets) Let $f :P \to Q$ be left adjoint to $g:Q \to P$. Suppose $A \subseteq Q$ any subset. Then if A has a meet then $g(A)$ has a meet in P.
$$
g(\bigwedge A) \cong \bigwedge g(A)
$$
i.e. right adjoints preserve meets. Similarly left adjoints preserve joins. if $A \subseteq P$ has a join then $f(A)$ also has a join in Q.
$$
f(\bigvee A) \cong \bigvee f(A)
$$
**Proof:**











**Theorem:**(Adjoint functor theorem for preorders) A monotone map f is a left adjoint iff it preserves joins and a right adjoint if it preserves meets.

**Proof:**

### Applications:




