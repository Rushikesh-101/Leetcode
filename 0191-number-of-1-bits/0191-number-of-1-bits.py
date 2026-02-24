class Solution:
    def hammingWeight(self, n: int) -> int:
            
        set_count = 0
        while n:                # -- cant use in rnage(n), cause n represents dec lenght.
            if (n & 1) == 1:
                set_count += 1
            n = n >> 1

        return set_count