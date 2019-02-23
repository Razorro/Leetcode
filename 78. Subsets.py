"""
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

执行用时: 48 ms, 在Subsets的Python3提交中击败了98.97% 的用户
内存消耗: 6.7 MB, 在Subsets的Python3提交中击败了64.14% 的用户

No other tricks, just find the recursive path clearly.
"""


class Solution:
    def subsets(self, nums: 'List[int]') -> 'List[List[int]]':
        current = []
        result = []
        for i in range(len(nums)):
            self.solve(nums, result, current, i)
        return result

    def solve(self, nums, result, current, i):
        if i == len(nums):
            return

        current.append(nums[i])
        result.append(list(current))
        for j in range(i + 1, len(nums) + 1):
            self.solve(nums, result, current, j)
        current.pop()