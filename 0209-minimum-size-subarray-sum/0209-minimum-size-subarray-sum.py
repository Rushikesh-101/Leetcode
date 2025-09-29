class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        

        if len(nums) == 1 and nums[0] < target:
            return 0
        elif len(nums) == 1 and nums[0] >= target:
            return 1

        else :
            prefix = [0]
            sum = 0
            for i in range(len(nums)):

                
                prefix.append(sum + nums[i])
                sum += nums[i]


            dcrsngQue = deque()

            left = 0
            right = 0

            #iterate through nums using left and right
            while left <= len(nums)-1 and right <= len(nums)-1 and left <= right:
                

                # right - left(is non zero) >= target
                if left > 0 and prefix[right+1]-prefix[left] >= target :
                    #append to dec que
                    while dcrsngQue and dcrsngQue[-1] > right-left : 
                        dcrsngQue.pop() 
                    dcrsngQue.append(right-left)

                    # progress pointers ahead
                    if left != right:
                        left += 1
                    else:
                        left += 1
                        right += 1


                # right - left(is zero) >= target
                elif left == 0 and prefix[right+1] >= target:
                    #append to dec que
                    while dcrsngQue and dcrsngQue[-1] > right-left : 
                        dcrsngQue.pop() 
                    dcrsngQue.append((right-left))

                    # progress pointers ahead
                    if left != right:
                        left += 1
                    else:
                        left += 1
                        right += 1


                # when L == R and that element is >= target 
                elif left == right and prefix[right] - prefix[left-1] >= target:
                    return 1
                

                elif left == right == len(nums)-1 :
                    if prefix[right] - prefix[left-1] >= target:
                        while dcrsngQue and dcrsngQue[-1] > 1 : 
                            dcrsngQue.pop() 
                        dcrsngQue.append(1)
                        break

                    else:
                        break


                elif prefix[right+1] - prefix[left] < target:
                    if right != len(nums)-1:
                        right += 1
                    elif left != len(nums)-1:
                        left += 1
                        
                

            if dcrsngQue  :
                val = dcrsngQue[0] + 1
                return val
            else:
                return 0