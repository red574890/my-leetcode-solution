class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """     
        M=len(matrix)
        out_in=int(M/2)
        layer_in=0
        row=0
        col=0
        move=M-1
        n=0
        
        while(layer_in<out_in):
            row=layer_in
            col=layer_in
            n=0
            for i in range(0,M-1):
                j=0
                while(j<4):
                    if(j==0):
                        temp1=matrix[row][col]
                    if(j==0):
                        row+=n
                        col+=(move-n)
                    elif(j==1):
                        row+=(move-n)
                        col-=n
                    elif(j==2):
                        row-=n
                        col-=(move-n)
                    elif(j==3):
                        row-=(move-n)
                        col+=n   
                    temp2=matrix[row][col]
                    matrix[row][col]=temp1
                    temp1=temp2
                    j+=1

                
                n+=1
                row=layer_in
                col=layer_in+n
            M-=2
            layer_in+=1
            move-=2
        
                    
                    
                    
                
        
        
