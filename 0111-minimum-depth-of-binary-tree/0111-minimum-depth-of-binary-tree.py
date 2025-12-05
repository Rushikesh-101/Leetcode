# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        # # if right or left ++
        # # else return depth
        # if root :
        #     que = deque([root])
        #     depth = 1
        #     while que :

        #         for i in range(len(que)):
        #             node = que.popleft()

        #             if node.left or node.right:
        #                 if node.right:
        #                     que.append(node.right)
        #                 if node.left:
        #                     que.append(node.left)
                
        #             else:
        #                 return depth
        #         depth += 1
        # else:
        #     return 0


        # Recursive solution 

        def minDepth(node):

            if not node:
                return 0
            
            left = minDepth(node.left)
            right = minDepth(node.right)

            if left == 0 or right == 0:
                return 1 + max(left,right)
            
            return 1 + min(left,right)
        
        return minDepth(root)