class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        
        for i in range(numRows):
            if(i == 0):
                res.append([1])
            
            elif(i == 1):
                res.append([1,1])
            else:
                prev = res[len(res)-1]
                prev = [0]+prev
                prev = prev + [0]
                tmp = []
                for j in range(len(prev)-1):
                    tmp.append(prev[j]+prev[j+1])
                
                res.append(tmp)
        
        return res

