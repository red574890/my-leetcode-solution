class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        all_zeros = all(all(item == 0 for item in sublist) for sublist in triangle)

        if(all_zeros):
            return 0
        
        length = len(triangle)
        memo = {}

        def find_min(index,layer):

            if(layer == length-1):
                return triangle[layer][index]
            
            if(index >= len(triangle[layer]) ):
                return float('inf')
            
            if (index, layer) in memo:
                return memo[(index, layer)]
            
            cur = triangle[layer][index]
           
            
            memo[(index, layer)] = cur+ min(find_min(index,layer+1), find_min(index+1,layer+1))

            return memo[(index, layer)]

        
        return find_min(0,0)
