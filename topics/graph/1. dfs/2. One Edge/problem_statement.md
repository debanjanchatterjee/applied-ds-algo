# Problem: One Edge

## Description

You are given an undirected graph with `n` nodes and `m` edges. Your goal is to add **exactly one edge** between two nodes **not already connected directly or indirectly** in such a way that the **total number of connected components in the graph decreases**.

Your task is to find the **number of valid ways** to add such an edge.

---

## Input Format

- The first line contains two integers `n` and `m`:  
  the number of nodes and the number of edges.  
  (1 ≤ n ≤ 10⁵, 1 ≤ m ≤ 2 × 10⁵)
- The next `m` lines each contain two integers `a` and `b`, denoting an edge between node `a` and node `b`.  
  (1 ≤ a, b ≤ n)

---

## Output Format

- Print a single integer: the number of ways to add one new edge that reduces the number of connected components.

---

## Constraints

- No self-loops (`a ≠ b`)
- No multi-edges (at most one edge between any pair of nodes)

---

## Sample Input 1

```
5 4
1 2
2 3
1 3
4 5
```

---

## Sample Output 1

```
6
```

---

## Sample Input 2

```
4 3
1 2
2 3
3 4
```

## Sample Output 2

```
0
```

---

## Notes

- In **Sample 1**, there are 2 components: `{1, 2, 3}` and `{4, 5}`.  
  We can add an edge between any node from the first component and any node from the second.  
  That’s `3 × 2 = 6` ways.

- In **Sample 2**, the graph is already fully connected.  
  Any additional edge would create a cycle, not reduce the number of components — so the answer is `0`.

---
