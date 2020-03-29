import functools


def kadane(arr, start=0, k=-1, var = [0, -float('inf')], func='kadane'):
    if func == 'kadane':
        var = [0, -float('inf')]
        func = [lambda i, x: arr[i] + max(x[0], 0), lambda i, x: max(x)]
    elif func == 'house_robber':
        k = 1
        var = [0, 0, 0]
        func = [lambda i, x: x[1], lambda i, x: max(x[1], nums[i] + x[2]),
            lambda i, x: x[0]]
    for i in range(start, len(arr)):
        for j, f in enumerate(func):
            var[j] = f(i, var)
    return var[k]


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