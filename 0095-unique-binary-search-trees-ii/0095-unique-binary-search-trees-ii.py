# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        # here we cant just provide how many values are allowed for each node, we also have to mentionwhich values are allowed
        
        if n == 0:
            return []

        def generate(start,end):
            if start > end:
                return [None]

            result = []
            
            for i in range (start,end+1):
                '''
                   for each value of root we have possible sub trees returned by
                   recursive left and right, they are stored in this left_trees and 
                   right_trees list.
                '''
                left_trees = generate(start, i-1)
                right_trees = generate(i+1,end)
                
                '''
                    And in turn this root will combine each possible root value each 
                    left sub tree with each right sub tree and store that in a list and 
                    return above, this is the same result aquired by this roots parent 
                    from its left or right child. 
                '''
                for left in left_trees:
                    for right in right_trees:
                        root = TreeNode(i)
                        root.left = left
                        root.right = right
                        result.append(root)

            return result
         
        return generate(1,n)