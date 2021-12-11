class Solution:
    def maxArea(self, height: List[int]) -> int:
        
       
        left=0
        right=len(height)-1
        maxsize=0
        while(left<right):
            if(height[left]>height[right]):
                if(height[right]*abs(right-left)>maxsize):
                    maxsize=height[right]*abs(right-left)
                right-=1
                
            else:
                if(height[left]*abs(right-left)>maxsize):
                    maxsize=height[left]*abs(right-left)
                left+=1
            
        return maxsize
