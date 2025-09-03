# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q=deque()
        q.append(root)
        i=0
        res=[]
        while q:
            level=[]
            for _ in range(len(q)):
                node=q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            i+=1
            if level and i%2==0:
                res.append(level[::-1])
            elif level and i%2!=0:
                res.append(level)
        return res