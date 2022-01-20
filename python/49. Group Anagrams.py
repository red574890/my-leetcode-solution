class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=[]
        strs = sorted(strs, key=len)


        while(len(strs)>0):

            
            temp=[]
            word=strs.pop(0)


            temp.append(word)
            word=sorted(word)
            pop_list=[]

            for i in range(len(strs)):

                if(len(strs[i])!=len(word)):
                    break
               
                
                elif(sorted(strs[i])==word):
                    pop_list.append(strs[i])
                    temp.append(strs[i])
                    
            
            for i in pop_list:
                strs.remove(i)
                
            
            
                
                
            
            res.append(temp)
        
        return res
                    
            
