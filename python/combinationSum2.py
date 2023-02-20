class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        if(sum(candidates) == target):
            return [candidates]
        elif(sum(candidates) < target):
            return []

        if(max(candidates) != min(candidates)):
            candidates = sorted(candidates)

        res = []
        current = []
    

        def petition(current_list,pos,cand,target):
            
            prev = -1

            for i in range(pos,len(cand)):
                
                if(cand[i] == prev):
                    continue

                if(cand[i]> target):
                    break
      
                elif(cand[i] == target):
                     current = current_list.copy()
                     current.append(cand[i])
                     if(current not in res ):
                         res.append(current)

                elif(cand[i] < target):
                    current = current_list.copy()
                    current.append(cand[i])
                    prev = cand[i]
                    petition(current, i+1 ,cand,target - cand[i])
 
        

        petition(current,0,candidates,target)

        return res
