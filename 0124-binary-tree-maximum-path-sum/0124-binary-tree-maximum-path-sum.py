# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_path_sum = float('-inf')
        def maxpath(node):
            
            if not node:
                return 0
            print("\n node val : ", node.val)
            nonlocal max_path_sum

            ret_val = node.val
            total = node.val

            right = maxpath(node.right)
            left = maxpath(node.left)
            print("\n vals : ", right, left)

            # check if this node as pivot gives the highest
            if right > 0:
                total += right
            if left > 0:
                total += left
            
            max_path_sum = max(max_path_sum,total)

            # calculate whats the maximum it can send up 
            higher = max(right,left)

            if higher > 0:
                ret_val += higher
            
            return ret_val
        
        maxpath(root)
        return max_path_sum
