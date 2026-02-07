class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # at most 2 people allowed !
        def numRescue():
            people.sort()
            l = 0
            r = len(people)-1
            boat = 0

            while l <= r:
                if l == r:
                    boat += 1
                    return boat
                elif people[r] == limit:    #right == limit
                    boat += 1
                    r -= 1
                else :                      # right < limit
                    if people[r]+people[l] <= limit:
                        boat += 1
                        r-=1
                        l+=1
                    else:
                        boat += 1
                        r -= 1
            return boat
        return numRescue()


