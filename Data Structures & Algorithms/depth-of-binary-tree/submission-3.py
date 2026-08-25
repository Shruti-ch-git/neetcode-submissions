# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        s=[(root,1)] # brackets imp
        l=0
        while s:
            n, d = s.pop()
            l=max(l,d)
            if n.left:
                s.append((n.left, d+1)) #add maxDepth
            if n.right:
                s.append((n.right, d+1)) #add 2 values, add 2 brackets
        return l
            

        
        
        