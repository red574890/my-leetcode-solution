class Solution:
    def canJump(self, nums: List[int]) -> bool:
        for i in range(len(nums)):

            if(nums[i]>0):
                continue
            elif(i+1 < len(nums)-1):
                if(nums[i+1] == 0):
                    continue
    
            if(nums[i] == 0 and i != len(nums)-1):
                jump = 0
                for j in range(0,i):
                    if(nums[j]+j > i):
                        jump = 1
                        break

                if(jump == 1):
                    continue
                else:
                    return False

        return True
