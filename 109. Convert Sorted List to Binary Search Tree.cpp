/*
Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted linked list: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5
*/


/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 * 
 * repeat with the previous question
 */
class Solution {
public:
    TreeNode* sortedListToBST(ListNode* head) {
        vector<ListNode*> coll;
        auto p = head
        while(p)
        {
          coll.push_back(p);
          p = p->next;
        }

        return _sortedListToBST(coll, 0, coll.size()-1);
    }

    TreeNode* _sortedListToBST(vector<ListNode*>& nodes, int start, int end)
    {
      if(start > end)
        return nullptr;

      int mid = (start + end) / 2;
      TreeNode* node = new TreeNode(nodes[mid]->val);
      node->left = _sortedListToBST(nodes, start, mid-1);
      node->right = _sortedListToBST(nodes, mid+1, end);
      return node;
    }
};