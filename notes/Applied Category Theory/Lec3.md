### Resource theories
Motivation: Can I make what I want from what I have?

Monoidal categories. enriched categories
**Def:** Monoidal set (monoid) is a semi-group with identity, i.e. a group without restriction of inverses.

Similarly,
**Def:** Monoidal poset consists of :
1. M is a poset
2. $*:M\times M \to M$ is a monotone function.
3. there is an element e in M
where \* is associative, has identity e.

Remark: the order on $M\times M$ is $(m_{1},m_{2}) \leq (m_{3},m_{4})$ iff $m_{1}\leq m_{3} \ \text{and} \ m_{2} \leq m_{4}$ .

### Examples:
1. $(\mathbb{N},\leq,+,0)$
2. $(\mathbb{N},\leq,max,0)$
3. (non-example) $(\mathbb{R},\leq,\times,1)$

There are also monoidal spaces etc...

### Wiring Diagrams/ String Diagrams
*"Involving the human visual cortex"*
![[Pasted image 20250708180651.png]]

![[wire diagram 1.excalidraw]]

We can add,
**Discard Axiom**: $\forall a \in M, a \leq e$
**Copy Axiom**: $\forall a \in M,\ a\leq a*a$
We can use this axiom to discard objects in the wire diagrams. But convention we can discard elements.

$(\mathbb{N} \cup \{ \infty  \}, \leq, \infty, min)$ is a monoidal poset.
This has the discard axiom since $a \leq \infty$  for all a and the copy axiom since $a \leq min(a,a)$ for all a

Remark: A poset is a preorder that obeys $x\leq y,y\leq x \implies x=y$
Fact: every preorder is equivalent to a poset

### Symmetric monoidal preorder

**Def:** A monoidal preorder $(P,\leq,e,\otimes )$ is:
1. a preorder $(P,\leq )$
2. a function $\otimes:P\times P \to P$
such that:
$\otimes$ is associative and has e as the identity and is monotone.

**Example**:
1. Bool = $(\{ T,F \},\implies,T,\wedge )$
2. Cost = $([0,\infty ],\geq,0,+)$
3. P(X) = $(P(X),\subseteq,X,\cap )$

#### Wiring diagrams:
$(P,\leq,e,\otimes )$
elements of P are the wires
$\leq$ is the box
and e is conventionally avoided
parallel lines joining the box is $\otimes$

**Def:** A monoidal preorder is symmetric if it obeys:
$$
a \otimes b \leq b \otimes a \quad \text{(symmetry)}
$$
### (Enriched) Categories:
Idea: monoidal preorder structure the question of getting from A to B.
Possible ? Bool
At what cost?  Cost
How?  P(X)

**Def:** Let V = $(P,\leq,e,\otimes )$ be a SMP.
A V-category is
1. a set X
2. a function $X\times X \xrightarrow{\mathscr{C}} P$
such that
 a) $e \leq \mathscr{C}(x,x) \quad \forall x \in X$
 b) $\mathscr{C}(x,y)\otimes \mathscr{C}(y,z) \leq \mathscr{C}(x,z) \quad \forall x,y,z \in X$

Q. what do (a),(b) say when V = Bool
 $T \implies \mathscr{C}(x,x)$ i.e. $\mathscr{C}(x,x) = T \quad \forall x$
$\mathscr{C}(x,y) \wedge \mathscr{C}(y,z) \implies \mathscr{C}(x,z)$  i.e. $\mathscr{C}(x,y)$ and $\mathscr{C}(y,z)$ are true then $\mathscr{C}(x,z)$ is also true.

Now thinking of $\mathscr{C}$ as defining a relation we get the same structure as a preorder. So Preorders are Bool-category.

A cost-category is a
 1. set X
 2. a function $X\times X \to [0,\infty]$
such that
a) $0 \geq d(x,x)$
b) $d(x,y) + d(y,z) \geq d(x,z)$

This is called a Lowvere metric space.

