class Solution:
    def trap(self, height: List[int]) -> int:
        

        #prefix map and suffix map
        # water[i] = min(prefixMax[i],suffix[max]) - height[i]

        #prefix max
        n = len(height)
        maxSeen = 0
        prefixMax = [0] * n
        for i in range(1,n):
            maxSeen = max(height[i-1],maxSeen)
            prefixMax[i] = maxSeen
        # print(prefixMax)

        #suffix max
        maxSeen = 0
        suffixMax = [0] * n
        for i in range(n-2,-1,-1):
            maxSeen = max(maxSeen,height[i+1])
            suffixMax[i] = maxSeen
        # print(suffixMax)

        #calc
        netWater = 0
        for i in range(n):
            trappedWater = max(0, min(prefixMax[i],suffixMax[i])-height[i])
            netWater+=trappedWater
        return netWater




