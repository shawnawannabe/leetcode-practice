"""
No.: 79
Topic: backtracking, array, matrix

##########################################################
Question:
Given an m x n grid of characters board and a string word, return true if word exists in the grid.
The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false

Constraints:
m == board.length
n = board[i].length
1 <= m, n <= 6
1 <= word.length <= 15
board and word consists of only lowercase and uppercase English letters.

Follow up: Could you use search pruning to make your solution faster with a larger board?
##########################################################

Approach:
1. the idea is to check every cell, backtrack and search the next left/right/up/down cell
2. the conditions to be fulfilled are commented as below
3. edge cases: if board does not exist, return False
"""


class Solution:
    # this backtracking question is slightly more complicated then the other

    def __init__(self):
        pass

    def exist(board, word) -> bool:
        def dfs(board, row, column, word):
            if len(word) == 0:  # succeed in searching the whole word
                return True
            # first 4 cond : row and column tracker, the last condition = char in word does not match the next cell
            if row < 0 or row >= len(board) or column < 0 or column >= len(board[0]) or word[0] != board[row][column]:
                return False
            tmp = board[row][column]    # store in a tmp variable
            board[row][column] = "#"    # change it to avoid visiting it again
            res = dfs(board, row+1, column, word[1:]) or dfs(board, row-1, column, word[1:]) or dfs(
                board, row, column+1, word[1:]) or dfs(board, row, column-1, word[1:])
            board[row][column] = tmp    # need to change it back after visiting, else searches in other direction would go wrong, eg. word = ab, board = [[aaa],[aba]], the second a in board[0] would become "#" and when searching board[0][1] downwards, it would be "#b"
            return res

        if not board:
            print(False)
            return False
        for row in range(len(board)):
            for column in range(len(board[0])):
                if dfs(board, row, column, word):
                    print(True)
                    return True
        print(False)
        return False


board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "ABCCED"
solution = Solution.exist(board, word)
