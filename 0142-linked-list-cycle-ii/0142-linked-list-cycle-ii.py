# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        slow = head
        fast = head
        static = head

        while fast and fast.next :

            slow = slow.next
            fast = fast.next.next

            if slow == fast :
                if slow == static:
                    return static
                else : 
                    slow = slow.next
                while slow != fast:
                    if slow == static :
                        return static
                    else :
                        slow = slow.next
                static = static.next
        return None
            
            

