"""
date: 1/3/2022
question: 39
topic: array, backtracking

strategy:
dfs
1. it's more like a format
"""


def combinationSum(candidates, target):
    res = []

    def dfs(nums, target, path, res):
        if target < 0:
            return
        if target == 0:
            res.append(path)
            return
        for i in range(len(nums)):
            dfs(nums[i:], target-nums[i], path + [nums[i]], res)

    dfs(candidates, target, [], res)
    return res


candidates = [2, 3, 6, 7]
target = 7

combinationSum(candidates, target)
