"""
Description 21:
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4

Easy.......
Runtime: 40 ms, faster than 100.00% of Python3 online submissions for Merge Two Sorted Lists.
"""


# Definition for singly-linked list.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head, tail = None, None
        while l1 or l2:
            if l1 and l2:
                if l1.val <= l2.val:
                    if head is None:
                        head, tail = l1, l1
                    else:
                        tail.next = l1
                        tail = l1
                    l1 = l1.next
                else:
                    if head is None:
                        head, tail = l2, l2
                    else:
                        tail.next = l2
                        tail = l2
                    l2 = l2.next
            elif l1:
                if head is None:
                    head, tail = l1, l1
                else:
                    tail.next = l1
                    tail = l1
                l1 = l1.next
            elif l2:
                if head is None:
                    head, tail = l2, l2
                else:
                    tail.next = l2
                    tail = l2
                l2 = l2.next
        return head