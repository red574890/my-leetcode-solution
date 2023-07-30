class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        if(n == 0):
            return 1
        if(n < 0):
            x = (1/x)
            n *= -1

        if(x == 1):
            return 1
        elif(x == -1):
            if(n%2 ==1):
                return -1
            else:
                return 1
        
        org = x
        times = 1
        while(times < n):
  
            if(times*2 <= n):
                times*=2
                x = x*x
            else:
                if(org < 1 and x== 0):
                    break

                times+=1
                x *= org
        

        return x
