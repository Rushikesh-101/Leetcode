class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        opStack = []
        prevN = 0
        valString = ''
        fVal = 0
        for n in tokens :

                if len(tokens) == 1:
                    fVal = int(n)
            
                elif n == '+' or n == '-' or n == '*' or n == '/' :
                    # print("\n entered daddy if: ")
                    # print("\n this is stack:", opStack)
                    prevN = opStack.pop()
                    # if opStack[-1] and fVal != 0:
                    if opStack and fVal == 0:
                        # print("\n entered first small if :")
                        valString = opStack.pop()
                        valString += " " + n 
                        valString+= " " + prevN
                        print("\n printing valstring:", valString)

                        fVal = eval(valString)
                        valString = ''
                        print("\n printed fval before :", fVal)
                        fVal = int(fVal) 
                        print("\n printed fval afyer :", fVal)
                        opStack.append(str(fVal))
                       


                    elif opStack :
                        valString =   " " + opStack[-1]
                        valString += " " + n
                        valString += " " + prevN
                        fVal = eval(valString)
                        
                        print("\n printing valstring:", valString)
                        valString = ''
                        
                        opStack.pop()
                        print("\n printed fval before :", fVal)
                        fVal = int(fVal) 
                        print("\n printed fval after :", fVal)
                        opStack.append(str(fVal))
                        # print("\nthis is valString: ", valString)
                        # valString = ''
                        # print("\n this is stack:", opStack) 
                        # print("\n this is fVal: ", fVal)

                    # elif not opStack or fVal != 0 :
                    #     # print("\n this is small else :")
                    #     valString = " " + str(fVal)
                    #     valString += " " + n
                    #     valString += " " + prevN                    
                    #     fVal = eval(valString)

                    #     opStack.append(fVal)
                    #     # print("\nthis is valString: ", valString)
                    #     # valString = ''
                    #     # print("\n this is stack:", opStack)
                    #     # print("\n this is fVal: ", fVal)

                    
                else :
                    # print("\n this is daddy else: ")
                    opStack.append(n)
                    # valString = valString + " " + n
                    # print("\nthis is valString: ", valString)
                    # print("\n this is stack:", opStack)
                    # print("\n this is fVal: ", fVal)

        return fVal