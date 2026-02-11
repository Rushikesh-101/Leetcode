class Solution:
    def maximumSwap(self, num: int) -> int:
        '''
        def swapp(num):
            num = str(num)
            l = 0
            maxx = (0,0)
            new = ''
            for r in range((len(num)-1),0,-1):
                if int(num[r]) > maxx[0]:
                    maxx = (int(num[r]),r)
            
            found = 0
            while l < maxx[1]:
                if int(num[l]) < maxx[0]:
                    new = num[:l]+str(maxx[0])+num[l+1:maxx[1]]+num[l]+num[maxx[1]+1:]
                    found = 1
                if found:
                    break
                l += 1
            if new == '':
                return int(num)
            else:
                return int(new)
        
        return swapp(num)
        '''

        # Problem with above, comparing left to right with global maximum :
        # Fails at testcases like 99901, where 9 was max and 0 was supposed to be replaced by 1

        # Solution : For each index from right to left track greatest to right for each index
        # Then move from left to right and swap the first greatest you find 


        def swap(num):
            num = str(num)
            maxx = (0,0)
            res = [-1]*len(num)
            for i in range(len(num)-1,-1,-1):
                if int(num[i]) < int(maxx[0]):
                    res[i] = maxx
                elif int(num[i]) == int(maxx[0]):
                    pass
                else:
                    maxx = (num[i],i)
            
            new = ''
            for i in range(len(res)):
                if res[i] != -1:
                    idx = res[i][1]
                    val = res[i][0]
                    # we have to swap num[i] with maxx[i]
                    new = num[:i] +val +num[i+1:idx] +num[i] + num[idx+1:]
                    break
            
            if new == '':
                return int(num)
            else:
                return int(new)
        
        return swap(num)

