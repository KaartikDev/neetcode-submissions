class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        

        nums.sort()
        ans = []
        i = 0
        
        while i < len(nums) - 2: #need at leats two numbers for this to work
            x1 = nums[i]

            if i >= 1 and nums[i] == nums[i-1]: #dont reuse starting values
                i+=1
                continue
            
            l = i +1
            r = len(nums)-1

            while l < r:
                curr = nums[l] + nums[r] + x1
                if curr == 0:
                    ans.append([nums[i],nums[l],nums[r]])
                    #now to ensure the second value is also not resused
                    l+=1
                    while l<r and nums[l] == nums[l-1]:
                        l+=1
                elif curr > 0:
                    r-=1
                elif curr < 0:
                    l+=1
            
            i+=1

        return ans










        # ansSet = set()

        # for i in range(len(nums)):
        #     indexHash = {}

        #     x1 = nums[i]

        #     for j in range(i+1,len(nums)):
                
        #         x2 = nums[j]

        #         complement = -x1 - x2 #complement is x3 as --> x1+x2+x3 = 0

        #         if complement in indexHash and indexHash[complement] != j and indexHash[complement] != i:
        #             temp = [x1,x2,complement] 
        #             temp.sort() #sort the arr so  duplicates do not get stored
                    
        #             ansSet.add(tuple(temp))
                
        #         if x2 not in indexHash:
        #             indexHash[x2] = j
            
        # # print(ansSet)

        # ansList = []

        # for key in ansSet:
        #     ansList.append(list(key))
        # return ansList
                
                
