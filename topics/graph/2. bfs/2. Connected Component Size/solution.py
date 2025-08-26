import sys
from collections import deque

# Fast input reading
input = sys.stdin.read
sys.setrecursionlimit(1 << 25)

''' Fast IO '''

def read_int(): return int(sys.stdin.readline().strip())


def read_ints(): return map(int, sys.stdin.readline().strip().split())


def read_list(): return list(map(int, sys.stdin.readline().strip().split()))


def read_str(): return sys.stdin.readline().strip()


def read_strs(): return sys.stdin.readline().strip().split()


# Fast output
def print_list(arr, sep=" "):
    sys.stdout.write(sep.join(map(str, arr)) + "\n")


def print_dict(d):
    for key, value in d.items():
        sys.stdout.write(f"{key}: {value}\n")

def print_graph(g, n):
    for i in range(n):
        print(" ".join(map(str, g[i])))


def solve():
    n, m = read_ints()
    g = []
    for i in range(n):
        row = read_list()
        g.append(row)

    cc_size = dict() # comp_id -> size
    comp_id = 1

    visited = [[0 for _ in range(m)] for _ in range(n)]
    dist = [[int(1e9) for _ in range(m)] for _ in range(n)]


    def bfs(node, comp_id):
        nonlocal g, n, m, visited, dist

        def is_valid(x, y):
            if x < 0  or x >=n or y < 0 or y>= m or g[x][y] == 1:
                return False
            return True

        dx = [1, 0, -1, 0]
        dy = [0, -1, 0, 1]
        size = 1
        q = deque()


        q.append(node)
        dist[node[0]][node[1]] = 0

        while len(q) > 0:
            cur = q.popleft()
            curx, cury = cur[0], cur[1]

            if visited[curx][cury] > 0:
                continue

            visited[curx][cury] = comp_id

            for xi, xj in zip(dx, dy):
                nx, ny = curx + xi, cury + xj
                # print(nx, ny)
                if is_valid(nx, ny) and dist[nx][ny] > dist[curx][cury] + 1:
                    q.append([nx, ny])
                    dist[nx][ny] = dist[curx][cury] + 1
                    size += 1
        return size

    for i in range(n):
        for j in range(m):
            if g[i][j] == 0 and visited[i][j] == 0:
                comp_size = bfs([i,j], comp_id)
                cc_size[comp_id] = comp_size
                comp_id += 1

    for i in range(n):
        for j in range(m):
            if g[i][j] == 0 and cc_size[visited[i][j]] > 1:
                g[i][j] = cc_size[visited[i][j]]

    print_graph(g, n)


t = read_int()
for _ in range(t):
    solve()


