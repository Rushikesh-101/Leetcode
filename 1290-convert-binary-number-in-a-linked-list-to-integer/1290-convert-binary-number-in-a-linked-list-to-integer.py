# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
       
       #decimal_value = int(binary_string, 2)

        curr = head
        number = ""
        while curr :

            number += str(curr.val)
            curr = curr.next


        value = int(number, 2)
        return value