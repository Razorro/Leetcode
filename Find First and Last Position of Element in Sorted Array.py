"""
Description 34:
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Quite easy, with some extention of binary search
"""


class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        head, tail = 0, len(nums)-1
        while head <= tail:
            pivot = (head+tail) // 2
            if nums[pivot] > target:
                tail = pivot - 1
            elif nums[pivot] < target:
                head = pivot + 1
            else:
                upper, lower = pivot, pivot
                while upper+1 < len(nums) and nums[upper+1] == nums[pivot]:
                    upper += 1
                while lower-1 >= 0 and nums[lower-1] == nums[pivot]:
                    lower -= 1
                return [lower, upper]
            
        return [-1,-1]