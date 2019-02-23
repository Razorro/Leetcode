"""
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in
complexity O(n).

Example:

Input: S = "ADOBECACEBANC", T = "ABCC"
Output: "BANC"
Note:

If there is no such window in S that covers all characters in T, return the empty string "".
If there is such window, you are guaranteed that there will always be only one unique minimum window in S.

执行用时: 112 ms, 在Minimum Window Substring的Python3提交中击败了93.50% 的用户
内存消耗: 6.9 MB, 在Minimum Window Substring的Python3提交中击败了67.31% 的用户

Not totally figure out the problem...
Can't get a clear solution in this problem, must find those point that block me.
Maybe I'm restrain by the condition 'use O(n) time complex', I can just take a step
back, without the condition, how can I solve the problem?
The following solution are really similar, but in the check point that complish the
target string, the logic get strange, not make clean of that.

It turns out that the iteration procedure is not clear, pity that I'm not deal with it solely.
"""


class Solution:
    def minWindow(self, s: 'str', t: 'str') -> 'str':
        from collections import defaultdict
        d = defaultdict(int)
        for i in t:
            d[i] += 1

        m, l, ml, cnt = 2 ** 30, 0, 0, 0
        for r in range(len(s)):
            c = s[r]
            if c in d:
                cnt = cnt + 1 if d[c] > 0 else cnt
                d[c] -= 1
            while cnt == len(t):
                if r - l < m:
                    m = r - l
                    ml = l
                c2 = s[l]
                if c2 in d:
                    if d[c2] >= 0:          # overload character process
                        cnt -= 1
                    d[c2] += 1
                l += 1
        return '' if m == 2 ** 30 else s[ml:ml + m + 1]


if __name__ == '__main__':
    s = Solution()
    print(s.minWindow("ADOBECODEBANC", 'ABC'))