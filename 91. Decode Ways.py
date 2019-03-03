"""
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.

Example 1:

Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).
Example 2:

Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).


执行用时: 60 ms, 在Decode Ways的Python3提交中击败了45.38% 的用户
内存消耗: 13.4 MB, 在Decode Ways的Python3提交中击败了0.00% 的用户

Although the both the efficiencies are not good, but the idea is same, we can easily get that
F(n) = F(n-1) + F(n-2), but with some condition:
For one character, it can't be 0, for there is no alphabet matched one
For two characters, it must greater equal to 10 and less equal to 26 for matching the alphabet

First it can be easily conducted to DFS, but out of limit time, so DP can be a great optimum method,
but I stuck at how to describle the repeated subproblems.
Always not good at DP programs, still not grasp the tricky part that with a right direction to
cut in. The core concept is repeated subproblems, just dunno why it's such a problem not make a
problem clear.
"""


class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s) == 0:
            return

        record = {-1: 1 if 10 <= int(s[:2]) <= 26 else 0, 0: 1 if s[0] != '0' else 0}
        return self.solve(s, record)

    def solve(self, s, record):
        idx = 1
        while idx < len(s):
            if s[idx] != '0':
                single = record[idx - 1]
            else:
                single = 0

            if 10 <= int(s[idx - 1:idx + 1]) <= 26:
                multi = record[idx - 2]
            else:
                multi = 0
            record[idx] = single + multi
            idx += 1

        return record[idx - 1]
