class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        repeater = set()
        for i in nums:
            if i in repeater:
                return True
            else:
                repeater.add(i)
        return False