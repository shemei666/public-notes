---
title: Differential geometry and Lie groups
tags:
  - incomplete
created: 2025-08-04
draft: false
---


**Def:** $S \subset \mathbb{R}^{3}$ is called a surface if $\forall p \in S, \exists W_{p} \subset \mathbb{R}^{3}$ open such that $\exists$ a homeomorphism $\sigma_{U} \to W \cap S \subset \mathbb{R}^{3}$
$\mathscr{A} = \{ W_{p} \cap S | W_{p},S \quad \text{as above} \}$ is called atlas.

S is called _regular_ if $\sigma$ is also differentiable and $\nabla_{x}: \mathbb{R}^{2} \to \mathbb{R}^{3}$ $\nabla  \sigma$ has rank 2 at each patch in an atlas.


Transition functions:
![[SVG/tikz1755255125.7149007.svg|diagram]]
remark: goes through the intersection.

**Theorem:** In a regular atlas, all transition fns are smooth.

**Proof:** Since $\nabla \sigma_{U}$ has rank 2, exists a 2x2 minor of it that is non zero. 
$$
\sigma_{v}^{-1} \circ \sigma_{U} = (\sigma_{V}^{-1} \circ p_{12}^{-1}) \circ (p_{12} \circ \sigma_{U})
$$
#### Equivalence relation on atlases
$\mathscr{A_{1},A_{2}}$ be 2 regular atlases on S. $\mathscr{A_{1} \sim A_{2}}$ iff $\forall (U,\sigma_{U})$ in $\mathscr{A_{1}}$. $\forall (V,\tau _{V})$ in$\mathscr{A_{2}}$ 
if $\sigma_{U}(U) \cap \tau_{V}(V) \neq \varnothing$


**Def:** f: S1 -> S2 be a continuous map we say f is smooth iff $\sigma_{2}^{-1}\circ f \circ \sigma_{1}$ is smooth for all regular patches




