# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        def twinSum():
            headA = head
            headB = head
            fast = head

            # finding mid
            while fast and fast.next:
                fast = fast.next.next
                headB = headB.next

            # reversing second half
            prev = headB
            curr = prev.next

            while curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            headB.next = None
            # Obtaining global max
            headB = prev
            maxx = 0
            while headB:
                vall = headA.val + headB.val
                headA = headA.next
                headB = headB.next
                maxx = max(maxx,vall)
            
            return maxx


        return twinSum()

