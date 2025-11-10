# Problem Description

Among the sequences **P** that are permutations of **(1, 2, …, N)** and satisfy the condition below, find the lexicographically smallest sequence.

For each **i = 1, …, M**, **Ai** appears earlier than **Bi** in **P**.

If there is no such **P**, print **-1**.

---

## Input Format
Input is given from Standard Input in the following format:

```
N M
A1 B1
:
AM BM
```

---

## Output Format
Print the answer.  
If there is no valid permutation, print **-1**.

---

## Constraints
- 2 ≤ N ≤ 2 × 10^5  
- 1 ≤ M ≤ 2 × 10^5  
- 1 ≤ Ai, Bi ≤ N  
- Ai ≠ Bi  
- All values in input are integers.

---

## Sample Input 1

```
4 3
2 1
3 4
2 4
```

## Sample Output 1

```
2 1 3 4
```

## Sample Input 2

```
2 3
1 2
1 2
2 1
```

## Sample Output 2

```
-1
```


---

## Note
- In the first sample, a valid topological ordering that is lexicographically smallest is `[2, 1, 3, 4]` because all constraints are satisfied and `2` is the smallest available vertex at the start.  
- In the second sample, there is a cycle so no valid permutation exists, hence `-1` is printed.