class Solution:
    def isPalindrome(self, x: int) -> bool:
        res=str(x)
        for i in range(0,len(res)):
            if(res[i]!=res[len(res)-1-i]):
                return False
        return True
        
