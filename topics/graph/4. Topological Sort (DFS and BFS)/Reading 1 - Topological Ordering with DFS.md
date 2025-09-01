# Topological Sorting

## Directed Acyclic Graphs (DAGs)

### Definition
A **Directed Acyclic Graph (DAG)** is a graph that is:
- **Directed**: edges have a direction.
- **Acyclic**: contains no cycles.

In other words, there is no sequence of vertices such that the first vertex is the same as the last, and the edges follow their prescribed direction.

### Properties
- DAGs are often used to model relationships with a **temporal or hierarchical nature**.
- Common in **scheduling problems** where tasks must be executed in a specific order.
- Useful for representing **dependencies** between elements in various systems.

---

## Topological Sorting

### Definition
Topological sorting is an ordering of the vertices of a **directed acyclic graph (DAG)** such that for every directed edge `(u, v)`, vertex `u` comes **before** vertex `v` in the ordering.

In simpler terms, it's a **linear ordering** of the vertices that respects the partial order defined by the edges.

### Uniqueness
- Topological sorting is **not unique**.  
- A graph can have multiple valid topological orderings.  
- This flexibility allows for different valid sequences of tasks or events that respect the directed dependencies in the graph.

---

## DFS Code for Topological Sorting

```cpp
#include <bits/stdc++.h>
using namespace std;

vector<vector<int>> g;
vector<int> vis;
int n, m;
vector<int> topo;

void dfs_topo(int node)
{
    vis[node] = 1;
    for (auto v : g[node])
    {
        if (!vis[v])
        {
            dfs_topo(v);
        }
    }
    topo.push_back(node);
}

int main()
{
    cin >> n >> m;
    g.resize(n + 1);
    vis.assign(n + 1, 0);

    for (int i = 0; i < m; i++)
    {
        int l, r;
        cin >> l >> r;
        g[l].push_back(r);
    }

    for (int i = 1; i <= n; i++)
    {
        if (!vis[i])
        {
            dfs_topo(i);
        }
    }
    reverse(topo.begin(), topo.end());

    for (int i = 0; i < topo.size(); i++)
    {
        cout << topo[i] << " ";
    }
}
```

## Why It Works
- The **depth-first search (DFS)** approach is crucial for topological sorting.
- By visiting each vertex and exploring as deeply as possible before backtracking, the algorithm ensures that a vertex is added to the stack only after all its dependencies have been explored.
- The stack, when reversed, provides a valid topological ordering of the vertices.

---

## Time Complexity
- The time complexity of the topological sorting algorithm is **O(V + E)**, where:  
  - `V` = number of vertices  
  - `E` = number of edges  
- This arises because each vertex and each edge is visited **once** during the DFS traversal.

