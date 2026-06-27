class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        if(len(s1)+len(s2) != len(s3)):
            return False
        
        if(s1+s2 == s3 or s2+s1 == s3):
            return True


        n_1 = 0
        n_2 = 0
        n_3 = 0
        visited = {}

        def match(n_1,n_2,n_3):
            if(n_1 >= len(s1)):
                if((n_1,n_2) not in visited.keys()):
                    visited[(n_1,n_2)] = s3[n_3:]== s2[n_2:]
                return s3[n_3:]== s2[n_2:]
            if(n_2 >= len(s2)):
                if((n_1,n_2) not in visited.keys()):
                    visited[(n_1,n_2)] = s3[n_3:]== s1[n_1:]
                return s3[n_3:]== s1[n_1:]

            if((n_1,n_2) in visited.keys()):
                return visited[(n_1,n_2)]

            
            if(s3[n_3] == s1[n_1] and s3[n_3] != s2[n_2]):
                visited[(n_1+1,n_2)] = match(n_1+1,n_2,n_3+1)
                return match(n_1+1,n_2,n_3+1)

            elif(s3[n_3] == s2[n_2] and s3[n_3] != s1[n_1]):
                visited[(n_1,n_2+1)] = match(n_1,n_2+1,n_3+1)
                return match(n_1,n_2+1,n_3+1)

            elif(s3[n_3] != s2[n_2] and s3[n_3] != s1[n_1]):
                visited[(n_1,n_2)] = False
                return False
            else:
                
                if (n_1+1, n_2) in visited:
                    ans1 = visited[(n_1+1, n_2)]
                else:
                    ans1 = match(n_1+1, n_2, n_3+1)
                    visited[(n_1+1, n_2)] = ans1
                
                # 2. Evaluate or fetch the second path (s2)
                if (n_1, n_2+1) in visited:
                    ans2 = visited[(n_1, n_2+1)]
                else:
                    ans2 = match(n_1, n_2+1, n_3+1)
                    visited[(n_1, n_2+1)] = ans2

                # 3. Memoize the current state and return the combined result
                visited[(n_1, n_2)] = ans1 | ans2
            
            return visited[(n_1, n_2)]

        return match(n_1,n_2,n_3)
