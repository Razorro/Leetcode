"""
Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7


Runtime: 216 ms, faster than 43.91% of Python3 online submissions for Construct Binary Tree from Inorder and Postorder Traversal.
Memory Usage: 87.8 MB, less than 5.26% of Python3 online submissions for Construct Binary Tree from Inorder and Postorder Traversal.


Same with the previous question.
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, inorder: 'List[int]', postorder: 'List[int]') -> TreeNode:
        if len(inorder) == 0:
            return None

        rootIdx = inorder.index(postorder[-1])
        root = TreeNode(postorder[-1])
        root.left = self.buildTree(inorder[:rootIdx], postorder[:rootIdx])
        root.right = self.buildTree(inorder[rootIdx + 1:], postorder[rootIdx:-1])
        return root