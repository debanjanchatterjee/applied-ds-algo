# Kahn's Algorithm for Topological Sorting

## Idea
Kahn's algorithm is a popular algorithm for **topological sorting** of directed acyclic graphs (DAGs).  
The algorithm relies on the concept of **indegrees**, where the indegree of a vertex is the number of edges directed **into** that vertex.

---

## Algorithm Steps
1. Compute the indegree of each vertex in the graph.  
2. Initialize a queue and enqueue all vertices with an indegree of `0`.  
3. Dequeue a vertex, output it, and reduce the indegree of its neighbors.  
4. If any neighbor’s indegree becomes `0`, enqueue it.  
5. Repeat steps 3–4 until the queue is empty.  

---

## BFS Code for Topological Sorting using Kahn's Algorithm

```cpp
#include <bits/stdc++.h>
using namespace std;

vector<vector<int>> g;
vector<int> indegree;

void kahnTopologicalSort(int vertices) {
    queue<int> q;

    // Enqueue all vertices with indegree 0
    for (int i = 0; i < vertices; ++i) {
        if (indegree[i] == 0) {
            q.push(i);
        }
    }

    while (!q.empty()) {
        int current = q.front();
        q.pop();

        cout << current << " ";

        for (int neighbor : g[current]) {
            indegree[neighbor]--;
            if (indegree[neighbor] == 0) {
                q.push(neighbor);
            }
        }
    }
}

int main() {
    int n, m;
    cin >> n >> m;

    g.resize(n);
    indegree.assign(n, 0);

    for (int i = 0; i < m; ++i) {
        int l, r;
        cin >> l >> r;
        g[l].push_back(r);
        indegree[r]++;
    }

    cout << "Topological Sorting Order: ";
    kahnTopologicalSort(n);

    return 0;
}
```

## Time Complexity
- Kahn’s algorithm has a time complexity of **O(V + E)**, where:  
  - `V` = number of vertices  
  - `E` = number of edges  
- **Reason**:  
  - Each vertex is enqueued/dequeued once.  
  - Each edge is considered once when reducing indegrees.  
  - Indegree computation takes **O(V + E)**, and the BFS-like traversal also takes **O(V + E)**.  

---

## Note
- If you want to obtain the **lexicographically smallest topological sort**, use a **priority queue** instead of a regular queue in Kahn’s algorithm.  
- The priority queue ensures that vertices with the **smallest indices** are processed first.  
- This guarantees the **smallest possible topological order**.  
