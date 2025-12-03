# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        ogArray = []
        curr = head
        while curr :
            ogArray.append(curr.val)
            curr = curr.next


        result_array = []
        for i in range(len(ogArray)):
            result_array.append(0)


        monoStack = []
        for index,value in enumerate(ogArray):
            if not monoStack :
                monoStack.append(index)
            
            while monoStack and ogArray[monoStack[-1]] < value:
                indexUpdate = monoStack.pop()
                result_array[indexUpdate] = value
            monoStack.append(index)


        return result_array

