"""
date: 15/4/2022
no.: 62
topic: dynamic programming

question:
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top? 

example:
Input: n = 2
Output: 2

Input: n = 3
Output: 3

strategy:
1. it is actually a pattern, the solution = n-1 + n-2
2. why? n = 3, output = 3, | n = 4 , output = 5
3. the python syntax: a, b = b , a+b  means exactly this 
"""


class Solution:
    def __init__(self):
        pass

    def climbStairs(n: int) -> int:
        a = 1
        b = 1
        for _ in range(n):
            # tmp = a+b
            # a = b
            # b = tmp
            a, b = b, a + b  # same meaning as the commented code above
        return a


n = 2
a = Solution.climbStairs(n)
print(a)
