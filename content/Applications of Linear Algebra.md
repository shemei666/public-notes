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


**Theorem:** For a bipartite graph $G$ with partitions $U$ and $V$ of equal size $n$, $G$ has a perfect matching if and only if $\det(B)$ is not zero.

**Lemma (Leibniz Formula):** 
$$\det(B) = \sum_{\sigma \in S_n} \text{sgn}(\sigma) \prod_{i=1}^n b_{i, \sigma(i)}$$
where $S_n$ is the symmetric group of all permutations of the set $\{1, 2, \dots, n\}$, and $\text{sgn}(\sigma)$ denotes the sign of the permutation $\sigma$ ($+1$ for even and $-1$ for odd permutations).
**Proof of Lemma:**
By the multilinearity of the determinant with respect to its rows, we can expand $\det(B)$ as:
$$\det(B) = \det\left(\sum_{j_1=1}^n b_{1,j_1} \mathbf{e}_{j_1}, \dots, \sum_{j_n=1}^n b_{n,j_n} \mathbf{e}_{j_n}\right) = \sum_{j_1, \dots, j_n} \left( \prod_{i=1}^n b_{i,j_i} \right) \det(\mathbf{e}_{j_1}, \dots, \mathbf{e}_{j_n})$$


### Incidence Matrix
For a graph $G = (V, E)$ with $n$ vertices and $m$ edges, the **incidence matrix** $M$ is an $n \times m$ matrix.

For an **undirected graph**, the entries $m_{ij}$ are defined as:
$$m_{ij} = \begin{cases} 1 & \text{if vertex } v_i \text{ is incident to edge } e_j \\ 0 & \text{otherwise} \end{cases}$$

**Properties:**
1. The sum of the entries in each column is exactly 2.
2. The sum of the entries in the $i$-th row is equal to the degree $d(v_i)$ of vertex $v_i$.


**Lemma:** For a connected graph $G$ with $n$ vertices, the rank of the oriented incidence matrix is $n-1$. 
**Proof Sketch:** The sum of all rows in $M$ is the zero vector, as each column contains exactly one $1$ and

one $-1$.

**Theorem:** If $G$ is a graph on $n$ vertices and has $k$ connected components, then $\text{rank}(Q(G)) = n - k$.
**Corollary:** The dimension of the null space of $Q(G)$ is equal to the number of connected components $k$.




## Polynomials
The set of all polynomials over a field $\mathbb{F}$, denoted by $\mathcal{P}$, forms an infinite-dimensional vector space under the operations of polynomial addition and scalar multiplication.

For any $n \in \mathbb{N}$, the set of polynomials of degree at most $n$, denoted by $\mathcal{P}_n$, is a subspace of $\mathcal{P}$.

**Standard Basis for $\mathcal{P}_n$:**
The standard basis for $\mathcal{P}_n$ is the set of monomials:
$$\mathcal{B} = \{1, x, x^2, \dots, x^n\}$$
Any polynomial $p(x) = a_n x^n + a_{n-1} x^{n-1} + \dots + a_1 x + a_0$ can be uniquely represented as a linear combination of these basis vectors, which implies $\dim(\mathcal{P}_n) = n+1$.

### Polynomial Interpolation
**Problem:** Given $n+1$ distinct points $(x_0, y_0), (x_1, y_1), \dots, (x_n, y_n)$ in $\mathbb{F}^2$, does there exist a unique polynomial $p(x) \in \mathcal{P}_n$ such that $p(x_i) = y_i$ for all $i = 0, 1, \dots, n$?


### Resultant and Sylvester Matrix
The **resultant** of two polynomials $p(x)$ and $q(x)$ is a scalar value that determines whether they share a common root.

