---
title: Differential geometry and Lie groups
tags:
  - incomplete
created: 2025-08-04
draft: false
---

**Idea**: Differentiation on closed sets of $\mathbb{R}^{3}$ regular surfaces $S \subset \mathbb{R}^{3}$ can define smooth structure and any $f:S\to \mathbb{R}$ can be differentiated (meaningfully)

## Covariant derivative of vector field

**Def:** (Smooth vector field on S) $f:S\to \mathbb{R}^{3}$ is called a smooth vector field if $f(p)\in T_{p}(S) ,\forall p \in S$ and $f$ is a smooth function.
**Explanation**: $E \subseteq S \times \mathbb{R}^{3}$, $E = \{ (p,w) \mid w \in T_{p}(S) \}= \bigsqcup_{p \in S} T_{p}(S)$. So they make up a pair $(E, \pi, S)$ where $\pi(p,w) = p$. This is called the tangent bundle of $S$ and is denoted by $TS$. A smooth vector field is a smooth section of the tangent bundle, i.e. a smooth map $f:S\to E$ such that $\pi \circ f = id_{S}$.)

Given $\sigma:U \implies S$ patch around p, $f(p) = a(p)\sigma_{u}+b(p)\sigma_{v}$

Any smooth vector field f can be thought of as a function $f:S\to \mathbb{R}^{3}$ let $y \in T_{p}(S)$ let $\alpha:(-\varepsilon,\varepsilon)\to S$ be any curve such that $\alpha(0) = p$ and $\alpha'(0) = y$, $g(t)=f \circ \alpha(t)$. Then we define the covariant derivative of $f$ in the direction $y$ by

**Def:** $D_{y}f(p)$, the covariant derivative of $f$ along the vector $y$ is the projection of $\frac{dg(t)}{dt}|_{t=0}$ onto $T_{p}(S)$.

**Exercise:** 
1. $D_{y}f|_{p}$ depends only on y not on $\alpha$. (where $\alpha$ is a curve that fits $y$ at $p$), 
2. Also does not depend on the choice of $N$,
3. But not independent of $<,>$ on $\mathbb{R}^{3}$

**Solution:**

### Explicit formula for the covariant differentiation
$S \subseteq \mathbb{R}^{3}$ , $p \in S$ $\sigma:U\to  S$ patch around p. $y \in T_{p}(S)$, $w:S\to \mathbb{R}^{3}$ smooth vector field. We need to find $D_{y}w|_{p}$. Let $\alpha(t)= \sigma(u(t),v(t))$ with $\alpha'(0)=y$ and $w(t)=a(u(t),v(t))\sigma_{u}+b(u(t),v(t))\sigma_{v}$ then
$$
\begin{gather}
\frac{dw(t)}{dt} = a(\sigma_{uu}u' + \sigma_{uv}v') + b(\sigma_{vu}u' + \sigma_{uv} v') + a'\sigma_{u}+b'\sigma_{v} \\
=(a'+ \Gamma_{11}^{1}au' + \Gamma_{12}^{1}av' + \Gamma_{12}^{1}bu' +\Gamma_{22}^{1}bv')\sigma_{u} +  (b' + \Gamma_{11}^{2}au' + \Gamma_{12}^{2}av' +  \\
\Gamma_{12}^{2}bu' +\Gamma_{22}^{2}bv')\sigma_{v} + (aL+bM)N
\end{gather}
$$
$\implies D_{y}w = \frac{dw}{dt} - *N$ where $*=(aL+bM)$.

**Remark:**
1. If $S$ is a plane in $\mathbb{R}^{3}$ then $\sigma_{uu} = \sigma_{uv}= \sigma_{vu}=0$. $\implies D_{y}w = \frac{dw}{dt}|_{t=0}$ the directional derivative along $y$.
2. In the definition of $D_{y}w$, we do not need any information of $w(p)$ for $p\neq \alpha(t)$ $t \in (-\varepsilon,\varepsilon)$ where $\alpha$ is a curve fitting $y$ at $p$.

**Def:** Let $\alpha:I \to S$ be a curve $\alpha(0)=p,\alpha'(0)=y$ and $w$ is a vector field defined only on $\mathrm{Im}(\alpha)$ then $\frac{Dw}{dt}$ is the covariant derivative of $w(t)$ along $\alpha'(t)$ for all t.

**Remark:** If two surface meet tangentially along $\alpha$ then the covariant derivative of a field $w$ along $\alpha$ is same for both surfaces.

