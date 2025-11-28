# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        stack = []
        slow = head
        fast = head

        while fast :
            stack.append(fast.val)
            fast = fast.next
        print("this is the stack : ", stack)
        while slow :
            if slow.val != stack.pop():
                return False
            slow = slow.next
        return True


        
        

