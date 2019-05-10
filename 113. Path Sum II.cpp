/*
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1
Return:

[
   [5,4,11,2],
   [5,8,4,5]
]

*/

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    vector<vector<int>> pathSum(TreeNode* root, int sum) {
        vector<vector<int>> coll;
        vector<int> curPath;
        _pathSum(root, sum, coll, curPath);
        return coll;
    }
    
    void _pathSum(TreeNode* node, int sum, vector<vector<int>>& coll, vector<int>& curPath)
    {
        if(node == nullptr)
            return;
        
        if(sum < node->val)
            return;
        
        curPath.push_back(node->val);
        if(sum == node->val)
        {
            
            coll.push_back(curPath);
            curPath.pop_back();
            return;
        }
        
        _pathSum(node->left, sum-node->val, coll, curPath);
        _pathSum(node->right, sum-node->val, coll, curPath);

        curPath.pop_back();
    }
};