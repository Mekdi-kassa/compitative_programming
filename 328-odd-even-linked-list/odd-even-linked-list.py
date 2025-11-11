# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        i=0
        dummy_node=ListNode()
        dummy_node2=ListNode()
        cur2=dummy_node2
        cur1=dummy_node
        cur=head
        while cur:
            if i%2==0:
                temp=cur
                cur=cur.next
                temp.next=None
                cur1.next=temp
                cur1=cur1.next
            else:
                temp=cur
                cur=cur.next
                temp.next=None
                cur2.next=temp
                cur2=cur2.next
            i+=1
        cur1.next=dummy_node2.next
        return dummy_node.next