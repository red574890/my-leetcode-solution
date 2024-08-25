class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        path = set()


        def DFS(r,c,i):
            if(i == len(word)):
                return True
            
            if(r < 0 or c< 0 or r>=rows or c >= cols  or (r,c) in path):
                return False
            if(word[i]!= board[r][c]):
                return False


            path.add((r,c))

            res = (DFS(r+1,c,i+1) or DFS(r-1,c,i+1) or DFS(r,c+1,i+1) or DFS(r,c-1, i+1))
            path.remove((r,c))
            return res
        
        for r in range(rows):
            for c in range(cols):
                if(DFS(r,c,0)):
                    return True
        
        return False
       
