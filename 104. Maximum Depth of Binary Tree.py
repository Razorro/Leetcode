"""
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.


No other trick, use the devide and conquer
"""


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        return self.trigger(root)

    def trigger(self, root):
        if root is None:
            return 0

        return max(self.trigger(root.left), self.trigger(root.right)) + 1