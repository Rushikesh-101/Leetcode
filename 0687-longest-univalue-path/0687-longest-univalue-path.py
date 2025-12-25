# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        
        maxpath = 0

        def longestpath(node):
            if not root:
                return 0
            nonlocal maxpath
            left = 0
            right = 0
            count = 0

            if not node.right and not node.left:
                return 1
                
            if node.left:
                left = longestpath(node.left)  
            if node.right:
                right = longestpath(node.right)

            if node.right and node.left:
                if node.right.val == node.val and node.left.val == node.val:
                    if maxpath < count + left + right:
                        maxpath = count + left + right
                    count = max(left,right)
                elif node.right.val == node.val:
                    count += right
                elif node.left.val == node.val:
                    count += left

            else:
                if node.left and node.left.val == node.val:
                    count += left
                elif node.right and node.right.val == node.val:
                    count += right
            
            if maxpath < count:
                maxpath = count
            
            return count+1
        
        longestpath(root)
        return maxpath
            
            

            
