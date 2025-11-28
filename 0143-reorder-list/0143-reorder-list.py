# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        slow = head
        fast = head

        while fast and fast.next :
            slow = slow.next
            fast = fast.next.next
        # slow is in the middle, or more than middle
        # reverse till slow ( not slow )
        curr = slow.next
        prev = None
        slow.next = None
        
        while curr != None : 
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        L1 = head
        L2 = prev

        while L2 != None :

            temp1 = L1.next
            temp2 = L2.next

            L1.next = L2 
            L2.next = temp1

            L1 = temp1
            L2 = temp2

        return head
