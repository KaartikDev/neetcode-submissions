class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        
        if not nums:
            return 0
        if len(nums) == 1:
            return 1 if nums[0] == k else 0
        
        

        #prefix[-1] = 0 (So we can inlude el zero)
        #note j < i

        #prefix[i] = sum(nums[0]+nums[1]+...+nums[i])
        #prefix[j] = sum(nums[0]+nums[1]+...+nums[j])

        #sum(nums[j+1]+nums[j+2]+...+nums[i]) = prefix[i]-prefix[j] = k

        #prefix[i]-k = prefix[j] 

        #Basicaly, if currPrefix-k was seen before we can make a subarray that sums to k
        #We should use a hashmap to count how many times a prefix sum is seen and inc res by that amount

        prefix = 0
        res = 0
        prefixCounts = {0:1} #prefix[-1] = 0
        
        for n in nums:
            prefix+=n
            pastNeededPrefix = prefix-k 
            if pastNeededPrefix in prefixCounts:
                res+=prefixCounts[pastNeededPrefix]
            prefixCounts[prefix] = prefixCounts.get(prefix,0)+1
        return res




        
        #brute force: sum subarray from 1 to len(n) and count+1 if sum(subarr) == k
        #O(n^2) --> O(n) sub arrays and O(n) to sum each
        #cuz of constraints we get max 2^10^8 iters; 100 mill iter isnt crazy but no idieal fs

            
             