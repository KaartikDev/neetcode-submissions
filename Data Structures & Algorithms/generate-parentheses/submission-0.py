class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        st = []
        res = []

        def generateStr(openParen,closeParen):
            if openParen == closeParen and closeParen == n:
                res.append("".join(st))
                return
            
            if openParen < n:
                st.append('(')
                generateStr(openParen+1,closeParen)
                st.pop()
            
            if closeParen < openParen:
                st.append(')')
                generateStr(openParen,closeParen+1)
                st.pop()
                
        generateStr(0,0)
        return res
            


    


