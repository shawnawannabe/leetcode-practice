"""
date: 7/3/22
question: 55
topic: dynamic programming, greedy

approach:
1. keep track of the can reach variable
2. once the can reach variable can reach the last index in the array, first condition for the question is fullfilled
3. second condition: false, will be fullfilled if we have finish looping throught the array and the index still unable to reach the variable
"""

def canJump(nums):
    can_reach = 0
    for i, val in enumerate(nums):
        if i > can_reach:   # can be read as finish looping through the array
            return False
        can_reach = max(can_reach, i + val)
        if can_reach >= len(nums)-1:
            return True