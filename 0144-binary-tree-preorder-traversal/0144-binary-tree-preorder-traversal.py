# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        result = []

        # def traverse(node):
        #     if not node:
        #         return 

        #     result.append(node.val)
        #     traverse(node.left)
        #     traverse(node.right)
        
        # traverse(root)

        # return result


        def preorder(node,result):
            result.append(node.val)
            if node.left:
                preorder(node.left,result)
            if node.right :
                preorder(node.right,result)
        
        preorder(root,result)
        return result

