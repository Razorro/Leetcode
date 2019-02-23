"""
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.

执行用时: 164 ms, 在Word Search的Python3提交中击败了95.59% 的用户
内存消耗: 7.4 MB, 在Word Search的Python3提交中击败了98.59% 的用户

Normal backtracking problem, not too much details.
"""


class Solution:
    def exist(self, board: 'List[List[str]]', word: 'str') -> 'bool':
        for x in range(len(board)):
            for y in range(len(board[0])):
                if board[x][y] == word[0]:
                    temp, board[x][y] = board[x][y], None
                    if self.search(board, word, 1, x, y):
                        return True
                    board[x][y] = temp
        return False

    def search(self, board, word, i, x, y):
        if i == len(word):
            return True

        targetChar = word[i]
        if x - 1 >= 0 and board[x - 1][y] is not None and board[x - 1][y] == targetChar:
            temp, board[x - 1][y] = board[x - 1][y], None
            if self.search(board, word, i + 1, x - 1, y):
                return True
            board[x - 1][y] = temp

        if x + 1 < len(board) and board[x + 1][y] is not None and board[x + 1][y] == targetChar:
            temp, board[x + 1][y] = board[x + 1][y], None
            if self.search(board, word, i + 1, x + 1, y):
                return True
            board[x + 1][y] = temp

        if y - 1 >= 0 and board[x][y - 1] is not None and board[x][y - 1] == targetChar:
            temp, board[x][y - 1] = board[x][y - 1], None
            if self.search(board, word, i + 1, x, y - 1):
                return True
            board[x][y - 1] = temp

        if y + 1 < len(board[0]) and board[x][y + 1] is not None and board[x][y + 1] == targetChar:
            temp, board[x][y + 1] = board[x][y + 1], None
            if self.search(board, word, i + 1, x, y + 1):
                return True
            board[x][y + 1] = temp

        return False