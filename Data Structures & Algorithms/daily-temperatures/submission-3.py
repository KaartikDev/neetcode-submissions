class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        st = [] #[index, temp]
        #st is always decreasing

        res = [0] *len(temperatures)

        for i in range(len(temperatures)):
            while st and temperatures[i] > st[-1][1]:
                stackInd,stackTemp = st.pop()
                res[stackInd] = i - stackInd
            st.append([i,temperatures[i]])
        
        return res
