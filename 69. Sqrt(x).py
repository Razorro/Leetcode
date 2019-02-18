"""
Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

Example 1:

Input: 4
Output: 2
Example 2:

Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since
             the decimal part is truncated, 2 is returned.

Runtime: 56 ms, faster than 84.74% of Python3 online submissions for Sqrt(x).
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Sqrt(x).

Without too much consideration, commit several wrong answer, the core idea is simple, use binary search to find the most
close answer, the tricky place is how to deal with the integer part.
"""

class Solution:
    def mySqrt(self, x: 'int') -> 'int':
        if x == 1:
            return x

        up, low, trial = x, 0, -1
        while True:
            if trial == (up + low) // 2:
                return trial

            trial = (up + low) // 2
            trialRes = trial * trial

            if trialRes > x:
                up = trial
            elif trialRes < x:
                low = trial

if __name__ == '__main__':
    s = Solution()
    print(s.mySqrt(9))