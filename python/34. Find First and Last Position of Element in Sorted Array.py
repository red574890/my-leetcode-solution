class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        if(len(nums)==0):
            return [-1,-1]

        mid = int(len(nums)/2)
        low = 0
        high = len(nums)-1
        

        while(low<high-1):
            if(nums[mid]>target):
                high = mid
                mid = int((high+low)/2)
            elif(nums[mid]<target):
                low = mid
                mid = int((high+low)/2)
            else:
                break

        if(nums[low]==target):
            mid = low
        elif(nums[high] == target):
            mid = high

        if(nums[mid]!=target):
            return[-1,-1]
        
        for high in range(mid,len(nums)):
            if(nums[high]!=target):
                high -=1
                break
        
        for low in range(mid,-1,-1):
            if(nums[low]!=target):
                low+=1
                break
        
        return [low,high]
