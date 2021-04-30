class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # find the one that have only value and fill it first
        # guess the one that have two value
        
        def find_empty(board):
            for i in range(len(board)):
                for j in range(len(board)):
                    if(board[i][j]=="."):
                        return i,j
            return None
                           
        def valid(board,num,pos):
            for i in range(len(board)):
                if(board[pos[0]][i] == str(num) and i!=pos[1]):
                    return False
                
            for i in range(len(board)):
                if(board[i][pos[1]] == str(num) and i!=pos[0]):
                    return False
            
            #Check box
            box_x=pos[1]//3
            box_y=pos[0]//3
            for i in range(box_y *3,box_y*3+3):
                for j in range(box_x*3,box_x*3+3):
                    if(board[i][j]==str(num) and (i,j)!=pos):
                        return False
            return True
        
        def solve(board):
            find = find_empty(board)
            if(find == None):
                return True
            else:
                x,y=find

                
            for i in range(1,10):
                if valid(board,i,(x,y)):
                    board[x][y] = str(i)
                   
                   
                    if solve(board):
                        return True
                    
                    board[x][y]="."
            return False
        solve(board)
