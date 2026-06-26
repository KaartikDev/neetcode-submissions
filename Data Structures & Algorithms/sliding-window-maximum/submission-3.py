import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ansArr = []
        l = 0
        r = k-1
        #idea: maiantin a widnow max heap. At each step, pop left append right peek at top to store. 
        #note: as heapq are min heaps, we can negate inputs before push and negate again when pop to emulate max heap

        # print(l,r,nums[l:r+1])
        window = nums[l:r+1]
        monoWindowQueue = deque()
        # heapq.heapify(windowHeap)

        for n in window:
            if len(monoWindowQueue) == 0:
                monoWindowQueue.appendleft(n)
            else:
                while len(monoWindowQueue) > 0 and n > monoWindowQueue[0]:
                    monoWindowQueue.popleft()
                monoWindowQueue.appendleft(n)
                

                
        
        ansArr.append(monoWindowQueue[-1])
        # print(l,r,monoWindowQueue,ansArr[-1])
        # r+=1 
        while r < len(nums)-1:
            r+=1
            while len(monoWindowQueue) > 0 and nums[r] > monoWindowQueue[0]:
                    monoWindowQueue.popleft()
            #if the top is the same as what we are losing then we need to get rid of it
            if len(monoWindowQueue) > 0 and nums[l] == monoWindowQueue[-1]:
                monoWindowQueue.pop()
            l+=1
            
            monoWindowQueue.appendleft(nums[r])
            ansArr.append(monoWindowQueue[-1])
            # print(l,r,monoWindowQueue,ansArr[-1])
        
        return ansArr
        # while r < len(nums):
            
