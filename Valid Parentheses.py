"""
Description 20:
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:
Input: "()"
Output: true

Example 2:
Input: "()[]{}"
Output: true

Example 3:
Input: "([)]"
Output: false

Bravo!!!
Runtime: 32 ms, faster than 100.00% of Python3 online submissions for Valid Parentheses.
"""


class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        leftP = {'[', '(', '{'}
        rightP = {']': '[', '}': '{', ')': '('}
        stack = []
        for p in s:
            if p in leftP:
                stack.append(p)
            else:
                if len(stack) == 0 or rightP[p] != stack[-1]:
                    return False
                else:
                    stack.pop()

        if len(stack):
            return False
        else:
            return True