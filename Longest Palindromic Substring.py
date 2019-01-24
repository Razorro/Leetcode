"""
Description:
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

The key is pivot, I thought. So, just traverse the string with each char as the pivot, need to notice that you may choose
the ch itself as the pivot, or the middle between current char and the char right next.
"""


class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) <= 1:
            return s

        ret = [0, 0]
        for pivot_idx in range(len(s)):
            # mirrored at itself
            left, right = pivot_idx-1, pivot_idx+1
            while left >= 0 and right < len(s):
                if s[left] != s[right]:
                    break
                left -= 1
                right += 1

            if right-left-2 > ret[1] - ret[0]:
                ret[0] = left+1
                ret[1] = right-1

            # mirrored at the left side
            left, right = pivot_idx, pivot_idx+1
            while left >= 0 and right < len(s):
                if s[left] != s[right]:
                    break
                left -= 1
                right += 1

            if right-left-2 < 0:
                continue

            if right - left - 2 > ret[1] - ret[0]:
                ret[0] = left+1
                ret[1] = right-1

        return s[ret[0]:ret[1]+1]


if __name__ == '__main__':
    testCase = [
        "babad", ('bab', 'aba'),
        "cbbd", ('bb',),
        "baabc", ('baab',),
        "bb", ('bb',),
    ]

    s = Solution()
    for i in range(len(testCase)//2):
        dataIdx = 2*i
        answerIdx = 2*i+1
        ret = s.longestPalindrome(testCase[dataIdx])
        print(ret, ret in testCase[answerIdx])