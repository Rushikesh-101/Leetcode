# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def checkIdentical(p,q):
            if not p and not q : 
                return True
            if not p or not q:
                return False
            if p.val != q.val : 
                return False
            
            right = checkIdentical(p.right,q.right)
            left = checkIdentical(p.left,q.left)

            if right and left:
                return True
            else:
                return False
            
        return checkIdentical(p,q)