"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
Example 1:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: true
Example 2:

Input:
matrix = [
  [1,  3,  5,  10],
  [7, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
Output: false

执行用时: 48 ms, 在Search a 2D Matrix的Python3提交中击败了96.49% 的用户
内存消耗: 7.5 MB, 在Search a 2D Matrix的Python3提交中击败了78.10% 的用户

What! I even not use binary search for the row need to be checked...
So waht the point of the question want to be checked?
"""


class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        for row in range(len(matrix)):
            if matrix[row][-1] >= target >= matrix[row][0]:
                for col in range(len(matrix[0])):
                    if matrix[row][col] == target:
                        return True
        else:
            return False