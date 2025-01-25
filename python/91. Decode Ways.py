class Solution:
    def numDecodings(self, s: str) -> int:

        
        code = []
        for i in range(1,27):
            code.append(str(i))
        
        memo = {}  # Dictionary for memoization

        def comb(n):
            

            if(n in memo):
                return memo[n]
            if(n == len(s)):
                return 1
            if(n > len(s)):
                return 0
            
            count = 0

            if(s[n:n+1] in code):
                count += comb(n+1)

            

            if( n + 1 < len(s) and s[n:n+2] in code):
                count += comb(n+2)
                
            memo[n] = count  # Store result in memo
            return count
     
 
 
        return comb(0)
