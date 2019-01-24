"""
Description 16:
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target.
Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:

Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""


class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        left = 0
        diff = 65535
        while left < len(nums)-2:
            tempTarget = target - nums[left]
            right = len(nums) - 1
            middle = left + 1
            while middle < right:
                if nums[middle] + nums[right] > tempTarget:
                    temp = tempTarget - nums[middle] - nums[right]
                    diff = temp if abs(temp) < abs(diff) else diff
                    while right > middle and nums[right] == nums[right - 1]: right -= 1
                    right -= 1
                elif nums[middle] + nums[right] < tempTarget:
                    temp = tempTarget - nums[middle] - nums[right]
                    diff = temp if abs(temp) < abs(diff) else diff
                    while middle < right and nums[middle] == nums[middle + 1]: middle += 1
                    middle += 1
                else:
                    return nums[left] + nums[middle] + nums[right]

            while left < len(nums)-2 and nums[left] == nums[left+1]: left += 1
            left += 1

        return target - diff


if __name__ == '__main__':
    s = Solution()
    print(s.threeSumClosest([-1, 2, 1, -4], 1))