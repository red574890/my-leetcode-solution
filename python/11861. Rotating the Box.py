class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:

        # 1 reshape the data
        new = []
        for j in range(len(boxGrid[0])):
            tmp = []
            for i in range(len(boxGrid)-1,-1,-1):
                tmp.append(boxGrid[i][j])
            new.append(tmp)


        for line in range(len(new[0])):
            n = len(new)-1
            while(n>=0):
                if(new[n][line]=='.'):
                    n-=1
                elif(new[n][line]=='*'):
                    n-=1
                else:
                    if(n+1 <= len(new)-1):
                        if(new[n+1][line] == '.'):
                            new[n][line] = '.'
                            new[n+1][line] = '#'
                            n+=1
                        else:
                            n-=1
                    else:
                        n-=1
        return new
