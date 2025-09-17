# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root :
            res = []
            return res

        else :
            que = deque([root])
            res = []
        
            while que:
                iniNode = que.popleft()
                res.append(iniNode.val)
                ctr = 0
                if iniNode.right:
                    que.append(iniNode.right)
                    ctr += 1
                if iniNode.left:
                    que.append(iniNode.left)
                    ctr += 1

                for i in range(len(que) - ctr):
                    node = que.popleft()
                    
                    if node.right:
                        que.append(node.right)

                    if node.left:
                        que.append(node.left)
                        
            
            return res