import sys
from collections import Counter

# Fast input reading
input = sys.stdin.read
sys.setrecursionlimit(1 << 25)

def read_ints():
    return map(int, sys.stdin.readline().strip().split())

def read_list():
    return list(map(int, sys.stdin.readline().strip().split()))

def solve():
    n, m, q = read_ints()

    # Adjacency list for the graph
    g = [[] for _ in range(n + 1)]

    for _ in range(m):
        u, v = read_ints()
        g[u].append(v)
        g[v].append(u)

    # visited[i] will store component id of node i
    visited = [0] * (n + 1)

    # DFS to mark connected components
    def dfs(node, component_id):
        visited[node] = component_id
        for neighbor in g[node]:
            if visited[neighbor] == 0:
                dfs(neighbor, component_id)

    component_id = 1
    for i in range(1, n + 1):
        if visited[i] == 0:
            dfs(i, component_id)
            component_id += 1

    # Count number of nodes in each component
    node_count = Counter(visited)

    # Process queries
    for _ in range(q):
        query = read_list()
        if len(query) == 2:
            # Type 1: size of component containing X
            x = query[1]
            print(node_count[visited[x]])
        else:
            # Type 2: check if X and Y are in the same component
            x, y = query[1], query[2]
            print("YES" if visited[x] == visited[y] else "NO")

# Single test case
solve()