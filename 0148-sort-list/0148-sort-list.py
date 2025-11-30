# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # if len something is greater than 1 :
        # split it till only pairs remain.
        # then merge these pairs using std merg sorted arrays

        '''
        
        def merge() {

            Merging 2 sorted list 
            will first act on singular nodes, 
            these 2 merged sorted will be returned to the divide function, 
        }

        def divide(){
            This will divide anything greater than singletons,
            call merge function on them,
        }

        '''


        def merge(lefthead,righthead):

            dummynode = ListNode(0)
            dummy = dummynode

            currA = lefthead
            currB = righthead

            while currA or currB :

                if currA and not currB:
                    dummy.next = currA
                    dummy = dummy.next
                    currA = currA.next

                    
                elif currB and not currA:
                    dummy.next = currB
                    dummy = dummy.next
                    currB = currB.next
                    
                else:
                    if currA.val >= currB.val:
                        dummy.next = currB
                        dummy = dummy.next
                        currB = currB.next
                    else:
                        dummy.next = currA
                        dummy = dummy.next
                        currA = currA.next

            return dummynode.next
                     


        def divide(head):
            if not head or not head.next:
                return head

            right = head.next
            left = head

            while right and right.next:
                left = left.next
                right = right.next.next

            lefthead = head
            righthead = left.next
            left.next = None 

            righthead = divide(righthead)
            lefthead = divide(lefthead)

            return merge(lefthead,righthead)


        return divide(head)