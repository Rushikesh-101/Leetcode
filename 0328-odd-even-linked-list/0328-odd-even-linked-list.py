# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # Splitting and rebuilding 
        if not head:
            return None
        elif not head.next :
            return head


        firstdummy = ListNode(0)
        seconddummy = ListNode(0)
        firstdummy.next = head
        seconddummy.next = head.next

        first = head
        second = head.next

        while first.next and second.next :

            first.next = second.next
            second.next = second.next.next

            first = first.next
            second = second.next
        
        first.next = seconddummy.next
        return firstdummy.next


           


        