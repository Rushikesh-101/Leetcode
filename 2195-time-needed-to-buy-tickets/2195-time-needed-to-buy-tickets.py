class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        
        #fix a pointer on first element of que
            # move pointer in reverse direction,
                # ptr -= 1, if 0, len(que)-1

        #while pointer != k


        que = deque()

        for i in range(len(tickets)):
            que.append(tickets[i])
        ptr = k
        time = 0
        while que:

            if que[0] == 1:
                if ptr == 0: # meansque[0] is tgt
                    time += 1
                    return time
                else:
                    que.popleft() # non tgt element got over : len(que) got reduced so ptr will be -1
                    
                    ptr -= 1
                    time += 1
                
            else:
                if ptr == 0: # means que[0] is tgt but its not 1:

                    que.append(que[ptr]-1)
                    que.popleft()
                    ptr = len(que)-1
                    time += 1

                else: # means que[0] is non tgt and not 1:
                    val = que.popleft()-1
                    que.append(val)
                    ptr -= 1
                    time += 1






