"""
Description 42:
Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it is able to trap after raining.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case,
6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6

The key is, find the logic of how it counts as the valid water trapper? Need to observe more clearly,
Not AC the last test because of time, my answer really is not a very efficient way, the following answer is
from Adeath's solution:


Indeed this question can be solved in one pass and O(1) space, but it's probably hard to come up with in a short interview.
If you have read the stack O(n) solution for Largest Rectangle in Histogram, you will find this solution is very very similar.

The main idea is : if we want to find out how much water on a bar(bot), we need to find out the left larger bar's
index (il), and right larger bar's index(ir), so that the water is (min(A[il],A[ir])-A[bot])*(ir-il-1),
use min since only the lower boundary can hold water, and we also need to handle the edge case that there is no il.

To implement this we use a stack that store the indices with decreasing bar height, once we find a bar who's height is
larger, then let the top of the stack be bot, the cur bar is ir, and the previous bar is il.

That's a really genius, make perfect usage of stack and the logic is very clear.
"""


class Solution:
    def trap(self, height: 'List[int]') -> 'int':
        water = 0
        left = None
        remain = {idx: trapper for idx, trapper in enumerate(height) if trapper > 0}
        while len(remain):
            dismiss = []
            for idx in sorted(remain.keys()):
                if left is None:
                    left = idx
                elif idx - left == 1:
                    left = idx
                else:
                    water += idx - left - 1
                    left = idx

                remain[idx] -= 1
                if remain[idx] == 0:
                    dismiss.append(idx)

            for idx in dismiss:
                del remain[idx]
            left = None

        return water

    def trapAns(self, height):
        if len(height) == 0:
            return 0

        stack = []
        i, maxWater, maxBotWater = 0, 0, 0
        while i < len(height):
            if len(stack) == 0 or height[i] <= height[stack[-1]]:
                stack.append(i)
                i += 1
            else:
                bot = stack.pop()
                maxBotWater = 0 if len(stack) == 0 else (min(height[stack[-1]], height[i])-height[bot])*(i-stack[-1]-1)
                maxWater += maxBotWater

        return maxWater

if __name__ == '__main__':
    s = Solution()
    print(s.trapAns([0,1,0,2,1,0,1,3,2,1,2,1]))