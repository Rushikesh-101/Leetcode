# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        # Pointer redirection : 
        # Redirecting both pointers from end of list to start of other list. 
        # Thus equal distance travelled by both list and at the end they 
        # either meet at intersection or at end of list


        currA = headA
        currB = headB

        
        while currA != currB :
            # pointing to other lists head

            if currA != None:
                currA = currA.next
            else :
                currA = headB
              
            if currB != None :
                currB = currB.next
            else :
                currB = headA
    
        return currA