# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = ListNode(0)
        dummy = result
        temp = 0
        while l1 or l2 or temp:
            cur = temp
            if l1:
                cur += l1.val
                l1 = l1.next
            if l2:
                cur += l2.val
                l2 = l2.next
            if cur >= 10:
                temp = 1
                cur -= 10
            else:
                temp = 0
            tempNode = ListNode(cur)
            dummy.next = tempNode
            dummy = dummy.next
        return result.next