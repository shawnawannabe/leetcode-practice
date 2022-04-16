"""
date: 16/4/2022
no.: 73
topic: matrix, hash table, array

question:
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
You must do it in place.

example:
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

strategy:
1. go through every single element/entries, if there's a zero, mark the first row and first col as 0
2. this is because we can use the zero marked as an indicator to which row/column we want as 0
3. if there's a zero at the first row / col, the whole row / col would be 0 as well
4. the only catch here is the above rule does not apply to the first row and first col, that's why we have to use an indicator
"""


class Solution:
    def __init__(self):
        pass

    def setZeroes(matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])

        first_row_has_zero = False
        first_col_has_zero = False

        # iterate through matrix to mark the zero row and cols
        for row in range(m):
            for col in range(n):
                if matrix[row][col] == 0:
                    if row == 0:
                        first_row_has_zero = True
                    if col == 0:
                        first_col_has_zero = True
                    matrix[row][0] = matrix[0][col] = 0

        # iterate through matrix to update the cell to be zero if it's in a zero row or col
        for row in range(1, m):
            for col in range(1, n):
                matrix[row][col] = 0 if matrix[0][col] == 0 or matrix[row][0] == 0 else matrix[row][col]

        # update the first row and col if they're zero
        if first_row_has_zero:
            for col in range(n):
                matrix[0][col] = 0

        if first_col_has_zero:
            for row in range(m):
                matrix[row][0] = 0


matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
solution = Solution.setZeroes(matrix)
