class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack=[]
        poped=float('-inf')
        for i in range(len(nums)-1,-1,-1):
            if nums[i] < poped:
                return True
            while stack and stack[-1] < nums[i]:
                poped=stack.pop()
     
            stack.append(nums[i])
        return False