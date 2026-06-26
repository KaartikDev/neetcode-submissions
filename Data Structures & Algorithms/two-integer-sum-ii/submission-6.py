class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}
        temp = 0

        for i in range(len(numbers)):
            complement = target - numbers[i]

            if complement in seen:
                #i > complement is gaurnteed as we only add nums after seeing  
                return [seen[complement]+1,i+1]
            else:
                seen[numbers[i]] = i
            
            # print(seen,numbers[i])
        
        # bad input gaurd
        return [-1,-1]