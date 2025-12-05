# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        # 2 oppositely symmetric nodes will be passed as arguments, their right, left and left, right will
        # be further passed as arguments

        def checkSymmetry(leftnode,rightnode):
            if leftnode and rightnode:
                if leftnode.val != rightnode.val:
                    return False
            
                else:
                    leftleftnode = leftnode.left
                    rightrightnode = rightnode.right
                    leftrightnode = leftnode.right
                    rightleftnode = rightnode.left
                    return checkSymmetry(leftleftnode,rightrightnode) and checkSymmetry(leftrightnode,rightleftnode)

            elif not leftnode and not rightnode:
                return True

            else:
                return False

                
        return checkSymmetry(root.left,root.right)



