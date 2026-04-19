# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
from typing import Deque


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        s=[]
        q=deque()
        q.append(root)
        while q:
            l=[]
            for i in range(len(q)):
                node=q.popleft()
                if node:
                    l.append(node.val) # imp to put val otherwise returns node and not its value
                    q.append(node.left)
                    q.append(node.right)
            if l:
                s.append(l)
        return s
                
            
            
        

        