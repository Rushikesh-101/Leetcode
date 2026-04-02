class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        # lets use merge sort with recursion 

        def mergesort(numA, numB):
            a = b = 0 
            new_list = []
            while a < len(numA) and b < len(numB):
                # compare and create new list
                if numA[a] < numB[b]:
                    new_list.append(numA[a])
                    a += 1
                else:
                    new_list.append(numB[b])
                    b += 1
                
            while a < len(numA):
                new_list.append(numA[a])
                a += 1

            while b < len(numB):
                new_list.append(numB[b])
                b += 1
            return new_list

                
            
        
        def div(arr):


            if len(arr) == 1:
                return arr
            
            else:
                split = len(arr)//2
                numA = arr[:split]
                numB = arr[split:]

                left = div(numA)
                right = div(numB)

                return mergesort(left,right)
        
        return div(nums)
