# Cycle Detection in Undirected Graph Using DFS

## Problem
Detect if there is a cycle in an undirected graph using DFS traversal.

## Key Concepts

### 1. DFS Coloring Scheme
- **1 (White)**: Unvisited
- **2 (Gray)**: Visiting
- **3 (Black)**: Visited

### 2. DFS Traversal
- For each unvisited node, perform DFS.
- Skip the immediate parent node to avoid falsely detecting a cycle.
- If a visiting node (color 2) is encountered, it means a back edge is found, indicating a cycle.

### 3. Edge Classification (applied in DFS context):
- **Tree Edge**: To an unvisited node.
- **Back Edge**: To an ancestor in the current DFS path (indicates a cycle).
- **Forward Edge**: (Not present in undirected graphs in cycle detection)
- **Cross Edge**: (Not relevant in undirected graphs but appears in DAGs or directed graphs)

## Pseudocode Summary

```
for each node:
    if node is unvisited:
        dfs(node, parent)
        if cycle found:
            return YES
return NO
```

## Python Code Snippet

```python
color = [1] * (n + 1)  # 1: unvisited, 2: visiting, 3: visited

def dfs(node, parent):
    color[node] = 2
    for neighbor in graph[node]:
        if neighbor == parent:
            continue
        if color[neighbor] == 1:
            dfs(neighbor, node)
        elif color[neighbor] == 2:
            # Back edge found
            has_cycle = True
    color[node] = 3
```

## Complexity
- **Time Complexity**: O(N + M), where N is the number of nodes and M is the number of edges.
- **Space Complexity**: O(N) for visited states and recursion stack.