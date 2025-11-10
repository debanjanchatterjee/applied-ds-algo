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
    n, w = read_ints()
    weights = []
    values = []
    dp = [[-1 for _ in range(w+1)] for _ in range(n+1)]
    for _ in range(n):
        wi, vi = read_ints()
        weights.append(wi)
        values.append(vi)

    def rec(level, cur_w):
        if cur_w > w:
            return -(10**9)
        if level == n:
            return 0
        if dp[level][cur_w] != -1:
            return dp[level][cur_w]
        #dont take
        ans = rec(level+1, cur_w)

        #take
        ans = max(ans, values[level] + rec(level+1, cur_w + weights[level]))

        dp[level][cur_w] = ans
        return dp[level][cur_w]

    print(rec(0, 0))

# Single test case
solve()