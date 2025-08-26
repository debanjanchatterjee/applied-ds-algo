# Solution Summary

The problem requires replacing each connected component of `0`s in a binary matrix with its component size, except when the component size is `1`, in which case we leave the `0` unchanged. `1`s act as walls and remain unchanged.

---

## Key Idea
- Use **DFS/BFS** to find all connected components of `0`s.
- For each component:
  - Count its size.
  - Replace all `0`s in that component with the size (if size > 1).
  - Keep them as `0` if the size is `1`.

---

## Steps
1. **Traverse the matrix**:
   - Whenever an unvisited `0` is found, perform DFS/BFS to explore its connected component.
2. **Mark visited cells** to avoid recounting.
3. **Store the component size** and update all its cells accordingly.
4. **Output the modified matrix**.

---

## Complexity
- Each cell is visited **at most once**, so:
  - **Time Complexity**: `O(N × M)`
  - **Space Complexity**: `O(N × M)` (for visited + recursion/queue)

---
