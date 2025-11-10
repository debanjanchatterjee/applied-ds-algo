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
