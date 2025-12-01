# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        if not head.next:
            return head
        start = head
        end = head
        list_lenght = 1
        while end.next :
            end = end.next
            list_lenght += 1

        end.next = start
        if list_lenght >= k:
            for i in range(list_lenght - k):
                end = end.next
                start = start.next
        else : 
            remain = k % list_lenght
            for i in range(list_lenght - remain):
                end = end.next
                start = start.next

        end.next = None
        return start