# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        '''
        Traverse from root till bottom
        Add a depth parameter in recur function

        '''

        def sum(node,depth):
            if not node.left and not node.right:
                return node.val,depth
            
            if node.right and node.left:
                rightval,rdepth = sum(node.right,depth+1)
                leftval,ldepth = sum(node.left, depth+1)

                if rdepth == ldepth:# same depth, return sum of both and depth
                    return rightval + leftval, rdepth
                elif rdepth > ldepth :
                    return rightval, rdepth
                else:
                    return leftval, ldepth
                

            elif node.right:
                rightval, rdepth = sum(node.right, depth+1)
                return rightval, rdepth

            elif node.left:
                leftval, ldepth = sum(node.left, depth+1)
                return leftval, ldepth
            
        value, depth = sum(root,1)
        return value
                
            

            
        
      