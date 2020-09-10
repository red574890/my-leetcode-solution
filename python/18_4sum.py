class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        size=len(nums)
        n3=len(nums)-2
        n2=1
        n1=0
        res=[]
        nums.sort()
        left=2
        right=len(nums)-1
        if(size<4):
            res=[]
        else:
            for i in range(0,size-3):
                if(i!=0 and nums[i]==nums[i-1]):
                    continue
                for j in range(i+1,size-2):
                    if(j!=i+1 and nums[j]==nums[j-1]):
                        continue
                    right=len(nums)-1
                    left=j+1
                    while(right>left):
                        if(nums[i]+nums[j]+nums[left]+nums[right]==target):
                            temp=[nums[i],nums[j],nums[left],nums[right]]
                            temp.sort()
                            res.append(temp)
                            left+=1
                            right-=1
                            while(right>left and nums[left]==nums[left-1]):
                                left+=1
                            while(right>left and nums[right]==nums[right+1]):
                                right-=1
                        elif(nums[i]+nums[j]+nums[left]+nums[right]<target):
                            left+=1
                        elif(nums[i]+nums[j]+nums[left]+nums[right]>target):
                            right-=1
                            
 
        
        return res
