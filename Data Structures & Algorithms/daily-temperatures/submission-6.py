class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        st = []

        for i,t in enumerate(temperatures):
            # print(st)
            while st and st[-1][0] < t:
                oldT,oldIndex = st.pop()
                res[oldIndex] = i - oldIndex

            
            st.append((t,i))
        return res
            
