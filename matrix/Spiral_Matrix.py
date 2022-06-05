"""
No: 54
Topic: Matrix, Array, Simulation

#################################################
Given an m x n matrix, return all elements of the matrix in spiral order.

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100
#################################################

Approach:
1. Set and name the variables correctly and thats about it
2. Watch out for edge cases tho
"""


class Solution:

    def spiralOrder(init, matrix):
        height = len(matrix)
        width = len(matrix[0])

        top = 0
        bottom = height - 1
        left = 0
        right = width - 1

        ans = []
        while top < bottom and left < right:
            for col in range(left, right):
                ans.append(matrix[top][col])

            for row in range(top, bottom):
                ans.append(matrix[row][right])

            for col in range(right, left, -1):
                ans.append(matrix[bottom][col])

            for row in range(bottom, top, -1):
                ans.append(matrix[row][left])

            top += 1
            bottom -= 1
            left += 1
            right -= 1

        # If a matrix is either a 1xn or a mx1 | eg. [[1, 2, 3]] or [[1], [2], [3]]
        # this also applies to matrix remaining | eg. [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
        # a linear scan will return the same order as spiral for these
        if len(ans) < height * width:
            for row in range(top, bottom+1):
                for col in range(left, right+1):
                    ans.append(matrix[row][col])

        print(ans)
        return ans


matrix = [[1, 2, 3]]
solution = Solution().spiralOrder(matrix)
