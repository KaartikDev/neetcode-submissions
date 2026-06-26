class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #list is increasing
        #Can use the two pointer trick :)
        i = 0
        j = len(numbers) -1

        curr = 0
        while i<j:
            curr = numbers[i] + numbers[j]
            if curr > target: #need to move bigger pointer
                j-=1
            elif curr < target:
                i+=1
            else:
                break
        return [i+1,j+1] #using 1 index arr so add 1

        