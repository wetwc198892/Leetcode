# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        if not root:
            return 0
        stack = []
        stack.append(root)
        result = 0
        while stack:
            cur = stack.pop()
            if(self.isUnitree(cur)):
                result += 1
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)
        return result
    
    def isUnitree(self,root:TreeNode):
        if not root:
            return True
        if root.left and root.val != root.left.val:
            return False
        if root.right and root.val != root.right.val:
            return False
        if self.isUnitree(root.left) and self.isUnitree(root.right):
            return True

        