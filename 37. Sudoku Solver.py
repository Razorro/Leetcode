"""
Description 37:
Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
Empty cells are indicated by the character '.'.

Note:

The given board contain only digits 1-9 and the character '.'.
You may assume that the given Sudoku puzzle will have a single unique solution.
The given board size is always 9x9.

Runtime: 112 ms, faster than 82.30% of Python3 online submissions for Sudoku Solver.
Memory Usage: 6.5 MB, less than 48.11% of Python3 online submissions for Sudoku Solver.

Use space to record the invalid nums, to reduce the range of possible nums,
Being blocked for a long period, because of during the back tracing procedure,
Forget to recover the assignment, I thought it was not necessary because of short path,
In the end, you should recover the "." to make the n-deepth recursion can be fully recovered.
"""


class Solution:
    def solveSudoku(self, board: 'List[List[str]]') -> 'None':
        """
        Do not return anything, modify board in-place instead.
        """
        row_checker = {}
        col_checker = {}
        square_checker = {}
        self.collectInfo(board, row_checker, col_checker, square_checker)
        self.addNum(board, row_checker, col_checker, square_checker, 0, 0)

    def collectInfo(self, board, row_checker, col_checker, square_checker):
        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] != '.':
                    row_collector = row_checker.setdefault(row, set())
                    row_collector.add(board[row][col])

                    col_collector = col_checker.setdefault(col, set())
                    col_collector.add(board[row][col])

                    square_collector = square_checker.setdefault((row // 3, col // 3), set())
                    square_collector.add(board[row][col])

    def addNum(self, board, row_checker, col_checker, square_checker, row, col):
        if col == len(board[0]):
            col = 0
            row += 1
            if row == len(board):
                return True

        if board[row][col] == '.':
            default_set = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}
            default_set -= row_checker.setdefault(row, set())
            default_set -= col_checker.setdefault(col, set())
            default_set -= square_checker.setdefault((row // 3, col // 3), set())

            for n in default_set:
                board[row][col] = n
                row_collector = row_checker.setdefault(row, set())
                row_collector.add(n)

                col_collector = col_checker.setdefault(col, set())
                col_collector.add(n)

                square_collector = square_checker.setdefault((row // 3, col // 3), set())
                square_collector.add(n)

                if self.addNum(board, row_checker, col_checker, square_checker, row, col + 1):
                    return True

                row_collector.remove(n)
                col_collector.remove(n)
                square_collector.remove(n)
            board[row][col] = '.'
            return False

        else:
            return self.addNum(board, row_checker, col_checker, square_checker, row, col + 1)