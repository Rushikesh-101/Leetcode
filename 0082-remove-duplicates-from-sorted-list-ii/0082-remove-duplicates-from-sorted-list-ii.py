# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        curr = head  
        freq = {}
        while curr :
            value = curr.val
            if value in freq:
                freq[value] += 1
            else :
                freq[value] = 1
            curr = curr.next
        print("printing freq : ", freq)
        
        curr = head
        dummynode = ListNode(0)
        dummynode.next = head
        prev = dummynode

        while curr:
            if curr.val in freq and freq[curr.val] > 1:
                prev.next = curr.next
                curr = curr.next
            else:
                prev = curr
                curr = curr.next
        return dummynode.next