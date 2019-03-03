"""
Given a string containing only digits, restore it by returning all possible valid IP address combinations.

Example:

Input: "25525511135"
Output: ["255.255.11.135", "255.255.111.35"]

Runtime: 44 ms, faster than 64.95% of Python3 online submissions for Restore IP Addresses.
Memory Usage: 13.2 MB, less than 5.16% of Python3 online submissions for Restore IP Addresses.


Normal backtracking.
"""


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result = []
        current = []
        self.collect(s, 0, result, current)
        return result

    def collect(self, s, idx, result, current):
        if idx > len(s):
            return

        if len(current) == 4 and idx < len(s):
            return

        if idx == len(s):
            if len(current) == 4:
                result.append('.'.join(current))
            return

        current.append(s[idx])
        self.collect(s, idx + 1, result, current)
        current.pop()

        if idx + 1 < len(s) and s[idx] > '0':
            current.append(s[idx:idx + 2])
            self.collect(s, idx + 2, result, current)
            current.pop()

        if idx + 2 < len(s) and s[idx:idx + 3] <= '255' and s[idx] != '0':
            current.append(s[idx:idx + 3])
            self.collect(s, idx + 3, result, current)
            current.pop()