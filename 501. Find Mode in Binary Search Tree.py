# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        list_result = []
        queue = [root]
        while queue:
            cur = queue.pop(0)
            list_result.append(cur.val)
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
        dic = collections.Counter(list_result)
        maxvalue = {0:0}
        for key,value in dic.items():
            temp = list(maxvalue.values())[0]
            if value>temp:
                maxvalue = {key:value}
            elif value== temp:
                maxvalue.setdefault(key,value)
        return maxvalue