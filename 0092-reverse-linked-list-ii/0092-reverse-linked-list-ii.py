# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        if left == right :
            return head

        
        Left = head
        
        Dummy = ListNode(0)
        Dummy.next = head
        
        Before = Dummy
        Before.next = Left

        Right = head

        for i in range (left-1):
            Left = Left.next
            Before = Before.next
        
        for i in range (right-1):
            Right = Right.next
        After = Right.next 


        prev = Left
        curr = Left.next
        

        while prev != Right :
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        Before.next = prev
        Left.next = After

        return Dummy.next


        
        
        


        