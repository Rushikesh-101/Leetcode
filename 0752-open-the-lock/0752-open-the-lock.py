class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        

        def dead():

            deadset = set()
            for d in deadends:
                deadset.add(d)
            que = deque()
            if '0000' in deadset:
                return -1
            if target == '0000':
                return 0
            que.append('0000')
            flips = 1

            while que:
                for _ in range(len(que)):
                    digit = que.popleft()
                    for s in range(len(digit)):
                        num = int(digit[s])
                        up = 0 if num == 9 else num + 1
                        down = 9 if num == 0 else num - 1
                        
                        newf = digit[:s] + str(up) + digit[s+1:]
                        newb = digit[:s] + str(down) + digit[s+1:]

                        if newf not in deadset:
                            if newf == target:
                                return flips
                            deadset.add(newf)
                            que.append(newf)

                        if newb not in deadset:
                            if newb == target:
                                return flips

                            deadset.add(newb)
                            que.append(newb)
                        
                        
                        
                        
                                
                flips += 1
                
            return -1    

        return dead()   
                                

                                    
                            



