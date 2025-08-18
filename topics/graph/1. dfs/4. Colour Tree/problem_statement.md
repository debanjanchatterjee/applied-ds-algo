# Tree Coloring Problem

## Problem Description
You have been given a **tree** with **N nodes** and **N - 1 edges**.  
You want to **colour each node** such that:  

1. No two **adjacent nodes** (directly connected by an edge) have the same colour.  
2. No two **nearly-adjacent nodes** (both directly connected to a common node) have the same colour.  

Your task is to find the **minimum number of colours** required to accomplish this.

---

## Input Format
- The first line contains an integer `N`, the number of nodes.  
- Each of the next `N−1` lines contains two integers `u` and `v`, representing an edge between nodes `u` and `v`.  

---

## Output Format
Print **one integer** — the minimum number of colours required.

---

## Constraints
- `1 ≤ N ≤ 10^5`

---

## Sample Input 1


```
4
1 2
4 3
2 3
```

## Sample Output 1

```commandline
3
```

---

## Note
One possible colouring of the nodes is:  
- colour(1) = 1  
- colour(2) = 2  
- colour(3) = 3  
- colour(4) = 1  

This satisfies both adjacency and nearly-adjacency constraints.