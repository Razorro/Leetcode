"""
Description:
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

[1,2,3,4] -> [1,2,4,3] -> [1,3,2,4] -> [1,3,4,2]

Runtime: 76 ms, faster than 20.77% of Python3 online submissions for Permutations.
Memory Usage: 12.7 MB, less than 0.87% of Python3 online submissions for Permutations.

with very low speed get AC...

Here is the answer of StefanPochmann:
Solution 1: Recursive, take any number as first

Take any number as the first number and append any permutation of the other numbers.

def permute(self, nums):
    return [[n] + p
            for i, n in enumerate(nums)
            for p in self.permute(nums[:i] + nums[i+1:])] or [[]]
Solution 2: Recursive, insert first number anywhere

Insert the first number anywhere in any permutation of the remaining numbers.

def permute(self, nums):
    return nums and [p[:i] + [nums[0]] + p[i:]
                     for p in self.permute(nums[1:])
                     for i in range(len(nums))] or [[]]
Solution 3: Reduce, insert next number anywhere

Use reduce to insert the next number anywhere in the already built permutations.

def permute(self, nums):
    return reduce(lambda P, n: [p[:i] + [n] + p[i:]
                                for p in P for i in range(len(p)+1)],
                  nums, [[]])
Solution 4: Using the library

def permute(self, nums):
    return list(itertools.permutations(nums))
That returns a list of tuples, but the OJ accepts it anyway. If needed, I could easily turn it into a list of lists:

def permute(self, nums):
    return map(list, itertools.permutations(nums))
"""


class Solution:
    def permute(self, nums: 'List[int]') -> 'List[List[int]]':
        head = len(nums) - 2
        collector = [list(nums)]
        nums_up, nums_down = list(nums), list(nums)
        while head >= 0:
            tail = len(nums_up) - 1
            while tail > head:
                if nums_up[tail] > nums_up[head]:
                    nums_up[tail], nums_up[head] = nums_up[head], nums_up[tail]
                    nums_up = nums_up[:head+1] + sorted(nums_up[head+1:])
                    head = len(nums_up) - 1
                    collector.append(list(nums_up))
                    break
                tail -= 1
            head -= 1

        head = len(nums) - 1
        while head >= 0:
            tail = len(nums_down) - 1
            while tail > head:
                if nums_down[tail] < nums_down[head]:
                    nums_down[tail], nums_down[head] = nums_down[head], nums_down[tail]
                    nums_down = nums_down[:head+1] + sorted(nums_down[head+1:], reverse=True)
                    head = len(nums_down) - 1
                    collector.append(list(nums_down))
                    break
                tail -= 1
            head -= 1
        return collector


if __name__ == '__main__':
    s = Solution()
    print(s.permute([0,-1,1]))