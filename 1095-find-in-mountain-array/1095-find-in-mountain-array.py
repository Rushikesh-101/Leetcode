# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        def binarySearch(left,right):
            while left <= right:
                mid = left + (right-left)//2
                mid_val = mountainArr.get(mid)
                if mid_val == target:
                    return mid
                elif mid_val > target:
                    right = mid-1
                else:
                    left = mid+1
            return False
        
        def revbinarySearch(left,right):
            while left <= right:
                mid = left + (right-left)//2
                mid_val = mountainArr.get(mid)
                if mid_val == target:
                    return mid
                elif mid_val < target:
                    right = mid-1
                else:
                    left = mid+1
            return False
        
        end = mountainArr.length()-1
        left = 0
        right = end
        pivot = 0
        while left <= right:
            mid = left + (right-left)//2
            mid_val = mountainArr.get(mid)

            if mid == 0 :
                if mid_val > mountainArr.get(mid+1):
                    pivot = 0
                    break
                left += 1
            elif mid == end :
                if mountainArr.get(mid-1) < mid_val:
                    pivot = end
                    break
            elif mountainArr.get(mid-1) < mid_val > mountainArr.get(mid+1):
                pivot = mid
                break
            elif mid_val <  mountainArr.get(mid+1):
                left = mid+1
            else:
                right = mid-1

        first = binarySearch(0,pivot)
        second = revbinarySearch(pivot,end)

        
        if type(first) == int:
            return first
        elif type(second) == int:
            return second 
        else:
            return -1

        


            


