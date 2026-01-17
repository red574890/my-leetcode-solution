class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        nums = sorted(nums)
        min_diff = 100000
        for i in range(len(nums)-2):

            l = i+1
            r = len(nums)-1
            while(l<r):
                curr_sum = nums[i] + nums[l] + nums[r]
                diff = abs(curr_sum - target)

                if diff < min_diff:
                    min_diff = diff
                    best_sum = curr_sum

                if curr_sum < target:
                    l += 1
                elif curr_sum > target:
                    r -= 1
                else:
                    return curr_sum
            
        return best_sum


        
        
