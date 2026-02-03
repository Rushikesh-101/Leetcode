class Solution:
    def reverseWords(self, s: str) -> str:


        # # HOW TO OPTIMISE THIS ??? 

        # def reverse():
        #     stack = []
        #     word = ''
        #     for c in range(len(s)):
        #         if s[c] == ' ':
        #             if word:
        #                 stack.append(word)
        #                 word = ''
        #         elif c == len(s)-1 and s[c] != ' ':
        #               word += s[c]
        #               stack.append(word)
        #         else:
        #             word += s[c]


        #     sentence = ''
        #     while stack:
        #         sentence += stack.pop()
        #         if stack:
        #             sentence += ' '

        #     return sentence
        
        # return reverse()


        # Possibily optimal approach
        def reverse():
            sentence =''
            word = ''
            for c in range(len(s)):
                if s[c] == ' ':
                    if word:
                        sentence = word + ' ' + sentence
                        word = ''
                elif c == len(s)-1 and s[c] != ' ':
                      word += s[c]
                      sentence = word + ' ' + sentence 
                else:
                    word += s[c]

            return sentence[:len(sentence)-1]
        
        return reverse()
        