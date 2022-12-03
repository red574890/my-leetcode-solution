class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
    
        
        def solve(a,b):
            tmp1 = []
            tmp2 = []

            for i in range(len(a)):
                tmp1.append(int(a[i]))

            for i in range(len(b)):
                tmp2.append(int(b[i]))

            for i in range(len(b)):
                tmp1[len(a)-1-i] = tmp1[len(a)-1-i] + tmp2[len(b)-1-i]
            
            
            for i in range(0,len(tmp1)):
                if(tmp1[len(tmp1)-1-i] >= 2):
                    if(len(tmp1)-1-i>0):
                        
                        tmp1[len(tmp1)-1-i-1]+= int(tmp1[len(tmp1)-1-i]/2)
                        tmp1[len(tmp1)-1-i] = tmp1[len(tmp1)-1-i] % 2
                    else:

                        lastn = tmp1[len(tmp1)-1-i]
                        while(lastn>=2):
       
                            tmp1.insert(0,int(lastn/2))
                            tmp1[1] = lastn  % 2
                            lastn = int(lastn/2)
                
            res = ''.join(str(e) for e in tmp1)
                
            return res
        
        
        if(len(a)>len(b)):
            res = solve(a,b)
        else:
            res = solve(b,a)
            
        return res
