# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if(root == None):
            return 0
        
        
        queue = [root]
        
        depth = 0
        while(len(queue) > 0):
            depth+=1
            
            current_tier = len(queue)
            
            for i in range(0,current_tier):
                cur = queue.pop(0)

                if(cur.left!=None):
                    queue.append(cur.left)
                    
                if(cur.right!=None):
                    queue.append(cur.right)
      
        return(depth)
