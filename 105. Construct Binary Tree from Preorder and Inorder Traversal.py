"""
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7


Runtime: 276 ms, faster than 18.73% of Python3 online submissions for Construct Binary Tree from Preorder and Inorder Traversal.
Memory Usage: 87.8 MB, less than 5.27% of Python3 online submissions for Construct Binary Tree from Preorder and Inorder Traversal.

Not very efficient, but I think this answer make the devide and conquer clear.
The association about preorder and inorder costs quite a lot time to make clear...
With that in mind, the devide and conquer policy out of mind.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder: 'List[int]', inorder: 'List[int]') -> TreeNode:
        if len(preorder) == 0:
            return None
        root = TreeNode(preorder[0])
        middle = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:middle + 1], inorder[:middle])
        root.right = self.buildTree(preorder[middle + 1:], inorder[middle + 1:])
        return root