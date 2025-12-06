# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
                
        def sum(node,total):
            total += node.val
            print("\n Total this time : ",total)
            if total == targetSum and not node.right and not node.left:
                return True
            
            else:
                if node.right:
                    if sum(node.right,total) == True:
                        return True
                if node.left:
                    if sum(node.left,total) == True:
                        return True
           
        if sum(root,0) == True:
            return True
        else:
            return False

        
        # Above function should output True or nothing for any given tree.
        # If it outputs None, meaning equal sum not found, we will return False
            