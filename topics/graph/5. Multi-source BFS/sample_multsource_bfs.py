from collections import deque

# Directions: down, up, right, left
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def is_valid(x, y, n, m, arr):
    return 0 <= x < n and 0 <= y < m and arr[x][y] == '.'

def multi_bfs(mons, dis_mons, arr, n, m):
    q = deque()
    for x, y in mons:
        q.append((x, y))
        dis_mons[x][y] = 0

    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if is_valid(nx, ny, n, m, arr):
                if dis_mons[nx][ny] > dis_mons[x][y] + 1:
                    q.append((nx, ny))
                    dis_mons[nx][ny] = dis_mons[x][y] + 1

def bfs(start, dis_pers, arr, n, m):
    q = deque()
    q.append(start)
    dis_pers[start[0]][start[1]] = 0

    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if is_valid(nx, ny, n, m, arr):
                if dis_pers[nx][ny] > dis_pers[x][y] + 1:
                    q.append((nx, ny))
                    dis_pers[nx][ny] = dis_pers[x][y] + 1

def solve(n, m, arr, st, mons, bd_cells):
    # Initialize distance matrices
    INF = 10**9
    dis_pers = [[INF] * m for _ in range(n)]
    dis_mons = [[INF] * m for _ in range(n)]

    # BFS from monsters
    multi_bfs(mons, dis_mons, arr, n, m)

    # BFS from person
    bfs(st, dis_pers, arr, n, m)

    # Check boundary cells
    for x, y in bd_cells:
        if dis_pers[x][y] < dis_mons[x][y]:
            print("YES")
            print(dis_pers[x][y])
            return
    print("NO")

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    n, m = map(int, input().split())
    arr = []
    mons = []
    bd_cells = []
    st = None

    for i in range(n):
        row = list(input().strip())
        arr.append(row)
        for j, ch in enumerate(row):
            if ch == 'A':
                st = (i, j)
                if i == 0 or j == 0 or i == n-1 or j == m-1:
                    bd_cells.append((i, j))
            elif ch == 'M':
                mons.append((i, j))
            elif (i == 0 or j == 0 or i == n-1 or j == m-1) and ch == '.':
                bd_cells.append((i, j))

    solve(n, m, arr, st, mons, bd_cells)