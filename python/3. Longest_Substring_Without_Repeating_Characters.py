class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        times=0
        begin=0
        end=0
        for i in range(0,len(s)):
            j=i+1
            n=0
            while(j<len(s)):
                if(s[j] not in s[i:j]):
                    j+=1
                elif(s[j] in s[i:j]):
                    break
            n=len(s[i:j])
            i=j
            if(n>times):
                times=n
        return times
        
