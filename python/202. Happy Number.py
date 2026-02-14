class Solution:
    def isHappy(self, n: int) -> bool:

        
        check = []
        seen = set()
        while(True):
            n = str(n)
            tmp = list(n)

            n = 0
            for t in tmp:
                n+= int(t)**2
            if(n in seen):
                return False

            if(n==1):
                return True

            check.append(n)
            seen.add(n)
     
 



        
