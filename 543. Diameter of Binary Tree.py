# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def depth(root):
            nonlocal maxDiameter
            if not root:
                return 0
            left = depth(root.left)
            right = depth(root.right)
            currentDiameter = left+right
            maxDiameter = max(maxDiameter,currentDiameter)
            return max(left,right)+1
        maxDiameter = 0
        depth(root)
        return maxDiameter