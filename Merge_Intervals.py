"""
date: 29/3/22
question: 56
topic: sorting

approach:
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
