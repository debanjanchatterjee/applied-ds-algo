import sys
import heapq
sys.setrecursionlimit(1 << 25)

# Fast input
def read_ints(): return map(int, sys.stdin.readline().strip().split())

def solve():
    n, m = read_ints()
    g = [[] for _ in range(n+1)]
    indegree = [0] * (n+1)
    for i in range(m):
        a, b = read_ints()
        g[a].append(b)
        indegree[b] += 1

    def kahnsalgo():
        nonlocal g, n, m, indegree
        pq = []
        for i, x in enumerate(indegree):
            if i == 0:
                continue
            if x==0:
                heapq.heappush(pq, i)

        ans = []
        while len(pq) > 0:
            cur = heapq.heappop(pq)
            ans.append(cur)
            for x in g[cur]:
                indegree[x] -= 1
                if indegree[x] == 0:
                    heapq.heappush(pq, x)
        return ans

    smallest_permutation = kahnsalgo()
    if len(smallest_permutation) < n:
        print(-1)
    else:
        print(" ".join(map(str,smallest_permutation)))


# Entry point
t = 1
for _ in range(t):
    solve()