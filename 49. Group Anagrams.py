"""
Description:
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.

Runtime: 152 ms, faster than 39.32% of Python3 online submissions for Group Anagrams.
Memory Usage: 15.5 MB, less than 100.00% of Python3 online submissions for Group Anagrams.

Not very fast, but I guess all the answer comply the rule:
Make unique hash value of those same anagrams.
"""


class Solution:
    def groupAnagrams(self, strs: 'List[str]') -> 'List[List[str]]':
        import collections
        h = collections.defaultdict(list)
        for s in strs:
            h[''.join(sorted(s))].append(s)
        return list(h.values())

        return list(collectorDict.values())