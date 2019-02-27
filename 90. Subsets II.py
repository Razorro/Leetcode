"""
Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]

Runtime: 48 ms, faster than 58.58% of Python3 online submissions for Subsets II.
Memory Usage: 13.3 MB, less than 5.47% of Python3 online submissions for Subsets II.


No other tricks, just split those repeat numbers as a unit, recurse from them by unit.
"""


class Solution:
    def subsetsWithDup(self, nums: 'List[int]') -> 'List[List[int]]':
        result = []
        collector = []
        nums.sort()
        self.solve(nums, result, collector, 0)
        return result

    def solve(self, nums, result, collector, idx):
        if idx >= len(nums):
            result.append(collector)
            return

        tail = idx + 1
        while tail < len(nums) and nums[tail] == nums[idx]:
            tail += 1

        for times in range(tail - idx + 1):
            collector += [nums[idx]] * times
            self.solve(nums, result, collector, tail)
            collector = collector[:len(collector) - times]