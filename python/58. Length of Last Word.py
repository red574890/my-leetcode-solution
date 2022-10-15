class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        tmp = s.split(" ")
        for i in range(len(tmp)):
            if(tmp[len(tmp)-i-1] == ''):
                pass
            else:
                return len(tmp[len(tmp)-i-1])
        
