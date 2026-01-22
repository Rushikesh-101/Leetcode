class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        
        # Operator will always come outside the bracket
        # ignore the commas inside of brackets 
        # Once you hit ) you have to evaute 
        # two operators are also separeted by 
        # Either there will be an operator behind a bracket or another value 
            # if its another value, use the last seen operator 


        def bool_exp():
            stack = []
            op = ''
            op_set = {'&','|','!'}
            for char in expression:

                if char == ',':
                    continue
                
                elif char == ')':
                    val = ''
                    while stack[-1] != '(':
                        val += stack.pop()
                    stack.pop() # removed opening bracket

                    if stack and stack[-1] in op_set: 
                        res = ''
                        match stack.pop():
                            case '!':
                                if val =='t':
                                    res = 'f'
                                else:
                                    res = 't'
                            case '&':
                                if 'f' in val:
                                    res = 'f'
                                else:
                                    res = 't'
                            case '|':
                                if 't' in val:
                                    res = 't'
                                else:
                                    res = 'f'
                        stack.append(res)

                
                else:
                    if char in op_set:
                        op = char
                    stack.append(char)
                
            if stack.pop() == 'f':
                return False
            else:
                return True
        
        return bool_exp()
            
