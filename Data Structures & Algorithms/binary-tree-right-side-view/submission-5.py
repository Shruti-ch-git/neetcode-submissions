# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        result=[]
        d=deque([root])
        while d:
            n=len(d)
            for i in range(n):
                r= d.popleft()
                if i==n-1:
                    result.append(r.val)
                if r.left:
                    d.append(r.left)
                if r.right:
                    d.append(r.right)
        return result
            


            

                        
            
            


        
        
        