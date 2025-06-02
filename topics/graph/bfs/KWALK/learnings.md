# Knight Walk — Key Ideas

- **Problem:** Find minimum knight moves on an N×N chessboard from start (Sx, Sy) to final (Fx, Fy). Return -1 if unreachable.

- **Knight Moves:**  
  Possible moves are defined by coordinate shifts:  
  `dx = [1, 2, 2, 1, -1, -2, -2, -1]`  
  `dy = [2, 1, -1, -2, -2, -1, 1, 2]`

- **Board Validation:**  
  Check if a position is inside the board boundaries using:  
  `1 <= x <= N` and `1 <= y <= N`

- **BFS Approach:**  
  Use Breadth-First Search to find the shortest path since all moves cost 1.  
  Maintain a queue for current positions to explore.

- **Tracking State:**  
  Maintain two 2D arrays:  
  - `visited[x][y]` to mark visited cells  
  - `dist[x][y]` to store minimum moves to reach (x, y)  

- **Initialization:**  
  Set all distances to a large number (e.g., 1e9) initially.  
  Distance at the starting position is 0.

- **Queue Processing:**  
  For each position dequeued, check all knight moves.  
  If new position is valid and can be reached in fewer moves, update distance and enqueue.

- **Result:**  
  After BFS, if `dist[Fx][Fy]` is still large, print `-1`. Otherwise, print the minimum moves.

- **Time Complexity:**  
  O(N²) worst case — feasible for N up to 1000.

---

*This summary highlights the main ideas behind solving the Knight Walk problem efficiently.*


# Problem: Knight Walk

```
Description
You are given an N×N chessboard and a knight with starting position (Sx,Sy). You are given a final position (Fx,Fy). You have to find the minimum number of moves required to reach the final position.

Complete the function:

int KnightWalk(int N, int Sx, int Sy, int Fx, int Fy);

Input Format
The first line contains a single integer T - the number of test cases.
The first line of each test case contains five integers N Sx Sy Fx Fy - the size of the board, initial position and final position.

Output Format
For every test case print the minimum number of moves required. If it is not possible print -1.

Constraints
1 ≤ T ≤ 20
1 ≤ N ≤ 1000
1 ≤ Sx, Sy, Fx, Fy ≤ N

Sample Input 1
3
6 4 5 1 1
6 3 3 6 6
6 6 1 1 6

Sample Output 1
3
2
4

Note
The situation described in test case 1 is:

Chessboard Knight Move

The minimum number of moves is 3.
```
