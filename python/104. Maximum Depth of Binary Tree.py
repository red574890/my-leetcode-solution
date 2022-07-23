# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        
        
        depth_list = set()
        
        
        def check_depth(point,n):
                
            if(point.left is None and point.right is None):
                depth_list.add(n)
                return depth_list
                
            elif(point.left is not None and point.right is None):
                check_depth(point.left,n+1)
            
            elif(point.left is None and point.right is not None):
                check_depth(point.right,n+1)
            
            else:
                check_depth(point.left,n+1)
                check_depth(point.right,n+1)


            return depth_list
        
        if(root is None):
            return(0)
       
        res = max(check_depth(root,1))
        
        return(res)
