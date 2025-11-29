# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        # add from left to right, count carry's and add to next one 
        resultNode = ListNode(0)
        result = resultNode
        carry = 0
        currA =l1
        currB = l2

        while currA or currB :

            result.next = ListNode(0)
            result = result.next

            if currA and not currB:
                addition = currA.val + carry
                if addition >= 10 : 
                    result.val = addition - 10
                    carry = 1
                else :
                    result.val = addition
                    carry = 0

                currA = currA.next
                
                

            elif currB and not currA:
                addition = currB.val + carry
                if addition >= 10 : 
                    result.val = addition - 10
                    carry = 1
                else :
                    result.val = addition
                    carry = 0

                currB = currB.next
                

            else:
                addition = currA.val + currB.val + carry

                if addition >= 10 :
                    result.val = addition - 10 
                    carry = 1
                    
                else : 
                    result.val = addition 
                    carry = 0

                currA = currA.next
                currB = currB.next


        if carry == 1:
            result.next = ListNode(1)
            result = result.next

        return resultNode.next
                    


