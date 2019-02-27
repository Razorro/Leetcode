"""
We have two special characters. The first character can be represented by one bit 0. The second character can be
represented by two bits (10 or 11).

Now given a string represented by several bits. Return whether the last character must be a one-bit character or not.
The given string will always end with a zero.

Example 1:
Input:
bits = [1, 0, 0]
Output: True
Explanation:
The only way to decode it is two-bit character and one-bit character. So the last character is one-bit character.
Example 2:
Input:
bits = [1, 1, 1, 0]
Output: False
Explanation:
The only way to decode it is two-bit character and two-bit character. So the last character is NOT one-bit character.


I dont' think this problem gonna make any knowledge challenage...
"""


class Solution:
    def isOneBitCharacter(self, bits: 'List[int]') -> bool:
        i = 0
        while i < len(bits):
            if bits[i] != 0:
                i += 2
            else:
                if i == len(bits) - 1:
                    return True
                else:
                    i += 1
        else:
            return False
