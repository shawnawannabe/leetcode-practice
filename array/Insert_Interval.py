"""
No.: 57
Topic: array

################################################
Question:
You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.
Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).
Return intervals after the insertion.

Example:
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

Constraints:
0 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 105
intervals is sorted by starti in ascending order.
newInterval.length == 2
0 <= start <= end <= 105

################################################

Approach:
1. the key: how to find the larger one between 2 intervals
2. take the smallest value in one interval and compare with the largest value in the other interval
"""


class Solution:
    def __init__(self):
        pass

    def insert(intervals, newInterval):
        result = []

        for interval in intervals:
            # smaller than
            if interval[1] < newInterval[0]:
                result.append(interval)
            # larger than
            elif interval[0] > newInterval[1]:
                result.append(newInterval)
                newInterval = interval
            # overlapping
            elif interval[1] >= newInterval[0] or interval[0] <= newInterval[1]:
                newInterval[0] = min(interval[0], newInterval[0])
                newInterval[1] = max(newInterval[1], interval[1])

        result.append(newInterval)
        print(result)
        return result


intervals = [[1, 3], [6, 9]]
newInterval = [2, 5]

# solution = Solution.insert(intervals, newInterval)

# Instances initialized at line 66 and a function (aka method) is called
solution = Solution
solution.insert(intervals, newInterval)
