# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        cur=head
        arr=set()
        arr.add(cur.val)
        while cur and cur.next : 
            if cur.next.val in arr:
                cur.next=cur.next.next
            else:
                arr.add(cur.next.val)
                cur=cur.next  
        return head