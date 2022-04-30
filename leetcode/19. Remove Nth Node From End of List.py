# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        len = 0
        temp = head
        while temp:
            temp = temp.next
            len+=1
        if len ==n:
            head = head.next
            return head
            
        temp = head
        for i in range(len - n-1):
            temp = temp.next

        temp1 = temp.next
        if temp1 :
            temp.next = temp1.next
        else:
            temp.next = None
        return head