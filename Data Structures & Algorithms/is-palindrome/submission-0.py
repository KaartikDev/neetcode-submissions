class Solution:
    def isPalindrome(self, s: str) -> bool:
        #two pointer method
        i = 0
        j = len(s) -1

        while i < j: #two pointers
            
            while i < j and not s[i].isalnum(): #move pointer if pointa  non alphanumer
                i+=1
            while i < j and not s[j].isalnum():
                j-=1
        
            if i < j and s[i].lower() != s[j].lower(): #check if the two alpha numeric charcters are same lowercase
                
                return False
            i+=1 #move pointers in
            j-=1
        
        return True