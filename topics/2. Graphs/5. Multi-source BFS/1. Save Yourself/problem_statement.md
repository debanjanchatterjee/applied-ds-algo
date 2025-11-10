# Escape the Monsters

## Description
You and some monsters are in a matrix. When taking a step to some direction in the matrix, each monster may simultaneously take one as well. Your goal is to reach one of the boundary squares without ever sharing a square with a monster.

Your task is to find out if your goal is possible, and if it is, print the shortest length of the path that you can follow. Your plan has to work in any situation; even if the monsters know your path beforehand.

---

## Input Format
- The first input line has two integers `n` and `m`: the height and width of the matrix.  
- After this, there are `n` lines of `m` characters describing the matrix.  
- Each character is:
  - `.` (floor)
  - `#` (wall)
  - `A` (start position of the player)
  - `M` (monster position)  

There is exactly one `A` in the input.

---

## Output Format
- Print **"YES"** if your goal is possible, and **"NO"** otherwise.  
- If your goal is possible, also print the length of the shortest path that you'll follow.

---

## Constraints
```
1 ≤ n, m ≤ 1000
```

---

## Sample Input 1
```
5 8
########
#M..A..#
#.#.M#.#
#M#..#..
#.######
```

### Sample Output 1
```
YES
5
```

---

## Sample Input 2
```
1 3
##A
```

### Sample Output 2
```
YES
0
```

---

## Sample Input 3
```
3 3
###
#A#
#M.
```

### Sample Output 3
```
NO
```

---

## Note
- For the first sample, the person can reach a boundary cell in **5** steps before any monster can reach that cell.  
- For the second sample, the person is already on a boundary cell, so the shortest path length is **0**.  
- For the third sample, the person cannot reach any boundary safely.
