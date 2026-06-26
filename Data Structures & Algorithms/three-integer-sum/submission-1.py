class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        ansSet = set()

        for i in range(len(nums)):
            indexHash = {}

            x1 = nums[i]

            for j in range(len(nums)):
                if j == i: #skip when equal to each other
                    continue
                
                x2 = nums[j]

                complement = -x1 - x2 #complement is x3 as --> x1+x2+x3 = 0

                if complement in indexHash and indexHash[complement] != j and indexHash[complement] != i:
                    temp = [x1,x2,complement]
                    temp.sort()
                    
                    ansSet.add(tuple(temp))
                
                if x2 not in indexHash:
                    indexHash[x2] = j
            
        # print(ansSet)

        ansList = []

        for key in ansSet:
            ansList.append(list(key))
        return ansList
                
                
