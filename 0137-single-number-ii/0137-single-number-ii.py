class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        # approach was to create a number where at each digit place we count number of set bits of all number
        # Divide it by three
        # Only single bit will remain
        # We will be running nested loops: 
        # Outside loop for 0-32 bit of result
        # Inside loop to check each elements that particular bit condition

        # Between both loops a count exists for each bit position
        # by end of inner loop the count is divide by 3 
        # If divisible then ans bit is 0 on that position, else 1


        def single():

            ans = 0
            for i in range(0,32):
                count = 0
                for j in range(0,len(nums)):
                    if nums[j] & (1 << i):
                        count += 1
                
                if count%3 != 0:
                    ans = ans | (1 << i) # using OR cause 1 has to be taken if exists in any
            if ans >= 2**31:    # This is because python has dynamic memory allocation, and doesnt interpret 31st bit as a sign bit
                ans -= 2**32
            return ans

        return single()