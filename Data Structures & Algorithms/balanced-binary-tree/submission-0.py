class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def checkBalance(node):
            if not node:
                return 0  # Base case: height is 0
            
            leftHeight = checkBalance(node.left)
            rightHeight = checkBalance(node.right)

            # If left or right subtree is unbalanced, return -1
            if leftHeight == -1 or rightHeight == -1:
                return -1
            
            # If current node is unbalanced, return -1
            if abs(leftHeight - rightHeight) > 1:
                return -1 

            # Otherwise, return height of the current node
            return 1 + max(leftHeight, rightHeight)

        return checkBalance(root) != -1  # If -1 is returned, the tree is unbalanced
