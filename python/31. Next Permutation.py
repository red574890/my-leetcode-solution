class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def compare(a,b):
            for i in range(len(a)):
                if(a[i]<b[i]):
                    return True
                elif(a[i]>b[i]):
                    return False
                else:
                    continue
            return True
                    
        def switch(a,i,j):
            numbers = a.copy()
            temp=numbers[i]
            numbers[i]=numbers[j]
            numbers[j]=temp
            return numbers
        
        n=len(nums)
        first_loc=-1
        for i in range(0,n-1):

            if(nums[n-1-i]  >  nums[n-2-i]):
                first_loc=n-2-i
                break
       
        if(first_loc>=0):
            gap=1000000
            for i in range(first_loc+1,len(nums)):
                if(nums[i]>nums[first_loc]):
                    if(nums[i]-nums[first_loc]<gap):
                        gap=nums[i]-nums[first_loc]
                        second_loc=i
            
            new_nums=switch(nums,first_loc,second_loc)
            tail=new_nums[first_loc+1:]
            tail=sorted(tail,reverse=False)
            new_nums=new_nums[0:first_loc+1]+tail
            
            
            for i in range(len(new_nums)):
                nums[i]=new_nums[i]
        else:
            new_nums=sorted(nums,reverse=False)
            for i in range(len(new_nums)):
                nums[i]=new_nums[i]
        
        
            
                
        

        
        
        
     


            
            
            
            
