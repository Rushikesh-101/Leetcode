class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        def uniquePair():
            pair = 0
            for n in nums:
                pair = pair ^ n

            diff_bit = pair & -pair
            grp_A = 0
            grp_B = 0
            for n in nums:
                if n & diff_bit:
                    grp_A ^= n
                else:
                    grp_B ^= n

            res = [grp_A,grp_B]

            return res
        return uniquePair()



