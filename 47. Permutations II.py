"""
Description:
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:

Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]

Runtime: 68 ms, faster than 90.05% of Python3 online submissions for Permutations II.
Memory Usage: 12.6 MB, less than 4.23% of Python3 online submissions for Permutations II.

With some hints of Stefan's answer of Question46, the key is, pass by the same number.
"""


class Solution:
    def permuteUnique(self, nums: 'List[int]') -> 'List[List[int]]':
        nums.sort()
        return self.solve(nums)

    def solve(self, nums):
        i = 0
        collector = []
        while i < len(nums):
            for p in self.solve(nums[:i] + nums[i + 1:]):
                collector.append([nums[i]] + p)

            head = nums[i]
            while i < len(nums) and head == nums[i]: i += 1
        return collector or [[]]


if __name__ == '__main__':
    s = Solution()
    print(s.permuteUnique([1,1,2]))