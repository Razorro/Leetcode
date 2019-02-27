"""
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

Example 1:

Input: 1->2->3->3->4->4->5
Output: 1->2->5
Example 2:

Input: 1->1->1->2->3
Output: 2->3

执行用时: 56 ms, 在Remove Duplicates from Sorted List II的Python3提交中击败了100.00% 的用户
内存消耗: 6.5 MB, 在Remove Duplicates from Sorted List II的Python3提交中击败了85.51% 的用户

Without any tricks, just need to notice hwo to operate the rotate node.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: 'ListNode') -> 'ListNode':
        slow = ListNode(-1); slow.next = head
        fast = head
        while fast and fast.next:
            if fast.val == fast.next.val:
                val = fast.val
                fast = fast.next.next
                while fast and val == fast.val:
                    fast = fast.next
                if head.val == val:
                    head = fast
                slow.next = fast
            else:
                slow, fast = slow.next, fast.next

        return head