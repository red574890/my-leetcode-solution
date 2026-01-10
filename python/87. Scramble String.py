class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        memo = {}
        def DFS(s1,s2):
            if sorted(s1) != sorted(s2):
                memo[(s1, s2)] = False
                return False
            if((s1,s2) in memo):
                return memo[(s1,s2)]
            if(s1==s2):
                return True
            for i in range(1,len(s1)):
                al = s1[:i]
                ar = s1[i:]

                # no swap
                if(DFS(al,s2[:i]) and DFS(ar,s2[i:])):
                    memo[(s1,s2)] = True
                    return True
                
                # swap
                if(DFS(al,s2[len(s1)-len(al):]) and DFS(ar,s2[:len(ar)])):
                    memo[(s1,s2)] = True
                    return True
            memo[(s1,s2)] = False
            return False

        return DFS(s1,s2)
