class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        left = 0
        right = len(nums)-1
        middle = (left + right)//2
        value = nums[middle]
        
        while left <= right :

            middle = (left + right)//2
            value = nums[middle]

            if value == target :
                return middle

            elif value < target :

                left = middle + 1 

            else :

                right = middle - 1 

        if value > target and middle == 0 :
            return 0 

        elif value > target and middle != 0 :
            return middle 

        elif value < target and middle == 0 :
            return 1 

        elif value < target and middle != 0 :
            return middle + 1




        