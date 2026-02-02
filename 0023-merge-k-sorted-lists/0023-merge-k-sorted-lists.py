# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        # list[0] will give you head of first linked list 
        # old_array = lists

        # def merge(headA, headB):
        #     currA = headA
        #     currB = headB
        #     dummy_node = ListNode(0)
        #     dummy = dummy_node

        #     while currA or currB :

        #         if not currA and currB:
        #             dummy.next = currB
        #             dummy = dummy.next 
        #             currB = currB.next

        #         elif not currB and currA: 
        #             dummy.next = currA
        #             dummy = dummy.next
        #             currA = currA.next
                
        #         else:

        #             if currA.val > currB.val :
        #                 dummy.next = currB
        #                 dummy = dummy.next 
        #                 currB = currB.next
                    
        #             else :
        #                 dummy.next = currA
        #                 dummy = dummy.next
        #                 currA = currA.next

        #     return dummy_node.next

        
        # while len(old_array) > 1 :
            
        #     array_len = len(old_array)
        #     new_array = []
            
        #     if array_len % 2 == 0:

        #         for i in range(0, array_len, 2): # even LL in array
        #             new_array.append(merge(old_array[i],old_array[i+1]))
                
        #     else:

        #         for i in range(0, array_len-1, 2): # odd LL in array
        #             new_array.append(merge(old_array[i],old_array[i+1]))
        #         new_array.append(old_array[array_len-1])


        #     old_array = new_array
            
            
        # if old_array:
        #     return old_array[0]
        # else :
        #     return None
        


        # HEAP BASED APPROACH
        def heapMerge():
            # if not lists or not lists[0]:
            #     return None
            hip = []
            heapq.heapify(hip)
            res = ListNode(0)
            curr = res

            # Add all initial node ref into heap
            for i in lists:
                if not i:
                    continue
                heapq.heappush(hip,(i.val,id(i),i))
            
            # Build merged list till heap exists
            while hip:
                pop = heapq.heappop(hip)
                curr.next = ListNode(pop[0])
                curr = curr.next
                if pop[2].next:
                    new = pop[2].next
                    heapq.heappush(hip,(new.val,id(new),new))
            
            return res.next
        
        return heapMerge()
            
