"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head :
            return None
        # if not head.next:
        #     clone = Node(head.val)

        #     if head.random:
        #         clone.random = Node(0)
        #     return clone


        prev = head
        curr = head.next

        while curr:

            clone = Node(prev.val)
            prev.next = clone
            clone.next = curr

            prev = curr
            curr = prev.next
        clone = Node(prev.val)
        prev.next = clone


        prev = head
        curr = prev.next

        while prev and curr:
            if prev.random:
                curr.random = prev.random.next
            prev = curr.next
            if curr.next:
                curr = curr.next.next
        

        clone_head = head.next
        curr = head
        clone = clone_head
        

        while curr and clone :
            curr.next = clone.next
            if clone.next:
                clone.next = clone.next.next

            curr = curr.next
            clone = clone.next
        
        return clone_head

        