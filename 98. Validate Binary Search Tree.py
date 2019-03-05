"""
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
Example 1:

Input:
    2
   / \
  1   3
Output: true
Example 2:

    5
   / \
  1   4
     / \
    3   6
Output: false
Explanation: The input is: [5,1,4,null,null,3,6]. The root node's value
             is 5 but its right child's value is 4.


Runtime: 56 ms, faster than 58.25% of Python3 online submissions for Validate Binary Search Tree.
Memory Usage: 16.3 MB, less than 5.14% of Python3 online submissions for Validate Binary Search Tree.


Inorder recursion, check with last value
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        lastVal = [-9999999999]
        return self.solve(root, lastVal)

    def solve(self, root, lastVal):
        if root is None:
            return True

        if self.solve(root.left, lastVal) is False:
            return False

        if root.val <= lastVal[0]:
            return False

        lastVal[0] = root.val
        if self.solve(root.right, lastVal) is False:
            return False

        return True
