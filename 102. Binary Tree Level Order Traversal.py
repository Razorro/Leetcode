"""
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]


执行用时 : 60 ms, 在Binary Tree Level Order Traversal的Python3提交中击败了40.96% 的用户
内存消耗 : 13.5 MB, 在Binary Tree Level Order Traversal的Python3提交中击败了0.96% 的用户

just BFS.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: 'TreeNode') -> 'List[List[int]]':
        if root is None:
            return []

        coll = []
        l = [root]
        while l:
            n = len(l)
            levelNodes = []
            for _ in range(n):
                node = l.pop(0)
                levelNodes.append(node.val)

                if node.left:
                    l.append(node.left)
                if node.right:
                    l.append(node.right)

            coll.append(list(levelNodes))
            levelNodes.clear()

        return coll
