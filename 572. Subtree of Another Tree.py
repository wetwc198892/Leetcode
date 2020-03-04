# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not s:
            return False
        if not t:
            return True
        if self.isSame(s,t):
            return True
        return self.isSubtree(s.left,t) or self.isSubtree(s.right,t)
            
    def isSame(self,s:TreeNode,t:TreeNode):
        if not s and not t:
            return True
        elif(not s or not t):
            return False
        elif s.val != t.val:
            return False
        else:
            return self.isSame(s.left,t.left) and self.isSame(s.right,t.right)