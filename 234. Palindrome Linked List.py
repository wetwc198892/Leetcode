# Given a singly linked list, determine if it is a palindrome.

# Example 1:

# Input: 1->2
# Output: false
# Example 2:

# Input: 1->2->2->1
# Output: true
# Follow up:
# Could you do it in O(n) time and O(1) space?

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if(head == None or head.next == None):
            return True
        list1 = []
        while(head.next != None):
            list1.append(head.val)
            head = head.next
        list1.append(head.val)
        if(list1 == list1[::-1]):
            return True
        else:
            return False
