"""
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

Example:

Input: "Hello World"
Output: 5

Runtime: 36 ms, faster than 75.73% of Python3 online submissions for Length of Last Word.
Memory Usage: 12.5 MB, less than 100.00% of Python3 online submissions for Length of Last Word.

Without any trick...
"""


class Solution:
    def lengthOfLastWord(self, s: 'str') -> 'int':
        count = 0
        for i in range(len(s)):
            if s[i] != ' ':
                count += 1
            elif i < len(s)-1 and s[i+1] != ' ':
                count = 0

        return count