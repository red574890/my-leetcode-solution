class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        alll=list(range(1,len(isConnected)+1))
        n=len(isConnected)
        for i in range(0,n):
            
            for j in range(0,n):
                if(isConnected[i][j]==1):
                    temp=alll[j]
                    for z in range(0,n):
                        if(alll[z]==temp):
                            alll[z]=i+1
                elif(isConnected[i][j]==0):
                    continue
            print(alll)
        
        return(len(set(alll)))
                
        
                    
