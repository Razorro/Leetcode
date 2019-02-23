"""
Description 19:
Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        preNode = ListNode(-1)
        preNode.next = head
        self._removeNthFromEnd(preNode, n, [0])
        return preNode.next

    def _removeNthFromEnd(self, node, n, curLevel):
        if node and node.next:
            self._removeNthFromEnd(node.next, n, curLevel)

        curLevel[0] += 1
        if curLevel[0] - n == 1:
            node.next = node.next.next


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    s = Solution()
    s.removeNthFromEnd(head, 5)