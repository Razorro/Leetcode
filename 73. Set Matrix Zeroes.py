"""
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.

Example 1:

Input:
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
Output:
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
Example 2:

Input:
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
Output:
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]
Follow up:

A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?

执行用时: 116 ms, 在Set Matrix Zeroes的Python3提交中击败了79.55% 的用户
内存消耗: 7.1 MB, 在Set Matrix Zeroes的Python3提交中击败了68.60% 的用户

Use the call stack to keep the setting zero infomation, but it seems not very well.
"""


class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        self.solve(matrix, 0, 0)
        return matrix

    def solve(self, matrix, row, col):
        if col >= len(matrix[0]):
            col = 0
            row += 1

        if row >= len(matrix):
            return

        while row < len(matrix):
            if matrix[row][col] != 0:
                col += 1
                if col >= len(matrix[0]):
                    col = 0
                    row += 1
            else:
                break
        else:
            return

        self.solve(matrix, row, col+1)
        print('set zero position (%s, %s)' % (row, col))
        for i in range(len(matrix[0])):     # set row to zero
            matrix[row][i] = 0

        for i in range(len(matrix)):        # set col to zero
            matrix[i][col] =0


if __name__ == '__main__':
    s = Solution()
    print(s.setZeroes([
        [[-1], [2], [3]]
    ]))