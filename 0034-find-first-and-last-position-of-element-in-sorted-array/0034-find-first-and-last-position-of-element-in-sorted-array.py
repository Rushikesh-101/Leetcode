class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        if len(nums) == 0:
            INDEX = [-1,-1]
        
        else :
            INDEX = [0,0]

            left = 0 
            right = len(nums)-1
            middle = 0

            while left <= right :

                middle = (left + right)//2

                if nums[middle] == target:
                    break

                if nums[middle] < target :
                    left = middle + 1

                else :
                    right = middle - 1


            # now we have middle == target

            #searching for leftmost 

            left = 0
            right = middle
            resultL = 0
            

            while left <= right :

                mid = (left + right)//2

                if nums[mid] == target :
                    
                    resultL = mid
                    right = mid
                
                if nums[mid] < target :
                    left = mid + 1

                else :
                    right = mid -1
                    

            if nums[resultL] != target:
                INDEX[0] = -1
            else :
                INDEX[0] = resultL


                

            left = middle
            right = len(nums)-1
            mid = 0
            resultR = 0

            while left <= right :

                mid = (left + right)//2

                if nums[mid] == target:
                    resultR = mid
                    left = mid

                if nums[mid] > target:
                    right = mid -1
                
                else :
                    left = mid +1
                    

            if nums[resultR] != target:
                INDEX[1] = -1
            else:
                INDEX[1] = resultR


        return INDEX

