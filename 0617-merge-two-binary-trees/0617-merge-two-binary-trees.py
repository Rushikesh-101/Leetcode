# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1:
            return root2
        elif not root2:
            return root1


        def merge(p1,p2):
            if not p1 and p2:
                return 
            p1.val += p2.val

            if not p1.right and p2.right:
                p1.right = TreeNode(0)
            if not p1.left and p2.left:
                p1.left = TreeNode(0)
           
            if p1.left and p2.left:
                merge(p1.left,p2.left)
            if p1.right and p2.right:
                merge(p1.right,p2.right)

        
        merge(root1,root2)
        return root1
            
            
