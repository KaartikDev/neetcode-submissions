class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        i = len(temperatures)-1
        st = [] # pair: [temp, index] The key
        res = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            while st and temp > st[-1][0]:
                stackT, stackInd = st.pop()
                res[stackInd] = i - stackInd
            st.append([temp,i])
        return res