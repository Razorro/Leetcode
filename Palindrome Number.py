"""
Description:
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.
"""


class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False

        if 0 <= x < 10:
            return True

        strX = str(x)
        i, j = 0, len(strX)-1
        while i < j:
            if strX[i] != strX[j]:
                return False
            i += 1
            j -= 1
        return True


if __name__ == '__main__':
    pass
