# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        sum = 0

        def roottoleaf(node,path):
            nonlocal sum

            path += str(node.val)
            if not node.left and not node.right:
                sum += int(path)
            
            if node.right:
                roottoleaf(node.right,path)
            if node.left:
                roottoleaf(node.left,path)
            
        path = ''
        roottoleaf(root,path)
        return sum