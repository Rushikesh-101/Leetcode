# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        #enter every list into a stack.
        #empty the stack into resultlist and return it

        if not root:
            arr = []
            return arr
        
        else:

            queue = deque([root])   # root not iterable so [root]
            result = []
            while queue:
                print("entered")
                
                
                arr = []
                for i in range(len(queue)):
                    node = queue.popleft()
                    print("entered")

                    arr.append(node.val)

                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                    
                result.append(arr)
            fResult = []
            while result:
                fResult.append(result.pop())

            return fResult