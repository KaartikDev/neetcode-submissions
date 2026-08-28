class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        #make the shorter string A
        #make the longer string B
        #start with all of A, see if it cleanly divides B and check if replicaitng A that many times works
        #keep cutting letters till none left

        gcd = math.gcd(len(str1),len(str2))
        prefix = str1[:gcd]

        check1 = ""
        while len(check1) < len(str1):
            check1+=prefix
        if check1 != str1:
            return ""
        

        check2 = ""
        while len(check2) < len(str2):
            check2+=prefix
        if check2 != str2:
            return ""
        

        return prefix