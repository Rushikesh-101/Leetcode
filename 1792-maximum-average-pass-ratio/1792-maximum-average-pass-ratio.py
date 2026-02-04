class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        def calcu(i):
            old = classes[i][0]/classes[i][1]
            new = (classes[i][0]+1)/(classes[i][1]+1)
            gain = new - old
            return gain

        def ratioratio():
            hip = []
            heapq.heapify(hip)
            # Calculating and pushing all initial gains
            for i in range(len(classes)):
                gain = calcu(i)
                heapq.heappush(hip,(-gain,i))

            for _ in range(extraStudents):
                pop = heapq.heappop(hip)
                idx = pop[1]
                gain = pop[0]
                x,y = classes[idx]
                x += 1
                y += 1
                classes[idx] = [x,y]

                new_gain = calcu(idx)
                heapq.heappush(hip,(-new_gain,idx))
            
            total = 0
            for i in classes:
                total += i[0]/i[1]
            return total/len(classes)

        
        return ratioratio()


            