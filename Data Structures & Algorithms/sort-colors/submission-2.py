class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        l,r = 0,len(nums)-1
        
        #everthing before left is a 0
        #everything after right is a 2

        curr = 0
        while curr <= r: #we can stop process once at rigth cuz every thing after garunteed to be 2
            
            if nums[curr] == 0: #swap this 0 with the left value, move both left and curr forward
                temp = nums[curr]
                nums[curr] = nums[l]
                nums[l] = temp
                l+=1
                curr+=1
            elif nums[curr] == 2: #swap this 2 with the right value, move right backward and curr alone
                temp = nums[curr]
                nums[curr] = nums[r]
                nums[r] = temp
                r-=1
            else:
                curr+=1