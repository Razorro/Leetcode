"""
Description 18:
Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target?
Find all unique quadruplets in the array which gives the sum of target.

Note:

The solution set must not contain duplicate quadruplets.

Example:

Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2],
]

My solution is no matter how many nums to be calculated, I break down the question to two part:
First pick a number, and then recursively shrink the account of needed nums, as it make to find the last two
numbers need accumulate to be the targe, great! that's the familiar problem we've shooted already.

But the speed is not the ideal...
Runtime: 1128 ms, faster than 36.05% of Python3 online submissions for 4Sum.

A better solution I find online, but the idea is quit same...
I guess just making the index move forward is a little bit trivial...
Noooooooo!!!
Not make use of the 'sorted' condition, to filter those already not fulfill target traversal

def fourSum(self, nums, target):
    nums.sort()
    results = []
    self.findNsum(nums, target, 4, [], results)
    return results

def findNsum(self, nums, target, N, result, results):
    if len(nums) < N or N < 2: return

    # solve 2-sum
    if N == 2:
        l,r = 0,len(nums)-1
        while l < r:
            if nums[l] + nums[r] == target:
                results.append(result + [nums[l], nums[r]])
                l += 1
                r -= 1
                while l < r and nums[l] == nums[l - 1]:
                    l += 1
                while r > l and nums[r] == nums[r + 1]:
                    r -= 1
            elif nums[l] + nums[r] < target:
                l += 1
            else:
                r -= 1
    else:
        for i in range(0, len(nums)-N+1):   # careful about range
            if target < nums[i]*N or target > nums[-1]*N:  # take advantages of sorted list
                break
            if i == 0 or i > 0 and nums[i-1] != nums[i]:  # recursively reduce N
                self.findNsum(nums[i+1:], target-nums[i], N-1, result+[nums[i]], results)
    return
"""


class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def _fourSum(nums, curIdx, coll, gather, target):
            if len(gather) == 2:
                right = len(nums) - 1
                middle = curIdx
                while middle < right:
                    if nums[middle] + nums[right] > target:
                        while right > middle and nums[right] == nums[right - 1]: right -= 1
                        right -= 1
                    elif nums[middle] + nums[right] < target:
                        while middle < right and nums[middle] == nums[middle + 1]: middle += 1
                        middle += 1
                    else:
                        coll.append([*gather, nums[middle], nums[right]])
                        while middle < right and nums[middle] == nums[middle + 1]: middle += 1
                        middle += 1
                return

            while curIdx < len(nums) - (3-len(gather)):
                # forget to use the sorted condition...
                if target < nums[curIdx]*(4-len(gather)) or target > nums[-1]*(4-len(gather)):
                    return

                gather.append(nums[curIdx])
                _fourSum(nums, curIdx+1, coll, gather, target-nums[curIdx])
                gather.pop()

                while curIdx < len(nums)-(3-len(gather)) and nums[curIdx] == nums[curIdx + 1]: curIdx += 1
                curIdx += 1

        nums.sort()
        coll = []
        _fourSum(nums, 0, coll, [], target)
        return coll


if __name__ == '__main__':
    s = Solution()
    print(s.fourSum([1, 0, -1, 0, -2, 2], 0))
