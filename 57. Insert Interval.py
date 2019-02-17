"""
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

Runtime: 52 ms, faster than 98.46% of Python3 online submissions for Insert Interval.
Memory Usage: 16 MB, less than 100.00% of Python3 online submissions for Insert Interval.

Same as the Question56, just use the case of 56
"""


# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __repr__(self):
        return '(%s, %s)' % (self.start, self.end)

class Solution:
    def insert(self, intervals: 'List[Interval]', newInterval: 'Interval') -> 'List[Interval]':
        intervals.append(newInterval)
        intervals = sorted(intervals, key=lambda e: e.start)
        print(intervals)
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
    a = [[1,2],[3,5],[6,7],[8,10],[12,16]]
    b = [4,8]
    test = [Interval(x, y) for x, y in a]
    insertNode = Interval(b[0], b[1])
    s = Solution()
    print(s.insert(test, insertNode))