# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Pattern 2 : preorder decision 
        # Validate at parent before moving to childrens
        # Here nodes pass ancestral constraints and check them before moving forward

        def binary(node,low,high):
            left_val = False
            right_val = False
        
            if node.val <= low or node.val >= high:
                return False

            if not node.right and not node.left:
                return True
            
            if node.left:
                if node.val > node.left.val :
                    left_val = binary(node.left, low, node.val)
                else: 
                    return False

            if node.right:
                if node.val < node.right.val :
                    right_val = binary(node.right, node.val, high)
                else:
                    return False

            if node.val == 6 :
                print("\n left rcvd : ", left_val)
                print("\n right rcvd : ", right_val )
            if not node.right or not node.left:
                if not left_val and not right_val:
                    return False
                else :
                    return True
            
            else :
                if left_val and right_val:
                    return True
                else:
                    return False

                     
        
        return binary(root,float('-inf'),float('inf'))
            
            