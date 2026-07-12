class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        #not backtracking as must be contiguous
        #must be non empty

        if len(nums) == 1:
            return nums[0]
        if len(nums) == 0:
            return 0

        def allZero(nums):
            for n in nums:
                if n!=0:
                    return False
            return True
        if allZero(nums):
            return 0
        
        #dp(i) means max subarray of nums[i:]
        # maybe we can take insparation for the palindrom
        #some sort of expand solution

        maxProd = 1
        minProd = 1
        res = max(nums)

        for n in nums:
            if n == 0:
                maxProd,minProd=1,1
                continue
            
            prevMax,prevMin = maxProd,minProd

            maxProd = max(n*prevMax,n*prevMin,n)
            minProd = min(n*prevMax,n*prevMin,n)
            res = max(maxProd,minProd,res)
        return res



