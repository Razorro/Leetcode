# encoding=utf8

"""
Description 28
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().

Got a bunch of time to figure out the problem, that just the usage of Knuth-Morris-Pratt algorithm.
Need to review the algorithm... Hold the control of every detail deduction, that the charming place when I learn how to
solve a problem by programming


Time complexity table
Algorithm          Preprocessing time                   Matching time
----------------------------------------------------------------------
Native                    0                             O((n - m +1)m)
Rabin-Karp              Θ(m)                           O((n - m +1)m)
Finite automation       O(m|∑|)                        Θ(n)
Knuth-Morris-Pratt      Θ(m)                           Θ(n)

The key thing is, when the pattern is not matched, we preprocess the max valid shift, that save quite a lot comparison
Π[q] = max{k : k < q and Pk suffix to Pq}
"""


class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(needle) == 0:
            return 0

        shift = self.computePrefix(needle)
        q = 0
        for i in range(len(haystack)):
            while q > 0 and needle[q] != haystack[i]:
                q = shift[q-1]

            if needle[q] == haystack[i]:
                q += 1

            if q == len(needle):
                return i-len(needle)+1
        else:
            return -1

    def computePrefix(self, needle):
        shift = [0] * len(needle)
        k = 0                                   # number of characters matched
        for q in range(1, len(needle)):
            while k > 0 and needle[k] != needle[q]:
                k = shift[k-1]                    # next character does not match
            if needle[k] == needle[q]:
                k += 1
            shift[q] = k
        return shift


if __name__ == '__main__':
    s = Solution()
    print(s.strStr("aaaaa", "bba"))