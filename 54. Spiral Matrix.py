"""
Description:
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

Runtime: 32 ms, faster than 100.00% of Python3 online submissions for Spiral Matrix.
Memory Usage: 12.4 MB, less than 100.00% of Python3 online submissions for Spiral Matrix.

Nice shoot!
"""


class Solution:
    def spiralOrder(self, matrix: 'List[List[int]]') -> 'List[int]':
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return []

        rows, cols = len(matrix), len(matrix[0])
        r, c = 0, -1
        direction = 0
        collector = []
        while rows > 0 and cols > 0:
            if direction == 0:
                for _ in range(cols):
                    c += 1
                    collector.append(matrix[r][c])
                rows -= 1
            elif direction == 1:
                for _ in range(rows):
                    r += 1
                    collector.append(matrix[r][c])
                cols -= 1
            elif direction == 2:
                for _ in range(cols):
                    c -= 1
                    collector.append(matrix[r][c])
                rows -= 1
            else:
                for _ in range(rows):
                    r -= 1
                    collector.append(matrix[r][c])
                cols -= 1
            direction = (direction+1) % 4

        return collector

if __name__ == '__main__':
    s = Solution()
    print(s.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))