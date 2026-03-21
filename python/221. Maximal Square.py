class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        max_side = 0
        DP = []

        max_side = 0
        for i in range(0,len(matrix)):
            tmp = []
            for j in range(0,len(matrix[0])):
                tmp.append(int(matrix[i][j]))
                max_side = max(max_side,int(matrix[i][j]))
            DP.append(tmp)

        
        for i in range(0,len(matrix)):
            for j in range(0,len(matrix[0])):
                if(i==0 or j == 0):
                    continue

                if(DP[i][j] == 0):
                    continue
                
                if(int(matrix[i-1][j]) == 0 and int(matrix[i][j-1]) == 0 and int(matrix[i-1][j-1]) == 0):
                    continue
                else:
                    DP[i][j] =  min(DP[i-1][j], DP[i][j-1], DP[i-1][j-1]) + 1
                max_side = max(max_side,DP[i][j])
    
         

        return max_side*max_side
