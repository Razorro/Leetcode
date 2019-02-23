"""
Description 39:
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), 
find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
Example 2:

Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]

Runtime: 56 ms, faster than 99.51% of Python3 online submissions for Combination Sum.
Memory Usage: 6.5 MB, less than 82.57% of Python3 online submissions for Combination Sum.

Those backtracking problems should be aware of the recursion path, how and when, although
without real situation, the talking is nonsense, but the path is most important,
Another, really should notice the shallow copy and deep copy point!!!
More than several times met the pitfall.
"""


class Solution:
    def combinationSum(self, candidates: 'List[int]', target: 'int') -> 'List[List[int]]':
        candidates.sort()
        collector = []
        current = []

        self._solve(candidates, 0, current, collector, target)

        return collector

    def _solve(self, candidates, i, current, collector, target):
        if target == 0:
            collector.append(list(current))
            return

        for j in range(i, len(candidates)):
            if target < candidates[j]:
                return

            current.append(candidates[j])
            self._solve(candidates, j, current, collector, target-candidates[j])
            current.pop()


if __name__ == '__main__':
    s = Solution()
    print(s.combinationSum([2,3,6,7], 7))