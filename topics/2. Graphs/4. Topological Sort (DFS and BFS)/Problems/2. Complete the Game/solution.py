import sys
from sys import stdin, stdout
from collections import deque

def main():
    data = stdin.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1

    edge = [[] for _ in range(n + 1)]
    backedge = [[] for _ in range(n + 1)]
    in_degree = [0] * (n + 1)
    dp = [0] * (n + 1)
    dp[1] = 1

    for _ in range(m):
        a = int(data[idx]); idx += 1
        b = int(data[idx]); idx += 1
        edge[a].append(b)
        backedge[b].append(a)
        in_degree[b] += 1

    #uses Kahn's algorithm
    q = deque()
    for i in range(1, n + 1):
        if in_degree[i] == 0:
            q.append(i)

    MOD = 10**9 + 7
    while q:
        node = q.popleft()
        for prev in backedge[node]:
            dp[node] = (dp[node] + dp[prev]) % MOD
        for nxt in edge[node]:
            in_degree[nxt] -= 1
            if in_degree[nxt] == 0:
                q.append(nxt)

    stdout.write(str(dp[n]))

if __name__ == "__main__":
    main()
