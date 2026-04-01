class Solution:
    def reverseString(self, s: List[str]) -> None:
        
        def rev(arr):
            l = 0
            r = len(s)-1

            while l < r:
                temp = arr[l]
                arr[l] = arr[r]
                arr[r] = temp

                l += 1
                r -= 1
        
            return arr

        return rev(s)