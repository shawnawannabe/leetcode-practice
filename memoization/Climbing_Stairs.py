class Solution:
    def __init__(self):
        self

    def climbStairs(n: int) -> int:
        a = 1
        b = 1
        for x in range(n):
            tmp = a+b
            a = b
            b = tmp
        return a


n = 3
a = Solution.climbStairs(n)
