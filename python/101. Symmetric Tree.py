# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        
        # check all point of node_left using the concept of BFS
        
        queue = [root.left]
        visit = []
        
        while (len(queue)>0):
            node = queue.pop(0)
            if(node == None):
                visit.append(None)
                continue
            visit.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        
        
        queue = [root.right]
        visit1 = []
        
        while (len(queue)>0):
            node = queue.pop(0)
            if(node == None):
                visit1.append(None)
                continue
            visit1.append(node.val)
            
            queue.append(node.right)
                
            queue.append(node.left)
        
        print(visit)
        print(visit1)
        
        return visit1 == visit
            
            
            
        
        
        
