class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = sorted(nums)
        for n in range(0,len(nums)):
            if(nums[n]>0):
                break
        j=1
        while(j<nums[len(nums)-1]):
            if(n+1<len(nums)):
                if(nums[n+1] == nums[n] ):
                    n+=1
                    continue
                else:
                    pass
            if(j==nums[n]):
                n+=1
                j+=1
            else:
                return j
        
        if(nums[len(nums)-1]>0):
            return nums[len(nums)-1]+1
        else:
            return 1
                    
