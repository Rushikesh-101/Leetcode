# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        dummynode = ListNode(0)
        dummy = dummynode
        dummynode.next = head
        curr = head

        while curr:
            if curr.val == val:
                dummy.next = curr.next
                curr = curr.next
            else:
                dummy = dummy.next
                curr = curr.next

        return dummynode.next