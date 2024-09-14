class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        
        n = 0
        def swap(i,j):
            tmp = nums[j]
            nums[j] = nums[i]
            nums[i] = tmp

        while(n<len(nums)-1):    
          
            if(nums[n]>nums[n+1]):
                swap(n,n+1)
                if(n==0):
                    pass
                else:
                    n-=1
            else:
                n+=1
