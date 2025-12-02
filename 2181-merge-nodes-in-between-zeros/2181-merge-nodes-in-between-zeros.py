# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = head
        curr = head.next
        dummynode = ListNode(0)
        prevsum = dummynode
        while curr and curr.next:
            sum = 0
            while curr.val != 0:
                sum += curr.val
                prev.next = None
                prev = curr
                curr = curr.next
            prev.val = sum
            prevsum.next = prev
            prevsum = prevsum.next
            prev.next = None
            prev = curr
            curr = curr.next
        
        return dummynode.next



