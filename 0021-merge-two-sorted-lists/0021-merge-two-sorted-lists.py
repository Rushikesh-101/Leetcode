# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 :
            return list2
        elif not list2 :
            return list1
        
        
        DummyNode = ListNode(0)
        Dummy = DummyNode
        
        currA = list1
        currB = list2

        

        while currA != None or currB != None :

            if not currA and currB :
                Dummy.next = currB
                Dummy = Dummy.next
                currB = currB.next

            elif not currB and currA:
                Dummy.next = currA
                Dummy = Dummy.next
                currA = currA.next

            else:
                if currA.val >= currB.val:
                    Dummy.next = currB
                    Dummy = Dummy.next
                    currB = currB.next
                else:
                    Dummy.next = currA
                    currA = currA.next
                    Dummy = Dummy.next
               

        return DummyNode.next


        