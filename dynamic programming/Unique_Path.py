"""
date: 14/4/2022
question: 62
topic: dynamic programming

strategy:
1. it always starts from top left corner, we can create a array based on n
2. basically just keep adding the number of steps needed starting from the top row
2. it is easier when refering to the picture
"""


def uniquePaths(m: int, n: int) -> int:
    dp = [1]*n
    for i in range(1, m):
        for j in range(1, n):
            dp[j] = dp[j] + dp[j-1]
    return dp[n-1]


m = 3
n = 6

uniquePaths(m, n)
