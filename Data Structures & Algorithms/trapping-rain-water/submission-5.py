class Solution:
    def trap(self, height: List[int]) -> int:


        maxRight = 0
        rightMax = [0] * len(height)
        for i in range(len(height)-1, -1, -1):
            maxRight = max(height[i],maxRight)

            if i == len(height)-1:
                pass
            else:
                rightMax[i] = maxRight
        
        print(rightMax)

        leftMax = 0
        sumWater = 0

        for i in range(len(height)):
            leftMax = max(leftMax,height[i])
            
            if i == 0:
                pass
            else:
                currWater = min(leftMax,rightMax[i]) - height[i]
                if currWater > 0:
                    sumWater += currWater
        
        return sumWater
