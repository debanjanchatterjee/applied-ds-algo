# Minimum Colours in Tree Coloring Problem

## Problem Recap
- Given a **tree** with `N` nodes and `N-1` edges.  
- Colour nodes such that:  
  1. No two **adjacent nodes** share the same colour.  
  2. No two **nearly-adjacent nodes** (nodes sharing a common neighbor) share the same colour.  
- Goal: find the **minimum number of colours** required.

---

## Key Observation
Consider a node `v` with **degree d**:

- `v` is adjacent to `d` neighbors → cannot share a colour with them.  
- Each neighbor is nearly-adjacent to all other neighbors → all `d` neighbors must have **different colours**.  
- `v` itself needs **one extra colour** different from all its neighbors.

✅ Locally, for node `v` with degree `d`, we need `d + 1` colours.

---

## Maximum Degree Rule
- The **most restrictive node** is the node with the **highest degree** (`max_degree`).  
- This node determines the minimum number of colours for the entire tree.  

```commandline
Minimum colours required = max_degree + 1
```


---

