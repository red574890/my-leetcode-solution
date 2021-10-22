# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        #top == 1 -> left == 2 -> right, ==0 root
        res=0
        def travel(root,top,res):
            
            if(root==None):
                return 0
            
            if(top==1 and root.left==None and root.right==None):
                return root.val
            if(root.left!=None or root.right!=None):
                res=travel(root.left,1,res)+travel(root.right,2,res)
         
            return res
            
            
            
                
        res=travel(root,0,0)
        
        return res
        
