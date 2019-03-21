"""
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]

Runtime: 44 ms, faster than 64.80% of Python3 online submissions for Binary Tree Level Order Traversal II.
Memory Usage: 13.4 MB, less than 14.13% of Python3 online submissions for Binary Tree Level Order Traversal II.

BFS..
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrderBottom(self, root: TreeNode) -> 'List[List[int]]':
        if root is None:
            return []
        coll = []
        q = [root]

        while q:
            n = len(q)
            data = []
            for _ in range(n):
                node = q.pop(0)
                data.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            coll.append(data)

        coll.reverse()
        return coll