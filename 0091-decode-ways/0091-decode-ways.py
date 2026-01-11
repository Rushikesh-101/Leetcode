class Solution:
    def numDecodings(self, s: str) -> int:
        lenght = len(s)-1
        DP = {}
        def no_of_ways(n):

            if n in DP :
                return DP[n]

            else:

                if n == lenght :
                    return 1
                left = 0
                right = 0


                if n < lenght and s[n+1] != '0':
                    left =  no_of_ways(n+1)

                if n < lenght - 1 and int(s[n+1:n+3]) < 27 and s[n+1] != '0':
                    right = no_of_ways(n+2)

                DP[n] = right + left

                return right + left
        
        if s[0] == '0':
            return 0 
        elif len(s) == 1:
            return 1

        return  no_of_ways(-1)