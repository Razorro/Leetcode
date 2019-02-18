"""
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"

Runtime: 48 ms, faster than 61.91% of Python3 online submissions for Add Binary.
Memory Usage: 12.5 MB, less than 100.00% of Python3 online submissions for Add Binary.
"""


class Solution:
    def addBinary(self, a: 'str', b: 'str') -> 'str':
        la, lb = len(a), len(b)
        i = -1
        carry = 0
        result = []
        while la > 0 or lb > 0:
            ch1 = a[i] if i >= -len(a) else '0'
            ch2 = b[i] if i >= -len(b) else '0'
            total = int(ch1) + int(ch2) + carry
            carry = total // 2
            result.append(str(total%2))
            la -= 1
            lb -= 1
            i -= 1

        if carry:
            result.append('1')

        result.reverse()
        return ''.join(result)


if __name__ == '__main__':
    s = Solution()
    print(s.addBinary('11', '1'))