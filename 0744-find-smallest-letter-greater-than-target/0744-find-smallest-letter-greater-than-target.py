class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        def BSonLetters():
            left = 0
            right = len(letters)-1

            while left < right:
                mid = left + (right-left)//2

                if letters[mid] > target:
                    right = mid
                else :
                    left = mid+1
            if letters[right] > target:
                return letters[right]
            else:
                return letters[0]
        return BSonLetters()