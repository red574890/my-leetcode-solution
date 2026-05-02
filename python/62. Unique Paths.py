class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # create a grid
        grid = []
        for i in range(0,m):
            tmp = []
            for j in range(0,n):
                if(j == 0 or i == 0):
                    tmp.append(1)
                else:
                    tmp.append(grid[i-1][j]+tmp[j-1])
            
            grid.append(tmp)
        return grid[m-1][n-1]
