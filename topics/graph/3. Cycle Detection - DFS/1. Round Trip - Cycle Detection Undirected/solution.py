import sys
sys.setrecursionlimit(1 << 25)

# Fast input
def read_ints(): return map(int, sys.stdin.readline().strip().split())

def solve():
    n, m = read_ints()
    g = [[] for _ in range(n + 1)]

    for _ in range(m):
        u, v = read_ints()
        g[u].append(v)
        g[v].append(u)

    color = [1] * (n + 1)  # 1: unvisited, 2: visiting, 3: visited
    parent = [0] * (n + 1)
    has_cycle = False

    def dfs(node, par):
        nonlocal has_cycle
        parent[node] = par
        color[node] = 2

        for v in g[node]:
            if v == parent[node]:
                continue
            if color[v] == 1:
                dfs(v, node)
            elif color[v] == 2:
                has_cycle = True

        color[node] = 3

    for i in range(1, n + 1):
        if color[i] == 1:
            dfs(i, 0)
            if has_cycle:
                print("YES")
                return

    print("NO")

# Entry point
t = 1
for _ in range(t):
    solve()