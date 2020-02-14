# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def flatten(self, root: TreeNode) -> None:
        if root == None:
            return
        list_tree = []

        def recursive(node):
            nonlocal list_tree
            if not node:
                return
            list_tree.append(node)
            recursive(node.left)
            recursive(node.right)
            return
        recursive(root)
        currentNode = list_tree.pop(0)
        while list_tree:
            currentNode.left = None
            currentNode.right = list_tree.pop(0)
            currentNode = currentNode.right

        """
        Do not return anything, modify root in-place instead.
        """
