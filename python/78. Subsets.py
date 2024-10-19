class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
       
        length = len(nums)

        res = [[]]

        for i in range(length):

            for j in range(len(res)):
                tmp = res[j]

                sub = tmp.copy()
                sub.append(nums[i])

                res.append(sub)
            
        return res

        
                 

            
            







        
