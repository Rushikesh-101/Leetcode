class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        
        left = 0
        right = len(arr)-1
        mid = 0

        while left <= right :

            mid = (left + right)//2

            if arr[mid-1] < arr[mid] > arr[mid+1] :
                print("\n this is the final mid:",mid)
                return mid 


            elif arr[mid-1] >= arr[mid]:
                right = mid
            elif arr[mid] <= arr[mid+1]:
                left = mid

            
