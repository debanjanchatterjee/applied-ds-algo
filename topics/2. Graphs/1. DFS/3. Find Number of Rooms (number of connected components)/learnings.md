# Counting the Number of Rooms in a Building Map

## Problem Overview
Given a 2D map of a building with walls (`#`) and floor spaces (`.`), the goal is to count the number of **rooms**. A room is defined as a connected region of floor spaces where you can move **up, down, left, or right**.  

---

## Approach
1. **Graph Representation**
   - The 2D map is treated as a grid graph.
   - Each floor cell (`.`) is a node.
   - Edges exist between adjacent floor cells (up, down, left, right).

2. **Depth-First Search (DFS)**
   - For each unvisited floor cell, start a DFS.
   - Mark all connected floor cells as visited.
   - Each DFS traversal represents **one room**.

3. **Validation Function**
   - Ensures the next cell is inside the grid, is a floor, and is unvisited.

4. **Counting Rooms**
   - Iterate through all cells.
   - Start a DFS whenever an unvisited floor cell is found.
   - Increment a counter for each DFS call (number of rooms).

---

## Implementation Highlights
- **Visited Grid:** Tracks whether a cell has been visited to avoid revisiting.  
- **Directional Arrays (`dx`, `dy`):** Simplifies moving in four directions.  
- **Fast Input & Large Recursion Limit:**  
  ```python
  import sys
  input = sys.stdin.read
  sys.setrecursionlimit(1 << 25)
  ```
  

