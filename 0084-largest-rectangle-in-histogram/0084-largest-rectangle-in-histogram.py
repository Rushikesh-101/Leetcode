class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        #intution: Performing NSE on LTR and RTL.
        # storing indexes instead of values
        # taking difference of NSE indexes with actual indexes
        # adding the LTR and RTL 
        # finding max number from it

        # NSE = []
        # LTR = []
        # RTL = []
        # compStack = []

        # for n in heights :
        #     NSE.append(-1)

        # for index, value in enumerate(heights) :

        #     if not compStack :
        #         compStack.append(index)
        #         LTR[index] = -1

        #     elif value <= heights[compStack[-1]] :

        #         while value <= heights[compStack[-1]] :

        #             compStack.pop()

        #         LTR[index] = compStack[-1]
        #         compStack.append(index)

        #     else :
        #         compStack.append(index)
        #         LTR[index] = -1

        # for index, values in enumerate(LTR) :
        #     if value == -1 :
        #         NSE[index] = 0
        #     else :
        #         NSE[index] = LTR[index] - index

        
        # compStack = []
        # for index, value in enumerate(reversed(heights)) :


        #     if not compStack :
        #         compStack.append(index)
        #         RTL[index] = -1

        #     elif value <= heights[compStack[-1]] :

        #         while value <= heights[compStack[-1]] :

        #             compStack.pop()

        #         RTL[index] = compStack[-1]
        #         compStack.append(index)

        #     else :
        #         compStack.append(index)
        #         RTL[index] = -1

            
        compStack = []
        maxArea = 0
        toCalc = 0

        for index, value in enumerate(heights) :

            if not compStack :
                compStack.append(index)
                
            
            elif compStack and value <= heights[compStack[-1]] :
                
                
                while compStack and value <= heights[compStack[-1]] :
                    toCalc = compStack.pop()
                    if compStack :
                        PSE = compStack[-1]
                    else :
                        PSE = -1
                    NSE = index
    
                    Area = ( ( index - toCalc ) + ( toCalc - PSE ) -1 ) * heights[toCalc]
                    # print(" \n this is the area for :",heights[toCalc],"\n", Area )
                    if Area > maxArea :
                        maxArea = Area
                    # print("\n calculated with elif ")
                compStack.append(index)
            
            else :
                compStack.append(index)
                

        #alpha IF
        if compStack :
            # print("\n this is the index used for alpha IF :", index)
            size = compStack[-1]
            toCalc = compStack.pop()
            if compStack :
                PSE = compStack[-1]
            else :
                PSE = -1 

            Area = (( size - toCalc    ) + ( toCalc - PSE ))  * heights[toCalc]
            # print(" \n this is the area for :",heights[toCalc],"\n", Area )
            if Area > maxArea :
                maxArea = Area
            # print("\ncalculated with first if")

        if compStack :
            while compStack :
                toCalc = compStack.pop()
                if compStack :
                    PSE = compStack[-1]
                else :
                    PSE = -1 

                Area = (( size - toCalc    ) + ( toCalc - PSE ))  * heights[toCalc]
                # print(" \n this is the area for :",heights[toCalc],"\n", Area )
                if Area > maxArea :
                    maxArea = Area
                # print("\ncalculated with second if ")



        return maxArea


            



