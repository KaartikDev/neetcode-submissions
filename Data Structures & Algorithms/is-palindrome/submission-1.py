class Solution:
    def isPalindrome(self, s: str) -> bool:
        r = len(s)-1
        l = 0

        while r >= l:
            while r >= 0 and not s[r].isalnum():
                r-=1
            while l < len(s) and not s[l].isalnum():
                l+=1
            
            if r >= 0 and l < len(s) and s[r].lower() != s[l].lower():
                print(s[l],s[r])
                return False
            
            r-=1
            l+=1
        
        return True
        