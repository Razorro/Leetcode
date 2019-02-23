"""
Description 36:
Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated 
according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.
"""

class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        row_validator = {}
        col_validator = {}
        box_validator = {}
        
        for r in range(len(board)):
            for c in range(len(board[r])):
                if board[r][c] == '.':
                    continue
                    
                validator = row_validator.setdefault(r, set())
                if board[r][c] in validator:
                    return False
                validator.add(board[r][c])
                
                validator = col_validator.setdefault(c, set())
                if board[r][c] in validator:
                    return False
                validator.add(board[r][c])
                
                validator = box_validator.setdefault((r//3, c//3,), set())
                if board[r][c] in validator:
                    return False
                validator.add(board[r][c])
                
        return True