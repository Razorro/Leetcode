"""
Description 32:
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

Example 1:

Input: "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()"
Example 2:

Input: "((()()))"
Output: 4
Explanation: The longest valid parentheses substring is "()()"

"()(()"
"(()"

I made it! When I occur the hard level problem, always think that it surpass my ability to solve it.
It turns out, as you carefully clear the path of the problem, the left is only the implementation.

Runtime: 52 ms, faster than 68.84% of Python3 online submissions for Longest Valid Parentheses.
"""


def test(s):
    remain = []
    for i in range(len(s)):
        if s[i] == '(':
            remain.append(i)
        elif len(remain):
            remain.pop()
        else:
            return remain

    return remain

class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        return self._checkMaxLen(s, 0, len(s)-1)

    def _checkMaxLen(self, s, start, end):
        if start >= len(s):
            return 0

        if end - start <= 1:
            return 2 if s[start] == '(' and s[end] == ')' else 0

        remains = []
        invalidIdx = None

        for i in range(start, end+1):
            if s[i] == '(':
                remains.append(i)
            elif len(remains) > 0:
                remains.pop()
            else:
                invalidIdx = i
                break

        if len(remains):
            left = remains[0] - start
            middle = 0
            for k in range(len(remains)-1):
                middle = max(middle, (remains[k+1]-remains[k]-1))
            maxLen = max(left, middle, self._checkMaxLen(s, remains[-1]+1, end))
        elif invalidIdx is not None:
            left = invalidIdx - start
            maxLen = max(left, self._checkMaxLen(s, invalidIdx+1, end))
        else:
            maxLen = end - start + 1

        return maxLen


if __name__ == '__main__':
    s = Solution()
    print(s.longestValidParentheses(")(((((()())()()))()(()))("))
