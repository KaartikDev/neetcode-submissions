import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ansArr = []
        l = 0
        r = k

        # print(l,r,nums[l:r+1])
        window = nums[l:r]
        monoWindowQueue = deque()

        for i in range(k):
            if not monoWindowQueue:
                monoWindowQueue.appendleft(nums[i])
            else:
                while len(monoWindowQueue) > 0 and nums[i] > monoWindowQueue[0]:
                    monoWindowQueue.popleft()
                monoWindowQueue.appendleft(nums[i])
                

                
        
        ansArr.append(monoWindowQueue[-1])
        while r < len(nums):

            if len(monoWindowQueue) > 0 and nums[l] == monoWindowQueue[-1]:
                monoWindowQueue.pop()
            l+=1

            while len(monoWindowQueue) > 0 and nums[r] > monoWindowQueue[0]:
                monoWindowQueue.popleft()
            
            
            
            monoWindowQueue.appendleft(nums[r])
            ansArr.append(monoWindowQueue[-1])
            # print(l,r,monoWindowQueue,ansArr[-1])
            r+=1
        
        return ansArr
        # while r < len(nums):
            
