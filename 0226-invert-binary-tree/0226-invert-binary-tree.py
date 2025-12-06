# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        '''
            Think about just exchanging every left right of a node

        '''

        def invert(node):
            if not node:
                return 
                
            if node.right and node.left:
                temp = node.right
                node.right= node.left
                node.left = temp

            elif node.right:
                node.left = node.right
                node.right = None

            elif node.left :
                node.right = node.left
                node.left = None

            invert(node.right)
            invert(node.left)
            
        
        invert(root)
        return root
