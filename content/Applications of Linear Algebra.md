## Introduction
A **vector space** $V$ over a field $F$ (e.g., $\mathbb{R}, \mathbb{C}, \mathbb{Q}$) is a set of vectors satisfying given axioms under addition and scalar multiplication:
1. **Addition:** Must be associative, commutative, have an identity ($\mathbf{0}$), and have inverses ($-\mathbf{v}$).
2. **Scalar Multiplication:** Defines how a scalar $c \in F$ scales a vector $\mathbf{v} \in V$. It must satisfy:
    * **Identity:** $1\mathbf{v} = \mathbf{v}$ for the multiplicative identity $1 \in F$.
    * **Compatibility:** $a(b\mathbf{v}) = (ab)\mathbf{v}$ for all $a, b \in F$.
    * **Distributivity over Vector Addition:** $a(\mathbf{u} + \mathbf{v}) = a\mathbf{u} + a\mathbf{v}$.
    * **Distributivity over Scalar Addition:** $(a + b)\mathbf{v} = a\mathbf{v} + b\mathbf{v}$.

**Examples:**
* **Polynomials:** $\mathbb{R}[x]$, the set of polynomials over $\mathbb{R}$
* **Matrices:** $M_{m \times n}(F)$, the set of all $m \times n$ matrices.
* **Function Spaces:** $C[a, b]$, the set of continuous real-valued functions on an interval.

### Basis and Dimension
A **basis** $\mathcal{B} = \{\mathbf{v}_1, \dots, \mathbf{v}_n\}$ for $V$ is a set that is:
1. **Linearly Independent:** $\sum c_i \mathbf{v}_i = \mathbf{0} \implies c_i = 0$ for all $i$.
2. **Spanning:** Every $\mathbf{v} \in V$ is a linear combination of $\mathcal{B}$.

Size of the basis is called **dimension** of $V$.


### Eigenvalues and Eigenvectors
For a square matrix $A \in M_{n \times n}(F)$, a non-zero vector $\mathbf{v}$ is an **eigenvector** if:
$$A\mathbf{v} = \lambda\mathbf{v}$$
where $\lambda \in F$ is the corresponding **eigenvalue**.

This is equivalent to $(A - \lambda I)\mathbf{v} = \mathbf{0}$. For a non-zero solution to exist, the matrix $(A - \lambda I)$ must be singular, leading to the **characteristic equation**:
$$\det(A - \lambda I) = 0$$
where $I$ is the $n \times n$ identity matrix. The determinant yields a polynomial $p(\lambda)$ of degree $n$, whose roots are the eigenvalues of $A$.



## Graph theory



## Polynomials

## Geometry
