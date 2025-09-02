# Problem Statement: Game Levels and Teleporters

## Description
You are playing a game that has `n` levels connected by `m` teleporters. Your task is to get from level `1` to level `n`.  

The game is designed such that the underlying graph has **no directed cycles**. You need to determine the number of distinct ways to complete the game, starting at level `1` and ending at level `n`.

Since the number of ways can be very large, output the result **modulo 10^9 + 7**.

---

## Input Format
- The first line contains two integers `n` and `m`:  
  - `n` = number of levels (`1 ≤ n ≤ 10^5`)  
  - `m` = number of teleporters (`1 ≤ m ≤ 2 × 10^5`)  
- The next `m` lines each contain two integers `a` and `b` (`1 ≤ a, b ≤ n`):  
  - indicating that there is a teleporter from level `a` to level `b`.

---

## Output Format
- Print a single integer: the number of ways to go from level `1` to level `n`, modulo `10^9 + 7`.

---

## Constraints
- `1 ≤ n ≤ 10^5`  
- `1 ≤ m ≤ 2 × 10^5`  
- `1 ≤ a, b ≤ n`  
- The graph is a **DAG** (Directed Acyclic Graph).

---

## Sample Input 1

```
4 5
1 2
2 4
1 3
3 4
1 4
```

## Sample Output 1

```
3
```

---

## Explanation
There are three distinct paths from level `1` to level `4`:
1. `1 → 4`  
2. `1 → 2 → 4`  
3. `1 → 3 → 4`

Thus, the answer is **3**.

