"""
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

Example:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

执行用时: 160 ms, 在Combinations的Python3提交中击败了85.61% 的用户
内存消耗: 9.1 MB, 在Combinations的Python3提交中击败了56.38% 的用户

Not bad, just use recursive method to create the situation that fit this question.
"""


class Solution:
    def combine(self, n: 'int', k: 'int') -> 'List[List[int]]':
        def combine(self, n: 'int', k: 'int') -> 'List[List[int]]':
            if n <= 0 or k <= 0:
                return [[]]

            result = []
            current = []
            k = min(n, k)
            self.solve(n, k, 1, result, current)
            return result

        def solve(self, n, k, i, result, current):
            if k == 0:
                result.append(list(current))
                return

            k -= 1
            if n - i < k:
                return

            for j in range(i, n + 1):
                current.append(j)
                self.solve(n, k, j + 1, result, current)
                current.pop()