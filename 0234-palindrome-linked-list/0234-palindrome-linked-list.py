# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        # stack = []
        slow = head
        fast = head

        # while fast :
        #     stack.append(fast.val)
        #     fast = fast.next
        # print("this is the stack : ", stack)
        # while slow :
        #     if slow.val != stack.pop():
        #         return False
        #     slow = slow.next
        # return True

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
           

        prev = None
        curr = slow
        

        while curr != None :
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        

        L1 = head
        L2 = prev

        while L2 != None :
            if L1.val != L2.val :
                return False
            L1 = L1.next
            L2 = L2.next
        return True


        
        

