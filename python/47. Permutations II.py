class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def DFS(path,remain):

            if(len(remain) == 0):
      
                res.append(path)
                return 
            else:
                used = set()
                for i in range(len(remain)):
                    
                    tmp = remain.copy()
                    current = tmp.pop(i)
                    if(current in used):
                        continue

                    
                    path_tmp = path.copy()
                    
                    used.add(current)
                    path_tmp.append(current)
                    DFS(path_tmp,tmp)
            
 
        DFS([],nums)

        return res
