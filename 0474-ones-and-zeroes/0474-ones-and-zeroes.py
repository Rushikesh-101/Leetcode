class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # DP = {}
        # def fit(s,capM,capN):
        #     print("with : ",s)
        #     if (s,capM,capN) in DP :
        #         return DP[s,capM,capN]
        #     else :
        #         new_capM = capM
        #         new_capN = capN

        #         for i in strs[s]:
        #             if i == '0':
        #                 new_capM -= 1
        #             else:
        #                 new_capN -= 1
                
        #         if capM == 0 and capN == 0:
        #             DP[(s,capM,capN)] = 0
        #             return 0

        #         elif new_capM == 0 and new_capN == 0 :
        #             if s < len(strs)-1: 
        #                 return max( 1 , fit(s+1,capM,capN) )
        #             else :
        #                 return 1

                
        #         elif capM < 0 or capN < 0 :
        #                 return 0
                
        #         elif new_capM < 0 or new_capN < 0 :
        #             if s < len(strs)-1:
        #                 result = fit(s+1,capM,capN)
        #                 DP[(s,capM,capN)] = result
        #                 return result
        #             else:
        #                 return 0
                
        #         else:
        #             if s < len(strs)-1:
        #                 print("entered")
        #                 with_me = fit(s+1,new_capM,new_capN)
        #                 without_me = fit(s+1,capM,capN)
        #                 if with_me == 0 and without_me == 0:
        #                     return 0
        #                 result = max(1+with_me, without_me)
        #                 DP[(s,capM,capN)] = result
        #                 return result
        #             else :
        #                 return 1
                    
        # return fit(0,m,n)
        


















        DP = {}
        def func(idx,m,n):
            if idx == len(strs):
                return 0

            if (idx,m,n) in DP:
                return DP[(idx,m,n)]            

            else:

                new_m = m
                new_n = n
                for i in strs[idx]:
                    if i == '0':
                        new_m -= 1
                    else:
                        new_n -= 1



                result = func(idx+1,m,n)
                

                if new_m >= 0 and new_n >= 0:
                    result = max(result , (func(idx+1,new_m,new_n)+1))
                    
                DP[(idx,m,n)] = result
                return result
                    
                    
        return func(0,m,n)


       





















                

