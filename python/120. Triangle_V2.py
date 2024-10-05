class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n_layer = len(triangle)
        for i in range(n_layer-2,-1,-1):

            for j in range(len(triangle[i+1])-1):
  
                triangle[i][j] += min(triangle[i+1][j] , triangle[i+1][j+1])


        return triangle[0][0]
