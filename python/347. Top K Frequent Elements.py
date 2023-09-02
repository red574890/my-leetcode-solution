class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        tmp = {}

        for i in nums:
            if(i not in tmp.keys()):
                tmp[i] = 1

            else:
                tmp[i]+=1

        print(tmp)

        tmp = sorted(tmp.items(), key=lambda x:x[1], reverse=True)

        res = []
        for i in range(k):
            res.append(tmp[i][0])


        return res
