class Solution:
    def decodeString(self, s: str) -> str:
        
        # ruled by [ ] square brackets 
        # Trigger : ] closing square bracket
        # After evaluation again append into the stack
        def decode():
            stack = []
            i = 0
            n = len(s)

            while i < n :

                if s[i].isdigit():
                    num = ''
                    while i < n and s[i].isdigit():
                        num += s[i]
                        i += 1
                    stack.append(num)
                
                elif s[i].isalpha():
                    word = ''
                    while i < n and s[i].isalpha():
                        word += s[i]
                        i += 1
                    if stack and stack[-1].isalpha():
                        word = stack.pop()+word
                    stack.append(word)
                
                elif s[i] == ']':   # EXECUTION
                    print(stack)
                    word = stack.pop()
                    stack.pop() # removed open bracket
                    count = stack.pop()
                    new_word = ''
                    for _ in range(int(count)):
                        new_word += word
                    
                    if stack and stack[-1].isalpha():
                        new_word = stack.pop()+new_word
                    stack.append(new_word)

                    i += 1
                
                else:
                    stack.append(s[i])
                    i += 1

            print(stack[-1])
            return stack.pop()

        return decode()