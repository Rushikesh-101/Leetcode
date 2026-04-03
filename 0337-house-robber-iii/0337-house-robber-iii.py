# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        # based on take not take values

        def robber(node):
            if not node:
                return (0,0)
            
            else:
                own_val = node.val 
                take, nottake = node.val,0

                right_take, right_not = robber(node.right)

                left_take, left_not = robber(node.left)

                take += (right_not + left_not)
                nottake = max(right_take,right_not) + max(left_take, left_not)
                return (take,nottake)
        
        take,nottake = robber(root)
        return max(take,nottake)