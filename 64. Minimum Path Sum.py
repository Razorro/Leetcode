"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.

Runtime: 48 ms, faster than 99.38% of Python3 online submissions for Minimum Path Sum.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Minimum Path Sum.

With easy observation...
"""


class Solution:
    def minPathSum(self, grid: 'List[List[int]]') -> 'int':
        path = [0] * len(grid[0])
        total = 0
        for i, n in enumerate(grid[0]):
            total += n
            path[i] = total

        for row in range(1, len(grid)):
            for col in range(len(grid[0])):
                path[col] = min(path[col], path[col-1] if col-1 >= 0 else 99999) + grid[row][col]

        return path[-1]