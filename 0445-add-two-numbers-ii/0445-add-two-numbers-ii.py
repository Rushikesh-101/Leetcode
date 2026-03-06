# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        def adding():

            nodeA = l1
            num1 = ''
            while nodeA:
                num1 += str(nodeA.val)
                nodeA = nodeA.next

            nodeB = l2
            num2 = ''
            while nodeB:
                num2 += str(nodeB.val)
                nodeB = nodeB.next
            
            summ = int(num1) + int(num2)
            dummyNode = ListNode(0)
            dummy = dummyNode
            for i in str(summ):
                dummy.next = ListNode(int(i))
                dummy = dummy.next
            
            return dummyNode.next
        
        return adding()

            


