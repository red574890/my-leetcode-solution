class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s)!=len(t)):
            return False
        else:
            s=sorted(list(s))
            t=sorted(list(t))
            n=len(s)
            for i in range(0,n):
                if(s[i]!=t[i]):
                    return False
            return True
