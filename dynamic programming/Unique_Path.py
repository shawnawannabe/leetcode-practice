def uniquePaths(m: int, n: int) -> int:
    dp = [1]*n
    for i in range(1, m):
        for j in range(1, n):
            dp[j] = dp[j] + dp[j-1]
    return dp[n-1]


m = 3
n = 6

uniquePaths(m, n)
