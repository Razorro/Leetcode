"""
Descrition:
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.

Note:
The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]


Runtime: 1052 ms, faster than 64.77% of Python3 online submissions for 3Sum.
Emmm... Not a good result, let's find out some better answer.
But the solution approximately familiar.
"""


class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return []

        nums.sort()
        ret = []
        left = 0
        while left < len(nums)-2:
            target = -nums[left]
            right = len(nums) - 1
            middle = left + 1
            while middle < right:
                if nums[middle] + nums[right] > target:
                    while right > middle and nums[right] == nums[right-1]: right -= 1
                    right -= 1
                elif nums[middle] + nums[right] < target:
                    while middle < right and nums[middle] == nums[middle+1]: middle += 1
                    middle += 1
                else:
                    ret.append([nums[left], nums[middle], nums[right]])
                    while middle < right and nums[middle] == nums[middle+1]: middle += 1        # advance middle value, break the balance
                    middle += 1

            while left < len(nums)-2 and nums[left] == nums[left+1]: left += 1
            left += 1

        return ret


if __name__ == '__main__':
    s = Solution()
    print(s.threeSum([-1, 0, 1, 2, -1, -4]))