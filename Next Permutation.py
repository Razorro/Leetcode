"""
Description 31:
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1

After several times error and trials, finally get result...
Runtime: 44 ms, faster than 99.50% of Python3 online submissions for Next Permutation.

Problem is kind of easy, but the obtacle block my mind is how to clearly claim the relationship between the permutation arrangement.
That's the crucial part. Yes, use language to clearly describe the action of every detail.
"""


class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        head = len(nums)-2
        while head >= 0:
            for tail in range(len(nums)-1, head, -1):
                if nums[tail] > nums[head]:
                    nums[head], nums[tail] = nums[tail], nums[head]
                    start, end = head+1, len(nums)-1
                    while start < end:
                        nums[start], nums[end] = nums[end], nums[start]
                        start += 1
                        end -= 1
                    return
            else:
                head -= 1

        nums.sort()




if __name__ == '__main__':
    s = Solution()
    a = [4,2,0,2,3,2,0]
    s.nextPermutation(a); print(a)
