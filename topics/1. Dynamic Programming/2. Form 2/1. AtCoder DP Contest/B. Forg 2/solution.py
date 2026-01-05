import sys
from collections import Counter

# Fast input reading
input = sys.stdin.readline
sys.setrecursionlimit(1 << 25)

dp = []
h = []
k = 0
def read_int():
    return int(input())

def read_ints():
    return map(int, sys.stdin.readline().strip().split())

def read_list():
    return list(map(int, sys.stdin.readline().strip().split()))

def rec(level):
    global k, h, dp
    if level < 0:
        return int(1e9)
    if level == 0:
        return 0

    if dp[level] != -1:
        return dp[level]
    ans = int(1e9)
    for i in range(1,k+1):
        ans = min(ans, rec(level-i) + abs(h[level]-h[level-i]))
    dp[level] = ans
    return ans

def solve():
    global k, h, dp
    n, k = read_ints()
    h = read_list()
    dp = [-1]*(n+1)
    print(rec(n-1))




# Single test case
solve()