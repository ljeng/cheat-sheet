def kadane(arr, start, i, var, func):
    for j in range(start, len(arr)):
        for k in range(len(var)):
            var[k] = func[k](j, var)
    return var[i]


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


def knapsack(items, capacity, base, a, b, c):
    each_cell = lambda dp, x, y, i, j: b(dp, i, j) if a(i, j) else c(dp, i, j)
    return hirschberg(items, range(capacity + 1), base,
        lambda dp, x, y, i: base,
        lambda dp, x, y, j: each_cell(dp, x, y, 0, j), each_cell, False
    )