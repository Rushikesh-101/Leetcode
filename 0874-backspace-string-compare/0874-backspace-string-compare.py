class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1 = []
        stack2 = []

        for n in s :
            if n != '#' :
                stack1.append(n)

            else :
                if stack1 :
                    stack1.pop()
            print("\n this is stack1 after append : \n", stack1)

        for n in t :
            if n != '#' :
                stack2.append(n)

            else :
                if stack2 :
                    stack2.pop()

            print("\n this is stack2 after append : \n", stack2)

        if stack1 == stack2 :
            return True

        else :
            return False