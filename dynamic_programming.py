def longest_common_subsequence(x, y):
    n, m = map(len, (x, y))
    if not n or not m: return 0
    dp = [[0 for j in range(m)] for i in range(n)]
    dp[0][0], r, q = int(x[0] == y[0]), range(1, n), range(1, m)
    for i in r: dp[i][0] = max(dp[i - 1][0], int(x[i] == y[0]))
    for j in q: dp[0][j] = max(dp[0][j - 1], int(x[0] == y[j]))
    for i in r:
        row = i - 1
        for j in q:
            col = j - 1
            dp[i][j] = max(dp[row][j], dp[i][col], dp[row][col] + int(x[i] == y[j]))
    return dp[-1][-1]

def matrix_chain_multiplication(dimensions):
    n = len(dimensions)
    r = range(n)
    dp = [[float('inf') for j in r] for i in r]
    for i in range(1, n): dp[i][i] = 0
    for length in range(2, n):
        for i in range(n - length + 1):
            j = i + length - 1
            for k in range(i, j):
                cost = dp[i][k] + dp[k + 1][j]
                cost += dimensions[i - 1]*dimensions[j]*dimensions[k]
                dp[i][j] = min(dp[i][j], cost)
    return dp[1][-1]