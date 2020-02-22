# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head:
            return head
        temp = ListNode(0)
        temp.next = head
        cur = temp
        while cur.next and cur.next.next:
            a = cur.next
            b = cur.next.next
            a.next = b.next
            cur.next = b
            cur.next.next = a
            cur = cur.next.next
        return temp.next