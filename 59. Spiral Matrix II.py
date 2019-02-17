"""
Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

Example:

Input: 3
Output:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]

Runtime: 36 ms, faster than 96.43% of Python3 online submissions for Spiral Matrix II.
Memory Usage: 12.3 MB, less than 100.00% of Python3 online submissions for Spiral Matrix II.

Just same as the one before
"""


class Solution:
    def generateMatrix(self, n: 'int') -> 'List[List[int]]':
        matrix = [[0]*n for _ in range(n)]
        rows, cols = n, n
        num = 1
        r, c = 0, -1
        direction = 0
        while rows > 0 and cols > 0:
            if direction == 0:
                for _ in range(cols):
                    c += 1
                    matrix[r][c] = num
                    num += 1
                rows -= 1
            elif direction == 1:
                for _ in range(rows):
                    r += 1
                    matrix[r][c] = num
                    num += 1
                cols -= 1
            elif direction == 2:
                for _ in range(cols):
                    c -= 1
                    matrix[r][c] = num
                    num += 1
                rows -= 1
            else:
                for _ in range(rows):
                    r -= 1
                    matrix[r][c] = num
                    num += 1
                cols -= 1
            direction = (direction+1) % 4

        return matrix