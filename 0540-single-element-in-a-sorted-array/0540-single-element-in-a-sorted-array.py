class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:

        left = 0
        right = len(nums)-1
        mid = 0
        while left <= right :

            mid = (left+right)//2

            if left == right:
                 print("\nelement at end:",nums[left])
                 break

            if nums[mid]==nums[mid+1] :
                if ( right - mid )%2 == 0:
                    left = mid + 2
                    print("\nthis is for if1:","\nthis is L:",left,"\nthis is R:",right)
                else :
                     right = mid -1
                print("\nthis is for elif2:","\nthis is L:",left,"\nthis is R:",right)
                     

            elif nums[mid] != nums[mid-1]: 
                print("\nthis is for elif1:","\nthis is L:",left,"\nthis is R:",right)
                print("\nthis is from elif1:", nums[mid])
                return nums[mid]
              
            
            else :
                if (right-mid)%2 == 0 :
                      right = mid -2
                else :
                     left = mid + 1
                print("\nthis is for else:","\nthis is L:",left,"\nthis is R:",right)
                print("\nthis is from else:", nums[mid])
             

            

        print("\nthis is last return:",nums[mid])
        return nums[mid]
            


                



               