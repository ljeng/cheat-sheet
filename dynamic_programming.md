## dynamic_programming

[dynamic_programming.**kadane**(*arr*, *start*, *var*, *func*, *i*)](/dynamic_programming.py)

Solves a dynamic programming problem with input `arr` using a generalized form of Kadane's algorithm by doing the following steps:

1. Iterate through `arr` starting from index `start`. For each iteration do:
    * For each index `j` in `range(len(var))`, apply `func[j]` to `var[j]`.
1. Return `var[i]`.

Examples:

[Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)
```python
def maxSubArray(nums):
    return kadane(nums,
        1,
        [nums[0], nums[0]],
        [lambda i, x: nums[i] + max(x[0], 0), lambda i, x: max(x)],
        1
    )
```

[Decode Ways](https://leetcode.com/problems/decode-ways)
```python
def numDecodings(s):
    return kadane(s,
        0,
        [0, 0, int(bool(s)), ''],
        [lambda i, x: x[1],
            lambda i, x: x[2],
            lambda i, x: (s[i] > '0')*x[2] + (0 < int(x[3] + s[i]) <= 26)*x[0],
            lambda i, x: s[i]
        ],
        2
    )
```

[Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)
```python
def maxProfit(prices):
    return kadane(prices,
        1,
        [0, 0],
        [lambda i, x: max(x[0] + prices[i] - prices[i - 1], 0),
            lambda i, x: max(x)
        ],
        1
    )
```

[Best Time to Buy and Sell Stock III](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii)
```python
def maxProfit(prices):
    return kadane(prices,
        0,
        [0, -float('inf'), 0, -float('inf')],
        [lambda i, x: max(x[0], x[1] + prices[i]),
            lambda i, x: max(x[1], x[2] - prices[i]),
            lambda i, x: max(x[2], x[3] + prices[i]),
            lambda i, x: max(x[3], -prices[i])
        ],
        0
    )
```

[Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray)
```python
def maxProduct(nums):
    return kadane(nums,
        1,
        [0, 0, nums[0], nums[0], nums[0]],
        [lambda i, x: max(max(nums[i]*x[3], nums[i]*x[4]), nums[i]),
            lambda i, x: min(min(nums[i]*x[3], nums[i]*x[4]), nums[i]),
            lambda i, x: max(x[0], x[2]),
            lambda i, x: x[0],
            lambda i, x: x[1]
        ],
        2
    ) if nums else 0
```

[House Robber](https://leetcode.com/problems/house-robber/)
```python
def rob(nums):
    return kadane(nums,
        0,
        [0, 0, 0],
        [lambda i, x: x[1],
            lambda i, x: max(x[1], nums[i] + x[2]),
            lambda i, x: x[0]
        ],
        1
    )
```

[House Robber II](https://leetcode.com/problems/house-robber-ii)
```python
def rob(nums):
    def rob1(start):
        return kadane(nums,
            start,
            [0, 0, 0],
            [lambda i, x: x[1],
                    lambda i, x: max(x[1], nums[i] + x[2]),
                    lambda i, x: x[0]
                ],
        1)
    money = rob1(1)
    nums.pop()
    return max(money, rob1(0))
```

```python
def maxProfit(prices):
    return kadane(prices,
        1,
        [0, -prices[0], 0, 0],
        [lambda i, x: x[1],
            lambda i, x: max(x[2] - prices[i], x[0]),
            lambda i, x: x[3],
            lambda i, x: max(x[0] + prices[i], x[2])
        ],
        3
    ) if prices else 0
```

[dynamic_programming.**wagner_fischer**(*matrix*, *initial*, *left*, *top*, *each_cell*)](/dynamic_programming.py)

Solves a dynamic programming problem with input `matrix` using a generalized form of the Wagner-Fischer algorithm by doing the following steps:

1. Fill the top-left cell with `initial`.
1. Update the top row with `top`, where `top` is a function in the form of `lambda j: [function]` and `j` is the column number.
1. For each subsequent row:
    * Update the left-most cell with `left`, where `left` is a function in the form of `lambda i: [function]` and `i` is the row number.
    * Update the subsequent cells with `each_cell`, where `each_cell` is a function in the form of `lambda i, j: [function]`.

Note that this function modifies `matrix` in-place.

Examples:

[Unique Paths II](https://leetcode.com/problems/unique-paths-ii)
```python
def uniquePathsWithObstacles(obstacleGrid):
    wagner_fischer(obstacleGrid,
        1^obstacleGrid[0][0],
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
    wagner_fischer(grid,
        grid[0][0],
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
        if i > j: increment = min(previous, triangle[row][j])
        else: increment = previous
        return triangle[i][j] + increment

    wagner_fischer(triangle,
        triangle[0][0],
        lambda i: triangle[i - 1][0] + triangle[i][0],
        lambda j: triangle[0][0],
        each_cell
    )
    return min(triangle[-1])
```

[Maximal Square](https://leetcode.com/problems/maximal-square/)
```python
def maximalSquare(matrix):
    wagner_fischer(matrix,
        int(matrix[0][0]),
        lambda i: int(matrix[i][0]),
        lambda j: int(matrix[0][j]),
        lambda i, j: min(matrix[i - 1][j - 1],
            matrix[i - 1][j],
            matrix[i][j - 1]
        ) + 1 if matrix[i][j] == '1' else 0
    )
    return max(map(max, matrix))**2 if matrix else 0
```
[Range Sum Query 2D - Immutable](https://leetcode.com/problems/range-sum-query-2d-immutable)
```python
class NumMatrix:

    def __init__(self, matrix):
        n, m = len(matrix), len(matrix[0])
        self.prefix_sum = [[0] * (m+1) for i in range(n + 1)]
        wagner_fischer(self.prefix_sum,
            0,
            lambda i: 0,
            lambda j: 0,
            lambda i, j: (
                matrix[i - 1][j - 1]
                - self.prefix_sum[i - 1][j - 1]
                + self.prefix_sum[i - 1][j]
                + self.prefix_sum[i][j - 1]
            )
        )

    def sumRegion(self, row1, col1, row2, col2):
        return (self.prefix_sum[row1][col1]
            - self.prefix_sum[row1][col2 + 1]
            - self.prefix_sum[row2 + 1][col1]
            + self.prefix_sum[row2 + 1][col2 + 1]
        )
```

[Largest 1-Bordered Square](https://leetcode.com/problems/largest-1-bordered-square)
```python
def largest1BorderedSquare(grid):
    n, m = len(grid), len(grid[0])
    r = range(n)
    horizontal, vertical = [[0]*m for i in r], [[0]*m for i in r]
    hor_each_cell = lambda i, j: grid[i][j] * (horizontal[i][j - 1] + 1)
    vert_each_cell = lambda i, j: grid[i][j] * (vertical[i - 1][j] + 1)
    wagner_fischer(horizontal,
        grid[0][0],
        lambda i: hor_each_cell(i, 0),
        lambda j: grid[0][j],
        hor_each_cell
    )
    wagner_fischer(
        vertical,
        grid[0][0],
        lambda i: grid[i][0],
        lambda j: vert_each_cell(0, j),
        vert_each_cell
    )
    side_len = 0
    for i in range(n - 1, -1, -1):
        for j in range(m - 1, -1, -1):
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
    wagner_fischer(matrix,
        0,
        lambda i: matrix[i][0],
        lambda j: matrix[0][j],
        lambda i, j: matrix[i][j]*min(matrix[i - 1][j - 1]
            matrix[i - 1][j],
            matrix[i][j - 1])
        + 1
    )
    return sum(map(sum, matrix))
```

[Matrix Block Sum](https://leetcode.com/problems/matrix-block-sum)
```python
def matrixBlockSum(mat, K):

    def each_cell(i, j):
        r1 = max(i - K, 0)
        c1 = max(j - K, 0)
        r2 = min(i + K + 1, m)
        c2 = min(j + K + 1, n)
        return (prefix_sum[r1][c1]
            - prefix_sum[r1][c2]
            - prefix_sum[r2][c1]
            + prefix_sum[r2][c2])

    n, m = len(mat), len(mat[0])
    prefix_sum = [[0]*(m+1) for i in range(n + 1)]
    wagner_fischer(prefix_sum,
        0,
        lambda i: 0,
        lambda j: 0,
        lambda i, j: (mat[i - 1][j - 1]
            - prefix_sum[i - 1][j - 1]
            + prefix_sum[i - 1][j]
            + prefix_sum[i][j - 1]
        )
    )
    answer = [[0]*m for i in range(n)]
    wagner_fischer(answer,
        each_cell(0, 0),
        lambda i: each_cell(i, 0),
        lambda j: each_cell(0, j),
        each_cell)
    return answer
```

[dynamic_programming.**hirschberg**(*x*, *y*, *initial*, *left*, *top*, *each_cell*)](/dynamic_programming.py)

Solves a dynamic programming problem with inputs `x` and `y` using a generalized form of Hirschberg's algorithm by doing the following steps:

1. Fill the top-left cell with `initial`.
1. Fill the top row with `top`, where `top` is a function in the form of `lambda x, y, j: [function]` and `j` is the column number.
1. For each subsequent row:
    * Fill the left-most cell with `left`, where `left` is a function in the form of `lambda x, y, i: [function]` and `i` is the row number.
    * Fill the subsequent cells with `each_cell`, where `each_cell` is a function in the form of `lambda x, y, i, j: [function]`.
1. Return the bottom-right cell.

Examples:

[Edit Distance](https://leetcode.com/problems/edit-distance)
```python
def minDistance(word1, word2):
    if word1 and word2:
        return hirschberg(word1,
            word2,
            int(word1[0] != word2[0]),
            lambda dp, x, y, i: max(dp[0][0] + int(x[i] != y[0]), i),
            lambda dp, x, y, j: max(dp[0][j - 1] + int(x[0] != y[j]), j),
            lambda dp, x, y, i, j: min(dp[0][col],
                dp[0][j],
                dp[i][j - 1]
                ) + 1 if x[i] != y[j] else dp[0][j - 1]
            )[-1]
    return len(word1 + word2)
```

[Longest Palindromic Subsequence](https://leetcode.com/problems/longest-palindromic-subsequence)
```python
def longestPalindromeSubseq(s):
    n = len(s)
    r = range(n + 1)
    return hirschberg(r,
        r,
        0,
        lambda dp, x, y, i: 0,
        lambda dp, x, y, j: 0,
        lambda dp, x, y, i, j: max(dp[0][j],
            dp[1][j - 1]
        ) if x[0] != s[n - j] else dp[0][j - 1] + 1
    )
```

[Delete Operation for Two Strings](https://leetcode.com/problems/delete-operation-for-two-strings)
```python
def minDistance(word1, word2):
    return len(word1 + word2) - hirschberg(word1,
        word2,
        int(word1[0] == word2[0]),
        lambda dp, x, y, i: max(dp[0][0], int(x[i] == y[0])),
        lambda dp, x, y, j: max(dp[0][j - 1], int(x[0] == y[j])),
        lambda dp, x, y, i, j: max(dp[0][j],
            dp[1][j - 1],
            dp[0][j - 1] + int(x[i] == y[j])
        )
    )
```

[Minimum ASCII Delete Sum for Two Strings](https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings)
```python
def minimumDeleteSum(s1, s2):
    return sum(map(ord, s1 + s2)) - 2*hirschberg(s1,
        s2,
        0 if s1[0] != s2[0] else ord(s1[0]),
        lambda dp, x, y, i: dp[0][0] if x[i] != y[0] else ord(x[i]),
        lambda dp, x, y, j: dp[0][j - 1] if x[0] != y[j] else ord(y[j]),
        lambda dp, x, y, i, j: max(dp[0][j],
            dp[1][j - 1]) if x[i] != y[j] else dp[0][j - 1] + ord(x[i])
    )
```

[Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence)
```python
def longestCommonSubsequence(text1, text2):
    return hirschberg(text1,
        text2,
        int(x[0] == y[0]),
        lambda dp, x, y, i: max(dp[0][0], int(x[i] == y[0])),
        lambda dp, x, y, j: max(dp[0][j - 1], int(x[0] == y[j])),
        lambda dp, x, y, i, j: max(dp[0][j],
            dp[1][j - 1],
            dp[0][j - 1] + int(x[i] == y[j])
        )
    )
```

[Minimum Insertion Steps to Make String a Palindrome](https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome)
```python
def minInsertions(s):
    n = len(s)
    r = range(n + 1)
    return n - hirschberg(r,
        r,
        0,
        lambda dp, x, y, i: 0,
        lambda dp, x, y, j: 0,
        lambda dp, x, y, i, j: max(dp[0][j],
            dp[1][j - 1]
        ) if s[i - 1] != s[-j] else dp[0][j - 1] + 1
    )
```