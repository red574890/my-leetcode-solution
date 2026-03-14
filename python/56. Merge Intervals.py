class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])

        
        def merge_intervals(index, res):
      
            if(index == len(res)-1):
                return 
            
            if(res[index][1]>=res[index+1][0]):
     
                tmp = res[index]+res[index+1]
                tmp1 = [min(tmp),max(tmp)]
      
                res[index] = tmp1

                res.pop(index+1)

                merge_intervals(index, res)
            else:
                merge_intervals(index+1, res)
        
        merge_intervals(0, intervals)

        return intervals
          
