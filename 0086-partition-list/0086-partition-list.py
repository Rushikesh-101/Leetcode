# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        # split original list into lists in single traversal, 
        # join those two lists

        curr = head
        firstdummy = ListNode(0)
        seconddummy = ListNode(0)
        first = firstdummy
        second = seconddummy

        while curr :
            if curr.val >= x:
                newsecond = ListNode(curr.val)
                second.next = newsecond
                second = second.next
            else:
                newfirst = ListNode(curr.val)
                first.next = newfirst
                first = first.next

            curr = curr.next

        first.next = seconddummy.next
        return firstdummy.next
            



