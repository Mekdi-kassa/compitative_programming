# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        str1=""
        str2=""
        dummy_node=ListNode()
        cur=dummy_node
        while l1 :
            str1+=str(l1.val)
            l1=l1.next
        while l2:
            str2+=str(l2.val)
            l2=l2.next
        str1=str1[::-1]
        str2=str2[::-1]
        num=str(int(str1)+int(str2))[::-1]
        i=0
        while i<len(num):
            cur.next=ListNode(int(num[i]))
            cur=cur.next
            i+=1
        return dummy_node.next
    
        