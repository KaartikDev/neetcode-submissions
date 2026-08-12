class Solution:
    def isPalindrome(self, x: int) -> bool:
        # return str(x) == str(x)[::-1]
        if x < 0:
            return False
        
        rev = 0
        copyX = x
        while copyX > 0:
            # print("d")
            lastDigit = copyX%10
            rev = rev * 10 + lastDigit
            copyX = copyX//10
        
        return x == rev
        

