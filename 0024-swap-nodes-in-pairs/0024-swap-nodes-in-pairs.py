# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        if not head.next:
            return head

        dummynode = ListNode(0)
        dummynode.next = head.next
        prev = head
        curr = head.next
        before = dummynode

        while curr :

            temp = curr.next
            curr.next = prev
            prev.next = temp
            before.next = curr
            before = prev
            prev = prev.next

            if not prev:
                return dummynode.next
            else:
                curr = prev.next

        return dummynode.next
            




