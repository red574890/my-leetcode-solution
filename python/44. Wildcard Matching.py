class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if(s==p):
            return True
        
        if(s==""):
            s+=" "
        
        S=[]
        s=" "+s
        for i in s:
            S.append(i)
        s=S
        
        p=" "+p
        stack=[]
        first=False
        
        n=0
        
        while (n<len(p)):
            if(p[n]!="*"):
                stack.append(p[n])
                
            if(p[n]=="*"):
                stack.append(p[n])
                while(n<len(p)):
                    if(p[n]=="*"):
                        n+=1
                    else:
                        stack.append(p[n])   
                        break
                
            n+=1
        
        p=stack
      
        M=[]
        #Create Matrix
        for i in range(0,len(s)):
            M.append(len(p)*[False])
        

        #Insert value into Table
        
        for i in range(0,len(s)):
            for j in range(0,len(p)):
                
                if(i==0 and j ==0):
                    M[i][j] = True
                elif(i==0 and j!=0):
                    if(p[j]=="*"):
                        if(M[i][j-1]):
                            M[i][j] = True
                    else:
                        M[i][j] = False
                elif(j==0 and i>0):
                    M[i][j] = False
                
                else:
                    if(s[i]==p[j] or (p[j]=='?' and s[i]!=' ')):
                        if(M[i-1][j-1]==True):
                            M[i][j]=True
                        else:
                            M[i][j]=False
                    elif(s[i]!=p[j] and p[j]!="*"):
                        M[i][j]=False
                        
                    elif(p[j]=="*"):
                        if(M[i-1][j] or M[i][j-1] ):
                            M[i][j]=True
                        else:
                            M[i][j]=False
        return M[len(s)-1][len(p)-1]          
                        
                           
       
