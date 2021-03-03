class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        lengthM=len(matrix)
        #res=matrix.copy()
        res=[]
        for i in range(0,lengthM):
            temp=[]
            for j in range(0,lengthM):
                temp.append(matrix[lengthM-1-j][i])
                
            res.append(temp)
        
        for i in range(0,lengthM):
            for j in range(0,lengthM):
                matrix[i][j]=res[i][j]
