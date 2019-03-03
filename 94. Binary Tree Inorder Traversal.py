"""
Given a binary tree, return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
Follow up: Recursive solution is trivial, could you do it iteratively?


Runtime: 36 ms, faster than 75.59% of Python3 online submissions for Binary Tree Inorder Traversal.
Memory Usage: 13 MB, less than 5.64% of Python3 online submissions for Binary Tree Inorder Traversal.


The recursion version is easy, just a common inorder traversal, but got stuck in iterative style.

It got me lots time to deal with the backtracking process, for after the left node of some node's traversal,
not figured out quickly how to avoid dead loop of looking from left to right, still, I modified the left node,
it may destroy the original data.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        self.solve(root, result)
        return result

    def solve(self, root, result):
        if root is None:
            return

        self.solve(root.left, result)
        result.append(root.val)
        self.solve(root.right, result)

    def iterTraversal(self, root):
        if root is None:
            return []
        stack = []
        stack.append(root)
        result = []
        while len(stack):
            node = stack[-1]
            if node.left:
                stack.append(node.left)
                node.left = None
                continue

            node = stack.pop()
            result.append(node.val)

            if node.right:
                stack.append(node.right)

        return result