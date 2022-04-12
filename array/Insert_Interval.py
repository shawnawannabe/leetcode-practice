"""
date: 12/4/2022
question: 57
topic: array

strategy:
1. the key: how to find the larger one between 2 intervals
2. take the smallest value in one interval and compare with the largest value in the other interval
"""


def insert1(intervals, newInterval):
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
    return result


intervals = [[1, 3], [6, 9]]
newInterval = [2, 5]

insert1(intervals, newInterval)
