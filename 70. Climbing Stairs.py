"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

Runtime: 32 ms, faster than 100.00% of Python3 online submissions for Climbing Stairs.
Memory Usage: 12.5 MB, less than 100.00% of Python3 online submissions for Climbing Stairs.
"""


class Solution:
    def climbStairs(self, n: 'int') -> 'int':
        if n <= 2:
            return n

        s1, s2 = 1,2
        current = 3
        methods = 0
        while current <= n:
            methods = s1 + s2
            s1, s2 = s2, methods
            current += 1

        return methods
