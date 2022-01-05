class Solution:
    def trap(self, height: List[int]) -> int:
        secondhigh=0
        water=0
        i=0
        j=0

        while(i<len(height)-1):
            leftskew=False
            if(height[i]<height[i+1] ):
                i+=1
                continue
            else:
                
                for j in range(i+1,len(height)):
                    if(height[j]>=height[i]):
                        leftskew=True
                        break
        
                if(leftskew):
                    for z in range(i+1,j):
                        if(height[z]<height[i]):
                            water+=height[i]-height[z]
                    i=j
                else:
                    second=0
                    location=0
                    for z in range(i+1,len(height)):
                        if(height[z]>=second):
                            second=height[z]
                            location=z
                    
                    for z in range(i+1,location):
                        if(height[z]<height[location]):
                            water+=height[location]-height[z]
                            
                    i=location
                                            
                
                    
            
    
        return water
                
                
                
                
                

            
            
            
        
