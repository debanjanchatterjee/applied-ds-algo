# Round Trip Detection in Zenithland

## 📝 Problem Description

Zenithland has `n` cities and `m` roads between them. Your task is to check for the existence of a **round trip** that:

- Begins in a city,
- Goes through **two or more other cities**,
- And finally returns to the starting city.

**Important:** Every intermediate city on the route must be **distinct**.

The roads are **undirected**, meaning you can go both ways between cities.

---

## 📥 Input Format

- The first line contains two integers `n` and `m`:  
  `n` = number of cities  
  `m` = number of roads

- The next `m` lines each contain two integers `a` and `b`, indicating a road between cities `a` and `b`.

### Constraints

- `1 ≤ n ≤ 10^5`  
- `1 ≤ m ≤ 2 × 10^5`  
- `1 ≤ a, b ≤ n`  
- No self-loops (`a != b`) and at most one road between any two cities.

---

## 📤 Output Format

Print `"YES"` if such a round trip exists, otherwise print `"NO"`.

---

## 🔍 Sample Input 1

```
5 6
1 3
1 2
5 3
1 5
2 4
4 5
```

### Sample Output 1

```
YES
```

---

## 🔍 Sample Input 2

```
4 3
1 2
1 3
3 4
```

### Sample Output 2

```
NO
```

---

## 🔁 Graph Theory Note

This problem is equivalent to **detecting a cycle** in an **undirected graph**.

### Types of Edges in DFS Traversal:

- **Tree Edge:** Leads to an unvisited node.
- **Back Edge:** Leads to an ancestor in the DFS tree → this indicates a **cycle**.
- **Forward Edge & Cross Edge:** These are more relevant in **directed graphs**. In undirected graphs, only tree and back edges matter.

If a **back edge** is encountered during DFS, a cycle (and hence a round trip) exists.

---

## ✅ Approach

1. Model cities as graph nodes and roads as undirected edges.
2. Use DFS or Union-Find to detect cycles.
3. If a cycle is found, output `"YES"`; otherwise, output `"NO"`.

