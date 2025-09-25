class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        
        studque = deque()
        sandque = deque()
        indx = []

        for i in range(len(students)):
            studque.append(students[i])
        for i in range(len(sandwiches)):
            sandque.append(sandwiches[i])

        
        while studque:

            lenght = len(sandque)
            print("this is lenght:",lenght)

            for i in range(len(studque)):
                if studque[0] == sandque[0]:
                    studque.popleft()
                    sandque.popleft()
                    
                else:
                    studque.append(studque.popleft())
                    print("\nque after rot:",studque)

            if len(sandque) == 0:
                return 0
            
            print("this is lenght",len(sandque))
            if lenght == len(sandque):
                
                return len(studque)
            
        


        
