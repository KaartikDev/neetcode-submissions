class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        i = 0
        j = 1

        curr = nums[i] + nums[j]

        for i in range(len(nums)):
            for j in range(len(nums)):
                curr = nums[i] + nums[j]
                if curr == target and i != j:
                    small = min(i,j)
                    big = max(i,j)
                    return [small,big]

        #THIS DOESNT WORK BECAUSE NUMS IS NOT SORTED
        # #implment a 2 pointer greedy algo(move pointert that gets sum closer)

        # i = 0
        # j = len(nums) - 1
        # currSum = nums[i] + nums[j]

        # while i < j and currSum != target:
        #     print(currSum, i, j)
        #     if currSum > target: #move the pointer pointing to larger element to decrease sum
        #         if nums[i] > nums[j]:
        #             i+=1  #element at i is larger
        #         else:
        #             j-=1 #element at j is larger
        #     else: #move pointer pointing to smaller obj element to increase sum
        #         if nums[i] < nums[j]:
        #             i+=1 #element at i is smaller
        #         else:
        #             j-=1 #element at j is smaller
            
        #     if i < j: #list bounds gaurd
        #         currSum = nums[i] + nums[j]
        
        # print(currSum, i, j)
        # return [i,j]            
