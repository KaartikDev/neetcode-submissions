class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if len(s) < 2: #empty or single char gaurd
            return len(s)
        
        currSubStr = deque()
        l = 0
        r = 1
        currSubStr.append(s[0])
        maxLen = 1

        while r < len(s):
            

            while s[r] in currSubStr:
                currSubStr.popleft()
            
            else:
                currSubStr.append(s[r])
                maxLen = max(maxLen, len(currSubStr))
                r+=1
            
        return maxLen
