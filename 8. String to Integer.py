"""
Description:
Implement atoi which converts a string to an integer.

The function first discards as many whitespace characters as necessary until the first non-whitespace character is found.
Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits
as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no
 effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number,
or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.

Note:

Only the space character ' ' is considered as whitespace character.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1].
If the numerical value is out of the range of representable values, INT_MAX (2^31 − 1) or INT_MIN (−2^31) is returned.
"""


class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if len(str) == 0:
            return 0

        constant = 2**31
        gather = []
        signFlag = None
        numericCh = {e for e in range(48, 58)}         # ASCII
        for ch in str:
            if ch == ' ' and signFlag is None:
                continue

            if ord(ch) in numericCh:
                if signFlag is None:
                    signFlag = '+'
                gather.append(ch)
            else:
                if signFlag is None and (ch == '+' or ch == '-'):
                    signFlag = ch
                    continue
                else:
                    break

        if signFlag is None or len(gather) == 0:
            return 0


        if signFlag == '+':
            strNum = ''.join(gather)
            return min(constant-1, int(strNum))
        else:
            strNum = signFlag + ''.join(gather)
            return max(-constant, int(strNum))