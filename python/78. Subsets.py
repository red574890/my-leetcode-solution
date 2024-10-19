class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []


        def backtrack(loc,path):
            res.append(path)

            for i in range(loc,len(nums)):
                backtrack(i+1,path+[nums[i]])
            
        
        backtrack(0,[])
        
 
        return res

        
                 

            
            







        
