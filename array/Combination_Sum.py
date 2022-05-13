"""
No: 39
Topic: array, backtracking

################################
Question:
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.


Example:
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]

Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]

Input: candidates = [2], target = 1
Output: []


Constraints:
1 <= candidates.length <= 30
1 <= candidates[i] <= 200
All elements of candidates are distinct.
1 <= target <= 500
################################

Approach:
dfs
1. it's more like a format
"""


class Solution:
    def __init__(self) -> None:
        pass

    def combinationSum(candidates, target):
        res = []

        def dfs(nums, target, path, res):
            if target < 0:
                return
            elif target == 0:
                res.append(path)
                return
            else:
                for i in range(len(nums)):
                    dfs(nums[i:], target-nums[i], path + [nums[i]], res)

        dfs(candidates, target, [], res)
        print(res)
        return res


candidates = [2, 3, 6, 7]
target = 7

# Instances initialized and the function (python syntax: method) called in the same line (python syntax: expression)
solution = Solution.combinationSum(candidates, target)
