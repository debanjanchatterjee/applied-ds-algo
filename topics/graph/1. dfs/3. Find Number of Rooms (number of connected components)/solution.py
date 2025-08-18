import sys
from collections import Counter

# Fast input reading
input = sys.stdin.read
sys.setrecursionlimit(1 << 25)

def read_ints():
    return map(int, sys.stdin.readline().strip().split())

def solve():
    n, m = read_ints()
    g = []
    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]

    visited = [[0 for _ in range(m)] for _ in range(n)]
    for _ in range(n):
        row = sys.stdin.readline().strip()
        g.append(list(row))

    def is_valid(x, y):
        nonlocal n, m
        if x < 0 or y < 0 or x >= n or y >= m or g[x][y] == '#':
            return False
        return True

    def dfs(x, y):
        nonlocal dx, dy
        visited[x][y] = 1
        for ddx, ddy in zip(dx, dy):
            u = x + ddx
            v = y + ddy
            if is_valid(u, v) and visited[u][v] == 0:
                dfs(u, v)

    ans = 0     # number of connected components
    for i in range(n):
        for j in range(m):
            if is_valid(i, j) and visited[i][j] == 0:
                ans += 1
                dfs(i, j)
    print(ans)





solve()