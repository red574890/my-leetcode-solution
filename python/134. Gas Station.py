class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
       

        if(sum(gas)<sum(cost)):
            return -1
        n = len(gas)

        
  
        for v in range(0,n):

            i = v     
            if(i+1 < n and i>0):
                if(gas[i] - cost[i]<=0 and cost[i+1]>=0):
                    continue
                elif(gas[i] == gas[i+1] and gas[i-1] == gas[i] and cost[i-1] == cost[i] and cost[i] == cost[i+1]):
                    continue
            else:
                if(gas[i] - cost[i]<0):
                    continue

            total_gas = gas[i]

            for j in range(0,n):
                a = i+1+j
                pre_a = i+j
                if(a>=n):
                    a -= n
                if(pre_a >= n):
                    pre_a -= n

                if(a == i):
                    continue
                else:
                    total_gas -= cost[pre_a]
                    if(total_gas < 0 ):
                        break

                    total_gas += gas[a]
                    
                if(total_gas < 0):
                    break

        
            if(total_gas - cost[pre_a] >= 0):
                return i
                
        return -1
