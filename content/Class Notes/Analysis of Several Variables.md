---
publish: true
---

# Analysis of Several Variables

## Euclidean Inner Product and Norm

**Def (Euclidean Inner Product):** 
The Euclidean inner product on $\mathbb{R}^n$ is a map
$$ \langle \cdot, \cdot \rangle : \mathbb{R}^n \times \mathbb{R}^n \longrightarrow \mathbb{R} $$
defined for $x = (x_1, \dots, x_n)$ and $y = (y_1, \dots, y_n)$ by
$$ (x, y) \mapsto \langle x, y \rangle = \sum_{i=1}^n x_i y_i $$

### Properties

- **Bilinearity & Positive Definiteness**:
  - $\langle x + u, y \rangle = \langle x, y \rangle + \langle u, y \rangle \quad \forall x, y, u \in \mathbb{R}^n$
  - $\langle x, \lambda y \rangle = \lambda \langle x, y \rangle \quad \forall \lambda \in \mathbb{R}$
  - $\langle x, x \rangle \geq 0 \quad \forall x \in \mathbb{R}^n \quad \text{and} \quad \langle x, x \rangle = 0 \iff x = 0$

- **Induced Norm Structure**:
  When given an inner product on $\mathbb{R}^n$, we can define a norm structure on $\mathbb{R}^n$:
  $$ \|\cdot\| : \mathbb{R}^n \longrightarrow \mathbb{R}_{\geq 0}, \quad \|x\| = \sqrt{\langle x, x \rangle} $$
  *(The norm obtained from the Euclidean inner product is called the **Euclidean norm**).*
