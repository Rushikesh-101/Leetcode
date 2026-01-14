class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        


        def no_of_subarrays():
            left = 0
            right = 0
            total = 0
            count = 0
            target = threshold * k

            for right in range(k):
                total += arr[right]
            if total >= target :
                count += 1

            for right in range(k,len(arr)):
                total += arr[right]
                total -= arr[left]
                left += 1

                if total >= target:
                    count += 1
            
            return count
        
        return no_of_subarrays()

