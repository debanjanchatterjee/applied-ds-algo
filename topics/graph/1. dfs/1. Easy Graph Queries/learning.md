## Learnings

- Applied DFS to find connected components in an undirected graph.
- Used a `visited[]` array to assign a component ID to each node.
- Precomputed component sizes using `Counter` for efficient query responses.
- Handled two types of queries efficiently:
  - Size of the connected component of a node.
  - Whether two nodes belong to the same component.
- Learned the importance of precomputing in graph problems to handle multiple queries in O(1) time.