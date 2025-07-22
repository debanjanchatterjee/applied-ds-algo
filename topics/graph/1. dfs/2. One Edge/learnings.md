## Learnings

### 🔍 Problem Summary
The problem asks to find the number of valid ways to add exactly one edge between two **unconnected components** of an undirected graph so that the **total number of connected components decreases**.

### 🧠 Core Concepts & Techniques
- **Graph Traversal (DFS):** Used Depth-First Search to label all nodes with a unique connected component ID.
- **Component Size Tracking:** After DFS, we used `Counter` to track how many nodes are present in each connected component.
- **Mathematical Insight:** To reduce the number of components, we must add an edge between **any two different components**. The total number of such valid edges is:
  
  \[
  \text{Total Ways} = \sum_{i < j} (\text{size}_i \times \text{size}_j)
  \]

  Instead of checking every pair (which is O(k²)), we computed this efficiently using a running sum:
  
  ```python
  total_so_far = 0
  for size in component_sizes:
      result += size * total_so_far
      total_so_far += size


⚠️ Edge Cases Considered


	•	If the graph is already fully connected (only 1 component), no new edge can reduce the number of components → answer is 0.
	•	Handles multiple components and isolated nodes correctly.
	•	No self-loops or duplicate edges are added as per constraints.

🧮 Time and Space Complexity

⏱ Time Complexity
	•	O(N + M):
	•	DFS to visit each node and edge once → O(N + M)
	•	Counting component sizes → O(N)
	•	Computing result via linear scan of components → O(K), where K = number of components (K ≤ N)

🧠 Space Complexity
	•	O(N + M):
	•	Adjacency list → O(N + M)
	•	Visited array → O(N)
	•	Component counter → O(N) in worst case

✅ Why This Works

This approach reduces the problem to a component-level combinatorics problem:
	•	If we know the sizes of each connected component, we just need to count the number of edges we can add between those components.
	•	This avoids checking individual node pairs and scales efficiently even for large inputs (N ≤ 10⁵, M ≤ 2×10⁵).

⸻

This problem reinforced how graph traversal + mathematical formulation can turn a potentially brute-force problem into a fast and elegant solution.