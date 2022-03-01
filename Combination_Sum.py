"""
date: 1/3/2022
question: 39
topic: backtracking

strategy:
dfs
1. it's more like a format
"""

class Solution:
  def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
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
