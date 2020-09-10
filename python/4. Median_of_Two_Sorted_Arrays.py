class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        num3=sorted(nums1+nums2)
        n=len(num3)
        res=0
        
        if(n%2==0):
                 res=(num3[int(n/2)-1]+num3[int(n/2)])
                 res=res*0.5
        else:
                 res=num3[int(round(n/2))]
        
        
        return res
        
        
        
