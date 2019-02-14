"""
Description:
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Note:

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
DO NOT allocate another 2D matrix and do the rotation.

Example 1:

Given input matrix =
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

rotate the input matrix in-place such that it becomes:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
Example 2:

Given input matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
],

rotate the input matrix in-place such that it becomes:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]

Runtime: 32 ms, faster than 100.00% of Python3 online submissions for Rotate Image.
Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Rotate Image.

Unbelievable! The best answer! The question has no other tricks, just observation.
"""


class Solution:
    def rotate(self, matrix: 'List[List[int]]') -> 'None':
        """
        Do not return anything, modify matrix in-place instead.
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return

        rows, cols = len(matrix) - 1, len(matrix[0]) - 1
        from math import ceil
        for row in range( len(matrix) // 2):
            for col in range(ceil(len(matrix[0]) / 2)):
                matrix[row][col], matrix[col][rows - row], \
                matrix[rows-row][cols-col], matrix[cols-col][row] = \
                matrix[cols - col][row], matrix[row][col], \
                matrix[col][rows - row], matrix[rows - row][cols - col]


if __name__ == '__main__':
    s = Solution()
    test = [[1,2,3], [4,5,6], [7,8,9]]
    s.rotate(test)
    print(test)