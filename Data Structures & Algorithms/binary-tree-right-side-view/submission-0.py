import collections
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        res = []
        q = collections.deque([root])  # Start with the root node in the queue
        
        while q:
            qLen = len(q)  # Number of nodes at the current level
            for i in range(qLen):
                node = q.popleft()  # Pop the leftmost node
                if i == qLen - 1:  # If it's the last node in the level
                    res.append(node.val)  # Add it to the result list
                # Add the children of the current node to the queue
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        
        return res
