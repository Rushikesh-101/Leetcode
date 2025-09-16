# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
       

            if not root:
                arr = []
                return arr 

            else :

                que = deque([root])
                arr = []
                
                while que:
                    result = []
                    for i in range(len(que)):
                        node = que.popleft()

                        result.append(node.val)
                        if node.left:
                            que.append(node.left)
                        if node.right:
                            que.append(node.right)
                    arr.append(result)
                return arr

        
