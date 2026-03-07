# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k==1:
            return head
        count = 0 
        dummyNode = ListNode(0)
        bfr = dummyNode
        srt = head
        end = dummyNode
        bfr.next = srt
        
        while srt:
            for i in range(k):
                if not end.next:
                    return dummyNode.next
                end = end.next
            aft = end.next

            # reversing from srt to end
            prev = srt
            curr = srt.next
            end.next = None
            while curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            bfr.next = end
            srt.next = aft

            # Reassigning pointers
            bfr = srt
            srt = bfr.next
            end = bfr

        return dummyNode.next
        
