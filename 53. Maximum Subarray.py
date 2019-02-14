"""
Description:
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach,
which is more subtle.

Runtime: 44 ms, faster than 95.25% of Python3 online submissions for Maximum Subarray.
Memory Usage: 13 MB, less than 100.00% of Python3 online submissions for Maximum Subarray.
"""

class Solution:
    def maxSubArray(self, nums: 'List[int]') -> 'int':
        current, maxTotal = 0, -2147483648
        for n in nums:
            current += n
            if current < 0:
                current = 0
            maxTotal = max(current, maxTotal)