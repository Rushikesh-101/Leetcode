# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        def chor(node):
            if not node :
                return 0,0

            do_rob_left, dont_rob_left = chor(node.left)
            do_rob_right, dont_rob_right = chor(node.right)

            do_rob_node = dont_rob_right + dont_rob_left + node.val
            dont_rob_node = max((do_rob_right + do_rob_left),(dont_rob_right+dont_rob_left),(do_rob_right + dont_rob_left),(do_rob_left+dont_rob_right))

            return do_rob_node,dont_rob_node
        
        val1,val2 = chor(root)
        return max(val1,val2)
        
            




