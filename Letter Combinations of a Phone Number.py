"""
Description 17:
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:

Although the above answer is in lexicographical order, your answer could be in any order you want.

Reslut:
Runtime: 32 ms, faster than 100.00% of Python3 online submissions for Letter Combinations of a Phone Number.

It seems pretty clear.
"""


class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
            return []

        key2char = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }

        ret = []
        def _backtracking(i, answer):
            if i >= len(digits):
                ret.append(answer)
                return

            charLst = key2char[digits[i]]
            for char in charLst:
                newAnswer = answer + char
                _backtracking(i+1, newAnswer)

        _backtracking(0, '')
        return ret


if __name__ == '__main__':
    s = Solution()
    print(s.letterCombinations("23"))