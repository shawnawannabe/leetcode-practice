"""
No.: 56
Topic: Sorting, Array

#################################################
Question:
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

Example 2:
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

Constraints:
1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104
#################################################

Approach:
1. sort the intervals first, to fulfill one of the edge cases
2. loop through the intervals, if empty, just append into result
3. if not, compare before appending
4. how to compare? refer code

edge cases:
[[1, 4], [0, 0]] - to counter this, just sort
"""


def merge(intervals):
    intervals.sort(key=lambda x: x[0])
    merged = []
    for inter in intervals:

        # if merged is empty or no overlap
        if not merged or merged[-1][1] < inter[0]:
            merged.append(inter)
        else:
            # found overlap
            last = merged.pop()

            start = min(last[0], inter[0])
            end = max(last[1], inter[1])

            merged.append([start, end])

    print(merged)
    return merged


intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
# intervals = [[1, 4], [0, 0]]
merge(intervals)
