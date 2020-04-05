# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        list1,list2 = [],[]
        while l1 != None:
            list1.append(l1.val)
            l1 = l1.next
        while l2 != None:
            list2.append(l2.val)
            l2 = l2.next
        list3 = sorted(list1 + list2)
        cur = temp = ListNode(0)
        for i in list3:
            cur.next = ListNode(i)
            cur = cur.next
        return temp.next
        