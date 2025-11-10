import sys
import heapq
from collections import Counter,  deque
from bisect import bisect_right

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

def solve():
    n, m = read_ints()
    g = [[] for _ in range(n+1)]
    visited = [0] * (n + 1)
    dist = [int(1e9) for _ in range(n + 1)]

    for _ in range(m):
        u, v = read_ints()
        g[u].append(v)
        g[v].append(u)

    def bfs(node):
        nonlocal n, m, g
        q = deque()
        q.append(node)
        dist[node] = 0

        while len(q) > 0:
            cur = q.popleft()
            if visited[cur] == 1:
                continue
            visited[cur] = 1

            for neigh in g[cur]:
                if dist[neigh] > dist[cur] + 1:
                    dist[neigh] = dist[cur] + 1
                    q.append(neigh)

    number_of_connected_components = 0

    for v in range(1, n+1):
        if visited[v] == 0:
            bfs(v)
            number_of_connected_components += 1

    print(number_of_connected_components-1)

solve()


