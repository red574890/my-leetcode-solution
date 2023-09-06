class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        memo = []
        for i in range(len(coins)):
            memo.append([])
        print(memo)
        for tier in range(len(coins)):

            for i in range(amount+1):

                if(i==0):
                    memo[tier].append(1)
                else:
                    if(i-coins[tier] < 0 and tier ==0):
                        memo[tier].append(0)
                    elif(i-coins[tier] < 0 and tier > 0):
                        memo[tier].append(memo[tier-1][i])
                    elif(tier == 0):
                        this_tier = memo[tier][i-coins[tier]]
                        memo[tier].append(this_tier)

                    else:
                        up_tier = memo[tier-1][i]
                        this_tier = memo[tier][i-coins[tier]]
                        memo[tier].append(up_tier+this_tier)

        return memo[tier][amount]
