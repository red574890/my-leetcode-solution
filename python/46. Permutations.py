class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        
        def tree(pick,remain,target):
            if(len(remain)==0):
                target.append(pick)
                res.append(target)
                return 
            else:
                target.append(pick)
                for i in range(0,len(remain)):
                    tmp_remain = remain.copy()
                    next_pick = tmp_remain.pop(i)
                    tree(next_pick,tmp_remain,target.copy())

                   
            
            
       
        for i in range(0,len(nums)):

            tmp_nums = nums.copy()
            next_pick = tmp_nums.pop(i)
            tree(next_pick,tmp_nums,[])
            

        return res
                
