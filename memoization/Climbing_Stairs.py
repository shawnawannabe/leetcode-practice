"""
No.: 62
Topic: Dynamic programming, Math, Memoization

#################################################################
Question:
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top? 

Example:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

Constraints:
1 <= n <= 45
#################################################################

Approach:
1. It is actually a pattern, the solution = n-1 + n-2
2. Why? n = 3, output = 3, | n = 4 , output = 5
3. The python syntax: a, b = b , a+b  means exactly this 
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
        print(a)
        return a


n = 2
a = Solution.climbStairs(n)
