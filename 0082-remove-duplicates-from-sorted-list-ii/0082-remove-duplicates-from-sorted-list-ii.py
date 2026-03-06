# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def deletion():
            if not head:
                return None
            if not head.next:
                return head
                
            dummyNode = ListNode(0)
            dummyNode.next = head

            curr = dummyNode

            while curr.next:
                nextt = curr.next
                temp = nextt.next
                if not nextt.next:
                    return dummyNode.next
                if nextt.val != temp.val:
                    curr = curr.next
                else:

                    while temp and temp.val == nextt.val:
                        temp = temp.next
                        
                    curr.next = temp
            
            return dummyNode.next
        
        return deletion()

