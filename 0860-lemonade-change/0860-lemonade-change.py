class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        def lemoChange():
            trsry = (0,0)   # denote amount for each demonition 10 and 5
            for cust in bills:
                pop = cust
                if pop == 20 and trsry[0] != 0:
                    pop -= 10
                    trsry = trsry[0]-10, trsry[1]
                
                while pop >= 10 and trsry[1] != 0:
                    pop -= 5
                    trsry = trsry[0],trsry[1]-5
                
                if pop > 5:
                    return False
                else:
                    if cust == 10:
                        trsry = trsry[0]+10,trsry[1]
                    elif cust == 5:
                        trsry = trsry[0], trsry[1]+5


            return True
        return lemoChange()