"""
No: 48
Topic: matrix, array, math

##############################################
Question: 
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Example:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]

Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

Constraints:
n == matrix.length == matrix[i].length
1 <= n <= 20
-1000 <= matrix[i][j] <= 1000
##############################################

Approach:
1. Reverse the matrix, meaning making the first row the last row, and so on
2. Transpose the matrix (transpose = row become column and column become row), how?, matrix[row][col] = matrix[col][row]
"""


class Solution:
    def rotate(self, matrix) -> None:
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
        print(matrix)


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
solution = Solution().rotate(matrix)
# print(matrix[0][1], matrix[1][0])
