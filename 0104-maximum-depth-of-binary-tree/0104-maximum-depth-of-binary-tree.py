# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        '''
        Queue based solution : 


        if root :
         
            que = deque([root]) # [root] brackets cause root isnt iterative
            depth = 0
            while que:

                for i in range(len(que)):
                    node = que.popleft()
                    if node.left:
                        que.append(node.left)
                    if node.right:
                        que.append(node.right)
                depth += 1
            
            return depth
        else :
            return 0
        '''

        
    # Recursive solution :

        def depth(node):
            # If node, called function, upon doesnt exist,returns 0 height value
            if not node:
                return 0

            # Calls th function on right and left child if they exist 
            right = depth(node.right)
            left = depth(node.left)
            
            # When returning value from node A , we return maximum of it right child and left child height,
            # +1 of itself
            return 1 + max(left,right) 
        
        return depth(root)
            

    