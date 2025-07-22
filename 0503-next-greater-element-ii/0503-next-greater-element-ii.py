class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        Arr = []
        nxtGrt = []
        for x in nums:
            Arr.append(x)
            nxtGrt.append(-1)
        for x in nums:
            Arr.append(x)
            nxtGrt.append(-1)

        print("\n this is nums twice: ", Arr)

        compStack = []
        
        y = 0
        for x in Arr:

            if not compStack:
                compStack.append(x)
                nxtGrt[y] = -1
                y+=1
                # print("\nif loop : printing nxtGrt:", nxtGrt)
                # print("\n this is the tack : ", compStack)
            
            elif compStack and x > compStack[-1]:
                z = y-1
                while compStack and x > compStack[-1]:
                    if compStack[-1] == Arr[z]:
                        compStack.pop()
                        nxtGrt[z] = x
                        z-=1
                    else :
                        z-=1

                compStack.append(x)
                # while z != y:
                #     nxtGrt[z] = x
                #     z+=1
                y+=1
                # print("\n elif loop : printing nxtGrt:", nxtGrt)
                # print("\n this is the tack : ", compStack)

            else:
                compStack.append(x)
                nxtGrt[y] = -1
                y+=1
                # print("\n else loop : printing nxtGrt:", nxtGrt)
                # print("\n this is the tack : ", compStack)
        a = len(nums)
        result = nxtGrt[0:a]
        return result

        




