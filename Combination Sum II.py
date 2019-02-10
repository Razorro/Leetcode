"""
Description 40:
Given a collection of candidate numbers (candidates) and a target number (target), find all unique
combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:
Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]

Example 2:

Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]

Runtime: 56 ms, faster than 85.97% of Python3 online submissions for Combination Sum II.
Memory Usage: 6.5 MB, less than 74.96% of Python3 online submissions for Combination Sum II.

Not bad. Those problems really should notice the recursion path processing.
"""


class Solution:
    def combinationSum2(self, candidates: 'List[int]', target: 'int') -> 'List[List[int]]':
        if len(candidates) == 0:
            return []

        candidates.sort()
        current, collector = [], []
        self.solve(candidates, target, current, collector, 0)
        return collector

    def solve(self, candidates, target, current, collector, tail):
        if target == 0:
            collector.append(current)
            return

        if tail == len(candidates) or target < candidates[tail]:
            return

        head = tail
        initNum = candidates[head]
        while tail < len(candidates) and candidates[tail] == initNum:
            tail += 1

        count = tail - head
        for i in range(count+1):
            current += [initNum] * i
            self.solve(candidates, target-initNum*i, current, collector, tail)
            current = current[:len(current)-i]


if __name__ == '__main__':
    s = Solution()
    print(s.combinationSum2([10,1,2,7,6,1,5], 8))