"""
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Example:

Input: head = 1->4->3->2->5->2, x = 3
Output: 1->2->2->4->3->5


执行用时: 60 ms, 在Partition List的Python3提交中击败了39.15% 的用户
内存消耗: 13.3 MB, 在Partition List的Python3提交中击败了0.00% 的用户


From space and efficiency speaking, both are not good...
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        preNode = ListNode(-1)
        preNode.next = head
        current, insertNode = preNode, preNode
        travelIdx, insertIdx = 0, 0
        while current and current.next:
            if current.next.val < x:
                if travelIdx > insertIdx:
                    temp = current.next
                    current.next = current.next.next
                    temp.next = insertNode.next
                    insertNode.next = temp
                    insertNode = insertNode.next
                    continue
                else:
                    insertIdx += 1
                    insertNode = insertNode.next

            current = current.next
            travelIdx += 1

        return preNode.next

    def otherAns(self, head, x):
        """ other answer
        This answer use left node and right node to classify those nodes,
        and then connect the left nodes' leftmost to the right nodes' rightmost node
        """
        l, r = ListNode(0), ListNode(0)
        L, R = l, r
        while head:
            if head.val < x:
                l.next = head
                l = l.next
            else:
                r.next = head
                r = r.next
            head = head.next
        r.next = None
        l.next = R.next
        return L.next