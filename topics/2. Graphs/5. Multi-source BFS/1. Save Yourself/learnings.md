# Solution Summary

## Approach
- The problem is solved using **multi-source BFS** for both monsters and the player (`A`).  
- Two BFS runs are performed:
  1. **Monster BFS**: Compute the earliest time each monster can reach every cell (`distMon`).  
  2. **Player BFS**: Compute the earliest time the player can reach every cell (`distA`) while storing parent pointers (`parx`, `pary`) for path reconstruction.

## Steps
1. **Input parsing**: Read the grid and initialize:
   - `distMon` for monsters' distances.
   - `distA` for the player’s distances.
   - Parent matrices for reconstructing the path.
   - Queues for BFS (`monsterOcc` and `AOcc`).
2. **Monster BFS**: Spread from all monster cells simultaneously, marking the shortest time monsters can reach each cell.
3. **Player BFS**: Spread from the starting position `A`, but only to cells where:
   - The cell is walkable.
   - It hasn’t been visited by the player yet.
4. **Escape check**: For all boundary cells, check if:
   - The player can reach that cell.
   - The player reaches strictly earlier than any monster (or the monster never reaches it).
5. **Output**:
   - If no boundary is reachable safely → print `"NO"`.
   - If reachable → print `"YES"` and the shortest distance.
   - Path reconstruction logic is outlined in comments (not implemented in Python code).

## Key Ideas
- **Multi-source BFS** ensures shortest distances from multiple monsters at once.  
- Compare distances (`distA < distMon`) to guarantee safety.  
- Use parent pointers for path reconstruction (similar to C++ logic, but not implemented here).  

## Complexity
- Time Complexity: **O(n × m)** (each cell processed at most once for player and monsters).  
- Space Complexity: **O(n × m)** for grids and distance matrices.