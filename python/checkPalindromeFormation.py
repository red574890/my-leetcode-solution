class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        def check(a1,b1):
            n = 0
            z = len(a1)-1

            while(n<z):
                if(a1[n] == b1[z]):
                    n+=1
                    z-=1
                else:
                    s1 = a1[n:z+1]
                    s2 = b1[n:z+1]
            
                    return s1==s1[::-1] or s2 == s2[::-1]
            return True

        return check(a,b) or check(b,a)
