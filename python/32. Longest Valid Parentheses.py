class Solution:
    def longestValidParentheses(self, s: str) -> int:
        
        if(s==""):
            return(0)
        
        Number=[]
        for i in range(len(s)):
            if(s[i]=="("):
                Number.append(1)
            else:
                Number.append(-1)
        left=0
        right=len(Number)-1
        
        while(Number[left]!=1 and right>left):
            left+=1
            
        while(Number[right]!=-1 and right>left):
            right-=1
        
        if(left>=right):
            return(0)
        
        #check where to start
        sum_of_left=abs(sum(Number[left:int((right+left/2))]))
        sum_of_right=abs(sum(Number[int((right+left/2)):right]))
        res=0
        
        #------
        if(sum_of_left>sum_of_right):
            while(left<right):
            
                while(Number[right]==1 and left<right):
                    right-=1
            
                total=0
                i=right
                temp=0
                temprange=0
            
                while(left<=i):
                    if(total==0 and Number[i]==1):
                        right=i+1
                        break
                    
                    total+=Number[i]
                    temp+=1
                    if(total==0):
                        temprange+=temp
                        temp=0
                    
                    i-=1
            
                if(temprange>res):
                    res=temprange
            
                right-=1
                    
            return(res)
        else:
            while(left<right):
            
                while(Number[left]==-1 and left<right):
                    left+=1
            
                total=0
                i=left
                temp=0
                temprange=0
            
                while(i<=right):
                    if(total==0 and Number[i]==-1):
                        left=i-1
                        break
                    total+=Number[i]
                    temp+=1
                    if(total==0):
                        temprange+=temp
                        temp=0
                    
                    i+=1
            
                if(temprange>res):
                    res=temprange
            
                left+=1
                    
            return(res)
        
        
        
        #------
        
        
