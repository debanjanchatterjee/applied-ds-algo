# Problem: Easy Graph Queries

## Description

You are given an undirected graph **G** with **N** nodes and **M** edges. You have to answer **Q** queries.  
Each query is of one of the following two types:

- `1 X`: Print the size of the connected component containing node `X`.
- `2 X Y`: Print `YES` if node `X` and `Y` belong to the same connected component, else print `NO`.

---

## Input Format

- The first line contains three space-separated integers `N`, `M`, and `Q`  
  (1 ≤ N, M, Q ≤ 10⁵)
- The next **M** lines each contain two space-separated integers `u` and `v`, representing an undirected edge between nodes `u` and `v`.  
  (1 ≤ u, v ≤ N)
- The next **Q** lines each contain one of the two types of queries:
  - Type 1: `1 X`
  - Type 2: `2 X Y`

---

## Output Format

- Print **Q** lines, each containing the answer to a query:
  - For type `1 X`, print the size of the connected component containing node `X`.
  - For type `2 X Y`, print `YES` or `NO`.

---

## Constraints

- 1 ≤ N, M, Q ≤ 10⁵  
- 1 ≤ u, v, X, Y ≤ N

---

## Sample Input

```
6 5 5
1 2
2 3
1 3
4 4
5 6
1 2
1 4
2 3 4
1 5
2 5 6
```


---

## Sample Output

```
3
1
NO
2
YES
```

---

## Notes

- Nodes 1, 2, and 3 form a connected component of size 3.
- Node 4 is only connected to itself, so the component size is 1.
- Nodes 5 and 6 form a connected component of size 2.

---