class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        dictionary = {}
        
        for i in range(len(nums)):

            if(nums[i] in dictionary.keys()):
                dictionary[nums[i]]+=1
                if(dictionary[nums[i]]>len(nums)/2):
                    return nums[i]
            else:
                dictionary[nums[i]] = 1
                if(dictionary[nums[i]]>len(nums)/2):
                    return nums[i]
