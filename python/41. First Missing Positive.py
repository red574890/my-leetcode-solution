class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n=1
        visited=set([1])

        experience_n=set()
        for i in nums:
            if(i in experience_n):
                continue
            
            experience_n.add(i)
            
            if(i<=0):
                continue
            if(i not in visited):
                visited.add(i)
            else:
                loop=True
                while(loop):
                    n+=1
                    if(n not in visited):
                        loop=False
                        break
                visited.add(n)
                    
        return n
                
