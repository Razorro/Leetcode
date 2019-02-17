"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?



An obstacle and empty space is marked as 1 and 0 respectively in the grid.

Note: m and n will be at most 100.

Example 1:

Input:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
Output: 2
Explanation:
There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right

Runtime: 40 ms, faster than 59.05% of Python3 online submissions for Unique Paths II.
Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Unique Paths II.

Not too fast, but the idea must quite same, some error commit because of the dealing of initialization
"""


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: 'List[List[int]]') -> 'int':
        path = [1] * len(obstacleGrid[0])
        for row in range(1, len(obstacleGrid)):
            for col in range(len(path)):
                if obstacleGrid[row][col] == 1:
                    path[col] = 0
                else:
                    left = path[col - 1] if col - 1 >= 0 else 0
                    path[col] = left + path[col]

        return path[-1]