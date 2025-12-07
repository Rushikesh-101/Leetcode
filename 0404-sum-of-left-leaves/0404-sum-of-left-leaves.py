# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        sum = 0

        def leftSum(node):

            nonlocal sum
            
            if not node.left and not node.right :
                return 
            if node.left:
                if not node.left.left and not node.left.right:
                    sum += node.left.val
                leftSum(node.left)
            if node.right:
                leftSum(node.right)
            
        leftSum(root)
        return sum