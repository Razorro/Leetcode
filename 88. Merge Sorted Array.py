"""
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]


No other tricks, just observation.

执行用时: 68 ms, 在Merge Sorted Array的Python3提交中击败了8.11% 的用户
内存消耗: 13.1 MB, 在Merge Sorted Array的Python3提交中击败了0.51% 的用户

Although the result is not so well, but I think there is no big difference with other solutions.
"""


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        idx1, idx2 = m - 1, n - 1
        fillIdx = len(nums1) - 1
        while idx1 >= 0 and idx2 >= 0:
            if nums1[idx1] > nums2[idx2]:
                nums1[fillIdx] = nums1[idx1]
                idx1 -= 1
            else:
                nums1[fillIdx] = nums2[idx2]
                idx2 -= 1
            fillIdx -= 1

        while idx2 >= 0:
            nums1[fillIdx] = nums2[idx2]
            idx2 -= 1
            fillIdx -= 1