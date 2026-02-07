class Solution:
    def maxArea(self, height: List[int]) -> int:
        def max_water():
            left = 0
            right = len(height)-1
            water = 0

            while left < right:
                area = ((right-left)) * min(height[right],height[left]) 
                water = max(water,area)

                if height[left] < height[right]:
                    left += 1
                elif height[left] > height[right]:
                    right -= 1
                else:
                    if height[left+1] < height[right-1]:
                        right -= 1
                    elif height[left+1] < height[right-1]:
                        left += 1
                    else:
                        left += 1
            
            return water
        
        return max_water()