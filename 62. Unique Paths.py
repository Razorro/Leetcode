"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner
of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?


Above is a 7 x 3 grid. How many possible unique paths are there?

Note: m and n will be at most 100.

Example 1:

Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right

Runtime: 32 ms, faster than 100.00% of Python3 online submissions for Unique Paths.
Memory Usage: 12.4 MB, less than 100.00% of Python3 online submissions for Unique Paths.

With right observation of the order, use a little dynamic programming, get things done.
"""

class Solution:
    def uniquePaths(self, m: 'int', n: 'int') -> 'int':
        pass