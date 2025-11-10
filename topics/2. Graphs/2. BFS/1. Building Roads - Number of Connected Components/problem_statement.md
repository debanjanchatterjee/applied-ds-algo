# Minimum Roads to Connect Cities

## Problem Description
Zenithland has **n cities** and **m roads** between them. The goal is to **construct new roads** so that there is a route between **any two cities**.  
- A road is **bidirectional**.  
- Your task is to find out the **minimum number of roads required**.

---

## Input Format
- The first line contains two integers `n` and `m`: the number of cities and roads. The cities are numbered `1, 2, …, n`.  
- The next `m` lines describe the roads. Each line has two integers `a` and `b`, representing a road between cities `a` and `b`.  

**Notes:**  
- A road always connects two **different cities**.  
- There is at most **one road between any two cities**.

---

## Output Format
Print **one integer** — the minimum number of roads required.

---

## Constraints
- `1 ≤ n ≤ 10^5`  
- `1 ≤ m ≤ 2 × 10^5`  
- `1 ≤ a, b ≤ n`  

---

## Sample Input 1

```
4 2
1 2
3 4
```

## Sample Output 1

```
1
```

---

## Note
Construct a road between cities `1` and `3` to make all cities connected.