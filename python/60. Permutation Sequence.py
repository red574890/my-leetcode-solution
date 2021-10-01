class Solution:
    
    
    def getPermutation(self, n: int, k: int) -> str:
        
        def factorial(n):
            res=1   
            for i in range(1,n+1):
                res*=i  
            return res
        
        res=[0]*n
        remind = list(range(1,n+1))
        loc=0


        while(n>0):
            
            block=factorial(n-1) 

            if(block==k and k==1):
                position=0
            else:
                if(k%block==0):
                    position=int(k/block)-1
                else:
                    position=int(k/block)
      
                k=k-position*block
  
            res[loc]=remind.pop(position)
            
     
            
            
            
            loc+=1
            n-=1
        result="" 
        for i in res:
            result+=str(i)
            
        return result
