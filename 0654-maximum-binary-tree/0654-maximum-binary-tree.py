# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None

        def construct(start,end,nums):
            if start > end :
                return None
            if start == end :
                return TreeNode(nums[start])

                
            root = 0
            maxi = 0
            for i in range(start,end+1):
                if nums[i] > maxi :
                    maxi = nums[i]
                    root = i
            if maxi == 0 :
                print (start,end)
            print("\n first maxi was : ", maxi)
            rootNode = TreeNode(maxi)
            print("\n initiated root was :", root)
            rootNode.left = construct(start, root-1, nums)
            rootNode.right = construct(root+1, end, nums)
            return rootNode

        return construct(0,len(nums)-1,nums)
        
    