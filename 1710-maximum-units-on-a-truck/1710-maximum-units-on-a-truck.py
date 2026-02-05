class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key = lambda x: x[1], reverse = True)
        i = 0
        total = 0
        while truckSize and i < len(boxTypes):
            for j in range(boxTypes[i][0]):
                if truckSize == 0:
                    return total
                truckSize -= 1
                total += boxTypes[i][1]
            i += 1
        return total