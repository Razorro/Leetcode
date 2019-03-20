"""
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]


Runtime: 40 ms, faster than 66.53% of Python3 online submissions for Binary Tree Zigzag Level Order Traversal.
Memory Usage: 13.2 MB, less than 5.36% of Python3 online submissions for Binary Tree Zigzag Level Order Traversal.


Just the usage of BFS, no other trick
"""


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []

        coll = []
        l = [root]
        levelNodes = []
        direction = 0
        while l:
            n = len(l)
            if direction == 0:
                itor = range(n)
            else:
                itor = range(-1, -n - 1, -1)

            for idx in itor:
                levelNodes.append(l[idx].val)

            for i in range(n):
                if l[i].left:
                    l.append(l[i].left)
                if l[i].right:
                    l.append(l[i].right)

            l = l[n:]
            coll.append(list(levelNodes))
            direction ^= 1
            levelNodes.clear()

        return coll