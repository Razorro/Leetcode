"""
Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

Runtime: 56 ms, faster than 99.17% of Python3 online submissions for Merge Intervals.
Memory Usage: 14.9 MB, less than 100.00% of Python3 online submissions for Merge Intervals.

Nice shoot! With many solutions, I tried to fix the start points, and iterate from all those points,
with that preparation, we can easily describe the process of code.
"""


# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


    def __repr__(self):
        return '(%s, %s)' % (self.start, self.end)

class Solution:
    def merge(self, intervals: 'List[Interval]') -> 'List[Interval]':
        if len(intervals) <= 1:
            return intervals

        intervals = sorted(intervals, key=lambda e: e.start)
        i = 0
        collector = []
        fixed = intervals[0]
        while i < len(intervals):
            if fixed is None:
                fixed = intervals[i]
            if i == len(intervals) - 1:
                collector.append(fixed)
                break

            if fixed.end < intervals[i + 1].start:
                collector.append(fixed)
                i += 1
                fixed = None
            else:
                fixed.end = max(fixed.end, intervals[i + 1].end)
                i += 1

        return collector


if __name__ == '__main__':
    a = [Interval(1,4), Interval(4,5),]
    s = Solution()
    print(s.merge(a))