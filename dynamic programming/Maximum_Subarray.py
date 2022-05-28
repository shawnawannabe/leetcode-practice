"""
No: 53
Topic: Dynamic programming, Array, Divide and conquer

#######################################################
Question:
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
A subarray is a contiguous part of an array.

Example:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Input: nums = [1]
Output: 1

Input: nums = [5,4,-1,7,8]
Output: 23

Constraints:
1 <= nums.length <= 105
-104 <= nums[i] <= 104

Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
#######################################################

Approach:
1. loop through the whole nums array by saving the maximum CURRENT sum
2. then return the maximum sum in the dp table
3. if you don't understand why did we get the answer through step 1 and 2, 
  it's ok, it's more of a dp pattern, do more of these kind of pattern will get you down
"""


class Solution:
    def maxSubArray(self, nums) -> int:
        dp = [0] * len(nums)
        for i, value in enumerate(nums):
            dp[i] = max(dp[i-1] + value, value)
        print(max(dp))
        return max(dp)


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

solution = Solution()
solution.maxSubArray(nums)
