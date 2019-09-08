## Dynamic Programming
### Longest Common Subsequence
Given two sequences *x* and *y*, return the length of the longest common subsequence.
```python
def longest_common_subsequence(x, y):
    n, m = map(len, (x, y))
    if not n or not m: return 0
    dp = [[0 for j in range(m)] for i in range(n)]
    dp[0][0], r, q = int(x[0] == y[0]), range(1, n), range(1, m)
    for i in r: dp[i][0] = max(dp[i - 1][0], int(x[i] == y[0]))
    for j in q: dp[0][j] = max(dp[0][j - 1], int(x[0] == y[j]))
    for i in r:
        a = i - 1
        for j in q:
            b = j - 1
            dp[i][j] = max(dp[a][j], dp[i][b], dp[a][b] + int(x[i] == y[j]))
    return dp[-1][-1]
```
### Knapsack Problem
You're given a set of items, each with a weight and value. Determine the maximum value of items you may put in a knapsack that has a maximum weight limit, or capacity.
```python
def knapsack(values, weights, capacity):
    n = len(values)
    r, q = map(range, (n, capacity + 1))
    dp = [[0 for j in q] for i in r]
    for i in r:
        a = i - 1
        for j in q: dp[i][j] = dp[a][j] if weights[i] > j else max(dp[a][j], dp[a][j - weights[i]] + values[i])
    return dp[-1][-1]
```
### Matrix Chain Multiplicaion
You're given a list of matrix dimensions. For example, `dimensions = [22, 17, 68, 3, 88, 59, 54, 23, 22, 77]` means you have a 22 × 17 matrix, a 17 × 68 matrix, a 68 × 3 matrix, a 3 × 88 matrix, an 88 × 59 matrix, a 59 × 54 matrix, a 54 × 23 matrix, a 23 × 22 matrix, and a 22 × 77 matrix. Find the least number of operations needed to multiply these matrices.
```python
def matrix_chain_multiplication(dimensions):
    n = len(dimensions)
    r = range(n)
    dp = [[float('inf') for j in r] for i in r]
    for i in range(1, n): dp[i][i] = 0
    for length in range(2, n):
        for i in range(n - length + 1):
            j = i + length - 1
            for k in range(i, j):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j] + dimensions[i - 1]*dimensions[j]*dimensions[k])
    return dp[1][-1]
```