# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        result = 0

        def check(node,p,q):

            nonlocal result 
            if not node :
                return False
            

            left = check(node.left,p,q)
            right = check(node.right,p,q)

            if left and right :
                print("entered first for : ", node.val) 
                result = node
                return True

            elif left or right :
                print("entered second for : ", node.val) 
                if node == p  or node  == q :
                    result = node
                return True

            else :
                print("entered third for : ", node.val) 

                if node == p or node == q:
                    print("entered for true : ", node.val) 
                    
                    return True
                else:
                    return False

            
            


        check(root,p,q)
        return result 
                