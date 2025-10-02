---
title: Design and Analysis of Algorithms
tags:
  - incomplete
created: 2025-07-25
draft: false
---

DAA - Week 01 - jnair.work@gmail.com

## Design of Algorithms
1. Introduction
2. Design of Algorithms
3. Analysis of Algorithms
4. Algorithm design techniques
5. Problem types
6. Example problem


Definition:
Algo :: Sequence of unambiguous instructions for obtaining a required output for any legitimate input in finite amount of time

### Fibonacci Series

$$
F_{n} = F_{n-1} + F_{n-2},\quad F(1) =1, \quad F(0) = 0
$$
```
fib1
if n = 0 return 0
if n = 1 reutrn 1
else return fib1(n-1) + fib1(n-2)
```

```
fib2
if n = 0 return 0
create an array f[0,...,n]
f(0) = 0 f(1) = 1
for i =2:n
	f[i]= f[i-1] + f[i-2]
return f[n]
```

fib3
$$
\begin{pmatrix} 
F_{n} \\ 
F_{n+1}
\end{pmatrix}
 = \begin{pmatrix}
0 & 1 \\ 
1 & 1
\end{pmatrix}^n
\begin{pmatrix}
F_{0} \\
F_{1}
\end{pmatrix}
$$

### Finding GCD

Euclid's algorithm
1. if n = 0, return value of m
2. Divide m by n, set m % n to r
3. Assign value of n to m and r to n, repeat from 1.

algorithm 2
1. find prime factors of m and n
2. find common factors -> largest subset of common factors
3. find the product

Designing an Algorithm and data structures
Methods of specifying an algo
Proving an algo correctness
Analyzing an Algorithm 


**Amortized Efficiency**

#### Transitive property
If f(n) is O(g(n)) and g(n) is O(h(n)) then f(n) = O(h(n))

#### Reflexive property
...



f(n) = O(g(n)) and f() = $\Omega (g(n))$ then f(n) = $\Theta(g(n))$

f(n) = O(g(n)) and d(n) = O(e(n)), 
then f(n) + d(n) = O(max(g(n),e(n)))

f(n) = O(g(n)) and d(n) = O(e(n)) then f(n) d(n) 

### Design Techniques
Divide and conquer
Prune and Search
Dynamic programing
Greedy algorithms

##### Prune and search
$T(n) = T\left( \left( 1-\frac{1}{f} \right)n \right) + E(n) +O(n)$

#### Problems Types
1. Searching
2. Sorting
3. String Processing
4. Graph Problems
5. Combinatorial Problems
6. Geometric Problems
7. Numerical Problems

#### Data Structures
Linear:
	arrays
	lists
	queues
	stacks
	strings
Graph:
	Undirected/ Directed
	Weighted/Binary
	Dense/Sparse
	Signed
	k-partite
	Representation - sets
	 Paths and cycles
	 connected components
Trees
	Rooted and unrooted

## Mathematical analysis
1. Non recursive vs recursive algorithms
2. Empirical analysis of algorithms
	1. Formula
	2. Visualisation
3. Towers of Hanoi

Formula for time complexity
1. Backward substitution:
	1. $M(n) = M(n-1) + 1$ for $n>0$
2.  General plan for solving (non)recursive algorithms.
	1. Decide on parameter dependent on input size (n)
	2. Identify the algo/s basic operation
	3. Decide if the implementation of the op is different of $\Theta, O,o$

| Recursive Algorithms                                                       | Non-recursive algorithms |
| -------------------------------------------------------------------------- | ------------------------ |
| 4. find your recurrence relation initial conditon / terminating condition. | 4.                       |
| 5.                                                                         | 5.                       |

### Algorithm for Determining an Array has Distinct Elements
$$

$$
```

```

### Plotting Empirical Analysis of Algorithms

```tikz
\begin{document}
\begin{tikzpicture}
%draw a x-y plaine
\draw[->] (0,0) -- (6,0) node[right] {n};
\draw[->] (0,0) -- (0,6) node[above] {T(n)};
% Draw a sqrt x plot with increased sampling
\draw[domain=0:5, samples=100, smooth, variable=\x] plot ({\x}, {sqrt(\x)});
% add random points around the graph
\foreach \x in {0,1,2,3,4,5} {
		\fill[black] (\x,{sqrt(\x) + rand}) circle (2pt);
}


\end{tikzpicture}
\end{document}
```

### Towers of Hanoi




$$
\begin{align}
T(n) = 2T(n-1) + 1 \\
T(n-1) = (2T(n-2) + 1) +1\\
i: T(n) = 2^{i}T(n-i) + 2^i - 1 \\
\end{align}
$$
```tikz
\begin{document} 
\begin{tikzpicture} % Define the style for the pegs and disks 
\tikzstyle{peg}=[line width=2pt] 
\tikzstyle{disk}=[draw, fill=blue!50, line width=1pt] 
% Draw the base 
\draw[thick] (-5,0) -- (5,0); 
% Draw the pegs 
\foreach \x in {-3, 0, 3} { \draw[peg] (\x,0) -- (\x,4); } 
% Draw the disks on the first peg 
\foreach \y/\w in {0.5/2.5, 1/2, 1.5/1.5, 2/1} { \draw[disk] (-3-\w/2,\y-0.5) rectangle (-3+\w/2,\y+0.3-0.5); } % Optionally, label the pegs 
\node at (-3,-0.5) {A}; 
\node at (0,-0.5) {B}; 
\node at (3,-0.5) {C}; 
\end{tikzpicture} 
\end{document}
```
### Brute force, Decrease-and-Conquer & D & C Algorithms

