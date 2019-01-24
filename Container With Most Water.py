"""
Description:
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai).
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).
Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

Example:

Input: [1,8,6,2,5,4,12,3,7]
Output: 49

Sigh... with one hour eclapsed, still not figure out the question. Here is best answer in the discuss section:


I've seen some "proofs" for the common O(n) solution, but I found them very confusing and lacking.
Some even didn't explain anything but just used lots of variables and equations and were like "Tada! See?".
I think mine makes more sense:

Idea / Proof:

The widest container (using first and last line) is a good candidate, because of its width.
Its water level is the height of the smaller one of first and last line.
All other containers are less wide and thus would need a higher water level in order to hold more water.
The smaller one of first and last line doesn't support a higher water level and can thus be safely removed from further consideration.

class Solution:
    def maxArea(self, height):
        i, j = 0, len(height) - 1
        water = 0
        while i < j:
            water = max(water, (j - i) * min(height[i], height[j]))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return water

Got thought of using first and last element as the good initial candidate, but the traversal processing not make it clear...
My mistake is making right as the fixed point, then traverse the left point, find each biggest water of right point.
Not make good use of implict condition 'the shortest as the valid height', and I try to compare the latter one at the
traversal period, just make all compare of the possible biggest water.
"""


class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        area = 0
        # assume the biggest area is by two side, that makes the length is biggest,
        # initialize the left side at the point next to left side
        maxLeftHeight, maxLeftIdx = -1, -1
        for rightIdx in range(len(height)-1, -1, -1):
            for leftIdx in range(rightIdx):
                pass

        return area



if __name__ == '__main__':
    pass
