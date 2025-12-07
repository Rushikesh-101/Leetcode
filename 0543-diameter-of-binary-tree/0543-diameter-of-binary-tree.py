# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        maxD = 0

        def func(node):
            nonlocal maxD
            left = 0
            right = 0
            if not node.left and not node.right:
                return 1
            
            if node.left:
                left = func(node.left)
            if node.right:
                right = func(node.right)

            
            diameter = left + right
            if maxD < diameter:
                maxD = diameter

            return 1 + max(left,right)
        
        func(root)
        return maxD