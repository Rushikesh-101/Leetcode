# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        l1 = headA
        l2 = headB

        count1 = 0
        while l1:
            count1 += 1
            l1 = l1.next

        count2 = 0
        while l2:
            count2 += 1
            l2 = l2.next
        
        
        if count1 > count2:
            grtr = headA
            diff = count1 - count2
            for i in range(diff):
                grtr = grtr.next
            l2 = headB
            while grtr:
                if grtr == l2:
                    return grtr
                grtr = grtr.next
                l2 = l2.next
                
            return None
            
        else:
            grtr = headB
            diff = count2 - count1
            for i in range(diff):
                grtr = grtr.next
            l1 = headA
            while grtr:
                if grtr == l1:
                    return grtr
                grtr = grtr.next
                l1 = l1.next
            return None
            