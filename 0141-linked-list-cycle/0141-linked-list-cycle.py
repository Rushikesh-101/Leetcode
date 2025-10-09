# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        if head :
            pt1 = head
            pt2 = head
            
            while pt2 and pt2.next :    
                pt1 = pt1.next
                pt2 = pt2.next.next

                if pt1 == pt2:
                    return True
            return False
        else : 
            return False

    
        # Note : only pt2 in while loop cause slow ptr will never be ahead of fast one if cycle terminates