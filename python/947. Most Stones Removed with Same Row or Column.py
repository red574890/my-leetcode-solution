class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:

      
        # create union for each 
        
        if(len(stones) == 0):
            return 0
        
        main_stack = list(range(0,len(stones)))
        
        res = 0
        while(len(main_stack)>0):

            root = main_stack[0]
            stack = [root]
            visited = set()
            while(len(stack)!=0):
                target = stack.pop()
                visited.add(target)
                for i in range(len(stones)):

                    if(i in visited):
                        continue
                    else:
                        if(stones[i][0] == stones[target][0] or stones[i][1] == stones[target][1]):
                            stack.append(i)
                            
            res+= len(visited)-1
            
            main_stack = list(set(main_stack) ^ visited)
            

        return res
            
