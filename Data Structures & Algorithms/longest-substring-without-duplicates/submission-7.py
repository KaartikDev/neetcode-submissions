class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "": #empty str gaurd
            return 0
        l = 0
        r = 1
        maxSize = r - l
        seen = set(s[l])

        while r < len(s):

            currChar = s[r]
            while currChar in seen and l < r:
                # print(seen, l, r)
                seen.remove(s[l])
                l+=1
            else:
                seen.add(currChar)
            
            r+=1
            maxSize = max(maxSize, r - l)
            # print("curr max size: ", maxSize, seen)
        

        return maxSize
