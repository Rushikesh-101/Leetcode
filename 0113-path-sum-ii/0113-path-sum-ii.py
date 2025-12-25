# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        # pass a temp array as parameter
        resultArray = []
        def path(node,tempArray,sum):
            nonlocal resultArray
            tempArray.append(node.val)
            sum += node.val

            if not node.right and not node.left and sum == targetSum:
                resultArray.append(tempArray[:])

            if node.right:
                path(node.right,tempArray,sum)

            if node.left:
                path(node.left,tempArray,sum)

            tempArray.pop()


        tempArray = []
        sum = 0
        path(root,tempArray,sum)
        return resultArray

