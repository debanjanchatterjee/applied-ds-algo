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

def printf(x):
    sys.stdout.write(x)

def pop_back_s(s):
    return s[:-1]

def print_first_char(s):
    printf(s[0]+'\n')

'''  Maths  '''

def binpow(a,b,mod):
    if b == 0:
        return 1
    if b%2 == 0:
        temp = (a * a) % mod
        return binpow(temp, b //2, mod) % mod
    else:
        return (a*binpow(a,b-1,mod)) % mod


class FenwickTree:
    def __init__(self, size):
        self.N = size + 2
        self.tree = [0] * self.N

    def update(self, index, value):
        while index < self.N:
            self.tree[index] += value
            index += index & -index

    def query(self, index):
        res = 0
        while index > 0:
            res += self.tree[index]
            index -= index & -index
        return res

def is_valid(n, x, y):
    if x < 1 or x > n or y < 1 or y > n:
        return False
    return True


def bfs(n, sx, sy, fx, fy):

    dx = [1,2,2,1,-1,-2,-2,-1]
    dy = [2,1,-1,-2,-2,-1,1,2]

    visited = [[0 for _ in range(n+1)] for _ in range(n+1)]
    dist = [[1e9 for _ in range(n+1)] for _ in range(n+1)]
    q = deque()

    q.append((sx,sy))
    dist[sx][sy] = 0

    while len(q) > 0:
        cur = q.popleft()
        curx = cur[0]
        cury = cur[1]

        if visited[curx][cury] == 1:
            continue
        visited[curx][cury] = 1
        for ddx, ddy in zip(dx, dy):
            nx = curx + ddx
            ny = cury + ddy
            if is_valid(n, nx, ny) and dist[nx][ny] > dist[curx][cury] + 1:
                dist[nx][ny] = dist[curx][cury] + 1
                q.append((nx,ny))

    return dist[fx][fy]


def solve():
    n, sx, sy, fx, fy = read_ints()
    ans = bfs(n, sx, sy, fx, fy)
    if ans < 1e9:
        print(ans)
    else:
        print(-1)


t = read_int()

for _ in range(t):
    solve()


