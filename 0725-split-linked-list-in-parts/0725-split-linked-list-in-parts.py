# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        if not head:
            array = []
            for i in range(k):
                array.append(None)
            return array


        curr = head
        lenght = 0
        while curr :
            lenght += 1
            curr = curr.next
        array = []
        if lenght % k == 0: # equal parts
            units = lenght // k
            curr = head
            while curr :
                newnode = ListNode(0)
                new = newnode
                for i in range(units):
                    onenode = ListNode(curr.val)
                    new.next = onenode
                    new = new.next
                    curr = curr.next
                array.append(newnode.next)
            
            return array



        
        elif lenght < k :
            units = lenght   # no of lists with single unit 
            nulls = k - lenght # no o f empty lists
            curr = head
            for i in range(units) :
                array.append(ListNode(curr.val))
                curr = curr.next
            for i in range(nulls) :
                array.append(None)

            return array

        else:
            units = lenght // k # no of units in all lists
            remains = lenght % k # no of startting lists with one extra link
            curr = head
            for i in range(remains):
                dummynode = ListNode(0)
                new = dummynode
                
                for i in range(units+1):
                    onenode = ListNode(curr.val)
                    new.next = onenode
                    new = new.next
                    curr = curr.next
                array.append(dummynode.next)
            
            for i in range(k-remains):
                newnode = ListNode(0)
                new = newnode
                for i in range(units):
                    onenode = ListNode(curr.val)
                    new.next = onenode
                    new = new.next
                    curr = curr.next
                array.append(newnode.next)
            
            return array




