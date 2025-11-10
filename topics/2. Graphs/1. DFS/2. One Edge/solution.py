import sys
from collections import Counter

# Fast input reading
input = sys.stdin.read
sys.setrecursionlimit(1 << 25)

def read_ints():
    return map(int, sys.stdin.readline().strip().split())

def solve():
    n, m = read_ints()

    # Build graph
    g = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = read_ints()
        g[u].append(v)
        g[v].append(u)

    visited = [0] * (n + 1)

    # DFS to label connected components
    def dfs(node, comp_id):
        visited[node] = comp_id
        for neighbor in g[node]:
            if visited[neighbor] == 0:
                dfs(neighbor, comp_id)

    component_id = 1
    for i in range(1, n + 1):
        if visited[i] == 0:
            dfs(i, component_id)
            component_id += 1

    # Count nodes in each component
    node_counts = Counter(visited[1:])

    # Calculate number of valid edge additions
    # Total = sum of product of sizes of different components
    result = 0
    total_so_far = 0
    for count in node_counts.values():
        result += count * total_so_far
        total_so_far += count

    print(result)

solve()