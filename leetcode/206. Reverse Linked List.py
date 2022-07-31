# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        while True:
            nxt = None
            nextnext = None
            if temp.next:
                nxt = temp.next
                nextnext = nxt.next
            if nextnext ==None:
                
            


            
