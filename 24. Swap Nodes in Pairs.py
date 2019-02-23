"""
Description 24
Given a linked list, swap every two adjacent nodes and return its head.

Example:

Given 1->2->3->4, you should return the list as 2->1->4->3.
Note:

Your algorithm should use only constant extra space.
You may not modify the values in the list's nodes, only nodes itself may be changed.

Runtime: 48 ms, faster than 30.72% of Python3 online submissions for Swap Nodes in Pairs.
Emm... Not so fast as I think, but I reckoned the solution is pretty clear.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur = head
        tail = None
        while cur and cur.next:
            if cur is head:
                head = cur.next

            third = cur.next.next
            nextHead = cur.next
            cur.next.next = cur
            cur.next = third

            if tail:
                tail.next = nextHead

            tail = cur
            cur = cur.next

        return head


if __name__ == '__main__':
    s = Solution()
    print(s.swapPairs())