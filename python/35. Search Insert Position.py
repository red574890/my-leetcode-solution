class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        high=len(nums)-1
        
        low=0
        mid=int((high-low)/2)
        if(nums[mid]==target):
            return mid
        
        if(target>nums[high]):
            return(high+1)
        elif(target==nums[high]):
            return(high)
        elif(target<=nums[0]):
            return(0)
        
        # find the closest number
        n=0
        while(high-low>2):
            
            if(nums[mid]>target):
                high=mid
                mid=int(low+(high-low)/2)+1
            
            elif(nums[mid]<target):
                low=mid
                mid=int(low+(high-low)/2)+1
            
            elif(nums[mid]==target):
                return mid
                
   
        for i in range(low,high):
            print(i)
            if(nums[i]<target and nums[i+1]>target):
                return(i+1)
            if(nums[i]==target):
                return(i)
