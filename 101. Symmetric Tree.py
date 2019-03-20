"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3



执行用时 : 60 ms, 在Symmetric Tree的Python3提交中击败了46.11% 的用户
内存消耗 : 13.3 MB, 在Symmetric Tree的Python3提交中击败了0.87% 的用户


Not very good, the idea is clear, use BFS to scan each row of the tree.
The recursive way looks much clean for the iterative way...
So, rather prefer the recursive one.

But the recursive one seems not good at both efficiency and space...
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True

        deq = [root.left, root.right]
        while deq:
            head, tail = 0, len(deq) - 1
            leftL, rightL = [], []
            while head < tail:
                if deq[head] is None or deq[tail] is None:
                    if deq[head] is deq[tail]:
                        head += 1
                        tail -= 1
                        continue
                    else:
                        return False

                if deq[head].val != deq[tail].val:
                    return False

                leftL = leftL + [deq[head].left, deq[head].right]
                rightL = [deq[tail].left, deq[tail].right] + rightL

                head += 1
                tail -= 1

            deq = leftL + rightL

        return True
