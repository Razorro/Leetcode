"""
Given a linked list, rotate the list to the right by k places, where k is non-negative.

Example 1:

Input: 1->2->3->4->5->NULL, k = 2
Output: 4->5->1->2->3->NULL
Explanation:
rotate 1 steps to the right: 5->1->2->3->4->NULL
rotate 2 steps to the right: 4->5->1->2->3->NULL
Example 2:

Input: 0->1->2->NULL, k = 4
Output: 2->0->1->NULL
Explanation:
rotate 1 steps to the right: 2->0->1->NULL
rotate 2 steps to the right: 1->2->0->NULL
rotate 3 steps to the right: 0->1->2->NULL
rotate 4 steps to the right: 2->0->1->NULL

Runtime: 68 ms, faster than 25.67% of Python3 online submissions for Rotate List.
Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Rotate List.

Not too fast, the key is, how to keep the infomation of new head, tail and spin the new head and the old head.
Just can be more concise, not need to use recursion to get the backtracking info, use fast-slow iteration can be
more easily and clear to get the answer.
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def rotateRight(self, head: 'ListNode', k: 'int') -> 'ListNode':
        if head is None or head.next is None:
            return head

        prehead = ListNode(0)
        prehead.next = head
        self.solve(head, prehead.next, k, [0, None, prehead])
        return prehead.next

    def solve(self, head, current, k, info):
        if current is None:
            info[0] = info[0] if k % info[0] == 0 else k % info[0]
            return

        if current.next is None:
            info[1] = current

        info[0] += 1
        self.solve(head, current.next, k, info)
        if info[0] == 0:
            info[1].next = head
            info[2].next = current.next
            current.next = None

        info[0] -= 1


if __name__ == '__main__':
    s = Solution()
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    print(s.rotateRight(head, 2))