Let $p(x) = a_n x^n + a_{n-1} x^{n-1} + \dots + a_0$ and $q(x) = b_m x^m + b_{m-1} x^{m-1} + \dots + b_0$. The **Sylvester matrix** $S(p, q)$ is an $(n+m) \times (n+m)$ matrix constructed from their coefficients:
$$S(p, q) = \begin{pmatrix} 
a_n & a_{n-1} & \dots & a_0 & 0 & \dots & 0 \\ 
0 & a_n & a_{n-1} & \dots & a_0 & \dots & 0 \\ 
\vdots & \vdots & \vdots & \ddots & \vdots & \ddots & \vdots \\ 
0 & \dots & 0 & a_n & a_{n-1} & \dots & a_0 \\ 
b_m & b_{m-1} & \dots & b_0 & 0 & \dots & 0 \\ 
0 & b_m & b_{m-1} & \dots & b_0 & \dots & 0 \\ 
\vdots & \vdots & \vdots & \ddots & \vdots & \ddots & \vdots \\ 
0 & \dots & 0 & b_m & b_{m-1} & \dots & b_0 \\ 
\end{pmatrix}$$

### Algebraic Numbers
A complex number $\alpha$ is called an **algebraic number** if it is a root of a non-zero polynomial with coefficients in $\mathbb{Q}$. That is, there exists $p(x) = a_n x^n + a_{n-1} x^{n-1} + \dots + a_0$ where $a_i \in \mathbb{Q}$ and $a_n \neq 0$, such that $p(\alpha) = 0$.





## Geometry

### Euclidean distances
**Problem:** Given three points $P_1, P_2, P_3$ and their pairwise distances $d_{12}, d_{23}, d_{31}$, how can we determine if these points can be constructed in the Euclidean plane $\mathbb{R}^2$?

The points can be embedded in $\mathbb{R}^2$ if and only if they satisfy the **triangle inequality**:
$$d_{ij} \le d_{ik} + d_{kj}$$
for all distinct $i, j, k \in \{1, 2, 3\}$.

**Example:**
Can we find points $p, q, r$ such that $|p - q| = 1, |q - r| = 1$, and $|p - r| = 3$?
No, because the triangle inequality requires:
$$|p - r| \le |p - q| + |q - r| \implies 3 \le 1 + 1 = 2$$
This is a contradiction, so such points cannot exist in any Euclidean space.

**Sufficiency for $n=3$:**
The triangle inequality is also **sufficient** for three points. Geometrically, we can construct the points by placing $P_1$ and $P_2$ at a distance $d_{12}$ apart. Consider two circles: $\mathcal{C}_1$ centered at $P_1$ with radius $d_{13}$, and $\mathcal{C}_2$ centered at $P_2$ with radius $d_{23}$. These circles intersect at a point $P_3$ if and only if the distance between their centers $d_{12}$ satisfies:
$$|d_{13} - d_{23}| \le d_{12} \le d_{13} + d_{23}$$
This condition is equivalent to the triangle inequalities for the three distances.

### General case for $n$ points
**Problem:** Given $n$ points and their pairwise distances $d_{ij}$, how can we determine if these points can be embedded in a Euclidean space $\mathbb{R}^k$?

```tikz
\begin{document}
\begin{tikzpicture}[scale=3,thick]
% Define coordinates for the square vertices

\coordinate (s) at (0,1);

\coordinate (r) at (1,1);

\coordinate (p) at (0,0);

\coordinate (q) at (1,0);

% Draw edges with weights

% Top edge

\draw (s) -- (r) node[midway, above] {2};

% Bottom edge

\draw (p) -- (q) node[midway, below] {2};

% Left edge

\draw (s) -- (p) node[midway, left] {2};

% Right edge

\draw (r) -- (q) node[midway, right] {2};

% Draw diagonals with weights

% Diagonal from s to q (top-left to bottom-right)

\draw (s) -- (q) node[pos=0.25, above right] {3};

% Diagonal from p to r (bottom-left to top-right)

\draw (p) -- (r) node[pos=0.75, above left] {3};

% Draw the vertices (bullets) and their labels

\foreach \n/\pos in {s/left, r/right, p/left, q/right}

\fill (\n) circle (1.5pt) node[\pos] {$\mathbf{\n}$};
\end{tikzpicture}
\end{document}
```
In the figure above, every subset of three points satisfies the triangle inequality (e.g., for triangle $pqr$, $2+2 > 3$). However, these four points cannot be embedded in any Euclidean space $\mathbb{R}^k$.




