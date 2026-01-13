class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        def max_average(nums,k):
            left = 0
            right = k-1
            total = 0

            for i in range(0,k):
                total += nums[i]

            avg = total/k

            max_avg = avg

            while right < len(nums)-1:
                total -= nums[left]
                total += nums[right+1]
                avg = total/k

                if avg > max_avg :
                    print("for avg till", right)
                    max_avg = avg

                left += 1
                right += 1

                
            return max_avg

        return max_average(nums,k)

