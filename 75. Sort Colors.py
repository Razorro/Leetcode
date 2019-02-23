"""
Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color
are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.

Example:

Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Follow up:

A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total
number of 0's, then 1's and followed by 2's.
Could you come up with a one-pass algorithm using only constant space?

执行用时: 44 ms, 在Sort Colors的Python3提交中击败了100.00% 的用户
内存消耗: 6.5 MB, 在Sort Colors的Python3提交中击败了73.59% 的用户

I don't think this question has any prictical meaning, the complex only need to add one more full iteration, but the
algorithm not worth the exchange of readability and efficiency
"""


class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        zero, two = -1, len(nums)
        i = 0
        while i < two:
            while nums[i] != 1 and two-zero > 1:
                if nums[i] == 0:
                    if zero == i:
                        break
                    zero += 1
                    nums[i], nums[zero] = nums[zero], nums[i]
                elif nums[i] == 2:
                    if two == i:
                        break
                    two -= 1
                    nums[i], nums[two] = nums[two], nums[i]

            i += 1

        return nums


if __name__ == '__main__':
    s = Solution()
    print(s.sortColors([2,0,2,1,1,0]))