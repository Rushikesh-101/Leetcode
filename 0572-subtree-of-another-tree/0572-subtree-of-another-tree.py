# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
       

            # using 2 functions :
                # 1st to find potential matching roots
                # 2nd to confirm sub tree similarity



            def check(node,subnode):
                if not node and not subnode:
                    return True
                if not node or not subnode:
                    return False
                if node.val != subnode.val:
                    return False
                
                leftval = check(node.left,subnode.left)
                
                rightval = check(node.right,subnode.right)

                if leftval and rightval:
                    return True


                
                




            
            def subtree(node,subRoot):
                
                if node.val == subRoot.val:
                    print("was called")
                    # call crosschecking function
                    if check(node,subRoot) == True:
                        print("went to another function")
                        return True

                if not node.left and not node.right:
                    print("returned from here")
                    return 
                else:
                    print("entered")                    
                    if node.left and subtree(node.left,subRoot) :
                        return True                   
                    if node.right and subtree(node.right,subRoot) :
                        return True
                        
            
            if subtree(root,subRoot) != True:
                return False
            else:
                return True
                
           