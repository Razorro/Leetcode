"""
Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.

You have the following 3 operations permitted on a word:

Insert a character
Delete a character
Replace a character
Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation:
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation:
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')

A good question! I thought it was similiar with the dynamic programming example in CLRS,
it turns out the skeleton may has a little similiarity, but the core idea can't be extracted
with the situation of this question.

It was called Levenshtein distance.
Mathematically, the Levenshtein distance between two strings {\displaystyle a,b} a,b (of length {\displaystyle |a|} |a| and {\displaystyle |b|} |b| respectively) is given by {\displaystyle \operatorname
{lev} _{a,b}(|a|,|b|)} \operatorname{lev}_{a,b}(|a|,|b|) where
            | --- max(i, j)               if min(i, j) = 0
lev(i, j) = | min --- lev(i-1, j) + 1
               |  --- lev(i, j-1) + 1
               |  --- lev(i-1, j-1) + 1


Computing the Levenshtein distance is based on the observation that if we reserve a matrix to hold the Levenshtein distances
between all prefixes of the first string and all prefixes of the second, then we can compute the values in the matrix in
a dynamic programming fashion, and thus find the distance between the two full strings as the last value computed.

This algorithm, an example of bottom-up dynamic programming, is discussed, with variants, in the 1974 article The
String-to-string correction problem by Robert A. Wagner and Michael J. Fischer.[4]
"""


class Solution:
    def minDistance(self, word1: 'str', word2: 'str') -> 'int':
        points = self.findBiggestCommon(word1, word2)

    def findBiggestCommon(self, source, target):
        path = [0] * len(source)
        directions = []
        for i in range(len(target)):
            current = [0] * len(source)
            d = []
            for j in range(len(source)):
                if target[i] == source[j]:
                    current[j] = path[j-1] + 1 if j-1 >= 0 else 1
                    d.append('=')
                else:
                    left = current[j-1] if j-1 >= 0 else 0
                    if left > path[j]:
                        d.append('l')
                    else:
                        d.append('u')
                    current[j] = max(left, path[j])
            path = current
            directions.append(d)

        x_y = []
        row, col = len(target)-1, len(source)-1
        while row >= 0 and col >=0:
            if directions[row][col] == '=':
                x_y.append((row, col))
                row -= 1
                col -= 1
            elif directions[row][col] == 'u':
                row -= 1
            else:
                col -= 1
        return x_y

    def standardAnswer(self, word1, word2):
        m = len(word1) + 1
        n = len(word2) + 1
        det = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            det[i][0] = i
        for i in range(n):
            det[0][i] = i
        for i in range(1, m):
            for j in range(1, n):
                det[i][j] = min(det[i][j - 1] + 1, det[i - 1][j] + 1, det[i - 1][j - 1] +
                                                0 if word1[i - 1] == word2[j - 1] else 1)
        return det[m - 1][n - 1]


if __name__ == '__main__':
    s = Solution()
    distance = s.findBiggestCommon('horse', 'ros')
    distance = sorted(distance, key=lambda e: e[1])
    c = 0
    trans = 0
    for left, right in distance:
        trans += abs(right - left) + left-c
        c = left + 1
    print(s.findBiggestCommon('horse', 'ros'))