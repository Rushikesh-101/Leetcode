# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        # while len(old list) == 1:
            # pop 2 lists in pair from lists
            # merge sort them
            # add each list to new club list
            # at end make new list as old list

        # only 2 pointer merge sorting
        def merge(listA,listB):
            if not listA or not listB:
                if not listA and not listB:
                    return None
                if not listA:
                    return listB
                else:
                    return listA
                
            dummyNode = ListNode(0)
            c1 = dummyNode
            p1 = listA
            p2 = listB

            while p1 and p2:
                if p1.val < p2.val:
                    c1.next = p1 
                    p1 = p1.next
                    c1 = c1.next
                else:
                    c1.next = p2
                    p2 = p2.next
                    c1 = c1.next
            
            if p1 :
                c1.next = p1
            elif p2:
                c1.next = p2
            return dummyNode.next
        





        while len(lists) > 1:
            
            new_list = []
            while len(lists) >= 2:
                listA = lists.pop()
                listB = lists.pop()
                new = merge(listA,listB)
                new_list.append(new)
            if lists:
                new_list.append(lists.pop())
            lists = new_list
        return lists[0] if lists else None