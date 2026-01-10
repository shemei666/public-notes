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
Graph theory is the study of graphs, which are mathematical structures used to model pairwise relations between objects.

A **graph** $G = (V, E)$ consists of:
*   **Vertices:** A set $V = \{v_1, v_2, \dots, v_n\}$ representing the objects.
*   **Edges:** A set $E$ of pairs of vertices representing the connections between them.

### Definitions
*   **Degree:** The degree of a vertex $v$, denoted $d(v)$, is the number of edges incident to it.
*   **Walk:** A sequence of vertices and edges $v_0, e_1, v_1, e_2, \dots, e_k, v_k$ starting and ending at vertices.
*   **Trail:** A walk in which no edges are repeated.
*   **Path:** A walk in which no vertices (and consequently no edges) are repeated.
*   **Connectedness:** A graph is **connected** if there is a path between every pair of vertices. A graph that is not connected is called **disconnected**.
*   **Connected Component:** A maximal connected subgraph of a graph. Every graph can be uniquely partitioned into its connected components.

### Special Graphs
*   **Complete Graph ($K_n$):** A graph where every pair of distinct vertices is connected by a unique edge. It has $\binom{n}{2}$ edges.
*   **Bipartite Graph:** A graph whose vertices can be partitioned into two disjoint sets $U$ and $V$ such that every edge connects a vertex in $U$ to one in $V$. A **complete bipartite graph** $K_{m,n}$ contains all possible edges between the two sets.
*   **Tree:** A connected graph that contains no cycles. For a graph with $n$ vertices, being a tree is equivalent to being connected and having exactly $n-1$ edges.

## Adjacency Matrix
The **adjacency matrix** $A$ of a graph $G$ with $n$ vertices is an $n \times n$ matrix where the entry $a_{ij}$ is defined as:
$$a_{ij} = \begin{cases} 1 & \text{if there is an edge between } v_i \text{ and } v_j \\ 0 & \text{otherwise} \end{cases}$$

**Example:**
For a graph with vertices $V = \{v_1, v_2, v_3, v_4\}$ and edges $E = \{(v_1, v_2), (v_1, v_3), (v_2, v_3), (v_3, v_4)\}$, the adjacency matrix $A$ is:
$$A = \begin{pmatrix} 0 & 1 & 1 & 0 \\ 1 & 0 & 1 & 0 \\ 1 & 1 & 0 & 1 \\ 0 & 0 & 1 & 0 \end{pmatrix}$$


### Remarks
*   **Symmetry:** For an undirected graph, the adjacency matrix is symmetric ($A = A^T$).
*   **Vertex Degree:** The sum of the entries in the $i$-th row (or column) of $A$ is equal to the degree $d(v_i)$ of the vertex $v_i$.

### Powers of the Adjacency Matrix
**Theorem:** Let $A$ be the adjacency matrix of a graph $G$. The entry $(A^k)_{ij}$ is equal to the number of walks of length $k$ from vertex $v_i$ to vertex $v_j$.

**Corollary:** The number of triangles in a simple graph $G$ is given by:
$$\text{Number of triangles} = \frac{1}{6} \text{tr}(A^3)$$
where $\text{tr}(A^3)$ is the trace of $A^3$. This follows from the theorem for $k=3$, as $(A^3)_{ii}$ counts the number of walks of length 3 from $v_i$ to itself. In a simple graph, such a walk must be a triangle, and each triangle is counted 6 times (starting at each of the 3 vertices and traversing in 2 directions).

### Matchings
A **matching** $M$ in a graph $G = (V, E)$ is a subset of edges such that no two edges share a common vertex.

A **perfect matching** is a matching that covers all vertices of the graph. A matching $M$ is perfect if every vertex $v \in V$ is incident to exactly one edge in $M$. This implies that the total number of vertices $|V|$ must be even, and the matching contains exactly $|V|/2$ edges.

### Adjacency Matrix of Bipartite Graphs
If $G$ is a bipartite graph with vertex partitions $U$ and $V$ of sizes $m$ and $n$ respectively, its adjacency matrix $A$ can be expressed in block form by ordering the vertices of $U$ before $V$:
$$A = \begin{pmatrix} \mathbf{0}_{m \times m} & B \\ B^T & \mathbf{0}_{n \times n} \end{pmatrix}$$
where $B$ is an $m \times n$ matrix such that $b_{ij} = 1$ if there is an edge between $u_i \in U$ and $v_j \in V$, and $0$ otherwise.









## Polynomials

## Geometry
