"""
Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

Example:

Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST's:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3


Just passed the problem, not figured out the solution.
Still not good at DP, so let's review the DP steps from CLRS:

When developing a dynamic-programming algorithm, we follow a sequence of four steps:
1. Characterize the structure of an optimal solution.
2. Recursively define the value of an optimal solution.
3. Compute the value of an optimal solution, typically in a bottom-up fashion.
4. Construct an optimal solution from computed information

The first approach is top-down with memoization.In this approach, we write
the procedure recursively in a natural manner, but modified to save the result of
each subproblem (usually in an array or hash table). The procedure now first checks
to see whether it has previously solved this subproblem. If so, it returns the saved
value, saving further computation at this level; if not, the procedure computes the
value in the usual manner. We say that the recursive procedure has been memoized;
it “remembers” what results it has computed previously.
The second approach is the bottom-up method. This approach typically depends
on some natural notion of the “size” of a subproblem, such that solving any particular subproblem depends only on solving “smaller” subproblems. We sort the
subproblems by size and solve them in size order, smallest first. When solving a
particular subproblem, we have already solved all of the smaller subproblems its
solution depends upon, and we have saved their solutions. We solve each subproblem only once, and when we first see it, we have already solved all of its
prerequisite subproblems
"""


class Solution:
    memo = [0, 1, 2]  # used for storing base solutions

    def countBST(self, n):
        if n <= (len(self.memo) - 1):  # base case
            return self.memo[n]
        count = 2 * self.countBST(n - 1)  # cal recursively for taking care of edge cases

        # core of the problem
        for i in range(1, n - 1):
            count = count + (self.memo[i] * self.memo[n - i - 1])

        # append the freshly calculted value
        self.memo.append(count)
        return count

    def numTrees(self, n: int) -> int:
        return self.countBST(n)