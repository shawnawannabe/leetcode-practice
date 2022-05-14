"""
No.: 33
Topic: array, binary search

###########################################
Question:
There is an integer array nums sorted in ascending order (with distinct values).
Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].
Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.
You must write an algorithm with O(log n) runtime complexity.

Constraints:
1 <= nums.length <= 5000
-104 <= nums[i] <= 104
All values of nums are unique.
nums is an ascending array that is possibly rotated.
-104 <= target <= 104

Examples:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

Input: nums = [1], target = 0
Output: -1
###########################################

Approach:
1. the first part of the question is just bs
2. just loop through the array
3. if there's a match return the match
4. else, return -1
5. do the edge cases: if there's nothing in the array return -1
"""


class Solution:
    # def __init__():
    #     pass

    def search(self, nums, target) -> int:
        if not nums:
            print(-1)
            return -1
        for i in range(len(nums)):
            if nums[i] == target:
                print(i)
                return i
        print(-1)
        return -1


nums = [4, 5, 6, 7, 0, 1, 2]
target = 0

# initialized and called in 2 seperate lines (aka expressions)
solution = Solution()
solution.search(nums, target)

# can also be written the way below
# solution = Solution().search(nums, target)
