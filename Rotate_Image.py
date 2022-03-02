"""
date: 2/3/22
question: 48
topic: matrix, array, math

strategy:
1. the reverse the matrix
2. transpose the matrix (transpose = row become column and column become row)
"""


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # reverse
        l = 0
        r = len(matrix) - 1
        while l < r:
            # https://stackoverflow.com/questions/11502268/how-does-pythons-comma-operator-work-during-assignment#:~:text=All%20the%20expressions%20to%20the%20right%20of%20the%20assignment%20operator%20are%20evaluated%20before%20any%20of%20the%20assignments%20are%20made.
            matrix[l], matrix[r] = matrix[r], matrix[l]
            l += 1
            r -= 1

        # transpose
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
