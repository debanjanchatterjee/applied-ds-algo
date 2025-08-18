// For AZ submission

#include <bits/stdc++.h>
using namespace std;

int n, m;
vector<string> g;
vector<vector<int>> visited;
int dx[4] = {1, 0, -1, 0};
int dy[4] = {0, -1, 0, 1};

bool is_valid(int x, int y) {
    return x >= 0 && y >= 0 && x < n && y < m && g[x][y] == '.';
}

void dfs(int x, int y) {
    visited[x][y] = 1;
    for (int k = 0; k < 4; ++k) {
        int nx = x + dx[k];
        int ny = y + dy[k];
        if (is_valid(nx, ny) && !visited[nx][ny]) {
            dfs(nx, ny);
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> n >> m;
    g.resize(n);
    visited.assign(n, vector<int>(m, 0));
    for (int i = 0; i < n; ++i) {
        cin >> g[i];
    }

    int ans = 0;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            if (g[i][j] == '.' && !visited[i][j]) {
                ++ans;
                dfs(i, j);
            }
        }
    }

    cout << ans << "\n";
    return 0;
}