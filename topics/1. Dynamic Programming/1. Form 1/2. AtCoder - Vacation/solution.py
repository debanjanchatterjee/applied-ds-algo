import sys
from collections import Counter

# Fast input reading
input = sys.stdin.readline
sys.setrecursionlimit(1 << 25)

def read_int():
    return int(input())

def read_ints():
    return map(int, sys.stdin.readline().strip().split())

def read_list():
    return list(map(int, sys.stdin.readline().strip().split()))

def solve():
    n = read_int()

    h = []
    dp = [[-1 for _ in range(3)] for _ in range(n+1)]
    for _ in range(n):
        a, b, c = read_ints()
        h.append([a, b, c])

    def rec(level, last_choice):
        if level == n:
            return 0
        if dp[level][last_choice] != -1:
            return dp[level][last_choice]
        ans = 0
        for i in range(len(h[0])):
            if i == last_choice:
                continue
            ans = max(ans, h[level][i] + rec(level+1, i))
        dp[level][last_choice] = ans
        return ans

    print(rec(0, -1))




# Single test case
solve()