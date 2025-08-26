
# Problem Statement

## Description
You have a 2-D array of size N x M. Consider connected 0s (which share a common edge) as one single component and 1s as walls. Replace 0s with the size of the connected component but if the size of the component is one, then leave it with 0.

## Input Format
The first line contains a single integer t, the number of test cases.  
For each test case, the first line contains two integers N and M and then there are N lines containing M 0s and 1s, representing a N x M binary matrix.

## Output Format
For each test case, print the final matrix after replacing all the 0s accordingly.

## Constraints
- 1 ≤ Sum of (N x M) over all test cases ≤ 2 x 10^5  
- 0 ≤ Ai ≤ 1

## Sample Input 1
```
2
2 2
0 1
1 0
6 5
1 0 0 1 0
0 1 0 0 0
0 0 1 1 0
0 1 1 0 1
1 1 1 1 1
0 1 0 0 0
```

## Sample Output 1
```
0 1 
1 0 
1 7 7 1 7
4 1 7 7 7
4 4 1 1 7
4 1 1 0 1
1 1 1 1 1
0 1 3 3 3
```

## Note
In the first test case, we have only 2 components and both have size 1. So nothing is replaced.  
In the second test case, we have a total of 5 components of size 7, 4, 3, 1, 1 respectively. So all the 0s are replaced accordingly.
