# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        strs = ""
        while head.next != None:
            val = head.val            
            strs += str(val)
            head = head.next
        val = head.val
        strs += str(val)
        return int(strs,2)