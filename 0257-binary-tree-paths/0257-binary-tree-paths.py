# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        result = []
        def binary(s,node):
            s += str(node.val)
            if not node.right and not node.left:
                result.append(s[:])
            
            else:
                
                if node.right:
                    string = s + '->'
                    binary(string,node.right)
                if node.left:
                    string = s +'->'
                    binary(string,node.left)

        s = ''
        if not root:
            return s
        binary(s,root)
        return result
