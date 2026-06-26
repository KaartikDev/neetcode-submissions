class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        #Goal: Figure out right procuts
        # at pos i its producet of everything to right execpt forself
        # we need to save curr value to multiply for next iter

        rightProducts = nums.copy()
        past = nums[len(nums)-1]
        for i in range(len(nums)-2,-1,-1):
            running = rightProducts[i]*past
            if i == len(nums)-2:
                rightProducts[i] = rightProducts[i+1]
            else:
                rightProducts[i] = past

            past = running
            # print(running, past, rightProducts)
        # print('\n')
        # #goal now multiple left values starting from second el not inclduing curr?
        # past = nums[0]
        # for i in range(1,len(nums)):
        #     running = running*past
        #     if i != 0:
        #         rightProducts[i] = running*rightProducts[i]
        #     past = running
        #     print(running, past, rightProducts)

        left_running = nums[0]
        
        # output = nums.copy()
        # output[0] = rightProducts[0]
        for i in range(1,len(nums)):
            if i == len(nums)-1:
                rightProducts[i] = left_running #left_running does not inclde curr index 
            else:
                rightProducts[i] = left_running*rightProducts[i] 
            left_running*=nums[i] #running now includes curr index and everything to left


        return rightProducts
        