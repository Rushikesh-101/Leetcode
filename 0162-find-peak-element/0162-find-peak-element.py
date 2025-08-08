class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        # intution : get a mid : 

        #             if mid-1 < mid > mid+1:
        #                 return mid 

        #             elif mid-1 > mid :
        #                 move right to mid

        #             else mid < mid +1 :
        #                 move left to mid

        left = 0 
        right = len(nums)-1
        mid = 0

        while left <= right :

            mid = (left + right)//2
            print("\nthis is mid:",mid,"\nthis is left:",left,"\nthis is right:",right)

            if len(nums)==1:
                return 0
            
            
            elif mid == 0 or mid == len(nums)-1:
                print("entered edge case")

                if mid == 0 and nums[mid] > nums[mid+1]:
                    print("\nmid at left mid:", nums[mid])
                    return mid
                elif mid == len(nums)-1 and nums[mid-1]<nums[mid]:
                    print("\nmid at right mid:",nums[mid])
                    return mid
                # else :
                #     if mid == 0:
                #         mid = mid+1
                #     elif mid == len(nums)-1:
                #         mid = mid -1
                
            
            
            if right==mid or left==mid :
                if nums[mid-1] < nums[mid] > nums[mid+1]:
                    return mid
                
                else :
                    if mid == 0:
                        mid = right
                        if nums[mid-1] < nums[mid] :
                            return mid

                    elif mid == len(nums)-1:
                        mid= mid-1
                    if nums[mid-1] < nums[mid] > nums[mid+1]:
                        return mid 


            if nums[mid-1] < nums[mid] > nums[mid+1]:
                print("\nthis is the final mid", nums[mid])
                return mid
  
            
            elif nums[mid] <= nums[mid+1] :
                left = mid+1

            elif nums[mid-1] >= nums[mid] :
                right = mid-1
            
            

            
            
        return -1

