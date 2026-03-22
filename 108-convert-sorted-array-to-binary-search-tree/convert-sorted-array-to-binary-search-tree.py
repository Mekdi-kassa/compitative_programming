# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # mid=len(nums)//2
        # def BST(nums):
        #     mid=len(nums)//2
        #     if len(nums)== 0:
        #         return None
            
        #     left=BST(nums[:mid])
        #     right=BST(nums[mid+1:])
        #     return TreeNode(nums[mid],left,right)

       
        # return BST(nums)
        

        #what about using left and right 
        mid=len(nums)//2
        def BST(nums,mid):
            if len(nums)==0:
                return None
            if len(nums)==1:
                root=TreeNode(nums[0])
                return root
                
            root=TreeNode(nums[mid])
            root.left=BST(nums[:mid],len(nums[:mid])//2)
            root.right=BST(nums[mid+1:],len(nums[mid+1:])//2)
            return root
        return BST(nums,mid)