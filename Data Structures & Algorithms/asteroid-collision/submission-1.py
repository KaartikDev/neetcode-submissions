class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st = []

        for el in asteroids:
            broken = False
            while st and (st[-1] > 0 and el < 0) and not broken:
                absTop = abs(st[-1])
                absEl = abs(el)
                if absEl < absTop:
                    broken = True
                elif absEl == absTop:
                    st.pop()
                    broken = True
                else: #incoming is bigger than prev
                    st.pop()
            
            if not broken:
                st.append(el)
        
        return st
                
