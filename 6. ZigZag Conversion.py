"""
Description:
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
(you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:
"""

class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        charOrders = {}
        curRow, curCol = 0, 0
        flag = '+'
        for ch in s:
            charOrders.setdefault(curRow, []).append(ch)
            if flag == '+':
                curRow += 1
                if curRow == numRows-1:
                    flag = '-'
            else:
                curRow -= 1
                if curRow == 0:
                    flag = '+'

        ret = ''
        for part in charOrders.values():
            ret += ''.join(part)
        return ret


if __name__ == '__main__':
    s = Solution()
    print(s.convert("PAYPALISHIRING", 3))