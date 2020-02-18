# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if m == n:
            return head
        i = 1
        cur = head
        tempList = []
        while i <= n:
            if i >= m and i <= n:
                tempList.append(cur)
            cur = cur.next
            i += 1
        n = len(tempList)
        for i in range(n//2):
            tempList[i].val, tempList[n-1 -
                                      i].val = tempList[n-1-i].val, tempList[i].val
        return head