#### Brute Force: Selection Sort
```Selection sort
// Sorts a given array by selection sort
//Input: An array A of n elements
//Output: A sorted array A
for i = 0 to n-1
	min = i
	for j = i+1 to n-1
		if A[j] < A[min]
			min = j
	swap A[i] with A[min]
```

has $\Theta(n^{2})$ for all inputs

#### Brute force: Bubble Sort
```Bubble sort
// Sorts a given array by bubble sort
//Input: An array A of n elements
//Output: A sorted array A
for i = 0 to n-1
	for j = 0 to n-2-i
		if A[j] > A[j+1]
			swap A[j] with A[j+1]
```

#### Brute-Force: Sequential Search
```
Sequential search
// Searches for a key in an array
//Input: An array A of n elements and a key k
//Output: The index of k in A or -1 if not found
for i = 0 to n-1
	if A[i] == k
		return i
	return -1
		
```
```
//Sequential with search key as sentinel
Sequential search with search key as the last element of array to avoid extra condition
#todo



```


#### Brute-force: String matching
```String matching
// Searches for a pattern in a text
//Input: A text T of length n and a pattern P of length m
//Output: The index of the first occurrence of P in T or -1 if not found
for i = 0 to n-m
	for j = 0 to m-1
		if T[i+j] != P[j]
			break
	if j == m-1
		return i
	return -1
```

#### Exhaustive Search: Traveling Salesman Problem
```tikz
\begin{document}
\begin{tikzpicture}
% Define the style for vertices and edges 
\tikzstyle{vertex}=[circle, draw, minimum size=20pt, inner sep=0pt] 
\tikzstyle{edge}=[draw, thick] % Define the positions of the vertices 
\node[vertex] (A) at (0, 1.5) {A}; 
\node[vertex] (B) at (1.5, 0) {B}; 
\node[vertex] (C) at (0, -1.5) {C}; 
\node[vertex] (D) at (-1.5, 0) {D}; % Draw the edges with labels 
\draw[edge] (A) -- (B) node[midway, above right] {5}; 
\draw[edge] (A) -- (C) node[midway, right] {1}; 
\draw[edge] (A) -- (D) node[midway, above left] {4}; 
\draw[edge] (B) -- (C) node[midway, below right] {3}; 
\draw[edge] (B) -- (D) node[midway, below] {2}; 
\draw[edge] (C) -- (D) node[midway, below left] {1};
\end{tikzpicture}
\end{document}
```

#### Exhaustive Search: Knapsack Problem

Knapsack Problem statement : Given a set of items, each with a weight and a value, determine the number of each item to include in a collection so that the total weight is less than or equal to a given limit and the total value is as large as possible.
#### Exhaustive Search: DFS: Data Structures

#### Exhaustive Search: BFS: Data Structures


**Divide and Conquer**:
1. Strategy
2. Parallelism
3. reduction

### General D&C Recurrence Formula
$$
T(n) = aT\left( \frac{n}{b} \right) + f(n)
$$
where $f(n) \in \Theta(n^{d}), d\geq 0$ and f(n) is the time spent on dividing an instance of size n to instances of size n/b.

Thus the order of growth of T(n) depends on:
- values of constants a,b
- order of growth of f(n)
#### Master Theorem
$$
T(n) \in \begin{cases}
\Theta(n^{d})  & \quad a<b^{d} \\
\Theta (n^{d} \log n) & \quad a = b^{d} \\
\Theta(n^{\log_{b}a}) & \quad a > b^{d}
\end{cases}
$$

**Exercise:** 
1. $T(n) = 2T(n) + 1$
2. $T(n) = 4T\left( \frac{n}{2} \right) + n$
3. $T(n)=4T\left( \frac{n}{2} \right) +n^{2}$
4. $T(n) = 4T\left( \frac{n}{2} \right)+n^{3}$


**Solution:**


### Multiplication algorithm D&C

Multiplication of 2 large numbers karatsuba

$T(n)=3T\left( \frac{n}{2} \right) + cn$, from the Master theorem we have $T(n) \in \Theta(n^{\log_{2}3})$ 

Example:
1.

### D&C Multiplication of 2 Matrices - Strassen's Method

#incomplete 

## Quicksort
```
def QUICKSORT(A,p,r):
	q = PARTITION(A,p,r)
	QUICKSORT(A,p,q-1)
	QUICKSORT(A,q+1,r)
```

```
def PARTITION(A,p,r):
	x = A[r]
	i = p-1
	for j=p to r-1:
		if A[j] <= x:
			i++
			swap(A[i],A[j])
	swap(A[i+1],A[r])
	return (i+1)
```

**Loop Invariant**: at the beginning of each iteration (loop liens 3-6 of partition) for any array index k, the foll. condn hold:
1. If $p\leq k\leq i$ then $A[k] \leq x$ pivot
![[IMG_20250822_101328.jpg]]

### D & C randomized algorithm for selection of median 


**Lemma:**

**Proof:**


