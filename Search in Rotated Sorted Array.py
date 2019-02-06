"""
Description 33:
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

Damn it! I try to firstly find the pivot of the array, and then use standard binary search to find whether the
target is in array. That makes trivial condition judgement.

The fact is, when you notice the binary search condition processing, you can easily modify the procedure of
binary searching, almost get there, but without deeper thinking, I discard the clue.

"""

class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        head, tail = 0, len(nums)-1
        while head <= tail:
            pivot = (head+tail) // 2
            if nums[pivot] == target:
                return pivot

            if nums[pivot] > target:
                if nums[pivot] > target >= nums[tail]:
                    tail = pivot - 1
                elif nums[pivot] > nums[tail] > target:
                    head = pivot + 1
                else:
                    tail = pivot - 1
            else:
                if nums[pivot] < nums[tail] <= target:
                    head = pivot + 1
                else:
                    tail = pivot - 1

        return -1



if __name__ == '__main__':
    s = Solution()
    print(s.search([3,1], 1))