# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        # list[0] will give you head of first linked list 
        old_array = lists

        def merge(headA, headB):
            print("\n merger called !")
            currA = headA
            currB = headB
            dummy_node = ListNode(0)
            dummy = dummy_node

            while currA or currB :

                if not currA and currB:
                    dummy.next = currB
                    dummy = dummy.next 
                    currB = currB.next

                elif not currB and currA: 
                    dummy.next = currA
                    dummy = dummy.next
                    currA = currA.next
                
                else:

                    if currA.val > currB.val :
                        dummy.next = currB
                        dummy = dummy.next 
                        currB = currB.next
                    
                    else :
                        dummy.next = currA
                        dummy = dummy.next
                        currA = currA.next

            return dummy_node.next

        
        while len(old_array) > 1 :
            
            array_len = len(old_array)
            new_array = []
            
            if array_len % 2 == 0:

                for i in range(0, array_len, 2): # even LL in array
                    print("\n entered this ")
                    print("\n current i and i+1 : ", i, i+1)
                    new_array.append(merge(old_array[i],old_array[i+1]))
                
            else:

                for i in range(0, array_len-1, 2): # odd LL in array
                    print("\n current i and i+1 : ", i, i+1)
                    new_array.append(merge(old_array[i],old_array[i+1]))
                new_array.append(old_array[array_len-1])


            old_array = new_array
            print("\n this is the updating lenght of old array : ", len(new_array))
            
        if old_array:
            return old_array[0]
        else :
            return None
        


