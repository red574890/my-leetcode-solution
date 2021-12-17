class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        
        
        def combination(number,target,candidates,path,alll):
            path=path.copy()
            path.append(number)
            if(target>sum(path)):

                for i in candidates:
                    combination(i,target,candidates,path,alll)
                return alll
            elif(target==sum(path)):
                path=sorted(path)
                if((path in alll)==False):
                    alll.append(path)
        
        candidates=sorted(candidates)
        
        if(candidates[0]>target):
            return []
        res=[]
        for i in range(0,len(candidates)):
            if(target==candidates[i]):
                res.append([candidates[i]])
                candidates=candidates[0:i]
                break
       
        
        
      
        for i in candidates:
            temp=combination(i,target,candidates,[],[])

            if(temp!=None):
                for j in temp:
                    if((j in res)==False):
                        res.append(j)
            else:
                continue
                
        return res

                
