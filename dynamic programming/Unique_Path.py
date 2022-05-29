"""
No: 62
Topic: Dynamic programming, Math, Combinatorics

#############################################################
Question:
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.
Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.
The test cases are generated so that the answer will be less than or equal to 2 * 109.

Example:
Input: m = 3, n = 7
Output: 28

Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down

Constraints:
1 <= m, n <= 100
#############################################################

Approach:
1. trying to find out the pattern
    a. m = 2, n = 1, number of path = 1
    b. m = 2, n = 2, nop = 2
    c. m = 2, n = 3, nop = 3
    d. m = 2, n = 4, nop = 4

    a. m = 3, n = 1, number of path = 1
    b. m = 3, n = 2, nop = 3
    c. m = 3, n = 3, nop = 6
    d. m = 3, n = 4, nop = 10

    a. m = 4, n = 1, number of path = 1
    b. m = 4, n = 2, nop = 4
    c. m = 4, n = 3, nop = 10
    d. m = 4, n = 4, nop = 20

Dynamic Programming pattern:
        
    Base case:
    DP(0, j) = 1 , only reachable from one step left
    DP(i, 0) = 1 , only reachable from one step up
    
    General case:
    DP(i,j) = number of path reach to (i, j)
            = number of path reach to one step left + number of path reach to one step up
            = number of path reach to (i, j-1) + number of path to (i-1, j)
            = DP(i, j-1) + DP(i-1, j)
"""


def uniquePaths(m: int, n: int) -> int:
    rows, cols = m, n
    path_dp = [[1 for j in range(cols)] for i in range(rows)]

    for i in range(1, m):
        for j in range(1, n):
            path_dp[i][j] = path_dp[i][j-1] + path_dp[i-1][j]

    # Destination coordination = (rows-1, cols-1) aka the last column at the last row
    print(path_dp[-1][-1])
    return path_dp[rows-1][cols-1]


m = 3
n = 7

uniquePaths(m, n)
