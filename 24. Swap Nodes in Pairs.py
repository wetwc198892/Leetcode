# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head:
            return head
        i = 1
        cur = head
        while cur.next:
            if i%2 !=0:
                cur.val,cur.next.val = cur.next.val,cur.val
            cur = cur.next
            i  += 1
        return head