# Learnings from Lexicographically Smallest Topological Sort

## 1. Problem Understanding
- We need to find the **lexicographically smallest topological order** of a directed graph.
- If the graph contains a cycle, topological sorting is impossible → output `-1`.

---

## 2. Key Algorithm: Kahn’s Algorithm with Min-Heap
- **Kahn’s Algorithm** is a BFS-based topological sorting algorithm.
- Normally, a queue is used to store nodes with indegree `0`.
- To ensure **lexicographically smallest order**, replace the queue with a **min-heap**:
  - Always extract the smallest numbered node available.
  - Push new nodes with indegree `0` into the heap.

---

## 3. Implementation Details
- **Graph Representation**: adjacency list `g[a] → b`.
- **Indegree Array**: tracks number of incoming edges for each node.
- **Heap (`heapq`)**:
  - Stores all nodes with indegree `0`.
  - Pops the smallest available node first.
- **Cycle Detection**:
  - If the result has fewer than `n` nodes, the graph has a cycle.

---

## 4. Code Improvements Learned
1. **Avoid `nonlocal`**: Not required inside nested functions when variables are already accessible.
2. **Cleaner Loops**: Iterate directly from `1` to `n` instead of checking `i == 0`.
3. **Meaningful Variable Names**:
   - `pq` → `min_heap`
   - `ans` → `topo_order`
4. **Multiple Test Cases**: Can be handled by looping over `t`.

---

## 5. Complexity Analysis
- **Time Complexity**:  
  - `O(V + E + V log V)`  
  - `O(V + E)` for indegree + adjacency traversal.  
  - `O(V log V)` from heap operations.  
- **Space Complexity**:  
  - `O(V + E)` for adjacency list + indegree array.

---

## 6. Key Takeaways
- Using a **min-heap** ensures lexicographically smallest ordering in topological sort.
- **Kahn’s algorithm** is an iterative, cycle-detecting approach suitable for large graphs.
- Clean code practices (naming, avoiding redundant checks) improve readability and maintainability.