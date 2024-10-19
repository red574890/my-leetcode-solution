class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        def DFS(path,remain):

            if(len(remain) == 0):
                if(path not in res):
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
