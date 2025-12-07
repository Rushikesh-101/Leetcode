# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return True
        if not root.right and not root.left:
            return True
            
        def balance(node):
            right = 0
            left = 0
            if not node.right and not node.left:
                return 1
            else:
                if node.right:
                    right = balance(node.right)
                   
                    if right == False:
                        return False

                if node.left:
                    left = balance(node.left)  
                    
                    if left == False:
                        return False
            print("\n current left right :",left-right)
            if -2 >= left - right or  left - right >= 2:
                return False
            
            if node == root:
                diff = left - right
                if -2 >= diff or diff >= 2:
                    return False
                else:
                    return True

            else:
                print("\n returning max as:", max(left,right))
                return 1 + max(left,right)

        # result = balance(root)
        # print("this is printed result :", result)

        return balance(root)
        


        # if result == False:
        #     print("\nreturned through midpoint")
        #     return False

        
        # else:
        #     print("\n returned false from here ")
        #     return False