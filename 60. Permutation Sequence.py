"""
The set [1,2,3,...,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Note:

Given n will be between 1 and 9 inclusive.
Given k will be between 1 and n! inclusive.
Example 1:

Input: n = 3, k = 3
Output: "213"
Example 2:

Input: n = 4, k = 9
Output: "2314"

Runtime: 4200 ms, faster than 3.99% of Python3 online submissions for Permutation Sequence.
Memory Usage: 12.3 MB, less than 100.00% of Python3 online submissions for Permutation Sequence

With very slow speed, because I calculate all the possible permutation before k, I thought there is
no other method to avoid the precalculation, got a big mistake...

Here is the smart solution:
def getPermutation(self, n, k):
        nums = [i for i in range(1, n + 1)]
        k -= 1 # So the index starts from 0.
        result = ""

        while n > 1:
            step = math.factorial(n) / n # How big are the groups with the same first digit.
            i, k = divmod(k, step)       # i = Index of the k-th group.
            n -= 1                       # k = Relative position within the next group of permutations made out of digits excluding nums[i].
            result += str(nums[i])
            del nums[i]
        result += str(nums[0])
        return result

Really an amazing answer, with such observation, just cut the problem as clean as it looks.
"""


class Solution:
    def getPermutation(self, n: 'int', k: 'int') -> 'str':
        if n <= 1:
            return '1'[:n]

        data = ['123456789'[i] for i in range(n)]
        permute = 1
        head, tail = n-2, n-1
        while permute < k:
            while head < tail:
                if data[head] < data[tail]:
                    data[head], data[tail] = data[tail], data[head]
                    back = data[head+1:]; back.sort()
                    data = data[:head+1] + back
                    head, tail = n - 2, n - 1
                    permute += 1
                    if permute == k:
                        break
                else:
                    tail -= 1
            head -= 1
            tail = n-1


        return ''.join(data)


if __name__ == '__main__':
    s = Solution()
    print(s.getPermutation(3,3))