"""
date: 17/4/2022
no.: 79
topic: backtracking, array, matrix

question:
Given an m x n grid of characters board and a string word, return true if word exists in the grid.
The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

example:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false

strategy:
1. the idea is to check every cell, backtrack and search the next left/right/up/down cell
2. the conditions to be fulfilled are commented below
"""


class Solution:
    # this bt is slightly more complicated then the other questions

    def __init__(self):
        pass

    def exist(board, word) -> bool:
        def dfs(board, row, column, word):
            if len(word) == 0:  # succeed in searching the whole word
                return True
            # first 4 cond : row and column tracker, the last one = char in word does not match the next cell
            if row < 0 or row >= len(board) or column < 0 or column >= len(board[0]) or word[0] != board[row][column]:
                return False
            tmp = board[row][column]    # store in a tmp variable
            board[row][column] = "#"    # change it to avoid visiting it again
            res = dfs(board, row+1, column, word[1:]) or dfs(board, row-1, column, word[1:]) or dfs(
                board, row, column+1, word[1:]) or dfs(board, row, column-1, word[1:])
            board[row][column] = tmp    # need to change it back after visiting, else searches in other direction would go wrong, eg. word = ab, board = [[aaa],[aba]], the second a in board[1] would become "#" and when searching board[1][2] downwards, it would be "#b"
            return res

        if not board:
            return False
        for row in range(len(board)):
            for column in range(len(board[0])):
                if dfs(board, row, column, word):
                    return True
        return False


board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "ABCCED"
solution = Solution.exist(board, word)
