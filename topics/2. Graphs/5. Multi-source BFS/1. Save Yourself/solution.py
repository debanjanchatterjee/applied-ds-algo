import sys
from sys import stdin, stdout
from collections import deque

def main():
    data = stdin.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1

    mod = 10**9 + 7
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    grid = [[False]*m for _ in range(n)]
    distA = [[-1]*m for _ in range(n)]
    distMon = [[-1]*m for _ in range(n)]
    parx = [[-2]*m for _ in range(n)]
    pary = [[-2]*m for _ in range(n)]

    monsterOcc = deque()
    AOcc = deque()

    for i in range(n):
        s = data[idx]; idx += 1
        for j in range(m):
            grid[i][j] = True
            if s[j] == '#':
                grid[i][j] = False
            elif s[j] == 'M':
                distMon[i][j] = 0
                monsterOcc.append((i, j))
            elif s[j] == 'A':
                distA[i][j] = 0
                AOcc.append((i, j))
                parx[i][j] = -1
                pary[i][j] = -1

    while monsterOcc:
        x, y = monsterOcc.popleft()
        for i in range(4):
            xx = x + dx[i]; yy = y + dy[i]
            if xx < 0 or xx >= n or yy < 0 or yy >= m:
                continue
            if grid[xx][yy] and distMon[xx][yy] == -1:
                distMon[xx][yy] = distMon[x][y] + 1
                monsterOcc.append((xx, yy))

    while AOcc:
        x, y = AOcc.popleft()
        for i in range(4):
            xx = x + dx[i]; yy = y + dy[i]
            if xx < 0 or xx >= n or yy < 0 or yy >= m:
                continue
            if grid[xx][yy] and distA[xx][yy] == -1:
                distA[xx][yy] = distA[x][y] + 1
                AOcc.append((xx, yy))
                parx[xx][yy] = x
                pary[xx][yy] = y

    finx = -1; finy = -1; findist = 10**9

    for i in range(n):
        if grid[i][0] and distA[i][0] >= 0 and (distA[i][0] < distMon[i][0] or distMon[i][0] == -1):
            finx = i; finy = 0; findist = min(findist, distA[i][0])
        if grid[i][m-1] and distA[i][m-1] >= 0 and (distA[i][m-1] < distMon[i][m-1] or distMon[i][m-1] == -1):
            finx = i; finy = m-1; findist = min(findist, distA[i][m-1])

    for i in range(m):
        if grid[0][i] and distA[0][i] >= 0 and (distA[0][i] < distMon[0][i] or distMon[0][i] == -1):
            finx = 0; finy = i; findist = min(findist, distA[0][i])
        if grid[n-1][i] and distA[n-1][i] >= 0 and (distA[n-1][i] < distMon[n-1][i] or distMon[n-1][i] == -1):
            finx = n-1; finy = i; findist = min(findist, distA[n-1][i])

    if finx == -1:
        stdout.write("NO\n")
    else:
        stdout.write("YES\n")
        stdout.write(str(findist) + "\n")
        # /*****************************************
        # ----PRINTING PATH---
        # string path = "";
        # int x = finx, y = finy;
        # while(true) {
        #     int prex = par[x][y].first;
        #     int prey = par[x][y].second;
        #     if(prex == -1 && prey == -1) break;
        #     if(y - prey == 1) path += 'R';
        #     else if(y - prey == -1) path += 'L';
        #     else if(x - prex == 1) path += 'D';
        #     else path += 'U';
        #     x = prex; y = prey;
        # }
        # reverse(path.begin(), path.end());
        # cout << path << "\n";
        # ******************************************/

if __name__ == "__main__":
    main()
