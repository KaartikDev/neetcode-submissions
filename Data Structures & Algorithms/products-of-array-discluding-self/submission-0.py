class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        suffixMult = []
        currSuffix = 1
        for i in range(len(nums)-1,-1,-1):
            if i == len(nums)-1:
                suffixMult.append(currSuffix)
            else:
                currSuffix = currSuffix*nums[i+1] #multipley with elemnt to right
                suffixMult.append(currSuffix)
        
        suffixMult.reverse()
        print(suffixMult)

        prefixSuffix  = 1

        for i in range(len(nums)):
            if i == 0:
                pass
            else:
                prefixSuffix = prefixSuffix * nums[i-1]
                suffixMult[i] = suffixMult[i] * prefixSuffix
        
        return suffixMult
        #O(N) time complexity (suffix multiplications, list reversal, final calc)
        #O(N) space complexity (O(1) if you dont count return arr
