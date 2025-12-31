# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        arr = 1,2,3,4,5,6,7

        def nextNode(node,left,right):
            if left > right:
                return 
            if left == right: 
                node.val = nums[left]
                return 
            
            mid = (left + right) // 2
            print("\n this was left and right :", left, right)
            print("\n this is mid :", mid)
            node.val = nums[mid]

            if left != mid :
                node.left = TreeNode(0)
                newRight = mid-1
                nextNode(node.left,left,newRight)
            
            if right != mid :
                node.right = TreeNode(0)
                newLeft = mid+1
                nextNode(node.right,newLeft,right)

        root = TreeNode(0)
        nextNode(root,0,len(nums)-1)

        return root

