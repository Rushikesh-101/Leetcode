# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        ''' 
        Solution :
        for every parent child, get possible value from left and right
        add both and its own value and check against global maximum
        if greater, update

        else, take max(leftchild, rightchild)
        return that plus itself to its parent above.

        '''
        maximum = float('-inf')
        def maxsum(node):
            nonlocal maximum
            right = 0
            left = 0

            if maximum < node.val:
                maximum = node.val

            if not node.right and not node.left:
                return node.val
            
            if node.right:
                right = maxsum(node.right)

            if node.left:
                left = maxsum(node.left)
            
            if right +left +node.val > maximum:
                maximum = right+left+node.val
            if right + node.val > maximum:
                maximum = right + node.val
            if left + node.val > maximum:
                maximum = left + node.val
            
            if node.val + max(right,left) > node.val:
                
                return max(right,left)+node.val
            else:
                return node.val
        
        maxsum(root)
        return maximum
            
            

