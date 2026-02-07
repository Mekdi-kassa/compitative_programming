# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def check(temp,max1,min1):
            if not temp:
                return True
            
            if not(min1<temp.val<max1):
                return False

            return check(temp.left,temp.val,min1) and check(temp.right,max1,temp.val)
        
        return check(root,float('inf'),float('-inf'))