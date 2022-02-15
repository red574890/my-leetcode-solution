class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # find the shortest one first
        length=100000
        loc=0
        for i in range(len(strs)):
            if(len(strs[i])<length):
                length=len(strs[i])
                loc=i
        
        shortest=strs[loc]
        res=""
        n=0
        
        while(length>=n):
            alltrue=True
            for i in strs:
                if(shortest[0:n] != i[0:n]):
                    alltrue=False
                    break
            if(alltrue):
                res=shortest[0:n]
            n+=1
        return res
