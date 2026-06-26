class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        #the key idea is to have a stakc which has tuples of the temperature and index. 
        # When we get to a new value, while it is larger than top of stak, pop the stack.
        # This creates a "monotonic decreasing stack" (not rly cuz equal value okay ut basically)
        # Storing the orignal index in the stakc allows to compute difference to get days
        st = [] #hold elements like [index, temp]
        res = [0] * len(temperatures)
        for i, temp in enumerate(temperatures):
            while st and temp > st[-1][1]:
                stackInd, stackTemp = st.pop()
                res[stackInd] = i - stackInd
            st.append([i,temp])
        return res