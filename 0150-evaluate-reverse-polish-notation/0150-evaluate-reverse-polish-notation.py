class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        def reverse_polish():
            stack = []

            for op in tokens:

                if op == '+' or op == '-' or op == '*' or op =='/':
                    a = int(stack.pop())
                    b = int(stack.pop())
                    res = 0
                    match op:
                        case '+':
                            res = a+b
                        case '-':
                            res = b-a
                        case '*':
                            res = a*b
                        case '/':
                            res = b/a
                    stack.append(res)

                
            
                else:
                    stack.append(op)
                
            return int(stack.pop())
        return reverse_polish()