**Example:** $\alpha$ smooth curve on $S$ $w(t)=\alpha'(t)$ itself $Dw =$ tangential component of $\alpha''(t)$. Acceleration along the surface $\frac{D\alpha'}{dt}=$ acceleration seen from the surface.

**Def:** A vector field $w$ along a parametrized curve $\alpha:T \to S$ is said to be parallel if $\frac{Dw}{dt} = 0,\forall t$

**Proposition:** let $w,v$ be parallel vector field along $\alpha:I\to S$ then $<w(t),v(t)>$ = const.

**Proof:** $\frac{Dw(t)}{dt} = 0 \implies \frac{dw(t)}{dt}$ is in the normal direction: $\implies$ $<v(t),w'(t)> = <v'(t),w(t)> = 0$ implies $<v,w> =$ is const.

Existence and uniqueness of solution of differential equations implies that given $p \in S$ and $y,w_{0} \in T_{p}(S)$ there exists a unique parallel vector field $w(t)$ along $\alpha$ such that $w(0)=w_{0}$ and $\alpha'(0)=y$.
**Proposition:** $\alpha:I \to S$ parametrized curve in $S$. and $w_{0} \in T_{\alpha(t_{0})}(S)$ $t_{0} \in I$ then $\exists!$ parallel vector field $w$ along $\alpha$ such that
$$
w(t_{0}) = w_{0}
\frac{Dw}{dt}=0 ,\forall t
$$

# Post Midsem Material

![[Pasted image 20251022213834.png]]

![[Pasted image 20251022214130.png]]

![[Pasted image 20251023002054.png]]

![[Pasted image 20251023004033.png]]

![[Pasted image 20251023010840.png]]

![[Pasted image 20251023011320.png]]

![[Pasted image 20251028205253.png]]

![[Pasted image 20251028211040.png]]
![[Pasted image 20251028235607.png]]

![[Pasted image 20251028234910.png]]
> [!Proof:]-
> ![[Pasted image 20251028234937.png]]

![[Pasted image 20251028235908.png]]

![[Pasted image 20251029000043.png]]

![[Pasted image 20251029012309.png]]
> [!Proof:]-
> ![[Pasted image 20251029012331.png]]

![[Pasted image 20251029020007.png]]

![[Pasted image 20251029015947.png]]

![[Pasted image 20251031140113.png]]
> [!Proof:]-
> ![[Pasted image 20251031161521.png]]

![[Pasted image 20251031161824.png]]

![[Pasted image 20251031203201.png]]
> [!Proof:]-
> ![[Pasted image 20251031203217.png]]

![[Pasted image 20251031203329.png]]
> [!Proof:]-
> ![[Pasted image 20251031203345.png]]

![[Pasted image 20251031203357.png]]
> [!Proof:]-
> ![[Pasted image 20251031203408.png]]

![[Pasted image 20251101111407.png]]

![[Pasted image 20251101111434.png]]

![[Pasted image 20251101111451.png]]

![[Pasted image 20251101111459.png]]
> [!Proof:]-
> ![[Pasted image 20251101111514.png]]

![[Pasted image 20251101111526.png]]
> [!Proof:]-
> ![[Pasted image 20251101111539.png]]

![[Pasted image 20251101111549.png]]
> [!Proof:]-
> ![[Pasted image 20251101111559.png]]

![[Pasted image 20251115122151.png]]
![[Pasted image 20251115122225.png]]

![[Pasted image 20251115123657.png]]
 
![[Pasted image 20251115123710.png]]

![[Pasted image 20251115123748.png]]
![[Pasted image 20251115123801.png]]
![[Pasted image 20251115123820.png]]
## Existence Theorem

![[Pasted image 20251115123916.png]]

![[Pasted image 20251115124257.png]]

![[Pasted image 20251115124311.png]]

![[Pasted image 20251115124336.png]]

## Differentiation of Vector fields

![[Pasted image 20251115153500.png]]

![[Pasted image 20251115155954.png]]
![[Pasted image 20251115160004.png]]
![[Pasted image 20251115160011.png]]

# Class Notes
![[IMG_20251023_152530.jpg]]

![[IMG_20251023_154407.jpg]]

![[IMG_20251023_155441.jpg]]

![[IMG_20251027_113747.jpg]]![[IMG_20251027_114845.jpg]]
![[IMG_20251027_120618.jpg]]![[IMG_20251027_121619.jpg]]![[IMG_20251027_121624.jpg]]![[IMG_20251027_122029.jpg]]![[IMG_20251027_125640.jpg]]![[IMG_20251027_125643.jpg]]![[IMG_20251027_130537.jpg]]