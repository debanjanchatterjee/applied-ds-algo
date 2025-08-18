import sys
from collections import Counter



# Fast input reading
input = sys.stdin.read
sys.setrecursionlimit(1 << 25)


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
    n = read_int()
    degree = [0] * (n+1)
    for _ in range(n-1):
        u, v = read_ints()
        degree[u] += 1
        degree[v] += 1

    ans = max(degree) + 1
    print(ans)


solve()