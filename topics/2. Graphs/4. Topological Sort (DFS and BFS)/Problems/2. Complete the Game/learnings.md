# Learnings: Counting Paths in a DAG using Dynamic Programming

## 1. DAG Property
- Directed Acyclic Graphs (DAGs) have no cycles.
- This enables **Dynamic Programming (DP)** because nodes can be processed in a **topological order**.

---

## 2. DP Formulation
- Define `dp[v]` = number of distinct paths from node `1` to node `v`.
- Transition:
  ```
  dp[v] = Σ dp[u]  for all edges (u → v)
  ```
- Initialization:
  ```
  dp[1] = 1
  ```
- Process nodes in **topological order** so that all predecessors `u` are computed before processing `v`.

---

## 3. Implementation Strategy
- Use **Kahn’s algorithm (BFS-based)** or **DFS-based topological sort**.
- For each node `v`, update:
  ```
  dp[v] = (dp[v] + dp[u]) % MOD
  ```
  where `MOD = 10^9 + 7`.

---

## 4. Complexity Analysis
- **Time Complexity**:  
  - `O(n + m)`  
  - Each node and edge is processed once.
- **Space Complexity**:  
  - `O(n + m)`  
  - Needed for adjacency list + `dp` array.

---

## 5. Key Takeaways
- **Topological order** ensures DP dependencies are satisfied.
- The problem reduces to **path counting in DAGs**, which is efficiently solvable using DP.
- Modular arithmetic (`10^9 + 7`) prevents overflow in large path counts.
