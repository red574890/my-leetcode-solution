class Solution:
    def climbStairs(self, n: int) -> int:
        numb_of_two=0
        combination=0
        while(n-2>=0):
            n-=2
            numb_of_two+=1
            # factorial
            numerator=factorial(n+numb_of_two)
            denominator=factorial(n)*factorial(numb_of_two)
            combination+=numerator/denominator
        combination+=1
        
        return int(combination)
            
             
            
    def factorial(self,n):
        res=1
        while(n>0):
            res*=n
            n-=1
        return res
        
