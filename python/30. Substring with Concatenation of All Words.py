class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        
        substrlength = len(words[0])
        
        total_length = len(words)*substrlength
        
        
        res = []
        visited_wrong = set()
        visited_correct = set()
        for i in range(0,len(s)-total_length+1):
            cand_str = s[i:i+total_length]
            new_words = words.copy()
            n=0
            
            if(cand_str in visited_wrong):
                continue
            elif(cand_str in visited_correct):
                res.append(i)
                continue

            
      
            for j in range(len(words)):
                tmp = cand_str[n:n+substrlength]
                if(tmp in new_words):
                    new_words.remove(tmp)
                    
                n+=substrlength
                
            if(len(new_words)==0):
                res.append(i)
                visited_correct.add(cand_str)
            else:
                visited_wrong.add(cand_str)
                
        return(res)
