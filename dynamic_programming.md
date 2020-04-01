## dynamic_programming

### [dynamic_programming.**kadane**(*arr*, *func*)](/dynamic_programming.py)

Solve a dynamic programming problem with input `arr` using a generalized form of Kadane's algorithm. `func` can either be a function in the form of `lambda i, x: [function]` or one of the following built-in algorithms:

* `kadane`: Kadane's algorithm
* `house_robber`: algorithm to solve the [house robber](https://leetcode.com/problems/house-robber) problem

`k` isn't needed if a built-in `func` is used, unless you want to override it.

[Maximum Subarray](https://leetcode.com/problems/maximum-subarray)
```python
def maxSubArray(nums):
    return kadane(nums, func='max_subarray')
```

[House Robber](https://leetcode.com/problems/house-robber)
```python
def rob(nums):
    return kadane(nums, func='house_robber')
```

[House Robber II](https://leetcode.com/problems/house-robber-ii)
```python
def rob(nums):
    r = kadane(nums, func='house_robber')
    return max(r(nums[:-1]), r(nums[1:]))
```

[Maximum Sum Circular Subarray](https://leetcode.com/problems/maximum-sum-circular-subarray)
```python
def maxSubarraySumCircular(A):
    max_sum = kadane(A, func='max_subarray')
    return max(max_sum, sum(A) + kadane([-x for x in A], func='max_subarray')
    ) if max_sum > 0 else max_sum
```

### [dynamic_programming.**max_profit**(*prices*, *k=float('inf')*)](/dynamic_programming.py)

Solve [Best Time to Buy and Sell Stock IV](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv).

[Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock)
```python
def maxProfit(prices):
    return max_profit(prices, k=1)
```

[Best Time to Buy and Sell Stock II](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii)
```python
def maxProfit(prices):
    return max_profit(prices)
```

[Best Time to Buy and Sell Stock III](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii)
```python
def maxProfit(prices):
    return max_profit(prices, k=2)
```

[Best Time to Buy and Sell Stock IV](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv)
```python
def maxProfit(k, prices):
    return max_profit(prices, k=k)
```

### [dynamic_programming.**single_number**(*arr*, *k=2*)](/dynamic_programming.py)

Solve the problem:

> Given a non-empty array `arr` of integers, every element appears `k` times except for one, which appears exactly once. Find that single one.

[Single Number](https://leetcode.com/problems/single-number)
```python
def singleNumber(nums):
    return single_number(nums)
```

[Single Number II](https://leetcode.com/problems/single-number-ii)
```python
def singleNumber(nums):
    return single_number(nums, k=3)
```

[Single Number III](https://leetcode.com/problems/single-number-iii)
```python
import functools
def singleNumber(nums):
    mask = single_number(nums)
    mask &= -mask
    x = y = 0
    for num in nums:
        if num & mask:
            x ^= num
        else:
            y ^= num
    return x, y
```

### [dynamic_programming.**wagner_fischer**(*matrix*, *base*, *left*, *top*, *each_cell*)](/dynamic_programming.py)

Solve a dynamic programming problem with input `matrix` using a generalized form of the Wagner-Fischer algorithm by doing the following steps:

1. Fill the top-left cell with `base`.
1. Update the top row with `top`, where `top` is a function in the form of `lambda j: [function]` and `j` is the column number.
1. For each subsequent row:
    * Update the left-most cell with `left`, where `left` is a function in the form of `lambda i: [function]` and `i` is the row number.
    * Update the subsequent cells with `each_cell`, where `each_cell` is a function in the form of `lambda i, j: [function]`.

Note that this function modifies `matrix` in-place.

[Unique Paths II](https://leetcode.com/problems/unique-paths-ii)
```python
def uniquePathsWithObstacles(obstacleGrid):
    wagner_fischer(obstacleGrid, 1^obstacleGrid[0][0],
        lambda i: (1^obstacleGrid[i][0]) * obstacleGrid[i - 1][0],
        lambda j: (1^obstacleGrid[0][j]) * obstacleGrid[0][j - 1],
        lambda i, j: (1^obstacleGrid[i][j]) * (obstacleGrid[i - 1][j]
            + obstacleGrid[i][j - 1]
        )
    )
    return obstacleGrid[-1][-1]
```

[Minimum Path Sum](https://leetcode.com/problems/minimum-path-sum)
```python
def minPathSum(grid):
    wagner_fischer(grid, grid[0][0],
        lambda i: grid[i - 1][0] + grid[i][0],
        lambda j: grid[0][j - 1] + grid[0][j],
        lambda i, j: min(grid[i - 1][j], grid[i][j - 1]) + grid[i][j]
    )
    return grid[-1][-1]
```

[Triangle](https://leetcode.com/problems/triangle)
```python
def minimumTotal(triangle):

    def each_cell(i, j):
        row = i - 1
        previous = triangle[row][j - 1]
        if i > j:
            increment = min(previous, triangle[row][j])
        else:
            increment = previous
        return triangle[i][j] + increment

    wagner_fischer(triangle, triangle[0][0],
        lambda i: triangle[i - 1][0] + triangle[i][0],
        lambda j: triangle[0][0], each_cell
    )
    return min(triangle[-1])
```

[Maximal Square](https://leetcode.com/problems/maximal-square)
```python
def maximalSquare(matrix):
    wagner_fischer(matrix, int(matrix[0][0]), lambda i: int(matrix[i][0]),
        lambda j: int(matrix[0][j]),
        lambda i, j: min(matrix[i - 1][j - 1], matrix[i - 1][j],
            matrix[i][j - 1]
        ) + 1 if matrix[i][j] == '1' else 0
    )
    return max(map(max, matrix))**2 if matrix else 0
```

[Largest 1-Bordered Square](https://leetcode.com/problems/largest-1-bordered-square)
```python
def largest1BorderedSquare(grid):
    n, m = len(grid), len(grid[0])
    r = range(n)
    horizontal, vertical = [[0]*m for i in r], [[0]*m for i in r]
    hor_each_cell = lambda i, j: grid[i][j] * (horizontal[i][j - 1] + 1)
    vert_each_cell = lambda i, j: grid[i][j] * (vertical[i - 1][j] + 1)
    wagner_fischer(horizontal, grid[0][0], lambda i: hor_each_cell(i, 0),
        lambda j: grid[0][j], hor_each_cell
    )
    wagner_fischer(vertical, grid[0][0], lambda i: grid[i][0],
        lambda j: vert_each_cell(0, j), vert_each_cell
    )
    side_len = 0
    for i in reversed(range(n)):
        for j in reversed(range(m)):
            k = min(horizontal[i][j], vertical[i][j])
            while k >= side_len:
                if min(horizontal[i - k + 1][j], vertical[i][j - k + 1]) >= k:
                    side_len = k
                k -= 1
    return side_len**2
```

[Count Square Submatrices with All Ones](https://leetcode.com/problems/count-square-submatrices-with-all-ones)
```python
def countSquares(matrix):
    wagner_fischer(matrix, 0, lambda i: matrix[i][0], lambda j: matrix[0][j],
        lambda i, j: matrix[i][j]*min(matrix[i - 1][j - 1], matrix[i - 1][j],
            matrix[i][j - 1]
        ) + 1
    )
    return sum(map(sum, matrix))
```

### [dynamic_programming.**construct_prefix_sum**(*matrix*)](/dynamic_programming.py)

Construct a matrix where each cell `(i, j)` is the prefix sum of submatrix `matrix[:i][:j]`.

[Range Sum Query 2D - Immutable](https://leetcode.com/problems/range-sum-query-2d-immutable)
```python
class NumMatrix:

    def __init__(self, matrix):
        self.prefix_sum = construct_prefix_sum(matrix)

    def sumRegion(self, row1, col1, row2, col2):
        return range_sum(self.prefix_sum, row1, row2 + 1, col1, col2 + 1)
```

### [dynamic_programming.**range_sum**(*prefix_sum*, *r1*, *c1*, *r2*, *c2*)]

Given a matrix `prefix_sum`, which is the prefix sum matrix of some matrix *M*, return the sum of values in submatrix `M[r1:r2][c1:c2]`.

[Matrix Block Sum](https://leetcode.com/problems/matrix-block-sum)
```python
def matrixBlockSum(mat, K):

    def each_cell(i, j):
        return range_sum(prefix_sum, max(i - K, 0), min(i + K + 1, m),
            max(j - K, 0), min(j + K + 1, n)
        )
    
    n, m = len(mat), len(mat[0])
    prefix_sum = construct_prefix_sum(mat)
    answer = [[0]*m for i in range(n)]
    wagner_fischer(answer, each_cell(0, 0), lambda i: each_cell(i, 0),
        lambda j: each_cell(0, j), each_cell
    )
    return answer
```

### [dynamic_programming.**hirschberg**(*x*, *y*, *base*, *left*, *top*, *each_cell*, *flexible=True*)](/dynamic_programming.py)

Solve a dynamic programming problem with inputs `x` and `y` using a generalized form of Hirschberg's algorithm by doing the following steps:

1. Fill the top-left cell with `base`.
1. Fill the top row with `top`, where `top` is a function in the form of `lambda x, y, j: [function]` and `j` is the column number.
1. For each subsequent row:
    * Fill the left-most cell with `left`, where `left` is a function in the form of `lambda x, y, i: [function]` and `i` is the row number.
    * Fill the subsequent cells with `each_cell`, where `each_cell` is a function in the form of `lambda x, y, i, j: [function]`.
1. Return the bottom-right cell.

If `flexible` is `True`, `x` and `y` will be swapped as needed to minimize memory usage. If `flexible` is `False`, `x` and `y` won't be swapped and your problem will be treated as a knapsack problem where `x` is the list of items, `y` is `range(capacity + 1)`, and `capacity` is how much weight the knapsack can hold.

[Edit Distance](https://leetcode.com/problems/edit-distance)
```python
def minDistance(word1, word2):
    if word1 and word2:
        return hirschberg(word1, word2, int(word1[0] != word2[0]),
            lambda dp, x, y, i: max(dp[0][0] + int(x[i] != y[0]), i),
            lambda dp, x, y, j: max(dp[0][j - 1] + int(x[0] != y[j]), j),
            lambda dp, x, y, i, j: min(dp[0][j - 1], dp[0][j], dp[1][j - 1]
                ) + 1 if x[i] != y[j] else dp[0][j - 1]
            )
    return len(word1 + word2)
```

[Minimum ASCII Delete Sum for Two Strings](https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings)
```python
def minimumDeleteSum(s1, s2):
    return sum(map(ord, s1 + s2)) - 2*hirschberg(s1, s2,
        ord(s1[0])*(s1[0] == s2[0]),
        lambda dp, x, y, i: dp[0][0] if x[i] != y[0] else ord(x[i]),
        lambda dp, x, y, j: dp[0][j - 1] if x[0] != y[j] else ord(y[j]),
        lambda dp, x, y, i, j: max(dp[0][j],
            dp[1][j - 1]) if x[i] != y[j] else dp[0][j - 1] + ord(x[i])
    )
```

### [dynamic_programming.**lcs**(*x*, *y*)](/dynamic_programming.py)

Find the length of the longest common subsequence of `x` and `y`.

[Delete Operation for Two Strings](https://leetcode.com/problems/delete-operation-for-two-strings)
```python
def minDistance(word1, word2):
    return len(word1 + word2) - lcs(word1, word2)
```
[Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence)
```python
def longestCommonSubsequence(text1, text2):
    return lcs(text1, text2)
```

### [dynamic_programming.**lps**(*s*)](/dynamic_programming.py)

Find the length of the longest palindromic subsequence of `s`.

[Longest Palindromic Subsequence](https://leetcode.com/problems/longest-palindromic-subsequence)
```python
def longestPalindromeSubseq(s):
    return lps(s)
```

[Minimum Insertion Steps to Make String a Palindrome](https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome)
```python
def minInsertions(s):
    return len(s) - lps(s)
```