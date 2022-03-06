"""
date: 6/3/22
question: 53
topic: dynamic programming

approach:
1. loop through the whole array by saving the maximum CURRENT sum
2. then return the maximum sum in the dp table
3. if you don't understand why did we get the answer through step 1 and 2, 
  it's ok, it's more of a dp pattern, do more of these kind of pattern will get you down
"""


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        for i, value in enumerate(nums):
            dp[i] = max(dp[i-1] + value, value)
        return max(dp)
