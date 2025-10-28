# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        que = deque()
        que.append(root)
        ans = []
        while que:
            qlen = len(que)
            level = []
            for _ in range(qlen):
                node = que.popleft()
                if node:
                    level.append(node.val)
                    que.append(node.left)
                    que.append(node.right)
            if level:
                ans.append(level)
        return ans