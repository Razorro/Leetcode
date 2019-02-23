"""
Description 35:
Given a sorted array and a target value, return the index if the target is found. If not, return the index where 
it would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:

Input: [1,3,5,6], 5
Output: 2
Example 2:

Input: [1,3,5,6], 2
Output: 1
Example 3:

Input: [1,3,5,6], 7
Output: 4
Example 4:

Input: [1,3,5,6], 0
Output: 0

Easy...
"""


class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        head, tail = 0, len(nums)-1
        while head <= tail:
            pivot = (head+tail) // 2
            if nums[pivot] > target:
                tail = pivot - 1
            elif nums[pivot] < target:
                head = head + 1
            else:
                return pivot
            
        return head