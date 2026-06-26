class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # if len(s) < 2: #empty or single char gaurd
        #     return len(s)
        
        # currSubStr = deque()
        # currSubStr.append(s[0])  #this queue is the sliding window
        # p = 1 #pointer
        # maxLen = 1

        # while p < len(s):

        #     while s[p] in currSubStr: #keep removing characters from left till current no longer exists
        #         currSubStr.popleft()
            
            
        #     currSubStr.append(s[p]) #add current
        #     maxLen = max(maxLen, len(currSubStr)) #check if new record
        #     p+=1 #move on
            
        # return maxLen

        charSet = set()
        l = 0
        result = 0
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l+=1

            charSet.add(s[r])
            result = max(result,r-l+1)
        
        return result
            

        
