"""
Description:
Given two non-negative integers num1 and num2 represented as strings, return the product
of num1 and num2, also represented as a string.

Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"
Note:

The length of both num1 and num2 is < 110.
Both num1 and num2 contain only digits 0-9.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.
You must not use any built-in BigInteger library or convert the inputs to integer directly.

I thought this kind of problems is not very interesting, but when I look others' answer,
quite still has some details to deal with.

"""


class Solution:
    def multiply(self, num1: 'str', num2: 'str') -> 'str':
        if num1[0] == 0 or num2[0] == 0:
            return '0'

        multiArr = [0] * (len(num1)+len(num2))
        str2num = {
            '0': 0,
            '1': 1,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '9': 9
        }

        for i1 in range(len(num1)):
            for i2 in range(len(num2)):
                multiArr[i1+i2] += str2num[num1[len(num1)-i1-1]] * str2num[num2[len(num2)-i2-1]]
        print(multiArr)
        result = [0] * (len(num1)+len(num2))
        for i in range(len(num1)+len(num2)-1):
            total = multiArr[i] + result[i]
            result[i] = total % 10
            result[i+1] = total // 10

        result = ''.join([str(e) for e in result])[::-1]
        return result if result[0] != '0' else result[1:]


if __name__ == '__main__':
    s = Solution()
    print(s.multiply('123', '456'))