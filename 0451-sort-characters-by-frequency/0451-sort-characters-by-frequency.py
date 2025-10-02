class Solution:
    def frequencySort(self, s: str) -> str:
        
        # Intuition

        # 1. Take freq count with help of dict
        # 2. Creat priority max heap(value : alphabet ) with negative freq of those char
        # 3. As per count of each alphabet from pop of heap, append to array
        # 4. string made from array

    # storing freq of each char of str in a dict
        freqdict = {}

        for char in s :
            if char in freqdict:
                freqdict[char] += 1
            else:
                freqdict[char] = 1

    # creating heap from key values of dict
        myHeap = []
        for char, freq in freqdict.items() :
            heapq.heappush(myHeap,(-freq,char))

    #   each pop into an array with count
        res = []
        while myHeap :
            priority, value = heapq.heappop(myHeap)
            while priority != 0:
                res.append(value)
                priority += 1
        print("\n Array res by end of heap pop : ", res)

        output = "".join(res)
        print("\n This is final string : ", output)

        return output

        