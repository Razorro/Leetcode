"""
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list,
and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.

Runtime: 36 ms, faster than 99.44% of Python3 online submissions for Plus One.
Memory Usage: 12.3 MB, less than 100.00% of Python3 online submissions for Plus One

Without tricks, just normal plus
"""

class Solution:
    def plusOne(self, digits: 'List[int]') -> 'List[int]':
        i = len(digits)-1
        carry = 0
        while i >= 0:
            digits[i] += 1
            if digits[i] >= 10:
                digits[i] %= 10
                carry = 1
            else:
                carry = 0
                break
            i -= 1

        if i == -1 and carry:
            digits.insert(0, 1)

        return digits