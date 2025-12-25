# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0

        def good(node,greatest):
            nonlocal count
            
            if node.val >= greatest:
                count += 1
                greatest = node.val

            if node.right :
                # if node.right.val >= node.val and node.right.val >= root.val :
                #     count += 1
                good(node.right,greatest)

            if node.left:
                # if node.left.val >= node.val and node.left.val >= root.val:
                #     count += 1
                good(node.left,greatest)


        # if root.right :
        #     good(root.right)
        # if root.left :
        #     good(root.left)
        good(root,root.val)
        return count
            

