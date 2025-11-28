# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        Dummy = ListNode(0)
        Dummy.next = head

        before = Dummy
        left = head

        right = head

        for i in range(k-1):
            right = right.next
        after = right.next

        while right != None :
                prev = left
                curr = left.next

                while prev != right :
                    temp = curr.next
                    curr.next = prev
                    prev = curr
                    curr = temp
                
                left.next = after
                before.next = prev

                before = left
                left = after
                right = after
                for i in range(k-1):
                    if right :
                        right = right.next
                    else :
                        break
                if right :
                    after = right.next
                else : 
                    break
        
        return Dummy.next