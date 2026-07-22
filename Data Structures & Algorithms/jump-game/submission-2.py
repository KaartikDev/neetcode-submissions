class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums: #trivial case
            return True
        if nums[0] == 0: #only one element case
            return len(nums) == 1
        
        jumpsLeft = nums[0]
        i = 1

        while i < len(nums) and jumpsLeft > 0:
            #we take the jumps at pos i if its greater than jumps left
            print("ind=",i,"jumpLeft=",jumpsLeft,"nums[i]=",nums[i])
            jumpsLeft-=1
            if nums[i] >= jumpsLeft:
                jumpsLeft = nums[i]
            i+=1
        
        return i == len(nums)
        

