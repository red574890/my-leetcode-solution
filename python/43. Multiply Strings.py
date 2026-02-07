class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        num_map = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}

        def converter(s):
            tmp = 1
            res = 0
            for i in range(0,len(s)): 
                res+=num_map[s[len(s)-i-1]]*tmp
