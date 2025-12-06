# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        prev_path = ""
        result = []
        def path(node,prev_path):
            if not node.left and not node.right:
                prev_path += str(node.val)
                result.append(prev_path)
            else:
                prev_path += str(node.val) + "->"
            
            if node.right:
                path(node.right,prev_path)
            if node.left:
                path(node.left,prev_path)
        
        path(root,prev_path)
        return result