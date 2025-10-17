# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head and not head.next :
            return head
        elif not head :
            return None
        else :
            prev = head
            curr = head.next

            while prev.next :

                if prev.val == curr.val :
                    curr = curr.next
                    prev.next = curr
                else:
                    prev = prev.next
                    curr = curr.next

            return head