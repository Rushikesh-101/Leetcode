# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        arr = 1,2,3,4,5,6,7

        def nextNode(left,right):
            if left > right:
                return None
            
            mid = (left + right) // 2

            root = TreeNode(nums[mid])
            root.left = nextNode(left, mid-1)
            root.right = nextNode(mid+1, right)
            return root
            
        return nextNode(0,len(nums)-1)



