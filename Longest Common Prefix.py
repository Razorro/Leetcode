"""
Description:
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"], ["aca","cba"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.
"""


class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ''

        prefix = strs[0]
        for s in strs[1:]:
            common = []
            for i in range(min(len(prefix), len(s))):
                if prefix[i] == s[i]:
                    common.append(s[i])
                else:
                    break

            if len(common) < len(prefix):
                prefix = ''.join(common)

        return prefix


if __name__ == '__main__':
    s = Solution()
    print(s.longestCommonPrefix(["aca","cba"]))