class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:

        n = 0
        comp_list = set()
        res = []
        while(n<=len(s)-10):
            if(s[n:n+10] in comp_list):
                if(s[n:n+10] not in res):
                    res.append(s[n:n+10])             
            else:
                comp_list.add(s[n:n+10])

            n+=1

        return res
