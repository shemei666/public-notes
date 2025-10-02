# Databases and data transformation

Data kinematics: how data rests and how it moves(databases and data transformations)
#### Database:
![[Pasted image 20250709001731.png]]
(Presents a category)

**Def:** A category $\mathscr{C}$ consists of:
1. A set Ob($\mathscr{C}$) of objects
2. For every $c_{1},c_{2} \in Ob(\mathscr{C})$ a set $Hom_{\mathscr{C}}(c_{1},c_{2})= \mathscr{C}(c_{1},c_{2})$
3. For every object $c \in Ob(\mathscr{C})$ there exists $id_{c} \in \mathscr{C}(c,c)$
4. For every $c_{1},c_{2},c_{3}$ a function $\circ:\mathscr{C}(c_{1},c_{2}) \times \mathscr{C}(c_{2},c_{4}) \to \mathscr{C}(c_{1},c_{4})$
Satisfying
A. for all $c_{1},c_{2} \quad id_{c_{1}} \circ f = f = f \circ id_{c_{2}}$ 
B.  $f\circ(g\circ h) = (f \circ g) \circ h$

### **Examples**:
1. Each poset is a category
2. Free categories
![[Drawing 2025-07-09 00.45.16.excalidraw]]
By convention we don't draw the identity maps in Hasse diagrams.

**Set**: the category of sets
Ob(Set) = all sets (class of all sets)
$S_{1},S_{2} \in  Ob(\mathbf{Set})$
The morphisms are the set maps between $S_{1},S_{2}$ and the identity is the usual identity function and the composition is the usual composition.

**Vect**: the category of vector spaces
the objects are vector spaces and the morphisms are the linear maps

**Cat**: the category of categories. The morphism are functors.

## Functors

**Def:** $\mathscr{C},\mathscr{D}$ categories. A functor $F:\mathscr{C} \to \mathscr{D}$ is
1. a function $F:Ob(\mathscr{C}) \to Ob(\mathscr{D})$
2. for all objects $X,Y \in  \mathscr{C}$ a function $\mathscr{C}(X,Y) \to \mathscr{D}(FX,FY)$
such that
(a) $F(id_{X}) = id_{FX}$ (preserves identity)
(b) $Ff\circ Fg = F(f\circ g)$ (preserves composition) 

**Examples**:
![[Pasted image 20250709012243.png]]

#### Monotone maps
Suppose $\mathscr{C}= (C,\leq)$  $\mathscr{D}= (D,\leq)$ are preorders
i) $F : \mathscr{C} \to \mathscr{D}$
ii) if $X\leq Y$ then $FX = FY$
so functor are just monotone maps

#### Monoid homomorphisms
Suppose $(\mathscr{C},\times )$ $(\mathscr{D},\times )$  are monoids
i) C and D are one object sets
ii) $F:\mathscr{C} \to \mathscr{D}$
such that
a) $F 1_{\mathscr{C}} = 1_{\mathscr{D}}$
b)$F(f\times g) = Ff \times Fg$

#### Database Instances
![[Drawing 2025-07-09 01.43.24.excalidraw]]
![[Pasted image 20250709014727.png]]

**Algebraic Topology**
We have the categories **Top** and the functor
$$
\mathbf{Top} \xrightarrow{\pi_{1}} \mathbf{Grp}
$$
## Naturality
**Def:** Let $\mathscr{C} \xrightarrow{F,G} \mathscr{D}$  be functors
A _natural transformation_  $\alpha$ is 
for each $X \in \mathscr{C}$ a morphism $\alpha_{X}:FX \to GX$
such that
$\forall f:X \to Y$
![[Drawing 2025-07-09 02.13.05.excalidraw]]

**Example**:
(a) ![[Drawing 2025-07-09 02.21.32.excalidraw]]
then $\alpha: X \to Y$ is just a morphism in $\mathscr{C}$ since 1 only has one element and an identity morphism
**Def:** Given categories $\mathscr{C,D}$
there is a category $[\mathscr{C,D}]$
-objects: functors $F:\mathscr{C\to D}$
-morphisms: natural transformation. 

Given a database schema $\mathscr{C}$, we say $[\mathscr{C,\text{Set}}]$ is the category of $\mathscr{C}$-instances

## Universality

**Def:** An adjunction is pair of functors
![[Pasted image 20250709025614.png]]
such that
$$
\mathscr{D}(FX,Y) \cong \mathscr{C}(X,GY)
$$
in a natural way

**Fact**:
![[Pasted image 20250709030326.png]]
