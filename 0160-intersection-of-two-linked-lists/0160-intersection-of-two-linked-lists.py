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

        
        # while currA != currB :
        #     # pointing to other lists head

        #     if currA != None:
        #         currA = currA.next
        #     else :
        #         currA = headB
              
        #     if currB != None :
        #         currB = currB.next
        #     else :
        #         currB = headA
    
        # return currA

        ctr1 = 0
        while currA != None:
            ctr1 += 1
            currA = currA.next

        ctr2 = 0
        while currB != None:
            ctr2 += 1
            currB = currB.next
        
        currA = headA
        currB = headB

        if ctr1 > ctr2:
            diff = ctr1 - ctr2 
            while diff != 0:
                currA = currA.next
                diff -= 1

        else :
            diff = ctr2-ctr1
            while diff != 0:
                currB = currB.next
                diff -= 1
        
        while currA or currB:
            if currA == currB:
                return currA
            currA = currA.next
            currB = currB.next
        return None