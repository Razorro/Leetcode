"""
Description 38:
The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.

 

Example 1:

Input: 1
Output: "1"
Example 2:

Input: 4
Output: "1211"

Just that simple...
"""


class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
		count, data = 1, '1'
        while count < n:
            new_data = ''
            num, head = 1, data[0]
            for i in range(1, len(data)):
                if data[i] == head:
                    num += 1
                else:
                    new_data += str(num) + str(head)
                    num = 1
                    head = data[i]
            data = new_data + str(num) + str(head)
            count += 1
            
        return data