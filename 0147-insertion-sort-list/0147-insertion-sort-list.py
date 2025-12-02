# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        if not head.next :
            return head
        ''' 

        INSERTION SORT :
        > create sorted list by detaching element one by one from original list.
        > compare detached element with sorted list elements by to know its insertion point

        '''


        dummynode = ListNode(0)
        dummy = dummynode
        curr = head
        temp = curr.next
        dummy.next = curr
        curr.next = None
        dummy = dummy.next
        curr = temp
        temp = curr.next
        '''
        > From above, first element is added in the sorted list and detached from unsorted list
        and curr is on the second node of unsorted list.
        > Dummy is on first sorted node
        '''
        ctr = 0
        while curr :
            prev = dummynode
            dummy = prev.next 

            temp = curr.next

            
            while dummy and curr.val > dummy.val:
                dummy = dummy.next
                prev = prev.next
            prev.next = curr
            curr.next = dummy
            curr = temp
            

        return dummynode.next

