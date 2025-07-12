class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:

        if(desiredTotal > (1+maxChoosableInteger) *maxChoosableInteger / 2 ):
            return False

        memo = {}
        def canwin(target,maxNum,used,currentotal):
            key = tuple(used)

            if key in memo:
                return memo[key]

            for i in range(1,maxNum+1):

                if(used[i-1]== False):
                    used[i-1] = True

                    if(currentotal+i >= target):
                        memo[key] = True
                        used[i - 1] = False  # Backtrack
                        return True

                    
                    oppoentcanwin = canwin(target,maxNum,used,currentotal+i)

                    if(oppoentcanwin == False):
                        memo[key] = True
                        used[i-1] = False
                        return True

                    used[i-1] = False
                

                    

            memo[key] = False
            return False
 
        used_list = [False] * maxChoosableInteger

        return canwin(desiredTotal,maxChoosableInteger,used_list,0)



        




        
