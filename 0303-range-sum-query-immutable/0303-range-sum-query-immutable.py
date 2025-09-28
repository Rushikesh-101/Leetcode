class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = [0]
        self.size = 0
        for i in range (len(nums)):
            self.prefix.append(self.size + nums[i])
            self.size += nums[i]
        
        

    def sumRange(self, left: int, right: int) -> int:

        val = self.prefix[right+1] - self.prefix[left]
        return val
        
        # calculates from prefix function and return sum

        #inclusive left right means prefix left should not have its on value
        #but inclusive right means prefix left should take left + 1 ki value


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)

