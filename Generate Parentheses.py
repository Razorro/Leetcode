"""
Description 22:
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

Very slow ...
Runtime: 360 ms, faster than 0.99% of Python3 online submissions for Generate Parentheses.


Take a look at others' answer, the following is StefanPochmann's answer:
p is the parenthesis-string built so far, left and right tell the number of left and right parentheses still to add,
and parens collects the parentheses.

Solution 1

I used a few "tricks"... how many can you find? :-)

def generateParenthesis(self, n):
    def generate(p, left, right, parens=[]):
        if left:         generate(p + '(', left-1, right)
        if right > left: generate(p + ')', left, right-1)
        if not right:    parens += p,
        return parens
    return generate('', n, n)


Solution 2

Here I wrote an actual Python generator. I allow myself to put the yield q at the end of the line because it's not that
bad and because in "real life" I use Python 3 where I just say yield from generate(...).

def generateParenthesis(self, n):
    def generate(p, left, right):
        if right >= left >= 0:
            if not right:
                yield p
            for q in generate(p + '(', left-1, right): yield q
            for q in generate(p + ')', left, right-1): yield q
    return list(generate('', n, n))


Solution 3

Improved version of this. Parameter open tells the number of "already opened" parentheses, and I continue the
recursion as long as I still have to open parentheses (n > 0) and I haven't made a mistake yet (open >= 0).

def generateParenthesis(self, n, open=0):
    if n > 0 <= open:
        return ['(' + p for p in self.generateParenthesis(n-1, open+1)] + \
               [')' + p for p in self.generateParenthesis(n, open-1)]
    return [')' * open] * (not n)
"""


class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0:
            return ''

        gather = set()
        self._generateor('()', 1, n, gather)
        return list(gather)

    def _generateor(self, curStr, curNum, n, gather):
        if curNum == n:
            gather.add(curStr)
            return

        for i in range(len(curStr)):
            newStr = curStr[:i] + '()' + curStr[i:]
            self._generateor(newStr, curNum+1, n, gather)


if __name__ == '__main__':
    s = Solution()
    print(s.generateParenthesis(3))