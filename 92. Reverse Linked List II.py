"""
Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.

Example:

Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL


Runtime: 40 ms, faster than 35.40% of Python3 online submissions for Reverse Linked List II.
Memory Usage: 13 MB, less than 5.22% of Python3 online submissions for Reverse Linked List II.


Still not good at efficiency, but the idea must be the same.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        prehead = ListNode(0)
        prehead.next = head
        current = prehead
        curIdx = 1
        while current.next and curIdx < m:
            current = current.next
            curIdx += 1
        leftNode = current

        stack = []
        while current.next and curIdx <= n:
            stack.append(current.next)
            current = current.next
            curIdx += 1

        rightNode = current.next
        tailIdx = len(stack) - 1
        while tailIdx > 0:
            stack[tailIdx].next = stack[tailIdx - 1]
            tailIdx -= 1

        leftNode.next = stack[-1]
        stack[0].next = rightNode

        return prehead.next

    def otherAnswer(self, head, m, n):
        """ From forum's answer
        This method try to modify node one by one, and that can imporve the efficiency
        just by one travel. But from the benchmark, the answer get a lower score...
        https://leetcode.com/problems/reverse-linked-list-ii/discuss/30709/Talk-is-cheap-show-me-the-code-(and-DRAWING)
        """
        if not head or m == n: return head
        p = dummy = ListNode(None)
        dummy.next = head
        for i in range(m - 1): p = p.next
        tail = p.next

        for i in range(n - m):
            tmp = p.next  # a)
            p.next = tail.next  # b)
            tail.next = tail.next.next  # c)
            p.next.next = tmp  # d)
        return dummy.next
