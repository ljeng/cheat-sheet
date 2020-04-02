import itertools


def kadane(arr, func):
    a = b = 0
    for element in arr:
        if func == 'max_subarray':
            a = max(a + element, 0)
            b = max(a, b)
        elif func == 'house_robber':
            a, b = max(a, b + house), a
    if func == 'max_subarray':
        answer = 'b'
    return b if func == 'max_subarray' else a


def rob(houses):
    previous = current = 0
    for house in houses:
        previous, current = max(previous, current + house), previous
    return previous


def max_profit(k, prices):
    if k < len(prices)//2:
        var = [0, -float('inf')]*k + [0]
        for i, price in enumerate(prices):
            for j in range(1, 2*k, 2):
                var[j - 1] =  max(var[j - 1], var[j] + price)
                var[j] = max(var[j], var[j + 1] - price)
        return var[0]
    return kadane(prices, 1, var = [0],
        func = [lambda i, x: x[0] + prices[i] - prices[i - 1]
            if prices[i - 1] < prices[i]
            else x[0]
        ]
    )


def single_number(arr, k=2):
    m = len(bin(max(arr))) - 2
    counter = [0]*m
    single = 0
    for integer, i in itertools.product(arr, range(m)):
        if integer & 1<<i: counter[i] += 1
    for i, x in enumerate(counter):
        if x%k:
            single |= 1<<i
    return single


def wagner_fischer(matrix, base, left, top, each_cell):
    matrix[0][0] = base
    r = range(1, len(matrix))
    for i in r:
        matrix[i][0] = left(i)
    for j in range(1, len(matrix[0])):
        matrix[0][j] = top(j)
    for i in r:
        for j in range(1, len(matrix[i])):
            matrix[i][j] = each_cell(i, j)


def construct_prefix_sum(matrix):
    if matrix:
        prefix_sum = [[0] * (len(matrix[0]) + 1)
            for i in range(len(matrix) + 1)
        ]
        wagner_fischer(prefix_sum, 0, lambda i: 0, lambda j: 0,
            lambda i, j: (matrix[i - 1][j - 1] - prefix_sum[i - 1][j - 1]
                + prefix_sum[i - 1][j] + prefix_sum[i][j - 1]
            )
        )
        return prefix_sum
    return [[0]]


range_sum = lambda prefix_sum, r1, r2, c1, c2: (prefix_sum[r1][c1]
    - prefix_sum[r1][c2] - prefix_sum[r2][c1] + prefix_sum[r2][c2]
)


def hirschberg(x, y, base, left, top, each_cell, flexible=True):
    if flexible:
        y, x = sorted([x, y], key=len)
    m = len(y)
    dp = [[0]*m for k in range(2)]
    dp[0][0] = base
    r, q = range(1, len(x)), range(1, m)
    for j in q:
        dp[0][j] = top(dp, x, y, j)
    for i in r:
        dp[1][0] = left(dp, x, y, i)
        for j in q:
            dp[1][j] = each_cell(dp, x, y, i, j)
        dp[0] = dp[1][:]
    return dp[1][-1]


def lcs(x, y):
    return hirschberg(x, y, int(x[0] == y[0]),
        lambda dp, x, y, i: max(dp[0][0], int(x[i] == y[0])),
        lambda dp, x, y, j: max(dp[0][j - 1], int(x[0] == y[j])),
        lambda dp, x, y, i, j: max(dp[0][j], dp[1][j - 1],
            dp[0][j - 1] + int(x[i] == y[j])
        )
    )


def lps(s):
    r = range(len(s) + 1)
    return hirschberg(r, r, 0, lambda dp, x, y, i: 0,
        lambda dp, x, y, j: 0,
        lambda dp, x, y, i, j: max(dp[0][j], dp[1][j - 1]
        ) if s[i - 1] != s[-j] else dp[0][j - 1] + 1
    )