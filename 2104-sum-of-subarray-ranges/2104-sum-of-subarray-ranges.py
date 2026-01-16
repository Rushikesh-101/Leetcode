class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        
        
        def min_ranges():
            mono = []
            min_total = 0
            for i in range(len(nums)):
                total = 0
                while mono and nums[mono[-1]] >= nums[i]:
                    k = mono.pop()
                    right = i 
                    left = mono[-1] if mono else -1

                    total = nums[k] * (right-k) * (k-left)
                    min_total += total
                mono.append(i)
            while mono:
                k = mono.pop()
                right = len(nums)
                left = mono[-1] if mono else -1

                total = nums[k] * (right-k) * (k-left)
                min_total += total
            print(min_total)
            return min_total
            
        def max_ranges():
            mono = []
            max_total = 0
            for i in range(len(nums)):
                total = 0
                while mono and nums[mono[-1]] <= nums[i]:
                    k = mono.pop()
                    right = i 
                    left = mono[-1] if mono else -1

                    total = nums[k] * (right-k) * (k-left)
                    max_total += total
                mono.append(i)
            while mono:
                k = mono.pop()
                right = len(nums)
                left = mono[-1] if mono else -1

                total = nums[k] * (right-k) * (k-left)
                max_total += total
            print(max_total)
            return max_total
        
        return (max_ranges() - min_ranges())

                


