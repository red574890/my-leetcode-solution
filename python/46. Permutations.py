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
                


##------------#   20241019 Ray H new code

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def DFS(path,remain):

            if(len(remain) == 0):
                res.append(path)
                return 
            else:
                for i in range(len(remain)):
                    tmp = remain.copy()
                    path_tmp = path.copy()
                    current = tmp.pop(i)
                    path_tmp.append(current)
                    DFS(path_tmp,tmp)
            
 
        DFS([],nums)

        return res
