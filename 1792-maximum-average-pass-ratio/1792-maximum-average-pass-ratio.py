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
            tot_gain = 0
            act_ratio = 0
            # Calculating and pushing all initial gains
            for i in range(len(classes)):
                gain = calcu(i)
                heapq.heappush(hip,(-gain,i))

                act_ratio += classes[i][0]/classes[i][1]


            for _ in range(extraStudents):
                pop = heapq.heappop(hip)
                idx = pop[1]
                gain = pop[0]
                tot_gain += -gain
                x,y = classes[idx]
                x += 1
                y += 1
                classes[idx] = [x,y]

                new_gain = calcu(idx)
                heapq.heappush(hip,(-new_gain,idx))
            
            max_total = (act_ratio+tot_gain)/len(classes)

            return max_total
        
        return ratioratio()


            