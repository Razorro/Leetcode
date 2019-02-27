"""
Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:

Input: 1->1->2
Output: 1->2
Example 2:

Input: 1->1->2->3->3
Output: 1->2->3

执行用时: 60 ms, 在Remove Duplicates from Sorted List的Python3提交中击败了90.08% 的用户
内存消耗: 6.5 MB, 在Remove Duplicates from Sorted List的Python3提交中击败了73.46% 的用户

No other tricks, still the list basic node operation
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: 'ListNode') -> 'ListNode':
        fast = head
        while fast and fast.next:
            if fast.val == fast.next.val:
                temp = fast.next.next
                while temp and temp.val == fast.val:
                    temp = temp.next
                fast.next = temp
                fast = temp
            else:
                fast = fast.next

        return head