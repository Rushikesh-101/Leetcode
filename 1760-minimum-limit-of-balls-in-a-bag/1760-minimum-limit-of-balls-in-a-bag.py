class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        

        def bags(mid):
            
            splits = maxOperations
            for n in nums:
                if n > mid:
                    if n%mid == 0:
                        splits -= (n//mid)-1
                    else:
                        splits -= n//mid
                if splits < 0:
                    return False
            return True



        def my_balls():

            left = 1
            right = max(nums)

            while left < right:
                mid = left + (right-left)//2

                if bags(mid):
                    right = mid
                else:
                    left = mid+1

            return right
        
        return my_balls()