class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        
        # maintain increasing monotonic stack
        total_sum = 0
        mono = []
        for i in range(len(arr)):
            while mono and arr[mono[-1]] >= arr[i]:
                total = 0
                pop = mono.pop()
                if mono :
                    total = (pop-mono[-1]) * (i-pop )
                else :
                    total = (pop+1) * (i-pop)

                total_sum += arr[pop]*total
            mono.append(i)

        while mono :
            pop = mono.pop()
            if mono :
                total =( pop-mono[-1] )* (len(arr)-pop )
            else :
                total = (pop+1) * (len(arr)-pop)

            total_sum +=  arr[pop]*total
        
        return total_sum%(10**9+7)


