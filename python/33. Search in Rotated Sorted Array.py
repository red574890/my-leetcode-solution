class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(low,mid,high,nums,target):
                found = False          
                if(nums[mid] == target):
                    return mid
                elif(nums[low] == target):
                    return low
                elif(nums[high] == target):
                    return high
                        
                
                while(mid >= low+1 and high >= mid+1):
                    if(nums[mid] == target):
                        found = True
                        break
                    elif(nums[mid]> target):
                        high = mid
                        mid  = int((low+high)/2)
                    elif(nums[mid]< target):
                        low = mid
                        mid  = int((low+high)/2)
                if(found):
                    return mid
                else:
                    return -1


        # find the break point first
        low = 0
        high = len(nums)-1
        mid = int((low+high)/2)

        con = True
        n= 0
        res = -1
        if(nums[mid] == target):
            return mid
        if(nums[high]== target):
            return high
        if(nums[low] == target):
            return low

        while(mid >= low+1 and high >= mid+1):

            if(nums[mid] == target):
                return mid
            if(nums[high]== target):
                return high
            if(nums[low] == target):
                return low
            


            if(nums[mid]>nums[low]):
                if(target >=  nums[low] and target <= nums[mid]):
                    print('1')

                    res = binary_search(low,int((low+mid)/2),mid,nums,target)
                    if(res==-1):
                        low = mid
                        mid = int((low+high)/2)
                    else:
                        break
                else:
                    low = mid
                    mid = int((low+high)/2)

                


            elif(nums[high]>nums[mid]):
                if(target >= nums[mid] and target <= nums[high]):
                    print(2)
                    res = binary_search(mid,int((mid+high)/2),high,nums,target)
                    if(res==-1):
                        high = mid
                        mid = int((low+high)/2)
                    else:
                        break

                else:
                    high = mid
                    mid = int((low+high)/2)

        return res
