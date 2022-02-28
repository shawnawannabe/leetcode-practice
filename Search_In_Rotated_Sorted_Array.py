"""
date: 28/2/22
question: 33

strategy:
1. the first part of the question is just bs
2. just loop through the array
3. if there's a match return the match
4. else, return -1
5. do the edge cases: if there's nothing in the array return -1
"""


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        return -1