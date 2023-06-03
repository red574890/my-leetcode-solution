class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
         
        if(n==1):
            return [['Q']]


        def fill(place,n,tier,res):
            if(tier == n):
                return

            for i in range(n):
                new_place = place.copy()

                if(i in place):
                    continue
                else:
                    d_line = False
                    for z in range(0,len(place)):
                        if(abs((tier)- z) == abs(i- place[z])):
                            d_line = True
                            break   
                            
                    if(d_line):
                        continue
                    else:
                        new_place.append(i)
                        if(tier == n-1 and len(new_place) == n and new_place not in res):
                            res.append(new_place)
                        
                        fill(new_place,n,tier+1,res)


        tier = 0
        res = []
        for i in range(0,n):
            tier = 1
            place = [i]
            fill(place,n,tier,res)


        board = []
        
        for i in range(n):
            board.append(n*".")
        

        final = []


        for i in range(0,len(res)):
            n_board = board.copy()
            for col in range(0,n):
                tmp = n_board[col]
                tmp = tmp[:res[i][col]]+'Q'+tmp[res[i][col]+1:]
                n_board[col] = tmp

            final.append(n_board)

        return final
