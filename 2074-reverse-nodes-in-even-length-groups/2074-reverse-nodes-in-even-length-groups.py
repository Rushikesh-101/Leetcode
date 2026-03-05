# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        dummyNode = ListNode(0)
        dummyNode.next = head

        bef = head
        prev = head.next

        if not prev or not prev.next:
            return head
        else:
            
        
            # we reverse prev to curr
            # match ends
            # move pointers
            grp = 2
            while bef.next:
                
                count = 0
                curr = bef
                while count < grp and curr.next != None:
                    curr = curr.next
                    count += 1
                if count%2 == 0:
                    aft = curr.next
                    prev = bef.next
                    
                    curr.next = None
                    Anode = prev
                    Bnode = prev.next

                    # Actual reversal
                    while Bnode:
                        temp = Bnode.next
                        Bnode.next = Anode
                        Anode = Bnode
                        Bnode = temp

                    # Joining ends
                    bef.next = curr
                    prev.next = aft

                    bef = prev

                else:
                    bef = curr
                
                grp += 1
            
            return dummyNode.next
            

