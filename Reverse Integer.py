"""
Description:
Given a 32-bit signed integer, reverse digits of an integer.

Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−2^31,  2^31 − 1].
For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

Easy...
Nope... forget to deal with overflow
"""


class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        flag = x < 0
        constant = 2**31
        x = abs(x)
        x = str(x)
        x = x[::-1]
        x = int(x)
        if flag:
            x = -x if x <= constant else 0
        else:
            x = x if x <= constant-1 else 0
        return x


if __name__ == '__main__':
    testCase = [

    ]