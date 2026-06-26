class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        indexStack = []
        results = [0] * len(temperatures)
        for i in range(len(temperatures)-1,-1,-1):
            if i == len(temperatures)-1:
                indexStack.append(i)
            else:
                # print(indexStack)
                while indexStack and temperatures[i] >= temperatures[indexStack[-1]]:
                    indexStack.pop()
                if indexStack:
                    results[i] = indexStack[-1] - i
                indexStack.append(i)
        return results

