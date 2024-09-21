class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # create box list
        box_list = {0: [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]], 1: [[0, 3], [0, 4], [0, 5], [1, 3], [1, 4], [1, 5], [2, 3], [2, 4], [2, 5]], 2: [[0, 6], [0, 7], [0, 8], [1, 6], [1, 7], [1, 8], [2, 6], [2, 7], [2, 8]], 3: [[3, 0], [3, 1], [3, 2], [4, 0], [4, 1], [4, 2], [5, 0], [5, 1], [5, 2]], 4: [[3, 3], [3, 4], [3, 5], [4, 3], [4, 4], [4, 5], [5, 3], [5, 4], [5, 5]], 5: [[3, 6], [3, 7], [3, 8], [4, 6], [4, 7], [4, 8], [5, 6], [5, 7], [5, 8]], 6: [[6, 0], [6, 1], [6, 2], [7, 0], [7, 1], [7, 2], [8, 0], [8, 1], [8, 2]], 7: [[6, 3], [6, 4], [6, 5], [7, 3], [7, 4], [7, 5], [8, 3], [8, 4], [8, 5]], 8: [[6, 6], [6, 7], [6, 8], [7, 6], [7, 7], [7, 8], [8, 6], [8, 7], [8, 8]]}
        


              # check row re
        for i in range(9):
            tmp = list(board[i])
            tmp = [x for x in tmp if x != '.']
  
            if(len(set(tmp)) < len(tmp) ):
                return False

            tmp2 = []
            for j in range(9):
                
                if(board[j][i] != '.'):
                    tmp2.append(board[j][i])

    
            if(len(set(tmp2)) < len(tmp2) ):
                return False

            box = box_list[i]
            tmp3 = []
            for z in range(len(box)):
                if(board[box[z][0]][box[z][1]] != '.'):
                    tmp3.append(board[box[z][0]][box[z][1]])
            if(len(set(tmp3)) < len(tmp3) ):
                return False
        
        return True
     
